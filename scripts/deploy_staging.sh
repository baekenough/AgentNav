#!/usr/bin/env bash
set -euo pipefail

SHA="${1:-${GITHUB_SHA:-unknown}}"

echo "[staging] deploy start: sha=${SHA}"

if [[ -n "${STAGING_DEPLOY_CMD:-}" ]]; then
  echo "[staging] running custom deploy command"
  bash -lc "${STAGING_DEPLOY_CMD}"
else
  echo "[staging] STAGING_DEPLOY_CMD not set -> no-op success"
fi

echo "[staging] deploy done"
