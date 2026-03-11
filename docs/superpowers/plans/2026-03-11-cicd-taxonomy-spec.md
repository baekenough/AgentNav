# AgentNav CI/CD + Taxonomy + Spec Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Improve CI/CD noise filtering, normalize M5 taxonomy to v0.2 spec, and finalize the agents.txt v0.2 specification.

**Architecture:** Four independent workstreams executed in phases. CI/CD changes modify detect_changes.py output + workflow issue routing. Taxonomy changes update agents.json type mappings + version bump. Format regeneration runs after JSON updates. Spec finalization cleans up the v0.2 document.

**Tech Stack:** Python 3.12, GitHub Actions, JSON, Markdown

---

## Chunk 1: CI/CD Noise Filtering

### Task 1: Modify detect_changes.py — Add change severity classification

**Files:**
- Modify: `scripts/detect_changes.py`

- [ ] **Step 1: Add severity classification to _build_gha_markers**

Add `CHANGE_SEVERITY=metadata|structural` output line. Currently all scheduled detections are metadata-only (upstream llms.txt, changelog, atom feed changes). Structural changes only come from agents.json push triggers.

The `_build_gha_markers` function should output:
```
CHANGES_DETECTED=true
CHANGE_SEVERITY=metadata
SOURCE_NAME=claude-code,gpt-codex
```

- [ ] **Step 2: Update run() to include severity in report**

Add `"severity": "metadata"` to the report dict. All schedule-detected changes are metadata severity.

### Task 2: Modify workflow — Issue separation by severity

**Files:**
- Modify: `.github/workflows/sync-docs.yml`

- [ ] **Step 1: Parse CHANGE_SEVERITY from detection output**

Add to the detect step:
```bash
SEVERITY=$(grep "^CHANGE_SEVERITY=" /tmp/detect-output.txt | cut -d= -f2 || echo "metadata")
echo "severity=$SEVERITY" >> "$GITHUB_OUTPUT"
```

- [ ] **Step 2: Update issue creation logic**

When severity=metadata:
- Search for open issue with `meta-only,automated` labels
- If exists → append comment
- If not → create new issue with `meta-only,automated` labels and title "Upstream metadata changes detected"

When severity=structural (future, from agents.json diff):
- Always create new issue with `doc-update,automated` labels

- [ ] **Step 3: Create meta-only label on GitHub**

```bash
gh label create "meta-only" --description "Metadata-only upstream changes (no agents.json impact)" --color "c5def5"
```

---

## Chunk 2: M5 Taxonomy Normalization

### Task 3: Update agents.json files

**Files:**
- Modify: `public/claude-code/agents.json`
- Modify: `public/gpt-codex/agents.json`

- [ ] **Step 1: Fix sdk-overview type in claude-code**

Change `"type": "sdk-overview"` → `"type": "sdk-guide"` for all 7 SDK overview pages in the SDK Overviews subsection.

- [ ] **Step 2: Bump version in claude-code**

Change `"agents_txt_version": "0.1"` → `"agents_txt_version": "0.2"`

- [ ] **Step 3: Bump version in gpt-codex**

Change `"agents_txt_version": "0.1"` → `"agents_txt_version": "0.2"`

### Task 4: Regenerate all formats

**Files:**
- Regenerate: `public/claude-code/agents.{md,xml,txt}`
- Regenerate: `public/gpt-codex/agents.{md,xml,txt}`

- [ ] **Step 1: Run format generator**

```bash
python scripts/generate_formats.py --all
```

- [ ] **Step 2: Verify output diff**

```bash
git diff --stat public/
```

Expected: version bump + sdk-overview→sdk-guide changes in all format files.

---

## Chunk 3: v0.2 Spec Finalization

### Task 5: Clean up spec document

**Files:**
- Modify: `docs/spec/agents-txt-v0.2.md`

- [ ] **Step 1: Update status**

Change `**Status**: Draft` → `**Status**: Published`

- [ ] **Step 2: Replace local paths with relative paths**

Replace all `/Users/sangyi/workspace/projects/AgentNav/` references with relative paths or URLs:
- `/Users/sangyi/workspace/projects/AgentNav/NAV-AGENT.md` → `../../NAV-AGENT.md`
- `/Users/sangyi/workspace/projects/AgentNav/docs/plan/ground-truth.md` → `../plan/ground-truth.md`

- [ ] **Step 3: Add sdk-overview deprecation note**

In the Content Type Taxonomy section (§4), add a note: `sdk-overview` was used in v0.1 and has been replaced by `sdk-guide` in v0.2.

---

## Chunk 4: Deploy Environment + Commit

### Task 6: Create GitHub production environment

- [ ] **Step 1: Create production environment**

```bash
gh api repos/baekenough/AgentNav/environments/production -X PUT
```

### Task 7: Commit all changes

- [ ] **Step 1: Stage and commit via mgr-gitnerd**

Commit message: `feat: CI/CD noise filtering, M5 taxonomy normalization, v0.2 spec finalization`

---

## Execution Order

```
Phase 1 (parallel):
  ├─ Task 1+2: CI/CD changes (detect_changes.py + workflow)
  ├─ Task 3: agents.json taxonomy + version bump
  └─ Task 5: v0.2 spec cleanup

Phase 2 (sequential, after Task 3):
  └─ Task 4: Format regeneration

Phase 3 (parallel):
  ├─ Task 6: GitHub environment
  └─ Task 7: Commit
```
