mod content_loader;
mod handlers;
mod models;

use axum::{
    extract::Request,
    http::StatusCode,
    middleware::{self, Next},
    response::Response,
    routing::{get, post},
    Router,
};
use content_loader::load_content_from_markdowns;
use handlers::{
    bookmarks::{get_bookmarks, toggle_bookmark, BookmarkStore},
    categories::{get_all_categories, get_category_by_id},
    notes::{get_notes, save_note, NoteStore},
    progress::record_review,
    questions::{get_questions_by_category, get_single_question},
    quiz::{generate_quiz, submit_quiz},
    search::search_handler,
};
use metrics_exporter_prometheus::PrometheusBuilder;
use std::{
    collections::HashMap,
    env,
    net::SocketAddr,
    path::Path,
    sync::Arc,
    time::{Duration, Instant},
};
use tokio::sync::RwLock;
use tower_http::cors::{Any, CorsLayer};
use tower_http::trace::TraceLayer;
use tracing_subscriber::{layer::SubscriberExt, util::SubscriberInitExt};
use utoipa::OpenApi;
use utoipa_swagger_ui::SwaggerUi;

#[derive(Clone, Default)]
struct RateLimiterState {
    clients: Arc<RwLock<HashMap<String, (Instant, u32)>>>,
}

async fn token_bucket_rate_limiter(
    state: axum::extract::State<RateLimiterState>,
    req: Request,
    next: Next,
) -> Result<Response, StatusCode> {
    let client_ip = req
        .headers()
        .get("x-forwarded-for")
        .and_then(|h| h.to_str().ok())
        .unwrap_or("127.0.0.1")
        .to_string();

    let now = Instant::now();
    let mut map = state.clients.write().await;
    let entry = map.entry(client_ip).or_insert((now, 100));

    // Refill tokens: 100 tokens max, replenishes every 1 second
    let elapsed = now.duration_since(entry.0);
    if elapsed >= Duration::from_secs(1) {
        entry.0 = now;
        entry.1 = 100;
    }

    if entry.1 > 0 {
        entry.1 -= 1;
        drop(map);
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
            models::BookmarkItem,
            models::BookmarkRequest,
            models::NoteItem,
            models::NoteRequest,
            models::SimpleStatusResponse,
        )
    ),
    tags(
        (name = "Categories", description = "Interview question categories"),
        (name = "Questions", description = "Interview questions and answers"),
        (name = "Search", description = "Instant full-text search"),
        (name = "Quiz", description = "Mock interview quizzes"),
        (name = "Spaced Repetition", description = "SM-2 Leitner spaced-repetition intervals"),
        (name = "Bookmarks", description = "Saved questions management"),
        (name = "Notes", description = "Custom candidate study notes")
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
    tracing_subscriber::registry()
        .with(tracing_subscriber::EnvFilter::try_from_default_env().unwrap_or_else(|_| "info".into()))
        .with(tracing_subscriber::fmt::layer())
        .init();

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

    let shared_store = Arc::new(RwLock::new(store_data));
    let bookmark_store: BookmarkStore = Arc::new(RwLock::new(Vec::new()));
    let note_store: NoteStore = Arc::new(RwLock::new(Vec::new()));
    let rate_limiter = RateLimiterState::default();

    let cors = CorsLayer::new()
        .allow_origin(Any)
        .allow_methods(Any)
        .allow_headers(Any);

    // API Routes
    let api_routes = Router::new()
        .route("/categories", get(get_all_categories))
        .route("/categories/:id", get(get_category_by_id))
        .route("/categories/:category_id/questions", get(get_questions_by_category))
        .route("/categories/:category_id/questions/:q_num", get(get_single_question))
        .route("/search", get(search_handler))
        .route("/quiz/generate", get(generate_quiz))
        .route("/quiz/submit", post(submit_quiz))
        .with_state(shared_store)
        .route("/progress/review", post(record_review))
        .route("/bookmarks", get(get_bookmarks).post(toggle_bookmark))
        .with_state(bookmark_store)
        .route("/notes", get(get_notes).post(save_note))
        .with_state(note_store)
        .layer(middleware::from_fn_with_state(rate_limiter, token_bucket_rate_limiter));

    let recorder_for_metrics = recorder_handle.clone();
    let app = Router::new()
        .merge(SwaggerUi::new("/swagger-ui").url("/api-docs/openapi.json", ApiDoc::openapi()))
        .route("/metrics", get(move || std::future::ready(recorder_for_metrics.render())))
        .route("/health", get(|| std::future::ready("OK")))
        .nest("/api", api_routes)
        .layer(cors)
        .layer(TraceLayer::new_for_http());

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
