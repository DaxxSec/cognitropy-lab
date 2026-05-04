# /recap-module — Multi-Stakeholder Module Recap Pack

Generate the four-audience recap that closes a module: a learner recap, a manager nudge, a facilitator log, and (when sponsor is Definitive) a sponsor highlight.

## Required Inputs
- Module number and title (or pull from `planning/plan.md`)
- Module objectives (Bloom-anchored if available)
- Live session highlights — what landed, what surprised, what was missed
- Engagement signals from the session: attendance %, polls, forum activity, asset opens
- Names of any learners who deserve named celebration (with their consent assumed from cohort onboarding)
- Names of any learners who appear at-risk (do NOT name in the learner recap; only in the facilitator log)
- Cohort culture context (whether public peer recognition is welcomed or muted)

## Steps

### 1. Compose the Learner Recap (`during-learner-recap-email`)
Body shape:
- One-line "what we did and why it mattered" (cognitive presence)
- 3 bullets: the points worth re-reading
- Application prompt — one specific thing to try this week (relatedness + autonomy)
- Office-hours link or peer thread link
- Sign-off with facilitator name and a one-line forward look to the next module

Length target: 180–250 words. Reading-level target: Grade 8.

### 2. Compose the Manager Nudge (`during-manager-nudge-email`)
Body shape:
- One-line "your team member just finished {{module_title}}"
- 3 bullets: what was covered, expressed in plain language for a non-attendee
- 2–3 1:1 prompts the manager can use this week (concrete, named to the objectives)
- Optional: a one-paragraph "what to listen for" cue that supports the application without coercing

Length target: 120–180 words. Tone: peer, not coercive.

### 3. Compose the Facilitator Log (`during-facilitator-recap-internal`)
Internal artifact, written for the facilitator and producer only. Sections:
- Session metrics: attendance, on-time %, poll results, forum thread count
- Engagement temperature (1–5) — facilitator's own read on the session's energy
- What worked, what dragged
- Named at-risk learners and rationale
- Adjustments to next module's plan
- Any content issue to escalate to the curriculum owner

Length target: 250–500 words. Privacy: not shared with learners or managers.

### 4. Compose the Sponsor Highlight (Definitive sponsors only)
Three-paragraph, ≤250 words:
- One paragraph: a story of one thing the cohort accomplished this module (no PII)
- One paragraph: the cohort-level signal — completion, attendance, pulse trend
- One paragraph: what the sponsor can do this week to amplify (a forward, a Slack post, a 5-min Loom thank-you)

If the sponsor is not Definitive, skip this artifact and queue a digest in the next sponsor cycle.

### 5. Quality Pass
For each artifact:
- Run the plain-language check (active voice, sentence length, common words)
- Confirm UDL: text + a 3-min Loom for the learner recap; alt text on any image
- Confirm one-ask rule: each artifact has exactly one ask of its audience
- Confirm time-bound: any deadline includes ISO date + time + zone

### 6. Render and Route
Write each artifact to `outputs/{cohort_id}/module-{n}-{audience}-{YYYY-MM-DD}.md`.

Update the cadence calendar (`planning/plan.md`) — mark the row "drafted" with the file path.

Open `work-log/<YYYY-MM-DD>.md` and log a single line per artifact with named approver and review SLA.

### 7. Hand Off for Approval
Surface the four artifacts to the named approvers from the RACI. The agent does not auto-send; the user reviews and dispatches via the approved channel.

## Output
- 3 to 4 markdown artifacts in `outputs/{cohort_id}/`
- Updated `planning/plan.md` row statuses
- Work-log entry per artifact

## Decision Points
- If the live session was canceled or notably under-attended, swap the learner recap for a `during-learner-makeup-email` that offers an asynchronous path before sending the manager nudge.
- If the at-risk list is long (>15% of cohort), do not name them in the facilitator log alone — schedule a same-week conversation with the producer and trigger `/at-risk-outreach` for each.
- If the cohort culture is reserved (e.g., regulated industries, senior-leader cohorts), keep the learner recap warm but private — peer-recognition belongs in DM, not in the cohort-wide recap.
