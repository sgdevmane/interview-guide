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
    let started = std::time::Instant::now();
    let r = store.read().await;
    let results = search_questions(&r, &params.q);
    let elapsed_ms = started.elapsed().as_secs_f64() * 1000.0;
    metrics::counter!("search_queries_total").increment(1);

    if let Some(pool) = crate::db::get_global_pool() {
        let pool = pool.clone();
        let query_str: String = params.q.chars().take(255).collect();
        let count = i32::try_from(results.len()).unwrap_or(i32::MAX);
        tokio::spawn(async move {
            if let Err(err) =
                crate::db::log_search_telemetry_db(&pool, &query_str, count, elapsed_ms).await
            {
                tracing::warn!("Failed to record search telemetry: {}", err);
            }
        });
    }

    Json(results)
}
