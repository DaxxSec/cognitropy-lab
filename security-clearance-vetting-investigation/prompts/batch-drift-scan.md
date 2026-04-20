# Batch Drift Scan

Use when the user wants to run a quarterly "book review" across the full caseload and prioritize attention.

```
Run a batch drift scan across every subject folder under outputs/subjects/.

For each subject:
- Load baseline and most recent scan.
- If no new information has surfaced since the last scan, carry all guideline scores forward.
- If the user pastes or links update data, score appropriately.
- Compute composite and trend.

Then produce a ranked report at outputs/reports/batch-YYYYMMDD.md with:

1. Top 10 by composite (descending).
2. Top 10 by positive delta since last scan (most-degraded).
3. Subjects overdue for a scan (next_scan < today).
4. Subjects stable below threshold for ≥ 3 scans (candidates to extend interval).

Sort output so the user can walk it top-down in a weekly triage meeting.
```
