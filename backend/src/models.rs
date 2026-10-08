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

// ==============================================================================
// Authentication
// ==============================================================================
#[derive(Debug, Clone, Deserialize, ToSchema)]
pub struct RegisterRequest {
    pub email: String,
    pub password: String,
    pub full_name: String,
}

#[derive(Debug, Clone, Deserialize, ToSchema)]
pub struct LoginRequest {
    pub email: String,
    pub password: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct UserProfile {
    pub id: String,
    pub email: String,
    pub full_name: Option<String>,
    pub role: String,
    pub created_at: DateTime<Utc>,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct AuthResponse {
    pub access_token: String,
    pub token_type: String,
    /// Access token lifetime in seconds. Refresh via `POST /api/auth/refresh` (HTTP-only cookie).
    pub expires_in: i64,
    pub user: UserProfile,
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

// ==============================================================================
// SM-18 Spaced Repetition Models
// ==============================================================================
#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct Sm18ReviewRequest {
    pub category_id: String,
    pub question_number: i32,
    /// Recall grade: 0 (blackout) to 5 (flawless)
    pub grade: u8,
    /// Estimated difficulty from candidate (1 to 10)
    pub difficulty_factor: Option<f32>,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct Sm18Item {
    pub category_id: String,
    pub question_number: i32,
    pub stability: f32,
    pub retrievability: f32,
    pub difficulty: f32,
    pub repetitions: u32,
    pub interval_days: u32,
    pub next_review: DateTime<Utc>,
    pub status: String,
}

// ==============================================================================
// Daily Challenge & Company Tracks
// ==============================================================================
#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct DailyChallengeResponse {
    pub date: String,
    pub question: Question,
    pub streak_count: u32,
    pub multiplier: f32,
    pub elo_rating: u32,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct CompanyTrackItem {
    pub id: String,
    pub company_name: String,
    pub description: String,
    pub difficulty: String,
    pub target_roles: Vec<String>,
    pub total_questions: usize,
    pub questions: Vec<Question>,
}

// ==============================================================================
// B2B Recruiter Assessments & Candidate Verification
// ==============================================================================
#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct RecruiterAssessmentRequest {
    pub recruiter_email: String,
    pub title: String,
    pub target_role: String,
    pub duration_minutes: u32,
    pub categories: Vec<String>,
    pub question_count: usize,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct RecruiterAssessment {
    pub id: String,
    pub token: String,
    pub recruiter_email: String,
    pub title: String,
    pub target_role: String,
    pub duration_minutes: u32,
    pub categories: Vec<String>,
    pub question_count: usize,
    pub is_active: bool,
    pub created_at: DateTime<Utc>,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct RecruiterSubmissionRequest {
    pub token: String,
    pub candidate_name: String,
    pub candidate_email: String,
    pub answers: Vec<usize>,
    pub tab_blur_count: u32,
    pub full_screen_exit_count: u32,
    pub duration_seconds: u32,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct RecruiterSubmissionResult {
    pub submission_id: String,
    pub candidate_name: String,
    pub candidate_email: String,
    pub score_percentage: f32,
    pub passed: bool,
    pub tab_blur_count: u32,
    pub anti_cheat_status: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct AssessmentAuditLogRequest {
    pub token: String,
    pub candidate_email: String,
    pub event_type: String,
    pub payload: serde_json::Value,
}

// ==============================================================================
// Candidate Certificates (Cryptographically Signed)
// ==============================================================================
#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct CandidateCertificateRequest {
    pub candidate_name: String,
    pub candidate_email: String,
    pub score_percentage: f32,
    pub domains_mastered: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct CandidateCertificate {
    pub certificate_number: String,
    pub candidate_name: String,
    pub candidate_email: String,
    pub score_percentage: f32,
    pub domains_mastered: Vec<String>,
    pub signature_sha256: String,
    pub issued_at: DateTime<Utc>,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct CertificateVerificationResult {
    pub is_valid: bool,
    pub certificate: Option<CandidateCertificate>,
    pub message: String,
}

// ==============================================================================
// ATS Integrations (Greenhouse, Lever, Ashby)
// ==============================================================================
#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct AtsWebhookPayload {
    pub provider: String,
    pub candidate_email: String,
    pub candidate_name: String,
    pub job_id: Option<String>,
    pub score_percentage: f32,
    pub assessment_title: String,
    pub certificate_url: Option<String>,
}

// ==============================================================================
// Global Leaderboard & Competitive Elo Models
// ==============================================================================
#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct LeaderboardEntry {
    pub username: String,
    pub elo_rating: i32,
    pub tier: String,
    pub battles_won: i32,
    pub battles_lost: i32,
    pub questions_solved: i32,
    pub updated_at: DateTime<Utc>,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct UpdateLeaderboardRequest {
    pub username: String,
    pub elo_delta: i32,
    pub won: bool,
}

// ==============================================================================
// Real-Time P2P Coding Battle Models
// ==============================================================================
#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct CreateBattleRequest {
    pub category_id: String,
    pub question_number: i32,
    pub host_username: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct JoinBattleRequest {
    pub battle_token: String,
    pub peer_username: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct CodingBattle {
    pub battle_token: String,
    pub category_id: String,
    pub question_number: i32,
    pub host_username: String,
    pub peer_username: Option<String>,
    pub winner_username: Option<String>,
    pub status: String,
    pub created_at: DateTime<Utc>,
}

// ==============================================================================
// Custom Curated Decks Models
// ==============================================================================
#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct CreateCustomDeckRequest {
    pub user_id: String,
    pub title: String,
    pub description: Option<String>,
    pub tags: Vec<String>,
    pub question_ids: Vec<String>,
    pub is_public: bool,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct CustomDeck {
    pub id: String,
    pub user_id: String,
    pub title: String,
    pub description: Option<String>,
    pub tags: Vec<String>,
    pub total_questions: usize,
    pub is_public: bool,
    pub created_at: DateTime<Utc>,
}

// ==============================================================================
// Keystroke Dynamics Biometric Models
// ==============================================================================
#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct KeystrokeAnalysisRequest {
    pub submission_id: String,
    pub flight_time_avg_ms: f32,
    pub dwell_time_avg_ms: f32,
    pub entropy_score: f32,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct KeystrokeAnalysisResponse {
    pub submission_id: String,
    pub is_biometrically_consistent: bool,
    pub entropy_score: f32,
    pub anomaly_flag: Option<String>,
}

// ==============================================================================
// W3C-Compatible Verifiable Credentials
// ==============================================================================
#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct IssueVerifiableCredentialRequest {
    pub candidate_did: String,
    pub candidate_name: String,
    pub certificate_number: String,
    pub track_title: String,
    pub score_percentage: f32,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct VerifiableCredentialResponse {
    pub credential_id: String,
    pub candidate_did: String,
    pub issuer_did: String,
    pub certificate_number: String,
    pub proof_signature: String,
    pub claim_data: serde_json::Value,
    pub issued_at: DateTime<Utc>,
}

// ==============================================================================
// Daily Streak Freeze Models
// ==============================================================================
#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct StreakFreezeResponse {
    pub user_id: String,
    pub available_freezes: i32,
    pub used_freezes: i32,
    pub last_freeze_applied_at: Option<DateTime<Utc>>,
    pub success: bool,
    pub message: String,
}

// ==============================================================================
// WebAuthn / Passkey Models (Item #39)
// ==============================================================================
#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct PasskeyRegisterStartResponse {
    pub challenge_id: String,
    pub public_key_credential_creation_options: serde_json::Value,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct PasskeyRegisterFinishRequest {
    pub challenge_id: String,
    pub credential: serde_json::Value,
    pub nickname: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct PasskeyLoginStartRequest {
    pub email: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct PasskeyLoginStartResponse {
    pub challenge_id: String,
    pub public_key_credential_request_options: serde_json::Value,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct PasskeyLoginFinishRequest {
    pub challenge_id: String,
    pub credential: serde_json::Value,
}

// ==============================================================================
// Append-Only Tamper-Evident Audit Ledger Models (Item #44)
// ==============================================================================
#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct AuditVerificationResponse {
    pub is_valid: bool,
    pub total_records: i64,
    pub broken_sequence_id: Option<i64>,
    pub message: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct AuditEventItem {
    pub sequence_id: i64,
    pub event_type: String,
    pub actor_id: Option<String>,
    pub target_id: Option<String>,
    pub payload_json: serde_json::Value,
    pub prev_hash: String,
    pub curr_hash: String,
    pub created_at: DateTime<Utc>,
}

// ==============================================================================
// SM-18 Spaced Repetition Models (Item #11)
// ==============================================================================

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct Sm18ReviewResponse {
    pub category_id: String,
    pub question_number: i32,
    pub repetition: u32,
    pub interval_days: u32,
    pub stability: f32,
    pub retrievability: f32,
    pub difficulty: f32,
    pub next_review_at: DateTime<Utc>,
}

// ==============================================================================
// Item Response Theory (IRT) Adaptive Difficulty Models (Item #37)
// ==============================================================================
#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct IrtAdaptiveQuestionResponse {
    pub category_id: String,
    pub question_number: i32,
    pub user_theta_ability: f32,
    pub question_difficulty_beta: f32,
    pub discrimination_alpha: f32,
    pub title: String,
    pub target_competency: String,
}

// ==============================================================================
// Shareable Custom Decks Models (Item #14)
// ==============================================================================
#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct ShareDeckRequest {
    pub title: String,
    pub description: Option<String>,
    pub category_id: Option<String>,
    pub question_ids: Vec<String>,
    pub is_public: bool,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct ShareDeckResponse {
    pub deck_id: String,
    pub title: String,
    pub share_code: String,
    pub question_count: usize,
    pub share_url: String,
    pub created_at: DateTime<Utc>,
}

// ==============================================================================
// Web Push Subscription Models (Item #15)
// ==============================================================================
#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct PushSubscriptionRequest {
    pub endpoint: String,
    pub p256dh: String,
    pub auth: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct PushSubscriptionResponse {
    pub id: String,
    pub endpoint: String,
    pub created_at: DateTime<Utc>,
    pub message: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct PushNotificationTestRequest {
    pub title: Option<String>,
    pub body: Option<String>,
    pub url: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct PushNotificationTestResponse {
    pub success: bool,
    pub dispatched_count: usize,
    pub message: String,
}

// ==============================================================================
// Timed Contests Models (Item #12)
// ==============================================================================
#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct TimedContestItem {
    pub id: String,
    pub contest_code: String,
    pub title: String,
    pub description: Option<String>,
    pub difficulty: String,
    pub category: Option<String>,
    pub start_time: DateTime<Utc>,
    pub duration_minutes: i32,
    pub participant_count: i64,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct JoinContestRequest {
    pub contest_code: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct SubmitContestRequest {
    pub contest_code: String,
    pub score: i32,
    pub time_taken_seconds: i32,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct ContestParticipantResponse {
    pub contest_id: String,
    pub contest_code: String,
    pub user_id: String,
    pub score: i32,
    pub time_taken_seconds: i32,
    pub rank: i64,
    pub finished: bool,
}

// ==============================================================================
// Platform Webhook Models (Item #13)
// ==============================================================================
#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct CreateWebhookRequest {
    pub service_name: String,
    pub webhook_url: String,
    pub events_subscribed: Option<Vec<String>>,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct WebhookItemResponse {
    pub id: String,
    pub service_name: String,
    pub webhook_url: String,
    pub events_subscribed: Vec<String>,
    pub is_active: bool,
    pub created_at: DateTime<Utc>,
}

#[derive(Debug, Clone, Serialize, Deserialize, ToSchema)]
pub struct TestWebhookRequest {
    pub webhook_id: String,
}



