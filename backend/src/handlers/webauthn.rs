//! WebAuthn / Passkey Handlers (Item #39)

use axum::{
    extract::State,
    http::{header, HeaderMap, StatusCode},
    response::IntoResponse,
    Json,
};
use chrono::{Duration, Utc};
use sqlx::{PgPool, Row};
use uuid::Uuid;
use webauthn_rs::prelude::*;

use crate::audit::record_audit_event;
use crate::auth::{self, AuthUser};
use crate::error::ApiError;
use crate::models::{
    AuthResponse, PasskeyLoginFinishRequest, PasskeyLoginStartRequest,
    PasskeyLoginStartResponse, PasskeyRegisterFinishRequest, PasskeyRegisterStartResponse,
    UserProfile,
};
use crate::webauthn::WebAuthnService;

#[derive(Clone)]
pub struct WebAuthnState {
    pub pool: PgPool,
    pub webauthn: WebAuthnService,
}

/// POST /api/auth/webauthn/register/start
#[utoipa::path(
    post,
    path = "/api/auth/webauthn/register/start",
    responses(
        (status = 200, description = "Passkey registration challenge generated", body = PasskeyRegisterStartResponse),
        (status = 401, description = "Unauthorized")
    ),
    tag = "Authentication"
)]
pub async fn register_start(
    State(state): State<WebAuthnState>,
    user: AuthUser,
) -> Result<Json<PasskeyRegisterStartResponse>, ApiError> {
    let user_uuid = Uuid::parse_str(&user.id)
        .map_err(|_| ApiError::bad_request("Invalid user id"))?;

    let (challenge_response, reg_state) = state
        .webauthn
        .start_registration(user_uuid, &user.email, &user.email, None)
        .map_err(|e| ApiError::internal_msg("Failed to initiate WebAuthn registration", e))?;

    let challenge_id = Uuid::new_v4();
    let reg_json = serde_json::to_string(&reg_state)
        .map_err(|e| ApiError::internal_msg("Failed to serialize challenge state", e.to_string()))?;

    let expires_at = Utc::now() + Duration::minutes(5);

    sqlx::query(
        r#"
        INSERT INTO webauthn_challenges (id, challenge, user_id, challenge_type, expires_at)
        VALUES ($1, $2, $3, 'registration', $4)
        "#,
    )
    .bind(challenge_id)
    .bind(&reg_json)
    .bind(user_uuid)
    .bind(expires_at)
    .execute(&state.pool)
    .await
    .map_err(|e| ApiError::internal_msg("Database error saving challenge", e.to_string()))?;

    let creation_options_json = serde_json::to_value(&challenge_response)
        .map_err(|e| ApiError::internal_msg("Failed to serialize creation options", e.to_string()))?;

    Ok(Json(PasskeyRegisterStartResponse {
        challenge_id: challenge_id.to_string(),
        public_key_credential_creation_options: creation_options_json,
    }))
}

