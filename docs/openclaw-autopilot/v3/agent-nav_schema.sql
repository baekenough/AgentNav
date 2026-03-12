-- AgentNav / OpenClaw control-plane schema draft

create table if not exists issues (
  id uuid primary key,
  github_issue_number integer unique,
  title text not null,
  type text not null check (type in ('bug','feature','chore','docs','infra')),
  summary text not null,
  expected_behavior text,
  priority text not null check (priority in ('low','medium','high')),
  target_env text not null check (target_env in ('dev','staging','prod')),
  status text not null,
  risk text check (risk in ('low','medium','high')),
  auto_fixable boolean not null default false,
  created_by text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists issue_events (
  id uuid primary key,
  issue_id uuid not null references issues(id) on delete cascade,
  event_type text not null,
  payload jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create table if not exists issue_runs (
  id uuid primary key,
  issue_id uuid not null references issues(id) on delete cascade,
  phase text not null check (phase in ('triage','planning','coding','verification','release','rollback')),
  status text not null check (status in ('queued','running','succeeded','failed','cancelled')),
  agent_name text not null,
  attempt integer not null default 1,
  summary jsonb not null default '{}'::jsonb,
  artifacts jsonb not null default '[]'::jsonb,
  started_at timestamptz,
  ended_at timestamptz,
  created_at timestamptz not null default now()
);

create table if not exists plans (
  id uuid primary key,
  issue_id uuid not null references issues(id) on delete cascade,
  version integer not null,
  content_markdown text not null,
  candidate_files jsonb not null default '[]'::jsonb,
  verification_plan jsonb not null default '{}'::jsonb,
  approved boolean not null default false,
  created_at timestamptz not null default now(),
  unique(issue_id, version)
);

create table if not exists pull_requests (
  id uuid primary key,
  issue_id uuid not null references issues(id) on delete cascade,
  github_pr_number integer not null,
  branch_name text not null,
  head_sha text,
  merge_commit_sha text,
  status text not null check (status in ('open','merged','closed')),
  ci_status text check (ci_status in ('pending','pass','fail')),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique(github_pr_number)
);

create table if not exists benchmark_reports (
  id uuid primary key,
  issue_id uuid references issues(id) on delete set null,
  pull_request_id uuid references pull_requests(id) on delete set null,
  suite_name text not null,
  commit_sha text not null,
  success_rate numeric(6,4) not null,
  avg_steps numeric(10,4),
  avg_cost_usd numeric(12,4),
  avg_latency_ms numeric(12,2),
  crash_count integer not null default 0,
  report_json jsonb not null,
  baseline_report_id uuid references benchmark_reports(id) on delete set null,
  created_at timestamptz not null default now()
);

create table if not exists policy_decisions (
  id uuid primary key,
  issue_id uuid not null references issues(id) on delete cascade,
  policy_name text not null,
  input_context jsonb not null,
  output_decision jsonb not null,
  created_at timestamptz not null default now()
);

create table if not exists deployments (
  id uuid primary key,
  issue_id uuid references issues(id) on delete set null,
  pull_request_id uuid references pull_requests(id) on delete set null,
  environment text not null check (environment in ('staging','prod')),
  artifact_version text not null,
  status text not null check (status in ('pending','running','succeeded','failed','rolled_back')),
  health_summary jsonb not null default '{}'::jsonb,
  rollback_of uuid references deployments(id) on delete set null,
  approved_by text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists approvals (
  id uuid primary key,
  issue_id uuid not null references issues(id) on delete cascade,
  scope text not null check (scope in ('merge','production-deploy','rollback')),
  approved_by text not null,
  comment text,
  created_at timestamptz not null default now()
);

create table if not exists artifacts (
  id uuid primary key,
  issue_id uuid references issues(id) on delete set null,
  issue_run_id uuid references issue_runs(id) on delete set null,
  artifact_type text not null,
  storage_uri text not null,
  checksum_sha256 text,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create table if not exists budgets (
  id uuid primary key,
  issue_id uuid references issues(id) on delete cascade,
  llm_cost_usd numeric(12,4) not null default 0,
  benchmark_cost_usd numeric(12,4) not null default 0,
  deploy_cost_usd numeric(12,4) not null default 0,
  total_cost_usd numeric(12,4) not null default 0,
  status text not null check (status in ('within_limit','warning','blocked')),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists idx_issue_events_issue_id on issue_events(issue_id);
create index if not exists idx_issue_runs_issue_id on issue_runs(issue_id);
create index if not exists idx_plans_issue_id on plans(issue_id);
create index if not exists idx_pull_requests_issue_id on pull_requests(issue_id);
create index if not exists idx_deployments_issue_id on deployments(issue_id);
create index if not exists idx_artifacts_issue_id on artifacts(issue_id);
