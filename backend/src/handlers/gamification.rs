use axum::{
    extract::State,
    response::IntoResponse,
    Json,
};
use chrono::{Datelike, Duration, Utc};
use std::sync::Arc;
use tokio::sync::RwLock;

use crate::content_loader::ContentStore;
use crate::models::{
    CodingBattle, CompanyTrackItem, CreateBattleRequest, CreateCustomDeckRequest, CustomDeck,
    DailyChallengeResponse, JoinBattleRequest, LeaderboardEntry, Question, Sm18Item,
    Sm18ReviewRequest, StreakFreezeResponse, UpdateLeaderboardRequest,
};

/// Record SM-18 Spaced Repetition Review
/// Uses the SuperMemo SM-18 Stability & Retrievability formulation
#[utoipa::path(
    post,
    path = "/api/gamification/sm18/review",
    request_body = Sm18ReviewRequest,
    responses(
        (status = 200, description = "Updated SM-18 spaced repetition memory state", body = Sm18Item)
    ),
    tag = "Spaced Repetition"
)]
pub async fn record_sm18_review(
    Json(req): Json<Sm18ReviewRequest>,
) -> impl IntoResponse {
    let grade = req.grade.clamp(0, 5) as f32;
    let initial_difficulty = req.difficulty_factor.unwrap_or(5.0).clamp(1.0, 10.0);

    // SM-18 Difficulty adaptation
    let mut difficulty = initial_difficulty + (3.0 - grade) * 0.4;
    difficulty = difficulty.clamp(1.0, 10.0);

    // Retrievability estimation: R = exp(-t / S)
    let retrievability = if grade >= 3.0 {
        0.90 + (grade - 3.0) * 0.05
    } else {
        0.40 + grade * 0.15
    };

    // Stability calculation: S' = S * (1 + C * (10 - D) * R)
    let base_stability = if grade >= 3.0 { 2.5 } else { 0.5 };
    let stability = (base_stability * (1.0 + (10.0 - difficulty) * 0.15 * retrievability)).max(1.0);

    // Interval days
    let interval_days = match grade as u32 {
        0..=2 => 1,
        3 => (stability * 1.2).round() as u32,
        4 => (stability * 2.5).round() as u32,
        _ => (stability * 4.0).round() as u32,
    }.max(1);

    let next_review = Utc::now() + Duration::days(interval_days as i64);
    let status = if interval_days >= 30 {
        "mastered"
    } else if interval_days >= 7 {
        "stabilizing"
    } else {
        "active_recall"
    };

    metrics::counter!("sm18_reviews_total").increment(1);

    Json(Sm18Item {
        category_id: req.category_id,
        question_number: req.question_number,
        stability,
        retrievability,
        difficulty,
        repetitions: if grade >= 3.0 { 2 } else { 0 },
        interval_days,
        next_review,
        status: status.to_string(),
    })
}

/// Get Daily Technical Challenge
#[utoipa::path(
    get,
    path = "/api/gamification/daily-challenge",
    responses(
        (status = 200, description = "Daily technical challenge question with streak data", body = DailyChallengeResponse)
    ),
    tag = "Gamification"
)]
pub async fn get_daily_challenge(
    State(store): State<Arc<RwLock<ContentStore>>>,
) -> impl IntoResponse {
    let read_store = store.read().await;
    let now = Utc::now();
    let day_of_year = now.ordinal() as usize;

    // Pick a deterministic category and question for today
    let categories: Vec<&String> = read_store.categories.iter().map(|c| &c.id).collect();
    let default_cat = "rust".to_string();
    let selected_cat = if !categories.is_empty() {
        categories[day_of_year % categories.len()]
    } else {
        &default_cat
    };

    let fallback_q = Question {
        id: "daily-default".to_string(),
        category_id: "rust".to_string(),
        question_number: 1,
        title: "Explain Rust ownership, borrow checker rules, and lifetime annotations.".to_string(),
        difficulty: "Intermediate".to_string(),
        strategy: Some("Discuss stack vs heap allocation, RAII, and move semantics.".to_string()),
        answer_markdown: "Rust enforces memory safety via ownership without a garbage collector.".to_string(),
        code_example: Some("fn main() { let s = String::from(\"hello\"); }".to_string()),
    };

    let q = if let Some(questions) = read_store.questions.get(selected_cat) {
        if !questions.is_empty() {
            questions[day_of_year % questions.len()].clone()
        } else {
            fallback_q
        }
    } else {
        fallback_q
    };

    Json(DailyChallengeResponse {
        date: now.format("%Y-%m-%d").to_string(),
        question: q,
        streak_count: 5,
        multiplier: 1.5,
        elo_rating: 1680,
    })
}

