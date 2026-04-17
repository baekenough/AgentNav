# Documentation Set Candidates — Evaluation Report

**Date**: 2026-04-17
**Author**: AgentNav research pass (WebFetch-based investigation)
**Context**: AgentNav currently hosts 4 documentation sets (Claude API 1,035p, Claude Code 111p, GPT Codex 71p, Gemini CLI 90p). Previously added Vercel (1,078p) / Supabase (691p) were removed — raw page count alone does not justify inclusion. This report evaluates 4 user-provided candidates plus 9 self-discovered AI-agent-relevant candidates.

---

## Summary Matrix

| # | Candidate | llms.txt URL | Pages (est.) | Quality | Stability | Recommend |
|---|-----------|--------------|--------------|---------|-----------|-----------|
| 1 | Docker | docs.docker.com/llms.txt | ~450 | B | High | Maybe |
| 2 | Stripe | docs.stripe.com/llms.txt | ~400 | B+ | High | Maybe |
| 3 | Convex | docs.convex.dev/llms.txt | ~380 | A | High | **Yes** |
| 4 | Replit | docs.replit.com/llms.txt | ~280 | B | Medium | Defer |
| 5 | LangChain (docs) | docs.langchain.com/llms.txt | ~1,100 | B (noisy) | High | Maybe |
| 6 | LangGraph | langchain-ai.github.io/langgraph/llms.txt | 16 | C (deprecated) | Low | Skip |
| 7 | CrewAI | docs.crewai.com/llms.txt | 343 | B+ | High | **Yes** |
| 8 | Cloudflare | developers.cloudflare.com/llms.txt | ~84 (hub) | B (hub) | High | Maybe |
| 9 | PostHog | posthog.com/llms.txt | ~800 | A | High | **Yes** |
| 10 | Linear | linear.app/llms.txt | 129 | B+ | High | Maybe |
| 11 | Notion API | developers.notion.com/llms.txt | 223 | B | High | Maybe |
| 12 | Railway | docs.railway.com/llms.txt | ~200 | A | High | **Yes** |
| 13 | Prisma | prisma.io/docs/llms.txt | ~650 | A | High | **Yes** |
| 14 | Fly.io | (none found) | — | — | — | Skip |
| 15 | Hono | hono.dev/llms.txt | 70 (hub) | C (hub-only) | Medium | Skip |
| 16 | Mistral AI | docs.mistral.ai/llms.txt | 87 | B | High | Maybe |
| 17 | Pydantic | pydantic.dev/.../llms.txt | ~110 | B | High | Maybe |

---

## Detailed Evaluation — Given Candidates

### 1. Docker

- **llms.txt**: `https://docs.docker.com/llms.txt` (HTTP 200)
- **llms-full.txt**: 404 (not available)
- **Pages**: ~450 links
- **Sections**: 3 (Get started, Guides, Manuals)
- **Structure**: Standard `[Title](URL): Description` markdown, no metadata header, no version tag
- **Pros**: High-volume, broad coverage (containerization, compose, orchestration). Stable official endpoint.
- **Cons**: Only 3 top-level sections — shallow hierarchy for 450 entries means low taxonomy value. Not strictly llms.txt-spec compliant (no header). Most Docker knowledge is already well-represented in LLM training corpora.
- **AI-agent utility**: Medium. Agents building Dockerfiles benefit from reference, but base knowledge is already strong in LLMs.
- **Verdict**: **Maybe** — host if a Docker-specific agent use case emerges. Risk of Vercel/Supabase pattern (large but low added value).

### 2. Stripe

- **llms.txt**: `https://docs.stripe.com/llms.txt` (HTTP 200)
- **llms-full.txt**: 404
- **Pages**: ~400 links
- **Sections**: 19 (Docs, Payments, Checkout, Connect, Billing, Issuing, etc.)
- **Structure**: Markdown links, well-organized, includes SDK version check hint in header
- **Pros**: Deep taxonomy (19 sections), official enterprise-grade source, frequent updates. Strong value for agentic payment/fintech integrations.
- **Cons**: Not formally llms.txt-compliant (no metadata header). Payment-specific — narrower audience than general dev tools.
- **AI-agent utility**: High for fintech/SaaS billing agents, otherwise low.
- **Verdict**: **Maybe** — depends on whether AgentNav targets fintech-adjacent users. Payment API coverage is excellent.

### 3. Convex

