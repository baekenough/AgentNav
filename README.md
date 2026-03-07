# AgentNav

![Specification](https://img.shields.io/badge/spec-agents.txt_v0.2-blue)
![Formats](https://img.shields.io/badge/formats-TXT_%7C_MD_%7C_JSON_%7C_XML-green)
![Grade](https://img.shields.io/badge/NAV--AGENT_grade-A_(95%25%2B)-brightgreen)
![Cross-LLM](https://img.shields.io/badge/cross--LLM_score-97.7%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

**Reference implementation of the agents.txt standard** — a machine-readable documentation sitemap format designed for LLM and AI agent consumption.

Live demo: **https://agentnav.baekenough.com**

---

## Why agents.txt?

When an AI agent needs to find documentation, the naive approach is to fetch pages one by one, burning tokens on irrelevant content. A better approach — used by web crawlers for decades — is to consult a structured index first.

`agents.txt` is that index for AI agents.

| Protocol | Designed For | Optimized For |
|----------|-------------|---------------|
| `robots.txt` | Web crawlers | Crawl exclusion |
| `sitemap.xml` | Search engines | Indexing priority |
| `agents.txt` | AI agents / LLMs | Token-efficient navigation |

With agents.txt, an agent can answer "which page documents prompt caching?" without fetching a single content page. It consults the index (3,200–9,600 tokens depending on format), builds a mental map of the site, and navigates directly to the right URL.

For a 651-page documentation site, this turns an unbounded crawl into a single structured lookup.

---

## What is agents.txt?

agents.txt is a documentation index format with four design goals:

1. **Token efficiency** — convey maximum structural information with minimum tokens
2. **Machine parseability** — structured enough for programmatic extraction
3. **Human readability** — understandable by developers without tooling
4. **Navigation utility** — sufficient to answer "which page for X?" without fetching anything

The format is served at `.well-known/agents.{format}` endpoints following [RFC 8615](https://www.rfc-editor.org/rfc/rfc8615), in four serialization variants:

```
https://{domain}/.well-known/agents.txt    # Plain text (token-efficient)
https://{domain}/.well-known/agents.md     # Markdown (LLM-friendly)
https://{domain}/.well-known/agents.json   # JSON (machine-parseable)
https://{domain}/.well-known/agents.xml    # XML (enterprise toolchains)
```

All four endpoints represent the same documentation index. The format choice is a trade-off between token cost and parseability.

### Format Comparison

| Format | Tokens (651 pages) | Machine Parseability | Human Readability | Recommended For |
|--------|-------------------|---------------------|-------------------|-----------------|
| TXT | ~3,200 | Good | Good | Token-constrained agents |
| MD | ~5,400 | Good | Best | LLM natural language processing |
| JSON | ~9,600 | Best | Moderate | Programmatic API integration |
| XML | ~7,000 | Best | Moderate | Enterprise XML toolchains |

Token counts are approximate (4 chars/token) for the Claude platform documentation (651 pages).

---

## Quick Start

### For AI Agents

Fetch the documentation index in your preferred format:

```bash
# Token-efficient plain text
curl https://agentnav.baekenough.com/claude-code/.well-known/agents.txt

# Structured JSON for programmatic parsing
curl https://agentnav.baekenough.com/claude-code/.well-known/agents.json

# Markdown for LLM natural language consumption
curl https://agentnav.baekenough.com/claude-code/.well-known/agents.md
```

Then implement the NAVIGATOR.md workflow to parse the response and answer navigation queries — without fetching any content pages.

### For Site Owners

Add agents.txt to your documentation site in four steps:

1. Create your documentation index in one or more of the 4 formats
2. Serve it at `/.well-known/agents.{format}` from your domain
3. Annotate each page with one of the 12 content types (see taxonomy below)
4. Use SDK Pattern Compression if your site has multiple SDKs sharing the same endpoint structure

### Self-Hosting

```bash
git clone <repo>
cd AgentNav
docker build -t agentnav .
docker run -p 8080:80 agentnav
# Visit http://localhost:8080
```

The container is a static nginx:alpine server — no backend required.

---

## Specification: agents.txt v0.2

The current specification is at `docs/spec/agents-txt-v0.2.md`. Key concepts:

### Content Type Taxonomy (12 types)

Every page in an agents.txt response must be annotated with a `type` from this controlled vocabulary:

| Type | Description | Example URLs |
|------|-------------|-------------|
| `tutorial` | Getting started guides and quickstarts | `quickstart`, `get-started` |
| `reference` | Static reference information | `glossary`, `pricing`, `deprecations` |
| `guide` | Feature-specific how-to guides | `prompt-caching`, `vision`, `streaming` |
| `overview` | Section entry points and landing pages | `models/overview`, `features/overview` |
| `use-case` | Use-case-specific implementation guides | `content-moderation`, `ticket-routing` |
| `tool-reference` | Documentation for a specific tool | `bash-tool`, `web-search-tool` |
| `sdk-guide` | SDK-specific integration guides | `agent-sdk/python`, `agent-sdk/typescript` |
| `api-reference` | API infrastructure documentation | `rate-limits`, `errors`, `versioning` |
| `api-endpoint` | Documentation for a single API endpoint | `messages/create`, `models/list` |
| `api-hub` | API section hub aggregating endpoints | `messages`, `admin`, `beta` |
| `best-practices` | Best practice and guardrail guidance | `reduce-hallucinations`, `reduce-latency` |
| `changelog` | Change log and release notes | `release-notes/overview` |

Classification rule: choose the most specific type that applies. `api-endpoint` takes precedence over `api-reference`; `tool-reference` takes precedence over `guide`.

### SDK Pattern Compression

For sites with multiple SDKs sharing the same endpoint structure, enumerating all pages individually is token-wasteful. The `sdk_pattern` object expresses repeating structures once:

```json
"sdk_pattern": {
  "sdks": ["python", "typescript", "java", "go", "csharp", "ruby", "php", "kotlin", "terraform", "cli"],
  "pages_per_sdk": 45,
  "url_template": "/docs/en/api/{sdk}/{endpoint}",
  "endpoint_paths": ["overview", "client", "messages", "messages/create", "models", "models/list"]
}
```

For the Claude platform docs (10 SDKs × 45 endpoints = 450 pages), this pattern replaces 450 explicit page entries with a single template block — a token reduction of approximately 90%.

### Minimal Valid JSON Example

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

### Multi-Provider Directory Structure

When a single host serves multiple documentation sets, each is scoped to a subdirectory:

```
https://agentnav.baekenough.com/.well-known/agents.json          # Claude docs (primary)
https://agentnav.baekenough.com/claude-code/.well-known/agents.json
https://agentnav.baekenough.com/gpt-codex/.well-known/agents.json
```

Provider subdirectory naming convention: `{vendor}-{product}` in lowercase kebab-case.

---

## Available Documentation Sets

| Provider | Pages | Sections | Endpoint Prefix |
|----------|-------|----------|-----------------|
| Claude Code (Anthropic) | 651 | 9 | `/claude-code/` |
| GPT Codex (OpenAI) | 69 | 14 | `/gpt-codex/` |

---

## Agent Specifications

AgentNav ships two agent specifications as Claude Code subagent definitions:

### NAVIGATOR.md — Consumer Agent

Any LLM can implement this spec to parse agents.txt and answer navigation queries.

**Workflow:**

1. **Discovery** — Try `.well-known/agents.json`, `.md`, `.xml`, `.txt` in order; accept the first HTTP 200
2. **Parse** — Extract sections, pages, SDK patterns, and navigation hints using format-specific parsing rules
3. **Build Site Map** — Construct an internal representation of the site structure
4. **Answer Queries** — Match user intent against titles, paths, and section names; return full URLs

The spec is format-agnostic (handles all 4 formats) and LLM-agnostic (works with Claude, GPT, Gemini, or any agent with HTTP fetch capability).

### NAV-AGENT.md — Verification Agent

Tests how effectively each format conveys documentation structure, using embedded ground truth.

**5 weighted metrics:**

| Metric | Weight | Question |
|--------|--------|---------|
| Section Discovery | 20% | How many top-level sections can be identified? |
| Page Coverage | 25% | How many representative pages can be located? |
| Navigation Accuracy | 30% | Can intent-based queries reach the correct page? |
| Pattern Recognition | 15% | Are repeating SDK structures recognized? |
| Content Classification | 10% | Are page types correctly annotated? |

**Grading scale:** A (90%+), B (70–89%), C (50–69%), F (<50%)

A compliant agents.txt implementation should score at least Grade B on this rubric.

---

## Test Results

### NAV-AGENT Verification (Claude)

All 4 format variants of the Claude Code documentation were verified using NAV-AGENT:

- All formats: **Grade A (95%+)**
- Content Classification: **100%** after v0.2 taxonomy normalization

### Cross-LLM Verification (GPT via Codex CLI)

The NAVIGATOR.md specification was validated against a different LLM to confirm portability:

- **Total queries:** 100 across 10 categories
- **Overall score:** 97.7/100 (Grade A)
- **Date:** 2026-03-07

| Category | Score |
|----------|-------|
| Structure Discovery | 10/10 (100%) |
| Direct Page Lookup | 10/10 (100%) |
| API Navigation | 10/10 (100%) |
| SDK Endpoint Lookup | 10/10 (100%) |
| Natural Language Navigation | 10/10 (100%) |
| Section Enumeration | 9.7/10 (97%) |
| Page Type Classification | 10/10 (100%) |
| Full URL Construction | 10/10 (100%) |
| Cross-Section Navigation | 9/10 (90%) |
| Edge Cases | 9/10 (90%) |

The 2.3-point gap comes from two edge cases: a cross-section query about model-related pages (I3), and a query for a non-existent Kubernetes deployment page (J3, correctly returned "not found" but scored against expected behavior).

Full results: `tests/navigator-codex-report.md`

---

## Project Structure

```
AgentNav/
├── README.md                    # This file
├── README_ko.md                 # Korean version
├── Dockerfile                   # nginx:alpine container
├── nginx.conf                   # URL rewrite rules for .well-known
├── NAVIGATOR.md                 # Consumer agent spec (parse & navigate)
├── NAV-AGENT.md                 # Verification agent spec (test & grade)
├── public/
│   ├── index.html               # Landing page
│   ├── claude-code/
│   │   ├── index.html           # Format selection page
│   │   ├── agents.json          # JSON format (~9,600 tokens)
│   │   ├── agents.md            # Markdown format (~5,400 tokens)
│   │   ├── agents.xml           # XML format (~7,000 tokens)
│   │   └── agents.txt           # Plain text format (~3,200 tokens)
│   └── gpt-codex/
│       ├── index.html
│       ├── agents.json
│       ├── agents.md
│       ├── agents.xml
│       └── agents.txt
├── docs/
│   └── spec/
│       └── agents-txt-v0.2.md   # Formal specification
└── tests/
    ├── navigator-codex-test.py  # Cross-LLM verification (100 queries)
    └── navigator-codex-report.md # Test results
```

### Architecture

The server is intentionally minimal:

- **Runtime:** nginx:alpine Docker container
- **Content:** Static files only — no backend, no database
- **HTTPS:** Cloudflare Tunnel
- **CORS:** `Access-Control-Allow-Origin: *` (public read access)
- **Compression:** gzip for all supported MIME types
- **Routing:** `.well-known/agents.*` rewrites to provider-scoped paths; `/?docs=provider` query parameter redirect for convenience

```
nginx.conf key behavior:
  /.well-known/agents.json  →  301  /claude-code/agents.json   (backward compat)
  /claude-code/agents.json  →  served directly from /usr/share/nginx/html/
```

---

## Adding Your Documentation

To add a new documentation set to AgentNav:

1. Create a provider directory under `public/` using the `{vendor}-{product}` naming convention:
   ```
   public/your-docs/
   ```

2. Create the four format files following the v0.2 specification:
   ```
   public/your-docs/agents.json
   public/your-docs/agents.md
   public/your-docs/agents.xml
   public/your-docs/agents.txt
   ```

3. Create a format selection page at `public/your-docs/index.html`

4. Add your provider card to `public/index.html`

5. Run NAV-AGENT verification against your files and confirm Grade B or higher before submitting

6. Rebuild and deploy the container

---

## Contributing

Before submitting a pull request:

- Follow the v0.2 specification at `docs/spec/agents-txt-v0.2.md`
- Use NAV-AGENT.md to verify your agents.txt achieves Grade B (70%+) or higher
- Test with NAVIGATOR.md to confirm the format is parseable by a generic LLM agent
- Use the 12-type content taxonomy for page classification — do not introduce new types without a spec change

---

## License

MIT

---

## Links

| Resource | Location |
|----------|----------|
| Live implementation | https://agentnav.baekenough.com |
| Specification | `docs/spec/agents-txt-v0.2.md` |
| Consumer agent spec | `NAVIGATOR.md` |
| Verification agent spec | `NAV-AGENT.md` |
| Test results | `tests/navigator-codex-report.md` |
