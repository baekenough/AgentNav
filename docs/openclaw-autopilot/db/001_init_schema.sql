-- 001_init_schema.sql
-- OpenClaw AgentNav Auto-Pilot MVP schema

BEGIN;

CREATE EXTENSION IF NOT EXISTS pgcrypto;
CREATE SCHEMA IF NOT EXISTS openclaw;
SET search_path = openclaw, public;

-- ========== ENUMS ==========
CREATE TYPE issue_type AS ENUM ('bug', 'feature', 'chore', 'docs', 'infra');
CREATE TYPE issue_status AS ENUM (
  'NEW',
  'TRIAGED',
  'REJECTED_AUTO',
  'PLANNED',
  'CODING',
  'PR_OPEN',
  'CI_RUNNING',
  'CI_FAILED',
  'READY_TO_MERGE',
  'MERGED',
  'STAGING_DEPLOYING',
  'STAGING_FAILED',
  'STAGING_DEPLOYED',
  'PROD_PENDING_APPROVAL',
  'PROD_DEPLOYING',
  'PROD_FAILED',
  'PROD_DEPLOYED',
  'ROLLED_BACK',
  'REOPENED',
  'CLOSED'
);

CREATE TYPE risk_level AS ENUM ('low', 'medium', 'high');
CREATE TYPE target_env AS ENUM ('dev', 'staging', 'prod');
CREATE TYPE run_phase AS ENUM ('triage', 'planning', 'coding', 'verify', 'release');
CREATE TYPE run_status AS ENUM ('queued', 'running', 'succeeded', 'failed', 'canceled');
CREATE TYPE pr_status AS ENUM ('open', 'merged', 'closed');
CREATE TYPE ci_status AS ENUM ('pending', 'running', 'pass', 'fail');
CREATE TYPE deploy_env AS ENUM ('staging', 'prod');
CREATE TYPE deployment_status AS ENUM ('pending', 'running', 'succeeded', 'failed', 'rolled_back');

-- ========== CORE TABLES ==========
CREATE TABLE issues (
  id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  issue_code          TEXT UNIQUE NOT NULL,
  github_issue_number INTEGER UNIQUE,

  title               TEXT NOT NULL,
  type                issue_type NOT NULL,
  status              issue_status NOT NULL DEFAULT 'NEW',
  risk                risk_level,
  auto_fixable        BOOLEAN,
  target_env          target_env NOT NULL DEFAULT 'staging',
  auto_fix_opt_in     BOOLEAN NOT NULL DEFAULT TRUE,

  summary             TEXT,
  expected_behavior   TEXT,
  repro_steps         JSONB NOT NULL DEFAULT '[]'::jsonb,
  logs                JSONB NOT NULL DEFAULT '{}'::jsonb,
  attachments         JSONB NOT NULL DEFAULT '[]'::jsonb,
  priority            TEXT,

  merge_policy        TEXT,
  deploy_policy       TEXT,

  created_by          TEXT,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE issue_runs (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  issue_id      UUID NOT NULL REFERENCES issues(id) ON DELETE CASCADE,
  phase         run_phase NOT NULL,
  status        run_status NOT NULL DEFAULT 'queued',
  agent_name    TEXT,

  started_at    TIMESTAMPTZ,
  ended_at      TIMESTAMPTZ,

  summary       JSONB NOT NULL DEFAULT '{}'::jsonb,
  artifacts     JSONB NOT NULL DEFAULT '{}'::jsonb,

  created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE plans (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  issue_id          UUID NOT NULL REFERENCES issues(id) ON DELETE CASCADE,
  version           INTEGER NOT NULL,

  content_markdown  TEXT NOT NULL,
  candidate_files   JSONB NOT NULL DEFAULT '[]'::jsonb,
  test_plan         JSONB NOT NULL DEFAULT '{}'::jsonb,
  rollback_plan     TEXT,

  approved          BOOLEAN NOT NULL DEFAULT FALSE,
  approved_by       TEXT,
  approved_at       TIMESTAMPTZ,

  created_at        TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  UNIQUE(issue_id, version)
);

CREATE TABLE pull_requests (
  id                 UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  issue_id           UUID NOT NULL REFERENCES issues(id) ON DELETE CASCADE,

  github_pr_number   INTEGER UNIQUE,
  branch_name        TEXT NOT NULL,
  merge_commit_sha   TEXT,

  status             pr_status NOT NULL DEFAULT 'open',
  ci_status          ci_status NOT NULL DEFAULT 'pending',

  checks             JSONB NOT NULL DEFAULT '{}'::jsonb,
  benchmark_delta    JSONB NOT NULL DEFAULT '{}'::jsonb,

  created_at         TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at         TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE deployments (
  id                 UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  issue_id           UUID NOT NULL REFERENCES issues(id) ON DELETE CASCADE,
  pr_id              UUID REFERENCES pull_requests(id) ON DELETE SET NULL,

  environment        deploy_env NOT NULL,
  artifact_version   TEXT NOT NULL,
  status             deployment_status NOT NULL DEFAULT 'pending',

  health_summary     JSONB NOT NULL DEFAULT '{}'::jsonb,
  rollback_of        UUID REFERENCES deployments(id) ON DELETE SET NULL,
  reason             TEXT,

  started_at         TIMESTAMPTZ,
  ended_at           TIMESTAMPTZ,
  created_at         TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE benchmarks (
  id               UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  pr_id            UUID NOT NULL REFERENCES pull_requests(id) ON DELETE CASCADE,

  suite_name       TEXT NOT NULL,
  success_rate     NUMERIC,
  avg_steps        NUMERIC,
  avg_cost         NUMERIC,
  avg_latency_ms   NUMERIC,
  crash_count      INTEGER,

  raw_report       JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at       TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- 내부 이벤트 버스/감사 저장용
CREATE TABLE issue_events (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  event_type    TEXT NOT NULL,
  event_id      TEXT UNIQUE,
  issue_id      UUID REFERENCES issues(id) ON DELETE CASCADE,

  payload       JSONB NOT NULL DEFAULT '{}'::jsonb,
  occurred_at   TIMESTAMPTZ NOT NULL,
  received_at   TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ========== INDEXES ==========
CREATE INDEX idx_issues_status            ON issues(status);
CREATE INDEX idx_issues_risk              ON issues(risk);
CREATE INDEX idx_issues_created_at        ON issues(created_at DESC);
CREATE INDEX idx_issue_runs_issue_phase   ON issue_runs(issue_id, phase);
CREATE INDEX idx_plans_issue_version      ON plans(issue_id, version DESC);
CREATE INDEX idx_pr_issue_status          ON pull_requests(issue_id, status);
CREATE INDEX idx_deploy_issue_env         ON deployments(issue_id, environment, created_at DESC);
CREATE INDEX idx_benchmarks_pr_suite      ON benchmarks(pr_id, suite_name, created_at DESC);
CREATE INDEX idx_issue_events_issue_time  ON issue_events(issue_id, occurred_at DESC);
CREATE INDEX idx_issue_events_type_time   ON issue_events(event_type, occurred_at DESC);

COMMIT;