/// POST /api/auth/webauthn/register/finish
#[utoipa::path(
    post,
    path = "/api/auth/webauthn/register/finish",
    request_body = PasskeyRegisterFinishRequest,
    responses(
        (status = 200, description = "Passkey credential registered successfully"),
        (status = 400, description = "Verification failed"),
        (status = 401, description = "Unauthorized")
    ),
    tag = "Authentication"
)]
pub async fn register_finish(
    State(state): State<WebAuthnState>,
    user: AuthUser,
    Json(payload): Json<PasskeyRegisterFinishRequest>,
) -> Result<StatusCode, ApiError> {
    let user_uuid = Uuid::parse_str(&user.id)
        .map_err(|_| ApiError::bad_request("Invalid user id"))?;

    let challenge_uuid = Uuid::parse_str(&payload.challenge_id)
        .map_err(|_| ApiError::bad_request("Invalid challenge_id format"))?;

    let row = sqlx::query(
        r#"
        SELECT challenge, expires_at
        FROM webauthn_challenges
        WHERE id = $1 AND user_id = $2 AND challenge_type = 'registration'
        "#,
    )
    .bind(challenge_uuid)
    .bind(user_uuid)
    .fetch_optional(&state.pool)
    .await
    .map_err(|e| ApiError::internal_msg("Database lookup failed", e.to_string()))?
    .ok_or_else(|| ApiError::bad_request("Challenge expired or not found"))?;

    let expires_at: chrono::DateTime<Utc> = row.try_get("expires_at").unwrap_or_else(|_| Utc::now());
    if Utc::now() > expires_at {
        let _ = sqlx::query("DELETE FROM webauthn_challenges WHERE id = $1")
            .bind(challenge_uuid)
            .execute(&state.pool)
            .await;
        return Err(ApiError::bad_request("Challenge has expired. Please retry."));
    }

    let challenge_str: String = row.try_get("challenge").unwrap_or_default();
    let reg_state: PasskeyRegistration = serde_json::from_str(&challenge_str)
        .map_err(|e| ApiError::internal_msg("Malformed challenge state", e.to_string()))?;

    let reg_cred: RegisterPublicKeyCredential = serde_json::from_value(payload.credential)
        .map_err(|e| ApiError::bad_request(format!("Invalid credential format: {}", e)))?;

    let passkey = state
        .webauthn
        .finish_registration(&reg_cred, &reg_state)
        .map_err(|e| ApiError::bad_request(format!("WebAuthn registration verification failed: {}", e)))?;

    let cred_id_str = reg_cred.id.to_string();
    let passkey_bytes = serde_json::to_vec(&passkey)
        .map_err(|e| ApiError::internal_msg("Failed to serialize passkey", e.to_string()))?;

    let nickname = payload.nickname.unwrap_or_else(|| "Hardware Passkey".to_string());

    // Insert passkey credential
    sqlx::query(
        r#"
        INSERT INTO webauthn_credentials (user_id, credential_id, public_key, counter, nickname)
        VALUES ($1, $2, $3, 0, $4)
        ON CONFLICT (credential_id) DO UPDATE SET public_key = EXCLUDED.public_key, counter = 0
        "#,
    )
    .bind(user_uuid)
    .bind(&cred_id_str)
    .bind(&passkey_bytes)
    .bind(&nickname)
    .execute(&state.pool)
    .await
    .map_err(|e| ApiError::internal_msg("Database error saving passkey credential", e.to_string()))?;

    // Cleanup challenge
    let _ = sqlx::query("DELETE FROM webauthn_challenges WHERE id = $1")
        .bind(challenge_uuid)
        .execute(&state.pool)
        .await;

    // Record audit event
    let _ = record_audit_event(
        &state.pool,
        "WEBAUTHN_REGISTERED",
        Some(user_uuid),
        Some(&user.email),
        serde_json::json!({ "credential_id": cred_id_str, "nickname": nickname }),
    )
    .await;

    Ok(StatusCode::OK)
}

