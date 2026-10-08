//! Timed Contests & Competitive Assessment Handlers (Items #10, #12)

use axum::{
    extract::{Path, State},
    Json,
};
use chrono::Utc;
use sqlx::{PgPool, Row};
use uuid::Uuid;

use crate::auth::AuthUser;
use crate::error::ApiError;
use crate::models::{
    ContestParticipantResponse, JoinContestRequest, SubmitContestRequest, TimedContestItem,
};

/// GET /api/contests
#[utoipa::path(
    get,
    path = "/api/contests",
    responses(
        (status = 200, description = "List all timed contests", body = Vec<TimedContestItem>)
    ),
    tag = "Competitive"
)]
pub async fn list_contests(
    State(pool): State<PgPool>,
) -> Result<Json<Vec<TimedContestItem>>, ApiError> {
    let rows = sqlx::query(
        r#"
        SELECT 
            c.id, c.contest_code, c.title, c.description, c.difficulty, c.category, 
            c.start_time, c.duration_minutes,
            COUNT(p.id) as participant_count
        FROM timed_contests c
        LEFT JOIN contest_participants p ON c.id = p.contest_id
        GROUP BY c.id
        ORDER BY c.start_time DESC
        "#,
    )
    .fetch_all(&pool)
    .await
    .map_err(|e| ApiError::internal_msg("Database lookup failed", e.to_string()))?;

    let contests = rows
        .into_iter()
        .map(|r| {
            let id: Uuid = r.try_get("id").unwrap_or_default();
            let contest_code: String = r.try_get("contest_code").unwrap_or_default();
            let title: String = r.try_get("title").unwrap_or_default();
            let description: Option<String> = r.try_get("description").ok();
            let difficulty: String = r.try_get("difficulty").unwrap_or_else(|_| "medium".to_string());
            let category: Option<String> = r.try_get("category").ok();
            let start_time: chrono::DateTime<Utc> = r.try_get("start_time").unwrap_or_else(|_| Utc::now());
            let duration_minutes: i32 = r.try_get("duration_minutes").unwrap_or(60);
            let participant_count: i64 = r.try_get("participant_count").unwrap_or(0);

            TimedContestItem {
                id: id.to_string(),
                contest_code,
                title,
                description,
                difficulty,
                category,
                start_time,
                duration_minutes,
                participant_count,
            }
        })
        .collect();

    Ok(Json(contests))
}

/// POST /api/contests/join
#[utoipa::path(
    post,
    path = "/api/contests/join",
    request_body = JoinContestRequest,
    responses(
        (status = 200, description = "Joined contest successfully", body = ContestParticipantResponse),
        (status = 404, description = "Contest not found"),
        (status = 401, description = "Unauthorized")
    ),
    tag = "Competitive"
)]
pub async fn join_contest(
    State(pool): State<PgPool>,
    user: AuthUser,
    Json(payload): Json<JoinContestRequest>,
) -> Result<Json<ContestParticipantResponse>, ApiError> {
    let user_uuid = Uuid::parse_str(&user.id)
        .map_err(|_| ApiError::bad_request("Invalid user id"))?;

    let contest_row = sqlx::query("SELECT id, contest_code FROM timed_contests WHERE contest_code = $1")
        .bind(&payload.contest_code)
        .fetch_optional(&pool)
        .await
        .map_err(|e| ApiError::internal_msg("Database lookup failed", e.to_string()))?
        .ok_or_else(|| ApiError::not_found("Contest not found"))?;

    let contest_id: Uuid = contest_row.try_get("id").unwrap_or_default();

    let part_row = sqlx::query(
        r#"
        INSERT INTO contest_participants (contest_id, user_id, score, time_taken_seconds)
        VALUES ($1, $2, 0, 0)
        ON CONFLICT (contest_id, user_id) DO UPDATE SET contest_id = EXCLUDED.contest_id
        RETURNING score, time_taken_seconds, finished_at
        "#,
    )
    .bind(contest_id)
    .bind(user_uuid)
    .fetch_one(&pool)
    .await
    .map_err(|e| ApiError::internal_msg("Database insert failed", e.to_string()))?;

    let score: i32 = part_row.try_get("score").unwrap_or(0);
    let time_taken_seconds: i32 = part_row.try_get("time_taken_seconds").unwrap_or(0);
    let finished_at: Option<chrono::DateTime<Utc>> = part_row.try_get("finished_at").ok();

    Ok(Json(ContestParticipantResponse {
        contest_id: contest_id.to_string(),
        contest_code: payload.contest_code,
        user_id: user.id,
        score,
        time_taken_seconds,
        rank: 1,
        finished: finished_at.is_some(),
    }))
}

