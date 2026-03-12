# AgentNav Auto-Pilot 2주 GitHub 이슈 백로그 (MVP v1)

> 기준: OpenClaw가 orchestration을 소유하고, GitHub는 코드/CI/CD 실행 기반으로 사용.

## 라벨 규칙 (권장)

- `area:intake|triage|planner|coding|verify|release|ui|infra`
- `type:feature|chore|infra|docs`
- `risk:low|medium|high`
- `priority:P0|P1|P2`
- `mvp:v1`

---

## Week 1 — 코어 파이프라인 구축

### 1) [P0] OpenClaw Issue 스키마 + DB 마이그레이션
- Labels: `area:intake`, `type:feature`, `priority:P0`, `mvp:v1`
- 산출물:
  - `issues`, `issue_runs`, `plans`, `pull_requests`, `deployments`, `benchmarks`, `issue_events`
  - 상태 enum + index
- DoD:
  - 신규 issue insert/query 가능
  - 마이그레이션 롤백 스크립트 존재

### 2) [P0] Issue Intake API (`POST /api/issues`, `GET /api/issues/{id}`)
- Labels: `area:intake`, `type:feature`, `priority:P0`, `mvp:v1`
- 산출물:
  - 입력 검증(필수 필드)
  - issue_code(`ISS-xxxx`) 생성
- DoD:
  - E2E로 issue 생성 후 조회 성공

### 3) [P0] GitHub App 인증/토큰 발급 모듈
- Labels: `area:infra`, `type:infra`, `priority:P0`, `mvp:v1`
- 산출물:
  - App JWT 생성
  - Installation token 교환
- DoD:
  - API로 issue 1건 생성 성공

### 4) [P0] OpenClaw → GitHub issue 동기화 worker
- Labels: `area:intake`, `type:feature`, `priority:P0`, `mvp:v1`
- 산출물:
  - issue.created 이벤트 소비
  - GitHub issue 생성 + 번호 저장
- DoD:
  - OpenClaw issue와 GitHub issue 번호 연결 확인

### 5) [P0] Triage Agent 출력 스키마/정책 엔진
- Labels: `area:triage`, `type:feature`, `priority:P0`, `mvp:v1`
- 산출물:
  - risk/auto_fixable/required_checks 판정
  - `TRIAGED` 상태 전이
- DoD:
  - 샘플 20건에서 스키마 validation 100%

### 6) [P1] 중복 이슈 탐지(키워드 + 임베딩 1차)
- Labels: `area:intake`, `type:feature`, `priority:P1`, `mvp:v1`
- 산출물:
  - 후보 issue top-3 반환
- DoD:
  - 중복 샘플셋에서 재현율 기준 충족(팀 기준 정의)

### 7) [P0] Planner Agent + plan 저장(`plans.version`)
- Labels: `area:planner`, `type:feature`, `priority:P0`, `mvp:v1`
- 산출물:
  - candidate_files/test_plan/rollback_plan 생성
- DoD:
  - TRIAGED→PLANNED 자동 전이 확인

### 8) [P0] Coding Agent 브랜치/커밋/PR 생성 루프
- Labels: `area:coding`, `type:feature`, `priority:P0`, `mvp:v1`
- 산출물:
  - 브랜치 규칙: `openclaw/issue-<no>-<slug>`
  - PR 템플릿 자동 삽입
- DoD:
  - 샘플 bug 1건에서 PR 생성 성공

### 9) [P0] 기본 CI 워크플로우(`ci.yml`) 적용
- Labels: `area:verify`, `type:infra`, `priority:P0`, `mvp:v1`
- 산출물:
  - lint/typecheck/unit/smoke/nav-benchmark 실행
- DoD:
  - PR에서 required checks로 동작

### 10) [P0] GitHub webhook consumer (`issues`, `pull_request`, `check_run`)
- Labels: `area:infra`, `type:feature`, `priority:P0`, `mvp:v1`
- 산출물:
  - 이벤트 멱등 처리(event_id unique)
  - 상태 동기화
