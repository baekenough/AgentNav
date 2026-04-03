---
agents_txt_version: "0.2"
format: markdown
schema:
  sections: "## heading = section name"
  subsections: "### heading = subsection grouping"
  pages: "- [title](path) {type}"
  page_types: [overview, tutorial, guide, reference, tool-reference, api-endpoint, best-practices]
---

# Supabase Documentation

- **URL**: https://supabase.com
- **Standard**: agents.txt v0.2 (AgentNav PoC)
- **Total Pages**: 691
- **Last Updated**: 2026-04-03

## Site Overview

| # | Section | Pages | Base Path |
|---|---------|-------|-----------|
| 1 | AI | 35 | /docs/guides/ai/ |
| 2 | API | 16 | /docs/guides/api/ |
| 3 | Auth | 80 | /docs/guides/auth/ |
| 4 | CLI | 1 | /docs/guides/ |
| 5 | Cron | 3 | /docs/guides/cron/ |
| 6 | Database | 83 | /docs/guides/database/ |
| 7 | Deployment | 13 | /docs/guides/deployment/ |
| 8 | Functions | 55 | /docs/guides/functions/ |
| 9 | Getting Started | 41 | /docs/guides/getting-started/ |
| 10 | Integrations | 6 | /docs/guides/integrations/ |
| 11 | Local Development | 11 | /docs/guides/local-development/ |
| 12 | Platform | 75 | /docs/guides/platform/ |
| 13 | Queues | 6 | /docs/guides/queues/ |
| 14 | Realtime | 19 | /docs/guides/realtime/ |
| 15 | Resources | 2 | /docs/guides/resources/ |
| 16 | Security | 7 | /docs/guides/security/ |
| 17 | Self Hosting | 13 | /docs/guides/self-hosting/ |
| 18 | Storage | 42 | /docs/guides/storage/ |
| 19 | Telemetry | 10 | /docs/guides/telemetry/ |
| 20 | Troubleshooting | 173 | /docs/guides/troubleshooting/ |

---

## AI (35 pages)

- [AI](/docs/guides/ai) {guide}
- [Automatic Embeddings](/docs/guides/ai/automatic-embeddings) {guide}
- [Choosing Compute Addon](/docs/guides/ai/choosing-compute-addon) {guide}
- [Concepts](/docs/guides/ai/concepts) {guide}
- [Engineering for Scale](/docs/guides/ai/engineering-for-scale) {guide}
- [Building Chatgpt Plugins](/docs/guides/ai/examples/building-chatgpt-plugins) {tutorial}
- [Headless Vector Search](/docs/guides/ai/examples/headless-vector-search) {tutorial}
- [Huggingface Image Captioning](/docs/guides/ai/examples/huggingface-image-captioning) {tutorial}
- [Image Search Openai Clip](/docs/guides/ai/examples/image-search-openai-clip) {tutorial}
- [Mixpeek Video Search](/docs/guides/ai/examples/mixpeek-video-search) {tutorial}
- [Nextjs Vector Search](/docs/guides/ai/examples/nextjs-vector-search) {tutorial}
- [Openai](/docs/guides/ai/examples/openai) {tutorial}
- [Semantic Image Search Amazon Titan](/docs/guides/ai/examples/semantic-image-search-amazon-titan) {tutorial}
- [Going to Prod](/docs/guides/ai/going-to-prod) {guide}
- [Google Colab](/docs/guides/ai/google-colab) {guide}
- [Hugging Face](/docs/guides/ai/hugging-face) {guide}
- [Hybrid Search](/docs/guides/ai/hybrid-search) {guide}
- [Amazon Bedrock](/docs/guides/ai/integrations/amazon-bedrock) {guide}
- [Llamaindex](/docs/guides/ai/integrations/llamaindex) {guide}
- [Roboflow](/docs/guides/ai/integrations/roboflow) {guide}
- [Keyword Search](/docs/guides/ai/keyword-search) {guide}
- [Langchain](/docs/guides/ai/langchain) {guide}
- [Python Clients](/docs/guides/ai/python-clients) {tool-reference}
- [Face Similarity](/docs/guides/ai/quickstarts/face-similarity) {tutorial}
- [Generate Text Embeddings](/docs/guides/ai/quickstarts/generate-text-embeddings) {tutorial}
- [Hello World](/docs/guides/ai/quickstarts/hello-world) {tutorial}
- [Text Deduplication](/docs/guides/ai/quickstarts/text-deduplication) {tutorial}
- [Rag with Permissions](/docs/guides/ai/rag-with-permissions) {guide}
- [Semantic Search](/docs/guides/ai/semantic-search) {guide}
- [Structured Unstructured](/docs/guides/ai/structured-unstructured) {guide}
- [Vecs Python Client](/docs/guides/ai/vecs-python-client) {tool-reference}
- [Vector Columns](/docs/guides/ai/vector-columns) {guide}
- [Vector Indexes](/docs/guides/ai/vector-indexes) {guide}
- [Hnsw Indexes](/docs/guides/ai/vector-indexes/hnsw-indexes) {guide}
- [Ivf Indexes](/docs/guides/ai/vector-indexes/ivf-indexes) {guide}

## API (16 pages)

- [API](/docs/guides/api) {guide}
- [API Keys](/docs/guides/api/api-keys) {api-endpoint}
- [Automatic Retries in Supabase Js](/docs/guides/api/automatic-retries-in-supabase-js) {api-endpoint}
- [Creating Routes](/docs/guides/api/creating-routes) {api-endpoint}
- [Custom Claims and Role Based Access Control RBAC](/docs/guides/api/custom-claims-and-role-based-access-control-rbac) {api-endpoint}
- [Hardening Data API](/docs/guides/api/hardening-data-api) {api-endpoint}
- [Quickstart](/docs/guides/api/quickstart) {tutorial}
- [Auto Generated Docs](/docs/guides/api/rest/auto-generated-docs) {api-endpoint}
- [Client Libs](/docs/guides/api/rest/client-libs) {tool-reference}
- [Generating Python Types](/docs/guides/api/rest/generating-python-types) {api-endpoint}
- [Generating Types](/docs/guides/api/rest/generating-types) {api-endpoint}
- [Postgrest Error Codes](/docs/guides/api/rest/postgrest-error-codes) {api-endpoint}
- [Securing Your API](/docs/guides/api/securing-your-api) {api-endpoint}
- [SQL to API](/docs/guides/api/sql-to-api) {api-endpoint}
- [SQL to Rest](/docs/guides/api/sql-to-rest) {api-endpoint}
- [Using Custom Schemas](/docs/guides/api/using-custom-schemas) {api-endpoint}

## Auth (80 pages)

