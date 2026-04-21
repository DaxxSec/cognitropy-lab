---
name: tolerance-analysis
description: Monte Carlo tolerancing and sensitivity ranking for the current prescription.
---

# /tolerance-analysis

## Prereqs
- Converged prescription in `outputs/prescription-v{latest}.csv`
- FMEA pass completed (`/run-fmea`)

## Steps
1. **Define tolerance set**: confirm with user which tier (commercial / precision / high-precision) from `context/for-agent/domain-knowledge.md` §6. Allow per-element overrides.
2. **Sensitivity pass (one-at-a-time)**: perturb each parameter by ±tol, record ΔMTF@Nyquist or ΔRMS-WFE. Rank hottest parameters.
3. **Monte Carlo**: 1000+ trials with all tolerances active simultaneously. Histogram MTF, compute p50, p90, p95, p99.
4. **Yield calc**: against the user's MTF spec, what is the predicted yield?
5. **Feedback**: update Occurrence scores in the FMEA for any mode tied to a hot tolerance.
6. **Recommend**: which tolerances to tighten, which to relax. Cost hint from `resources/glass-costs.md`.

## Outputs
- `outputs/tolerance-sensitivity.csv` — one-at-a-time ranking
- `outputs/tolerance-mc.csv` — Monte Carlo trial results
- `user-docs/tolerance-report.md` — narrative with plots (or plot-generation Python)

## Tool Pathways
- If Zemax is available: use Zemax Tolerancing, export CSV, post-process in Python.
- Python-only: scaffold provided in `resources/mc-tolerance-template.py`.