- **llms.txt**: `https://docs.convex.dev/llms.txt` (HTTP 200)
- **llms-full.txt**: HTTP 200 (exists, confirmed)
- **Pages**: ~380 links
- **Sections**: 30 (understanding, functions, database, realtime, auth, agents, ai, components, etc.)
- **Structure**: Best-in-class among candidates — clear taxonomy, includes dedicated `agents` and `ai` sections, references companion llms.txt
- **Pros**: Exceptional llms.txt-standard compliance. Purpose-built taxonomy for AI developers (explicit `agents`, `ai`, `components` sections). Active platform with growing adoption. Full-text companion available.
- **Cons**: Smaller ecosystem than Docker/Stripe. Convex users skew toward AI-first apps — small but aligned audience.
- **AI-agent utility**: **Very high** — directly serves AgentNav's target audience (AI developers). Convex has first-class agent framework support.
- **Verdict**: **Yes (highest-priority among given candidates)** — strongest fit for AgentNav's mission.

### 4. Replit

- **llms.txt**: `https://docs.replit.com/llms.txt` (HTTP 200)
- **llms-full.txt**: HTTP 200 (exists)
- **Pages**: ~280 links
- **Sections**: 14 (Billing, Cloud Services, Agent Features, AI Features, Tutorials, Changelogs, etc.)
- **Structure**: Markdown links, includes Agent/AI sections, mixed with changelog entries
- **Pros**: Has dedicated Replit Agent sections — relevant to AgentNav. Changelog coverage gives temporal context.
- **Cons**: Changelog entries inflate count (2024-2026 weekly entries). Replit platform has had ongoing repositioning — stability concern. Smaller user base than other candidates.
- **AI-agent utility**: Medium — Replit Agent is notable but niche. Changelog noise reduces signal density.
- **Verdict**: **Defer** — monitor Replit Agent evolution. Revisit in 6 months if Replit Agent adoption grows.

---

## Self-Discovered Candidates

### 5. LangChain Docs (unified)

- **llms.txt**: `https://docs.langchain.com/llms.txt` (HTTP 200, via 308 from python.langchain.com)
- **Pages**: ~1,100 links (includes LangSmith, LangGraph, LangChain, Fleet)
- **Sections**: API Refs, LangSmith, Fleet, LangGraph, OSS packages
- **Pros**: Single comprehensive hub for the entire LangChain ecosystem — highest AI-agent relevance by domain.
- **Cons**: Very noisy — first 30 lines are all OAuth/auth endpoint CRUD (Create/List/Remove Connection). Signal-to-noise ratio is poor. Rapid API churn — frequent breaking changes.
- **AI-agent utility**: High domain relevance, low signal quality.
- **Verdict**: **Maybe** — requires post-processing/filtering to prune API CRUD noise. If parser can denoise, high value.

### 6. LangGraph (standalone)

- **llms.txt**: `https://langchain-ai.github.io/langgraph/llms.txt` (HTTP 200)
- **Pages**: 16 links
- **Note**: Header explicitly says "LangGraph documentation has moved to docs.langchain.com"
- **Verdict**: **Skip** — superseded by candidate #5.

### 7. CrewAI

- **llms.txt**: `https://docs.crewai.com/llms.txt` (HTTP 200)
- **Pages**: 343 entries
- **Sections**: 3 (Docs, OpenAPI Specs, Optional)
- **Pros**: Major AI agent framework. Includes OpenAPI specs across 4 language variants.
- **Cons**: Shallow top-level taxonomy (3 sections for 343 entries). API CRUD-heavy.
- **AI-agent utility**: **Very high** — CrewAI is one of the top-3 multi-agent frameworks.
- **Verdict**: **Yes** — direct AgentNav audience alignment.

### 8. Cloudflare Developers

- **llms.txt**: `https://developers.cloudflare.com/llms.txt` (HTTP 200)
- **Pages**: ~84 product-level links (hub page pointing to per-product llms.txt)
- **Structure**: Hub-of-hubs — each product (Workers, R2, D1, etc.) has its own llms.txt
- **Pros**: Workers/AI-Workers/R2/D1 directly relevant to AI agents. Very high stability.
- **Cons**: Requires multi-endpoint parsing (hub → per-product → pages). Parser (`llms_to_agents_json.py`) would need recursion support.
- **AI-agent utility**: High for Cloudflare Workers users.
- **Verdict**: **Maybe** — host only if parser is extended to handle nested llms.txt hubs. Otherwise host a specific product subset (e.g., Workers only).

### 9. PostHog

