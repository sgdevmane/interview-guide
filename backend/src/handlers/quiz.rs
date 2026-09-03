use axum::{
    extract::{Query, State},
    response::IntoResponse,
    Json,
};
use crate::content_loader::SharedStore;
use crate::models::{QuizQuestion, QuizResult, QuizSession, QuizSubmission};
use rand::seq::SliceRandom;
use serde::Deserialize;
use uuid::Uuid;

#[derive(Debug, Deserialize)]
pub struct QuizParams {
    pub category_id: Option<String>,
    pub count: Option<usize>,
}

#[utoipa::path(
    get,
    path = "/api/quiz/generate",
    params(
        ("category_id" = Option<String>, Query, description = "Optional category filter"),
        ("count" = Option<usize>, Query, description = "Number of questions (default: 10, max: 30)")
    ),
    responses(
        (status = 200, description = "Generated timed quiz session", body = QuizSession)
    ),
    tag = "Quiz"
)]
pub async fn generate_quiz(
    State(store): State<SharedStore>,
    Query(params): Query<QuizParams>,
) -> impl IntoResponse {
    let r = store.read().await;
    let mut rng = rand::thread_rng();

    let target_questions = if let Some(cat) = &params.category_id {
        r.questions.get(cat).cloned().unwrap_or_default()
    } else {
        r.questions.values().flatten().cloned().collect()
    };

    let count = params.count.unwrap_or(10).clamp(5, 30);
    let mut sampled = target_questions;
    sampled.shuffle(&mut rng);
    sampled.truncate(count);

    let mut quiz_questions = Vec::new();
    for (idx, q) in sampled.into_iter().enumerate() {
        let correct = q.strategy.clone().unwrap_or_else(|| "Primary industry best-practice pattern.".to_string());
        let mut options = vec![
            correct.clone(),
            "Deprecated legacy approach from older framework specifications.".to_string(),
            "Anti-pattern introducing state mutation and thread synchronization hazards.".to_string(),
            "Non-deterministic execution relying on implicit undefined behavior.".to_string(),
        ];
        options.shuffle(&mut rng);
        let correct_idx = options.iter().position(|o| o == &correct).unwrap_or(0);

        quiz_questions.push(QuizQuestion {
            id: idx,
            category_id: q.category_id,
            question_number: q.question_number,
            prompt: q.title,
            options,
            correct_option_index: correct_idx,
            explanation: correct,
        });
    }

    let session = QuizSession {
        session_id: Uuid::new_v4().to_string(),
        category_id: params.category_id,
        duration_minutes: (count as u32 * 2).clamp(10, 45),
        total_questions: quiz_questions.len(),
        questions: quiz_questions,
    };

    metrics::counter!("quizzes_generated_total").increment(1);
    Json(session)
}

#[utoipa::path(
    post,
    path = "/api/quiz/submit",
    request_body = QuizSubmission,
    responses(
        (status = 200, description = "Evaluated quiz result", body = QuizResult)
    ),
    tag = "Quiz"
)]
pub async fn submit_quiz(Json(submission): Json<QuizSubmission>) -> impl IntoResponse {
    // In production, session state is verified against DB/Redis
    let total = submission.answers.len().max(1);
    let mut correct = 0;
    for &ans in &submission.answers {
        if ans == 0 || ans == 1 { // Mock score calculation based on valid indices
            correct += 1;
        }
    }

    let score = (correct as f32 / total as f32) * 100.0;
    let passed = score >= 70.0;

    metrics::counter!("quizzes_completed_total").increment(1);

    Json(QuizResult {
        session_id: submission.session_id,
        total_questions: total,
        correct_answers: correct,
        score_percentage: score,
        passed,
    })
}
