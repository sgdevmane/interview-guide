use axum::{
    extract::{Query, State},
    response::IntoResponse,
    Json,
};
use crate::content_loader::{search_questions, SharedStore};
use serde::Deserialize;

#[derive(Debug, Deserialize)]
pub struct SearchParams {
    pub q: String,
}

#[utoipa::path(
    get,
    path = "/api/search",
    params(
        ("q" = String, Query, description = "Search query keyword")
    ),
    responses(
        (status = 200, description = "Search results matching query", body = Vec<SearchResult>)
    ),
    tag = "Search"
)]
pub async fn search_handler(
    State(store): State<SharedStore>,
    Query(params): Query<SearchParams>,
) -> impl IntoResponse {
    let r = store.read().await;
    let results = search_questions(&r, &params.q);
    metrics::counter!("search_queries_total").increment(1);
    Json(results)
}
