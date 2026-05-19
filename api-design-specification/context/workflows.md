# API Design Specification — Workflows and Methodology

Step-by-step procedures and decision trees the agent uses when running tasks in this domain. Tied to today's `technique` — **multi-source intelligence fusion** — which structures every workflow below as a collect → weight → fuse → adjudicate → spec → trace loop.

## The Fusion Cycle (Backbone of Every Workflow)

Adapted from the classic intelligence cycle (direction → collection → processing → analysis → dissemination → feedback). For API specs:

1. **Direction.** What surface, what change, what decision is being asked? Anchor with a one-line problem statement.
2. **Collection.** Pull from each of the six source classes you have access to (set by `/source-elicit`). One section per source in the fusion brief.
3. **Processing.** Normalise each source's signal: telemetry → aggregated request-shape table; tickets → categorised pain themes; corpus → matched precedent excerpts; standards → cited paragraph reference; peer specs → URL + operation fragment; stakeholder → quoted constraint + speaker.
4. **Analysis (fusion).** Weight by reliability (A–F) and credibility (1–6). Identify corroboration (multiple sources agree → high confidence). Identify conflict (`CONFLICT` block in the brief).
5. **Production.** Emit the spec element (or adjudication memo, or breaking-change plan).
6. **Dissemination & feedback.** PR the spec; capture review feedback as a new ticket-source entry; re-run the affected workflow on the next change.

## Workflow 1: New Resource — Greenfield Operation

**Goal:** Draft a new operation (`POST /widgets`, `GET /widgets/{id}`, etc.) with full provenance.

### Steps

1. **`/source-elicit`** if not already done for this surface — confirm which source classes you have, with rating.
2. **`/fuse-requirements <resource>`** — runs the fusion cycle for the resource and emits `outputs/fusion/<resource>.md`.
3. **Conflict pass:** if the fusion brief has any `CONFLICT` blocks, run **`/contradiction-resolve`** until each conflict has an adjudication memo and a chosen resolution.
4. **`/spec-draft-openapi <resource>`** — converts the resolved fusion brief into `outputs/spec/<resource>.yaml` with `x-provenance` and `x-fusion-reliability` retained.
5. **`/standards-alignment`** on the drafted file — catch unconscious drift before the team sees it.
6. **Internal review** — paste the spec + the fusion brief + the adjudication memos into the review request. Reviewers cite source disagreements, not stylistic preferences.
7. **Land** the spec. Capture the PR comments as a new ticket-source entry (`outputs/sources/tickets/internal-review-<date>.md`) so the next iteration has them.

### Decision Points

- If `/source-elicit` shows fewer than three accessible source classes: pause; greenfield design with only two sources (e.g. just stakeholders + standards) is high risk. Escalate to acquire telemetry / corpus access first.
- If the corpus has no precedent for the resource pattern: standards and peer specs become the dominant sources; record this in the brief.
- If a conflict is between security-stakeholder and any other source: security has lane veto; resolve in security's favour and explicitly document the trade-off lost.

## Workflow 2: Versioned Successor — `v(N+1)` of an Existing Resource

**Goal:** Design the next version of an existing resource without breaking existing telemetry-validated assumptions.

### Steps

1. **Telemetry pull.** Sample 30–90 days of v(N) requests. Tabulate: request method × path × top-10 query params × top-5 request body shapes × response code distribution. This becomes the telemetry source for the fusion brief.
2. **Ticket pull.** Filter the ticket system for v(N)-tagged items in the same window. Categorise: contract confusion / missing field / pagination pain / error envelope confusion / auth.
3. **`/fuse-requirements <resource>-v(N+1)`** — same fusion brief shape as Workflow 1, but with telemetry and tickets pre-weighted because they describe a real existing system.
4. **Conflict pass:** `/contradiction-resolve` for any telemetry-vs-standards or telemetry-vs-stakeholder conflicts (these are the most common; e.g. telemetry shows 40% of clients still send the deprecated field, but standards / stakeholder want it gone).
5. **`/spec-draft-openapi`** + **`/standards-alignment`** as in Workflow 1.
6. **Backward-compatibility analysis.** For each v(N) field absent from v(N+1), record the migration approach in the spec's `x-migration` extension.

### Decision Points

- If telemetry is sparse for v(N) (low traffic): downweight the telemetry source to D-rating; corpus and standards lead.
- If tickets are dominated by one or two angry customers: flag source-poisoning risk in adjudication.

