# /intake-subject

Create a pseudonymized baseline profile for a single subject. The baseline anchors every future drift scan.

## Inputs
Interactive; user can paste a redacted summary instead of answering Q&A.

## Steps
1. Assign the next `SUBJ-NNNN` ID (check `outputs/subjects/` for last used).
2. Capture:
   - Clearance level and eligibility date (year only).
   - Investigation tier.
   - Position sensitivity / mission criticality (1-5).
   - Access program categories (no program names).
   - Prior adverse issue categories by SEAD 4 guideline letter.
   - Any mitigation already on record.
3. Create `outputs/subjects/SUBJ-NNNN/` with:
   - `baseline.md` — YAML front-matter + narrative.
   - `scans/scan-index.json` — empty list `[]`.
   - `notes/` — empty directory (`.gitkeep`).
4. Schedule the first drift scan and propose a date (default: now + 30 days, or sooner if baseline already shows a guideline ≥ 3).
5. Log to `work-log/YYYY-MM-DD.md`.

## Output format
```yaml
---
id: SUBJ-NNNN
created: YYYY-MM-DD
clearance_level: TS|S|Public Trust|...
tier: T3R|T5R|...
eligibility_year: YYYY
mission_criticality: 1-5
access_categories: [compartment-categoryA, compartment-categoryB]
prior_issues: [F, G]
next_scan: YYYY-MM-DD
---
```
