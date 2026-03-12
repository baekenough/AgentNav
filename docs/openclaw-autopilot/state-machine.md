# Issue State Machine (Enum + Guard)

## 상태 Enum

`NEW -> TRIAGED -> PLANNED -> CODING -> PR_OPEN -> CI_RUNNING -> READY_TO_MERGE -> MERGED -> STAGING_DEPLOYING -> STAGING_DEPLOYED -> PROD_PENDING_APPROVAL -> PROD_DEPLOYING -> PROD_DEPLOYED -> CLOSED`

예외/실패 흐름:
- `TRIAGED -> REJECTED_AUTO`
- `CI_RUNNING -> CI_FAILED -> CODING(재시도) | REJECTED_AUTO(인간 검토)`
- `STAGING_DEPLOYING -> STAGING_FAILED -> ROLLED_BACK -> REOPENED -> PLANNED`
- `PROD_DEPLOYING -> PROD_FAILED -> ROLLED_BACK -> REOPENED -> PLANNED`

## Guard 코드

- `triage_completed`
- `needs_human_true`
- `auto_fixable_true`
- `plan_created`
- `coding_started`
- `pr_created`
- `ci_started`
- `required_check_failed`
- `checks_green_within_budget`
- `retry_available`
- `retry_exhausted_or_needs_human`
- `merge_policy_satisfied`
- `staging_policy_satisfied`
- `staging_healthcheck_passed`
- `staging_deploy_failed`
- `prod_approval_required`
- `prod_approved`
- `prod_policy_auto_allowed`
- `prod_deploy_failed`
- `prod_deploy_succeeded`
- `rollback_succeeded`
- `reopen_requested`
- `close_condition_met`

> 실제 평가는 정책 엔진(애플리케이션 레이어)에서 수행하고, DB는 전이 허용 관계와 감사 로그를 보관하는 방식이 권장됩니다.
