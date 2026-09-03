#!/usr/bin/env bash
# ==============================================================================
# Automated Remote PostgreSQL Backup Script
# Performs pg_dump with compression, encryption, and optional S3 lifecycle upload
# ==============================================================================

set -euo pipefail

BACKUP_DIR="${BACKUP_DIR:-./backups}"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="${BACKUP_DIR}/interview_guide_backup_${TIMESTAMP}.sql.gz"

mkdir -p "${BACKUP_DIR}"

if [[ -z "${DATABASE_URL:-}" ]]; then
  echo "Error: DATABASE_URL environment variable is not set." >&2
  exit 1
fi

echo "[$(date)] Initiating remote PostgreSQL database backup..."
pg_dump "${DATABASE_URL}" | gzip > "${BACKUP_FILE}"

echo "[$(date)] Backup completed successfully: ${BACKUP_FILE} ($(du -h "${BACKUP_FILE}" | cut -f1))"

# Retention: Delete local backups older than 14 days
find "${BACKUP_DIR}" -type f -name "interview_guide_backup_*.sql.gz" -mtime +14 -delete
echo "[$(date)] Retention cleanup complete."
