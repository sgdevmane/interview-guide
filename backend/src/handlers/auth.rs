use std::sync::OnceLock;

use axum::{
    http::{header, HeaderMap, StatusCode},
    response::{IntoResponse, Response},
    Json,
};
use chrono::{DateTime, Duration, Utc};
use sqlx::{PgPool, Row};

use crate::auth::{self, AuthUser, REFRESH_COOKIE};
use crate::error::ApiError;
use crate::models::{AuthResponse, LoginRequest, RegisterRequest, UserProfile};

const BCRYPT_COST: u32 = 12;
/// bcrypt only uses the first 72 bytes; reject longer input instead of silently truncating.
const MAX_PASSWORD_BYTES: usize = 72;
const MIN_PASSWORD_CHARS: usize = 8;

fn pool() -> Result<&'static PgPool, ApiError> {
    crate::db::get_global_pool().ok_or_else(|| {
        ApiError::ServiceUnavailable("Accounts are unavailable: database not configured".to_string())
    })
}

fn normalize_email(raw: &str) -> Result<String, ApiError> {
    let email = raw.trim().to_lowercase();
    let valid = (3..=255).contains(&email.len())
        && !email.chars().any(char::is_whitespace)
        && matches!(email.split_once('@'), Some((local, domain))
            if !local.is_empty() && domain.contains('.') && !domain.starts_with('.')
                && !domain.ends_with('.') && !domain.contains('@'));
    if valid {
        Ok(email)
    } else {
        Err(ApiError::BadRequest("Please enter a valid email address".to_string()))
    }
}

fn validate_password(password: &str) -> Result<(), ApiError> {
    if password.chars().count() < MIN_PASSWORD_CHARS {
        return Err(ApiError::BadRequest(format!(
            "Password must be at least {MIN_PASSWORD_CHARS} characters"
        )));
    }
    if password.len() > MAX_PASSWORD_BYTES {
        return Err(ApiError::BadRequest(format!(
            "Password must be at most {MAX_PASSWORD_BYTES} bytes"
        )));
    }
    Ok(())
}

fn validate_full_name(raw: &str) -> Result<String, ApiError> {
    let name = raw.trim().to_string();
    if name.is_empty() || name.chars().count() > 128 || name.chars().any(char::is_control) {
        return Err(ApiError::BadRequest("Full name must be 1-128 characters".to_string()));
    }
    Ok(name)
}

/// Hash used when the email does not exist, so response timing does not reveal account existence.
fn dummy_hash() -> &'static str {
    static DUMMY: OnceLock<String> = OnceLock::new();
    DUMMY.get_or_init(|| {
        bcrypt::hash("timing-equalisation-placeholder", BCRYPT_COST).unwrap_or_default()
    })
}

async fn hash_password(password: String) -> Result<String, ApiError> {
    tokio::task::spawn_blocking(move || bcrypt::hash(password, BCRYPT_COST))
        .await
        .map_err(|e| ApiError::Internal(format!("hash task failed: {e}")))?
        .map_err(|e| ApiError::Internal(format!("bcrypt hash failed: {e}")))
}

async fn verify_password(password: String, hash: String) -> Result<bool, ApiError> {
    tokio::task::spawn_blocking(move || bcrypt::verify(password, &hash).unwrap_or(false))
        .await
        .map_err(|e| ApiError::Internal(format!("verify task failed: {e}")))
}

fn user_agent(headers: &HeaderMap) -> Option<String> {
    headers
        .get(header::USER_AGENT)
        .and_then(|v| v.to_str().ok())
        .map(|ua| ua.chars().take(255).collect())
}

/// Persist a fresh refresh token and mint an access token for `user`.
async fn start_session(
    pool: &PgPool,
    headers: &HeaderMap,
    user: UserProfile,
    status: StatusCode,
) -> Result<Response, ApiError> {
    let cfg = auth::config();
    let refresh = auth::generate_refresh_token();
    let expires_at = Utc::now() + Duration::seconds(cfg.refresh_ttl_secs);

    sqlx::query(
        "INSERT INTO refresh_tokens (user_id, token_hash, user_agent, expires_at) \
         VALUES ($1::uuid, $2, $3, $4)",
    )
    .bind(&user.id)
    .bind(auth::hash_refresh_token(&refresh))
    .bind(user_agent(headers))
    .bind(expires_at)
    .execute(pool)
    .await?;

    let access_token = auth::issue_access_token(&user.id, &user.email, &user.role)?;
    let body = AuthResponse {
        access_token,
        token_type: "Bearer".to_string(),
        expires_in: cfg.access_ttl_secs,
        user,
    };
    Ok((
        status,
        [
            (header::SET_COOKIE, auth::refresh_cookie(&refresh, headers)),
            (header::CACHE_CONTROL, "no-store".parse().expect("static header")),
        ],
        Json(body),
    )
        .into_response())
}

