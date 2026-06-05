# /incident-report

Produce an injury, mortality, or escape report for the regulating authority and the sponsor, within the reporting window.

## Inputs

- Incident type: injury, illness death, escape/loss, recovery, theft.
- Bird identity: species, source, **band/marker number**, permit number.
- Date/time, circumstances, and actions taken (telemetry search, vet, etc.).

## Steps

1. Classify the incident and check the applicable **reporting window** in `context/references.md` (mortality/loss are typically reportable; 3-186A events commonly within 10 days).
2. Reconstruct the timeline factually: what happened, when, where, weather, and what was done.
3. For a loss/escape: record telemetry use, search actions, and outcome (recovered/unrecovered).
4. For a mortality: note suspected cause, whether a vet/necropsy was involved, and band disposition.
5. Draft the notice to the **state coordinator/USFWS** and a parallel note to the **sponsor**.
6. Add the event to the acquisition/disposition register and file any required form.

## Output

`outputs/incident-report-YYYY-MM-DD.md`: incident classification, bird identity + band number, factual timeline, actions taken, outcome, the reporting deadline, and the drafted notices to authority and sponsor.

## Notes

- File within the window even if details are still developing — supplement later.
- Telemetry on every free flight is the difference between a recoverable loss and a permanent one.
- This structures the report; the state's form/portal is authoritative for required fields.
