#!/usr/bin/env bash
set -euo pipefail

SHA="${1:-${GITHUB_SHA:-unknown}}"

echo "[prod] deploy start: sha=${SHA}"

if [[ -n "${PROD_DEPLOY_CMD:-}" ]]; then
  echo "[prod] running custom deploy command"
  bash -lc "${PROD_DEPLOY_CMD}"
else
  echo "[prod] PROD_DEPLOY_CMD not set -> no-op success"
fi

echo "[prod] deploy done"
