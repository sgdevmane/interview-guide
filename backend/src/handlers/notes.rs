use axum::{
    extract::State,
    http::StatusCode,
    response::IntoResponse,
    Json,
};
use chrono::Utc;
use std::sync::Arc;
use tokio::sync::RwLock;
use uuid::Uuid;
use crate::models::{NoteItem, NoteRequest};
use crate::auth::MaybeAuthUser;
use crate::db;

const DEFAULT_DEMO_USER: &str = "00000000-0000-0000-0000-000000000002";

#[derive(Clone)]
pub struct NoteStore {
    pub in_memory: Arc<RwLock<Vec<NoteItem>>>,
    pub pool: Option<sqlx::PgPool>,
}

impl NoteStore {
    pub fn new(pool: Option<sqlx::PgPool>) -> Self {
        Self {
            in_memory: Arc::new(RwLock::new(Vec::new())),
            pool,
        }
    }
}

#[utoipa::path(
    get,
    path = "/api/notes",
    responses(
        (status = 200, description = "List all user notes", body = Vec<NoteItem>)
    ),
    security(("bearer_auth" = [])),
    tag = "Notes"
)]
pub async fn get_notes(
    State(store): State<NoteStore>,
    MaybeAuthUser(user): MaybeAuthUser,
) -> impl IntoResponse {
    let user_id = user.map(|u| u.id).unwrap_or_else(|| DEFAULT_DEMO_USER.to_string());
    if let Some(pool) = &store.pool {
        if let Ok(db_items) = db::fetch_user_notes(pool, &user_id).await {
            if !db_items.is_empty() {
                return Json(db_items);
            }
        }
    }
    let r = store.in_memory.read().await;
    Json(r.clone())
}

#[utoipa::path(
    post,
    path = "/api/notes",
    request_body = NoteRequest,
    responses(
        (status = 200, description = "Note updated", body = NoteItem),
        (status = 201, description = "Note created", body = NoteItem)
    ),
    security(("bearer_auth" = [])),
    tag = "Notes"
)]
pub async fn save_note(
    State(store): State<NoteStore>,
    MaybeAuthUser(user): MaybeAuthUser,
    Json(req): Json<NoteRequest>,
) -> impl IntoResponse {
    let user_id = user.map(|u| u.id).unwrap_or_else(|| DEFAULT_DEMO_USER.to_string());

    if let Some(pool) = &store.pool {
        if let Ok(Some(item)) = db::save_note_db(
            pool,
            &user_id,
            &req.category_id,
            req.question_number,
            &req.note_content,
        )
        .await
        {
            let mut w = store.in_memory.write().await;
            if let Some(existing) = w.iter_mut().find(|n| {
                n.category_id == req.category_id && n.question_number == req.question_number
            }) {
                *existing = item.clone();
                return (StatusCode::OK, Json(item));
            } else {
                w.push(item.clone());
                return (StatusCode::CREATED, Json(item));
            }
        }
    }

    let mut w = store.in_memory.write().await;
    if let Some(existing) = w.iter_mut().find(|n| {
        n.category_id == req.category_id && n.question_number == req.question_number
    }) {
        existing.note_content = req.note_content;
        existing.updated_at = Utc::now();
        (StatusCode::OK, Json(existing.clone()))
    } else {
        let item = NoteItem {
            id: Uuid::new_v4().to_string(),
            category_id: req.category_id,
            question_number: req.question_number,
            note_content: req.note_content,
            updated_at: Utc::now(),
        };
        w.push(item.clone());
        (StatusCode::CREATED, Json(item))
    }
}
