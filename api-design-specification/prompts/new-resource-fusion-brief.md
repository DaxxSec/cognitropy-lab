# new-resource-fusion-brief

## Purpose

Kick off `/fuse-requirements` for a new resource on a known surface. Pre-fills the direction and source-class slots from the dossier so the brief comes back actionable in one round-trip.

## Prompt Template

```
I'm starting a fusion brief for a new resource on the [SURFACE_IDENTIFIER] surface.

- **Resource:** [RESOURCE_NAME, e.g. orders-v3, payment-disputes, webhook-shipment-events]
- **Scope of operations:** [LIST_METHODS_AND_PATHS, e.g. POST /v3/orders, GET /v3/orders/{id}, GET /v3/orders]
- **Decision type:** greenfield
- **Source dossier:** [PATH_TO_LATEST_DOSSIER, e.g. outputs/sources/payments-api-2026-05-01.md]
- **Time window for telemetry/tickets:** [WINDOW, default 90 days]
- **Constraints / non-negotiables from stakeholders:** [LIST_IF_KNOWN, e.g. "security: must use oauth2 client_credentials only"]

Please:
1. Run the Phase 1–5 fusion cycle from `context/workflows.md`, writing the brief at `outputs/fusion/[RESOURCE_NAME].md`.
2. For each operation in scope, populate the Phase 4 fusion table with at least the corpus, standards, and stakeholder sources; pull telemetry and tickets per the dossier's access path.
3. List every CONFLICT block with a suggested adjudication owner.
4. If a source class in the dossier was inaccessible during this run, explain why in the Phase 2 section rather than silently dropping it.
```

## Expected Output

- A new `outputs/fusion/[RESOURCE_NAME].md` matching the Phase 1–5 template.
- A conflict register at the bottom of the brief, ready for `/contradiction-resolve`.
- A list of source classes consulted vs. dossier-listed, with reasons for any gaps.
- A forward reference to the future `outputs/spec/[RESOURCE_NAME].yaml` that `/spec-draft-openapi` will produce.
