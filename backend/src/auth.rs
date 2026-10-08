//! Authentication core: JWT access tokens, rotating refresh tokens, the
//! `AuthUser` request extractor, and a login brute-force limiter.

use std::{
    collections::HashMap,
    env,
    sync::{Mutex, OnceLock},
    time::{Duration, Instant},
};

use axum::{
    async_trait,
    extract::FromRequestParts,
    http::{header, request::Parts, HeaderMap, HeaderValue},
};
use chrono::Utc;
use jsonwebtoken::{decode, encode, Algorithm, DecodingKey, EncodingKey, Header, Validation};
use rand::RngCore;
use serde::{Deserialize, Serialize};
use sha2::{Digest, Sha256};

use crate::error::ApiError;

pub const REFRESH_COOKIE: &str = "ig_refresh";
const ISSUER: &str = "interview-guide";
const MIN_SECRET_LEN: usize = 32;

pub struct AuthConfig {
    encoding: EncodingKey,
    decoding: DecodingKey,
    pub access_ttl_secs: i64,
    pub refresh_ttl_secs: i64,
    /// `Some(true/false)` forces the cookie `Secure` flag; `None` derives it
    /// from the `X-Forwarded-Proto` header set by the TLS-terminating proxy.
    cookie_secure: Option<bool>,
}

static AUTH_CONFIG: OnceLock<AuthConfig> = OnceLock::new();

/// Initialise auth configuration from the environment. Must run once at startup.
pub fn init_auth_config() {
    let secret = match env::var("JWT_SECRET") {
        Ok(s) if s.len() >= MIN_SECRET_LEN => s.into_bytes(),
        Ok(_) => {
            tracing::warn!(
                "JWT_SECRET is shorter than {} chars; using an ephemeral random secret instead",
                MIN_SECRET_LEN
            );
            random_bytes(64)
        }
        Err(_) => {
            tracing::warn!(
                "JWT_SECRET not set; using an ephemeral random secret. Sessions will not survive \
                 restarts or work across multiple backend instances."
            );
            random_bytes(64)
        }
    };

    let cookie_secure = match env::var("COOKIE_SECURE").ok().as_deref() {
        Some("true") | Some("1") => Some(true),
        Some("false") | Some("0") => Some(false),
        _ => None,
    };

    let access_ttl_secs = env_i64("JWT_ACCESS_TTL_SECS", 900).clamp(60, 3600);
    let refresh_ttl_secs = env_i64("JWT_REFRESH_TTL_SECS", 30 * 24 * 3600).clamp(3600, 90 * 24 * 3600);

    let _ = AUTH_CONFIG.set(AuthConfig {
        encoding: EncodingKey::from_secret(&secret),
        decoding: DecodingKey::from_secret(&secret),
        access_ttl_secs,
        refresh_ttl_secs,
        cookie_secure,
    });
}

pub fn config() -> &'static AuthConfig {
    AUTH_CONFIG.get_or_init(|| {
        let secret = random_bytes(64);
        AuthConfig {
            encoding: EncodingKey::from_secret(&secret),
            decoding: DecodingKey::from_secret(&secret),
            access_ttl_secs: 900,
            refresh_ttl_secs: 30 * 24 * 3600,
            cookie_secure: None,
        }
    })
}

fn env_i64(key: &str, default: i64) -> i64 {
    env::var(key).ok().and_then(|v| v.parse().ok()).unwrap_or(default)
}

fn random_bytes(n: usize) -> Vec<u8> {
    let mut buf = vec![0u8; n];
    rand::thread_rng().fill_bytes(&mut buf);
    buf
}

// ---------------------------------------------------------------------------
// Access tokens (JWT, HS256)
// ---------------------------------------------------------------------------

#[derive(Debug, Serialize, Deserialize)]
pub struct Claims {
    pub sub: String,
    pub email: String,
    pub role: String,
    pub iss: String,
    pub iat: i64,
    pub exp: i64,
}

pub fn issue_access_token(user_id: &str, email: &str, role: &str) -> Result<String, ApiError> {
    let cfg = config();
    let now = Utc::now().timestamp();
    let claims = Claims {
        sub: user_id.to_string(),
        email: email.to_string(),
        role: role.to_string(),
        iss: ISSUER.to_string(),
        iat: now,
        exp: now + cfg.access_ttl_secs,
    };
    encode(&Header::new(Algorithm::HS256), &claims, &cfg.encoding)
        .map_err(|e| ApiError::Internal(format!("jwt encode failed: {e}")))
}

