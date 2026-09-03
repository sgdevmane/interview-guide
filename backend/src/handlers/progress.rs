use axum::{response::IntoResponse, Json};
use chrono::{Duration, Utc};
use crate::models::{SpacedRepetitionItem, SpacedRepetitionReviewRequest};

#[utoipa::path(
    post,
    path = "/api/progress/review",
    request_body = SpacedRepetitionReviewRequest,
    responses(
        (status = 200, description = "Updated SM-2 spaced repetition state", body = SpacedRepetitionItem)
    ),
    tag = "Spaced Repetition"
)]
pub async fn record_review(
    Json(req): Json<SpacedRepetitionReviewRequest>,
) -> impl IntoResponse {
    let q_score = req.rating.clamp(1, 5) as f32;
    
    // Default initial SM-2 values
    let mut ease_factor: f32 = 2.5;
    let mut repetitions: u32 = 1;
    let mut interval_days: u32 = 1;

    // Calculate updated ease factor
    ease_factor = ease_factor + (0.1 - (5.0 - q_score) * (0.08 + (5.0 - q_score) * 0.02));
    if ease_factor < 1.3 {
        ease_factor = 1.3;
    }

    if q_score < 3.0 {
        repetitions = 0;
        interval_days = 1;
    } else {
        repetitions += 1;
        interval_days = match repetitions {
            1 => 1,
            2 => 6,
            _ => ((interval_days as f32) * ease_factor).round() as u32,
        };
    }

    let next_review = Utc::now() + Duration::days(interval_days as i64);
    let status = if interval_days > 21 {
        "mastered"
    } else if repetitions > 0 {
        "learning"
    } else {
        "needs_review"
    };

    metrics::counter!("spaced_repetition_reviews_total").increment(1);

    Json(SpacedRepetitionItem {
        category_id: req.category_id,
        question_number: req.question_number,
        interval_days,
        repetitions,
        ease_factor,
        next_review,
        status: status.to_string(),
    })
}