## Workflow 3: Breaking Change / Sunset

**Goal:** Decide whether and how to deprecate or break an existing operation. Bound to `/breaking-change-fusion`.

### Steps

1. **`/breaking-change-fusion <operation>`** — runs the fusion brief but only for the four sources that drive a breaking-change decision: telemetry (who is calling), tickets (who is hurting), standards (does the replacement align), corpus (is the replacement consistent with the rest of the surface).
2. **Impact table.** Output is a per-client impact table: client_id × call_count_30d × last_call_at × estimated_migration_cost (S/M/L heuristic from request-shape complexity).
3. **Deprecation plan.** Sunset window (default 90 days; 180 if telemetry shows long-tail with >100 client IDs still active). `Deprecation` and `Sunset` HTTP headers per RFC 8594 + draft-ietf-httpapi-deprecation-header.
4. **Outreach list.** Top-N clients by call volume; carve out the inactive long tail; segment by tier (enterprise vs SMB vs unknown).
5. **Migration snippet.** Side-by-side request/response showing the v(N) → v(N+1) translation for the dominant request shape.

### Decision Points

- If <5 clients touch the operation in the trailing 30 days: short sunset (≤30 days) is justified; document in plan.
- If a tier-1 customer is in the impact list: sunset cannot land without account-team alignment; flag and pause.
- If the replacement is *not* aligned with current standards (e.g. RFC 9457): do not deprecate; re-design first.

## Workflow 4: Audit / Provenance Query

**Goal:** Answer "why does the spec say X?" — defensibly, in one query.

### Steps

1. **`/trace-provenance <jsonpath-into-spec>`** — e.g. `paths./v3/orders.post.responses.422`.
2. The command walks the `x-provenance` chain on the operation, response, schema as needed; emits a markdown report citing each source class, its rating, and the specific claim that contributed.
3. If the chain is incomplete (e.g. `x-provenance` was stripped by a doc generator): flag the gap; this is a tooling failure to fix at the pipeline level.

### Decision Points

- If the question is "why this status code" — most answers live on the response, not the operation. Walk both.
- If the question is "why this field shape" — most answers live on the schema. Walk the schema's `x-provenance`.
- If no provenance exists: this is a *legacy* element pre-dating fusion; mark for re-fusion in the next refactor pass.

## Workflow 5: Quarterly Spec Hygiene

**Goal:** Drift catch across the whole surface.

### Steps

1. **`/standards-alignment`** across all `outputs/spec/*.yaml` — output a remediation list per file.
2. **Refresh source ratings.** `/source-elicit` per surface — telemetry pipeline upgrades, ticket system migrations, corpus shifts since last quarter all change ratings.
3. **Provenance integrity sweep.** For a 10% sample of operations, run `/trace-provenance` and confirm the chain still parses. Catch tooling that silently strips `x-*`.
4. **Top-10 unresolved conflicts.** Scan `outputs/adjudication/` for memos marked `OPEN`; promote into the next sprint.

### Decision Points

- If a peer spec released a major version in the quarter (e.g. Stripe's annual revision): re-fuse any operations citing it.
- If a standard was superseded (e.g. RFC 7807 → RFC 9457): grep `outputs/spec/` for references to the older RFC; re-fuse affected operations.

## Methodology Phases (Single-Resource Fusion Brief)

The `/fuse-requirements` output is structured in five phases for a single resource. Use this as the brief template.

### Phase 1 — Direction

Single-line problem statement + scope (which methods, which surface).

### Phase 2 — Collection

One section per source class you have access to. For each: what was pulled, when, and the raw signal (request-shape table for telemetry, ticket IDs + summaries for tickets, file paths + line refs for corpus, RFC + section for standards, URL + operation for peers, name + quote for stakeholders).

### Phase 3 — Processing

Normalise each source's signal into a structured claim list: `(claim, source, reliability, credibility)`.

### Phase 4 — Analysis (Fusion)

Per spec element (path, method, parameter, request body field, response shape, error envelope), list the contributing claims with their ratings. Mark agreement (`CORROBORATED A1/A2/B1/B2`) or conflict (`CONFLICT — see /contradiction-resolve memo X`).

### Phase 5 — Production

Reference to the drafted operation. If the operation is drafted in the same pass, embed the YAML directly with `x-provenance` already populated.