- [Auth](/docs/guides/auth) {guide}
- [Architecture](/docs/guides/auth/architecture) {guide}
- [Audit Logs](/docs/guides/auth/audit-logs) {guide}
- [Auth Anonymous](/docs/guides/auth/auth-anonymous) {guide}
- [Auth Captcha](/docs/guides/auth/auth-captcha) {guide}
- [Auth Email Passwordless](/docs/guides/auth/auth-email-passwordless) {guide}
- [Auth Email Templates](/docs/guides/auth/auth-email-templates) {guide}
- [Auth Hooks](/docs/guides/auth/auth-hooks) {guide}
- [Before User Created Hook](/docs/guides/auth/auth-hooks/before-user-created-hook) {guide}
- [Custom Access Token Hook](/docs/guides/auth/auth-hooks/custom-access-token-hook) {guide}
- [Mfa Verification Hook](/docs/guides/auth/auth-hooks/mfa-verification-hook) {guide}
- [Password Verification Hook](/docs/guides/auth/auth-hooks/password-verification-hook) {guide}
- [Send Email Hook](/docs/guides/auth/auth-hooks/send-email-hook) {guide}
- [Send Sms Hook](/docs/guides/auth/auth-hooks/send-sms-hook) {guide}
- [Auth Identity Linking](/docs/guides/auth/auth-identity-linking) {guide}
- [Auth Mfa](/docs/guides/auth/auth-mfa) {guide}
- [Phone](/docs/guides/auth/auth-mfa/phone) {guide}
- [Totp](/docs/guides/auth/auth-mfa/totp) {guide}
- [Auth Smtp](/docs/guides/auth/auth-smtp) {guide}
- [Auth Web3](/docs/guides/auth/auth-web3) {guide}
- [Custom OAUTH Providers](/docs/guides/auth/custom-oauth-providers) {guide}
- [Error Codes](/docs/guides/auth/debugging/error-codes) {guide}
- [Enterprise SSO](/docs/guides/auth/enterprise-sso) {guide}
- [Auth SSO SAML](/docs/guides/auth/enterprise-sso/auth-sso-saml) {guide}
- [General Configuration](/docs/guides/auth/general-configuration) {reference}
- [Identities](/docs/guides/auth/identities) {guide}
- [JWT Fields](/docs/guides/auth/jwt-fields) {guide}
- [Jwts](/docs/guides/auth/jwts) {guide}
- [Managing User Data](/docs/guides/auth/managing-user-data) {guide}
- [Native Mobile Deep Linking](/docs/guides/auth/native-mobile-deep-linking) {guide}
- [OAUTH Server](/docs/guides/auth/oauth-server) {guide}
- [Getting Started](/docs/guides/auth/oauth-server/getting-started) {tutorial}
- [MCP Authentication](/docs/guides/auth/oauth-server/mcp-authentication) {guide}
- [OAUTH Flows](/docs/guides/auth/oauth-server/oauth-flows) {guide}
- [Token Security](/docs/guides/auth/oauth-server/token-security) {guide}
- [Password Security](/docs/guides/auth/password-security) {guide}
- [Passwords](/docs/guides/auth/passwords) {guide}
- [Phone Login](/docs/guides/auth/phone-login) {guide}
- [Nextjs](/docs/guides/auth/quickstarts/nextjs) {tutorial}
- [React](/docs/guides/auth/quickstarts/react) {tutorial}
- [React Native](/docs/guides/auth/quickstarts/react-native) {tutorial}
- [With Expo React Native Social Auth](/docs/guides/auth/quickstarts/with-expo-react-native-social-auth) {tutorial}
- [Rate Limits](/docs/guides/auth/rate-limits) {guide}
- [Redirect Urls](/docs/guides/auth/redirect-urls) {guide}
- [Server Side](/docs/guides/auth/server-side) {guide}
- [Advanced Guide](/docs/guides/auth/server-side/advanced-guide) {guide}
- [Creating a Client](/docs/guides/auth/server-side/creating-a-client) {tool-reference}
- [Migrating to Ssr from Auth Helpers](/docs/guides/auth/server-side/migrating-to-ssr-from-auth-helpers) {guide}
- [Sessions](/docs/guides/auth/sessions) {guide}
- [Implicit Flow](/docs/guides/auth/sessions/implicit-flow) {guide}
- [Pkce Flow](/docs/guides/auth/sessions/pkce-flow) {guide}
- [Signing Keys](/docs/guides/auth/signing-keys) {guide}
- [Signout](/docs/guides/auth/signout) {guide}
- [Social Login](/docs/guides/auth/social-login) {guide}
- [Auth Apple](/docs/guides/auth/social-login/auth-apple) {guide}
- [Auth Azure](/docs/guides/auth/social-login/auth-azure) {guide}
- [Auth Bitbucket](/docs/guides/auth/social-login/auth-bitbucket) {guide}
- [Auth Discord](/docs/guides/auth/social-login/auth-discord) {guide}
- [Auth Facebook](/docs/guides/auth/social-login/auth-facebook) {guide}
- [Auth Figma](/docs/guides/auth/social-login/auth-figma) {guide}
- [Auth Github](/docs/guides/auth/social-login/auth-github) {guide}
- [Auth Gitlab](/docs/guides/auth/social-login/auth-gitlab) {guide}
- [Auth Google](/docs/guides/auth/social-login/auth-google) {guide}
- [Auth Kakao](/docs/guides/auth/social-login/auth-kakao) {guide}
- [Auth Keycloak](/docs/guides/auth/social-login/auth-keycloak) {guide}
- [Auth Linkedin](/docs/guides/auth/social-login/auth-linkedin) {guide}
- [Auth Notion](/docs/guides/auth/social-login/auth-notion) {guide}
- [Auth Slack](/docs/guides/auth/social-login/auth-slack) {guide}
- [Auth Spotify](/docs/guides/auth/social-login/auth-spotify) {guide}
- [Auth Twitch](/docs/guides/auth/social-login/auth-twitch) {guide}
- [Auth Twitter](/docs/guides/auth/social-login/auth-twitter) {guide}
- [Auth Workos](/docs/guides/auth/social-login/auth-workos) {guide}
- [Auth Zoom](/docs/guides/auth/social-login/auth-zoom) {guide}
- [Auth0](/docs/guides/auth/third-party/auth0) {guide}
- [AWS Cognito](/docs/guides/auth/third-party/aws-cognito) {guide}
- [Clerk](/docs/guides/auth/third-party/clerk) {guide}
- [Firebase Auth](/docs/guides/auth/third-party/firebase-auth) {guide}
- [Overview](/docs/guides/auth/third-party/overview) {overview}
- [Workos](/docs/guides/auth/third-party/workos) {guide}
- [Users](/docs/guides/auth/users) {guide}

## CLI (1 page)

- [CLI](/docs/guides/cli) {tool-reference}

## Cron (3 pages)

- [Cron](/docs/guides/cron) {guide}
- [Install](/docs/guides/cron/install) {guide}
- [Quickstart](/docs/guides/cron/quickstart) {tutorial}

## Database (83 pages)

- [Arrays](/docs/guides/database/arrays) {guide}
- [Beekeeper Studio](/docs/guides/database/beekeeper-studio) {guide}
- [Connecting to Postgres](/docs/guides/database/connecting-to-postgres) {guide}
- [Serverless Drivers](/docs/guides/database/connecting-to-postgres/serverless-drivers) {guide}
- [Connection Management](/docs/guides/database/connection-management) {guide}
- [Custom Postgres Config](/docs/guides/database/custom-postgres-config) {reference}
- [Dbeaver](/docs/guides/database/dbeaver) {guide}
- [Debugging Performance](/docs/guides/database/debugging-performance) {guide}
- [Drizzle](/docs/guides/database/drizzle) {guide}
- [Extensions](/docs/guides/database/extensions) {guide}
- [HTTP](/docs/guides/database/extensions/http) {guide}
- [Hypopg](/docs/guides/database/extensions/hypopg) {guide}
- [Index Advisor](/docs/guides/database/extensions/index_advisor) {guide}
- [Pg Cron](/docs/guides/database/extensions/pg_cron) {guide}
- [Pg Graphql](/docs/guides/database/extensions/pg_graphql) {guide}
- [Pg Hashids](/docs/guides/database/extensions/pg_hashids) {guide}
- [Pg Jsonschema](/docs/guides/database/extensions/pg_jsonschema) {guide}
- [Pg Net](/docs/guides/database/extensions/pg_net) {guide}
- [Pg Partman](/docs/guides/database/extensions/pg_partman) {guide}
- [Pg Plan Filter](/docs/guides/database/extensions/pg_plan_filter) {guide}
- [Pg Repack](/docs/guides/database/extensions/pg_repack) {guide}
- [Pg Stat Statements](/docs/guides/database/extensions/pg_stat_statements) {guide}
- [Pgaudit](/docs/guides/database/extensions/pgaudit) {guide}
- [Pgjwt](/docs/guides/database/extensions/pgjwt) {guide}
- [Pgmq](/docs/guides/database/extensions/pgmq) {guide}
- [Pgroonga](/docs/guides/database/extensions/pgroonga) {guide}
- [Pgrouting](/docs/guides/database/extensions/pgrouting) {guide}
- [Pgsodium](/docs/guides/database/extensions/pgsodium) {guide}
- [Pgtap](/docs/guides/database/extensions/pgtap) {guide}
- [Pgvector](/docs/guides/database/extensions/pgvector) {guide}
- [Plpgsql Check](/docs/guides/database/extensions/plpgsql_check) {guide}
- [Plv8](/docs/guides/database/extensions/plv8) {guide}
- [Postgis](/docs/guides/database/extensions/postgis) {guide}
- [Postgres Fdw](/docs/guides/database/extensions/postgres_fdw) {guide}
- [Rum](/docs/guides/database/extensions/rum) {guide}
- [Timescaledb](/docs/guides/database/extensions/timescaledb) {guide}
- [Uuid Ossp](/docs/guides/database/extensions/uuid-ossp) {guide}
- [Overview](/docs/guides/database/extensions/wrappers/overview) {overview}
- [Full Text Search](/docs/guides/database/full-text-search) {guide}
- [Functions](/docs/guides/database/functions) {guide}
- [Import Data](/docs/guides/database/import-data) {guide}
- [Inspect](/docs/guides/database/inspect) {guide}
- [Joins and Nesting](/docs/guides/database/joins-and-nesting) {guide}
- [Json](/docs/guides/database/json) {guide}
- [Metabase](/docs/guides/database/metabase) {guide}
- [Migrating to Pg Partman](/docs/guides/database/migrating-to-pg-partman) {guide}
- [Orioledb](/docs/guides/database/orioledb) {guide}
- [Overview](/docs/guides/database/overview) {overview}
- [Partitions](/docs/guides/database/partitions) {guide}
- [Pgadmin](/docs/guides/database/pgadmin) {guide}
- [Postgres Js](/docs/guides/database/postgres-js) {guide}
- [Cascade Deletes](/docs/guides/database/postgres/cascade-deletes) {guide}
- [Column Level Security](/docs/guides/database/postgres/column-level-security) {guide}
- [Configuration](/docs/guides/database/postgres/configuration) {reference}
- [Dropping All Tables in Schema](/docs/guides/database/postgres/dropping-all-tables-in-schema) {guide}
- [Enums](/docs/guides/database/postgres/enums) {guide}
- [Event Triggers](/docs/guides/database/postgres/event-triggers) {guide}
- [First Row in Group](/docs/guides/database/postgres/first-row-in-group) {guide}
- [Indexes](/docs/guides/database/postgres/indexes) {guide}
- [Roles](/docs/guides/database/postgres/roles) {guide}
- [Roles Superuser](/docs/guides/database/postgres/roles-superuser) {guide}
- [Row Level Security](/docs/guides/database/postgres/row-level-security) {guide}
- [Setup Replication External](/docs/guides/database/postgres/setup-replication-external) {guide}
- [Timeouts](/docs/guides/database/postgres/timeouts) {guide}
- [Triggers](/docs/guides/database/postgres/triggers) {guide}
- [Which Version of Postgres](/docs/guides/database/postgres/which-version-of-postgres) {guide}
- [Prisma](/docs/guides/database/prisma) {guide}
- [Prisma Troubleshooting](/docs/guides/database/prisma/prisma-troubleshooting) {guide}
- [Psql](/docs/guides/database/psql) {guide}
- [Query Optimization](/docs/guides/database/query-optimization) {guide}
- [Replication](/docs/guides/database/replication) {guide}
- [Manual Replication Faq](/docs/guides/database/replication/manual-replication-faq) {guide}
- [Manual Replication Monitoring](/docs/guides/database/replication/manual-replication-monitoring) {guide}
- [Manual Replication Setup](/docs/guides/database/replication/manual-replication-setup) {guide}
- [Replication Faq](/docs/guides/database/replication/replication-faq) {guide}
- [Replication Monitoring](/docs/guides/database/replication/replication-monitoring) {guide}
- [Replication Setup](/docs/guides/database/replication/replication-setup) {guide}
- [Secure Data](/docs/guides/database/secure-data) {guide}
- [Supavisor](/docs/guides/database/supavisor) {guide}
- [Tables](/docs/guides/database/tables) {guide}
- [Testing](/docs/guides/database/testing) {guide}
- [Vault](/docs/guides/database/vault) {guide}
- [Webhooks](/docs/guides/database/webhooks) {guide}

