# /pulse-check — Mid-Course Pulse Survey + Stakeholder Summaries

Design and deploy a short pulse, aggregate responses, and produce the stakeholder-specific summary outputs that close the loop.

## Required Inputs
- Module count remaining (so you can target this pulse to the right window — typically after Module 2 of a 5-module cohort, or at the calendar midpoint)
- Cohort size and channel of choice for the pulse (LMS-native, Typeform, Qualtrics, etc.)
- Anonymity model — pseudonymous default; named only if the cohort explicitly opted in at enrollment
- The list of decisions the pulse needs to inform (this dictates the questions)

## Steps

### 1. Pulse Question Design
Hold to 5–7 items. Cover three dimensions: experience, learning, and intention. Default item set (adapt copy to the cohort):

1. **Reaction (Likert 1–5)**: "{{course_name}} is meeting my expectations so far."
2. **Learning (Likert 1–5)**: "I am becoming more capable of {{primary_program_skill}} as a result of this course."
3. **Cognitive presence (Likert 1–5)**: "I have had at least one 'aha' moment in the last two weeks."
4. **Social presence (Likert 1–5)**: "I feel connected to my cohort."
5. **Teaching presence (Likert 1–5)**: "The pace and structure are working for me."
6. **One open text (≤200 chars)**: "What is the single change that would help you most in the back half?"
7. **Optional autonomy item (Likert 1–5)**: "I have enough choice in how I apply what I'm learning."

Tag each item to the framework it observes (CoI presence, SDT driver) so analysis can route to the right intervention.

### 2. Build the Send
- Render `during-learner-pulse-email` with a 5-line invitation: why we ask, what we'll do with it, how long it takes (target <3 min), how anonymity works, deadline ISO + zone.
- Schedule the send during a learner-active window (mid-morning local for the largest TZ cluster).
- Plan one reminder at 48h. No reminders after the deadline.

### 3. Set the Loop-Closing Commitment
Commit in the invitation to publish the aggregated result and the change-in-response within X days (default 5 working days). This is the reciprocity contract — without it, pulse fatigue sets in by the second cohort.

### 4. Run the Pulse
- Send via the chosen channel.
- Monitor response rate; aim for ≥60% (cohorts <30) or ≥40% (larger). Below those thresholds, the result is suggestive, not decisive.
- If <40%, the diagnosis is in the *response rate*, not the responses — escalate to a /at-risk-outreach pattern at cohort scope.

### 5. Aggregate Honestly
- Compute mean and distribution per item, not just the mean.
- Pull anonymized free-text quotes; tag by theme.
- Identify directional shifts vs. previous pulse if any (no significance claims without enough N).
- Translate to the framework: which presence is sagging? Which SDT driver is unsupported?

### 6. Stakeholder-Specific Summaries

**Learner summary** (`during-learner-pulse-recap-email`):
- Headline: the result, in plain language
- The most common "single change" theme
- The change(s) you will make in response (concrete and time-bound)
- Thank-you and the next pulse cadence
- Length: ≤300 words

**Facilitator summary** (internal):
- All distributions
- Free-text themes in full
- Cross-cut by module (if traceable) and time zone
- Named risks
- Length: ≤500 words

**Sponsor summary** (`during-sponsor-pulse-email`, Definitive only):
- Three lines: where we are (Level 1 number), what learners are saying (theme), what we're doing in response
- One chart (trend if you have one, distribution otherwise)
- Length: ≤200 words; the sponsor reads this on a phone

**Admin summary** (operational):
- Items they can act on: scheduling, accessibility, channel friction
- A short list, not a narrative

### 7. Make the Change
Within 5 working days, ship one observable change tied to the pulse. Examples:
- A schedule shift if pacing is the complaint
- A peer-pairing update if relatedness is sagging
- A new resource asset if competence is the complaint
- A re-broadcast of objectives if teaching presence is unclear

Log the change to `outputs/{cohort_id}/pulse-{YYYY-MM-DD}-action.md`.

## Output
- Pulse instrument (written) in `outputs/{cohort_id}/pulse-{YYYY-MM-DD}-instrument.md`
- Aggregate result in `outputs/{cohort_id}/pulse-{YYYY-MM-DD}-results.md`
- Four stakeholder summaries in `outputs/{cohort_id}/pulse-{YYYY-MM-DD}-{audience}.md`
- A documented change-in-response in `outputs/{cohort_id}/pulse-{YYYY-MM-DD}-action.md`

## Decision Points
- If a single learner's free-text is identifiable (small cohort, distinct phrasing), redact or summarize before sharing.
- If a manager is named negatively in free text, do not surface to the manager. Take it to the facilitator + the L&D admin.
- If results contradict the facilitator's read of the room, trust the cohort and adjust; the facilitator's read is one data point, not the truth.
- If the cohort is <8 learners, drop Likert distributions in favor of qualitative themes — small-N statistics mislead.
