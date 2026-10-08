use sqlx::{postgres::PgPoolOptions, PgPool, Row};
use std::sync::OnceLock;
use std::time::Duration;
use tracing::{info, warn};
use crate::models::{BookmarkItem, LeaderboardEntry, NoteItem};
use chrono::{DateTime, Utc};

static GLOBAL_POOL: OnceLock<PgPool> = OnceLock::new();

pub fn set_global_pool(pool: PgPool) {
    let _ = GLOBAL_POOL.set(pool);
}

pub fn get_global_pool() -> Option<&'static PgPool> {
    GLOBAL_POOL.get()
}

pub async fn connect_db(database_url: &str) -> Option<PgPool> {
    info!("Connecting to PostgreSQL database: {}", sanitize_url(database_url));
    match PgPoolOptions::new()
        .max_connections(10)
        .acquire_timeout(Duration::from_secs(5))
        .connect(database_url)
        .await
    {
        Ok(pool) => {
            info!("Successfully established PostgreSQL connection pool!");
            set_global_pool(pool.clone());
            Some(pool)
        }
        Err(err) => {
            warn!("PostgreSQL connection failed: {}. Continuing with in-memory store.", err);
            None
        }
    }
}

pub fn sanitize_url(url: &str) -> String {
    if let Some(idx) = url.find('@') {
        let proto = url.split("://").next().unwrap_or("postgresql");
        let host_part = &url[idx..];
        format!("{}://***{}", proto, host_part)
    } else {
        url.to_string()
    }
}

/// Fetch bookmarks from PostgreSQL for a user
pub async fn fetch_user_bookmarks(pool: &PgPool, user_id: &str) -> Result<Vec<BookmarkItem>, sqlx::Error> {
    let rows = sqlx::query(
        r#"
        SELECT b.id::text, q.category_id, q.question_number, b.created_at
        FROM user_bookmarks b
        JOIN questions q ON b.question_id = q.id
        WHERE b.user_id = $1::uuid
        ORDER BY b.created_at DESC
        "#,
    )
    .bind(user_id)
    .fetch_all(pool)
    .await?;

    let bookmarks = rows.into_iter().map(|row| {
        let id: String = row.get(0);
        let category_id: String = row.get(1);
        let question_number: i32 = row.get(2);
        let created_at: DateTime<Utc> = row.get(3);
        BookmarkItem {
            id,
            category_id,
            question_number,
            created_at,
        }
    }).collect();

    Ok(bookmarks)
}

/// Toggle bookmark in PostgreSQL
pub async fn toggle_bookmark_db(
    pool: &PgPool,
    user_id: &str,
    category_id: &str,
    question_number: i32,
) -> Result<Option<BookmarkItem>, sqlx::Error> {
    // 1. Look up question_id
    let q_row = sqlx::query(
        "SELECT id::text FROM questions WHERE category_id = $1 AND question_number = $2 LIMIT 1",
    )
    .bind(category_id)
    .bind(question_number)
    .fetch_optional(pool)
    .await?;

    let q_id = match q_row {
        Some(r) => r.get::<String, _>(0),
        None => return Ok(None),
    };

    // 2. Check if bookmark exists
    let existing = sqlx::query(
        "SELECT id::text, created_at FROM user_bookmarks WHERE user_id = $1::uuid AND question_id = $2::uuid",
    )
    .bind(user_id)
    .bind(&q_id)
    .fetch_optional(pool)
    .await?;

    if let Some(ex) = existing {
        // Delete it
        let bookmark_id: String = ex.get(0);
        let created_at: DateTime<Utc> = ex.get(1);
        sqlx::query("DELETE FROM user_bookmarks WHERE id = $1::uuid")
            .bind(&bookmark_id)
            .execute(pool)
            .await?;

        Ok(Some(BookmarkItem {
            id: bookmark_id,
            category_id: category_id.to_string(),
            question_number,
            created_at,
        }))
    } else {
        // Insert new bookmark
        let new_id = uuid::Uuid::new_v4().to_string();
        let now = Utc::now();
        sqlx::query(
            "INSERT INTO user_bookmarks (id, user_id, question_id, created_at) VALUES ($1::uuid, $2::uuid, $3::uuid, $4)",
        )
        .bind(&new_id)
        .bind(user_id)
        .bind(&q_id)
        .bind(now)
        .execute(pool)
        .await?;

        Ok(Some(BookmarkItem {
            id: new_id,
            category_id: category_id.to_string(),
            question_number,
            created_at: now,
        }))
    }
}

