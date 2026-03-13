# agents.txt

![Specification](https://img.shields.io/badge/spec-v0.2-blue)
![Formats](https://img.shields.io/badge/formats-TXT_%7C_MD_%7C_JSON_%7C_XML-green)
![NAV-AGENT Grade](https://img.shields.io/badge/NAV--AGENT-Grade_A_(100%25)-brightgreen)
![Cross-LLM](https://img.shields.io/badge/cross--LLM-97.7%2F100-brightgreen)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

**A proposed web standard that lets documentation sites serve a machine-readable index for AI agents** — like `robots.txt` for crawlers and `sitemap.xml` for search engines, but designed for LLMs.

Reference implementation: **https://agentnav.baekenough.com**

---

## The Problem

Vercel discovered something alarming when they studied AI agents using Playwright MCP to browse the web: a single button click returns **12,891 characters** of accessibility tree data. Their solution ([agent-browser](https://www.productengineer.info/community/articles/10d24bff-1a0d-43d3-bf99-c4c4f3f72bd2)) reduced token usage by **93%** by creating a purpose-built AI interface instead of forcing AI through a human-designed one.

The same problem exists for documentation sites — and it is worse.

When an AI agent needs to find documentation, it navigates the way a human would: fetching pages, reading navigation menus, following links. But documentation sites are designed for humans, not AI agents. Every HTML page a bot fetches is padded with navigation chrome, sidebars, headers, and footers — most of which is irrelevant noise. For a 651-page documentation site, a naive crawl could consume **millions of tokens**. Even finding the right page to fetch requires multiple round-trips.

The existing web standards do not solve this:

| Standard | Designed For | What It Gives AI Agents |
|----------|-------------|------------------------|
| `robots.txt` | Web crawlers | Crawl exclusion rules — not navigation help |
| `sitemap.xml` | Search engines | A flat URL list — no semantic structure |
| `llms.txt` | LLMs reading site summaries | Free-text description — not navigable |
| `agents.txt` | **AI agents navigating docs** | Structured index with types, sections, SDK patterns |

---

## The Solution

`agents.txt` is a proposed web standard that lets any documentation site publish a structured, machine-readable index of its content — served at a well-known URL, in the format AI agents actually need.

```
https://your-docs.com/.well-known/agents.txt
```

An AI agent fetches this single file (~3,200 tokens for a 651-page site) and can immediately answer:

- "Which page documents prompt caching?" — without fetching a single content page
- "Where is the Python SDK quickstart?" — from the index, not a crawl
- "What API endpoints exist for batch processing?" — from the type annotations

The same idea that reduced Vercel's token usage by 93% — **build the interface for AI, not for humans** — applied at the web standard level.

---

## How It Works

```
Site Owner                         AI Agent
──────────                         ────────
Create agents.txt                  GET /.well-known/agents.txt
Serve at /.well-known/agents.*     Parse sections, pages, SDK patterns
Annotate pages with 12 types       Answer navigation queries directly
Use SDK Pattern Compression        Fetch only the relevant page
```

A site that serves `agents.txt` gives every AI agent a navigation map on first contact — no crawling required.

### The Analogy

| Protocol | Who Reads It | What It Enables |
|----------|-------------|-----------------|
| `robots.txt` | Search engine crawlers | Know which pages to skip |
| `sitemap.xml` | Search engine indexers | Know which pages to prioritize |
| `agents.txt` | AI agents | Navigate to the right page without crawling |

### Format Options

agents.txt is available in four serialization variants. Sites should serve all four:

```
https://your-docs.com/.well-known/agents.txt    # Plain text  (~3,200 tokens for 651 pages)
https://your-docs.com/.well-known/agents.md     # Markdown    (~5,400 tokens)
https://your-docs.com/.well-known/agents.json   # JSON        (~9,600 tokens)
https://your-docs.com/.well-known/agents.xml    # XML         (~7,000 tokens)
```

| Format | Token Cost | Best For |
|--------|-----------|---------|
| TXT | Lowest | Token-constrained agents, quick lookups |
| MD | Low | LLMs processing the index as natural language |
| JSON | Higher | Programmatic parsing, building navigation indexes |
| XML | Moderate | Enterprise toolchains, existing XML pipelines |

---

## For Site Owners: Adding agents.txt to Your Site

This is the primary goal of this project. If you maintain a documentation site, here is how to add `agents.txt` support in four steps.

### Step 1: Create your documentation index

Choose the JSON format as your canonical source. At minimum, you need:

```json
{
  "agents_txt_version": "0.2",
  "site": {
    "name": "Your Docs",
    "url": "https://docs.yoursite.com",
    "total_pages": 42,
    "last_updated": "2026-03-07"
  },
  "sections": [
    {
      "name": "Getting Started",
      "path_prefix": "/docs/getting-started",
      "page_count": 2,
      "pages": [
        { "path": "/docs/getting-started/quickstart", "title": "Quickstart", "type": "tutorial" },
        { "path": "/docs/getting-started/overview",   "title": "Overview",   "type": "overview" }
      ]
    },
    {
      "name": "API Reference",
      "path_prefix": "/docs/api",
      "page_count": 3,
      "pages": [
        { "path": "/docs/api/messages",        "title": "Messages",       "type": "api-hub"       },
        { "path": "/docs/api/messages/create", "title": "Create Message", "type": "api-endpoint", "method": "POST" },
        { "path": "/docs/api/rate-limits",     "title": "Rate Limits",    "type": "api-reference" }
      ]
    }
  ]
}
```

### Step 2: Annotate each page with a content type

Every page must carry a `type` from the 12-type taxonomy (see Specification section below). The type tells AI agents what kind of content to expect — a tutorial reads differently from an API endpoint reference.

### Step 3: Serve at the well-known URL

Add routing rules to serve your index at `/.well-known/agents.*`:

```nginx
# nginx example
location /.well-known/agents.json { alias /path/to/agents.json; }
location /.well-known/agents.md   { alias /path/to/agents.md;   }
location /.well-known/agents.txt  { alias /path/to/agents.txt;  }
location /.well-known/agents.xml  { alias /path/to/agents.xml;  }
```

Set `Content-Type` headers appropriately and add `Access-Control-Allow-Origin: *` for cross-origin agent access.

### Step 4: Verify your implementation

Use the NAV-AGENT verification agent in this repository to test that your agents.txt achieves Grade B (70%+) or higher before publishing.

### If You Have Multiple SDKs: Use Pattern Compression

If your documentation has multiple SDKs with identical endpoint structures (Python, TypeScript, Java, etc.), do not enumerate every page. Use the `sdk_pattern` field instead:

```json
"sdk_pattern": {
  "sdks": ["python", "typescript", "java", "go"],
  "pages_per_sdk": 30,
  "url_template": "/docs/api/{sdk}/{endpoint}",
  "endpoint_paths": ["overview", "client", "messages", "messages/create", "models", "models/list"]
}
```

For 4 SDKs × 30 pages = 120 pages, this single block replaces 120 explicit entries — roughly **90% token reduction** for the SDK section.

---

## Specification: agents.txt v0.2

Full specification: [`docs/spec/agents-txt-v0.2.md`](docs/spec/agents-txt-v0.2.md)

### Well-Known URL Convention (RFC 8615)

agents.txt follows [RFC 8615](https://www.rfc-editor.org/rfc/rfc8615), which defines the `.well-known` directory as the standard location for site-wide machine-readable metadata. This is the same convention used by `robots.txt` alternatives and security policy files.

### Content Type Taxonomy (12 types)

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

Classification rule: choose the most specific type. `api-endpoint` takes precedence over `api-reference`; `tool-reference` takes precedence over `guide`.

### SDK Pattern Compression

Repeating SDK structures are expressed once using a template, not enumerated per-page. For the Claude platform documentation (10 SDKs × 45 endpoints = 450 pages), the `sdk_pattern` block replaces 450 explicit page entries with a single template — approximately **90% token reduction** for the SDK section.

### Changes from v0.1

| Area | v0.1 | v0.2 |
|------|------|------|
| Content types | Informal, ad hoc | 12-type controlled vocabulary |
| URL convention | None | Well-known URL (RFC 8615) |
| Multi-provider | Not addressed | Provider subdirectory structure |
| SDK compression | Not defined | `sdk_pattern` schema |
| Navigation hints | Not defined | Optional `navigation` field |
| Verification | Not defined | NAV-AGENT 5-metric framework |

---

## Reference Implementation

AgentNav at [agentnav.baekenough.com](https://agentnav.baekenough.com) demonstrates the standard with two real documentation sites:

| Documentation Site | Pages | Sections | Prefix |
|-------------------|-------|----------|--------|
| Claude Code (Anthropic) | 651 | 9 | `/claude-code/` |
| GPT Codex (OpenAI) | 68 | 14 | `/gpt-codex/` |

Each site's agents.txt is available in all four formats at the well-known paths:

```bash
# Claude Code documentation index — plain text (lowest token cost)
curl https://agentnav.baekenough.com/.well-known/agents.txt

# JSON for programmatic parsing
curl https://agentnav.baekenough.com/.well-known/agents.json

# Provider-scoped access
curl https://agentnav.baekenough.com/claude-code/.well-known/agents.md
curl https://agentnav.baekenough.com/gpt-codex/.well-known/agents.json
```

### Self-Hosting

```bash
git clone <repo>
cd AgentNav
docker build -t agentnav .
docker run -p 8080:80 agentnav
```

The container is a static nginx:alpine server with no backend or database. The only runtime dependency is nginx.

---

## Agent Specifications

### NAVIGATOR.md — Consumer Agent

Any LLM can implement this spec to parse agents.txt and answer navigation queries without fetching content pages.

Workflow:
1. **Discover** — Try `.well-known/agents.json`, `.md`, `.xml`, `.txt` in order; accept the first HTTP 200
2. **Parse** — Extract sections, pages, SDK patterns, and navigation hints
3. **Build map** — Construct an internal representation of the site structure
4. **Answer queries** — Match intent against titles, paths, types; return the full URL

The spec is LLM-agnostic: it works with Claude, GPT, Gemini, or any agent with HTTP fetch capability.

### NAV-AGENT.md — Verification Agent

Tests how effectively each format conveys documentation structure. Uses embedded ground truth for the Claude platform docs (651 pages) as the scoring baseline.

**5 weighted metrics:**

| Metric | Weight | Question |
|--------|--------|---------|
| Section Discovery | 20% | How many top-level sections can be identified? |
| Page Coverage | 25% | How many representative pages can be located? |
| Navigation Accuracy | 30% | Can intent-based queries reach the correct page? |
| Pattern Recognition | 15% | Are repeating SDK structures recognized and usable? |
| Content Classification | 10% | Are page types correctly annotated? |

Grading: A (90%+), B (70-89%), C (50-69%), F (<50%). A compliant implementation should score Grade B or higher.

---

## Verification Results

### NAV-AGENT (Claude)

All four format variants of the Claude Code documentation index were tested:

- All formats: **Grade A (100%)**
- Content Classification: **100%** after v0.2 taxonomy normalization

### Cross-LLM Validation (GPT via Codex CLI)

NAVIGATOR.md was validated against a different LLM to confirm the specification is portable across models.

- **Total queries**: 100 across 10 categories
- **Overall score**: 97.7/100 (Grade A)
- **Date**: 2026-03-07

| Category | Score |
|----------|-------|
| Structure Discovery | 10/10 |
| Direct Page Lookup | 10/10 |
| API Navigation | 10/10 |
| SDK Endpoint Lookup | 10/10 |
| Natural Language Navigation | 10/10 |
| Section Enumeration | 9.7/10 |
| Page Type Classification | 10/10 |
| Full URL Construction | 10/10 |
| Cross-Section Navigation | 9/10 |
| Edge Cases | 9/10 |

Full results: [`tests/navigator-codex-report.md`](tests/navigator-codex-report.md)

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
├── .github/
│   └── workflows/               # CI/CD pipelines
├── dags/
│   └── agentnav_docs_drift.py   # Airflow DAG for drift detection
├── docs/
│   ├── spec/
│   │   └── agents-txt-v0.2.md  # Formal specification
│   └── plan/                   # Design notes and analysis
├── public/
│   ├── index.html               # Landing page
│   ├── claude-code/
│   │   ├── agents.json          # JSON format (~9,600 tokens)
│   │   ├── agents.md            # Markdown format (~5,400 tokens)
│   │   ├── agents.xml           # XML format (~7,000 tokens)
│   │   └── agents.txt           # Plain text format (~3,200 tokens)
│   └── gpt-codex/
│       ├── agents.json
│       ├── agents.md
│       ├── agents.xml
│       └── agents.txt
├── scripts/
│   └── generate_formats.py      # Generate MD/XML/TXT from JSON
└── tests/
    ├── navigator-codex-test.py  # Cross-LLM verification (100 queries)
    └── navigator-codex-report.md
```

### Architecture

The reference implementation is intentionally minimal:

- **Runtime**: nginx:alpine Docker container
- **Content**: Static files only — no backend, no database
- **HTTPS**: Cloudflare Tunnel
- **CORS**: `Access-Control-Allow-Origin: *` for public read access
- **Routing**: `.well-known/agents.*` rewrites to provider-scoped paths

---

## Contributing

### Adding a New Documentation Set

1. Create a provider directory under `public/` using `{vendor}-{product}` naming:
   ```
   public/your-product/
   ```

2. Create the four format files following the v0.2 specification

3. Run NAV-AGENT verification and confirm Grade B (70%+) or higher

4. Add your provider card to `public/index.html`

### Spec Changes

Before proposing changes to the specification:

- Use NAV-AGENT to verify any format changes maintain Grade B or higher
- Test with NAVIGATOR.md to confirm a generic LLM agent can parse the result
- Do not introduce new content types without updating the 12-type taxonomy in `docs/spec/agents-txt-v0.2.md`

---

## License

MIT

---

## Links

| Resource | Location |
|----------|----------|
| Live reference implementation | https://agentnav.baekenough.com |
| Formal specification | [`docs/spec/agents-txt-v0.2.md`](docs/spec/agents-txt-v0.2.md) |
| Consumer agent spec | [`NAVIGATOR.md`](NAVIGATOR.md) |
| Verification agent spec | [`NAV-AGENT.md`](NAV-AGENT.md) |
| Test results | [`tests/navigator-codex-report.md`](tests/navigator-codex-report.md) |
| Inspiration | [Vercel agent-browser article](https://www.productengineer.info/community/articles/10d24bff-1a0d-43d3-bf99-c4c4f3f72bd2) |