## Deployment (13 pages)

- [Deployment](/docs/guides/deployment) {guide}
- [Branching](/docs/guides/deployment/branching) {guide}
- [Configuration](/docs/guides/deployment/branching/configuration) {reference}
- [Dashboard](/docs/guides/deployment/branching/dashboard) {guide}
- [Github Integration](/docs/guides/deployment/branching/github-integration) {guide}
- [Integrations](/docs/guides/deployment/branching/integrations) {guide}
- [Troubleshooting](/docs/guides/deployment/branching/troubleshooting) {guide}
- [Working with Branches](/docs/guides/deployment/branching/working-with-branches) {guide}
- [Database Migrations](/docs/guides/deployment/database-migrations) {guide}
- [Going into Prod](/docs/guides/deployment/going-into-prod) {guide}
- [Managing Environments](/docs/guides/deployment/managing-environments) {guide}
- [Maturity Model](/docs/guides/deployment/maturity-model) {guide}
- [Shared Responsibility Model](/docs/guides/deployment/shared-responsibility-model) {guide}

## Functions (55 pages)

- [Functions](/docs/guides/functions) {guide}
- [AI Models](/docs/guides/functions/ai-models) {guide}
- [Architecture](/docs/guides/functions/architecture) {guide}
- [Auth](/docs/guides/functions/auth) {guide}
- [Auth Legacy JWT](/docs/guides/functions/auth-legacy-jwt) {guide}
- [Background Tasks](/docs/guides/functions/background-tasks) {guide}
- [Compression](/docs/guides/functions/compression) {guide}
- [Connect to Postgres](/docs/guides/functions/connect-to-postgres) {guide}
- [CORS](/docs/guides/functions/cors) {guide}
- [Dart Edge](/docs/guides/functions/dart-edge) {guide}
- [Debugging Tools](/docs/guides/functions/debugging-tools) {guide}
- [Dependencies](/docs/guides/functions/dependencies) {guide}
- [Deploy](/docs/guides/functions/deploy) {guide}
- [Development Environment](/docs/guides/functions/development-environment) {guide}
- [Development Tips](/docs/guides/functions/development-tips) {guide}
- [Ephemeral Storage](/docs/guides/functions/ephemeral-storage) {guide}
- [Error Handling](/docs/guides/functions/error-handling) {guide}
- [Amazon Bedrock Image Generator](/docs/guides/functions/examples/amazon-bedrock-image-generator) {tutorial}
- [Auth Send Email Hook React Email Resend](/docs/guides/functions/examples/auth-send-email-hook-react-email-resend) {tutorial}
- [Cloudflare Turnstile](/docs/guides/functions/examples/cloudflare-turnstile) {tutorial}
- [Discord Bot](/docs/guides/functions/examples/discord-bot) {tutorial}
- [Elevenlabs Generate Speech Stream](/docs/guides/functions/examples/elevenlabs-generate-speech-stream) {tutorial}
- [Elevenlabs Transcribe Speech](/docs/guides/functions/examples/elevenlabs-transcribe-speech) {tutorial}
- [Github Actions](/docs/guides/functions/examples/github-actions) {tutorial}
- [Image Manipulation](/docs/guides/functions/examples/image-manipulation) {tutorial}
- [MCP Server MCP Lite](/docs/guides/functions/examples/mcp-server-mcp-lite) {tutorial}
- [Og Image](/docs/guides/functions/examples/og-image) {tutorial}
- [Push Notifications](/docs/guides/functions/examples/push-notifications) {tutorial}
- [Rate Limiting](/docs/guides/functions/examples/rate-limiting) {tutorial}
- [Screenshots](/docs/guides/functions/examples/screenshots) {tutorial}
- [Semantic Search](/docs/guides/functions/examples/semantic-search) {tutorial}
- [Send Emails](/docs/guides/functions/examples/send-emails) {tutorial}
- [Sentry Monitoring](/docs/guides/functions/examples/sentry-monitoring) {tutorial}
- [Slack Bot Mention](/docs/guides/functions/examples/slack-bot-mention) {tutorial}
- [Stripe Webhooks](/docs/guides/functions/examples/stripe-webhooks) {tutorial}
- [Telegram Bot](/docs/guides/functions/examples/telegram-bot) {tutorial}
- [Upstash Redis](/docs/guides/functions/examples/upstash-redis) {tutorial}
- [Function Configuration](/docs/guides/functions/function-configuration) {reference}
- [HTTP Methods](/docs/guides/functions/http-methods) {guide}
- [Kysely Postgres](/docs/guides/functions/kysely-postgres) {guide}
- [Limits](/docs/guides/functions/limits) {guide}
- [Logging](/docs/guides/functions/logging) {guide}
- [Pricing](/docs/guides/functions/pricing) {reference}
- [Quickstart](/docs/guides/functions/quickstart) {tutorial}
- [Quickstart Dashboard](/docs/guides/functions/quickstart-dashboard) {tutorial}
- [Recursive Functions](/docs/guides/functions/recursive-functions) {guide}
- [Regional Invocation](/docs/guides/functions/regional-invocation) {guide}
- [Routing](/docs/guides/functions/routing) {guide}
- [Schedule Functions](/docs/guides/functions/schedule-functions) {guide}
- [Secrets](/docs/guides/functions/secrets) {guide}
- [Status Codes](/docs/guides/functions/status-codes) {guide}
- [Storage Caching](/docs/guides/functions/storage-caching) {guide}
- [Unit Test](/docs/guides/functions/unit-test) {guide}
- [Wasm](/docs/guides/functions/wasm) {guide}
- [Websockets](/docs/guides/functions/websockets) {guide}

## Getting Started (41 pages)

- [Getting Started](/docs/guides/getting-started) {tutorial}
- [AI Prompts](/docs/guides/getting-started/ai-prompts) {tutorial}
- [AI Skills](/docs/guides/getting-started/ai-skills) {tutorial}
- [Architecture](/docs/guides/getting-started/architecture) {tutorial}
- [Byo MCP](/docs/guides/getting-started/byo-mcp) {tutorial}
- [Features](/docs/guides/getting-started/features) {tutorial}
- [MCP](/docs/guides/getting-started/mcp) {tutorial}
- [Expo React Native](/docs/guides/getting-started/quickstarts/expo-react-native) {tutorial}
- [Flask](/docs/guides/getting-started/quickstarts/flask) {tutorial}
- [Flutter](/docs/guides/getting-started/quickstarts/flutter) {tutorial}
- [Hono](/docs/guides/getting-started/quickstarts/hono) {tutorial}
- [Ios Swiftui](/docs/guides/getting-started/quickstarts/ios-swiftui) {tutorial}
- [Kotlin](/docs/guides/getting-started/quickstarts/kotlin) {tutorial}
- [Laravel](/docs/guides/getting-started/quickstarts/laravel) {tutorial}
- [Nextjs](/docs/guides/getting-started/quickstarts/nextjs) {tutorial}
- [Nuxtjs](/docs/guides/getting-started/quickstarts/nuxtjs) {tutorial}
- [Reactjs](/docs/guides/getting-started/quickstarts/reactjs) {tutorial}
- [Redwoodjs](/docs/guides/getting-started/quickstarts/redwoodjs) {tutorial}
- [Refine](/docs/guides/getting-started/quickstarts/refine) {tutorial}
- [Ruby on Rails](/docs/guides/getting-started/quickstarts/ruby-on-rails) {tutorial}
- [Solidjs](/docs/guides/getting-started/quickstarts/solidjs) {tutorial}
- [Sveltekit](/docs/guides/getting-started/quickstarts/sveltekit) {tutorial}
- [Tanstack](/docs/guides/getting-started/quickstarts/tanstack) {tutorial}
- [Vue](/docs/guides/getting-started/quickstarts/vue) {tutorial}
- [With Angular](/docs/guides/getting-started/tutorials/with-angular) {tutorial}
- [With Expo React Native](/docs/guides/getting-started/tutorials/with-expo-react-native) {tutorial}
- [With Flutter](/docs/guides/getting-started/tutorials/with-flutter) {tutorial}
- [With Ionic Angular](/docs/guides/getting-started/tutorials/with-ionic-angular) {tutorial}
- [With Ionic React](/docs/guides/getting-started/tutorials/with-ionic-react) {tutorial}
- [With Ionic Vue](/docs/guides/getting-started/tutorials/with-ionic-vue) {tutorial}
- [With Kotlin](/docs/guides/getting-started/tutorials/with-kotlin) {tutorial}
- [With Nextjs](/docs/guides/getting-started/tutorials/with-nextjs) {tutorial}
- [With Nuxt 3](/docs/guides/getting-started/tutorials/with-nuxt-3) {tutorial}
- [With React](/docs/guides/getting-started/tutorials/with-react) {tutorial}
- [With Redwoodjs](/docs/guides/getting-started/tutorials/with-redwoodjs) {tutorial}
- [With Refine](/docs/guides/getting-started/tutorials/with-refine) {tutorial}
- [With Solidjs](/docs/guides/getting-started/tutorials/with-solidjs) {tutorial}
- [With Svelte](/docs/guides/getting-started/tutorials/with-svelte) {tutorial}
- [With Sveltekit](/docs/guides/getting-started/tutorials/with-sveltekit) {tutorial}
- [With Swift](/docs/guides/getting-started/tutorials/with-swift) {tutorial}
- [With Vue 3](/docs/guides/getting-started/tutorials/with-vue-3) {tutorial}