pub fn verify_access_token(token: &str) -> Result<Claims, ApiError> {
    let mut validation = Validation::new(Algorithm::HS256);
    validation.set_issuer(&[ISSUER]);
    validation.leeway = 5;
    decode::<Claims>(token, &config().decoding, &validation)
        .map(|data| data.claims)
        .map_err(|_| ApiError::Unauthorized("Invalid or expired access token".to_string()))
}

// ---------------------------------------------------------------------------
// Refresh tokens (opaque random, only SHA-256 hash persisted)
// ---------------------------------------------------------------------------

pub fn generate_refresh_token() -> String {
    hex::encode(random_bytes(32))
}

pub fn hash_refresh_token(token: &str) -> String {
    hex::encode(Sha256::digest(token.as_bytes()))
}

fn wants_secure_cookie(headers: &HeaderMap) -> bool {
    config().cookie_secure.unwrap_or_else(|| {
        headers
            .get("x-forwarded-proto")
            .and_then(|v| v.to_str().ok())
            .map(|v| v.eq_ignore_ascii_case("https"))
            .unwrap_or(false)
    })
}

pub fn refresh_cookie(token: &str, headers: &HeaderMap) -> HeaderValue {
    let secure = if wants_secure_cookie(headers) { "; Secure" } else { "" };
    let value = format!(
        "{REFRESH_COOKIE}={token}; HttpOnly; SameSite=Strict; Path=/api/auth; Max-Age={}{secure}",
        config().refresh_ttl_secs
    );
    HeaderValue::from_str(&value).unwrap_or_else(|_| HeaderValue::from_static(""))
}

pub fn clear_refresh_cookie(headers: &HeaderMap) -> HeaderValue {
    let secure = if wants_secure_cookie(headers) { "; Secure" } else { "" };
    let value = format!("{REFRESH_COOKIE}=; HttpOnly; SameSite=Strict; Path=/api/auth; Max-Age=0{secure}");
    HeaderValue::from_str(&value).unwrap_or_else(|_| HeaderValue::from_static(""))
}

pub fn read_cookie(headers: &HeaderMap, name: &str) -> Option<String> {
    headers
        .get_all(header::COOKIE)
        .iter()
        .filter_map(|v| v.to_str().ok())
        .flat_map(|v| v.split(';'))
        .filter_map(|pair| {
            let (k, v) = pair.trim().split_once('=')?;
            (k == name && !v.is_empty()).then(|| v.to_string())
        })
        .next()
}

// ---------------------------------------------------------------------------
// Request extractor
// ---------------------------------------------------------------------------

/// Authenticated caller, extracted from `Authorization: Bearer <jwt>`.
#[derive(Debug, Clone)]
#[allow(dead_code)]
pub struct AuthUser {
    pub id: String,
    pub email: String,
    pub role: String,
}

impl AuthUser {
    #[allow(dead_code)]
    pub fn require_role(&self, allowed: &[&str]) -> Result<(), ApiError> {
        if allowed.contains(&self.role.as_str()) {
            Ok(())
        } else {
            Err(ApiError::Forbidden("Insufficient permissions".to_string()))
        }
    }

    pub fn is_admin(&self) -> bool {
        self.role == "admin"
    }
}

#[async_trait]
impl<S: Send + Sync> FromRequestParts<S> for AuthUser {
    type Rejection = ApiError;

    async fn from_request_parts(parts: &mut Parts, _state: &S) -> Result<Self, Self::Rejection> {
        let token = parts
            .headers
            .get(header::AUTHORIZATION)
            .and_then(|v| v.to_str().ok())
            .and_then(|v| v.strip_prefix("Bearer "))
            .map(str::trim)
            .filter(|t| !t.is_empty())
            .ok_or_else(|| ApiError::Unauthorized("Authentication required".to_string()))?;

        let claims = verify_access_token(token)?;
        Ok(AuthUser { id: claims.sub, email: claims.email, role: claims.role })
    }
}

/// Optional authenticated caller: Some(user) if valid JWT Bearer header present, None otherwise.
#[derive(Debug, Clone)]
pub struct MaybeAuthUser(pub Option<AuthUser>);