/// POST /api/contests/submit
#[utoipa::path(
    post,
    path = "/api/contests/submit",
    request_body = SubmitContestRequest,
    responses(
        (status = 200, description = "Contest submission recorded", body = ContestParticipantResponse),
        (status = 404, description = "Contest not found"),
        (status = 401, description = "Unauthorized")
    ),
    tag = "Competitive"
)]
pub async fn submit_contest(
    State(pool): State<PgPool>,
    user: AuthUser,
    Json(payload): Json<SubmitContestRequest>,
) -> Result<Json<ContestParticipantResponse>, ApiError> {
    let user_uuid = Uuid::parse_str(&user.id)
        .map_err(|_| ApiError::bad_request("Invalid user id"))?;

    let contest_row = sqlx::query("SELECT id FROM timed_contests WHERE contest_code = $1")
        .bind(&payload.contest_code)
        .fetch_optional(&pool)
        .await
        .map_err(|e| ApiError::internal_msg("Database lookup failed", e.to_string()))?
        .ok_or_else(|| ApiError::not_found("Contest not found"))?;

    let contest_id: Uuid = contest_row.try_get("id").unwrap_or_default();

    sqlx::query(
        r#"
        INSERT INTO contest_participants (contest_id, user_id, score, time_taken_seconds, finished_at)
        VALUES ($1, $2, $3, $4, NOW())
        ON CONFLICT (contest_id, user_id) DO UPDATE
        SET score = EXCLUDED.score, time_taken_seconds = EXCLUDED.time_taken_seconds, finished_at = NOW()
        "#,
    )
    .bind(contest_id)
    .bind(user_uuid)
    .bind(payload.score)
    .bind(payload.time_taken_seconds)
    .execute(&pool)
    .await
    .map_err(|e| ApiError::internal_msg("Database update failed", e.to_string()))?;

    // Calculate user rank in contest
    let rank_row = sqlx::query(
        r#"
        SELECT COUNT(*) + 1 as rank
        FROM contest_participants
        WHERE contest_id = $1 AND (score > $2 OR (score = $2 AND time_taken_seconds < $3))
        "#,
    )
    .bind(contest_id)
    .bind(payload.score)
    .bind(payload.time_taken_seconds)
    .fetch_one(&pool)
    .await
    .map_err(|e| ApiError::internal_msg("Rank calculation error", e.to_string()))?;

    let rank: i64 = rank_row.try_get("rank").unwrap_or(1);

    Ok(Json(ContestParticipantResponse {
        contest_id: contest_id.to_string(),
        contest_code: payload.contest_code,
        user_id: user.id,
        score: payload.score,
        time_taken_seconds: payload.time_taken_seconds,
        rank,
        finished: true,
    }))
}

/// GET /api/contests/:contest_code/leaderboard
#[utoipa::path(
    get,
    path = "/api/contests/{contest_code}/leaderboard",
    params(
        ("contest_code" = String, Path, description = "Contest code e.g. WEEKLY-CONTEST-101")
    ),
    responses(
        (status = 200, description = "Contest leaderboard ranked by score and time", body = serde_json::Value),
        (status = 404, description = "Contest not found")
    ),
    tag = "Competitive"
)]
pub async fn contest_leaderboard(
    State(pool): State<PgPool>,
    Path(contest_code): Path<String>,
) -> Result<Json<serde_json::Value>, ApiError> {
    let contest_row = sqlx::query("SELECT id, title FROM timed_contests WHERE contest_code = $1")
        .bind(&contest_code)
        .fetch_optional(&pool)
        .await
        .map_err(|e| ApiError::internal_msg("Database lookup error", e.to_string()))?
        .ok_or_else(|| ApiError::not_found("Contest not found"))?;

    let contest_id: Uuid = contest_row.try_get("id").unwrap_or_default();
    let title: String = contest_row.try_get("title").unwrap_or_default();

    let rows = sqlx::query(
        r#"
        SELECT 
            p.user_id, u.email, u.full_name, p.score, p.time_taken_seconds, p.finished_at,
            RANK() OVER (ORDER BY p.score DESC, p.time_taken_seconds ASC) as rank
        FROM contest_participants p
        JOIN users u ON p.user_id = u.id
        WHERE p.contest_id = $1
        ORDER BY rank ASC
        LIMIT 50
        "#,
    )
    .bind(contest_id)
    .fetch_all(&pool)
    .await
    .map_err(|e| ApiError::internal_msg("Leaderboard query failed", e.to_string()))?;

    let entries: Vec<serde_json::Value> = rows
        .into_iter()
        .map(|r| {
            let rank: i64 = r.try_get("rank").unwrap_or(1);
            let email: String = r.try_get("email").unwrap_or_default();
            let full_name: String = r.try_get("full_name").unwrap_or_default();
            let score: i32 = r.try_get("score").unwrap_or(0);
            let time_taken_seconds: i32 = r.try_get("time_taken_seconds").unwrap_or(0);

            serde_json::json!({
                "rank": rank,
                "full_name": full_name,
                "email_masked": mask_email(&email),
                "score": score,
                "time_taken_seconds": time_taken_seconds
            })
        })
        .collect();

    Ok(Json(serde_json::json!({
        "contest_code": contest_code,
        "title": title,
        "leaderboard": entries
    })))
}

fn mask_email(email: &str) -> String {
    let parts: Vec<&str> = email.split('@').collect();
    if parts.len() != 2 {
        return "***".to_string();
    }
    let name = parts[0];
    let domain = parts[1];
    if name.len() <= 2 {
        format!("{}*@{}", name, domain)
    } else {
        format!("{}***{}@{}", &name[0..1], &name[name.len()-1..], domain)
    }
}
