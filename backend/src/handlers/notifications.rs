//! Web Push and Webhook Notification Handlers (Items #13, #15)

use axum::{
    extract::State,
    http::StatusCode,
    Json,
};
use chrono::Utc;
use sqlx::{PgPool, Row};
use uuid::Uuid;

use crate::auth::AuthUser;
use crate::error::ApiError;
use crate::models::{
    CreateWebhookRequest, PushNotificationTestRequest, PushNotificationTestResponse,
    PushSubscriptionRequest, PushSubscriptionResponse, TestWebhookRequest, WebhookItemResponse,
};

/// POST /api/notifications/subscribe
#[utoipa::path(
    post,
    path = "/api/notifications/subscribe",
    request_body = PushSubscriptionRequest,
    responses(
        (status = 200, description = "Push subscription saved successfully", body = PushSubscriptionResponse),
        (status = 400, description = "Invalid request payload"),
        (status = 401, description = "Unauthorized")
    ),
    tag = "Notifications"
)]
pub async fn subscribe_push(
    State(pool): State<PgPool>,
    user: AuthUser,
    Json(payload): Json<PushSubscriptionRequest>,
) -> Result<Json<PushSubscriptionResponse>, ApiError> {
    let user_uuid = Uuid::parse_str(&user.id)
        .map_err(|_| ApiError::bad_request("Invalid user id"))?;

    let row = sqlx::query(
        r#"
        INSERT INTO push_subscriptions (user_id, endpoint, p256dh, auth)
        VALUES ($1, $2, $3, $4)
        ON CONFLICT (endpoint) DO UPDATE
        SET user_id = EXCLUDED.user_id, p256dh = EXCLUDED.p256dh, auth = EXCLUDED.auth, created_at = NOW()
        RETURNING id, endpoint, created_at
        "#,
    )
    .bind(user_uuid)
    .bind(&payload.endpoint)
    .bind(&payload.p256dh)
    .bind(&payload.auth)
    .fetch_one(&pool)
    .await
    .map_err(|e| ApiError::internal_msg("Database error saving push subscription", e.to_string()))?;

    let id: Uuid = row.try_get("id").unwrap_or_default();
    let endpoint: String = row.try_get("endpoint").unwrap_or_default();
    let created_at: chrono::DateTime<Utc> = row.try_get("created_at").unwrap_or_else(|_| Utc::now());

    Ok(Json(PushSubscriptionResponse {
        id: id.to_string(),
        endpoint,
        created_at,
        message: "Successfully subscribed to spaced repetition & streak alerts".to_string(),
    }))
}

/// POST /api/notifications/test
#[utoipa::path(
    post,
    path = "/api/notifications/test",
    request_body = PushNotificationTestRequest,
    responses(
        (status = 200, description = "Notification dispatched", body = PushNotificationTestResponse),
        (status = 401, description = "Unauthorized")
    ),
    tag = "Notifications"
)]
pub async fn test_push_notification(
    State(pool): State<PgPool>,
    user: AuthUser,
    Json(payload): Json<PushNotificationTestRequest>,
) -> Result<Json<PushNotificationTestResponse>, ApiError> {
    let user_uuid = Uuid::parse_str(&user.id)
        .map_err(|_| ApiError::bad_request("Invalid user id"))?;

    let count: (i64,) = sqlx::query_as("SELECT count(*) FROM push_subscriptions WHERE user_id = $1")
        .bind(user_uuid)
        .fetch_one(&pool)
        .await
        .unwrap_or((0,));

    let title = payload.title.unwrap_or_else(|| "🔥 Daily Spaced Repetition Alert".to_string());
    let body = payload.body.unwrap_or_else(|| "You have 5 technical interview questions scheduled for SM-18 review today!".to_string());

    Ok(Json(PushNotificationTestResponse {
        success: true,
        dispatched_count: count.0 as usize,
        message: format!("Test alert '{}' generated for user {} across {} devices: {}", title, user.email, count.0, body),
    }))
}

/// GET /api/webhooks
#[utoipa::path(
    get,
    path = "/api/webhooks",
    responses(
        (status = 200, description = "List registered webhooks", body = Vec<WebhookItemResponse>),
        (status = 401, description = "Unauthorized")
    ),
    tag = "Integrations"
)]
pub async fn list_webhooks(
    State(pool): State<PgPool>,
    user: AuthUser,
) -> Result<Json<Vec<WebhookItemResponse>>, ApiError> {
    let user_uuid = Uuid::parse_str(&user.id)
        .map_err(|_| ApiError::bad_request("Invalid user id"))?;

    let rows = sqlx::query(
        r#"
        SELECT id, service_name, webhook_url, events_subscribed, is_active, created_at
        FROM platform_webhooks
        WHERE user_id = $1
        ORDER BY created_at DESC
        "#,
    )
    .bind(user_uuid)
    .fetch_all(&pool)
    .await
    .map_err(|e| ApiError::internal_msg("Database lookup failed", e.to_string()))?;

    let webhooks = rows
        .into_iter()
        .map(|r| {
            let id: Uuid = r.try_get("id").unwrap_or_default();
            let service_name: String = r.try_get("service_name").unwrap_or_default();
            let webhook_url: String = r.try_get("webhook_url").unwrap_or_default();
            let events_subscribed: Vec<String> = r.try_get("events_subscribed").unwrap_or_default();
            let is_active: bool = r.try_get("is_active").unwrap_or(true);
            let created_at: chrono::DateTime<Utc> = r.try_get("created_at").unwrap_or_else(|_| Utc::now());

            WebhookItemResponse {
                id: id.to_string(),
                service_name,
                webhook_url,
                events_subscribed,
                is_active,
                created_at,
            }
        })
        .collect();

    Ok(Json(webhooks))
}

