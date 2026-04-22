# Domain Knowledge — Palliative Care Symptom Assessment

## Palliative care, in one paragraph
Palliative care is specialized medical care focused on relief of suffering and improvement of quality of life for people with serious illness. It is appropriate at any age and any stage of illness, and can be provided alongside curative treatment. Hospice is a subset of palliative care for patients in the final phase of a terminal illness (in the US, typically defined as a prognosis of 6 months or less if the illness runs its expected course) who have chosen comfort-focused care. Care is interdisciplinary: physicians, APRNs, RNs, social workers, chaplains, home health aides, volunteers, pharmacists, and bereavement counselors all contribute.

## Why structured symptom assessment matters
Serious illness produces clustered, interacting symptoms: pain, dyspnea, nausea, constipation, fatigue, drowsiness, anorexia, anxiety, depression, existential distress. Patients under-report; families over-report; clinicians' unaided impressions vary. Validated instruments exist precisely so that a team member seeing the patient on Tuesday can compare to the team member who saw them on Friday, and so that a symptom burden can be tracked across a disease trajectory.

## Instruments this workspace supports

### ESAS-r — Edmonton Symptom Assessment System (revised)
- Patient self-reports 9 symptoms on a 0–10 numeric rating scale (0 = none, 10 = worst possible).
- Items: pain, tiredness, drowsiness, nausea, lack of appetite, shortness of breath, depression, anxiety, wellbeing. A 10th "other problem" slot is common.
- Time frame: "right now" (there are 24-hour variants; the team picks one and is consistent).
- Scoring: report each item individually; compute a composite sum (0–90) for trend purposes. A change of ≥ 1 point on an item or ≥ 3 on the composite is often treated as the minimal clinically important difference (MCID) — local policy may set a different threshold.
- Use: primary symptom-burden screen, repeated at each encounter, in both inpatient and community settings.

### IPOS — Integrated Palliative care Outcome Scale
- 17 items covering physical symptoms, emotional symptoms, family/practical concerns, and communication/information needs.
- Patient-rated and staff-rated versions exist; results correlate but do diverge.
- Time frame: typically "over the past 3 days" or "over the past 7 days" depending on version.
- Scoring: each item 0–4; composite 0–68. Subscale scores (physical, emotional, communication/practical) can be reported separately.
- License: Cicely Saunders Institute. Free for non-commercial clinical and research use with registration. Deploying teams must register.

### POS-S — Palliative care Outcome Scale — Symptoms
- 10-item symptom-focused subset of the POS family; patient-rated 0–4 per item (composite 0–40).
- Useful when the team wants a focused physical-symptom assessment without the broader IPOS domains.

### Abbey Pain Scale
- Observer-rated; designed for adults who cannot verbalize (advanced dementia, late-stage neurologic illness).
- 6 items: vocalization, facial expression, body language, behavioral change, physiological change, physical change.
- Each 0–3; total 0–18. Bands: 0–2 no pain, 3–7 mild, 8–13 moderate, ≥14 severe.
- Observation window: during or immediately after a care activity (repositioning, personal care) to capture movement-related pain.

### PAINAD — Pain Assessment in Advanced Dementia
- Observer-rated; 5 items (breathing, vocalization, facial expression, body language, consolability).
- Each 0–2; total 0–10. 1–3 mild, 4–6 moderate, 7–10 severe.
- Similar use-case to Abbey; some teams prefer PAINAD for brevity, others prefer Abbey for richer behavioral capture.

### RASS — Richmond Agitation-Sedation Scale
- 10-point scale, -5 (unarousable) to +4 (combative). 0 is alert and calm.
- Used to document sedation level during symptom-directed therapy, palliative sedation, or delirium workup.
- Documentation best practice: record the RASS with a timestamp and observation context (e.g., "at rest, prior to care").

### CAM — Confusion Assessment Method
- Delirium screen. 4 features:
  1. Acute onset and fluctuating course
  2. Inattention
  3. Disorganized thinking
  4. Altered level of consciousness
- Delirium present = feature 1 AND feature 2 AND (feature 3 OR feature 4).
- CAM-ICU is a variant for non-verbal ICU patients.

### Karnofsky Performance Status (KPS) and Palliative Performance Scale (PPS)
- Functional status. KPS: 0–100 in 10-point increments (100 = normal, no complaints; 0 = dead). PPS is similar but palliative-oriented, with explicit descriptors for ambulation, activity, self-care, intake, and consciousness at each 10-point band.
- Serial PPS is a prognostic signal — trends matter more than single values. PPS ≤ 30% often marks days-to-weeks prognosis; PPS ≤ 20% marks hours-to-days. **These are associations, not determinations.**

### FICA — Spiritual assessment framework
- F — Faith and belief
- I — Importance of faith in the person's life
- C — Community of faith
- A — Address in care (how the team should incorporate it)
- Qualitative, not scored. Typically captured by chaplaincy or social work; any team member can use the prompts.

## Common symptom clusters
- **Pain + anxiety + insomnia:** bidirectional; treating one without the others often fails.
- **Dyspnea + cough + fatigue:** common in advanced lung disease and CHF.
- **Nausea + anorexia + constipation:** often iatrogenic (opioid-related); review the medication profile.
- **Delirium + agitation + sleep disturbance:** often a harbinger of metabolic or infectious decompensation; CAM + RASS + workup.

## Thresholds and MCIDs (typical starting points)
- ESAS-r: item delta ≥ 1 = clinically meaningful; composite delta ≥ 3 = meaningful.
- IPOS: aggregate delta ≥ 3 = meaningful.
- Any item score ≥ 7 on ESAS-r: by default, flag for same-day clinician review.
- Pain score ≥ 5 on Abbey or PAINAD: flag.
- CAM positive: flag.
- PPS drop of ≥ 20% between captures: flag (possible phase transition).

Teams tune these; see `resources/escalation-thresholds.md`.

## What you must not do
- Do not attempt to identify the "cause" of a symptom from checklist data alone.
- Do not translate a score into a treatment. That is the clinician's job.
- Do not reproduce copyrighted full-text items if the team hasn't confirmed licensing.
- Do not claim validity beyond what the instruments' validation literature supports.
