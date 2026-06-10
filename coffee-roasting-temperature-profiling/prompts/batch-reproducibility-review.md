# Batch Reproducibility Review

## Purpose

Use to review a run of production batches against their golden profiles, detect drift, and decide dispositions — the daily/weekly QC pass. Pairs with `/match-profile-batch` and `/diagnose-roast-curve`.

## Prompt Template

```
You are a roast-QC agent in the coffee-roasting-temperature-profiling workspace.
Read context/concepts.md ("markers", "defects") and context/workflows.md (Workflow B) first.

Review these production batches against their golden profiles:

- **Period / shift:** [VALUE]
- **Batches:** [list: batch ID, SKU, profile version, charge & drop weight, log file/markers]
- **Golden profiles:** [reference markers/DTR/expected loss per SKU, or "in outputs/profiles/"]
- **Tolerances:** [or "use workspace defaults"]
- **Cupping/complaint notes:** [if any]

Please:
1. Score each batch against its golden (marker deltas, DTR, weight loss); classify in-tolerance / drifting / out-of-tolerance.
2. Flag any RoR-shape defects (crash/flick/stall) even where endpoints match.
3. Identify systematic drift across batches (e.g. FC consistently late → calibration suspect).
4. Recommend a disposition for each out-of-tolerance batch (release/quarantine/rework/blend-down).
5. Note any action: re-calibrate, re-dial profile, or investigate green quality.
```

## Expected Output

- A per-batch scorecard (deltas, DTR, loss, verdict, failing markers).
- A systematic-drift finding with a probable cause (machine/calibration vs profile vs green).
- Dispositions for out-of-tolerance batches and a prioritized action list.
- Updated batch-score history appended per profile for trend visibility.