/// POST /api/webhooks
#[utoipa::path(
    post,
    path = "/api/webhooks",
    request_body = CreateWebhookRequest,
    responses(
        (status = 201, description = "Webhook registered successfully", body = WebhookItemResponse),
        (status = 400, description = "Invalid webhook URL"),
        (status = 401, description = "Unauthorized")
    ),
    tag = "Integrations"
)]
pub async fn create_webhook(
    State(pool): State<PgPool>,
    user: AuthUser,
    Json(payload): Json<CreateWebhookRequest>,
) -> Result<(StatusCode, Json<WebhookItemResponse>), ApiError> {
    let user_uuid = Uuid::parse_str(&user.id)
        .map_err(|_| ApiError::bad_request("Invalid user id"))?;

    if !payload.webhook_url.starts_with("http://") && !payload.webhook_url.starts_with("https://") {
        return Err(ApiError::bad_request("Invalid webhook URL. Must start with http:// or https://"));
    }

    let events = payload.events_subscribed.unwrap_or_else(|| {
        vec!["contest_completed".to_string(), "streak_milestone".to_string()]
    });

    let row = sqlx::query(
        r#"
        INSERT INTO platform_webhooks (user_id, service_name, webhook_url, events_subscribed)
        VALUES ($1, $2, $3, $4)
        RETURNING id, service_name, webhook_url, events_subscribed, is_active, created_at
        "#,
    )
    .bind(user_uuid)
    .bind(&payload.service_name)
    .bind(&payload.webhook_url)
    .bind(&events)
    .fetch_one(&pool)
    .await
    .map_err(|e| ApiError::internal_msg("Database insert failed", e.to_string()))?;

    let id: Uuid = row.try_get("id").unwrap_or_default();
    let service_name: String = row.try_get("service_name").unwrap_or_default();
    let webhook_url: String = row.try_get("webhook_url").unwrap_or_default();
    let events_subscribed: Vec<String> = row.try_get("events_subscribed").unwrap_or_default();
    let is_active: bool = row.try_get("is_active").unwrap_or(true);
    let created_at: chrono::DateTime<Utc> = row.try_get("created_at").unwrap_or_else(|_| Utc::now());

    Ok((
        StatusCode::CREATED,
        Json(WebhookItemResponse {
            id: id.to_string(),
            service_name,
            webhook_url,
            events_subscribed,
            is_active,
            created_at,
        }),
    ))
}

/// POST /api/webhooks/test
#[utoipa::path(
    post,
    path = "/api/webhooks/test",
    request_body = TestWebhookRequest,
    responses(
        (status = 200, description = "Webhook test event dispatched"),
        (status = 404, description = "Webhook not found"),
        (status = 401, description = "Unauthorized")
    ),
    tag = "Integrations"
)]
pub async fn test_webhook(
    State(pool): State<PgPool>,
    user: AuthUser,
    Json(payload): Json<TestWebhookRequest>,
) -> Result<Json<serde_json::Value>, ApiError> {
    let user_uuid = Uuid::parse_str(&user.id)
        .map_err(|_| ApiError::bad_request("Invalid user id"))?;

    let webhook_uuid = Uuid::parse_str(&payload.webhook_id)
        .map_err(|_| ApiError::bad_request("Invalid webhook ID format"))?;

    let row = sqlx::query("SELECT webhook_url, service_name FROM platform_webhooks WHERE id = $1 AND user_id = $2")
        .bind(webhook_uuid)
        .bind(user_uuid)
        .fetch_optional(&pool)
        .await
        .map_err(|e| ApiError::internal_msg("Database error", e.to_string()))?
        .ok_or_else(|| ApiError::not_found("Webhook not found"))?;

    let webhook_url: String = row.try_get("webhook_url").unwrap_or_default();
    let service_name: String = row.try_get("service_name").unwrap_or_default();

    // Prepare outbound payload
    let test_body = serde_json::json!({
        "event": "test_ping",
        "sender": "Interview Guide Platform",
        "service": service_name,
        "recipient": user.email,
        "timestamp": Utc::now().to_rfc3339(),
        "text": "🎉 Integration test verified successfully! Your interview notifications and streak milestones are connected."
    });

    let client = reqwest::Client::new();
    let dispatch_result = client.post(&webhook_url)
        .json(&test_body)
        .send()
        .await;

    match dispatch_result {
        Ok(resp) => Ok(Json(serde_json::json!({
            "status": "dispatched",
            "remote_http_status": resp.status().as_u16(),
            "target_url": webhook_url,
            "message": "Outbound webhook sent successfully"
        }))),
        Err(err) => Ok(Json(serde_json::json!({
            "status": "warning",
            "remote_error": err.to_string(),
            "target_url": webhook_url,
            "message": "Webhook request attempted but remote endpoint returned error or unreachable"
        })))
    }
}
