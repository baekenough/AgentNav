# AgentNav OpenClaw Auto-Pilot Docs Pack

OpenClaw를 control plane으로 두고 AgentNav를 운영 자동화하기 위한 설계/구현 문서 모음입니다.

## 디렉터리 구성

- `db/`
  - `001_init_schema.sql` (MVP 스키마)
  - `002_state_machine.sql` (상태 전이/가드)
- `state-machine.md`
- `backlog-2weeks.md`

- `v2/agent-nav_auto-pilot_v2.ko.md`
  - 확장 설계안 (ADR, 정책 엔진, 계약, 큐, 비용/보안/운영 상세 포함)

- `v3/`
  - `agent-nav_auto-pilot_v3.md`
  - `agent-nav_openclaw-openapi.yaml`
  - `agent-nav_schema.sql`
  - `agent-nav_policy.example.yaml`
  - `agent-nav_benchmark-report.schema.json`
  - `agent-nav_runbook.md`
  - `agent-nav_mvp-backlog.md`
  - `workflows/*.example.yml` (CI/배포 예시)

## 참고

- 활성 workflow(표준 위치):
  - `.github/workflows/agentnav-ci.yml`
  - `.github/workflows/agentnav-deploy-staging.yml`
  - `.github/workflows/agentnav-deploy-prod.yml`
- `agentnav-deploy-staging.yml` 는 main push 시 staging 배포를 수행하고, 성공 시 커밋 메시지의 closing keyword(`Fixes #123` 등)를 읽어 이슈를 자동 close합니다.
- `agentnav-deploy-prod.yml` 는 staging 배포 성공 후 자동 실행되어 prod 배포를 진행합니다. (수동 dispatch도 가능)
- 배포 스크립트:
  - `scripts/deploy_staging.sh`, `scripts/healthcheck_staging.sh`
  - `scripts/deploy_prod.sh`, `scripts/healthcheck_prod.sh`
  - 기본은 no-op 성공이며, 실제 배포는 환경변수(`STAGING_DEPLOY_CMD`, `PROD_DEPLOY_CMD`, `*_HEALTHCHECK_URL`) 설정으로 연결합니다.
- `v3/workflows/*.example.yml` 는 설계 문서에 포함된 **원본 예시 템플릿**입니다.

## main 브랜치 보호

- 가이드: `docs/openclaw-autopilot/main-branch-protection.md`
- 예시 payload: `docs/openclaw-autopilot/main-branch-protection.example.json`
- 적용 스크립트: `scripts/setup_main_branch_protection.sh`
