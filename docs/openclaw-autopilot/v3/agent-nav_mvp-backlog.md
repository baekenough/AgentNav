# AgentNav OpenClaw MVP Backlog

## Epic 1 — Control Plane Foundation
- [ ] Create OpenClaw issue schema and validation
- [ ] Implement issue status machine
- [ ] Add issue timeline persistence
- [ ] Add GitHub App authentication
- [ ] Implement GitHub webhook receiver

## Epic 2 — GitHub Sync + PR Loop
- [ ] Sync OpenClaw issues to GitHub issues
- [ ] Create branch naming convention utility
- [ ] Implement PR creation service
- [ ] Add PR template for auto-generated changes
- [ ] Add labels for risk/type/deploy policy

## Epic 3 — Agent Contracts
- [ ] Triage agent JSON contract
- [ ] Planner agent JSON contract
- [ ] Coding agent JSON contract
- [ ] Verification agent JSON contract
- [ ] Release agent JSON contract

## Epic 4 — CI and Verification
- [ ] Add lint/typecheck/unit workflow
- [ ] Add smoke test harness
- [ ] Add benchmark runner CLI contract
- [ ] Persist benchmark reports
- [ ] Compare benchmark report to baseline

## Epic 5 — Deploy and Approval
- [ ] Add staging deployment workflow
- [ ] Add production deployment workflow with approval gate
- [ ] Add health-check ingest
- [ ] Add rollback endpoint and action
- [ ] Add approval queue UI/API

## Epic 6 — Ops and Safety
- [ ] Add policy engine with default-deny behavior
- [ ] Add cost budget tracking
- [ ] Add artifact checksum support
- [ ] Add pause/resume/retry controls
- [ ] Add incident runbook links into UI

## Definition of Done for MVP
- [ ] OpenClaw issue creates GitHub issue
- [ ] low-risk bug can create PR automatically
- [ ] CI runs and stores artifacts
- [ ] staging deploy can be triggered and recorded
- [ ] prod deploy remains approval-gated
- [ ] rollback path exists and is documented
