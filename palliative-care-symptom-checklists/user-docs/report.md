# Example Draft Output

An illustration of what the agent produces. This is a *fictitious* case; no real patient.

---

**Palliative Care — Structured Symptom Capture**

**Placeholder:** Patient A
**Date:** 2026-04-22
**Encounter type:** Weekly home visit
**Reporter:** Patient (self-report)
**Instrument:** ESAS-r
**Time frame:** Over the past 24 hours

| # | Item | Score (0–10) | Prior (N=3 avg) | Delta |
|---|---|---|---|---|
| 1 | Pain | 6 | 4.3 | +1.7 ↑ |
| 2 | Tiredness | 7 | 6.0 | +1.0 ↑ |
| 3 | Drowsiness | 5 | 5.0 | 0 |
| 4 | Nausea | 2 | 1.7 | +0.3 |
| 5 | Lack of appetite | 6 | 5.3 | +0.7 |
| 6 | Shortness of breath | 3 | 3.0 | 0 |
| 7 | Depression | 4 | 3.3 | +0.7 |
| 8 | Anxiety | 5 | 3.7 | +1.3 ↑ |
| 9 | Wellbeing | 6 | 4.7 | +1.3 ↑ |

**Composite:** 44 / 90  (prior 3-capture avg: 37.0; delta +7.0 ↑)

**Flags:**
- Pain ≥ 7 threshold not crossed, but pain delta ≥ 1 (MCID)
- Tiredness delta ≥ 1 (MCID)
- Anxiety delta ≥ 1 (MCID)
- Composite delta ≥ 3 (MCID)

**Symptom cluster note:** Pain + anxiety + tiredness trending up together over 4 captures — consider cluster review at IDT.

**Recommendation:** (clinician to complete)

---

**Draft — clinician review required. Not for medical-record entry without review and signature.**

Session log entry: appended to `work-log/session-log.md` with de-identified metadata only.

---

## What this example illustrates

- Numbers and trends captured without interpretation.
- Flags surfaced but no interventions proposed.
- Recommendation section left for the clinician.
- Draft footer making scope explicit.
- Symptom-cluster note is a structural observation, not a diagnosis.