/// POST /api/auth/webauthn/login/start
#[utoipa::path(
    post,
    path = "/api/auth/webauthn/login/start",
    request_body = PasskeyLoginStartRequest,
    responses(
        (status = 200, description = "Passkey login challenge generated", body = PasskeyLoginStartResponse)
    ),
    tag = "Authentication"
)]
pub async fn login_start(
    State(state): State<WebAuthnState>,
    Json(payload): Json<PasskeyLoginStartRequest>,
) -> Result<Json<PasskeyLoginStartResponse>, ApiError> {
    let mut allow_credentials = Vec::new();
    let mut resolved_user_id = None;

    if let Some(ref email) = payload.email {
        let user_row = sqlx::query("SELECT id FROM users WHERE LOWER(email) = LOWER($1)")
            .bind(email.trim())
            .fetch_optional(&state.pool)
            .await
            .map_err(|e| ApiError::internal_msg("Database lookup error", e.to_string()))?;

        if let Some(row) = user_row {
            let u_id: Uuid = row.try_get("id").unwrap_or_default();
            resolved_user_id = Some(u_id);

            let cred_rows = sqlx::query("SELECT public_key FROM webauthn_credentials WHERE user_id = $1")
                .bind(u_id)
                .fetch_all(&state.pool)
                .await
                .unwrap_or_default();

            for crow in cred_rows {
                if let Ok(bytes) = crow.try_get::<Vec<u8>, _>("public_key") {
                    if let Ok(passkey) = serde_json::from_slice::<Passkey>(&bytes) {
                        allow_credentials.push(passkey);
                    }
                }
            }
        }
    }

    let (req_challenge, auth_state) = state
        .webauthn
        .start_authentication(&allow_credentials)
        .map_err(|e| ApiError::internal_msg("Failed to initiate WebAuthn authentication", e))?;

    let challenge_id = Uuid::new_v4();
    let auth_state_json = serde_json::to_string(&auth_state)
        .map_err(|e| ApiError::internal_msg("Failed to serialize auth state", e.to_string()))?;

    let expires_at = Utc::now() + Duration::minutes(5);

    sqlx::query(
        r#"
        INSERT INTO webauthn_challenges (id, challenge, user_id, challenge_type, expires_at)
        VALUES ($1, $2, $3, 'authentication', $4)
        "#,
    )
    .bind(challenge_id)
    .bind(&auth_state_json)
    .bind(resolved_user_id)
    .bind(expires_at)
    .execute(&state.pool)
    .await
    .map_err(|e| ApiError::internal_msg("Database error saving challenge", e.to_string()))?;

    let request_options_json = serde_json::to_value(&req_challenge)
        .map_err(|e| ApiError::internal_msg("Failed to serialize request options", e.to_string()))?;

    Ok(Json(PasskeyLoginStartResponse {
        challenge_id: challenge_id.to_string(),
        public_key_credential_request_options: request_options_json,
    }))
}

