# API Design Specification — Core Concepts

Background the agent reads before acting. Three interlocking frames: the HTTP / OpenAPI / JSON Schema reality the spec lives on top of, the intelligence-fusion discipline this workspace borrows from, and the integration of the two into a spec authoring practice.

## HTTP & REST Fundamentals

- **Resources vs RPC.** REST organises the surface around nouns (resources) with a small fixed verb set (GET/POST/PUT/PATCH/DELETE/HEAD/OPTIONS). RPC organises around verbs (procedures). Most production APIs are pragmatic hybrids; the spec should make the model explicit, not let it drift.
- **Idempotency.** `GET`, `HEAD`, `PUT`, `DELETE`, `OPTIONS` are idempotent by HTTP semantics; `POST` and `PATCH` are not. Idempotency-Key (RFC draft-ietf-httpapi-idempotency-key) gives `POST` and `PATCH` an opt-in idempotency contract — non-trivial when fusion shows clients retry aggressively.
- **Safe methods.** `GET`, `HEAD`, `OPTIONS` are *safe* (no state change). `TRACE` is safe but rarely useful. The rest mutate.
- **Status code families.** `1xx` informational (rare in REST APIs except `100 Continue` and the SSE `204`-adjacent patterns), `2xx` success, `3xx` redirect/cache validation, `4xx` client error, `5xx` server error. Fine-grained selection matters — `400` vs `422` is the most-debated single dispute in API specs.
- **Conditional requests.** `If-Match` / `If-None-Match` / `ETag` and `Last-Modified` / `If-Modified-Since` are the lock-and-cache primitives. Strong vs weak ETag selection drives correctness of optimistic concurrency.
- **Caching.** `Cache-Control`, `Expires`, `Vary`, `Age` per RFC 7234 / 9111. `Vary: Accept` is required if the same URL returns different media types.
- **Content negotiation.** `Accept` and `Content-Type` with media types. Avoid putting versions in URL path *and* in media type — pick one channel.

## OpenAPI 3.1 & JSON Schema 2020-12

- **OpenAPI 3.1 aligns fully with JSON Schema 2020-12.** This was the breaking change vs 3.0: `nullable: true` is replaced by `type: ["string", "null"]`. Tooling that still emits `nullable: true` is on 3.0.
- **Top-level object shape.** `openapi`, `info`, `servers`, `paths`, `components`, `security`, `tags`, `externalDocs`, `webhooks` (new in 3.1).
- **`paths` → operations.** Path templating with `{name}`. Each operation under HTTP-method keys: `get`, `post`, `put`, `patch`, `delete`, etc. Required fields per operation: `responses` (at minimum one response code). Common fields: `operationId`, `summary`, `description`, `parameters`, `requestBody`, `security`, `tags`, `deprecated`.
- **`components`.** Reusable definitions — `schemas`, `responses`, `parameters`, `examples`, `requestBodies`, `headers`, `securitySchemes`, `links`, `callbacks`, `pathItems` (new in 3.1).
- **`$ref` resolution.** JSON Reference; can point at local (`#/components/...`) or external (`./shared.yaml#/...`) targets.
- **`webhooks`.** Out-of-band events the API *sends* to clients. Same shape as `paths` operations but no path-template — keyed by event name.
- **Extensions.** Any field with `x-` prefix is vendor-specific. This workspace uses `x-provenance` for source attribution and `x-fusion-reliability` for source rating per element. Both must round-trip through any spec post-processor.

### JSON Schema 2020-12 keywords most relevant to API specs

| Keyword | Purpose |
|---------|---------|
| `type`, `enum`, `const` | Primitive type and value constraints. |
| `format` | Hint: `date-time`, `uri`, `uuid`, `email`, etc. Not enforced unless tooling opts in. |
| `properties`, `additionalProperties`, `required` | Object shape. `additionalProperties: false` to forbid drift. |
| `oneOf`, `anyOf`, `allOf`, `not` | Compositional constraints. `oneOf` is exclusive; `anyOf` is permissive. |
| `if` / `then` / `else` | Conditional sub-schemas. Use sparingly — they wreck tooling that doesn't fully support them. |
| `unevaluatedProperties` | The 2020-12 fix for `additionalProperties` interacting with `allOf` composition. |
| `discriminator` | OpenAPI's polymorphism hint. Required for some tooling to generate language-level types. |
| `$ref`, `$defs` | Reference and local definitions. |
| `pattern`, `minLength`, `maxLength`, `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`, `multipleOf` | Value constraints. |

## Error Envelopes — RFC 9457 Problem Details

Canonical error format for HTTP APIs. Supersedes RFC 7807 (text aligned, IANA registry refreshed). Required fields: `type` (URI reference to a problem type), `title` (short human-readable), `status` (HTTP status mirror), `detail` (longer human description), `instance` (URI reference to the specific occurrence). Extensions are first-class — add your own fields freely.

Media type: `application/problem+json` (or `application/problem+xml`).

A spec that hand-rolls a `{ "code": ..., "message": ... }` envelope without justifying the deviation from RFC 9457 has lost a contradiction-resolve round it never ran.

## The Intelligence Fusion Frame (Why This Cross-Domain Borrow)

Intelligence fusion is the practice of combining heterogeneous sources of evidence — HUMINT (humans), SIGINT (signals), OSINT (open source), GEOINT (geospatial), MASINT (measurement) — into a single weighted assessment with full provenance and explicit treatment of contradictory reports. The transferable elements for API design:

