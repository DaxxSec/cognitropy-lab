# Core Workflows — Course Facilitation Engagement

Each workflow below is a decision tree the agent should walk before drafting. They are deliberately concrete; if a step says "consult the template library", that means: open `resources/stakeholder-template-library.md`, locate the matching ID, render the parameters from the workspace context.

## Workflow 1: Stakeholder Mapping & RACI

**Goal:** before any messaging, know who needs which depth of communication and who approves what.

### Steps
1. **Pull the stakeholder list** from `context/project.md` (initial pass written during `/onboard`).
2. **Score each stakeholder** on Power (1–5) and Interest (1–5). Place them on a Power–Interest grid:
   - Power ≥ 4, Interest ≥ 4 → **Manage closely** — full cadence, named approver, weekly minimum touchpoint
   - Power ≥ 4, Interest < 4 → **Keep satisfied** — milestone-driven cadence, never deluge
   - Power < 4, Interest ≥ 4 → **Keep informed** — full content but no decision asks
   - Power < 4, Interest < 4 → **Monitor** — one inform per phase boundary
3. **Apply Mitchell-Agle-Wood salience.** For each stakeholder, mark Power / Legitimacy / Urgency present (Y/N). Definitive (all 3) and Dominant (P+L) stakeholders get named approval lanes.
4. **Build the RACI** for each phase (pre / during / post). For every artifact (kickoff invite, pulse summary, sponsor readout, certificate), name:
   - Responsible (does the work — usually the agent + facilitator)
   - Accountable (signs off before send — single named person)
   - Consulted (reviews input — e.g., compliance, accessibility)
   - Informed (gets the result — typically the wider stakeholder list)
5. **Output to `outputs/stakeholder-register-{cohort_id}.md`** with the matrix, salience flags, and RACI. Mirror to `planning/plan.md` so the cadence calendar references the register, not duplicate stakeholder data.

### Decision Points
- If a stakeholder is missing a named approver: pause and ask the user before drafting.
- If two stakeholders compete for the same decision (e.g., compliance vs. sponsor on regulated language): document the conflict in the register and resolve before any send.
- If a stakeholder's salience changes mid-cohort: re-run this workflow; do not patch the register inline.

## Workflow 2: Cadence Design

**Goal:** produce a phase-by-phase calendar with explicit template IDs assigned to each touchpoint.

### Steps
1. **Read the course profile** (`context/project.md`) and the stakeholder register from Workflow 1.
2. **Lay down the phase backbone** (Pre, During-by-module, Midpoint, Post, Long-term) in `planning/plan.md`.
3. **For each phase × stakeholder cell**, decide whether a touchpoint is required:
   - Required if salience ≥ Dominant or if the phase is a transition (kickoff, midpoint, certification, D+30)
   - Optional if Discretionary/Dependent and the cell adds value (alumni invite at D+30, SME thank-you post-module)
   - Skipped otherwise
4. **Assign a template ID** from `resources/stakeholder-template-library.md` to every required cell. If the cell has no matching template, mark it `<<NEW>>` and flag for authoring.
5. **Resolve channel** based on stakeholder norms: senior sponsors prefer email + a 5-min Loom; learners prefer LMS announcement + Slack DM nudge; managers prefer email with a single bullet ask.
6. **Apply CoI balance check.** Sum the cognitive / social / teaching presence tags for the during-phase touchpoints. If any presence < 25% of the total, rebalance.
7. **Apply UDL representation check.** Confirm each module's outbound mix offers ≥2 means of representation (e.g., text recap + 3-min Loom).
8. **Time-zone audit.** For each scheduled send, compute send time in each represented learner time zone. Move any send that falls outside 08:00–20:00 local for ≥10% of the cohort.
9. **Approver attach.** Pull the named Accountable from the RACI for every send and attach it to the calendar entry.
10. **Render the calendar** to `planning/plan.md` — table with columns: ISO date | T-relative | stakeholder | template ID | channel | approver | status.

### Decision Points
- If two sends to the same audience fall within 24 hours: merge or stagger.
- If a manager send precedes the parallel learner send: reorder so learners always hear first about their own course.
- If the cohort spans more than three time zones, choose two send waves rather than one global wave.

## Workflow 3: Triggered Outreach (Engagement Signals → Templates)

**Goal:** translate an engagement signal into the right escalation chain.

