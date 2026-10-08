//! Audit Ledger Verification and Query Handlers (Item #44)

use axum::{
    extract::{Query, State},
    Json,
};
use chrono::{DateTime, Utc};
use serde::Deserialize;
use sqlx::{PgPool, Row};
use uuid::Uuid;

use crate::audit::verify_audit_ledger;
use crate::auth::AuthUser;
use crate::error::ApiError;
use crate::models::{AuditEventItem, AuditVerificationResponse};

#[derive(Debug, Deserialize)]
pub struct AuditQuery {
    pub limit: Option<i64>,
}

/// GET /api/audit/verify
#[utoipa::path(
    get,
    path = "/api/audit/verify",
    responses(
        (status = 200, description = "Audit ledger cryptographic chain verification result", body = AuditVerificationResponse)
    ),
    tag = "Enterprise"
)]
pub async fn verify_chain(
    State(pool): State<PgPool>,
) -> Result<Json<AuditVerificationResponse>, ApiError> {
    let result = verify_audit_ledger(&pool)
        .await
        .map_err(|e| ApiError::internal_msg("Database error verifying audit ledger", e.to_string()))?;

    let message = if result.is_valid {
        format!(
            "Cryptographic integrity intact: {} events chained with verified SHA-256 links.",
            result.total_records
        )
    } else {
        result.error_message.unwrap_or_else(|| "Broken chain detected".to_string())
    };

    Ok(Json(AuditVerificationResponse {
        is_valid: result.is_valid,
        total_records: result.total_records,
        broken_sequence_id: result.broken_sequence_id,
        message,
    }))
}

/// GET /api/audit/events
#[utoipa::path(
    get,
    path = "/api/audit/events",
    responses(
        (status = 200, description = "List recent platform audit ledger events", body = Vec<AuditEventItem>),
        (status = 401, description = "Unauthorized"),
        (status = 403, description = "Forbidden: Admin access required")
    ),
    tag = "Enterprise"
)]
pub async fn list_events(
    State(pool): State<PgPool>,
    user: AuthUser,
    Query(query): Query<AuditQuery>,
) -> Result<Json<Vec<AuditEventItem>>, ApiError> {
    if !user.is_admin() {
        return Err(ApiError::forbidden("Admin privileges required to view audit ledger events."));
    }

    let limit = query.limit.unwrap_or(50).clamp(1, 200);

    let rows = sqlx::query(
        r#"
        SELECT sequence_id, event_type, actor_id, target_id, payload_json, prev_hash, curr_hash, created_at
        FROM platform_audit_ledger
        ORDER BY sequence_id DESC
        LIMIT $1
        "#,
    )
    .bind(limit)
    .fetch_all(&pool)
    .await
    .map_err(|e| ApiError::internal_msg("Database error querying audit ledger", e.to_string()))?;

    let mut events = Vec::new();
    for row in rows {
        let seq: i64 = row.try_get("sequence_id").unwrap_or_default();
        let ev_type: String = row.try_get("event_type").unwrap_or_default();
        let actor: Option<Uuid> = row.try_get("actor_id").ok();
        let target: Option<String> = row.try_get("target_id").ok();
        let payload: serde_json::Value = row.try_get("payload_json").unwrap_or_default();
        let prev: String = row.try_get("prev_hash").unwrap_or_default();
        let curr: String = row.try_get("curr_hash").unwrap_or_default();
        let created: DateTime<Utc> = row.try_get("created_at").unwrap_or_else(|_| Utc::now());

        events.push(AuditEventItem {
            sequence_id: seq,
            event_type: ev_type,
            actor_id: actor.map(|u| u.to_string()),
            target_id: target,
            payload_json: payload,
            prev_hash: prev,
            curr_hash: curr,
            created_at: created,
        });
    }

    Ok(Json(events))
}
