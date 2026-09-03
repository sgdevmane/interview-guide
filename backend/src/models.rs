use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use utoipa::ToSchema;

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct Category {
    pub id: String,
    pub name: String,
    pub description: String,
    pub icon_path: String,
    pub total_questions: i32,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct Question {
    pub id: String,
    pub category_id: String,
    pub question_number: i32,
    pub title: String,
    pub difficulty: String,
    pub strategy: Option<String>,
    pub answer_markdown: String,
    pub code_example: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct SearchResult {
    pub question: Question,
    pub match_field: String,
    pub score: f32,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct BookmarkRequest {
    pub user_id: Option<String>,
    pub category_id: String,
    pub question_number: i32,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct BookmarkItem {
    pub id: String,
    pub category_id: String,
    pub question_number: i32,
    pub created_at: DateTime<Utc>,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct NoteRequest {
    pub user_id: Option<String>,
    pub category_id: String,
    pub question_number: i32,
    pub note_content: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct NoteItem {
    pub id: String,
    pub category_id: String,
    pub question_number: i32,
    pub note_content: String,
    pub updated_at: DateTime<Utc>,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct SpacedRepetitionReviewRequest {
    pub category_id: String,
    pub question_number: i32,
    /// Rating: 1 = Again, 2 = Hard, 3 = Good, 4 = Easy
    pub rating: u8,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct SpacedRepetitionItem {
    pub category_id: String,
    pub question_number: i32,
    pub interval_days: u32,
    pub repetitions: u32,
    pub ease_factor: f32,
    pub next_review: DateTime<Utc>,
    pub status: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct QuizQuestion {
    pub id: usize,
    pub category_id: String,
    pub question_number: i32,
    pub prompt: String,
    pub options: Vec<String>,
    pub correct_option_index: usize,
    pub explanation: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct QuizSession {
    pub session_id: String,
    pub category_id: Option<String>,
    pub duration_minutes: u32,
    pub total_questions: usize,
    pub questions: Vec<QuizQuestion>,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct QuizSubmission {
    pub session_id: String,
    /// User answers indexed by question id
    pub answers: Vec<usize>,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct QuizResult {
    pub session_id: String,
    pub total_questions: usize,
    pub correct_answers: usize,
    pub score_percentage: f32,
    pub passed: bool,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct SimpleStatusResponse {
    pub success: bool,
    pub message: String,
}
