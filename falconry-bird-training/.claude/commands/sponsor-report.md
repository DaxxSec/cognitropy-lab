# /sponsor-report

Generate a structured apprentice → sponsor progress report from the training log, on the agreed cadence.

## Inputs

- Reporting period (e.g. last month / quarter).
- The weight & training log in `outputs/` (from `/weight-log`).
- Milestones reached, equipment changes, and any open questions for the sponsor.

## Steps

1. Run `/weight-log` for the period to summarize weight band, response trend, flights, and feedings.
2. Pull milestones from the training plan: first creance flight, first free flight, first slip on quarry, first kill.
3. Note equipment or husbandry changes (new jesses, telemetry added, mews adjustment, diet change).
4. List concerns and **explicit questions** for the sponsor — the report is also a request for guidance.
5. Format with `prompts/sponsor-quarterly-update.md` and archive the sent copy.

## Output

`outputs/sponsor-report-YYYY-MM-DD.md`: period summary (weight band, response, flights/hunts), milestones reached this period, equipment/husbandry changes, concerns, and a numbered list of questions for the sponsor.

## Notes

- If progress stalled through the gates, make that the headline and request a field session.
- Escalate any welfare concern immediately — don't hold it for the next scheduled report.
