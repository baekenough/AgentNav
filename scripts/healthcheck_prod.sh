#!/usr/bin/env bash
set -euo pipefail

if [[ -n "${PROD_HEALTHCHECK_URL:-}" ]]; then
  echo "[prod] healthcheck: ${PROD_HEALTHCHECK_URL}"
  curl -fsS --max-time 15 "${PROD_HEALTHCHECK_URL}" >/dev/null
else
  echo "[prod] PROD_HEALTHCHECK_URL not set -> no-op success"
fi

echo "[prod] healthcheck ok"