impl MaybeAuthUser {
    pub fn user_id(&self) -> String {
        self.0
            .as_ref()
            .map(|u| u.id.clone())
            .unwrap_or_else(|| "00000000-0000-0000-0000-000000000002".to_string())
    }
}

#[async_trait]
impl<S: Send + Sync> FromRequestParts<S> for MaybeAuthUser {
    type Rejection = std::convert::Infallible;

    async fn from_request_parts(parts: &mut Parts, state: &S) -> Result<Self, Self::Rejection> {
        match AuthUser::from_request_parts(parts, state).await {
            Ok(user) => Ok(MaybeAuthUser(Some(user))),
            Err(_) => Ok(MaybeAuthUser(None)),
        }
    }
}

// ---------------------------------------------------------------------------
// Login brute-force limiter (per email, per instance)
// ---------------------------------------------------------------------------

const MAX_FAILED_LOGINS: u32 = 5;
const LOCKOUT_WINDOW: Duration = Duration::from_secs(15 * 60);

fn failed_logins() -> &'static Mutex<HashMap<String, (u32, Instant)>> {
    static FAILED: OnceLock<Mutex<HashMap<String, (u32, Instant)>>> = OnceLock::new();
    FAILED.get_or_init(|| Mutex::new(HashMap::new()))
}

pub fn check_login_allowed(email: &str) -> Result<(), ApiError> {
    let map = failed_logins().lock().map_err(|_| ApiError::Internal("limiter poisoned".into()))?;
    if let Some((count, first)) = map.get(email) {
        if *count >= MAX_FAILED_LOGINS && first.elapsed() < LOCKOUT_WINDOW {
            return Err(ApiError::TooManyRequests(
                "Too many failed sign-in attempts. Try again in 15 minutes.".to_string(),
            ));
        }
    }
    Ok(())
}

pub fn record_login_failure(email: &str) {
    if let Ok(mut map) = failed_logins().lock() {
        if map.len() > 10_000 {
            map.retain(|_, (_, first)| first.elapsed() < LOCKOUT_WINDOW);
        }
        let entry = map.entry(email.to_string()).or_insert((0, Instant::now()));
        if entry.1.elapsed() >= LOCKOUT_WINDOW {
            *entry = (0, Instant::now());
        }
        entry.0 += 1;
    }
}

pub fn clear_login_failures(email: &str) {
    if let Ok(mut map) = failed_logins().lock() {
        map.remove(email);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn access_token_round_trip() {
        let token = issue_access_token("00000000-0000-0000-0000-000000000009", "a@b.co", "user").unwrap();
        let claims = verify_access_token(&token).unwrap();
        assert_eq!(claims.sub, "00000000-0000-0000-0000-000000000009");
        assert_eq!(claims.role, "user");
        assert!(claims.exp > claims.iat);
    }

    #[test]
    fn tampered_token_is_rejected() {
        let token = issue_access_token("id", "a@b.co", "user").unwrap();
        let mut tampered = token.clone();
        tampered.push('x');
        assert!(verify_access_token(&tampered).is_err());
    }

    #[test]
    fn refresh_token_hash_is_stable_and_hex() {
        let t = generate_refresh_token();
        assert_eq!(t.len(), 64);
        assert_eq!(hash_refresh_token(&t), hash_refresh_token(&t));
        assert_eq!(hash_refresh_token(&t).len(), 64);
        assert_ne!(hash_refresh_token(&t), t);
    }

    #[test]
    fn reads_named_cookie_only() {
        let mut headers = HeaderMap::new();
        headers.insert(header::COOKIE, HeaderValue::from_static("other=1; ig_refresh=abc123; x=y"));
        assert_eq!(read_cookie(&headers, REFRESH_COOKIE).as_deref(), Some("abc123"));
        assert_eq!(read_cookie(&headers, "missing"), None);
    }

    #[test]
    fn lockout_after_max_failures() {
        let email = "lockout-test@example.com";
        clear_login_failures(email);
        for _ in 0..MAX_FAILED_LOGINS {
            assert!(check_login_allowed(email).is_ok());
            record_login_failure(email);
        }
        assert!(check_login_allowed(email).is_err());
        clear_login_failures(email);
        assert!(check_login_allowed(email).is_ok());
    }

    #[test]
    fn role_check() {
        let u = AuthUser { id: "1".into(), email: "e".into(), role: "user".into() };
        assert!(u.require_role(&["user", "admin"]).is_ok());
        assert!(u.require_role(&["admin"]).is_err());
    }
}
