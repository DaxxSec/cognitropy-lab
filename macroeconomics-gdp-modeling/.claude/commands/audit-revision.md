# /audit-revision — Decompose a Revised Print Against the Prior Vintage

Reconcile a newly released GDP print against the most recent prior vintage and decompose the delta into (a) data revision, (b) model drift, (c) genuine forecast innovation. Use within 24 hours of any official release that revises history.

## Required Inputs

- Target series (e.g. `GDPC1`).
- New vintage date — typically the day of release.
- Prior vintage to compare against — defaults to the last sealed vintage before today.
- Optional: model artifact reference for the model whose forecast is being audited.

## Steps

### 1. Confirm both vintages are sealed
The new vintage must already have been ingested via `/ingest-vintage`. The prior vintage must exist in the parquet store. If either is missing, abort and surface the gap.

### 2. Compute the data-revision component
Load both vintages. For every overlapping `(observation_date, value)` pair, compute the level revision and percent revision. Aggregate at:
- Quarter level (most relevant for GDP).
- Component level if the user audits sub-aggregates (C, I, G, NX).
- Annual benchmark revisions if the new vintage spans a benchmark year.

Output a `revision_table` with: observation date, prior value, new value, level delta, percent delta.

### 3. Compute the model-drift component
If a model artifact is supplied:
- Refit the same model class on the new vintage (same hyperparameters, same training window logic).
- Record the new fitted forecast for the same target horizons.
- Drift = new fitted forecast − prior fitted forecast (on identical horizons, holding model class fixed).

### 4. Isolate the innovation
Innovation = realised print − (prior fitted forecast + data revision component + model drift component). This is the genuine surprise.

### 5. Build the post-mortem
Write `outputs/forecasts/revision_audit__<targetQ>__v<YYYY-MM-DD>.md` containing:
- Headline numbers (prior print, new print, level delta, percent delta).
- Decomposition table: data revision / model drift / innovation.
- Component contributions (which sub-aggregates moved most).
- Narrative: short paragraph explaining the largest contributor and any anomalies (large signed revisions to inventories, services, healthcare imputations).
- Recommendation: refit model? recalibrate? leave alone?

### 6. Update the custody manifest
Append a `kind: "revision_audit"` entry referencing the prior vintage, new vintage, model artifact (if any), and audit document.

### 7. Update the work-log
Add a `work-log/<YYYY-MM-DD>.md` block summarising the audit and any next-step decisions (e.g. trigger `/estimate-model` for a refit).

## Output

A markdown post-mortem under `outputs/forecasts/`, a custody manifest entry, and a work-log block. The audit document is the primary deliverable to stakeholders who care about why the published forecast differed from the print.

## Heuristics

- **Large data revision, small innovation:** the source revised the past; the model would have been right on the prior vintage. Do **not** refit aggressively; document and continue.
- **Small data revision, large innovation:** the model missed something. Investigate omitted variables, structural break, or regime change. Open a `planning/` ticket.
- **Both large and offsetting:** common during benchmark revisions. Annotate; do not over-interpret a single quarter.
- **Persistent same-sign innovations across 4+ quarters:** model bias. Refit with updated training window or revise specification.
