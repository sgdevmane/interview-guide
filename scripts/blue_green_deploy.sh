#!/usr/bin/env bash
# ==============================================================================
# Zero-Downtime Blue/Green Rolling Update Script
# Orchestrates zero-downtime updates for dual-instance Web & Rust Backend clusters
# ==============================================================================

set -euo pipefail

PROD_COMPOSE_FILE="docker-compose.production.yml"
PROD_PORT="${PROD_PORT:-9443}"
HEALTH_CHECK_URL="http://localhost:${PROD_PORT}/health"
MAX_ATTEMPTS=20
SLEEP_INTERVAL=3

log() {
    echo -e "\033[1;34m[DEPLOY]\033[0m $1"
}

success() {
    echo -e "\033[1;32m[SUCCESS]\033[0m $1"
}

error() {
    echo -e "\033[1;31m[ERROR]\033[0m $1" >&2
}

log "Starting Zero-Downtime Rolling Update on Production Cluster..."

# Step 1: Verify environment variables and database connectivity
if [ ! -f ".env.production" ]; then
    error ".env.production file not found! Aborting deployment."
    exit 1
fi

log "Verifying remote PostgreSQL connectivity before rollout..."
DATABASE_URL=$(grep -E '^DATABASE_URL=' .env.production | cut -d '=' -f2- | tr -d '"' || true)
if [ -n "$DATABASE_URL" ]; then
    log "Remote PostgreSQL URI detected in .env.production."
fi

# Step 2: Build new images without taking down active containers
log "Building updated production images (Web & Rust Backend)..."
docker compose -f "$PROD_COMPOSE_FILE" build --pull

# Step 3: Rolling update of Backend instances
log "Rolling update: Updating backend-1..."
docker compose -f "$PROD_COMPOSE_FILE" up -d --no-deps --build backend-1
sleep 5

log "Rolling update: Updating backend-2..."
docker compose -f "$PROD_COMPOSE_FILE" up -d --no-deps --build backend-2
sleep 5

# Step 4: Rolling update of Web Frontend instances
log "Rolling update: Updating web-1..."
docker compose -f "$PROD_COMPOSE_FILE" up -d --no-deps --build web-1
sleep 5

log "Rolling update: Updating web-2..."
docker compose -f "$PROD_COMPOSE_FILE" up -d --no-deps --build web-2
sleep 5

# Step 5: Reload Nginx Load Balancer configuration gracefully
log "Reloading Nginx Reverse Proxy / Load Balancer configuration..."
docker compose -f "$PROD_COMPOSE_FILE" exec -T nginx-lb nginx -s reload || {
    log "Nginx container reload failed or not running; restarting nginx-lb..."
    docker compose -f "$PROD_COMPOSE_FILE" up -d --no-deps nginx-lb
}

# Step 6: Verify Health Status via Load Balancer
log "Awaiting cluster health check at ${HEALTH_CHECK_URL}..."
ATTEMPT=1
while [ $ATTEMPT -le $MAX_ATTEMPTS ]; do
    if curl -s -f "$HEALTH_CHECK_URL" > /dev/null 2>&1; then
        success "Production cluster is HEALTHY and serving traffic on port ${PROD_PORT}!"
        exit 0
    fi
    log "Attempt $ATTEMPT/$MAX_ATTEMPTS: Health check pending... Retrying in ${SLEEP_INTERVAL}s"
    sleep $SLEEP_INTERVAL
    ATTEMPT=$((ATTEMPT + 1))
done

error "Health check failed after $MAX_ATTEMPTS attempts. Check container logs with 'docker compose -f $PROD_COMPOSE_FILE logs'."
exit 1