## Integrations (6 pages)

- [Integrations](/docs/guides/integrations) {guide}
- [Build a Supabase OAUTH Integration](/docs/guides/integrations/build-a-supabase-oauth-integration) {guide}
- [OAUTH Scopes](/docs/guides/integrations/build-a-supabase-oauth-integration/oauth-scopes) {guide}
- [Supabase for Platforms](/docs/guides/integrations/supabase-for-platforms) {guide}
- [Supabase Marketplace](/docs/guides/integrations/supabase-marketplace) {guide}
- [Vercel Marketplace](/docs/guides/integrations/vercel-marketplace) {guide}

## Local Development (11 pages)

- [Local Development](/docs/guides/local-development) {guide}
- [Getting Started](/docs/guides/local-development/cli/getting-started) {tutorial}
- [Testing and Linting](/docs/guides/local-development/cli/testing-and-linting) {tool-reference}
- [Customizing Email Templates](/docs/guides/local-development/customizing-email-templates) {guide}
- [Declarative Database Schemas](/docs/guides/local-development/declarative-database-schemas) {guide}
- [Managing Config](/docs/guides/local-development/managing-config) {reference}
- [Overview](/docs/guides/local-development/overview) {overview}
- [Restoring Downloaded Backup](/docs/guides/local-development/restoring-downloaded-backup) {guide}
- [Seeding Your Database](/docs/guides/local-development/seeding-your-database) {guide}
- [Overview](/docs/guides/local-development/testing/overview) {overview}
- [Pgtap Extended](/docs/guides/local-development/testing/pgtap-extended) {guide}

## Platform (75 pages)

- [Platform](/docs/guides/platform) {guide}
- [Access Control](/docs/guides/platform/access-control) {guide}
- [AWS Marketplace](/docs/guides/platform/aws-marketplace) {guide}
- [Account Setup](/docs/guides/platform/aws-marketplace/account-setup) {guide}
- [Faq](/docs/guides/platform/aws-marketplace/faq) {guide}
- [Getting Started](/docs/guides/platform/aws-marketplace/getting-started) {tutorial}
- [Invoices](/docs/guides/platform/aws-marketplace/invoices) {guide}
- [Manage Your Subscription](/docs/guides/platform/aws-marketplace/manage-your-subscription) {guide}
- [Backups](/docs/guides/platform/backups) {guide}
- [Billing Faq](/docs/guides/platform/billing-faq) {reference}
- [Billing on Supabase](/docs/guides/platform/billing-on-supabase) {reference}
- [Clone Project](/docs/guides/platform/clone-project) {guide}
- [Compute and Disk](/docs/guides/platform/compute-and-disk) {guide}
- [Cost Control](/docs/guides/platform/cost-control) {guide}
- [Credits](/docs/guides/platform/credits) {guide}
- [Custom Domains](/docs/guides/platform/custom-domains) {guide}
- [Database Size](/docs/guides/platform/database-size) {guide}
- [Get Set Up for Billing](/docs/guides/platform/get-set-up-for-billing) {reference}
- [Hipaa Projects](/docs/guides/platform/hipaa-projects) {guide}
- [Ipv4 Address](/docs/guides/platform/ipv4-address) {guide}
- [Manage Your Subscription](/docs/guides/platform/manage-your-subscription) {guide}
- [Manage Your Usage](/docs/guides/platform/manage-your-usage) {guide}
- [Advanced Mfa Phone](/docs/guides/platform/manage-your-usage/advanced-mfa-phone) {guide}
- [Branching](/docs/guides/platform/manage-your-usage/branching) {guide}
- [Compute](/docs/guides/platform/manage-your-usage/compute) {guide}
- [Custom Domains](/docs/guides/platform/manage-your-usage/custom-domains) {guide}
- [Disk Iops](/docs/guides/platform/manage-your-usage/disk-iops) {guide}
- [Disk Size](/docs/guides/platform/manage-your-usage/disk-size) {guide}
- [Disk Throughput](/docs/guides/platform/manage-your-usage/disk-throughput) {guide}
- [Edge Function Invocations](/docs/guides/platform/manage-your-usage/edge-function-invocations) {guide}
- [Egress](/docs/guides/platform/manage-your-usage/egress) {guide}
- [Ipv4](/docs/guides/platform/manage-your-usage/ipv4) {guide}
- [Log Drains](/docs/guides/platform/manage-your-usage/log-drains) {guide}
- [Monthly Active Users](/docs/guides/platform/manage-your-usage/monthly-active-users) {guide}
- [Monthly Active Users SSO](/docs/guides/platform/manage-your-usage/monthly-active-users-sso) {guide}
- [Monthly Active Users Third Party](/docs/guides/platform/manage-your-usage/monthly-active-users-third-party) {guide}
- [Point in Time Recovery](/docs/guides/platform/manage-your-usage/point-in-time-recovery) {guide}
- [Read Replicas](/docs/guides/platform/manage-your-usage/read-replicas) {guide}
- [Realtime Messages](/docs/guides/platform/manage-your-usage/realtime-messages) {guide}
- [Realtime Peak Connections](/docs/guides/platform/manage-your-usage/realtime-peak-connections) {guide}
- [Storage Image Transformations](/docs/guides/platform/manage-your-usage/storage-image-transformations) {guide}
- [Storage Size](/docs/guides/platform/manage-your-usage/storage-size) {guide}
- [Org Mfa Enforcement](/docs/guides/platform/mfa/org-mfa-enforcement) {guide}
- [Migrating to Supabase](/docs/guides/platform/migrating-to-supabase) {guide}
- [Amazon Rds](/docs/guides/platform/migrating-to-supabase/amazon-rds) {guide}
- [Auth0](/docs/guides/platform/migrating-to-supabase/auth0) {guide}
- [Firebase Auth](/docs/guides/platform/migrating-to-supabase/firebase-auth) {guide}
- [Firebase Storage](/docs/guides/platform/migrating-to-supabase/firebase-storage) {guide}
- [Firestore Data](/docs/guides/platform/migrating-to-supabase/firestore-data) {guide}
- [Heroku](/docs/guides/platform/migrating-to-supabase/heroku) {guide}
- [Mssql](/docs/guides/platform/migrating-to-supabase/mssql) {guide}
- [Mysql](/docs/guides/platform/migrating-to-supabase/mysql) {guide}
- [Neon](/docs/guides/platform/migrating-to-supabase/neon) {guide}
- [Postgres](/docs/guides/platform/migrating-to-supabase/postgres) {guide}
- [Render](/docs/guides/platform/migrating-to-supabase/render) {guide}
- [Vercel Postgres](/docs/guides/platform/migrating-to-supabase/vercel-postgres) {guide}
- [Migrating Within Supabase](/docs/guides/platform/migrating-within-supabase) {guide}
- [Backup Restore](/docs/guides/platform/migrating-within-supabase/backup-restore) {guide}
- [Dashboard Restore](/docs/guides/platform/migrating-within-supabase/dashboard-restore) {guide}
- [Multi Factor Authentication](/docs/guides/platform/multi-factor-authentication) {guide}
- [Network Restrictions](/docs/guides/platform/network-restrictions) {guide}
- [Performance](/docs/guides/platform/performance) {guide}
- [Permissions](/docs/guides/platform/permissions) {guide}
- [Privatelink](/docs/guides/platform/privatelink) {guide}
- [Project Transfer](/docs/guides/platform/project-transfer) {guide}
- [Read Replicas](/docs/guides/platform/read-replicas) {guide}
- [Getting Started](/docs/guides/platform/read-replicas/getting-started) {tutorial}
- [Regions](/docs/guides/platform/regions) {guide}
- [SSL Enforcement](/docs/guides/platform/ssl-enforcement) {guide}
- [SSO](/docs/guides/platform/sso) {guide}
- [Azure](/docs/guides/platform/sso/azure) {guide}
- [Gsuite](/docs/guides/platform/sso/gsuite) {guide}
- [Okta](/docs/guides/platform/sso/okta) {guide}
- [Upgrading](/docs/guides/platform/upgrading) {guide}
- [Your Monthly Invoice](/docs/guides/platform/your-monthly-invoice) {guide}

## Queues (6 pages)

