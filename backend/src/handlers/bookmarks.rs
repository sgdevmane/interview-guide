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
use crate::auth::MaybeAuthUser;
use crate::db;

const DEFAULT_DEMO_USER: &str = "00000000-0000-0000-0000-000000000002";

#[derive(Clone)]
pub struct BookmarkStore {
    pub in_memory: Arc<RwLock<Vec<BookmarkItem>>>,
    pub pool: Option<sqlx::PgPool>,
}

impl BookmarkStore {
    pub fn new(pool: Option<sqlx::PgPool>) -> Self {
        Self {
            in_memory: Arc::new(RwLock::new(Vec::new())),
            pool,
        }
    }
}

#[utoipa::path(
    get,
    path = "/api/bookmarks",
    responses(
        (status = 200, description = "List all user bookmarks", body = Vec<BookmarkItem>)
    ),
    security(("bearer_auth" = [])),
    tag = "Bookmarks"
)]
pub async fn get_bookmarks(
    State(store): State<BookmarkStore>,
    MaybeAuthUser(user): MaybeAuthUser,
) -> impl IntoResponse {
    let user_id = user.map(|u| u.id).unwrap_or_else(|| DEFAULT_DEMO_USER.to_string());
    if let Some(pool) = &store.pool {
        if let Ok(db_items) = db::fetch_user_bookmarks(pool, &user_id).await {
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
    path = "/api/bookmarks",
    request_body = BookmarkRequest,
    responses(
        (status = 200, description = "Bookmark removed", body = BookmarkItem),
        (status = 201, description = "Bookmark created", body = BookmarkItem)
    ),
    security(("bearer_auth" = [])),
    tag = "Bookmarks"
)]
pub async fn toggle_bookmark(
    State(store): State<BookmarkStore>,
    MaybeAuthUser(user): MaybeAuthUser,
    Json(req): Json<BookmarkRequest>,
) -> impl IntoResponse {
    let user_id = user.map(|u| u.id).unwrap_or_else(|| DEFAULT_DEMO_USER.to_string());

    if let Some(pool) = &store.pool {
        if let Ok(Some(item)) =
            db::toggle_bookmark_db(pool, &user_id, &req.category_id, req.question_number).await
        {
            let mut w = store.in_memory.write().await;
            if let Some(pos) = w.iter().position(|b| {
                b.category_id == req.category_id && b.question_number == req.question_number
            }) {
                w.remove(pos);
                return (StatusCode::OK, Json(item));
            } else {
                w.push(item.clone());
                return (StatusCode::CREATED, Json(item));
            }
        }
    }

    let mut w = store.in_memory.write().await;
    if let Some(pos) = w.iter().position(|b| {
        b.category_id == req.category_id && b.question_number == req.question_number
    }) {
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