/// Fetch notes from PostgreSQL
pub async fn fetch_user_notes(pool: &PgPool, user_id: &str) -> Result<Vec<NoteItem>, sqlx::Error> {
    let rows = sqlx::query(
        r#"
        SELECT n.id::text, q.category_id, q.question_number, n.note_content, n.updated_at
        FROM user_question_notes n
        JOIN questions q ON n.question_id = q.id
        WHERE n.user_id = $1::uuid
        ORDER BY n.updated_at DESC
        "#,
    )
    .bind(user_id)
    .fetch_all(pool)
    .await?;

    let notes = rows.into_iter().map(|row| {
        let id: String = row.get(0);
        let category_id: String = row.get(1);
        let question_number: i32 = row.get(2);
        let note_content: String = row.get(3);
        let updated_at: DateTime<Utc> = row.get(4);
        NoteItem {
            id,
            category_id,
            question_number,
            note_content,
            updated_at,
        }
    }).collect();

    Ok(notes)
}

/// Save or update note in PostgreSQL
pub async fn save_note_db(
    pool: &PgPool,
    user_id: &str,
    category_id: &str,
    question_number: i32,
    content: &str,
) -> Result<Option<NoteItem>, sqlx::Error> {
    let q_row = sqlx::query(
        "SELECT id::text FROM questions WHERE category_id = $1 AND question_number = $2 LIMIT 1",
    )
    .bind(category_id)
    .bind(question_number)
    .fetch_optional(pool)
    .await?;

    let q_id = match q_row {
        Some(r) => r.get::<String, _>(0),
        None => return Ok(None),
    };

    let now = Utc::now();
    let row = sqlx::query(
        r#"
        INSERT INTO user_question_notes (user_id, question_id, note_content, created_at, updated_at)
        VALUES ($1::uuid, $2::uuid, $3, $4, $4)
        ON CONFLICT (user_id, question_id) DO UPDATE SET
            note_content = EXCLUDED.note_content,
            updated_at = EXCLUDED.updated_at
        RETURNING id::text, updated_at
        "#,
    )
    .bind(user_id)
    .bind(&q_id)
    .bind(content)
    .bind(now)
    .fetch_one(pool)
    .await?;

    let note_id: String = row.get(0);
    let updated_at: DateTime<Utc> = row.get(1);

    Ok(Some(NoteItem {
        id: note_id,
        category_id: category_id.to_string(),
        question_number,
        note_content: content.to_string(),
        updated_at,
    }))
}

/// Fetch global leaderboard from PostgreSQL
pub async fn fetch_leaderboard_db(pool: &PgPool) -> Result<Vec<LeaderboardEntry>, sqlx::Error> {
    let rows = sqlx::query(
        r#"
        SELECT username, elo_rating, tier, battles_won, battles_lost, questions_solved, updated_at
        FROM leaderboard_entries
        ORDER BY elo_rating DESC
        LIMIT 50
        "#,
    )
    .fetch_all(pool)
    .await?;

    let entries = rows.into_iter().map(|row| {
        LeaderboardEntry {
            username: row.get(0),
            elo_rating: row.get(1),
            tier: row.get(2),
            battles_won: row.get(3),
            battles_lost: row.get(4),
            questions_solved: row.get(5),
            updated_at: row.get(6),
        }
    }).collect();

    Ok(entries)
}

/// Log search telemetry to PostgreSQL
pub async fn log_search_telemetry_db(
    pool: &PgPool,
    query: &str,
    results_count: i32,
    execution_time_ms: f64,
) -> Result<(), sqlx::Error> {
    sqlx::query(
        r#"
        INSERT INTO search_telemetry (search_query, results_count, execution_time_ms)
        VALUES ($1, $2, $3)
        "#,
    )
    .bind(query)
    .bind(results_count)
    .bind(execution_time_ms)
    .execute(pool)
    .await?;

    Ok(())
}
