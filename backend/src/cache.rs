//! Distributed Cache & Rate Limiting Engine (Items #1 & #41)
//! Provides Redis/Dragonfly cache-aside with graceful fallback to in-memory caching,
//! plus distributed sliding-window rate limiting to ensure cluster-wide parity.

use redis::aio::ConnectionManager;
use redis::AsyncCommands;
use serde::de::DeserializeOwned;
use serde::Serialize;
use std::collections::HashMap;
use std::sync::Arc;
use std::time::{Duration, Instant};
use tokio::sync::RwLock;

/// Cache client supporting Redis connection management with in-memory fallback
#[derive(Clone)]
#[allow(dead_code)]
pub struct CacheClient {
    redis_conn: Option<ConnectionManager>,
    memory_cache: Arc<RwLock<HashMap<String, (String, Instant)>>>,
}

#[allow(dead_code)]
impl CacheClient {
    pub async fn new(redis_url: Option<String>) -> Self {
        let redis_conn = if let Some(url) = redis_url {
            tracing::info!("Attempting connection to Redis cluster at {}", url);
            match redis::Client::open(url.as_str()) {
                Ok(client) => match ConnectionManager::new(client).await {
                    Ok(cm) => {
                        tracing::info!("Connected successfully to Redis cluster.");
                        Some(cm)
                    }
                    Err(err) => {
                        tracing::warn!(
                            "Failed to initialize Redis connection manager: {}. Falling back to in-memory cache.",
                            err
                        );
                        None
                    }
                },
                Err(err) => {
                    tracing::warn!("Invalid REDIS_URL format ({}). Using in-memory fallback.", err);
                    None
                }
            }
        } else {
            tracing::info!("REDIS_URL not configured. Utilizing high-performance local memory cache.");
            None
        };

        Self {
            redis_conn,
            memory_cache: Arc::new(RwLock::new(HashMap::new())),
        }
    }

    /// Retrieve an entry from cache
    pub async fn get<T: DeserializeOwned>(&self, key: &str) -> Option<T> {
        if let Some(mut cm) = self.redis_conn.clone() {
            let res: redis::RedisResult<Option<String>> = cm.get(key).await;
            if let Ok(Some(json_str)) = res {
                if let Ok(val) = serde_json::from_str::<T>(&json_str) {
                    return Some(val);
                }
            }
        }

        // Fallback to in-memory cache
        let guard = self.memory_cache.read().await;
        if let Some((json_str, expiry)) = guard.get(key) {
            if Instant::now() < *expiry {
                if let Ok(val) = serde_json::from_str::<T>(json_str) {
                    return Some(val);
                }
            }
        }

        None
    }

    /// Store an entry in cache with a TTL
    pub async fn set<T: Serialize>(&self, key: &str, value: &T, ttl_secs: u64) {
        let Ok(json_str) = serde_json::to_string(value) else {
            return;
        };

        if let Some(mut cm) = self.redis_conn.clone() {
            let res: redis::RedisResult<()> = cm.set_ex(key, &json_str, ttl_secs).await;
            if res.is_ok() {
                return;
            }
        }

        // Store in local memory cache
        let mut guard = self.memory_cache.write().await;
        guard.insert(
            key.to_string(),
            (json_str, Instant::now() + Duration::from_secs(ttl_secs)),
        );
    }

    /// Invalidate a key
    pub async fn delete(&self, key: &str) {
        if let Some(mut cm) = self.redis_conn.clone() {
            let _: redis::RedisResult<()> = cm.del(key).await;
        }

        let mut guard = self.memory_cache.write().await;
        guard.remove(key);
    }
}

/// Distributed sliding-window rate limiter (Item #41)
#[derive(Clone)]
pub struct DistributedRateLimiter {
    redis_conn: Option<ConnectionManager>,
    memory_limiter: Arc<RwLock<HashMap<String, Vec<Instant>>>>,
}

impl DistributedRateLimiter {
    pub fn new(cache: &CacheClient) -> Self {
        Self {
            redis_conn: cache.redis_conn.clone(),
            memory_limiter: Arc::new(RwLock::new(HashMap::new())),
        }
    }

    /// Checks if a client/key is allowed under the rate limit (e.g., 60 requests per 60s).
    /// Returns `true` if allowed, `false` if limit exceeded.
    pub async fn check_rate_limit(&self, key: &str, max_requests: usize, window_secs: u64) -> bool {
        let rate_key = format!("ratelimit:{}", key);

        if let Some(mut cm) = self.redis_conn.clone() {
            let now_ms = chrono::Utc::now().timestamp_millis();
            let window_start_ms = now_ms - (window_secs as i64 * 1000);

            // Redis atomic sliding-window using transaction / pipeline
            let redis_res: redis::RedisResult<usize> = redis::pipe()
                .atomic()
                .zrembyscore(&rate_key, "-inf", window_start_ms)
                .zadd(&rate_key, now_ms, format!("{}:{}", now_ms, rand::random::<u32>()))
                .zcard(&rate_key)
                .expire(&rate_key, (window_secs + 10) as i64)
                .query_async(&mut cm)
                .await
                .map(|(_, _, count, _): (i64, i64, usize, i64)| count);

            if let Ok(count) = redis_res {
                return count <= max_requests;
            }
        }

        // Memory fallback sliding window
        let mut guard = self.memory_limiter.write().await;
        let now = Instant::now();
        let cutoff = now - Duration::from_secs(window_secs);

        let timestamps = guard.entry(rate_key).or_insert_with(Vec::new);
        timestamps.retain(|&t| t > cutoff);

        if timestamps.len() < max_requests {
            timestamps.push(now);
            true
        } else {
            false
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[tokio::test]
    async fn test_in_memory_cache_fallback() {
        let cache = CacheClient::new(None).await;
        cache.set("test_key", &vec![1, 2, 3], 60).await;
        let retrieved: Option<Vec<i32>> = cache.get("test_key").await;
        assert_eq!(retrieved, Some(vec![1, 2, 3]));
    }

    #[tokio::test]
    async fn test_in_memory_sliding_window_limiter() {
        let cache = CacheClient::new(None).await;
        let limiter = DistributedRateLimiter::new(&cache);

        // Allow 3 requests in 10s
        assert!(limiter.check_rate_limit("user:123", 3, 10).await);
        assert!(limiter.check_rate_limit("user:123", 3, 10).await);
        assert!(limiter.check_rate_limit("user:123", 3, 10).await);
        // 4th request must be rejected
        assert!(!limiter.check_rate_limit("user:123", 3, 10).await);
    }
}
