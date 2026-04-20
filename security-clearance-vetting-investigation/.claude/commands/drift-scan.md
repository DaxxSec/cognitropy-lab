# /drift-scan

Run a point-in-time risk reading for a subject — the condition-monitoring sensor read in the predictive-maintenance analogy.

## Inputs
- `SUBJ-ID` (required).
- Optional: freeform update from the user on any guideline.

## Steps
1. Load `outputs/subjects/<id>/baseline.md` and the last N scans (`scans/scan-*.md`).
2. For each of the 13 SEAD 4 guidelines (A-M):
   - Ask if the user has any new information.
   - If yes → score 0-5 per `resources/risk-scoring-rubric.md` and capture evidence.
   - If no → carry forward prior score and mark as "carried."
3. Compute a **weighted composite** = Σ (guideline_score × guideline_weight) / Σ weights.
4. Compare to prior composite:
   - Trend: `improving` if delta ≤ -0.3; `stable` if |delta| < 0.3; `degrading` if delta ≥ 0.3.
5. Apply `resources/action-decision-tree.md` to pick a recommendation:
   - Extend interval.
   - Scheduled re-scan.
   - Focused inquiry.
   - Out-of-cycle investigation.
   - Referral to adjudicator.
6. Write `outputs/subjects/<id>/scans/scan-YYYYMMDD.md`.
7. Append summary to `scans/scan-index.json`.
8. Log action in `work-log/YYYY-MM-DD.md`.

## Output artifact sketch
```markdown
---
scan_id: SUBJ-NNNN-YYYYMMDD
composite: 2.3
trend: stable
recommended_action: scheduled-rescan
next_scan: YYYY-MM-DD
---
# Scan summary
(guideline-by-guideline scores and evidence)
```