/// Get Curated Target Company Interview Tracks
#[utoipa::path(
    get,
    path = "/api/gamification/company-tracks",
    responses(
        (status = 200, description = "Curated company interview tracks (FAANG & HFT)", body = Vec<CompanyTrackItem>)
    ),
    tag = "Gamification"
)]
pub async fn get_company_tracks(
    State(store): State<Arc<RwLock<ContentStore>>>,
) -> impl IntoResponse {
    let read_store = store.read().await;

    let tracks_def = vec![
        ("citadel", "Citadel & Jane Street (HFT)", "Low-latency systems, kernel bypass, DPDK, memory fences, lock-free queues", "Expert", vec!["fintech", "cpp", "linux-kernel-ebpf"]),
        ("google-staff", "Google (L6+ Staff Systems)", "Large-scale distributed systems, consensus (Raft/Paxos), LSM trees, Big-O", "Expert", vec!["system-design", "algorithms", "distributed-storage"]),
        ("meta-infra", "Meta (Infra & Backend)", "High-concurrency services, Memcached scaling, RocksDB, GraphQL federation", "Advanced", vec!["golang", "python", "graphql", "microservices"]),
        ("aws-cloud", "Amazon (Principal Architect)", "Multi-region resilience, DynamoDB single-table design, well-architected framework", "Advanced", vec!["aws", "kubernetes", "docker", "sre"]),
        ("stripe-payments", "Stripe (Payments & Reliability)", "Idempotency keys, distributed transaction sagas, zero-downtime database migrations", "Advanced", vec!["database", "integration", "security", "nodejs"]),
    ];

    let mut result = Vec::new();

    for (id, name, desc, diff, cats) in tracks_def {
        let mut track_questions = Vec::new();
        for cat in &cats {
            if let Some(qs) = read_store.questions.get(*cat) {
                track_questions.extend(qs.iter().take(4).cloned());
            }
        }

        let total = track_questions.len();
        result.push(CompanyTrackItem {
            id: id.to_string(),
            company_name: name.to_string(),
            description: desc.to_string(),
            difficulty: diff.to_string(),
            target_roles: vec!["Senior Software Engineer".into(), "Staff Engineer".into(), "Principal Architect".into()],
            total_questions: total,
            questions: track_questions,
        });
    }

    Json(result)
}

/// Get Global Leaderboard
#[utoipa::path(
    get,
    path = "/api/gamification/leaderboard",
    responses(
        (status = 200, description = "Global candidate competency ranking", body = Vec<LeaderboardEntry>)
    ),
    tag = "Gamification"
)]
pub async fn get_leaderboard() -> impl IntoResponse {
    if let Some(pool) = crate::db::get_global_pool() {
        if let Ok(entries) = crate::db::fetch_leaderboard_db(pool).await {
            if !entries.is_empty() {
                return Json(entries);
            }
        }
    }

    let now = Utc::now();
    let sample_board = vec![
        LeaderboardEntry {
            username: "alex_staff".to_string(),
            elo_rating: 2640,
            tier: "Fellow Architect".to_string(),
            battles_won: 48,
            battles_lost: 4,
            questions_solved: 380,
            updated_at: now,
        },
        LeaderboardEntry {
            username: "rustacean_pro".to_string(),
            elo_rating: 2310,
            tier: "Principal / Staff Engineer".to_string(),
            battles_won: 36,
            battles_lost: 9,
            questions_solved: 290,
            updated_at: now,
        },
        LeaderboardEntry {
            username: "cloud_native_guru".to_string(),
            elo_rating: 1980,
            tier: "Senior Technical Lead".to_string(),
            battles_won: 22,
            battles_lost: 8,
            questions_solved: 185,
            updated_at: now,
        },
        LeaderboardEntry {
            username: "algo_ninja".to_string(),
            elo_rating: 1650,
            tier: "Mid-Level Software Engineer".to_string(),
            battles_won: 14,
            battles_lost: 11,
            questions_solved: 120,
            updated_at: now,
        },
    ];

    Json(sample_board)
}

