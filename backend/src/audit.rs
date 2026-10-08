//! Append-Only Tamper-Evident Audit Ledger (Item #44)
//! Every sensitive security and administrative event is recorded in `platform_audit_ledger`
//! using cryptographic SHA-256 hash chaining (curr_hash = SHA256(sequence_id:event_type:actor_id:target_id:payload:prev_hash:created_at)).
//! Any post-hoc database row alteration or row deletion breaks the cryptographic chain.

use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use sha2::{Digest, Sha256};
use sqlx::{PgPool, Row};
use uuid::Uuid;

pub const GENESIS_HASH: &str = "0000000000000000000000000000000000000000000000000000000000000000";

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct AuditEntry {
    pub sequence_id: i64,
    pub event_type: String,
    pub actor_id: Option<Uuid>,
    pub target_id: Option<String>,
    pub payload_json: serde_json::Value,
    pub prev_hash: String,
    pub curr_hash: String,
    pub created_at: DateTime<Utc>,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct AuditVerificationResult {
    pub is_valid: bool,
    pub total_records: i64,
    pub broken_sequence_id: Option<i64>,
    pub error_message: Option<String>,
}

/// Compute the deterministic SHA-256 hash of an audit event
pub fn compute_event_hash(
    sequence_id: i64,
    event_type: &str,
    actor_id: Option<Uuid>,
    target_id: Option<&str>,
    payload_str: &str,
    prev_hash: &str,
    created_at_epoch_ms: i64,
) -> String {
    let mut hasher = Sha256::new();
    let actor_str = actor_id
        .map(|u| u.to_string())
        .unwrap_or_else(|| "none".to_string());
    let target_str = target_id.unwrap_or("none");

    hasher.update(format!("{}:", sequence_id).as_bytes());
    hasher.update(format!("{}:", event_type).as_bytes());
    hasher.update(format!("{}:", actor_str).as_bytes());
    hasher.update(format!("{}:", target_str).as_bytes());
    hasher.update(format!("{}:", payload_str).as_bytes());
    hasher.update(format!("{}:", prev_hash).as_bytes());
    hasher.update(format!("{}", created_at_epoch_ms).as_bytes());

    let result = hasher.finalize();
    hex::encode(result)
}

/// Record an audit event into the append-only ledger with cryptographic hash chaining
pub async fn record_audit_event(
    pool: &PgPool,
    event_type: &str,
    actor_id: Option<Uuid>,
    target_id: Option<&str>,
    payload: serde_json::Value,
) -> Result<AuditEntry, sqlx::Error> {
    let payload_str = payload.to_string();
    let now = Utc::now();
    let now_epoch_ms = now.timestamp_millis();

    // Acquire transaction to guarantee sequential hash calculation without race conditions
    let mut tx = pool.begin().await?;

    // Fetch the latest entry hash and sequence
    let latest_row = sqlx::query(
        r#"
        SELECT sequence_id, curr_hash
        FROM platform_audit_ledger
        ORDER BY sequence_id DESC
        LIMIT 1
        FOR UPDATE
        "#,
    )
    .fetch_optional(&mut *tx)
    .await?;

    let (next_seq, prev_hash) = match latest_row {
        Some(row) => {
            let last_seq: i64 = row.try_get("sequence_id")?;
            let last_hash: String = row.try_get("curr_hash")?;
            (last_seq + 1, last_hash)
        }
        None => (1, GENESIS_HASH.to_string()),
    };

    let curr_hash = compute_event_hash(
        next_seq,
        event_type,
        actor_id,
        target_id,
        &payload_str,
        &prev_hash,
        now_epoch_ms,
    );

    let inserted_row = sqlx::query(
        r#"
        INSERT INTO platform_audit_ledger (
            sequence_id, event_type, actor_id, target_id, payload_json, prev_hash, curr_hash, created_at
        )
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
        RETURNING sequence_id, event_type, actor_id, target_id, payload_json, prev_hash, curr_hash, created_at
        "#,
    )
    .bind(next_seq)
    .bind(event_type)
    .bind(actor_id)
    .bind(target_id)
    .bind(&payload)
    .bind(&prev_hash)
    .bind(&curr_hash)
    .bind(now)
    .fetch_one(&mut *tx)
    .await?;

    tx.commit().await?;

    Ok(AuditEntry {
        sequence_id: inserted_row.try_get("sequence_id")?,
        event_type: inserted_row.try_get("event_type")?,
        actor_id: inserted_row.try_get("actor_id")?,
        target_id: inserted_row.try_get("target_id")?,
        payload_json: inserted_row.try_get("payload_json")?,
        prev_hash: inserted_row.try_get("prev_hash")?,
        curr_hash: inserted_row.try_get("curr_hash")?,
        created_at: inserted_row.try_get("created_at")?,
    })
}

/// Verify the entire cryptographic chain of platform_audit_ledger
pub async fn verify_audit_ledger(pool: &PgPool) -> Result<AuditVerificationResult, sqlx::Error> {
    let rows = sqlx::query(
        r#"
        SELECT sequence_id, event_type, actor_id, target_id, payload_json, prev_hash, curr_hash, created_at
        FROM platform_audit_ledger
        ORDER BY sequence_id ASC
        "#,
    )
    .fetch_all(pool)
    .await?;

    let total = rows.len() as i64;
    let mut expected_prev_hash = GENESIS_HASH.to_string();

    for row in rows {
        let seq: i64 = row.try_get("sequence_id")?;
        let event_type: String = row.try_get("event_type")?;
        let actor_id: Option<Uuid> = row.try_get("actor_id")?;
        let target_id: Option<String> = row.try_get("target_id")?;
        let payload: serde_json::Value = row.try_get("payload_json")?;
        let prev_hash: String = row.try_get("prev_hash")?;
        let curr_hash: String = row.try_get("curr_hash")?;
        let created_at: DateTime<Utc> = row.try_get("created_at")?;

        // 1. Verify prev_hash link
        if prev_hash != expected_prev_hash {
            return Ok(AuditVerificationResult {
                is_valid: false,
                total_records: total,
                broken_sequence_id: Some(seq),
                error_message: Some(format!(
                    "Broken hash chain at sequence {}: expected prev_hash {}, found {}",
                    seq, expected_prev_hash, prev_hash
                )),
            });
        }

        // 2. Verify curr_hash recalculation
        let calculated_hash = compute_event_hash(
            seq,
            &event_type,
            actor_id,
            target_id.as_deref(),
            &payload.to_string(),
            &prev_hash,
            created_at.timestamp_millis(),
        );

        if calculated_hash != curr_hash {
            return Ok(AuditVerificationResult {
                is_valid: false,
                total_records: total,
                broken_sequence_id: Some(seq),
                error_message: Some(format!(
                    "Tampered entry at sequence {}: record hash {} does not match computed hash {}",
                    seq, curr_hash, calculated_hash
                )),
            });
        }

        expected_prev_hash = curr_hash;
    }

    Ok(AuditVerificationResult {
        is_valid: true,
        total_records: total,
        broken_sequence_id: None,
        error_message: None,
    })
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_genesis_hash_computation() {
        let hash1 = compute_event_hash(
            1,
            "USER_REGISTERED",
            None,
            Some("candidate@example.com"),
            "{}",
            GENESIS_HASH,
            1700000000000,
        );
        let hash2 = compute_event_hash(
            1,
            "USER_REGISTERED",
            None,
            Some("candidate@example.com"),
            "{}",
            GENESIS_HASH,
            1700000000000,
        );
        assert_eq!(hash1, hash2);
        assert_eq!(hash1.len(), 64);
    }

    #[test]
    fn test_tamper_detection() {
        let hash_original = compute_event_hash(
            1,
            "USER_REGISTERED",
            None,
            Some("candidate@example.com"),
            r#"{"role":"user"}"#,
            GENESIS_HASH,
            1700000000000,
        );
        let hash_tampered = compute_event_hash(
            1,
            "USER_REGISTERED",
            None,
            Some("candidate@example.com"),
            r#"{"role":"admin"}"#, // Tampered payload
            GENESIS_HASH,
            1700000000000,
        );
        assert_ne!(hash_original, hash_tampered);
    }
}
