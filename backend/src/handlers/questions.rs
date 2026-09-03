use axum::{
    extract::{Path, Query, State},
    http::StatusCode,
    Json,
};
use crate::content_loader::SharedStore;
use crate::models::Question;
use serde::Deserialize;

#[derive(Debug, Deserialize)]
pub struct QuestionQuery {
    pub difficulty: Option<String>,
    pub limit: Option<usize>,
    pub offset: Option<usize>,
}

#[utoipa::path(
    get,
    path = "/api/categories/{category_id}/questions",
    params(
        ("category_id" = String, Path, description = "Category ID"),
        ("difficulty" = Option<String>, Query, description = "Filter by difficulty: Beginner, Intermediate, Advanced"),
        ("limit" = Option<usize>, Query, description = "Number of questions to return (default: 100)"),
        ("offset" = Option<usize>, Query, description = "Pagination offset")
    ),
    responses(
        (status = 200, description = "List of questions for the specified category", body = Vec<Question>),
        (status = 404, description = "Category not found")
    ),
    tag = "Questions"
)]
pub async fn get_questions_by_category(
    State(store): State<SharedStore>,
    Path(category_id): Path<String>,
    Query(query): Query<QuestionQuery>,
) -> Result<Json<Vec<Question>>, StatusCode> {
    let r = store.read().await;
    let questions = r.questions.get(&category_id).ok_or(StatusCode::NOT_FOUND)?;

    let mut filtered: Vec<Question> = questions
        .iter()
        .filter(|q| {
            if let Some(diff) = &query.difficulty {
                q.difficulty.eq_ignore_ascii_case(diff)
            } else {
                true
            }
        })
        .cloned()
        .collect();

    let offset = query.offset.unwrap_or(0);
    if offset < filtered.len() {
        filtered = filtered.split_off(offset);
    } else {
        filtered.clear();
    }

    let limit = query.limit.unwrap_or(100);
    filtered.truncate(limit);

    Ok(Json(filtered))
}

#[utoipa::path(
    get,
    path = "/api/categories/{category_id}/questions/{q_num}",
    params(
        ("category_id" = String, Path, description = "Category ID"),
        ("q_num" = i32, Path, description = "Question number (1-100)")
    ),
    responses(
        (status = 200, description = "Single question details", body = Question),
        (status = 404, description = "Question not found")
    ),
    tag = "Questions"
)]
pub async fn get_single_question(
    State(store): State<SharedStore>,
    Path((category_id, q_num)): Path<(String, i32)>,
) -> Result<Json<Question>, StatusCode> {
    let r = store.read().await;
    let questions = r.questions.get(&category_id).ok_or(StatusCode::NOT_FOUND)?;

    questions
        .iter()
        .find(|q| q.question_number == q_num)
        .cloned()
        .map(Json)
        .ok_or(StatusCode::NOT_FOUND)
}
