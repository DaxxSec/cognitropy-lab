# Workflows — End-to-End Operating Sequences

The agent runs three primary workflows: **daily ingest cycle**, **release-day cycle**, and **research/horserace cycle**. Each maps a chain of slash commands into a deterministic sequence with custody at every step.

## Workflow 1 — Daily / Mid-Cycle Ingest

**Trigger:** any day with potential new data (typical macro indicator releases happen most weekdays).

```
1. Confirm clean git tree.
2. /ingest-vintage --source fred-alfred --series PAYEMS,UNRATE,INDPRO,RRSFS,...
3. /ingest-vintage --source bea-nipa --series GDPC1,PCECC96,GPDIC1,...
   (idempotent — most days will be no-ops for the slow series)
4. If any new monthly indicator landed: /build-nowcast --target-quarter <Qx>
5. Append a work-log entry summarising new data, nowcast change, anomalies.
```

**Decision tree on indicator surprise:**
- |surprise| < 0.5σ → routine, no escalation.
- 0.5σ ≤ |surprise| < 2σ → annotate in work-log; re-run nowcast; flag if direction inconsistent with prior.
- |surprise| ≥ 2σ → annotate; re-run nowcast; open a `planning/` ticket if the model's bands fail to cover the realised value.

## Workflow 2 — GDP Release Day

**Trigger:** BEA / Eurostat / national stats office releases a new GDP estimate.

```
1. Confirm clean git tree.
2. /ingest-vintage --source bea-nipa --series GDPC1,GDPNOW (and component series)
   → seals today's vintage, computes diff against yesterday's vintage.
3. /audit-revision --series GDPC1 --new-vintage today --prior-vintage <yesterday>
   → produces the revision decomposition document.
4. If a model artifact is referenced in audit:
     /estimate-model --class same --refit  (only if audit recommends refit)
5. Update planning/plan.md with any model-review actions.
6. /compare-forecasts  (refresh metrics with the new realised vintage)
7. Append a release-day section to work-log/<YYYY-MM-DD>.md:
   - headline number, change vs nowcast, change vs prior vintage,
   - decomposition takeaway (data revision / model drift / innovation),
   - publication next steps (if any).
```

## Workflow 3 — Research / Horserace Cycle

**Trigger:** quarterly model review, or whenever a new candidate model class is evaluated.

```
1. Define candidate variants in planning/plan.md (model class, hyperparameters, training window).
2. For each candidate:
     /estimate-model --class <class> --hyperparams <...>
3. /compare-forecasts --sets [list of candidate manifest paths]
4. Read the comparison REPORT.md.
5. Decide:
     a. Promote a new model to "headline" — update context/project.md and README.
     b. Keep candidates in parallel — annotate planning/plan.md with the parallel set.
     c. Retire a candidate — record retirement reason in planning/.
6. Update work-log with the decision and the comparison artifact reference.
```

## Cross-Cutting Discipline

### Pre-flight (every run, every workflow)
- Working tree clean (`git status --porcelain` empty).
- Latest vintages sealed for all referenced series.
- `outputs/manifests/INDEX.json` schema valid.

### Post-flight (every run)
- New manifest entry written.
- Hash-verify any artifact the run produced.
- Append to `work-log/<YYYY-MM-DD>.md` with a one-line summary and the artifact paths.
- If the run produced a forecast artifact intended for publication, do **not** publish inline — call `/release-forecast` as a separate step.

### Diagnostic Decision Tree — Backtest RMSFE Suddenly Worsens

```
Has the validation panel changed (added/dropped series)? ──► yes ─► roll back panel; refit with prior panel; compare.
       │
       no
       ▼
Has a benchmark revision occurred in the last quarter? ──► yes ─► run /audit-revision; expect increased innovation;
       │                                                       refit on new vintage; expect partial recovery.
       no
       ▼
Has a structural break appeared in the indicator panel? ──► yes ─► add regime dummy; document in planning/.
       │                                                       refit; reassess.
       no
       ▼
Has a hyperparameter changed? ──► yes ─► roll back hyperparameters; A/B against new.
       │
       no
       ▼
Has the code changed? ──► yes ─► diff against prior commit; identify offending change; revert or roll forward.
       │
       no
       ▼
Open a planning/ ticket — likely an upstream library change (numpy/statsmodels). pin versions and rerun.
```

### Custody Recovery Procedure (if a manifest hash mismatch is detected)

1. Stop. Do not publish anything that depends on the offending artifact.
2. Compare the artifact bytes against the recorded hash.
3. If artifact is corrupt: restore from git (if tracked) or from offsite backup (if external evidence). Re-hash; reseal.
4. If artifact is fine but hash entry is wrong: open `planning/integrity-incident-<date>.md`, record the discrepancy, append a corrected entry to `INDEX.json` (without overwriting the original — append a `kind: "correction"` entry referencing the original).
5. Notify any downstream releases that depended on the offending artifact; consider issuing a republished release with corrected manifest.

This procedure exists because the discipline only works if integrity events are loud and traceable. Silent fixes destroy the audit trail.
