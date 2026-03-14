# AgentNav Docs Drift Detector DAG

## What it does

The `agentnav_docs_drift_detector` DAG runs daily and compares the current
structure of two live documentation sites against the AgentNav baseline
`agents.json` files stored in the [baekenough/AgentNav](https://github.com/baekenough/AgentNav)
repository.

When pages are added to or removed from a live documentation site, the DAG
opens a GitHub issue on the AgentNav repo so maintainers know the
`agents.txt`/`agents.json` files need updating.

### Sites monitored

| Site | Live source | AgentNav baseline |
|---|---|---|
| Claude Platform Docs | `https://platform.claude.com/sitemap.xml` (filtered to `/docs/en/` paths) | `public/claude-code/agents.json` |
| Codex Docs | `https://developers.openai.com/codex/llms.txt` | `public/gpt-codex/agents.json` |

> **Note:** The Claude baseline comparison accounts for SDK pattern expansion
> (10 SDKs × 45 endpoints = 450 pages defined via `sdk_pattern` template in
> `agents.json`). The Codex llms.txt parser strips `.md` suffixes from live
> URLs for consistent path comparison with the baseline.

### Task graph

```
fetch_claude_sitemap ──┐
                       ├─► compare_claude ──┐
fetch_agentnav_claude ─┘                    │
                                            ├─► generate_report ─► notify_if_drift
fetch_codex_llms_txt ──┐                    │
                       ├─► compare_codex ───┘
fetch_agentnav_codex ──┘
```

---

## Requirements

### Python packages

`requests` is the only non-standard dependency and is pre-installed in most
Airflow distributions. Verify with:

```bash
python -c "import requests; print(requests.__version__)"
```

If not present, install it:

```bash
pip install requests
```

### Airflow version

Airflow 3.x (tested on 3.1.8) with TaskFlow API support.

---

## Configuration

### Required: GitHub Token

A GitHub personal access token (PAT) with `repo` scope (specifically
`issues: write`) is required to create drift-detection issues.

Set it in **one** of two ways (Airflow Variable takes precedence):

**Option A – Airflow Variable (recommended)**

```bash
airflow variables set agentnav_github_token ghp_your_token_here
```

Or via the Airflow UI: Admin → Variables → Add.

**Option B – Environment variable**

```bash
export GITHUB_TOKEN=ghp_your_token_here
```

### Optional: Target repository

By default issues are opened on `baekenough/AgentNav`. To override:

```bash
airflow variables set agentnav_github_repo your-org/your-repo
```

---

## How to test locally

### 1. Parse check (no Airflow needed)

Verify the DAG file has no syntax errors and can be imported:

```bash
python dags/agentnav_docs_drift.py
```

### 2. Airflow DAG import check

```bash
airflow dags list | grep agentnav
```

If the DAG appears without errors, the file parses correctly.

### 3. Airflow standalone (single-machine test)

```bash
airflow standalone
# In another terminal:
airflow dags test agentnav_docs_drift_detector 2026-03-13
```

This runs all tasks sequentially with full logging output without writing
to the metadata database.

### 4. Test individual tasks

```bash
# Run only the Claude sitemap fetch
airflow tasks test agentnav_docs_drift_detector fetch_claude_sitemap 2026-03-13

# Run only the Codex llms.txt fetch
airflow tasks test agentnav_docs_drift_detector fetch_codex_llms_txt 2026-03-13
```

### 5. Dry-run notification (no real GitHub issue)

Set a dummy token to exercise the full path through `notify_if_drift` without
actually creating a GitHub issue – the task will fail at the API call stage
with an authentication error (HTTP 401), confirming the logic path was reached:

```bash
airflow variables set agentnav_github_token test-token
airflow tasks test agentnav_docs_drift_detector notify_if_drift 2026-03-13
```

---

## Expected behavior on drift detection

When one or more pages are added to or removed from a monitored documentation
site since the last AgentNav baseline snapshot:

1. `compare_claude` or `compare_codex` (or both) sets `drift_detected: True`.
2. `generate_report` aggregates both diffs into a Markdown report listing the
   exact added and removed paths per site.
3. `notify_if_drift` creates a GitHub issue on the AgentNav repo with:
   - **Title:** `[Drift Detected] Documentation structure changed - YYYY-MM-DD`
   - **Body:** The full Markdown drift report
   - **Labels:** `automated`, `drift-detection`
4. Before creating a new issue, the DAG checks for existing open issues with the `drift-detection` label using the GitHub REST List Issues API (not the Search API, which is eventually consistent). If one already exists, creation is skipped to prevent duplicate alerts.
5. Airflow logs the full report at `INFO` level regardless of drift status.

When no drift is detected, `notify_if_drift` logs "No documentation drift
detected" and exits without creating an issue.

---

## Error handling

The DAG distinguishes between transient and permanent errors:

- **Transient** (timeouts, connection errors, HTTP 5xx/429): allows Airflow to retry
  per `default_args` (`retries=1`, `retry_delay=5m`)
- **Permanent** (HTTP 4xx, malformed data, missing config): fails immediately via
  `AirflowFailException` without retry

If one documentation source fails (e.g., Codex endpoint is down), the other source's
drift results are still reported. The report will note which source was unavailable.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| DAG import error | Missing `requests` package | `pip install requests` |
| `AirflowFailException: GitHub token not found` | Neither Variable nor env var set | Set `agentnav_github_token` Variable |
| HTTP 401 from GitHub API | Invalid or expired token | Rotate the PAT and update the Variable |
| HTTP 422 from GitHub API | Label `drift-detection` or `automated` does not exist on the repo | Create both labels in the GitHub repo settings |
| `No /docs/en/ paths found in sitemap` | Sitemap structure changed | Check `https://platform.claude.com/sitemap.xml` manually |
| `No URLs extracted from llms.txt` | llms.txt format changed | Check `https://developers.openai.com/codex/llms.txt` manually and update the parsing logic in `fetch_codex_llms_txt` |
| Duplicate drift issues created daily | Issue deduplication check failing silently | Check GitHub API token permissions; ensure `drift-detection` label exists on the repo; verify the REST List Issues API endpoint is accessible |

---

## File structure

```
dags/
  agentnav_docs_drift.py        # Docs drift detection DAG
  claude_code_release_monitor.py # Claude Code release monitoring DAG
  README.md                      # This file
```

---

# Claude Code Release Monitor DAG

## What it does

The `claude_code_release_monitor` DAG runs daily and checks for new releases
of [anthropics/claude-code](https://github.com/anthropics/claude-code) on GitHub.
When a new release is detected that does not yet have a corresponding tracking
issue, the DAG creates one on the
[baekenough/oh-my-customcode](https://github.com/baekenough/oh-my-customcode)
repository.

Each issue includes:
- A 500-character summary of the release notes
- Breaking change detection and highlighted warnings
- A link to the original GitHub release page
- Action item checklist for review

### Task graph

```
fetch_releases ─► filter_new_releases ─► create_issues
```

---

## Requirements

### Python packages

`requests` is the only non-standard dependency (same as the drift detection DAG).

### Airflow version

Airflow 3.x (tested on 3.1.8) with TaskFlow API support.

---

## Configuration

### Required: GitHub Token

The same GitHub token used by the drift detection DAG. Requires `repo` scope
(specifically `issues: write`) on the **target** repository
(`baekenough/oh-my-customcode`).

Set it in **one** of two ways (Airflow Variable takes precedence):

**Option A -- Airflow Variable (recommended)**

```bash
airflow variables set agentnav_github_token ghp_your_token_here
```

**Option B -- Environment variable**

```bash
export GITHUB_TOKEN=ghp_your_token_here
```

### Optional: Target repository

By default issues are opened on `baekenough/oh-my-customcode`. To override:

```bash
airflow variables set omc_github_repo your-org/your-repo
```

### Required labels on target repo

The following labels must exist on the target repository:

| Label | Purpose |
|---|---|
| `automated` | Marks auto-generated issues |
| `claude-code-release` | Identifies release tracking issues; used for deduplication |
| `breaking-change` | (Optional) Auto-applied when breaking changes are detected |

---

## How to test locally

### 1. Parse check (no Airflow needed)

```bash
python dags/claude_code_release_monitor.py
```

### 2. Airflow DAG import check

```bash
airflow dags list | grep claude_code_release
```

### 3. Full DAG test

```bash
airflow dags test claude_code_release_monitor 2026-03-14
```

### 4. Test individual tasks

```bash
# Fetch releases only
airflow tasks test claude_code_release_monitor fetch_releases 2026-03-14

# Filter step (requires fetch_releases output)
airflow tasks test claude_code_release_monitor filter_new_releases 2026-03-14
```

---

## Expected behavior

When new releases are detected:

1. `fetch_releases` retrieves the 5 most recent releases from `anthropics/claude-code`.
2. `filter_new_releases` checks open issues on `baekenough/oh-my-customcode` with the
   `claude-code-release` label. Releases whose `tag_name` appears in an existing issue
   title are filtered out.
3. `create_issues` creates one issue per new release with:
   - **Title:** `[Claude Code {tag_name}] New release detected`
   - **Body:** Summary (max 500 chars) + breaking change section + action items + release link
   - **Labels:** `automated`, `claude-code-release` (plus `breaking-change` if applicable)

When no new releases are found, all tasks log informational messages and exit
without creating issues.

---

## Error handling

Same transient/permanent error distinction as the drift detection DAG:

- **Transient** (timeouts, connection errors, HTTP 5xx/429): allows Airflow to retry
- **Permanent** (HTTP 4xx, malformed data, missing config): fails immediately

If the deduplication check fails (e.g., network error), the DAG proceeds without
dedup and logs a warning. This may result in duplicate issues in rare cases.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `AirflowFailException: GitHub token not found` | Neither Variable nor env var set | Set `agentnav_github_token` Variable |
| HTTP 401 from GitHub API | Invalid or expired token | Rotate the PAT and update the Variable |
| HTTP 403 rate limit | Unauthenticated or token exhausted | Ensure token is set; check rate limit headers |
| HTTP 422 creating issue | Labels do not exist on target repo | Create `automated` and `claude-code-release` labels |
| Duplicate issues created | Dedup check failed silently | Check logs for dedup warnings; verify label exists |
| `Unexpected response from GitHub Releases API` | API response format changed or repo not found | Verify `anthropics/claude-code` is accessible |