- DoD:
  - CI 상태가 OpenClaw timeline에 반영

---

## Week 2 — 배포/정책/운영 안정화

### 11) [P0] Verification Agent (CI/benchmark parser)
- Labels: `area:verify`, `type:feature`, `priority:P0`, `mvp:v1`
- 산출물:
  - checks/pass-fail 정리
  - benchmark delta 계산
- DoD:
  - READY_TO_MERGE 판정 자동화

### 12) [P0] Auto-repair loop (최대 2회)
- Labels: `area:verify`, `type:feature`, `priority:P0`, `mvp:v1`
- 산출물:
  - 실패 signature 분류
  - retry budget 관리
- DoD:
  - 동일 signature 반복 시 human queue 전환

### 13) [P0] Auto-merge 정책 서비스
- Labels: `area:release`, `type:feature`, `priority:P0`, `mvp:v1`
- 산출물:
  - `auto-if-green`/`approval-required` 정책 평가
- DoD:
  - low-risk bug에서 자동 merge 성공

### 14) [P0] Staging 자동 배포 워크플로우(`deploy-staging.yml`)
- Labels: `area:release`, `type:infra`, `priority:P0`, `mvp:v1`
- 산출물:
  - main merge 후 staging 배포
  - health check
- DoD:
  - green merge 1건에서 staging 배포 성공

### 15) [P1] Production 수동 승인 배포(`deploy-prod.yml` + environment reviewers)
- Labels: `area:release`, `type:infra`, `priority:P1`, `mvp:v1`
- 산출물:
  - workflow_dispatch
  - GitHub Environment 승인 게이트
- DoD:
  - 승인 없이는 prod job 시작 불가

### 16) [P1] OpenClaw Execution Timeline UI v1
- Labels: `area:ui`, `type:feature`, `priority:P1`, `mvp:v1`
- 산출물:
  - 상태 전이 타임라인
  - GitHub issue/PR/run 링크
- DoD:
  - 이슈 상세에서 최근 20개 이벤트 표시

### 17) [P1] 알림 정책 연결 (PR 생성/CI 실패/staging 결과/prod 승인 요청)
- Labels: `area:release`, `type:feature`, `priority:P1`, `mvp:v1`
- 산출물:
  - 채널별 템플릿
- DoD:
  - 핵심 이벤트 4종 정상 발송

### 18) [P1] Kill Switch + Budget Limit
- Labels: `area:infra`, `type:feature`, `priority:P1`, `mvp:v1`
- 산출물:
  - auto-merge 중지 플래그
  - auto-deploy 중지 플래그
  - 일일 실행 예산 상한
- DoD:
  - 플래그 ON 시 자동 작업 즉시 중단

### 19) [P1] Runbook 문서화 (장애/롤백/수동개입)
- Labels: `area:docs`, `type:docs`, `priority:P1`, `mvp:v1`
- 산출물:
  - 장애 대응 체크리스트
  - 롤백 절차
- DoD:
  - 온콜이 문서만 보고 롤백 수행 가능

### 20) [P0] 운영 리허설 3회 (Game Day)
- Labels: `area:release`, `type:chore`, `priority:P0`, `mvp:v1`
- 산출물:
  - low-risk bug 자동흐름 2회
  - staging fail→rollback 1회
- DoD:
  - 리허설 리포트 + 개선 액션 5개 이상 도출

---

## 마일스톤 체크

### M1 (Week 1 종료)
- OpenClaw issue → GitHub issue/PR → CI까지 end-to-end 동작

### M2 (Week 2 종료)
- low-risk bug: auto-merge + staging 자동 배포
- prod: 승인형 배포 경로 준비 완료

---

## 권장 담당 체계

- 플랫폼(백엔드/큐/DB): #1, #2, #4, #10, #18
- 에이전트(트리아지/플래너/코딩/검증): #5, #7, #8, #11, #12, #13
- DevOps(CI/CD/환경): #3, #9, #14, #15, #20
- 제품/UI/운영: #16, #17, #19
