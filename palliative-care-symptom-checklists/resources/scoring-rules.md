# Scoring Rules

These are the canonical scoring rules the agent applies. The agent uses these exactly as written; it does not improvise.

## ESAS-r

- 9 items, each 0–10.
- Composite: sum of items 1–9 (range 0–90).
- Missing item handling: do not estimate. Report composite only if all 9 are present; otherwise report item-level scores and an incomplete-composite note.
- Delta thresholds (defaults, tunable per team):
  - Item delta ≥ 1 = clinically meaningful
  - Composite delta ≥ 3 = clinically meaningful
  - Any absolute item score ≥ 7 = flag for same-day clinician review

## IPOS

- 17 items, each 0–4.
- Subscales:
  - Physical symptoms: items 1–10 (range 0–40)
  - Emotional symptoms: items 11–13 (range 0–12)
  - Communication / practical: items 14–17 (range 0–16)
- Composite: sum of all items (range 0–68).
- Missing item handling: report subscale only if all items in that subscale are present; otherwise flag incomplete.
- Delta thresholds (defaults):
  - Composite delta ≥ 3 = meaningful
  - Subscale delta ≥ 2 = meaningful

## POS-S

- 10 symptom items, each 0–4.
- Composite: sum (range 0–40).
- Delta threshold default: composite delta ≥ 2 = meaningful.

## Abbey Pain Scale

- 6 items, each 0–3.
- Total: 0–18.
- Bands:
  - 0–2: no pain
  - 3–7: mild pain
  - 8–13: moderate pain
  - 14–18: severe pain
- Flag defaults: total ≥ 8, or upswing from prior total < 3 to current ≥ 5.

## PAINAD

- 5 items, each 0–2.
- Total: 0–10.
- Bands:
  - 0: no pain
  - 1–3: mild
  - 4–6: moderate
  - 7–10: severe
- Flag defaults: total ≥ 4, or upswing from prior total < 2 to current ≥ 3.

## RASS

- Single score, -5 to +4.
- Bands:
  - -5 to -3: deep sedation / unarousable
  - -2 to -1: light sedation
  - 0: alert and calm
  - +1 to +2: restless / agitated
  - +3 to +4: very / combative
- Flag defaults: RASS ≤ -3 or ≥ +2 = flag.

## CAM

- Features:
  1. Acute onset and fluctuating course
  2. Inattention
  3. Disorganized thinking
  4. Altered level of consciousness
- Delirium present = (1) AND (2) AND ((3) OR (4)).
- Flag: any positive CAM = flag.

## Karnofsky / PPS

- KPS: 0–100 in 10-point increments.
- PPS: 0–100% in 10-point increments, with descriptors for ambulation, activity, self-care, intake, LOC at each band.
- Flag: drop of ≥ 20 percentage points between captures = flag.

## FICA

- Qualitative; no numeric score.
- Output: narrative of each of F / I / C / A, captured in clinician's words.

## What the agent must not do

- Do not apply a scoring rule not documented here.
- Do not compose a custom composite by combining scales without explicit clinician instruction and a clear note in the draft.
- Do not treat any threshold as a treatment recommendation.
