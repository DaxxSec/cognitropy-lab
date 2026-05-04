# /at-risk-outreach — Triggered Engagement Escalation

When an engagement signal trips a threshold, generate the right escalation chain — never a single coercive blast. The escalation defaults are autonomy-preserving and only escalate to manager/sponsor lanes after the lighter touches have had time to land.

## Required Inputs
- The signal: who, what, when, source. Examples:
  - `learner_id=L042 no_login_days=9`
  - `cohort=C14 module=3 submission_pct=58 (threshold 80)`
  - `learner_id=L007 pulse_score=2.4 free_text="schedule is impossible"`
- The context from `resources/engagement-metrics-reference.md` — layer, scope, severity
- Any known life-event or external context (e.g., learner on documented medical leave; org-wide incident)

## Steps

### 1. Classify the Signal
Look up the signal in `resources/engagement-metrics-reference.md`:
- **Layer**: Logistical / Behavioral / Cognitive / Affective
- **Scope**: individual / cohort / cross-cohort
- **Severity**: low / medium / high

A 7-day no-login from one learner is Logistical-individual-low. A 58% module submission rate cohort-wide is Behavioral-cohort-medium.

### 2. Check Suppression Conditions
Do not proceed if any of:
- Learner has a documented life event (bereavement, medical leave) — replace with a single human-authored note from the facilitator
- Org-wide incident in the same 72h window (outage, layoff, news event) — pause 48–72h
- The cohort is in a freeze window from the cadence calendar
- The signal might be confounded by a known content issue (cohort spike on the help channel)

### 3. Choose the Starting Message

| Layer | Scope | Severity | Starting message |
|-------|-------|----------|------------------|
| Logistical | Individual | Low | `trigger-learner-nudge-email` (light, autonomy-preserving) |
| Logistical | Individual | Medium | `trigger-learner-remind-email` + office-hours offer |
| Logistical | Cohort | Medium | Cohort-wide friendly check-in via Slack, not email |
| Behavioral | Individual | Low | `trigger-learner-nudge-slack` (DM, ≤80 words) |
| Behavioral | Individual | Medium | `trigger-learner-remind-email` + concrete recovery option |
| Behavioral | Cohort | Medium | `during-learner-pulse-email` to find the cause before nudging |
| Cognitive | Individual | Any | 1:1 conversation prompt to facilitator — not an automated send |
| Affective | Individual | High | Human-authored facilitator note only; do not auto-send |
| Affective | Cohort | High | Run `prompts/silent-cohort-revival.md` end-to-end |

### 4. Sequence the Chain

Default sequence for individual signals (adjust based on register and consent):

| Step | T+ | Action |
|------|----|--------|
| 1 | T+0 | Send the chosen learner-facing template via the chosen channel |
| 2 | T+72h | If no movement on the signal, re-attempt with a different format (Loom, peer-thread mention, calendar offer of office hours) |
| 3 | T+5–7 days | Only if Power-Interest scoring of manager allows AND consent permits: manager nudge with learner-CC; framing is supportive, never disciplinary |
| 4 | T+14 days | Only on persistent Definitive risk: sponsor flag framed as "perspective needed", not "your investment is at risk" |

For cohort-scope signals, replace Step 1 with a cohort-wide message and skip the manager step entirely; the manager lane is reserved for individual recovery.

### 5. Render Each Step
For each scheduled step:
- Pull the matching template from `resources/stakeholder-template-library.md`
- Render with cohort variables and the signal's specifics
- Apply the plain-language and one-ask checks
- Store in `outputs/{cohort_id}/at-risk-{learner_id_or_cohort}-{step}-{YYYY-MM-DD}.md`

### 6. Log Everything
For every step, write a single line to `work-log/<YYYY-MM-DD>.md`:
```
{{ISO_timestamp}} signal={{signal}} action={{template_id}} approver={{name}} status={{drafted|sent|paused}}
```

Privacy note: the work-log can be pseudonymized; do not paste full free-text quotes.

### 7. Watch the Response
- Re-poll the signal at the scheduled step times.
- If the signal recovers at step 1, do not advance the chain. Mark the file `recovered`.
- If the signal recovers at step 2 with a different format, archive the format that worked — it informs future cadence design.
- If the chain runs to step 4 without recovery, schedule a human-to-human conversation; the workspace's job ends, the relationship's begins.

### 8. Honor the Exit
Every triggered template includes a graceful exit — "If now isn't the right time, here's how to opt out of this nudge sequence." If a learner opts out, suspend automated outreach and log the opt-out.

## Output
- 1–4 rendered messages in `outputs/{cohort_id}/at-risk-*`
- Work-log entries per step
- A `at-risk-summary.md` per learner or cohort signal that documents the chain's outcome

## Decision Points
- If the same learner trips multiple signals in a week (no login + missed assignment + low pulse), do not stack three chains. Run one combined human conversation.
- If the manager step is permitted but the manager is geographically remote with low time-zone overlap, switch the channel to email-only with a specific 1:1 prompt.
- If consent for manager-CC is unclear, default to no-CC and surface the consent question before advancing.
- If the signal's source is unreliable (LMS analytics partial outage, bounced email), pause the chain and verify the signal first.
