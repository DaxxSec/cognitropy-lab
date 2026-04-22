# /ipos

Run an IPOS (Integrated Palliative care Outcome Scale) assessment.

## Licensing precheck

IPOS is licensed through the Cicely Saunders Institute. Before starting, ask:
- "Has your organization registered for the IPOS license with the Cicely Saunders Institute?" (yes / no)
- If no, refuse to proceed and direct the user to the IPOS registration page. Do not continue.

## Input

- Session placeholder.
- Version: patient-rated vs. staff-rated.
- Time window: 3-day vs. 7-day.
- Confirmation that the clinician has the licensed IPOS form in front of them.

## Steps

1. For each of the 17 items, reference by **item number and topic** (e.g., "Item 3 — shortness of breath over the past 3 days"). **Do not reproduce the full copyrighted item wording.** Rely on the clinician's licensed form.
2. Capture 0–4 per item.
3. Compute subscale totals:
   - Physical symptoms (items 1–10)
   - Emotional symptoms (items 11–13)
   - Communication / practical (items 14–17)
4. Compute composite (0–68).
5. Trend against prior IPOS captures for this placeholder. Flag:
   - Aggregate delta ≥ 3
   - Any subscale delta ≥ 2
6. Draft note: subscale breakdown, composite, trend, flags, "Draft — clinician review required" footer.
7. Append de-identified `work-log` entry.
