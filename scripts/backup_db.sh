#!/usr/bin/env bash
# ==============================================================================
# Automated PostgreSQL Backup Script (Item #42)
# Exports schema and data from remote PostgreSQL DB, compresses, checks integrity,
# and uploads to S3/Cloudflare R2 object storage with retention management.
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# Load environment configuration (prefer .env.production, fallback to .env)
if [[ -f "${PROJECT_ROOT}/.env.production" ]]; then
    # shellcheck disable=SC1091
    source "${PROJECT_ROOT}/.env.production"
elif [[ -f "${PROJECT_ROOT}/.env" ]]; then
    # shellcheck disable=SC1091
    source "${PROJECT_ROOT}/.env"
fi

DB_USER="${DB_USER:-sterlingpixel}"
DB_PASSWORD="${DB_PASSWORD:-XspSmTGPxBeRhG84}"
DB_HOST="${DB_HOST:-213.199.39.44}"
DB_PORT="${DB_PORT:-35432}"
DB_NAME="${DB_NAME:-interview_staging}"

BACKUP_DIR="${PROJECT_ROOT}/backups"
TIMESTAMP="$(date -u +"%Y%m%d_%H%M%SZ")"
BACKUP_FILENAME="interview_guide_backup_${TIMESTAMP}.sql.gz"
BACKUP_PATH="${BACKUP_DIR}/${BACKUP_FILENAME}"
CHECKSUM_PATH="${BACKUP_PATH}.sha256"

mkdir -p "${BACKUP_DIR}"

echo "================================================================="
echo "[BACKUP] Starting automated backup at $(date -u)"
echo "[BACKUP] Target Host: ${DB_HOST}:${DB_PORT} / Database: ${DB_NAME}"
echo "================================================================="

# Execute pg_dump with compression
export PGPASSWORD="${DB_PASSWORD}"
if command -v pg_dump >/dev/null 2>&1; then
    pg_dump -h "${DB_HOST}" -p "${DB_PORT}" -U "${DB_USER}" -d "${DB_NAME}" --clean --if-exists --no-owner --no-privileges | gzip -9 > "${BACKUP_PATH}"
else
    echo "[BACKUP ERROR] pg_dump executable not found in PATH." >&2
    exit 1
fi
unset PGPASSWORD

# Validate that file was generated and is non-empty
if [[ ! -s "${BACKUP_PATH}" ]]; then
    echo "[BACKUP ERROR] Generated backup file is empty or missing." >&2
    rm -f "${BACKUP_PATH}"
    exit 1
fi

# Verify gzip archive integrity
gzip -t "${BACKUP_PATH}"
echo "[BACKUP] Archive integrity verified: OK"

# Generate SHA-256 checksum
if command -v shasum >/dev/null 2>&1; then
    shasum -a 256 "${BACKUP_PATH}" > "${CHECKSUM_PATH}"
elif command -v sha256sum >/dev/null 2>&1; then
    sha256sum "${BACKUP_PATH}" > "${CHECKSUM_PATH}"
fi

BACKUP_SIZE="$(ls -lh "${BACKUP_PATH}" | awk '{print $5}')"
echo "[BACKUP] Successfully created ${BACKUP_FILENAME} (Size: ${BACKUP_SIZE})"

# Upload to S3 / Cloudflare R2 if configured
if [[ -n "${S3_BUCKET:-}" ]]; then
    echo "[BACKUP] Uploading to object storage bucket: ${S3_BUCKET}..."
    S3_ENDPOINT_FLAG=""
    if [[ -n "${S3_ENDPOINT_URL:-}" ]]; then
        S3_ENDPOINT_FLAG="--endpoint-url ${S3_ENDPOINT_URL}"
    fi

    if command -v aws >/dev/null 2>&1; then
        aws s3 cp "${BACKUP_PATH}" "s3://${S3_BUCKET}/backups/${BACKUP_FILENAME}" ${S3_ENDPOINT_FLAG}
        aws s3 cp "${CHECKSUM_PATH}" "s3://${S3_BUCKET}/backups/${BACKUP_FILENAME}.sha256" ${S3_ENDPOINT_FLAG}
        echo "[BACKUP] S3 upload completed successfully."
    else
        echo "[BACKUP WARNING] aws CLI not available; S3 upload skipped."
    fi
fi

# Retention policy: Keep local backups within retention window (default: 14 days)
RETENTION_DAYS="${BACKUP_RETENTION_DAYS:-14}"
echo "[BACKUP] Applying local retention policy (Pruning backups older than ${RETENTION_DAYS} days)..."
find "${BACKUP_DIR}" -name "interview_guide_backup_*.sql.gz*" -type f -mtime +"${RETENTION_DAYS}" -delete

echo "[BACKUP] Backup routine completed successfully at $(date -u)"
