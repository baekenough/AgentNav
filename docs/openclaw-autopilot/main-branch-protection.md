# Main 브랜치 보호 가이드

운영 형태에 따라 `main` 보호를 2가지 모드로 가져갈 수 있습니다.

## A) 팀 협업 모드 (PR 기반)

- Direct push 금지
- Force push 금지
- Branch delete 금지
- PR 리뷰 승인 필요
- conversation resolution required
- admins 포함 동일 정책 적용

## B) 단독 운영 모드 (Single-owner)

> 현재 AgentNav처럼 실질적으로 1인 운영일 때 권장

- Direct push 허용
- Force push 금지
- Branch delete 금지
- PR 리뷰 요구 없음
- status check 고정 없음(CI 안정화 후 추가)

---

## 적용 방법

### 1) 팀 협업 모드 적용 (스크립트)

```bash
./scripts/setup_main_branch_protection.sh --repo owner/repo --approvals 1
```

### 2) 단독 운영 모드 적용 (gh api)

```bash
gh api -X PUT \
  -H "Accept: application/vnd.github+json" \
  repos/owner/repo/branches/main/protection \
  --input - <<'JSON'
{
  "required_status_checks": null,
  "enforce_admins": true,
  "required_pull_request_reviews": null,
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "required_conversation_resolution": false
}
JSON
```

## 참고 파일

- 예시 payload: `docs/openclaw-autopilot/main-branch-protection.example.json`
- 자동 스크립트: `scripts/setup_main_branch_protection.sh`

## 사전 조건

- `gh` 설치
- `gh auth login` 완료
- 저장소 admin 권한
