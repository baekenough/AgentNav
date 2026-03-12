#!/usr/bin/env bash
set -euo pipefail

if [[ -n "${STAGING_HEALTHCHECK_URL:-}" ]]; then
  echo "[staging] healthcheck: ${STAGING_HEALTHCHECK_URL}"
  curl -fsS --max-time 15 "${STAGING_HEALTHCHECK_URL}" >/dev/null
else
  echo "[staging] STAGING_HEALTHCHECK_URL not set -> no-op success"
fi

echo "[staging] healthcheck ok"
