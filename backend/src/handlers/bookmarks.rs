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
use crate::models::{BookmarkItem, BookmarkRequest};

pub type BookmarkStore = Arc<RwLock<Vec<BookmarkItem>>>;

#[utoipa::path(
    get,
    path = "/api/bookmarks",
    responses(
        (status = 200, description = "List all user bookmarks", body = Vec<BookmarkItem>)
    ),
    tag = "Bookmarks"
)]
pub async fn get_bookmarks(State(store): State<BookmarkStore>) -> impl IntoResponse {
    let r = store.read().await;
    Json(r.clone())
}

#[utoipa::path(
    post,
    path = "/api/bookmarks",
    request_body = BookmarkRequest,
    responses(
        (status = 201, description = "Bookmark created or toggled", body = BookmarkItem)
    ),
    tag = "Bookmarks"
)]
pub async fn toggle_bookmark(
    State(store): State<BookmarkStore>,
    Json(req): Json<BookmarkRequest>,
) -> impl IntoResponse {
    let mut w = store.write().await;
    if let Some(pos) = w.iter().position(|b| b.category_id == req.category_id && b.question_number == req.question_number) {
        let removed = w.remove(pos);
        (StatusCode::OK, Json(removed))
    } else {
        let item = BookmarkItem {
            id: Uuid::new_v4().to_string(),
            category_id: req.category_id,
            question_number: req.question_number,
            created_at: Utc::now(),
        };
        w.push(item.clone());
        (StatusCode::CREATED, Json(item))
    }
}