- [Queues](/docs/guides/queues) {guide}
- [API](/docs/guides/queues/api) {guide}
- [Consuming Messages with Edge Functions](/docs/guides/queues/consuming-messages-with-edge-functions) {guide}
- [Expose Self Hosted Queues](/docs/guides/queues/expose-self-hosted-queues) {guide}
- [Pgmq](/docs/guides/queues/pgmq) {guide}
- [Quickstart](/docs/guides/queues/quickstart) {tutorial}

## Realtime (19 pages)

- [Realtime](/docs/guides/realtime) {guide}
- [Architecture](/docs/guides/realtime/architecture) {guide}
- [Authorization](/docs/guides/realtime/authorization) {guide}
- [Benchmarks](/docs/guides/realtime/benchmarks) {guide}
- [Broadcast](/docs/guides/realtime/broadcast) {guide}
- [Concepts](/docs/guides/realtime/concepts) {guide}
- [Error Codes](/docs/guides/realtime/error_codes) {guide}
- [Getting Started](/docs/guides/realtime/getting_started) {guide}
- [Limits](/docs/guides/realtime/limits) {guide}
- [Postgres Changes](/docs/guides/realtime/postgres-changes) {guide}
- [Presence](/docs/guides/realtime/presence) {guide}
- [Pricing](/docs/guides/realtime/pricing) {reference}
- [Protocol](/docs/guides/realtime/protocol) {guide}
- [Realtime Listening Flutter](/docs/guides/realtime/realtime-listening-flutter) {guide}
- [Realtime User Presence](/docs/guides/realtime/realtime-user-presence) {guide}
- [Realtime with Nextjs](/docs/guides/realtime/realtime-with-nextjs) {guide}
- [Reports](/docs/guides/realtime/reports) {guide}
- [Settings](/docs/guides/realtime/settings) {reference}
- [Subscribing to Database Changes](/docs/guides/realtime/subscribing-to-database-changes) {guide}

## Resources (2 pages)

- [Resources](/docs/guides/resources) {guide}
- [Glossary](/docs/guides/resources/glossary) {guide}

## Security (7 pages)

- [Security](/docs/guides/security) {guide}
- [Hipaa Compliance](/docs/guides/security/hipaa-compliance) {guide}
- [Platform Audit Logs](/docs/guides/security/platform-audit-logs) {guide}
- [Platform Security](/docs/guides/security/platform-security) {guide}
- [Product Security](/docs/guides/security/product-security) {guide}
- [Security Testing](/docs/guides/security/security-testing) {guide}
- [Soc 2 Compliance](/docs/guides/security/soc-2-compliance) {guide}

## Self Hosting (13 pages)

- [Self Hosting](/docs/guides/self-hosting) {guide}
- [Copy from Platform S3](/docs/guides/self-hosting/copy-from-platform-s3) {guide}
- [Custom Email Templates](/docs/guides/self-hosting/custom-email-templates) {guide}
- [Docker](/docs/guides/self-hosting/docker) {guide}
- [Enable MCP](/docs/guides/self-hosting/enable-mcp) {guide}
- [Restore from Platform](/docs/guides/self-hosting/restore-from-platform) {guide}
- [Self Hosted Auth Keys](/docs/guides/self-hosting/self-hosted-auth-keys) {guide}
- [Self Hosted Functions](/docs/guides/self-hosting/self-hosted-functions) {guide}
- [Self Hosted OAUTH](/docs/guides/self-hosting/self-hosted-oauth) {guide}
- [Self Hosted Phone Mfa](/docs/guides/self-hosting/self-hosted-phone-mfa) {guide}
- [Self Hosted Proxy HTTPS](/docs/guides/self-hosting/self-hosted-proxy-https) {guide}
- [Self Hosted S3](/docs/guides/self-hosting/self-hosted-s3) {guide}
- [Self Hosted SAML SSO](/docs/guides/self-hosting/self-hosted-saml-sso) {guide}

## Storage (42 pages)

- [Storage](/docs/guides/storage) {guide}
- [Connecting to Analytics Bucket](/docs/guides/storage/analytics/connecting-to-analytics-bucket) {guide}
- [Creating Analytics Buckets](/docs/guides/storage/analytics/creating-analytics-buckets) {guide}
- [Apache Spark](/docs/guides/storage/analytics/examples/apache-spark) {tutorial}
- [Duckdb](/docs/guides/storage/analytics/examples/duckdb) {tutorial}
- [Pyiceberg](/docs/guides/storage/analytics/examples/pyiceberg) {tutorial}
- [Introduction](/docs/guides/storage/analytics/introduction) {overview}
- [Limits](/docs/guides/storage/analytics/limits) {guide}
- [Pricing](/docs/guides/storage/analytics/pricing) {reference}
- [Query with Postgres](/docs/guides/storage/analytics/query-with-postgres) {guide}
- [Creating Buckets](/docs/guides/storage/buckets/creating-buckets) {guide}
- [Fundamentals](/docs/guides/storage/buckets/fundamentals) {guide}
- [Fundamentals](/docs/guides/storage/cdn/fundamentals) {guide}
- [Metrics](/docs/guides/storage/cdn/metrics) {guide}
- [Smart CDN](/docs/guides/storage/cdn/smart-cdn) {guide}
- [Error Codes](/docs/guides/storage/debugging/error-codes) {guide}
- [Logs](/docs/guides/storage/debugging/logs) {guide}
- [Copy Move Objects](/docs/guides/storage/management/copy-move-objects) {guide}
- [Delete Objects](/docs/guides/storage/management/delete-objects) {guide}
- [Pricing](/docs/guides/storage/pricing) {reference}
- [Scaling](/docs/guides/storage/production/scaling) {guide}
- [Quickstart](/docs/guides/storage/quickstart) {tutorial}
- [Authentication](/docs/guides/storage/s3/authentication) {guide}
- [Compatibility](/docs/guides/storage/s3/compatibility) {guide}
- [Custom Roles](/docs/guides/storage/schema/custom-roles) {guide}
- [Design](/docs/guides/storage/schema/design) {guide}
- [Helper Functions](/docs/guides/storage/schema/helper-functions) {guide}
- [Access Control](/docs/guides/storage/security/access-control) {guide}
- [Ownership](/docs/guides/storage/security/ownership) {guide}
- [Bandwidth](/docs/guides/storage/serving/bandwidth) {guide}
- [Downloads](/docs/guides/storage/serving/downloads) {guide}
- [Image Transformations](/docs/guides/storage/serving/image-transformations) {guide}
- [File Limits](/docs/guides/storage/uploads/file-limits) {guide}
- [Resumable Uploads](/docs/guides/storage/uploads/resumable-uploads) {guide}
- [S3 Uploads](/docs/guides/storage/uploads/s3-uploads) {guide}
- [Standard Uploads](/docs/guides/storage/uploads/standard-uploads) {guide}
- [Creating Vector Buckets](/docs/guides/storage/vector/creating-vector-buckets) {guide}
- [Introduction](/docs/guides/storage/vector/introduction) {overview}
- [Limits](/docs/guides/storage/vector/limits) {guide}
- [Querying Vectors](/docs/guides/storage/vector/querying-vectors) {guide}
- [Storing Vectors](/docs/guides/storage/vector/storing-vectors) {guide}
- [Working with Indexes](/docs/guides/storage/vector/working-with-indexes) {guide}

## Telemetry (10 pages)

- [Telemetry](/docs/guides/telemetry) {guide}
- [Advanced Log Filtering](/docs/guides/telemetry/advanced-log-filtering) {guide}
- [Log Drains](/docs/guides/telemetry/log-drains) {guide}
- [Logs](/docs/guides/telemetry/logs) {guide}
- [Metrics](/docs/guides/telemetry/metrics) {guide}
- [Grafana Cloud](/docs/guides/telemetry/metrics/grafana-cloud) {guide}
- [Grafana Self Hosted](/docs/guides/telemetry/metrics/grafana-self-hosted) {guide}
- [Vendor Agnostic](/docs/guides/telemetry/metrics/vendor-agnostic) {guide}
- [Reports](/docs/guides/telemetry/reports) {guide}
- [Sentry Monitoring](/docs/guides/telemetry/sentry-monitoring) {guide}

## Troubleshooting (173 pages)

