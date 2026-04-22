# Escalation Thresholds

These are **starting defaults**. The medical director and nursing lead must review and adjust these to match the team's clinical policy before production use. The agent will prompt for re-review if the `Last reviewed` date below is more than 180 days old.

**Last reviewed:** 2026-04-22 (workspace initial build — **unverified, pilot-only**)
**Reviewed by:** (pending medical director sign-off)

## Same-day clinician review flags

| Instrument | Trigger |
|---|---|
| ESAS-r | Any item ≥ 7, or composite delta ≥ 3 from prior capture |
| IPOS | Composite delta ≥ 3, or any subscale delta ≥ 2 |
| Abbey | Total ≥ 8, or upswing from prior < 3 to current ≥ 5 |
| PAINAD | Total ≥ 4, or upswing from prior < 2 to current ≥ 3 |
| RASS | ≤ -3 or ≥ +2 |
| CAM | Any positive CAM |
| PPS | Drop ≥ 20 percentage points between captures |

## Urgent clinician review flags (escalation to on-call)

Surfaced in the draft, but **the agent does not page or notify**. The clinician at the session escalates via the team's standard channel.

| Trigger |
|---|
| ESAS-r pain ≥ 9 |
| Any acute-emergency phrase from the clinician describing the patient's condition |
| Reported suicidal ideation in patient or caregiver |
| Unsafe home environment disclosure |

## Notes on tuning

- Thresholds should be tuned with the team's medical director and informed by local population (hospice vs. upstream palliative vs. oncologic vs. neurologic emphases).
- MCIDs in the literature vary by population; the thresholds above are intentionally conservative starting points.
- Any change to these thresholds should be versioned in this file with reviewer initials and date.