fn profile_from_row(row: &sqlx::postgres::PgRow) -> UserProfile {
    UserProfile {
        id: row.get("id"),
        email: row.get("email"),
        full_name: row.get("full_name"),
        role: row.get::<Option<String>, _>("role").unwrap_or_else(|| "user".to_string()),
        created_at: row.get::<Option<DateTime<Utc>>, _>("created_at").unwrap_or_else(Utc::now),
    }
}

fn unauthorized_clearing_cookie(headers: &HeaderMap, message: &str) -> Response {
    let mut res = ApiError::Unauthorized(message.to_string()).into_response();
    res.headers_mut().insert(header::SET_COOKIE, auth::clear_refresh_cookie(headers));
    res
}

/// Create an account and start a session.
#[utoipa::path(
    post,
    path = "/api/auth/register",
    request_body = RegisterRequest,
    responses(
        (status = 201, description = "Account created; refresh cookie set", body = AuthResponse),
        (status = 400, description = "Validation error", body = crate::error::ErrorBody),
        (status = 409, description = "Email already registered", body = crate::error::ErrorBody)
    ),
    tag = "Auth"
)]
pub async fn register(headers: HeaderMap, Json(req): Json<RegisterRequest>) -> Result<Response, ApiError> {
    let pool = pool()?;
    let email = normalize_email(&req.email)?;
    validate_password(&req.password)?;
    let full_name = validate_full_name(&req.full_name)?;
    let password_hash = hash_password(req.password).await?;

    let row = sqlx::query(
        "INSERT INTO users (email, password_hash, full_name, role) VALUES ($1, $2, $3, 'user') \
         RETURNING id::text AS id, email, full_name, role, created_at",
    )
    .bind(&email)
    .bind(&password_hash)
    .bind(&full_name)
    .fetch_one(pool)
    .await
    .map_err(|err| match &err {
        sqlx::Error::Database(db) if db.code().as_deref() == Some("23505") => {
            ApiError::Conflict("An account with this email already exists".to_string())
        }
        _ => ApiError::from(err),
    })?;

    metrics::counter!("auth_registrations_total").increment(1);
    start_session(pool, &headers, profile_from_row(&row), StatusCode::CREATED).await
}

/// Sign in with email and password.
#[utoipa::path(
    post,
    path = "/api/auth/login",
    request_body = LoginRequest,
    responses(
        (status = 200, description = "Signed in; refresh cookie set", body = AuthResponse),
        (status = 401, description = "Invalid credentials", body = crate::error::ErrorBody),
        (status = 403, description = "Account disabled", body = crate::error::ErrorBody),
        (status = 429, description = "Too many failed attempts", body = crate::error::ErrorBody)
    ),
    tag = "Auth"
)]
pub async fn login(headers: HeaderMap, Json(req): Json<LoginRequest>) -> Result<Response, ApiError> {
    let pool = pool()?;
    let email = req.email.trim().to_lowercase();
    auth::check_login_allowed(&email)?;

    let row = sqlx::query(
        "SELECT id::text AS id, email, full_name, role, created_at, password_hash, is_active \
         FROM users WHERE email = $1",
    )
    .bind(&email)
    .fetch_optional(pool)
    .await?;

    let hash = row
        .as_ref()
        .map(|r| r.get::<String, _>("password_hash"))
        .unwrap_or_else(|| dummy_hash().to_string());
    let password_ok = verify_password(req.password, hash).await?;

    let row = match row {
        Some(row) if password_ok => row,
        _ => {
            auth::record_login_failure(&email);
            metrics::counter!("auth_login_failures_total").increment(1);
            return Err(ApiError::Unauthorized("Invalid email or password".to_string()));
        }
    };

    if !row.get::<Option<bool>, _>("is_active").unwrap_or(true) {
        return Err(ApiError::Forbidden("This account has been disabled".to_string()));
    }

    auth::clear_login_failures(&email);
    let profile = profile_from_row(&row);

    // Keep the token table bounded: drop this user's expired / long-revoked tokens.
    sqlx::query(
        "DELETE FROM refresh_tokens WHERE user_id = $1::uuid \
         AND (expires_at < now() OR revoked_at < now() - interval '1 day')",
    )
    .bind(&profile.id)
    .execute(pool)
    .await?;

    metrics::counter!("auth_logins_total").increment(1);
    start_session(pool, &headers, profile, StatusCode::OK).await
}

