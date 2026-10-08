mod audit;
mod auth;
mod cache;
mod content_loader;
mod db;
mod error;
mod handlers;
mod models;
mod webauthn;

use axum::{
    extract::{Request, State},
    http::{header, HeaderValue, StatusCode},
    middleware::{self, Next},
    response::Response,
    routing::{get, post},
    Router,
};
use content_loader::load_content_from_markdowns;
use handlers::{
    audit::{list_events, verify_chain},
    auth::{login, logout, me, refresh, register},
    bookmarks::{get_bookmarks, toggle_bookmark, BookmarkStore},
    categories::{get_all_categories, get_category_by_id},
    enterprise::{
        analyze_keystroke_dynamics, ats_webhook_sync, create_recruiter_assessment,
        get_assessment_by_token, issue_candidate_certificate, issue_verifiable_credential,
        log_audit_event, submit_assessment, verify_candidate_certificate,
        verify_verifiable_credential,
    },
    gamification::{
        apply_streak_freeze, create_coding_battle, create_custom_deck, get_company_tracks,
        get_daily_challenge, get_leaderboard, join_coding_battle, record_sm18_review,
        update_leaderboard,
    },
    learning::{get_adaptive_next_question, get_shared_deck, persist_sm18_review, share_deck},
    notifications::{
        create_webhook, list_webhooks, subscribe_push, test_push_notification, test_webhook,
    },
    contests::{contest_leaderboard, join_contest, list_contests, submit_contest},
    notes::{get_notes, save_note, NoteStore},
    progress::record_review,
    questions::{get_questions_by_category, get_single_question},
    quiz::{generate_quiz, submit_quiz},
    search::search_handler,
    webauthn::{login_finish, login_start, register_finish, register_start, WebAuthnState},
};
use metrics_exporter_prometheus::PrometheusBuilder;
use std::{
    env,
    net::SocketAddr,
    path::Path,
    sync::Arc,
};
use tokio::sync::RwLock;
use tower_http::cors::{Any, CorsLayer};
use tower_http::trace::TraceLayer;
use tracing_subscriber::{layer::SubscriberExt, util::SubscriberInitExt};
use utoipa::OpenApi;
use utoipa_swagger_ui::SwaggerUi;

/// Strict Security Headers & CSP Middleware (Item #45)
async fn security_headers_middleware(req: Request, next: Next) -> Response {
    let mut response = next.run(req).await;
    let headers = response.headers_mut();

    headers.insert(header::X_CONTENT_TYPE_OPTIONS, HeaderValue::from_static("nosniff"));
    headers.insert(header::X_FRAME_OPTIONS, HeaderValue::from_static("DENY"));
    headers.insert(header::X_XSS_PROTECTION, HeaderValue::from_static("1; mode=block"));
    headers.insert(
        header::REFERRER_POLICY,
        HeaderValue::from_static("strict-origin-when-cross-origin"),
    );
    headers.insert(
        header::CONTENT_SECURITY_POLICY,
        HeaderValue::from_static(
            "default-src 'self'; script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com; style-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com; img-src 'self' data: https:; font-src 'self' https://cdnjs.cloudflare.com; connect-src 'self'; frame-ancestors 'none';"
        ),
    );
    response
}

/// Distributed Sliding-Window Rate Limiter Middleware (Item #41)
async fn distributed_rate_limiter_middleware(
    State(limiter): State<cache::DistributedRateLimiter>,
    req: Request,
    next: Next,
) -> Result<Response, StatusCode> {
    let client_ip = req
        .headers()
        .get("x-forwarded-for")
        .and_then(|h| h.to_str().ok())
        .unwrap_or("127.0.0.1")
        .to_string();

    // Limit to 120 requests per 60 seconds across cluster instances
    if limiter.check_rate_limit(&client_ip, 120, 60).await {
        Ok(next.run(req).await)
    } else {
        metrics::counter!("rate_limit_exceeded_total").increment(1);
        Err(StatusCode::TOO_MANY_REQUESTS)
    }
}

