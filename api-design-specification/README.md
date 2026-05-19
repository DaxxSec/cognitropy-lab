# API Design Specification Workspace

> Treat API spec authoring as multi-source intelligence fusion: collect signals from telemetry, tickets, standards, peers, and stakeholders; weight them; produce a single OpenAPI specification with traceable provenance for every operation.

## What This Workspace Does

Most API specifications are drafted by one engineer reading the proposal doc and typing OpenAPI YAML. The result is consistent in style and quietly wrong in a hundred small places — `POST` where the existing corpus uses `PUT`, error envelopes that don't match the rest of the surface, pagination that disagrees with the documented house pattern, no consideration of how clients actually use the endpoint being replaced. The deeper failure: there is no audit trail. Six months later nobody can answer *why* `GET /v2/orders` returns `400` instead of `422` when the filter is malformed.

This workspace borrows the **multi-source intelligence fusion** discipline from defense and intelligence work — the practice of combining heterogeneous evidence (HUMINT, SIGINT, OSINT, GEOINT) into a single weighted assessment with full provenance — and applies it to API design. Each candidate operation is fused from six source classes: the existing internal API corpus, consumer telemetry, support and incident tickets, authoritative standards (OpenAPI 3.1, JSON Schema, RFCs), public peer specifications, and named human stakeholders. Sources get reliability ratings (the NATO STANAG 2022 A–F scheme adapts cleanly). Contradictions are surfaced and adjudicated explicitly. Every spec element retains a provenance tag.

The defining technique today is **multi-source intelligence fusion**. The defining output is an OpenAPI 3.1 document where `/v3/orders` doesn't just exist — it exists *because* the corpus has the `/v3/<resource>` pattern (corpus, reliability A2), the telemetry says 73% of v2 `GET /orders` calls already use the filter shape that v3 codifies (telemetry, B2), the RFC 9457 Problem Details envelope replaces the legacy error envelope flagged in 14 support tickets (tickets, C2 + standards, A1), and the security team approved the new `OAuth2` scope (stakeholder, A1). The `x-provenance` tag on the operation says exactly that.

## Why This Workspace Exists

API specifications outlive the engineers who write them, and any decision without a recorded rationale becomes a guess the next engineer has to re-litigate. Fusion gives the spec a traceability matrix instead of a tribal-knowledge oral history. It also pressure-tests the spec against the *actual* data — consumer telemetry catches "we don't need this field" before the field ships and ossifies for a decade; ticket fusion catches "this endpoint confuses everyone" before the next version repeats the mistake. The pattern is older than software; it is just under-applied here.

## Getting Started

### Prerequisites

- An OpenAPI editor / linter — Stoplight Studio, Redocly CLI, Spectral, or plain VS Code with the `42Crunch` extension.
- Read access to your service's request logs / API gateway telemetry (Datadog, Honeycomb, CloudWatch, GCP Cloud Logging, or raw access logs).
- Read access to the support / incident ticketing system (Zendesk, Jira Service Management, Linear, Intercom) — for ticket-source fusion.
- A current internal API corpus (`api/` directory of existing OpenAPI files, or a Backstage / SwaggerHub catalogue).
- `node` (for Redocly / Spectral) and `python3` (for the analysis scripts you will write into `outputs/`).
- Authorisation to view internal telemetry and ticket data per your organisation's data-handling policy.

### Quick Start

