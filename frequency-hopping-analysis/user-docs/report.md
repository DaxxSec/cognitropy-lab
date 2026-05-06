# Cumulative Engagement Report Index

`/report-findings` appends one line here per engagement. Use this as a top-level index across analyses; the per-engagement detailed reports live in `outputs/<engagement>/report.md`.

| Date | Engagement | System | Calibration | Headline finding | Report |
|------|------------|--------|-------------|------------------|--------|
|      |            |        |             |                  |        |

## How entries are added

When `/report-findings` runs, it appends a row with:
- The engagement date
- The engagement name (from `context/project.md`)
- The target system (e.g. "Bluetooth Classic", "Honeywell wireless fire panel")
- Calibration status (PASS / DOWNGRADED / FAIL)
- A one-sentence headline finding
- A relative path to the detailed report

## Manual maintenance

If a report supersedes an earlier one (re-analysis with better data), don't delete the old row — strike it through and add a new row pointing to the updated report. The audit trail matters for any work that gets cited later.