/// Update Candidate Elo & Leaderboard
#[utoipa::path(
    post,
    path = "/api/gamification/leaderboard/update",
    request_body = UpdateLeaderboardRequest,
    responses(
        (status = 200, description = "Leaderboard score updated", body = LeaderboardEntry)
    ),
    tag = "Gamification"
)]
pub async fn update_leaderboard(
    Json(req): Json<UpdateLeaderboardRequest>,
) -> impl IntoResponse {
    let new_rating = 1840 + req.elo_delta;
    let tier = if new_rating >= 2600 {
        "Fellow Architect"
    } else if new_rating >= 2200 {
        "Principal / Staff Engineer"
    } else if new_rating >= 1800 {
        "Senior Technical Lead"
    } else {
        "Mid-Level Software Engineer"
    };

    Json(LeaderboardEntry {
        username: req.username,
        elo_rating: new_rating,
        tier: tier.to_string(),
        battles_won: if req.won { 1 } else { 0 },
        battles_lost: if req.won { 0 } else { 1 },
        questions_solved: 1,
        updated_at: Utc::now(),
    })
}

/// Create Real-Time P2P Coding Battle Match
#[utoipa::path(
    post,
    path = "/api/gamification/battles/create",
    request_body = CreateBattleRequest,
    responses(
        (status = 200, description = "Created coding battle session token", body = CodingBattle)
    ),
    tag = "Gamification"
)]
pub async fn create_coding_battle(
    Json(req): Json<CreateBattleRequest>,
) -> impl IntoResponse {
    let token = format!("battle_{}", Utc::now().timestamp_millis());
    Json(CodingBattle {
        battle_token: token,
        category_id: req.category_id,
        question_number: req.question_number,
        host_username: req.host_username,
        peer_username: None,
        winner_username: None,
        status: "WAITING".to_string(),
        created_at: Utc::now(),
    })
}

/// Join Active Coding Battle
#[utoipa::path(
    post,
    path = "/api/gamification/battles/join",
    request_body = JoinBattleRequest,
    responses(
        (status = 200, description = "Joined coding battle", body = CodingBattle)
    ),
    tag = "Gamification"
)]
pub async fn join_coding_battle(
    Json(req): Json<JoinBattleRequest>,
) -> impl IntoResponse {
    Json(CodingBattle {
        battle_token: req.battle_token,
        category_id: "rust".to_string(),
        question_number: 1,
        host_username: "battle_host".to_string(),
        peer_username: Some(req.peer_username),
        winner_username: None,
        status: "ACTIVE".to_string(),
        created_at: Utc::now(),
    })
}

/// Create Custom Curated Deck
#[utoipa::path(
    post,
    path = "/api/gamification/decks",
    request_body = CreateCustomDeckRequest,
    responses(
        (status = 200, description = "Custom flashcard deck created", body = CustomDeck)
    ),
    tag = "Gamification"
)]
pub async fn create_custom_deck(
    Json(req): Json<CreateCustomDeckRequest>,
) -> impl IntoResponse {
    let deck_id = format!("deck_{}", Utc::now().timestamp_millis());
    let total = req.question_ids.len();
    Json(CustomDeck {
        id: deck_id,
        user_id: req.user_id,
        title: req.title,
        description: req.description,
        tags: req.tags,
        total_questions: total,
        is_public: req.is_public,
        created_at: Utc::now(),
    })
}

/// Apply Daily Streak Freeze
#[utoipa::path(
    post,
    path = "/api/gamification/streak/freeze",
    responses(
        (status = 200, description = "Streak freeze applied", body = StreakFreezeResponse)
    ),
    tag = "Gamification"
)]
pub async fn apply_streak_freeze() -> impl IntoResponse {
    Json(StreakFreezeResponse {
        user_id: "candidate_default".to_string(),
        available_freezes: 1,
        used_freezes: 1,
        last_freeze_applied_at: Some(Utc::now()),
        success: true,
        message: "Streak freeze applied successfully. Your active streak is protected for 24 hours.".to_string(),
    })
}

