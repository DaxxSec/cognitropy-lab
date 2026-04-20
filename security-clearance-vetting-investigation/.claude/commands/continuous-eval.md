# /continuous-eval

Triage a single continuous evaluation (CE) alert end-to-end.

## Inputs
- Subject ID (or create one with `/intake-subject` first).
- Alert source category (Criminal, Financial, Terrorism/Foreign, Public Records, Self-Report, Employer).
- Alert summary (redacted).
- Severity (low / moderate / high) per `resources/continuous-vetting-triggers.md`.

## Steps
1. Assign `CE-YYYYMMDD-NN` alert ID.
2. Map to SEAD 4 guideline(s). Note: a single alert can touch multiple guidelines (e.g., arrest for DUI touches G and J).
3. Recommend an initial inquiry:
   - Records to request (public record, agency-held, FBI rap sheet).
   - Interview questions to prepare for the subject.
   - Collateral interviews if applicable.
   - Timeline under agency policy.
4. Propose a disposition:
   - No action / closed favorable.
   - Documented inquiry (close in file, no further action).
   - Expanded inquiry.
   - Out-of-cycle investigation.
   - Refer to adjudicator.
5. Link the alert into the subject's folder:
   - `outputs/ce-alerts/CE-YYYYMMDD-NN.md` — the alert record.
   - Cross-link from `outputs/subjects/<id>/alerts.md`.
6. If the alert raises the scan trend or changes composite, update the subject folder and trigger a `/drift-scan`.
7. Log action.

## Output format
```markdown
---
alert_id: CE-YYYYMMDD-NN
subject: SUBJ-NNNN
guideline: [F, J]
severity: high
recommended_disposition: expanded-inquiry
---
# Alert
(redacted summary)

# Analysis
(guideline mapping, inquiry plan, disposition reasoning)
```