- [42501 Permission Denied for Table Httprequestqueue](/docs/guides/troubleshooting/42501--permission-denied-for-table-httprequestqueue-KnozmQ) {guide}
- [All About Supabase Egress](/docs/guides/troubleshooting/all-about-supabase-egress-a_Sg_e) {overview}
- [An Invalid Response Was Received from the Upstream Server Error When Querying Auth Ri4vl](/docs/guides/troubleshooting/an-invalid-response-was-received-from-the-upstream-server-error-when-querying-auth-RI4Vl-) {guide}
- [App Store Rejection TLS Error in Ipv6 Only Environments 4e9c62](/docs/guides/troubleshooting/app-store-rejection-tls-error-in-ipv6-only-environments-4e9c62) {guide}
- [Are All Features Available in Self Hosted Supabase](/docs/guides/troubleshooting/are-all-features-available-in-self-hosted-supabase-THPcqw) {guide}
- [Auth Error 401 Invalid Claim Missing Sub Afwmr](/docs/guides/troubleshooting/auth-error-401-invalid-claim-missing-sub--AFwMR) {guide}
- [Auth Hooks Invalid Payload When Anonymous Users Attempt Phone Changes 022c47](/docs/guides/troubleshooting/auth-hooks-invalid-payload-when-anonymous-users-attempt-phone-changes-022c47) {guide}
- [Autovacuum Stalled Due to Inactive Replication Slot D55aa2](/docs/guides/troubleshooting/autovacuum-stalled-due-to-inactive-replication-slot-d55aa2) {guide}
- [Avoiding Timeouts in Long Running Queries 6nmbdn](/docs/guides/troubleshooting/avoiding-timeouts-in-long-running-queries-6nmbdN) {guide}
- [Canceling Statement Due to Statement Timeout 581wfv](/docs/guides/troubleshooting/canceling-statement-due-to-statement-timeout-581wFv) {guide}
- [Cant Access Supabase Project Lovable Cloud](/docs/guides/troubleshooting/cant-access-supabase-project-lovable-cloud) {guide}
- [Certain Operations Are Too Complex to Perform Directly Using the Client Libraries 8japhh](/docs/guides/troubleshooting/certain-operations-are-too-complex-to-perform-directly-using-the-client-libraries-8JaphH) {tool-reference}
- [Change Email Associated with Supabase Account](/docs/guides/troubleshooting/change-email-associated-with-supabase-account-T5eHNT) {guide}
- [Change Project Region](/docs/guides/troubleshooting/change-project-region-eWJo5Z) {guide}
- [Check Usage for Monthly Active Users Mau](/docs/guides/troubleshooting/check-usage-for-monthly-active-users-mau-MwZaBs) {guide}
- [Cloudflare Origin Error 1016 on Custom Domain A57af4](/docs/guides/troubleshooting/cloudflare-origin-error-1016-on-custom-domain-a57af4) {guide}
- [Converted Github Account to Organisation Lost Supabase Account Access 5wse 1](/docs/guides/troubleshooting/converted-github-account-to-organisation---lost-supabase-account-access-5wsE_1) {guide}
- [Customizing Emails by Language Kz 38q](/docs/guides/troubleshooting/customizing-emails-by-language-KZ_38Q) {guide}
- [Dashboard Errors When Managing Users](/docs/guides/troubleshooting/dashboard-errors-when-managing-users-N1ls4A) {guide}
- [Database API 42501 Errors](/docs/guides/troubleshooting/database-api-42501-errors) {guide}
- [Database Error Remaining Connection Slots Are Reserved for Non Replication Superuser Connections 3v3nib](/docs/guides/troubleshooting/database-error-remaining-connection-slots-are-reserved-for-non-replication-superuser-connections-3V3nIb) {guide}
- [Database Error Saving New User Ru Ewb](/docs/guides/troubleshooting/database-error-saving-new-user-RU_EwB) {guide}
- [Deprecated RLS Features](/docs/guides/troubleshooting/deprecated-rls-features-Pm77Zs) {guide}
- [Disabling Prepared Statements](/docs/guides/troubleshooting/disabling-prepared-statements-qL8lEL) {guide}
- [Discovering and Interpreting API Errors in the Logs 7xrei9](/docs/guides/troubleshooting/discovering-and-interpreting-api-errors-in-the-logs-7xREI9) {guide}
- [Do I Need to Expose Security Definer Functions in Row Level Security Policies](/docs/guides/troubleshooting/do-i-need-to-expose-security-definer-functions-in-row-level-security-policies-iI0uOw) {guide}
- [Download Logical Backups](/docs/guides/troubleshooting/download-logical-backups) {guide}
- [Edge Function 401 Error Response](/docs/guides/troubleshooting/edge-function-401-error-response) {guide}
- [Edge Function 404 Error Response](/docs/guides/troubleshooting/edge-function-404-error-response) {guide}
- [Edge Function 500 Error Response](/docs/guides/troubleshooting/edge-function-500-error-response) {guide}
- [Edge Function 503 Response](/docs/guides/troubleshooting/edge-function-503-response) {guide}
- [Edge Function 504 Error Response](/docs/guides/troubleshooting/edge-function-504-error-response) {guide}
- [Edge Function 546 Error Response](/docs/guides/troubleshooting/edge-function-546-error-response) {guide}
- [Edge Function Bundle Size Issues](/docs/guides/troubleshooting/edge-function-bundle-size-issues) {guide}
- [Edge Function Cpu Limits](/docs/guides/troubleshooting/edge-function-cpu-limits) {guide}
- [Edge Function Dependency Analysis](/docs/guides/troubleshooting/edge-function-dependency-analysis) {guide}
- [Edge Function Fails Deploy](/docs/guides/troubleshooting/edge-function-fails-deploy) {guide}
- [Edge Function Monitoring Resource Usage](/docs/guides/troubleshooting/edge-function-monitoring-resource-usage) {guide}
- [Edge Function Shutdown Reasons Explained](/docs/guides/troubleshooting/edge-function-shutdown-reasons-explained) {guide}
- [Edge Function Takes Too Long to Respond](/docs/guides/troubleshooting/edge-function-takes-too-long-to-respond) {guide}
- [Edge Function Wall Clock Time Limit Reached](/docs/guides/troubleshooting/edge-function-wall-clock-time-limit-reached-Nk38bW) {guide}
- [Email Password Login Disabled Supabase Vercel Marketplace A7dd36](/docs/guides/troubleshooting/email-password-login-disabled-supabase-vercel-marketplace-a7dd36) {guide}
- [Email Template Not Updating](/docs/guides/troubleshooting/email-template-not-updating) {guide}
- [Enabling Ipv4 Addon](/docs/guides/troubleshooting/enabling-ipv4-addon) {guide}
- [Error Connection Refused When Trying to Connect to Supabase Database Hwg0dr](/docs/guides/troubleshooting/error-connection-refused-when-trying-to-connect-to-supabase-database-hwG0Dr) {guide}
- [Error Index Row Size Exceeds Btree Version 4 Maximum for Index](/docs/guides/troubleshooting/error-index-row-size-exceeds-btree-version-4-maximum-for-index-LMmoeU) {guide}
- [Error Invalid Byte Sequence for Encoding Utf8 0x00 When Accessing Triggers or Webhooks E78cf8](/docs/guides/troubleshooting/error-invalid-byte-sequence-for-encoding-utf8-0x00-when-accessing-triggers-or-webhooks-e78cf8) {guide}
- [Error Invalid Totp Code Entered](/docs/guides/troubleshooting/error-invalid-totp-code-entered-CukLCj) {guide}
- [Error No Pghbaconf Entry for Host Xxxxxxxxxxx User Postgres Database Postgres SSL Off](/docs/guides/troubleshooting/error-no-pghbaconf-entry-for-host-xxxxxxxxxxx-user-postgres-database-postgres-ssl-off-GOt5Ja) {guide}
- [Error Prepared Statement Xxx Already Exists 3laqem](/docs/guides/troubleshooting/error-prepared-statement-xxx-already-exists-3laqeM) {guide}
- [Error Target Organization Is Not Managed by Vercel Marketplace During Project Transfer 5262c3](/docs/guides/troubleshooting/error-target-organization-is-not-managed-by-vercel-marketplace-during-project-transfer-5262c3) {guide}
- [Exhaust Disk Io](/docs/guides/troubleshooting/exhaust-disk-io) {guide}
- [Exhaust Ram](/docs/guides/troubleshooting/exhaust-ram) {guide}
- [Exhaust Swap](/docs/guides/troubleshooting/exhaust-swap) {guide}
- [Failed to Fetch in Dashboard and Other Areas Browser Extension Dydtru](/docs/guides/troubleshooting/failed-to-fetch-in-dashboard-and-other-areas----browser-extension-dyDTRU) {guide}
- [Failed to Restore from Backup All Subscriptions and Replication Slots Must Be Dropped Before a Backup Can Be Restored L Rcvt](/docs/guides/troubleshooting/failed-to-restore-from-backup-all-subscriptions-and-replication-slots-must-be-dropped-before-a-backup-can-be-restored-L-rCvt) {guide}
- [Failed to Retrieve Tables](/docs/guides/troubleshooting/failed-to-retrieve-tables) {guide}
- [Failed to Run SQL Query Connection Terminated Due to Connection Timeout](/docs/guides/troubleshooting/failed-to-run-sql-query-connection-terminated-due-to-connection-timeout) {guide}
- [Fetch Requests to API Endpoints Arent Showing the Session](/docs/guides/troubleshooting/fetch-requests-to-api-endpoints-arent-showing-the-session-UbUwRs) {api-endpoint}
- [Fixing 520 Errors in the Database Rest API Ur5 B2](/docs/guides/troubleshooting/fixing-520-errors-in-the-database-rest-api-Ur5-B2) {guide}
- [Forbidden Resource Error from the CLI](/docs/guides/troubleshooting/forbidden-resource-error-from-the-cli-L6rm6l) {tool-reference}
- [Get Detailed Storage Metrics with the AWS CLI 587a7d](/docs/guides/troubleshooting/get-detailed-storage-metrics-with-the-aws-cli-587a7d) {tool-reference}
- [Google Auth Fails for Some Users](/docs/guides/troubleshooting/google-auth-fails-for-some-users-XcFXEu) {guide}
- [Grafana Not Displaying Data](/docs/guides/troubleshooting/grafana-not-displaying-data-sXJrMj) {guide}
- [High Cpu and Slow Queries with Error Must Be a Superuser to Terminate Superuser Process](/docs/guides/troubleshooting/high-cpu-and-slow-queries-with-error-must-be-a-superuser-to-terminate-superuser-process) {guide}
- [High Cpu Usage](/docs/guides/troubleshooting/high-cpu-usage) {guide}
- [High Latency with Supabase Client Z0pzzr](/docs/guides/troubleshooting/high-latency-with-supabase-client-z0pZzR) {tool-reference}
- [How Can I Revoke Execution of a Postgresql Function 2gyb0a](/docs/guides/troubleshooting/how-can-i-revoke-execution-of-a-postgresql-function-2GYb0A) {guide}
- [How Do I Check Gotrueapi Version of a Supabase Project](/docs/guides/troubleshooting/how-do-i-check-gotrueapi-version-of-a-supabase-project-lQAnOR) {guide}
- [How Do I Make the Cookies Httponly Vwwefx](/docs/guides/troubleshooting/how-do-i-make-the-cookies-httponly-vwweFx) {guide}
- [How Do I Reset My Supabase Database Password](/docs/guides/troubleshooting/how-do-i-reset-my-supabase-database-password-oTs5sB) {guide}
- [How Do I Update Connection Pool Settings in My Dashboard Waxtj](/docs/guides/troubleshooting/how-do-i-update-connection-pool-settings-in-my-dashboard-wAxTJ_) {reference}
- [How Do You Troubleshoot Nextjs Supabase Auth Issues Rimczv](/docs/guides/troubleshooting/how-do-you-troubleshoot-nextjs---supabase-auth-issues-riMCZV) {guide}
- [How Long Does It Take to Restore a Database from a Point in Time Backup Pitr](/docs/guides/troubleshooting/how-long-does-it-take-to-restore-a-database-from-a-point-in-time-backup-pitr-qO8gOG) {guide}
- [How Postgres Chooses Which Index to Use Jhrf4](/docs/guides/troubleshooting/how-postgres-chooses-which-index-to-use-_JHrf4) {guide}
- [How to Bypass Cooldown Period](/docs/guides/troubleshooting/how-to-bypass-cooldown-period) {guide}
- [How to Change Max Database Connections Bq8p5](/docs/guides/troubleshooting/how-to-change-max-database-connections-_BQ8P5) {guide}
- [How to Check If My Queries Are Being Blocked by Other Queries](/docs/guides/troubleshooting/how-to-check-if-my-queries-are-being-blocked-by-other-queries-NSKtR1) {guide}
- [How to Delete a Role in Postgres 8 Avxy](/docs/guides/troubleshooting/how-to-delete-a-role-in-postgres-8-AvxY) {guide}
- [How to Delete Vercel Linked Projects 9d08aa](/docs/guides/troubleshooting/how-to-delete-vercel-linked-projects-9d08aa) {guide}
- [How to Interpret and Explore the Postgres Logs](/docs/guides/troubleshooting/how-to-interpret-and-explore-the-postgres-logs-OuCIOj) {guide}
- [How to Migrate from Supabase Auth Helpers to Ssr Package 5nrunm](/docs/guides/troubleshooting/how-to-migrate-from-supabase-auth-helpers-to-ssr-package-5NRunM) {guide}
- [How to View Database Metrics Uqf2z](/docs/guides/troubleshooting/how-to-view-database-metrics-uqf2z_) {guide}
- [HTTP API Issues](/docs/guides/troubleshooting/http-api-issues) {guide}
- [HTTP Status Codes](/docs/guides/troubleshooting/http-status-codes) {guide}
- [I Am Not Receiving Password Reset Emails for Supabase Dashboard Co5yf](/docs/guides/troubleshooting/i-am-not-receiving-password-reset-emails-for-supabase-dashboard--cO5yf) {guide}
- [Identify Lovable Cloud or Supabase Backend](/docs/guides/troubleshooting/identify-lovable-cloud-or-supabase-backend) {guide}
- [Importing Stripe or Other Modules from Esmsh on Deno Edge Functions Throws an Error](/docs/guides/troubleshooting/importing-stripe-or-other-modules-from-esmsh-on-deno-edge-functions-throws-an-error-TmbB5p) {guide}
- [Increase Vector Lookup Speeds by Applying an Hsnw Index Ohlhum](/docs/guides/troubleshooting/increase-vector-lookup-speeds-by-applying-an-hsnw-index-ohLHUM) {guide}
- [Inserting into Sequenceserial Table Causes Duplicate Key Violates Unique Constraint Error Pi6dnc](/docs/guides/troubleshooting/inserting-into-sequenceserial-table-causes-duplicate-key-violates-unique-constraint-error-pi6DnC) {guide}
- [Inspecting Edge Function Environment Variables Wg5qoq](/docs/guides/troubleshooting/inspecting-edge-function-environment-variables-wg5qOQ) {guide}
- [Insufficient Privilege When Accessing Pgstatstatements E5m Eq](/docs/guides/troubleshooting/insufficient-privilege-when-accessing-pgstatstatements-e5M_EQ) {guide}
- [Interpreting Supabase Grafana Cpu Charts 9jslkc](/docs/guides/troubleshooting/interpreting-supabase-grafana-cpu-charts-9JSlkC) {guide}
- [Interpreting Supabase Grafana Io Charts](/docs/guides/troubleshooting/interpreting-supabase-grafana-io-charts-MUynDR) {guide}
- [Issues Serving Edge Functions Locally](/docs/guides/troubleshooting/issues-serving-edge-functions-locally) {guide}
- [JWT Expired Error in Supabase Dashboard](/docs/guides/troubleshooting/jwt-expired-error-in-supabase-dashboard-F06k3x) {guide}
- [Keeping Free Projects After Pro Upgrade](/docs/guides/troubleshooting/keeping-free-projects-after-pro-upgrade-Kf9Xm2) {guide}
- [Lost Accessforgot the Mfa Device Napt 7](/docs/guides/troubleshooting/lost-accessforgot-the-mfa-device-nAPT-7) {guide}
- [Manually Created Databases Are Not Visible in the Supabase Dashboard 4415aa](/docs/guides/troubleshooting/manually-created-databases-are-not-visible-in-the-supabase-dashboard-4415aa) {guide}
- [Memory and Swap Usage Explained](/docs/guides/troubleshooting/memory-and-swap-usage-explained-aPNgm0) {guide}
- [Migrating Auth Users Between Projects](/docs/guides/troubleshooting/migrating-auth-users-between-projects) {guide}
- [Monitor Supavisor Postgres Connections](/docs/guides/troubleshooting/monitor-supavisor-postgres-connections) {guide}
- [New Branch Doesnt Copy Database](/docs/guides/troubleshooting/new-branch-doesnt-copy-database) {guide}
- [New Variable Is Null in a Trigger Function L9aoz](/docs/guides/troubleshooting/new-variable-is-null-in-a-trigger-function--l9AOZ) {guide}
- [Nextjs 1314 Stale Data When Changing RLS or Table Data 85b8oq](/docs/guides/troubleshooting/nextjs-1314-stale-data-when-changing-rls-or-table-data-85b8oQ) {guide}
- [No Toast Messages on the Dashboard](/docs/guides/troubleshooting/no-toast-messages-on-the-dashboard-BrvP8h) {guide}
- [Not Receiving Auth Emails from the Supabase Project](/docs/guides/troubleshooting/not-receiving-auth-emails-from-the-supabase-project-OFSNzw) {guide}
- [OAUTH Sign in Isnt Redirecting on the Server Side](/docs/guides/troubleshooting/oauth-sign-in-isnt-redirecting-on-the-server-side-ShGMtr) {guide}
- [Otp Verification Failures Token Has Expired or Otp Expired Errors 5ee4d0](/docs/guides/troubleshooting/otp-verification-failures-token-has-expired-or-otp_expired-errors-5ee4d0) {guide}
- [Partitioning an Existing Table with Same Name](/docs/guides/troubleshooting/partitioning-an-existing-table-with-same-name-VEnbzK) {guide}
- [Pausing Pro Projects Vnl 2a](/docs/guides/troubleshooting/pausing-pro-projects-vNL-2a) {guide}
- [Performing Administration Tasks on the Server Side with the Servicerole Secret](/docs/guides/troubleshooting/performing-administration-tasks-on-the-server-side-with-the-servicerole-secret-BYM4Fa) {guide}
- [Pg Cron Launcher Crashes with Duplicate Key Value Violates Unique Constraint Cc6472](/docs/guides/troubleshooting/pg_cron-launcher-crashes-with-duplicate-key-value-violates-unique-constraint-cc6472) {guide}
- [Pgcron Debugging Guide N1ktaz](/docs/guides/troubleshooting/pgcron-debugging-guide-n1KTaz) {guide}
- [Pgrst106 the Schema Must Be One of the Following Error When Querying an Exposed Schema](/docs/guides/troubleshooting/pgrst106-the-schema-must-be-one-of-the-following-error-when-querying-an-exposed-schema) {guide}
- [Pkce Flow Errors Cannot Parse Response or Zgotmplz in Magic Link Emails 433665](/docs/guides/troubleshooting/pkce-flow-errors-cannot-parse-response-or-zgotmplz-in-magic-link-emails-433665) {guide}
- [Postgrest Not Recognizing New Columns or Functions Bd75f5](/docs/guides/troubleshooting/postgrest-not-recognizing-new-columns-or-functions-bd75f5) {guide}
- [Prisma Error Management Cm5p O](/docs/guides/troubleshooting/prisma-error-management-Cm5P_o) {guide}
- [Project Status Reports Unhealthy Services](/docs/guides/troubleshooting/project-status-reports-unhealthy-services) {guide}
- [Rclone Error S3 Protocol Error Received Listing V1 with Istruncated Set No Nextmarker and No Contents E64d34](/docs/guides/troubleshooting/rclone-error-s3-protocol-error-received-listing-v1-with-istruncated-set-no-nextmarker-and-no-contents-e64d34) {guide}
- [Realtime Concurrent Peak Connections Quota Jddqcp](/docs/guides/troubleshooting/realtime-concurrent-peak-connections-quota-jdDqcp) {guide}
- [Realtime Connections Timed Out Status](/docs/guides/troubleshooting/realtime-connections-timed_out-status) {guide}
- [Realtime Debugging with Logger](/docs/guides/troubleshooting/realtime-debugging-with-logger) {guide}
- [Realtime Handling Silent Disconnections in Backgrounded Applications 592794](/docs/guides/troubleshooting/realtime-handling-silent-disconnections-in-backgrounded-applications-592794) {guide}
- [Realtime Heartbeat Messages](/docs/guides/troubleshooting/realtime-heartbeat-messages) {guide}
- [Realtime Project Suspended for Exceeding Quotas](/docs/guides/troubleshooting/realtime-project-suspended-for-exceeding-quotas) {guide}
- [Realtime Too Many Channels Error](/docs/guides/troubleshooting/realtime-too-many-channels-error) {guide}
- [Refresh Postgrest Schema](/docs/guides/troubleshooting/refresh-postgrest-schema) {guide}
- [Resolving 42p01 Relation Does Not Exist Error W4 9 V](/docs/guides/troubleshooting/resolving-42p01-relation-does-not-exist-error-W4_9-V) {guide}
- [Resolving 500 Status Authentication Errors 7bu5u8](/docs/guides/troubleshooting/resolving-500-status-authentication-errors-7bU5U8) {guide}
- [Resolving Database Hostname and Managing Your Ip Address](/docs/guides/troubleshooting/resolving-database-hostname-and-managing-your-ip-address-pVlwE0) {guide}
- [RLS Performance and Best Practices](/docs/guides/troubleshooting/rls-performance-and-best-practices-Z5Jjwv) {best-practices}
- [RLS Simplified](/docs/guides/troubleshooting/rls-simplified-BJTcS8) {guide}
- [Rotating Anon Service and JWT Secrets 1jq6yd](/docs/guides/troubleshooting/rotating-anon-service-and-jwt-secrets-1Jq6yd) {guide}
- [Running Explain Analyze on Functions](/docs/guides/troubleshooting/running-explain-analyze-on-functions) {guide}
- [Scan Error on Column Confirmation Token Converting Null to String Is Unsupported During Auth Login A0c686](/docs/guides/troubleshooting/scan-error-on-column-confirmation_token-converting-null-to-string-is-unsupported-during-auth-login-a0c686) {guide}
- [Security of Anonymous Sign Ins](/docs/guides/troubleshooting/security-of-anonymous-sign-ins-iOrGCL) {guide}
- [Seeing No Pghbaconf Entry for Host Errors in Postgres and They Come from an Ip Address That I Dont Recognize 4gds9f](/docs/guides/troubleshooting/seeing-no-pghbaconf-entry-for-host-errors-in-postgres-and-they-come-from-an-ip-address-that-i-dont-recognize-4gds9f) {guide}
- [Should I Set a Shorter Max Age Parameter on the Cookies 8sbf4v](/docs/guides/troubleshooting/should-i-set-a-shorter-max-age-parameter-on-the-cookies-8sbF4V) {guide}
- [Slow Execution of Alter Table on Large Table When Changing Column Type Qmzrpz](/docs/guides/troubleshooting/slow-execution-of-alter-table-on-large-table-when-changing-column-type-qmZRpZ) {guide}
- [Soft Deletes with Supabase Js](/docs/guides/troubleshooting/soft-deletes-with-supabase-js) {guide}
- [SSO Error You Do Not Have Permissions to Join This Organization or Prompts to Create New Organization](/docs/guides/troubleshooting/sso-error-you-do-not-have-permissions-to-join-this-organization-or-prompts-to-create-new-organization) {guide}
- [Steps to Improve Query Performance with Indexes Q8poc9](/docs/guides/troubleshooting/steps-to-improve-query-performance-with-indexes-q8PoC9) {guide}
- [Supabase Your Network Ipv4 and Ipv6 Compatibility](/docs/guides/troubleshooting/supabase--your-network-ipv4-and-ipv6-compatibility-cHe3BP) {guide}
- [Supabase CLI Failed Sasl Auth or Invalid Scram Server Final Message](/docs/guides/troubleshooting/supabase-cli-failed-sasl-auth-or-invalid-scram-server-final-message) {tool-reference}
- [Supabase Dashboard Not Loading Project Not Loading on Dashboard](/docs/guides/troubleshooting/supabase-dashboard-not-loading-project-not-loading-on-dashboard-LfMq9F) {guide}
- [Supabase Grafana Memory Charts](/docs/guides/troubleshooting/supabase-grafana-memory-charts) {guide}
- [Supabase Project Provisioned via Bolt Not Visible in Dashboard 7188fc](/docs/guides/troubleshooting/supabase-project-provisioned-via-bolt-not-visible-in-dashboard-7188fc) {guide}
- [Supabase Storage Inefficient Folder Operations and Hierarchical RLS Challenges B05a4d](/docs/guides/troubleshooting/supabase-storage-inefficient-folder-operations-and-hierarchical-rls-challenges-b05a4d) {guide}
- [Supavisor and Connection Terminology Explained 9pr Zo](/docs/guides/troubleshooting/supavisor-and-connection-terminology-explained-9pr_ZO) {guide}
- [Supavisor Faq](/docs/guides/troubleshooting/supavisor-faq-YyP5tI) {guide}
- [Transfer Edge Function from One Project to Another](/docs/guides/troubleshooting/transfer-edge-function-from-one-project-to-another) {guide}
- [Transferring from Cloud to Self Host in Supabase 2ownvw](/docs/guides/troubleshooting/transferring-from-cloud-to-self-host-in-supabase-2oWNvW) {guide}
- [Unable to Call Edge Function](/docs/guides/troubleshooting/unable-to-call-edge-function) {guide}
- [Unable to Deploy Edge Function](/docs/guides/troubleshooting/unable-to-deploy-edge-function) {guide}
- [Understanding Postgresql Explain Output](/docs/guides/troubleshooting/understanding-postgresql-explain-output-Un9dqX) {guide}
- [Understanding Postgresql Logging Levels and How They Impact Your Project](/docs/guides/troubleshooting/understanding-postgresql-logging-levels-and-how-they-impact-your-project-KXiJRm) {guide}
- [Understanding the Usage Summary on the Dashboard](/docs/guides/troubleshooting/understanding-the-usage-summary-on-the-dashboard-D7Gnle) {guide}
- [Unused External Import Warning Vite Rollup](/docs/guides/troubleshooting/unused-external-import-warning-vite-rollup) {guide}
- [Upload File Size Restrictions](/docs/guides/troubleshooting/upload-file-size-restrictions-Y4wQLT) {guide}
- [Using Google Smtp with Supabase Custom Smtp](/docs/guides/troubleshooting/using-google-smtp-with-supabase-custom-smtp-ZZzU4Y) {guide}
- [Using Sqlalchemy with Supabase](/docs/guides/troubleshooting/using-sqlalchemy-with-supabase-FUqebT) {guide}
- [Webhook Debugging Guide](/docs/guides/troubleshooting/webhook-debugging-guide-M8sk47) {guide}
- [Why Am I Being Redirected to the Wrong URL When Using Auth Redirectto Option Vqieo](/docs/guides/troubleshooting/why-am-i-being-redirected-to-the-wrong-url-when-using-auth-redirectto-option-_vqIeO) {guide}
- [Why Are There Gaps in My Postgres ID Sequence](/docs/guides/troubleshooting/why-are-there-gaps-in-my-postgres-id-sequence-Frifus) {guide}
- [Why Cant I Uploadlistetc My Public Bucket](/docs/guides/troubleshooting/why-cant-i-uploadlistetc-my-public-bucket-Z6CmGt) {guide}
- [Why Do I See Auth API Requests in the Dashboard My App Has No Users](/docs/guides/troubleshooting/why-do-i-see-auth--api-requests-in-the-dashboard-my-app-has-no-users-CyadiO) {guide}
- [Why Is My Camelcase Name Not Working in Postgres Functions or RLS Policies](/docs/guides/troubleshooting/why-is-my-camelcase-name-not-working-in-postgres-functions-or-rls-policies-EJMzVd) {guide}
- [Why Is My Select Returning an Empty Data Array and I Have Data in the Table Xvopgx](/docs/guides/troubleshooting/why-is-my-select-returning-an-empty-data-array-and-i-have-data-in-the-table-xvOPgx) {guide}
- [Why Is My Service Role Key Client Getting RLS Errors or Not Returning Data 7 1k9z](/docs/guides/troubleshooting/why-is-my-service-role-key-client-getting-rls-errors-or-not-returning-data-7_1K9z) {tool-reference}
- [Why Is My Supabase API Call Not Returning](/docs/guides/troubleshooting/why-is-my-supabase-api-call-not-returning-PGzXw0) {guide}
- [Why Supabase Edge Functions Cannot Provide Static Egress Ips for Whitelisting 3d78b0](/docs/guides/troubleshooting/why-supabase-edge-functions-cannot-provide-static-egress-ips-for-whitelisting-3d78b0) {guide}
- [Will Backups Be Accessible from the Dashboard Immediately After Upgrading to a Paid Plan](/docs/guides/troubleshooting/will-backups-be-accessible-from-the-dashboard-immediately-after-upgrading-to-a-paid-plan-hXY4rs) {guide}

