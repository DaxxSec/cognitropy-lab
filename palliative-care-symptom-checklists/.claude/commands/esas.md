# /esas

Run an ESAS-r (Edmonton Symptom Assessment System — revised) assessment.

## Input

Before starting, confirm:
- Session placeholder for the patient (e.g., "Patient A").
- Time frame: "right now" vs. "over the past 24 hours". Pick one and use it consistently.
- Reporter: patient self-report vs. proxy (caregiver, staff).

## Steps

1. For each of the 9 items below, ask: "On a 0–10 scale, how would you rate [item] [time frame]? (0 = none, 10 = worst possible)":
   1. Pain
   2. Tiredness
   3. Drowsiness
   4. Nausea
   5. Lack of appetite
   6. Shortness of breath
   7. Depression
   8. Anxiety
   9. Wellbeing
2. Offer a 10th optional slot: "Any other problem to capture? (name and 0–10 score)"
3. Echo back the full item set before computing.
4. Compute composite (sum items 1–9, max 90).
5. Pull prior ESAS-r captures for this placeholder from the session history (if any). Compute per-item and composite deltas.
6. Apply flags:
   - Any item score ≥ 7
   - Any item delta ≥ 1
   - Composite delta ≥ 3
7. Produce a draft note structured as:
   - Header (placeholder, date, time frame, reporter)
   - Item table
   - Composite
   - Trend (if prior captures exist)
   - Flags
   - "Draft — clinician review required" footer
8. Append a de-identified entry to `work-log/session-log.md`.

## Reminders

- Do not translate scores into interventions.
- Do not assign diagnoses ("seems depressed" → no; "Depression item score of 6" → yes).
- If the clinician describes an acute emergency during capture, pause and redirect.
