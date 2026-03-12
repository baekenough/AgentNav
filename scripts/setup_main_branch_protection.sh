#!/usr/bin/env bash
set -euo pipefail

REPO=""
APPROVALS="1"
CONTEXTS=""

usage() {
  cat <<'EOF'
Usage:
  ./scripts/setup_main_branch_protection.sh [--repo owner/repo] [--approvals N] [--contexts "check1,check2"]

Examples:
  ./scripts/setup_main_branch_protection.sh
  ./scripts/setup_main_branch_protection.sh --repo baekenough/AgentNav --approvals 2
  ./scripts/setup_main_branch_protection.sh --contexts "agentnav-ci / validate"
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo)
      REPO="${2:-}"
      shift 2
      ;;
    --approvals)
      APPROVALS="${2:-}"
      shift 2
      ;;
    --contexts)
      CONTEXTS="${2:-}"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage
      exit 1
      ;;
  esac
done

if ! command -v gh >/dev/null 2>&1; then
  echo "gh CLI is required. Install from https://cli.github.com/" >&2
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "GitHub auth is required. Run: gh auth login" >&2
  exit 1
fi

if [[ -z "$REPO" ]]; then
  origin_url="$(git config --get remote.origin.url || true)"
  if [[ -z "$origin_url" ]]; then
    echo "Cannot detect repository. Use --repo owner/repo" >&2
    exit 1
  fi
  REPO="$(echo "$origin_url" | sed -E 's#^(git@github.com:|https://github.com/)##; s#\.git$##')"
fi

if ! [[ "$APPROVALS" =~ ^[0-9]+$ ]]; then
  echo "--approvals must be a non-negative integer" >&2
  exit 1
fi

PAYLOAD="$(python3 - <<'PY'
import json
import os

approvals = int(os.environ.get('APPROVALS', '1'))
contexts_raw = os.environ.get('CONTEXTS', '').strip()

if contexts_raw:
    contexts = [c.strip() for c in contexts_raw.split(',') if c.strip()]
    required_status_checks = {
        "strict": True,
        "contexts": contexts,
    }
else:
    required_status_checks = None

payload = {
    "required_status_checks": required_status_checks,
    "enforce_admins": True,
    "required_pull_request_reviews": {
        "dismiss_stale_reviews": True,
        "require_code_owner_reviews": False,
        "required_approving_review_count": approvals,
    },
    "restrictions": None,
    "allow_force_pushes": False,
    "allow_deletions": False,
    "required_conversation_resolution": True,
}
print(json.dumps(payload))
PY
)"

echo "Applying branch protection to ${REPO}:main"
gh api \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  "repos/${REPO}/branches/main/protection" \
  --input - <<<"${PAYLOAD}" >/dev/null

echo "Done. Branch protection applied to ${REPO}:main"