- **Source classes are heterogeneous and finite.** Six classes work for APIs: internal corpus, telemetry, tickets, standards, peer specs, named stakeholders. Each has characteristic strengths and biases.
- **Reliability rating decouples *who said it* from *how confident we are*.** A senior engineer's stylistic preference is HUMINT with a personal-bias adjustment, not a standard. Stating the reliability explicitly stops authority arguments.
- **Information credibility decouples *how confident we are in the source* from *how confident we are in the specific claim*.** A perfectly reliable telemetry source can deliver a sample-size-of-three claim that is low credibility.
- **Provenance is non-optional.** Every assessment links back to the sources that fed it. The spec analogue: `x-provenance` on every operation, schema, and response.
- **Contradictions are surfaced, not laundered.** When sources disagree, the analyst writes the adjudication. The spec analogue: `/contradiction-resolve` and the adjudication memo.

### NATO STANAG 2022 Source × Information Rating

Reliability of source (A–F) crossed with credibility of the specific information (1–6). The workspace uses both axes.

| Reliability | Meaning |
|---|---|
| A | Completely reliable |
| B | Usually reliable |
| C | Fairly reliable |
| D | Not usually reliable |
| E | Unreliable |
| F | Reliability cannot be judged |

| Credibility | Meaning |
|---|---|
| 1 | Confirmed by other sources |
| 2 | Probably true |
| 3 | Possibly true |
| 4 | Doubtful |
| 5 | Improbable |
| 6 | Truth cannot be judged |

### Mapping table — fusion → API design

| Intelligence concept | API design analogue |
|----------------------|---------------------|
| Source class (HUMINT, SIGINT, etc.) | corpus / telemetry / tickets / standards / peer-specs / stakeholders |
| Reliability rating (A–F) | per-source rating set at `/source-elicit` time and refreshed quarterly |
| Information credibility (1–6) | per-claim rating set at `/fuse-requirements` time |
| Source corroboration | multiple sources agreeing on an operation shape → A1/B1 confidence |
| Contradictory reporting | conflicting source signals → `/contradiction-resolve` |
| Intelligence product | the OpenAPI document with `x-provenance` |
| Analyst's footnote / source chain | `/trace-provenance` output |
| Indications & warnings | `/breaking-change-fusion` reading the leading indicators |
| Source compromise / poisoning | a stakeholder gaming the process by writing tickets to manufacture a "ticket source"; flag in adjudication |

## Default Source Ordering (Sane Tie-Break)

When sources conflict and no override applies, resolve in this order:

1. **Standards (RFC, OpenAPI, JSON Schema, JSON:API)** — authoritative; deviating requires written rationale.
2. **Peer specs (Stripe, GitHub, Twilio, Slack)** — strong precedent in the industry; deviating requires reason but not always rationale.
3. **Internal corpus** — house style; consistency across the surface usually outweighs a single new opinion.
4. **Telemetry** — what clients actually do; powerful for breaking-change decisions, less authoritative for greenfield.
5. **Tickets** — pain signal; high signal for "what confuses people", low signal for "what should the design be".
6. **Stakeholder opinion** — important for constraints (security, infra) but only authoritative within their lane.

This is the *default*. Document overrides — a tier-1 customer's ticket can outweigh a corpus convention; security's veto outweighs a peer-spec convention.

## Common Failure Modes

- **Silent contradiction resolution.** Two sources disagree; the author quietly picks one. The decision is unrecoverable later. `/contradiction-resolve` exists to prevent this.
- **Authority-driven design.** "Because Senior X said so." No reliability rating; no traceability; the next senior overrules and the spec churns.
- **Telemetry blindness.** Drafting the v(N+1) shape without checking what v(N) clients actually do. Result: a "cleaner" API that breaks 40% of the live traffic in unforeseen ways.
- **Standards drift.** Hand-rolled error envelopes, custom pagination grammars, `nullable: true` (3.0 vestige) — all because nobody ran `/standards-alignment` in the last 18 months.
- **Provenance stripping.** A spec post-processor or doc generator drops `x-*` extensions. The traceability matrix evaporates. Pin tooling that preserves extensions.
- **Source poisoning.** A stakeholder files tickets to manufacture a "ticket source" supporting their preferred design. Catch in adjudication: novelty-vs-recurrence test on the ticket source.
- **Discriminator-less polymorphism.** `oneOf` without `discriminator` — language-level codegen produces unusable union types.
- **422-vs-400 by vibe.** No documented decision rule. Inconsistent across the surface. Standards say either is legal; the corpus rule should be explicit.

## Operating Constraints

- **PII in telemetry / tickets.** Use aggregates and IDs; never persist raw bodies or verbatim customer quotes to `outputs/` unless the customer is internal and consented.
- **Peer-spec licensing.** Linking is fine; copying non-trivial schema fragments from a copyrighted peer spec into the internal repo is not. Cite, don't paste.
- **Spec stability.** OpenAPI documents are contracts. Edits land via the same review path as code changes; provenance annotations are part of the diff.
- **Webhook callbacks vs server-sent events vs WebSockets.** All three exist; the spec should declare the channel explicitly. Webhooks under `webhooks` (3.1 native); SSE / WebSocket under `paths` with the appropriate media type or upgrade contract.
