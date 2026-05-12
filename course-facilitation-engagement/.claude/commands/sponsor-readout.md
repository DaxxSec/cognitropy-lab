# /sponsor-readout — Kirkpatrick-Aligned Executive Readout

Produce a sponsor readout that moves attention up the Kirkpatrick levels rather than parking on smile-sheet reaction. Use at cohort close, and on a quarterly cadence for ongoing programs.

## Required Inputs
- The original commitment to the sponsor (recap from `context/project.md` engagement goals)
- Cohort metrics by Kirkpatrick level — pull from outputs and `work-log/`:
  - Level 1: pulse mean, close-out CSAT/NPS, anonymized qualitative quotes
  - Level 2: pre/post assessment delta if in scope
  - Level 3: manager-observed change, application-plan completion, peer-reviewed work artifacts at D+30
  - Level 4: business metric tied to the program (lead or lag indicator), with attribution caveats
- The sponsor's preferred reading length (most prefer ≤2 pages)
- The "what next" recommendation — next cohort, next intervention, next ask

## Steps

### 1. Pull the Four-Level Inventory
For each level, list the evidence you have and the evidence you do NOT have. Honest gaps land better than padded narratives.

```
Level 1 (Reaction)
- Pulse mean: {{pulse_mean}} (n={{pulse_n}}, mid-cohort and close)
- Close CSAT/NPS: {{csat}} / {{nps}}
- Qualitative themes: {{theme_1}}, {{theme_2}}, {{theme_3}}
- Gaps: {{any}}

Level 2 (Learning)
- Pre/post knowledge delta: +{{delta}} pts (n={{n}})
- Skill-artifact rubric scores at close: {{scores}}
- Gaps: {{any — e.g., no pre-assessment ran}}

Level 3 (Behavior)
- Manager-observed application: {{n_managers}} of {{m_managers}} reported change at D+30
- Application-plan completion: {{pct}}%
- Peer-reviewed work artifacts: {{count}} submitted, {{count_strong}} judged strong
- Gaps: {{any}}

Level 4 (Results)
- Business metric: {{metric}} moved from {{baseline}} to {{post}} (Δ {{delta}})
- Attribution confidence: {{low|medium|high}} — caveats: {{caveats}}
- Gaps: {{any}}
```

### 2. Frame the Narrative — Three Parts
**Part A — What we set out to do.**  Restate the sponsor's original commitment in their own words. Two sentences. This is not a generic course intro.

**Part B — What happened.**  Walk Levels 1 → 4 in order. Each level gets one paragraph; if Level 3/4 evidence is thin, name the gap and the proposed remedy. Use plain numbers, not "an engaging cohort experience".

**Part C — What we recommend next.**  Three options at most:
- Continue (next cohort, named dates)
- Adjust (named change, owner, by-when)
- Stop (with rationale and an alternative use of the budget)

### 3. Choose Visuals (Cap at Four)
1. Completion funnel (enrolled → active → completed → certified)
2. Pulse trend line (mid → close)
3. One Level-3 artifact image (anonymized; with the artifact-owner's consent)
4. One Level-4 metric chart with confidence interval

No vanity graphs — every visual must change a decision.

### 4. Write the Executive Summary First
Three bullets, ≤60 words total. The body of the readout is appendix to this summary.

Example shape:
- We delivered {{cohort_name}} to {{n_learners}} learners; completion {{pct}}%, pulse mean {{pulse}}.
- Behavior change at D+30 is observable in {{n_managers}} manager check-ins; the strongest signal is {{theme}}.
- Recommend {{continue|adjust|stop}} — next decision needed by {{date}}.

### 5. Apply the No-Surprises Rule
Anything in the readout that the sponsor has not heard at least once before should have been a precursor message during the cadence. If you find a surprise here, that is a cadence-design failure — note it in the appendix and adjust the next cohort's calendar.

### 6. Pre-brief the Named Accountable
Walk the sponsor's chief of staff or program-management partner through the draft 48h before the formal readout meeting. Capture their feedback in `outputs/{cohort_id}/sponsor-readout-prebrief-{YYYY-MM-DD}.md` and revise.

### 7. Render
Write to `outputs/{cohort_id}/sponsor-readout-{YYYY-MM-DD}.md` with:
- Executive summary (top)
- Narrative (the three parts)
- Evidence by level (the inventory from Step 1)
- Recommendation
- Appendix: methodology, attribution caveats, any cadence misses worth flagging

Render to PDF or slide form per the sponsor's preference using their org's deck template.

### 8. Send the Readout
Render `post-sponsor-recap-email` with:
- A 60-word body
- The artifact attached
- A 5-min Loom from the lead facilitator (UDL representation)
- One specific ask (a decision, a forward, a forward to a peer sponsor)

Log the send and the response window to `work-log/`.

## Output
- `outputs/{cohort_id}/sponsor-readout-{YYYY-MM-DD}.md` — full readout
- `outputs/{cohort_id}/sponsor-readout-prebrief-{YYYY-MM-DD}.md` — pre-brief notes
- `outputs/{cohort_id}/sponsor-readout-summary.md` — the 60-word body for email/slack
- Work-log entry recording the readout send and the named approver

## Decision Points
- If Level 3 evidence is thin: do not pad with Level 1. State the gap, propose how the next iteration will collect it, and ask the sponsor whether they want to underwrite that collection (manager surveys, on-the-job observation).
- If Level 4 movement is unclear: present leading indicators with named confidence intervals; do not claim attribution you cannot defend.
- If the sponsor signals they want to cut the next cohort, have the recommendation ready in the readout — do not be surprised in the meeting.
- If the cohort under-performed, lead with the strongest signal (often a Level 3 narrative) and frame the recommendation as "what would change next".