1. Clone this workspace into your API repository at `api/.claude-workspace/` (or wherever workspace tooling lives in your org).
2. Run `/source-elicit` to enumerate which of the six source classes you actually have access to for the target API surface, and what their reliability ratings are.
3. Run `/fuse-requirements` for each new or changed resource. The output is a fusion brief in `outputs/fusion/<resource>.md` with per-element provenance.
4. Run `/spec-draft-openapi` to convert the fusion brief into OpenAPI 3.1 YAML in `outputs/spec/<resource>.yaml` with `x-provenance` annotations retained.
5. Run `/contradiction-resolve` whenever the fusion brief flags conflicting sources; the adjudication lands in `outputs/adjudication/<date>-<topic>.md`.
6. Run `/standards-alignment` before any internal review to catch unconscious drift from OpenAPI 3.1 / RFC 9457 / etc.
7. For replacing or sunsetting an existing endpoint, run `/breaking-change-fusion` — never deprecate on opinion alone.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/source-elicit` | Enumerates and rates the six fusion source classes for a target API surface. | First contact with a new API surface, or quarterly to refresh ratings as data access changes. |
| `/fuse-requirements` | Combines source signals into a unified resource model with provenance and reliability. | Before drafting any new resource or changed operation. |
| `/spec-draft-openapi` | Drafts OpenAPI 3.1 YAML from the fused requirements, preserving `x-provenance`. | After `/fuse-requirements` and any required `/contradiction-resolve` rounds. |
| `/contradiction-resolve` | Surfaces conflicts across sources, scores them, proposes adjudication. | Whenever the fusion brief flags `CONFLICT` between source signals. |
| `/trace-provenance` | Produces the source chain that justifies any spec element. | During internal review, audit, or when challenged on a design decision. |
| `/breaking-change-fusion` | Fuses telemetry + tickets + standards drift into a deprecation + migration plan. | Before any v(N) → v(N+1) breaking change. |
| `/standards-alignment` | Measures conformance to OpenAPI 3.1, JSON Schema 2020-12, RFC 9457, RFC 5988, RFC 7234. | Before every internal review and before publishing externally. |

## Directory Structure

```
api-design-specification/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # 7 bespoke fusion-flavoured commands
├── context/
│   ├── concepts.md           # REST/HTTP, OpenAPI 3.1, intel-fusion analogy, source reliability rubric
│   ├── workflows.md          # Collect → weight → fuse → adjudicate → spec → trace loop
│   └── references.md         # HTTP status, OpenAPI/JSON Schema keywords, RFC index, peer-spec catalogue
├── prompts/                  # 3 reusable fusion prompt templates
└── outputs/                  # Fusion briefs, adjudications, draft specs, traceability matrices
```

## Example Use Cases

### Cutting v3 of a product API
The team wants `/v3/orders`. Instead of one engineer "scaling up" the v2 shape, run `/source-elicit` then `/fuse-requirements` to combine the v1+v2 corpus, the last 90 days of v2 telemetry, every v2-flagged support ticket, the RFC 9457 / JSON:API standards baseline, the Stripe / Shopify order-API peers, and the named stakeholders' constraints. The draft spec has a per-operation `x-provenance` block — review time is spent on real disputes, not unknowns.

### Adjudicating a long-running pagination debate
Half the surface uses `?cursor`, half uses `?page`+`?per_page`, and a senior engineer prefers `Link` headers per RFC 5988. `/contradiction-resolve` writes the explicit memo: corpus split 60/40 in favour of cursor, telemetry shows 91% of clients tolerate cursor, RFC 5988 is the standards anchor, two stakeholders prefer Link headers. Decision recorded with rationale; the next person doesn't relitigate.

### Defending an audit
A compliance auditor asks why `POST /v2/payments` returns `202` rather than `201`. `/trace-provenance payments.post.202` returns: corpus (A2) — async-handoff endpoints in this org use 202 since 2024-Q1; standards (A1) — RFC 7231 §6.3.3 permits 202 for accepted-but-not-yet-processed; tickets (C2) — three 2024 tickets confirmed clients handle 202 cleanly. Audit answered in one query.

### Planning a sunset
Telemetry says `GET /v1/users/{id}/legacy-prefs` is still called by 47 client IDs but only 6 of them are active in the last 30 days; tickets show 11 reports of misuse in the last quarter; standards say the replacement under JSON:API would be a sparse-fieldset query. `/breaking-change-fusion` produces a one-page deprecation plan with a 90-day sunset window, the 47-client outreach list pre-filtered by activity, and a migration snippet.

### Periodic spec hygiene
Run `/standards-alignment` quarterly across all `outputs/spec/` files. The remediation list catches drift the spec authors didn't notice: error envelopes that pre-date the RFC 9457 adoption, deprecated `nullable: true` instead of `type: [string, "null"]`, security scheme definitions that lost their flow.

## Recommended MCP Servers

- **Filesystem** — Read/write the fusion briefs, adjudications, and draft spec YAML in `outputs/`.
- **GitHub** — Pull the internal API corpus from neighbouring repos; open PRs for the new spec; fetch peer-spec references from Stripe / GitHub / Slack open repos.
- **HTTP / fetch** — Pull live OpenAPI documents from peer APIs (`https://api.stripe.com/openapi/spec3.json`, GitHub's `api.github.com` REST description) for the peer-source bucket.
- **A telemetry MCP if available** (Datadog, Honeycomb) — Sample real request shapes for the telemetry source. Where no MCP exists, paste exported queries into `outputs/fusion/<resource>.md`.
- **A ticketing MCP** (Linear, Jira, Zendesk) — Pull the ticket source. Same fallback applies.

## Legal & Ethical Considerations

- **Customer telemetry is sensitive.** Use aggregated request-shape statistics (counts, response codes, percentile latencies) rather than raw request bodies. Strip PII before the fusion brief; never persist raw bodies to `outputs/`.
- **Internal ticket text is sensitive.** Reference ticket IDs in the fusion brief, not the verbatim quote, unless the customer is internal.
- **Honour your organisation's data-handling policy.** Some telemetry stores have query retention; the fusion brief should cite the query, not embed snapshots that bypass retention.
- **Public peer-spec content is not always freely redistributable.** Link to upstream peer specs in `references.md`; do not copy non-trivial schema fragments into the internal repo without a licence check.

## Technical References

- [OpenAPI Specification 3.1.0](https://spec.openapis.org/oas/v3.1.0) — the authoritative spec format. Fully aligned with JSON Schema 2020-12.
- [JSON Schema 2020-12](https://json-schema.org/draft/2020-12) — the schema language OpenAPI 3.1 embeds.
- [RFC 9457 — Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html) — the canonical error-envelope format. Supersedes RFC 7807 (text aligned, IANA registry refreshed).
- [RFC 7231 — HTTP/1.1 Semantics](https://www.rfc-editor.org/rfc/rfc7231) — the source of truth for status code semantics.
- [RFC 5988 (now 8288) — Web Linking](https://www.rfc-editor.org/rfc/rfc8288.html) — pagination, navigation, and relation types via `Link` header.
- [JSON:API v1.1](https://jsonapi.org/format/) — opinionated JSON convention; useful as a peer-spec / standards anchor for resource-oriented APIs.
- [Stripe API Reference](https://stripe.com/docs/api) and [stripe/openapi GitHub](https://github.com/stripe/openapi) — canonical peer spec.
- [GitHub REST API description](https://github.com/github/rest-api-description) — second canonical peer spec.
- [NATO STANAG 2022 — Intelligence Source Reliability Ratings](https://en.wikipedia.org/wiki/Intelligence_source_and_information_reliability) — the A–F (reliability) × 1–6 (information credibility) matrix this workspace's source rating borrows.
- [JDP 2-00 / FM 2-22.3 Intelligence Fusion doctrine summaries](https://en.wikipedia.org/wiki/Intelligence_cycle) — public-domain framing for the fusion-cycle steps adapted in `context/workflows.md`.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
