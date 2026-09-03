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

pub type NoteStore = Arc<RwLock<Vec<NoteItem>>>;

#[utoipa::path(
    get,
    path = "/api/notes",
    responses(
        (status = 200, description = "List all user notes", body = Vec<NoteItem>)
    ),
    tag = "Notes"
)]
pub async fn get_notes(State(store): State<NoteStore>) -> impl IntoResponse {
    let r = store.read().await;
    Json(r.clone())
}

#[utoipa::path(
    post,
    path = "/api/notes",
    request_body = NoteRequest,
    responses(
        (status = 200, description = "Note saved", body = NoteItem)
    ),
    tag = "Notes"
)]
pub async fn save_note(
    State(store): State<NoteStore>,
    Json(req): Json<NoteRequest>,
) -> impl IntoResponse {
    let mut w = store.write().await;
    if let Some(existing) = w.iter_mut().find(|n| n.category_id == req.category_id && n.question_number == req.question_number) {
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