- **llms.txt**: `https://posthog.com/llms.txt` (HTTP 200)
- **Pages**: ~800 links
- **Sections**: 45+ (Analytics, Feature Flags, LLM Analytics, Data Warehouse, Workflows, etc.)
- **Structure**: Excellent — includes explicit "Instructions for AI Coding Assistants" header with integration wizard guidance
- **Pros**: **Best-structured llms.txt among all candidates**. Explicit AI-agent instructions. `.md` suffix pattern for raw markdown. Dedicated LLM Analytics section.
- **Cons**: Analytics/observability-specific — narrower audience than general dev tools.
- **AI-agent utility**: High for agents instrumenting/observing LLM apps.
- **Verdict**: **Yes** — exemplary llms.txt compliance + AI-observability fit.

### 10. Linear

- **llms.txt**: `https://linear.app/llms.txt` (HTTP 200) — note: `linear.app/docs/llms.txt` 404s
- **Pages**: 129 entries
- **Sections**: 23 (Getting started, Teams, Issues, Projects, Integrations, etc.)
- **Pros**: Clean, well-organized. Good for agents managing project workflows.
- **Cons**: Product-specific — Linear is narrower than GitHub Issues. Much is user-facing UX rather than API.
- **AI-agent utility**: Medium — useful for Linear-integration agents only.
- **Verdict**: **Maybe** — host if Linear API coverage is prioritized; otherwise low-priority.

### 11. Notion API

- **llms.txt**: `https://developers.notion.com/llms.txt` (HTTP 200)
- **Pages**: 223 entries
- **Sections**: 3 (Docs, OpenAPI Specs)
- **Pros**: Developer-focused (API-only, not consumer app). Includes OpenAPI.
- **Cons**: Shallow taxonomy. Notion API has known rate-limit / schema stability issues.
- **AI-agent utility**: Medium-high for knowledge-management agents.
- **Verdict**: **Maybe** — solid fit for agents integrating with Notion as knowledge backend.

### 12. Railway

- **llms.txt**: `https://docs.railway.com/llms.txt` (HTTP 200, note: `railway.com/docs/llms.txt` 404s)
- **llms-full.txt**: exists (referenced in header)
- **Pages**: ~200 entries
- **Sections**: 16 (Platform, AI, Languages, CLI, Build & Deploy, Networking, Observability, Integrations, etc.)
- **Pros**: Excellent llms.txt-standard compliance with metadata header pointing to full-text variant and `.md` suffix pattern. Dedicated AI section. Strong PaaS alternative positioning.
- **Cons**: Smaller than AWS/GCP/Cloudflare. Some overlap with Fly.io / Vercel space.
- **AI-agent utility**: High for agents provisioning deployments.
- **Verdict**: **Yes** — clean, standards-compliant, growing platform.

### 13. Prisma

- **llms.txt**: `https://www.prisma.io/docs/llms.txt` (HTTP 200)
- **Pages**: ~650 entries
- **Sections**: 2 (Latest v7, v6 legacy) — explicit versioning
- **Pros**: Explicit version separation (v7 current, v6 legacy) — strong signal for AI-agent consumption. ORM leader with broad adoption.
- **Cons**: Only 2 top-level sections; versioning done at top, feature taxonomy at page level.
- **AI-agent utility**: Very high — database/ORM is a core agent dev concern.
- **Verdict**: **Yes** — clean versioning + high domain relevance.

### 14. Fly.io

- **llms.txt**: Tried `fly.io/docs/llms.txt`, `fly.io/llms.txt`, `fly.io/docs/llms-full.txt` — all 404
- **Verdict**: **Skip** — no official llms.txt endpoint available as of 2026-04-17.

### 15. Hono

- **llms.txt**: `https://hono.dev/llms.txt` (HTTP 200, but is hub)
- **Pages**: ~70 links (hub to llms-full.txt and llms-small.txt)
- **Pros**: Active web framework, AI-SDK-adjacent (often used in AI agent backends).
- **Cons**: Hub-only; primary content in llms-full.txt or llms-small.txt — requires parser change.
- **Verdict**: **Skip** — defer until Hono provides primary-content llms.txt, or parse llms-full.txt separately.

### 16. Mistral AI

- **llms.txt**: `https://docs.mistral.ai/llms.txt` (HTTP 200)
- **Pages**: 87 entries
- **Sections**: 10 (Agents, Capabilities, Deployment, Getting Started, Guides)
- **Pros**: Major LLM provider with agents + function calling + MCP support. Covers Mistral-specific features.
- **Cons**: Smaller corpus. Not standards-compliant (no metadata header). Mistral market share < Anthropic/OpenAI.
- **AI-agent utility**: Medium-high if agents target multi-LLM routing.
- **Verdict**: **Maybe** — worthwhile for multi-LLM-provider coverage completeness.

### 17. Pydantic