### Steps
1. **Receive a signal.** Either pulled (cron-style watch on LMS analytics) or pushed (the user pastes a flag).
2. **Classify the signal** against the table in `resources/engagement-metrics-reference.md`:
   - Layer (Logistical / Behavioral / Cognitive / Affective)
   - Scope (individual / cohort / cross-cohort)
   - Severity (low / medium / high) using thresholds in the reference
3. **Choose the starting message** based on layer + scope + severity:
   - Logistical-individual-low → `trigger-learner-nudge-email` (single line, autonomy-preserving)
   - Behavioral-individual-medium → `trigger-learner-remind-email` + offer of office hours
   - Cognitive-individual-medium → 1:1 conversation prompt for the facilitator (not an automated send)
   - Affective-individual-high → human follow-up only; do not auto-send
   - Behavioral-cohort-medium → `during-cohort-pulse-email` to surface what is in the way before nudging
   - Affective-cohort-high → run `prompts/silent-cohort-revival.md` end-to-end
4. **Sequence the chain.** Default sequence:
   - T+0: learner template
   - T+72h if no movement: re-attempt with a different format (Loom, peer prompt)
   - T+5–7 days, only if Power-Interest scoring of manager allows: manager nudge, learner-CC
   - T+14 days, only on persistent Definitive risk: sponsor flag (frame as "need your perspective", not "your investment is at risk")
5. **Log every step** to `work-log/<YYYY-MM-DD>.md` with the signal, the template chosen, the time of send, and the named approver.
6. **Close the loop** by capturing the response signal: did the learner re-engage by T+7? If yes, send `during-learner-celebrate-slack` if the cohort culture allows; if no, escalate.

### Decision Points
- If the signal looks like a content issue (cohort spike on the help channel about a single module): do not message individual learners; talk to the facilitator and producer first.
- If the signal could be confounded by external factors (a public holiday, a known org-wide incident): pause the chain by 48–72h.
- If the learner has a documented life event (bereavement, medical leave): suspend triggered outreach; a single human-authored note from the facilitator is the only acceptable touch.

## Workflow 4: Sponsor Readout (Kirkpatrick-Aligned)

**Goal:** produce a readout that moves sponsor attention up the Kirkpatrick levels.

### Steps
1. **Pull the four-level evidence inventory:**
   - Level 1 — Reaction: pulse mean + close-out CSAT, NPS, qualitative quotes (anonymized)
   - Level 2 — Learning: pre/post knowledge or skill assessment delta
   - Level 3 — Behavior: manager-observed change, application-plan completion, peer-reviewed work artifacts
   - Level 4 — Results: business metric tied to the program (lead/lag indicator)
2. **Frame the narrative.** A good sponsor readout has three parts:
   - What we set out to do (recap the original commitment, not generic intro)
   - What happened (the four levels, in order)
   - What we recommend next (next cohort, next intervention, next ask)
3. **Choose visuals.** Limit to four: completion funnel, pulse trend, one Level-3 artifact image, one Level-4 metric chart. No vanity graphs.
4. **Write the executive summary first.** Three bullets, max 60 words. The rest of the readout is appendix to the summary.
5. **Apply the "no surprises" rule.** Anything in the readout the sponsor has not heard at least once before should have been a precursor message — if not, that is a cadence-design failure, not a readout problem.
6. **Pre-brief the named accountable.** Walk the sponsor's chief of staff or program-management partner through the draft 48h before the formal readout.
7. **Render to `outputs/sponsor-readout-{cohort_id}-{YYYY-MM-DD}.md`** and attach the source data to the work-log.

### Decision Points
- If Level 3 evidence is thin: do not pad with Level 1. State the gap and propose how the next iteration will collect it.
- If Level 4 movement is unclear: present leading indicators with named confidence intervals; do not claim attribution you cannot defend.
- If the sponsor wants to cut the next cohort: have the recommendation ready in the readout; do not be surprised in the meeting.

## Workflow 5 (Optional): Cohort-Close Reflection & Alumni Hand-off

**Goal:** convert engagement assets into evidence for next cohort and into the alumni network.

### Steps
1. Render the learner reflection prompt (`post-learner-reflect-email`).
2. Aggregate consenting learner stories into a sanitized success-story bank in `outputs/`.
3. Send the alumni invite (`post-alumni-invite-email`).
4. Loop best stories into the next cohort's `pre-learner-invite-email` as social proof.
5. Archive the cadence calendar; flag templates that under-performed for revision in the next cohort.
