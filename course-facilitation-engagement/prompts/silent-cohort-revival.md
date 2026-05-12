# Silent Cohort Revival — Whole-Cohort Disengagement Intervention

## Purpose
Use this prompt when the cohort goes quiet at scale — a Behavioral-cohort-medium (or worse) signal: submission rate sliding under 70%, two consecutive modules with attendance under 60%, forum thread count flatlining, pulse mean under 3.5/5. A cohort-scope problem cannot be solved with individual nudges; trying produces nudge fatigue and worsens the underlying disengagement.

## Prerequisites
- The signal source(s) and severity from `resources/engagement-metrics-reference.md`
- The cohort register, especially the consent posture for cohort-wide pulses
- Acknowledgement from the facilitator that an individual `/at-risk-outreach` chain is NOT the right move here

## Prompt Template

The cohort {{cohort_name}} is showing cohort-wide disengagement: {{describe_signals}}. Run the silent-cohort-revival pattern. Do not draft any individual at-risk outreach. The intervention is:

### Step 1 — Diagnose first, message second
Before sending anything, propose a one-question Slack pulse to learners:
- "What is the single biggest reason this course is hard to engage with right now?"
- 4 multiple-choice options + an "Other" with free text
- Anonymous

Render this as `during-learner-pulse-slack` with a 90-word framing that:
- Acknowledges the silence honestly (no euphemism)
- Names the time investment (it takes a minute)
- Commits to a response within 72 hours

### Step 2 — Format change, not volume increase
While the pulse runs (24–48h), draft a *format change* — not another email:
- A 4-minute facilitator Loom titled "Hi cohort — let's reset" — facilitator self-disclosure on what is going on, what the team will do, what the cohort can ask for
- A shifted live session — same content, different format (case-clinic, peer teach-back, sprint, AMA)
- A "this week, do less" message that reduces the scheduled load by ~30% with a clear restart point

Render the Loom script and the format-change announcement (`during-learner-reset-email`).

### Step 3 — Aggregate the pulse responses honestly
Within 72h of the pulse close, aggregate themes. Do not editorialize the aggregate.

The most common diagnoses, with default responses:
- **"Pacing is too fast"** → cut content density for the next module; publish what you cut
- **"Relevance is unclear"** → re-anchor to the program-level objective in the next live session; offer 1:1 office hours
- **"Asynchronous load is too heavy"** → drop a piece of asynchronous work; replace with live application
- **"I'm just busy at work"** → an external cause; the workspace's job is to reduce friction, not increase pressure
- **"The cohort feels disconnected"** → social-presence intervention: peer-pair, breakout introductions, a co-built artifact

### Step 4 — Publish the change
Render `during-learner-pulse-recap-email` with:
- The aggregate themes (ranked)
- The change you will make for each top theme — concrete, named, time-bound
- An invitation to opt in to a small voluntary peer-pair if relatedness was the theme
- A thank-you for the honesty

### Step 5 — Track the recovery signal
For 14 days, watch:
- Submission rate (target: returns to ≥80%)
- Pulse mean (re-pulse at +14 days)
- Forum activity (target: 30% of cohort posts at least once in the next 7 days)
- Live attendance (target: returns to ≥80%)

If any signal recovers, log the format change that worked into `outputs/{cohort_id}/cohort-recovery-{YYYY-MM-DD}.md` for next-cohort cadence design.

If two of four signals fail to recover within 14 days, the disengagement is structural (curriculum or scheduling, not facilitation) — escalate to the program owner with a structural-cause memo.

## Expected Output

`outputs/{cohort_id}/silent-revival-{YYYY-MM-DD}.md` with sections:
- The signals and the diagnosis
- The pulse instrument (rendered)
- The format change (rendered Loom script + email)
- The themes and the published change-in-response
- The recovery-tracking plan with named owner and dates

## Decision Points
- If the cohort culture is reserved or senior-heavy, run the pulse via a 1:1 sample (3–5 trusted learners) instead of cohort-wide; the dynamics are different.
- If only one signal is below threshold while the others are healthy, this is not silent-cohort revival — it is an `/at-risk-outreach` at cohort-scope on the specific signal.
- If the disengagement coincides with a known external event (org restructure, public crisis), pause the intervention and lead with empathy in a single facilitator message; resume in 72h if signals stay flat.
- If facilitator self-disclosure is not culturally appropriate, replace the Loom with a written message from the named program sponsor.
