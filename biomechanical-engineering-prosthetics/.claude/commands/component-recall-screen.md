# /component-recall-screen

Screen the practice's patient cohort against component recall notices (FDA MAUDE field-action, manufacturer safety bulletins, EU MDR FSCA) — generate a prioritised action list with regulatory-reporting checkpoints.

## Inputs

- **Recall / field-action notice** — source (FDA MAUDE, manufacturer bulletin, EU MDR Field Safety Corrective Action), affected manufacturer + model + lot range + serial range + dates of distribution. Class of recall (I = serious health risk / death likely, II = temporary or reversible harm, III = unlikely to cause harm).
- **Practice's component inventory** — patient-component mapping: `patient_id, encounter_date, manufacturer, model, lot/serial, fitting_status (active/replaced/lost)`. Should be queried from practice management system / inventory database.
- **Patient activity status** — currently active patients (will need outreach) vs. inactive/lost-to-follow-up (documentation only, often).
- **Reporting jurisdiction** — US (FDA 21 CFR 806), EU (MDR Article 87), UK (MHRA), other.

## Steps

1. Read `context/references.md` "Regulatory framework" + "FDA MAUDE database" for the relevant CFR/MDR references.
2. Filter practice inventory against the recall criteria (manufacturer + model + lot/serial intersection). Generate the affected-patient list.
3. Stratify by criticality:
   - **Class I + active patient** → immediate (24-72h) outreach + remove-from-service + emergency refit/replacement
   - **Class I + inactive patient** → documented good-faith outreach attempt (certified mail, registered phone log)
   - **Class II + active patient** → outreach within 30 days, schedule at next routine visit ASAP
   - **Class II + inactive patient** → documented outreach attempt
   - **Class III + any** → next routine visit + documentation
4. Generate per-patient action records with: patient ID, contact method + status, component status (in-use / removed / replaced), date of action, signing clinician. These become the audit trail.
5. Generate the practice-level compliance memo: total affected patients, action status distribution, projected completion date, regulatory reporting checklist (FDA Form 3500A submission if applicable, FSCA Coordinator notification, etc.).
6. Write outputs to `outputs/recalls/<recall-id>/<YYYY-MM-DD>-screen.md` (compliance memo) + `outputs/recalls/<recall-id>/<YYYY-MM-DD>-patient-actions.csv` (per-patient action ledger).
7. Schedule follow-up review — typically 14 days after initial outreach for Class I, 30 days for Class II.

## Output

- **Markdown compliance memo** — recall summary, affected patients count + breakdown, action-status distribution, regulatory reporting checklist, signing clinician, projected closure date.
- **CSV per-patient action ledger** — `patient_id, status, contact_method, contact_date, response, component_disposition, refit_appointment, signing_clinician, notes`. Audit-ready.

## Decision points

- **If a Class I recall affects >5% of the practice's active cohort** → escalate to practice leadership immediately; this is a programme-level emergency, not a per-patient action item.
- **If patient inventory data is incomplete (missing lot/serial for some encounters)** → those patients can't be definitively cleared or flagged; treat as "potentially affected" and prioritise inventory data-quality remediation.
- **If the recalled component is end-of-life and the manufacturer is no longer supplying replacements** → coordinate with the manufacturer's transition plan; document any patient who can't be refit with like-component and the alternative selected.

## Notes

- FDA 21 CFR 806 requires medical device user facilities to report device-related deaths within 10 days and serious injuries within 10 days; recall participation doesn't replace this duty.
- EU MDR Article 87 (Vigilance) has 2-day to 15-day reporting windows depending on severity.
- Document EVERY outreach attempt, including no-answers — gives the practice defensible standing if a patient later experiences harm from a known-recalled component.
- Some recalls are voluntary "field corrections" rather than removals (e.g., software update to a microprocessor knee). Those are still regulatory-reportable and require patient consent for the correction.
- Manufacturer field actions sometimes precede formal FDA recall notices by weeks — subscribe to manufacturer safety bulletins directly, don't wait for MAUDE.
