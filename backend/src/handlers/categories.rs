use axum::{
    extract::{Path, State},
    http::StatusCode,
    response::IntoResponse,
    Json,
};
use crate::content_loader::SharedStore;
use crate::models::Category;

#[utoipa::path(
    get,
    path = "/api/categories",
    responses(
        (status = 200, description = "List all 46 interview categories", body = Vec<Category>)
    ),
    tag = "Categories"
)]
pub async fn get_all_categories(State(store): State<SharedStore>) -> impl IntoResponse {
    let r = store.read().await;
    Json(r.categories.clone())
}

#[utoipa::path(
    get,
    path = "/api/categories/{id}",
    params(
        ("id" = String, Path, description = "Category ID (e.g. javascript, react, rust)")
    ),
    responses(
        (status = 200, description = "Category details", body = Category),
        (status = 404, description = "Category not found")
    ),
    tag = "Categories"
)]
pub async fn get_category_by_id(
    State(store): State<SharedStore>,
    Path(id): Path<String>,
) -> Result<Json<Category>, StatusCode> {
    let r = store.read().await;
    r.categories
        .iter()
        .find(|c| c.id.eq_ignore_ascii_case(&id))
        .cloned()
        .map(Json)
        .ok_or(StatusCode::NOT_FOUND)
}
