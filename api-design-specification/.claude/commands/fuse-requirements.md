# /fuse-requirements

Pull signals from every accessible source class for a target resource or operation and emit a fusion brief — the structured input every later command consumes. The single most important command in this workspace.

## Inputs

- **Resource identifier** (e.g. `orders-v3`, `payments-async`, `webhooks-shipment-events`) — the scope of the brief.
- **Source dossier** — most recent `/source-elicit` output for the surface (referenced by path).
- **Decision type** — `greenfield` (Workflow 1) | `versioned-successor` (Workflow 2) | `breaking-change` (Workflow 3, see `/breaking-change-fusion` instead).
- **Time window** for telemetry / ticket pulls — default trailing 90 days.

## Steps

1. **Direction.** State the resource and the decisions the brief will inform in one paragraph.
2. **Collection.** For each accessible source class in the dossier, pull and persist the raw signal:
   - `corpus` — list precedent operations / schemas with file refs and one-line summary of each.
   - `telemetry` — extract the request-shape table: method × path × top-10 query params × top-5 body shapes × response code distribution. Aggregate; no raw bodies.
   - `tickets` — list ticket IDs + one-line theme + reliability hint (tier, count of duplicates).
   - `standards` — cite RFC / OpenAPI section / JSON Schema keyword fragments that bear on the resource.
   - `peer-specs` — quote the corresponding operation fragment from 1–3 peers with URL.
   - `stakeholders` — quote constraints per named person with role (security, infra, PM, etc.).
3. **Processing.** Convert each source's raw signal into a structured claim list:
   `(claim, source_class, source_handle, reliability A–F, credibility 1–6)`. One claim per logical assertion.
4. **Analysis (fusion).** Per spec element (path, method, parameter, request-body field, response shape, status code, error envelope), assemble the contributing claims:
   - If sources agree → `CORROBORATED <rating>`, list the corroborating claims.
   - If sources disagree → `CONFLICT — see /contradiction-resolve <topic>`, list the conflicting claims with their ratings.
5. **Production.** Emit the fusion brief at `outputs/fusion/<resource>.md`. Follow the Phase 1–5 template in `context/workflows.md` (Direction / Collection / Processing / Analysis / Production).
6. **Conflict register.** At the bottom of the brief, list every `CONFLICT` block with a one-line topic and the suggested adjudication owner.

## Output

`outputs/fusion/<resource>.md` containing:

- Phase 1 — one-paragraph direction.
- Phase 2 — collection sections, one per source class.
- Phase 3 — flattened claim list (table).
- Phase 4 — per-element fusion table (`element | corroborated/conflict | contributing claims | rating`).
- Phase 5 — either embedded draft OpenAPI fragment with `x-provenance` (small resources) or a forward reference to the `outputs/spec/<resource>.yaml` to be produced by `/spec-draft-openapi`.

## Notes

- The brief is **the** artefact reviewers cite. If the brief is missing a source class that was in the dossier, explain why in the Phase 2 section (`access blocker: …` / `out of scope: …`).
- Default reliability is set by the dossier; override per-claim only with reason (e.g. a usually-reliable source produced an obviously-wrong single claim).
- A brief with zero `CONFLICT` blocks on a non-trivial resource is suspicious — re-check that sources were genuinely consulted, not rubber-stamped.
- For very large resources, split the brief by sub-resource and link from a parent `outputs/fusion/<resource>/index.md`.