/// Exchange the HTTP-only refresh cookie for a new access token (rotates the refresh token).
#[utoipa::path(
    post,
    path = "/api/auth/refresh",
    responses(
        (status = 200, description = "New access token; refresh cookie rotated", body = AuthResponse),
        (status = 401, description = "Missing, expired or revoked refresh token", body = crate::error::ErrorBody)
    ),
    tag = "Auth"
)]
pub async fn refresh(headers: HeaderMap) -> Result<Response, ApiError> {
    let pool = pool()?;
    let Some(token) = auth::read_cookie(&headers, REFRESH_COOKIE) else {
        return Ok(unauthorized_clearing_cookie(&headers, "No active session"));
    };

    let row = sqlx::query(
        "SELECT rt.id::text AS token_id, rt.revoked_at, rt.expires_at, \
                u.id::text AS id, u.email, u.full_name, u.role, u.created_at, u.is_active \
         FROM refresh_tokens rt JOIN users u ON u.id = rt.user_id \
         WHERE rt.token_hash = $1",
    )
    .bind(auth::hash_refresh_token(&token))
    .fetch_optional(pool)
    .await?;

    let Some(row) = row else {
        return Ok(unauthorized_clearing_cookie(&headers, "Session expired"));
    };

    let token_id: String = row.get("token_id");
    let user_id: String = row.get("id");

    if let Some(revoked_at) = row.get::<Option<DateTime<Utc>>, _>("revoked_at") {
        // A recently rotated token is expected when two tabs refresh at once.
        // Anything older is a replayed (likely stolen) token: revoke every session for the user.
        if Utc::now() - revoked_at > Duration::seconds(30) {
            tracing::warn!("Refresh token reuse detected for user {}; revoking all sessions", user_id);
            sqlx::query("UPDATE refresh_tokens SET revoked_at = now() WHERE user_id = $1::uuid AND revoked_at IS NULL")
                .bind(&user_id)
                .execute(pool)
                .await?;
            metrics::counter!("auth_refresh_reuse_detected_total").increment(1);
        }
        return Ok(unauthorized_clearing_cookie(&headers, "Session expired"));
    }

    let expires_at: DateTime<Utc> = row.get("expires_at");
    if expires_at <= Utc::now() || !row.get::<Option<bool>, _>("is_active").unwrap_or(true) {
        return Ok(unauthorized_clearing_cookie(&headers, "Session expired"));
    }

    let rotated = sqlx::query("UPDATE refresh_tokens SET revoked_at = now() WHERE id = $1::uuid AND revoked_at IS NULL")
        .bind(&token_id)
        .execute(pool)
        .await?;
    if rotated.rows_affected() != 1 {
        return Ok(unauthorized_clearing_cookie(&headers, "Session expired"));
    }

    start_session(pool, &headers, profile_from_row(&row), StatusCode::OK).await
}

/// Revoke the current refresh token and clear the cookie.
#[utoipa::path(
    post,
    path = "/api/auth/logout",
    responses((status = 204, description = "Signed out")),
    tag = "Auth"
)]
pub async fn logout(headers: HeaderMap) -> Result<Response, ApiError> {
    if let (Some(token), Some(pool)) = (auth::read_cookie(&headers, REFRESH_COOKIE), crate::db::get_global_pool()) {
        sqlx::query("UPDATE refresh_tokens SET revoked_at = now() WHERE token_hash = $1 AND revoked_at IS NULL")
            .bind(auth::hash_refresh_token(&token))
            .execute(pool)
            .await?;
    }
    Ok((
        StatusCode::NO_CONTENT,
        [(header::SET_COOKIE, auth::clear_refresh_cookie(&headers))],
    )
        .into_response())
}

/// Current signed-in user's profile.
#[utoipa::path(
    get,
    path = "/api/auth/me",
    responses(
        (status = 200, description = "Current user", body = UserProfile),
        (status = 401, description = "Not signed in", body = crate::error::ErrorBody)
    ),
    security(("bearer_auth" = [])),
    tag = "Auth"
)]
pub async fn me(user: AuthUser) -> Result<Json<UserProfile>, ApiError> {
    let pool = pool()?;
    let row = sqlx::query(
        "SELECT id::text AS id, email, full_name, role, created_at, is_active FROM users WHERE id = $1::uuid",
    )
    .bind(&user.id)
    .fetch_optional(pool)
    .await?
    .ok_or_else(|| ApiError::Unauthorized("Account no longer exists".to_string()))?;

    if !row.get::<Option<bool>, _>("is_active").unwrap_or(true) {
        return Err(ApiError::Forbidden("This account has been disabled".to_string()));
    }
    Ok(Json(profile_from_row(&row)))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn email_normalisation_and_validation() {
        assert_eq!(normalize_email("  Foo@Example.COM ").unwrap(), "foo@example.com");
        for bad in ["", "foo", "foo@", "@bar.com", "foo@bar", "foo@.com", "a b@c.com", "a@b@c.com"] {
            assert!(normalize_email(bad).is_err(), "{bad} should be rejected");
        }
    }

    #[test]
    fn password_rules() {
        assert!(validate_password("short").is_err());
        assert!(validate_password("longenough").is_ok());
        assert!(validate_password(&"a".repeat(73)).is_err());
    }

    #[test]
    fn bcrypt_verifies_pgcrypto_style_hashes() {
        // Hashes produced by pgcrypto's crypt(.., gen_salt('bf')) use the $2a$ prefix.
        let hash = bcrypt::hash_with_result("correct horse", 4).unwrap().format_for_version(bcrypt::Version::TwoA);
        assert!(hash.starts_with("$2a$"));
        assert!(bcrypt::verify("correct horse", &hash).unwrap());
        assert!(!bcrypt::verify("wrong", &hash).unwrap());
    }
}