#[derive(OpenApi)]
#[openapi(
    paths(
        handlers::categories::get_all_categories,
        handlers::categories::get_category_by_id,
        handlers::questions::get_questions_by_category,
        handlers::questions::get_single_question,
        handlers::search::search_handler,
        handlers::quiz::generate_quiz,
        handlers::quiz::submit_quiz,
        handlers::progress::record_review,
        handlers::bookmarks::get_bookmarks,
        handlers::bookmarks::toggle_bookmark,
        handlers::notes::get_notes,
        handlers::notes::save_note,
        handlers::auth::register,
        handlers::auth::login,
        handlers::auth::refresh,
        handlers::auth::logout,
        handlers::auth::me,
        handlers::webauthn::register_start,
        handlers::webauthn::register_finish,
        handlers::webauthn::login_start,
        handlers::webauthn::login_finish,
        handlers::audit::verify_chain,
        handlers::audit::list_events,
        handlers::learning::persist_sm18_review,
        handlers::learning::get_adaptive_next_question,
        handlers::learning::share_deck,
        handlers::learning::get_shared_deck,
        handlers::gamification::record_sm18_review,
        handlers::gamification::get_daily_challenge,
        handlers::gamification::get_company_tracks,
        handlers::gamification::get_leaderboard,
        handlers::gamification::update_leaderboard,
        handlers::gamification::create_coding_battle,
        handlers::gamification::join_coding_battle,
        handlers::gamification::create_custom_deck,
        handlers::gamification::apply_streak_freeze,
        handlers::enterprise::create_recruiter_assessment,
        handlers::enterprise::get_assessment_by_token,
        handlers::enterprise::submit_assessment,
        handlers::enterprise::log_audit_event,
        handlers::enterprise::issue_candidate_certificate,
        handlers::enterprise::verify_candidate_certificate,
        handlers::enterprise::ats_webhook_sync,
        handlers::enterprise::analyze_keystroke_dynamics,
        handlers::enterprise::issue_verifiable_credential,
        handlers::enterprise::verify_verifiable_credential,
        handlers::notifications::subscribe_push,
        handlers::notifications::test_push_notification,
        handlers::notifications::list_webhooks,
        handlers::notifications::create_webhook,
        handlers::notifications::test_webhook,
        handlers::contests::list_contests,
        handlers::contests::join_contest,
        handlers::contests::submit_contest,
        handlers::contests::contest_leaderboard,
    ),
    components(
        schemas(
            models::Category,
            models::Question,
            models::SearchResult,
            models::QuizSession,
            models::QuizQuestion,
            models::QuizSubmission,
            models::QuizResult,
            models::SpacedRepetitionItem,
            models::SpacedRepetitionReviewRequest,
            models::Sm18Item,
            models::Sm18ReviewRequest,
            models::Sm18ReviewResponse,
            models::IrtAdaptiveQuestionResponse,
            models::ShareDeckRequest,
            models::ShareDeckResponse,
            models::DailyChallengeResponse,
            models::CompanyTrackItem,
            models::RecruiterAssessment,
            models::RecruiterAssessmentRequest,
            models::RecruiterSubmissionRequest,
            models::RecruiterSubmissionResult,
            models::AssessmentAuditLogRequest,
            models::CandidateCertificate,
            models::CandidateCertificateRequest,
            models::CertificateVerificationResult,
            models::AtsWebhookPayload,
            models::BookmarkItem,
            models::BookmarkRequest,
            models::NoteItem,
            models::NoteRequest,
            models::RegisterRequest,
            models::LoginRequest,
            models::UserProfile,
            models::AuthResponse,
            models::PasskeyRegisterStartResponse,
            models::PasskeyRegisterFinishRequest,
            models::PasskeyLoginStartRequest,
            models::PasskeyLoginStartResponse,
            models::PasskeyLoginFinishRequest,
            models::AuditVerificationResponse,
            models::AuditEventItem,
            error::ErrorBody,
            models::SimpleStatusResponse,
            models::LeaderboardEntry,
            models::UpdateLeaderboardRequest,
            models::CodingBattle,
            models::CreateBattleRequest,
            models::JoinBattleRequest,
            models::CustomDeck,
            models::CreateCustomDeckRequest,
            models::KeystrokeAnalysisRequest,
            models::KeystrokeAnalysisResponse,
            models::IssueVerifiableCredentialRequest,
            models::VerifiableCredentialResponse,
            models::StreakFreezeResponse,
            models::PushSubscriptionRequest,
            models::PushSubscriptionResponse,
            models::PushNotificationTestRequest,
            models::PushNotificationTestResponse,
            models::TimedContestItem,
            models::JoinContestRequest,
            models::SubmitContestRequest,
            models::ContestParticipantResponse,
            models::CreateWebhookRequest,
            models::WebhookItemResponse,
            models::TestWebhookRequest,
        )
    ),
    tags(
        (name = "Authentication", description = "Authentication, JWT sessions & WebAuthn / Passkeys"),
        (name = "Categories", description = "Interview question categories"),
        (name = "Questions", description = "Interview questions and answers"),
        (name = "Search", description = "Instant full-text search"),
        (name = "Quiz", description = "Mock interview quizzes"),
        (name = "Spaced Repetition", description = "SM-2 and SM-18 spaced-repetition intervals"),
        (name = "Progress", description = "User progress & Item Response Theory (IRT) adaptive recommendation"),
        (name = "Gamification", description = "Daily challenge and company target tracks"),
        (name = "Enterprise", description = "Recruiter screening assessments, certificates, audit ledger & ATS sync"),
        (name = "Bookmarks", description = "Saved questions management"),
        (name = "Notes", description = "Custom candidate study notes"),
        (name = "Notifications", description = "Web Push notifications and daily streak review alerts"),
        (name = "Competitive", description = "Timed challenges, contests, and Elo ranked leaderboards"),
        (name = "Integrations", description = "Slack and Discord outbound webhooks")
    ),
    info(
        title = "Interview Guide Platform API",
        version = "2.0.0",
        description = "High-performance Rust Axum API for Interview Guide & Technical Knowledge Platform"
    )
)]
struct ApiDoc;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args: Vec<String> = env::args().collect();
    if args.len() > 1 && args[1] == "--export-openapi" {
        println!("{}", ApiDoc::openapi().to_pretty_json()?);
        return Ok(());
    }

    tracing_subscriber::registry()
        .with(tracing_subscriber::EnvFilter::try_from_default_env().unwrap_or_else(|_| "info".into()))
        .with(tracing_subscriber::fmt::layer())
        .init();

    // Initialize JWT Authentication Configuration
    auth::init_auth_config();

    // Initialize Prometheus Recorder
    let recorder_handle = PrometheusBuilder::new()
        .install_recorder()
        .expect("Failed to install Prometheus recorder");

    // Load content store from markdowns directory
    let md_path = env::var("MARKDOWNS_DIR").unwrap_or_else(|_| "../markdowns".to_string());
    tracing::info!("Loading interview questions from: {}", md_path);
    let store_data = load_content_from_markdowns(Path::new(&md_path));
    tracing::info!(
        "Loaded {} categories with {} total questions",
        store_data.categories.len(),
        store_data.questions.values().map(|v| v.len()).sum::<usize>()
    );

    // Load database configuration
    if env::var("DATABASE_URL").is_err() {
        for env_path in &["../.env.local", ".env.local", "../.env.staging", ".env.staging", "../.env", ".env"] {
            if let Ok(content) = std::fs::read_to_string(env_path) {
                for line in content.lines() {
                    let line = line.trim();
                    if let Some(stripped) = line.strip_prefix("DATABASE_URL=") {
                        let url = stripped.trim_matches('"').trim_matches('\'').trim();
                        if !url.is_empty() {
                            env::set_var("DATABASE_URL", url);
                            break;
                        }
                    }
                }
                if env::var("DATABASE_URL").is_ok() {
                    break;
                }
            }
        }
    }

    let db_pool = if let Ok(db_url) = env::var("DATABASE_URL") {
        db::connect_db(&db_url).await
    } else {
        None
    };

    // Initialize Distributed Cache & Rate Limiter (Redis / Memory)
    let redis_url = env::var("REDIS_URL").ok();
    let cache_client = cache::CacheClient::new(redis_url).await;
    let distributed_rate_limiter = cache::DistributedRateLimiter::new(&cache_client);

    let shared_store = Arc::new(RwLock::new(store_data));
    let bookmark_store = BookmarkStore::new(db_pool.clone());
    let note_store = NoteStore::new(db_pool.clone());

    let cors = CorsLayer::new()
        .allow_origin(Any)
        .allow_methods(Any)
        .allow_headers(Any);

    // Auth Routes
    let auth_routes = Router::new()
        .route("/auth/register", post(register))
        .route("/auth/login", post(login))
        .route("/auth/refresh", post(refresh))
        .route("/auth/logout", post(logout))
        .route("/auth/me", get(me));

    // WebAuthn Routes (Item #39)
    let webauthn_router = if let Some(ref pool) = db_pool {
        let rp_id = env::var("WEBAUTHN_RP_ID").unwrap_or_else(|_| "localhost".to_string());
        let rp_origin = env::var("WEBAUTHN_RP_ORIGIN")
            .unwrap_or_else(|_| "http://localhost:8080".to_string());

        match webauthn::WebAuthnService::new(&rp_id, &rp_origin) {
            Ok(service) => {
                let state = WebAuthnState {
                    pool: pool.clone(),
                    webauthn: service,
                };
                Router::new()
                    .route("/auth/webauthn/register/start", post(register_start))
                    .route("/auth/webauthn/register/finish", post(register_finish))
                    .route("/auth/webauthn/login/start", post(login_start))
                    .route("/auth/webauthn/login/finish", post(login_finish))
                    .with_state(state)
            }
            Err(err) => {
                tracing::warn!("WebAuthn disabled: {}", err);
                Router::new()
            }
        }
    } else {
        Router::new()
    };

    // Shared Markdown Content Routes
    let shared_store_routes = Router::new()
        .route("/categories", get(get_all_categories))
        .route("/categories/:id", get(get_category_by_id))
        .route("/categories/:category_id/questions", get(get_questions_by_category))
        .route("/categories/:category_id/questions/:q_num", get(get_single_question))
        .route("/search", get(search_handler))
        .route("/quiz/generate", get(generate_quiz))
        .route("/quiz/submit", post(submit_quiz))
        .route("/gamification/daily-challenge", get(get_daily_challenge))
        .route("/gamification/company-tracks", get(get_company_tracks))
        .with_state(shared_store);

    // Audit Ledger, Learning, Notifications & Contests Routes (Items #44, #11, #37, #14, #15, #13, #12)
    let pool_backed_routes = if let Some(ref pool) = db_pool {
        Router::new()
            .route("/audit/verify", get(verify_chain))
            .route("/audit/events", get(list_events))
            .route("/study/sm18/review", post(persist_sm18_review))
            .route("/study/adaptive-next", get(get_adaptive_next_question))
            .route("/decks/share", post(share_deck))
            .route("/decks/shared/:share_code", get(get_shared_deck))
            .route("/notifications/subscribe", post(subscribe_push))
            .route("/notifications/test", post(test_push_notification))
            .route("/webhooks", get(list_webhooks).post(create_webhook))
            .route("/webhooks/test", post(test_webhook))
            .route("/contests", get(list_contests))
            .route("/contests/join", post(join_contest))
            .route("/contests/submit", post(submit_contest))
            .route("/contests/:contest_code/leaderboard", get(contest_leaderboard))
            .with_state(pool.clone())
    } else {
        Router::new()
    };

    let stateless_routes = Router::new()
        .route("/health", get(|| std::future::ready("OK")))
        .route("/progress/review", post(record_review))
        .route("/gamification/sm18/review", post(record_sm18_review))
        .route("/gamification/leaderboard", get(get_leaderboard))
        .route("/gamification/leaderboard/update", post(update_leaderboard))
        .route("/gamification/battles/create", post(create_coding_battle))
        .route("/gamification/battles/join", post(join_coding_battle))
        .route("/gamification/decks", post(create_custom_deck))
        .route("/gamification/streak/freeze", post(apply_streak_freeze))
        .route("/enterprise/assessments/create", post(create_recruiter_assessment))
        .route("/enterprise/assessments/:token", get(get_assessment_by_token))
        .route("/enterprise/assessments/submit", post(submit_assessment))
        .route("/enterprise/assessments/keystrokes", post(analyze_keystroke_dynamics))
        .route("/enterprise/audit/log", post(log_audit_event))
        .route("/enterprise/certificates/issue", post(issue_candidate_certificate))
        .route("/enterprise/certificates/verify/:cert_number", get(verify_candidate_certificate))
        .route("/enterprise/credentials/issue", post(issue_verifiable_credential))
        .route("/enterprise/credentials/verify/:id", get(verify_verifiable_credential))
        .route("/enterprise/ats/webhook", post(ats_webhook_sync));

    let bookmark_routes = Router::new()
        .route("/bookmarks", get(get_bookmarks).post(toggle_bookmark))
        .with_state(bookmark_store);

    let note_routes = Router::new()
        .route("/notes", get(get_notes).post(save_note))
        .with_state(note_store);

    let api_routes = Router::new()
        .merge(auth_routes)
        .merge(webauthn_router)
        .merge(shared_store_routes)
        .merge(pool_backed_routes)
        .merge(stateless_routes)
        .merge(bookmark_routes)
        .merge(note_routes)
        .layer(middleware::from_fn_with_state(
            distributed_rate_limiter,
            distributed_rate_limiter_middleware,
        ));

    let recorder_for_metrics = recorder_handle.clone();
    let app = Router::new()
        .merge(SwaggerUi::new("/swagger-ui").url("/api-docs/openapi.json", ApiDoc::openapi()))
        .route("/metrics", get(move || std::future::ready(recorder_for_metrics.render())))
        .route("/health", get(|| std::future::ready("OK")))
        .nest("/api", api_routes)
        .layer(cors)
        .layer(TraceLayer::new_for_http())
        .layer(middleware::from_fn(security_headers_middleware));

    let port: u16 = env::var("PORT")
        .ok()
        .and_then(|p| p.parse().ok())
        .unwrap_or(8080);
    let addr = SocketAddr::from(([0, 0, 0, 0], port));

    tracing::info!("Server running on http://{}", addr);
    tracing::info!("Swagger UI available at http://{}/swagger-ui", addr);
    tracing::info!("Prometheus metrics at http://{}/metrics", addr);

    let listener = tokio::net::TcpListener::bind(addr).await?;
    axum::serve(listener, app)
        .with_graceful_shutdown(shutdown_signal())
        .await?;

    Ok(())
}

async fn shutdown_signal() {
    let ctrl_c = async {
        tokio::signal::ctrl_c()
            .await
            .expect("Failed to install Ctrl+C handler");
    };

    #[cfg(unix)]
    let terminate = async {
        tokio::signal::unix::signal(tokio::signal::unix::SignalKind::terminate())
            .expect("Failed to install signal handler")
            .recv()
            .await;
    };

    #[cfg(not(unix))]
    let terminate = std::future::pending::<()>();

    tokio::select! {
        _ = ctrl_c => {},
        _ = terminate => {},
    }

    tracing::info!("Shutdown signal received, draining active connections...");
}
