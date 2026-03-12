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

- `v3/workflows/*.example.yml` 는 **예시 템플릿**입니다.
- 실제 운영 repo에 적용할 때는 해당 repo의 스크립트/의존성 구조에 맞게 조정 후 `.github/workflows/`로 옮겨 사용하세요.

## main 브랜치 보호

- 가이드: `docs/openclaw-autopilot/main-branch-protection.md`
- 예시 payload: `docs/openclaw-autopilot/main-branch-protection.example.json`
- 적용 스크립트: `scripts/setup_main_branch_protection.sh`