/// POST /api/auth/webauthn/login/finish
#[utoipa::path(
    post,
    path = "/api/auth/webauthn/login/finish",
    request_body = PasskeyLoginFinishRequest,
    responses(
        (status = 200, description = "Passkey authentication successful", body = AuthResponse),
        (status = 401, description = "Authentication failed")
    ),
    tag = "Authentication"
)]
pub async fn login_finish(
    State(state): State<WebAuthnState>,
    headers: HeaderMap,
    Json(payload): Json<PasskeyLoginFinishRequest>,
) -> Result<impl IntoResponse, ApiError> {
    let challenge_uuid = Uuid::parse_str(&payload.challenge_id)
        .map_err(|_| ApiError::bad_request("Invalid challenge_id format"))?;

    let row = sqlx::query(
        r#"
        SELECT challenge, expires_at
        FROM webauthn_challenges
        WHERE id = $1 AND challenge_type = 'authentication'
        "#,
    )
    .bind(challenge_uuid)
    .fetch_optional(&state.pool)
    .await
    .map_err(|e| ApiError::internal_msg("Database lookup failed", e.to_string()))?
    .ok_or_else(|| ApiError::unauthorized("Challenge expired or not found"))?;

    let expires_at: chrono::DateTime<Utc> = row.try_get("expires_at").unwrap_or_else(|_| Utc::now());
    if Utc::now() > expires_at {
        let _ = sqlx::query("DELETE FROM webauthn_challenges WHERE id = $1")
            .bind(challenge_uuid)
            .execute(&state.pool)
            .await;
        return Err(ApiError::unauthorized("Challenge has expired. Please retry."));
    }

    let challenge_str: String = row.try_get("challenge").unwrap_or_default();
    let auth_state: PasskeyAuthentication = serde_json::from_str(&challenge_str)
        .map_err(|e| ApiError::internal_msg("Malformed auth state", e.to_string()))?;

    let cred: PublicKeyCredential = serde_json::from_value(payload.credential)
        .map_err(|e| ApiError::bad_request(format!("Invalid credential format: {}", e)))?;

    let cred_id_str = cred.id.to_string();

    // Look up saved credential
    let cred_row = sqlx::query(
        r#"
        SELECT c.user_id, c.public_key, c.counter, u.email, u.full_name, u.role
        FROM webauthn_credentials c
        JOIN users u ON c.user_id = u.id
        WHERE c.credential_id = $1
        "#,
    )
    .bind(&cred_id_str)
    .fetch_optional(&state.pool)
    .await
    .map_err(|e| ApiError::internal_msg("Database error", e.to_string()))?
    .ok_or_else(|| ApiError::unauthorized("Credential not found on this server"))?;

    let user_id: Uuid = cred_row.try_get("user_id").unwrap_or_default();
    let public_key_bytes: Vec<u8> = cred_row.try_get("public_key").unwrap_or_default();
    let user_email: String = cred_row.try_get("email").unwrap_or_default();
    let full_name: Option<String> = cred_row.try_get("full_name").ok();
    let role: String = cred_row.try_get("role").unwrap_or_else(|_| "user".to_string());

    let mut passkey: Passkey = serde_json::from_slice(&public_key_bytes)
        .map_err(|e| ApiError::internal_msg("Corrupted credential data in database", e.to_string()))?;

    let auth_result = state
        .webauthn
        .finish_authentication(&cred, &auth_state)
        .map_err(|e| ApiError::unauthorized(format!("Passkey signature verification failed: {}", e)))?;

    // Update credential counter & last used timestamp
    passkey.update_credential(&auth_result);
    let updated_bytes = serde_json::to_vec(&passkey).unwrap_or(public_key_bytes);

    let _ = sqlx::query(
        r#"
        UPDATE webauthn_credentials
        SET counter = counter + 1, last_used_at = CURRENT_TIMESTAMP, public_key = $1
        WHERE credential_id = $2
        "#,
    )
    .bind(&updated_bytes)
    .bind(&cred_id_str)
    .execute(&state.pool)
    .await;

    // Delete used challenge
    let _ = sqlx::query("DELETE FROM webauthn_challenges WHERE id = $1")
        .bind(challenge_uuid)
        .execute(&state.pool)
        .await;

    // Issue JWT access token
    let access_token = auth::issue_access_token(&user_id.to_string(), &user_email, &role)?;

    // Issue refresh token
    let raw_refresh = auth::generate_refresh_token();
    let refresh_hash = auth::hash_refresh_token(&raw_refresh);
    let cfg = auth::config();
    let refresh_expires = Utc::now() + Duration::seconds(cfg.refresh_ttl_secs);

    let _ = sqlx::query(
        r#"
        INSERT INTO refresh_tokens (user_id, token_hash, expires_at)
        VALUES ($1, $2, $3)
        "#,
    )
    .bind(user_id)
    .bind(&refresh_hash)
    .bind(refresh_expires)
    .execute(&state.pool)
    .await;

    // Record audit event
    let _ = record_audit_event(
        &state.pool,
        "WEBAUTHN_LOGIN_SUCCESS",
        Some(user_id),
        Some(&user_email),
        serde_json::json!({ "credential_id": cred_id_str }),
    )
    .await;

    let cookie_header = auth::refresh_cookie(&raw_refresh, &headers);
    let mut response_headers = HeaderMap::new();
    response_headers.insert(header::SET_COOKIE, cookie_header);

    let auth_resp = AuthResponse {
        access_token,
        token_type: "Bearer".to_string(),
        expires_in: cfg.access_ttl_secs,
        user: UserProfile {
            id: user_id.to_string(),
            email: user_email,
            full_name,
            role,
            created_at: Utc::now(),
        },
    };

    Ok((response_headers, Json(auth_resp)))
}
