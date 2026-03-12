-- 002_state_machine.sql
-- OpenClaw issue state-machine definition + guard registry

BEGIN;

SET search_path = openclaw, public;

CREATE TABLE IF NOT EXISTS transition_guards (
  code          TEXT PRIMARY KEY,
  description   TEXT NOT NULL,
  owner         TEXT NOT NULL DEFAULT 'openclaw-policy',
  created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS issue_state_transitions (
  id            BIGSERIAL PRIMARY KEY,
  from_status   issue_status NOT NULL,
  to_status     issue_status NOT NULL,
  guard_code    TEXT NOT NULL REFERENCES transition_guards(code),
  auto_allowed  BOOLEAN NOT NULL DEFAULT FALSE,
  notes         TEXT,
  UNIQUE(from_status, to_status)
);

CREATE TABLE IF NOT EXISTS issue_transition_log (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  issue_id      UUID NOT NULL REFERENCES issues(id) ON DELETE CASCADE,
  from_status   issue_status NOT NULL,
  to_status     issue_status NOT NULL,
  guard_code    TEXT,
  triggered_by  TEXT NOT NULL,
  trigger_reason TEXT,
  context       JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ---------- GUARD REGISTRY ----------
INSERT INTO transition_guards (code, description) VALUES
  ('triage_completed', 'Triage output exists and persisted'),
  ('needs_human_true', 'Triage marked needs_human=true'),
  ('auto_fixable_true', 'Triage marked auto_fixable=true'),
  ('plan_created', 'Planner output saved'),
  ('coding_started', 'Coding run started'),
  ('pr_created', 'GitHub PR created'),
  ('ci_started', 'CI/check suite started'),
  ('required_check_failed', 'One or more required checks failed'),
  ('checks_green_within_budget', 'All required checks passed and benchmark threshold satisfied'),
  ('retry_available', 'Auto repair retry budget remains'),
  ('retry_exhausted_or_needs_human', 'Auto retries exhausted or repeating failure signature'),
  ('merge_policy_satisfied', 'Merge policy is auto-if-green OR approved by human'),
  ('staging_policy_satisfied', 'Deploy policy allows staging auto deploy'),
  ('staging_healthcheck_passed', 'Staging deploy + health check passed'),
  ('staging_deploy_failed', 'Staging deploy or health check failed'),
  ('prod_approval_required', 'Policy requires prod approval'),
  ('prod_approved', 'Prod approval explicitly granted'),
  ('prod_policy_auto_allowed', 'Policy allows auto prod (default false in prod systems)'),
  ('prod_deploy_failed', 'Prod deploy or health check failed'),
  ('prod_deploy_succeeded', 'Prod deploy and health check succeeded'),
  ('rollback_succeeded', 'Rollback completed with stable artifact'),
  ('reopen_requested', 'Issue reopened after rollback/failure'),
  ('close_condition_met', 'Completion condition met for close')
ON CONFLICT (code) DO NOTHING;

-- ---------- TRANSITION MAP ----------
INSERT INTO issue_state_transitions (from_status, to_status, guard_code, auto_allowed, notes) VALUES
  ('NEW', 'TRIAGED', 'triage_completed', true, 'intake -> triage'),

  ('TRIAGED', 'REJECTED_AUTO', 'needs_human_true', true, 'auto flow rejected to human queue'),
  ('TRIAGED', 'PLANNED', 'auto_fixable_true', true, 'auto flow accepted'),

  ('PLANNED', 'CODING', 'coding_started', true, 'coding agent run started'),
  ('CODING', 'PR_OPEN', 'pr_created', true, 'PR opened'),

  ('PR_OPEN', 'CI_RUNNING', 'ci_started', true, 'GitHub checks running'),
  ('CI_RUNNING', 'CI_FAILED', 'required_check_failed', true, 'CI failed'),
  ('CI_RUNNING', 'READY_TO_MERGE', 'checks_green_within_budget', true, 'all gates passed'),

  ('CI_FAILED', 'CODING', 'retry_available', true, 'auto repair loop'),
  ('CI_FAILED', 'REJECTED_AUTO', 'retry_exhausted_or_needs_human', true, 'handoff to human review'),

  ('READY_TO_MERGE', 'MERGED', 'merge_policy_satisfied', true, 'auto merge or approved merge'),

  ('MERGED', 'STAGING_DEPLOYING', 'staging_policy_satisfied', true, 'start staging deploy'),
  ('STAGING_DEPLOYING', 'STAGING_FAILED', 'staging_deploy_failed', true, 'staging failed'),
  ('STAGING_DEPLOYING', 'STAGING_DEPLOYED', 'staging_healthcheck_passed', true, 'staging success'),

  ('STAGING_FAILED', 'ROLLED_BACK', 'rollback_succeeded', true, 'rollback after staging failure'),

  ('STAGING_DEPLOYED', 'PROD_PENDING_APPROVAL', 'prod_approval_required', true, 'wait for prod approval'),
  ('STAGING_DEPLOYED', 'PROD_DEPLOYING', 'prod_policy_auto_allowed', false, 'rare/no default'),
  ('PROD_PENDING_APPROVAL', 'PROD_DEPLOYING', 'prod_approved', false, 'human gate opened'),

  ('PROD_DEPLOYING', 'PROD_FAILED', 'prod_deploy_failed', true, 'prod failed'),
  ('PROD_DEPLOYING', 'PROD_DEPLOYED', 'prod_deploy_succeeded', true, 'prod success'),

  ('PROD_FAILED', 'ROLLED_BACK', 'rollback_succeeded', true, 'rollback after prod failure'),

  ('ROLLED_BACK', 'REOPENED', 'reopen_requested', true, 'open follow-up cycle'),
  ('REOPENED', 'PLANNED', 'plan_created', true, 're-planning after reopen'),

  ('PROD_DEPLOYED', 'CLOSED', 'close_condition_met', true, 'workflow done')
ON CONFLICT (from_status, to_status) DO NOTHING;

-- ---------- UPDATED_AT HELPER ----------
CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_issues_updated_at ON issues;
CREATE TRIGGER trg_issues_updated_at
BEFORE UPDATE ON issues
FOR EACH ROW
EXECUTE FUNCTION set_updated_at();

-- ---------- GUARD EVALUATOR (MVP) ----------
-- 실제 운영에서는 policy-engine 서비스에서 평가하는 것을 권장.
CREATE OR REPLACE FUNCTION can_transition(
  p_issue_id UUID,
  p_to_status issue_status,
  p_context JSONB DEFAULT '{}'::jsonb
)
RETURNS BOOLEAN AS $$
DECLARE
  v_from issue_status;
  v_guard TEXT;
BEGIN
  SELECT status INTO v_from FROM issues WHERE id = p_issue_id;
  IF v_from IS NULL THEN
    RETURN FALSE;
  END IF;

  SELECT guard_code INTO v_guard
  FROM issue_state_transitions
  WHERE from_status = v_from AND to_status = p_to_status;

  IF v_guard IS NULL THEN
    RETURN FALSE;
  END IF;

  RETURN CASE v_guard
    WHEN 'triage_completed' THEN COALESCE((p_context->>'triage_completed')::BOOLEAN, FALSE)
    WHEN 'needs_human_true' THEN COALESCE((p_context->>'needs_human')::BOOLEAN, FALSE)
    WHEN 'auto_fixable_true' THEN COALESCE((p_context->>'auto_fixable')::BOOLEAN, FALSE)
    WHEN 'plan_created' THEN COALESCE((p_context->>'plan_created')::BOOLEAN, FALSE)
    WHEN 'coding_started' THEN COALESCE((p_context->>'coding_started')::BOOLEAN, FALSE)
    WHEN 'pr_created' THEN COALESCE((p_context->>'pr_created')::BOOLEAN, FALSE)
    WHEN 'ci_started' THEN COALESCE((p_context->>'ci_started')::BOOLEAN, FALSE)
    WHEN 'required_check_failed' THEN COALESCE((p_context->>'required_check_failed')::BOOLEAN, FALSE)
    WHEN 'checks_green_within_budget' THEN COALESCE((p_context->>'checks_green_within_budget')::BOOLEAN, FALSE)
    WHEN 'retry_available' THEN COALESCE((p_context->>'retry_available')::BOOLEAN, FALSE)
    WHEN 'retry_exhausted_or_needs_human' THEN COALESCE((p_context->>'retry_exhausted_or_needs_human')::BOOLEAN, FALSE)
    WHEN 'merge_policy_satisfied' THEN COALESCE((p_context->>'merge_policy_satisfied')::BOOLEAN, FALSE)
    WHEN 'staging_policy_satisfied' THEN COALESCE((p_context->>'staging_policy_satisfied')::BOOLEAN, FALSE)
    WHEN 'staging_healthcheck_passed' THEN COALESCE((p_context->>'staging_healthcheck_passed')::BOOLEAN, FALSE)
    WHEN 'staging_deploy_failed' THEN COALESCE((p_context->>'staging_deploy_failed')::BOOLEAN, FALSE)
    WHEN 'prod_approval_required' THEN COALESCE((p_context->>'prod_approval_required')::BOOLEAN, FALSE)
    WHEN 'prod_approved' THEN COALESCE((p_context->>'prod_approved')::BOOLEAN, FALSE)
    WHEN 'prod_policy_auto_allowed' THEN COALESCE((p_context->>'prod_policy_auto_allowed')::BOOLEAN, FALSE)
    WHEN 'prod_deploy_failed' THEN COALESCE((p_context->>'prod_deploy_failed')::BOOLEAN, FALSE)
    WHEN 'prod_deploy_succeeded' THEN COALESCE((p_context->>'prod_deploy_succeeded')::BOOLEAN, FALSE)
    WHEN 'rollback_succeeded' THEN COALESCE((p_context->>'rollback_succeeded')::BOOLEAN, FALSE)
    WHEN 'reopen_requested' THEN COALESCE((p_context->>'reopen_requested')::BOOLEAN, FALSE)
    WHEN 'close_condition_met' THEN COALESCE((p_context->>'close_condition_met')::BOOLEAN, FALSE)
    ELSE FALSE
  END;
END;
$$ LANGUAGE plpgsql;

-- ---------- TRANSITION APPLY API ----------
CREATE OR REPLACE FUNCTION apply_transition(
  p_issue_id UUID,
  p_to_status issue_status,
  p_triggered_by TEXT,
  p_trigger_reason TEXT DEFAULT NULL,
  p_context JSONB DEFAULT '{}'::jsonb
)
RETURNS BOOLEAN AS $$
DECLARE
  v_from issue_status;
  v_guard TEXT;
BEGIN
  SELECT status INTO v_from FROM issues WHERE id = p_issue_id FOR UPDATE;
  IF v_from IS NULL THEN
    RETURN FALSE;
  END IF;

  SELECT guard_code INTO v_guard
  FROM issue_state_transitions
  WHERE from_status = v_from AND to_status = p_to_status;

  IF v_guard IS NULL THEN
    RETURN FALSE;
  END IF;

  IF NOT can_transition(p_issue_id, p_to_status, p_context) THEN
    RETURN FALSE;
  END IF;

  UPDATE issues
  SET status = p_to_status
  WHERE id = p_issue_id;

  INSERT INTO issue_transition_log (
    issue_id, from_status, to_status, guard_code,
    triggered_by, trigger_reason, context
  ) VALUES (
    p_issue_id, v_from, p_to_status, v_guard,
    p_triggered_by, p_trigger_reason, p_context
  );

  RETURN TRUE;
END;
$$ LANGUAGE plpgsql;

COMMIT;
