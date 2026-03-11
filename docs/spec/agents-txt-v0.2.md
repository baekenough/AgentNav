# agents.txt Specification v0.2

**Status**: Published
**Date**: 2026-03-11
**Reference implementation**: [agentnav.baekenough.com](https://agentnav.baekenough.com)

---

## 1. Overview

agents.txt is a machine-readable documentation sitemap format designed for LLM and AI agent consumption. It enables AI agents to discover, navigate, and understand the structure of a documentation site efficiently — before issuing any page requests.

**Analogy**: agents.txt is to AI agents what `robots.txt` is to web crawlers and `sitemap.xml` is to search engines. Unlike those formats, agents.txt is optimized for LLM token efficiency and semantic navigation rather than crawl priority or indexing.

### Design Goals

1. **Token efficiency** — convey maximum structural information with minimum tokens
2. **Machine parseability** — structured enough for programmatic extraction
3. **Human readability** — understandable by developers without tooling
4. **Navigation utility** — sufficient to answer "which page should I fetch for X?" without fetching anything
5. **Pattern compression** — express repeating structures (e.g., per-SDK API references) without enumerating every page

### Version History

| Version | Status | Notes |
|---------|--------|-------|
| v0.1 | Informal | Initial proof-of-concept, no published schema |
| v0.2 | This document | Formalizes type taxonomy, URL convention, schema, multi-provider support |

---

## 2. Well-Known URL Convention

agents.txt endpoints are served under the `.well-known` directory, following [RFC 8615](https://www.rfc-editor.org/rfc/rfc8615).

```
https://{domain}/.well-known/agents.txt    # Plain text (recommended primary)
https://{domain}/.well-known/agents.md     # Markdown
https://{domain}/.well-known/agents.json   # JSON
https://{domain}/.well-known/agents.xml    # XML
```

All four endpoints represent the same documentation index in different serialization formats. Servers should support all four; the `agents.txt` endpoint is the recommended default for agents that do not specify a format preference.

### Multi-Provider Directory Structure

When a single host serves multiple documentation providers, each provider is scoped to a subdirectory path:

```
https://{domain}/.well-known/agents.json                  # default (first/primary provider)
https://{domain}/{provider}/.well-known/agents.json        # provider-specific
```

Example (AgentNav reference implementation):

```
https://agentnav.baekenough.com/.well-known/agents.json       # Claude docs (primary)
https://agentnav.baekenough.com/claude-code/.well-known/agents.json
https://agentnav.baekenough.com/gpt-codex/.well-known/agents.json
```

Provider subdirectory naming convention: `{vendor}-{product}` in lowercase kebab-case (e.g., `claude-code`, `gpt-codex`, `vercel-docs`).

---

## 3. Format Variants

Four serialization formats are defined. Each has different trade-offs across token efficiency, machine parseability, and human readability.

| Format | MIME Type | Tokens (Claude docs, 651 pages) | Machine Parseability | Human Readability |
|--------|-----------|---------------------------------|----------------------|-------------------|
| TXT | `text/plain` | ~3,200 | Good | Good |
| MD | `text/markdown` | ~5,400 | Good | Best |
| JSON | `application/json` | ~9,600 | Best | Moderate |
| XML | `application/xml` | ~7,000 | Best | Moderate |

Token counts are approximate (4 chars/token estimate) for the Claude platform documentation (651 pages). Counts will vary by site size and sdk_pattern usage.

### Format Selection Guidance

- Use **TXT** or **MD** when token budget is the primary constraint or when the agent processes the response as natural language.
- Use **JSON** or **XML** when the agent will programmatically parse the response to build a lookup table or navigation index.
- **JSON** is preferred over XML for new integrations due to smaller footprint.

---

## 4. Content Type Taxonomy

Every page in an agents.txt response must be annotated with a `type` field drawn from the following controlled vocabulary of 12 types.

| Type | Description | Typical URL patterns |
|------|-------------|----------------------|
| `tutorial` | Getting started guides and quick-start walkthroughs | `quickstart`, `get-started` |
| `reference` | Static reference information that changes infrequently | `glossary`, `pricing`, `deprecations`, `migration-guide` |
| `guide` | Feature-specific how-to guides | `prompt-caching`, `vision`, `streaming`, `batch-processing` |
| `overview` | Section entry points and landing pages | `models/overview`, `features/overview` |
| `use-case` | Use-case-specific implementation guides | `content-moderation`, `ticket-routing`, `customer-support-chat` |
| `tool-reference` | Documentation for a specific tool | `bash-tool`, `web-search-tool`, `text-editor-tool` |
| `sdk-guide` | SDK-specific integration guides (not API reference) | `agent-sdk/python`, `agent-sdk/typescript` |
| `api-reference` | API infrastructure documentation (cross-cutting concerns) | `rate-limits`, `errors`, `versioning`, `authentication` |
| `api-endpoint` | Documentation for a single API endpoint | `messages/create`, `models/list`, `batches/create` |
| `api-hub` | API section hub or landing page aggregating multiple endpoints | `messages`, `admin`, `beta` |
| `best-practices` | Best practice, evaluation, and guardrail guidance | `reduce-hallucinations`, `reduce-latency`, `strengthen-guardrails` |
| `changelog` | Change log or release note entries | `release-notes/overview`, `release-notes/system-prompts` |

> **Note (v0.1 migration):** The `sdk-overview` type used in v0.1 has been replaced by `sdk-guide` in v0.2. Implementations upgrading from v0.1 should reclassify `sdk-overview` pages as `sdk-guide`.

**Classification rule**: choose the most specific type that applies. `api-endpoint` takes precedence over `api-reference`; `tool-reference` takes precedence over `guide`.

---

## 5. Schema

### 5.1 JSON Schema

```json
{
  "agents_txt_version": "0.2",
  "site": {
    "name": "string — human-readable site name",
    "url": "string — canonical base URL of the documentation",
    "total_pages": "integer — total page count across all sections",
    "last_updated": "string — ISO 8601 date (YYYY-MM-DD)"
  },
  "sections": [
    {
      "name": "string — section display name",
      "path_prefix": "string — common URL prefix for all pages in this section",
      "page_count": "integer — number of pages in this section",
      "pages": [
        {
          "path": "string — URL path relative to site.url",
          "title": "string — page title",
          "type": "string — one of the 12 content types",
          "method": "string — HTTP method, required for api-endpoint type (GET|POST|PATCH|DELETE)"
        }
      ],
      "subsections": [
        {
          "name": "string — subsection display name",
          "page_count": "integer — number of pages in this subsection",
          "pages": ["(same structure as sections[].pages)"]
        }
      ]
    }
  ],
  "sdk_pattern": {
    "sdks": ["string — SDK identifier list"],
    "pages_per_sdk": "integer — number of pages per SDK",
    "url_template": "string — URL pattern with {sdk} placeholder",
    "endpoint_paths": ["string — list of endpoint path suffixes"]
  },
  "navigation": {
    "string — intent or topic key": "string — recommended section name or path"
  }
}
```

`sdk_pattern` and `navigation` are optional. All other top-level fields and fields within `sections[].pages[]` are required.

### 5.2 Required vs Optional Fields

| Field | Required | Notes |
|-------|----------|-------|
| `agents_txt_version` | Yes | Must be `"0.2"` for this spec |
| `site.name` | Yes | |
| `site.url` | Yes | Must be a fully-qualified URL |
| `site.total_pages` | Yes | |
| `site.last_updated` | Yes | |
| `sections` | Yes | At least one section required |
| `sections[].name` | Yes | |
| `sections[].path_prefix` | Yes | |
| `sections[].page_count` | Yes | |
| `sections[].pages` | Yes | May be empty `[]` if sdk_pattern covers this section |
| `pages[].path` | Yes | |
| `pages[].title` | Yes | |
| `pages[].type` | Yes | Must be one of the 12 types |
| `pages[].method` | Conditional | Required when `type` is `api-endpoint` |
| `sections[].subsections` | No | Use for sections with internal grouping (e.g., API Reference with Infrastructure, Messages, Admin sub-groups) |
| `subsections[].name` | Yes* | Required when subsections is present |
| `subsections[].page_count` | Yes* | Required when subsections is present |
| `subsections[].pages` | Yes* | Required when subsections is present |
| `sdk_pattern` | No | Use when 2+ SDKs share the same endpoint structure |
| `navigation` | No | Use to provide intent-to-section shortcuts |

### 5.3 Minimal Valid Example

```json
{
  "agents_txt_version": "0.2",
  "site": {
    "name": "Example Docs",
    "url": "https://docs.example.com",
    "total_pages": 5,
    "last_updated": "2026-03-07"
  },
  "sections": [
    {
      "name": "Getting Started",
      "path_prefix": "/docs/getting-started",
      "page_count": 2,
      "pages": [
        { "path": "/docs/getting-started/quickstart", "title": "Quickstart", "type": "tutorial" },
        { "path": "/docs/getting-started/overview", "title": "Overview", "type": "overview" }
      ]
    },
    {
      "name": "API Reference",
      "path_prefix": "/docs/api",
      "page_count": 3,
      "pages": [
        { "path": "/docs/api/messages", "title": "Messages", "type": "api-hub" },
        { "path": "/docs/api/messages/create", "title": "Create Message", "type": "api-endpoint", "method": "POST" },
        { "path": "/docs/api/rate-limits", "title": "Rate Limits", "type": "api-reference" }
      ]
    }
  ]
}
```

---

## 6. SDK Pattern Compression

When a documentation site has multiple SDKs (e.g., Python, TypeScript, Java) each exposing the same set of endpoints, enumerating all pages individually is token-wasteful. The `sdk_pattern` object allows the provider to express this repeating structure once.

### Schema

```json
"sdk_pattern": {
  "sdks": ["python", "typescript", "java", "go", "csharp", "ruby", "php", "kotlin", "terraform", "cli"],
  "pages_per_sdk": 45,
  "url_template": "/docs/en/api/{sdk}/{endpoint}",
  "endpoint_paths": [
    "overview",
    "client",
    "messages",
    "messages/create",
    "models",
    "models/list"
  ],
  "endpoint_types": {
    "hub_pages": ["messages", "messages/batches", "models"],
    "endpoint_pages_type": "api-endpoint"
  }
}
```

### Semantics

- `sdks`: ordered list of SDK identifier strings. Each identifier is substituted for `{sdk}` in `url_template`.
- `pages_per_sdk`: the number of pages each SDK exposes (must be consistent across all SDKs listed).
- `url_template`: a URL template using `{sdk}` as a placeholder. Must match the actual URL structure.
- `endpoint_paths`: the list of path suffixes that, combined with `url_template`, produce the full set of SDK pages. The length of this list must equal `pages_per_sdk`.
- `endpoint_types` (optional): classifies which endpoint paths are hub/index pages (`hub_pages`, type `api-hub`) vs individual endpoints (type specified by `endpoint_pages_type`, default `api-endpoint`).

### When to Use

Use `sdk_pattern` when all of the following are true:
1. Two or more SDKs exist in the documentation.
2. Each SDK exposes the same set of endpoints.
3. The URL structure is `{prefix}/{sdk}/{endpoint}` or a similar templatable pattern.

Do not use `sdk_pattern` if SDK pages differ significantly in structure or content across SDKs. In that case, enumerate each SDK as a separate section.

---

## 7. Navigation Section

The optional `navigation` field provides intent-to-section shortcuts. It is a flat key-value map where keys are common user intents or topics and values are the recommended section name or starting path.

```json
"navigation": {
  "getting started": "Introduction",
  "models": "About Claude / models/overview",
  "api reference": "API Reference",
  "sdk setup": "API Reference / sdks",
  "agent development": "Agent SDK",
  "tool use": "Agents & Tools",
  "testing and evaluation": "Test & Evaluate"
}
```

Navigation hints are advisory. Agents should use them to reduce search scope when the user's intent is clear, but must not treat them as authoritative routing rules.

### Implementation Variations

The `navigation` field supports flexible structures beyond flat key-value maps. Implementations may use nested objects for grouping:

```json
"navigation": {
  "section_selection": {
    "concept_or_feature": "/docs/en/build-with-claude/{feature}",
    "api_endpoint": "/docs/en/api/{resource}/{action}"
  }
}
```

Parsers should handle both flat and nested navigation structures gracefully.

---

## 8. Format Examples

### 8.1 TXT Format

The plain text format uses indented sections and a compact page listing. No formal schema is enforced — the goal is maximum readability with minimum tokens.

```
agents.txt v0.2 | Example Docs | https://docs.example.com | 651 pages | 2026-03-07

SECTIONS
  Introduction (2 pages) — /docs/en/intro, /docs/en/get-started
  About Claude (12 pages) — /docs/en/about-claude/
  Build with Claude (35 pages) — /docs/en/build-with-claude/
  API Reference (546 pages) — /docs/en/api/

NAVIGATION
  getting started -> Introduction
  models -> About Claude / models/overview
  api -> API Reference

SDK PATTERN
  SDKs: python, typescript, java, go, csharp, ruby, php, kotlin, terraform, cli
  45 pages each | /docs/en/api/{sdk}/{endpoint}
```

### 8.2 MD Format

The markdown format uses headings and tables for human readability while remaining parseable.

```markdown
# agents.txt v0.2 — Example Docs

**Site**: https://docs.example.com
**Total pages**: 651
**Last updated**: 2026-03-07

## Sections

| Section | Pages | Path Prefix |
|---------|-------|-------------|
| Introduction | 2 | /docs/en/intro |
| About Claude | 12 | /docs/en/about-claude/ |
| API Reference | 546 | /docs/en/api/ |

## Introduction (2 pages)

| Path | Title | Type |
|------|-------|------|
| /docs/en/intro | Introduction | overview |
| /docs/en/get-started | Quickstart | tutorial |

## SDK Pattern

SDKs: python, typescript, java, go, csharp, ruby, php, kotlin, terraform, cli
45 pages per SDK | URL: `/docs/en/api/{sdk}/{endpoint}`
```

---

## 9. Verification Methodology

The effectiveness of an agents.txt response is measured using the NAV-AGENT verification framework (see `../../NAV-AGENT.md`).

A compliant agents.txt implementation should score at least **B (70%+)** on the NAV-AGENT verification rubric.

### Scoring Metrics

| Metric | Weight | Description |
|--------|--------|-------------|
| M1: Section Discovery | 20% | Fraction of top-level sections an agent can identify from the response |
| M2: Page Coverage | 25% | Fraction of representative pages whose paths can be determined (sampled) |
| M3: Navigation Accuracy | 30% | Fraction of intent-based queries correctly routed to the right page path |
| M4: Pattern Recognition | 15% | Ability to recognize and extrapolate repeating SDK structures |
| M5: Content Classification | 10% | Accuracy of page type annotations against the 12-type taxonomy |

### Grading Scale

| Grade | Score | Interpretation |
|-------|-------|----------------|
| A | 90%+ | Format effectively conveys site structure |
| B | 70-89% | Mostly effective, minor gaps |
| C | 50-69% | Partially effective, notable gaps |
| F | < 50% | Format fails to convey structure |

### Interpretation Notes

- M3 (Navigation Accuracy) carries the highest weight because the core purpose of agents.txt is to enable correct page selection without requiring page fetches.
- M4 (Pattern Recognition) rewards implementations that use `sdk_pattern` or equivalent compression rather than enumerating all SDK pages individually.
- Token efficiency is tracked separately (score/token ratio) and is not part of the primary grade, but is reported for format comparison purposes.

---

## 10. Implementation Notes

### Serving Requirements

- All four format endpoints must return the same documentation coverage.
- Response bodies must be UTF-8 encoded.
- Servers must set appropriate `Content-Type` headers per format.
- Responses should include `Cache-Control` headers; daily or per-deploy invalidation is recommended.

### `page_count` Consistency

The `page_count` in each section must equal the count of pages listed in `pages[]` plus (if sdk_pattern applies to this section) `sdks.length * pages_per_sdk`. The top-level `site.total_pages` must equal the sum of all section `page_count` values.

### Path Format

All `path` values must be URL paths relative to `site.url`, beginning with `/`. They must not include query strings or fragments. They should match the canonical URL path exactly (no trailing slashes unless the site uses them consistently).

### Backward Compatibility

Parsers implementing v0.2 must ignore unknown fields rather than rejecting the document. This enables forward-compatible extension without breaking existing consumers.

---

## 11. Changes from v0.1

| Area | v0.1 | v0.2 |
|------|------|------|
| Content types | Informal, ad hoc | Formalized 12-type taxonomy |
| URL convention | No standard | Well-known URL convention defined |
| Multi-provider | Not addressed | Provider subdirectory structure defined |
| SDK compression | Not defined | `sdk_pattern` schema formalized |
| Navigation hints | Not defined | Optional `navigation` field added |
| Verification | Not defined | NAV-AGENT 5-metric framework referenced |
| Schema | No formal schema | JSON schema documented |

---

## 12. References

- [RFC 8615 — Well-Known URIs](https://www.rfc-editor.org/rfc/rfc8615)
- [NAV-AGENT Verification Framework](../../NAV-AGENT.md)
- [Ground Truth Navigation Map](../plan/ground-truth.md)
- [AgentNav Reference Implementation](https://agentnav.baekenough.com)