- **llms.txt**: `https://pydantic.dev/docs/validation/latest/llms.txt` (HTTP 200, via 301 from docs.pydantic.dev)
- **Pages**: ~110 entries
- **Sections**: 9 (Get Started, Concepts, API Documentation, Internals, Examples, Integrations, etc.)
- **Pros**: Foundational library for AI-agent dev (Pydantic AI, Pydantic Logfire, LangChain schemas all use it).
- **Cons**: Base Pydantic already well-covered in LLM training data. 110 pages is modest.
- **AI-agent utility**: Medium — high relevance but low incremental value over training data.
- **Verdict**: **Maybe** — low priority given training-corpus overlap.

---

## Prioritized Recommendations

### Tier 1 — Recommend immediately (highest AgentNav fit)

1. **Convex** — Best structural fit. Dedicated agents/ai sections. Full-text companion available. Directly serves AgentNav's AI developer audience. **Strongest signal among given candidates.**
2. **PostHog** — Best-in-class llms.txt compliance. Explicit AI-assistant instructions in header. Covers LLM observability — a growing agent-dev concern.

### Tier 2 — Recommend (strong domain fit)

3. **CrewAI** — Top-3 multi-agent framework, core AgentNav audience.
4. **Prisma** — Clean version separation, high domain relevance.
5. **Railway** — Cleanest llms.txt standards compliance, AI section, deployment agent use case.

### Tier 3 — Maybe (requires specific use case signal)

6. **Stripe** — Enterprise-grade; only if fintech-agent audience prioritized.
7. **Docker** — High volume but low incremental value (Docker knowledge saturated in LLM corpora).
8. **LangChain** — High domain value but low signal quality; needs denoising in parser.
9. **Notion API** — Useful for knowledge-management agents.
10. **Linear** — Project workflow automation agents.
11. **Mistral AI** — Multi-LLM-provider completeness.
12. **Cloudflare** — Only if parser handles nested hubs.

### Tier 4 — Defer / Skip

- **Replit** — **Defer** 6 months; Replit Agent still repositioning.
- **Pydantic** — **Defer**; training-corpus overlap.
- **LangGraph (standalone)** — **Skip**; merged into LangChain docs.
- **Fly.io** — **Skip**; no llms.txt endpoint.
- **Hono** — **Skip** until primary-content llms.txt, or parse llms-full.txt variant instead.

---

## Top 2 Picks with Justification

1. **Convex** — Only candidate with *first-class AI agent taxonomy* (dedicated `agents`, `ai`, `components` sections). Full standards compliance + full-text companion. Audience-align score is the highest: Convex users are already building AI-native apps, exactly AgentNav's target. Low risk of the Vercel/Supabase "big but irrelevant" pattern.

2. **PostHog** — Only candidate whose llms.txt header contains *explicit AI-coding-assistant instructions*. The `.md` suffix pattern is already used by Claude Code's own docs. LLM Analytics section is directly AgentNav-audience-aligned. Sets a reference-quality standard for other hosted sets.

## Exclusions with Reasoning

- **Fly.io** — No llms.txt endpoint exists (verified 3 URL variants, all 404).
- **LangGraph (standalone)** — Redirects to LangChain unified docs; hosting separately would create duplicate/stale content.
- **Hono** — Hub-only file; primary content lives in llms-full.txt which the current parser doesn't target as the root entry.
- **Replit** — Changelog entries inflate page count artificially; platform repositioning creates stability risk for hosted content.
- **Pydantic** — Training-corpus saturation; agent developers already get correct Pydantic behavior from base model knowledge.

---

## Notes on Methodology

- All candidate URLs probed via WebFetch between 2026-04-17 sessions.
- Parser compatibility assumed: standard `[Title](URL): Description` markdown with `##` section headers, matching existing Claude API/Code/Gemini CLI format.
- For candidates requiring nested/recursive parsing (Cloudflare hub-of-hubs, Hono hub-of-full-text), parser extension needed before hosting.
- Vercel/Supabase precedent applied: large page count is not itself a reason to host. Taxonomy depth, AI-agent audience alignment, and signal-to-noise ratio weighted higher.

## Next Steps (if acting on this report)

1. Run `scripts/llms_to_agents_json.py` against Convex and PostHog llms.txt to validate parser compatibility.
2. Open GitHub issues for Tier 1 candidates (Convex, PostHog) with baseline URL counts captured.
3. Extend `scripts/baselines/` to include new sources before scheduling drift detection.
4. Revisit Tier 3 candidates after Tier 1 deployment; measure actual user/agent demand before adding more.
