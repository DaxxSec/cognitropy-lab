# Workflows

All workflows share a common shape:
1. **Context check** — who is using the tool, which patient placeholder, which instrument, which time frame.
2. **Administer** — walk the checklist item-by-item using the validated wording.
3. **Compute** — apply the published scoring rules.
4. **Trend** — compare against prior session captures, flag meaningful changes.
5. **Draft** — produce the structured output, clearly labeled "Draft — clinician review required."
6. **Log** — append a de-identified entry to `work-log/session-log.md`.

## Workflow: ESAS-r assessment

**Inputs from clinician:** patient placeholder, time frame ("right now" vs. "past 24 hours"), whether patient is self-reporting or proxy-reporting.

**Steps:**
1. Confirm placeholder and time frame. If proxy-reporting, note that in the draft.
2. For each of the 9 items, ask: "On a 0–10 scale, how would you rate [item] [time frame]?" Items in order: pain, tiredness, drowsiness, nausea, lack of appetite, shortness of breath, depression, anxiety, wellbeing. Offer a 10th "other" slot.
3. Confirm each score back to the clinician before moving to the next.
4. Compute composite (sum of items 1–9, max 90).
5. Pull last 3 captures from session history for this placeholder; compute deltas per item and composite.
6. Flag: any item delta ≥ 1, composite delta ≥ 3, or any absolute item score ≥ 7.
7. Produce a draft with: placeholder, time frame, reporter (self / proxy), item table, composite, deltas, flags, and a "Draft — clinician review required" footer.

## Workflow: IPOS assessment

**Inputs:** placeholder, version (patient-reported vs. staff-reported), time window (3-day vs. 7-day), licensing confirmation.

**Steps:**
1. Confirm the team has registered for the IPOS license with the Cicely Saunders Institute. If not confirmed, refuse to proceed and direct to registration.
2. Confirm placeholder, version, window.
3. For each of the 17 items, reference by item number and topic (e.g., "Item 3 — shortness of breath over the past 3 days"). Do not reproduce full copyrighted item text; rely on the team's licensed copy in front of the clinician.
4. Capture 0–4 response per item.
5. Compute subscale totals (physical, emotional, communication/practical) and composite (0–68).
6. Trend against prior IPOS captures; flag aggregate delta ≥ 3 or subscale delta ≥ 2.
7. Produce draft with subscale breakdown and flags.

## Workflow: Abbey Pain Scale

**Inputs:** placeholder, observation context (during / after care activity, or at rest), observer name placeholder.

**Steps:**
1. Confirm observation window.
2. Capture six items (0–3 each): vocalization, facial expression, body language, behavioral change, physiological change, physical change.
3. Sum to total (0–18). Map to band: 0–2 none, 3–7 mild, 8–13 moderate, ≥14 severe.
4. Flag total ≥ 8, or total ≥ 5 if prior total was < 3 (meaningful upswing).
5. Draft note with bands and flags.

## Workflow: PAINAD

Similar to Abbey but 5 items (breathing, vocalization, facial, body, consolability), 0–2 each, total 0–10. Bands: 1–3 mild, 4–6 moderate, 7–10 severe. Flag total ≥ 4 or upswing from < 2 to ≥ 3.

## Workflow: RASS

Single-score documentation. Ask clinician the observed RASS value (-5 to +4), observation context, timestamp. Draft a one-line note.

## Workflow: CAM

Walk the four features:
1. Acute onset and fluctuating course (yes/no)
2. Inattention (yes/no)
3. Disorganized thinking (yes/no)
4. Altered level of consciousness (yes/no)

Delirium present = (1) AND (2) AND ((3) OR (4)). Note which features are positive and whether CAM is positive overall.

## Workflow: Trend view

**Inputs:** placeholder, instrument, number of prior captures to include (default 5).

**Steps:**
1. Pull the last N captures of the specified instrument for this placeholder.
2. Produce a small table: date, composite, key items, notes.
3. Identify the direction of change for each item (improving / stable / worsening).
4. Flag any items that crossed the team's threshold in the most recent capture.
5. Do **not** interpret cause. Output is descriptive.

## Workflow: SBAR draft

**Inputs:** placeholder, clinical question (why is this handoff happening?), most recent captures to pull from.

**Steps:**
1. **Situation** — one-sentence description of why the handoff is needed. Clinician-provided.
2. **Background** — key diagnoses, goals-of-care status, current phase of care. Clinician-provided; agent structures.
3. **Assessment** — pulled from most recent structured captures (ESAS-r / IPOS / Abbey / PAINAD / RASS / CAM / PPS).
4. **Recommendation** — left as a clinician fill-in. Agent does not recommend specific interventions.

## Workflow: Family-meeting prep

**Inputs:** placeholder, meeting objective (goals-of-care discussion, transition discussion, bereavement-prep).

**Steps:**
1. Summarize symptom burden trajectory (last 2–4 captures) in lay language appropriate for clinician-to-family use.
2. Summarize functional trajectory (PPS / Karnofsky).
3. Surface open unmet needs from IPOS communication/practical subscale.
4. List discussion prompts (e.g., "What are they hoping for? What are they worried about? What matters most to them?") — drawn from validated serious-illness conversation guides.
5. Draft is labeled prep material, not a script.

## Workflow: Escalation flag

Whenever a threshold is crossed (per `resources/escalation-thresholds.md`), the agent surfaces it as a flag in the draft note. It does **not** page, email, SMS, or otherwise notify anyone outside the current session. Escalation is the clinician's responsibility.
