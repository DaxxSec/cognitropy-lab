# Engagement Metrics Reference

Signals, sources, polling cadences, default thresholds, and the layer they observe. Templates and triggered chains route off this table.

> Layer = where the signal lives in the four-layer model from `context/for-agent/domain-knowledge.md`: Logistical / Behavioral / Cognitive / Affective.

## Signal Catalog

### Logistical

| Signal | Source | Cadence | Default trigger |
|--------|--------|---------|-----------------|
| Login frequency (individual) | LMS analytics | Daily | No login > 7 days during active phase |
| Login frequency (cohort) | LMS analytics | Daily | <60% of cohort logged in within last 7 days |
| Asset open rate | LMS / video host | Per asset | <60% of cohort opened the recap asset within 72h |
| Pre-work completion | LMS | Pre-launch | <70% completed by T-3 |
| Calendar accept rate | Calendar / LMS | Pre-launch | <80% accepted by T-3 |

### Behavioral

| Signal | Source | Cadence | Default trigger |
|--------|--------|---------|-----------------|
| Assignment submission (individual) | LMS | Per assignment | Missed at deadline + grace 24h |
| Assignment submission (cohort) | LMS | Per assignment | <80% on time |
| Live attendance (individual) | Conferencing platform | Per session | Missed two consecutive sessions |
| Live attendance (cohort) | Conferencing platform | Per session | <70% of cohort attended live |
| Forum post count (individual) | LMS / community platform | Weekly | Zero posts in two consecutive weeks |
| Forum post count (cohort) | LMS / community platform | Weekly | Cohort post count drops >40% week-over-week |
| Peer-review completion | LMS | Per peer-review window | <80% completed within deadline + 48h |
| On-time completion | LMS | Continuous | >2 missed deadlines individually |

### Cognitive

| Signal | Source | Cadence | Default trigger |
|--------|--------|---------|-----------------|
| Question quality | Forum thread review | Module-end | Threads stay declarative — no questions, no challenges |
| Reflection depth | Open-text artifact | Per artifact | Reflection length collapses to single sentences across cohort |
| Applied artifact quality | Rubric scoring | Module-end | Mean rubric score drops below pre-defined floor |
| Pre/post knowledge delta | Assessment | Pre + post | Delta < pre-defined Level 2 threshold |

### Affective

| Signal | Source | Cadence | Default trigger |
|--------|--------|---------|-----------------|
| Pulse mean | Survey tool | Pulse weeks | Cohort mean <3.5/5 |
| Pulse individual | Survey tool | Pulse weeks | Individual <3 with low text engagement |
| NPS / CSAT | Survey tool | Close + D+30 | NPS <0 or CSAT <80% |
| Free-text sentiment | Survey tool | Pulse weeks | Negative-affect themes appear >2x baseline |
| Help-channel sentiment | Slack/Teams | Daily | Frustration phrases spike (rule-based check; never sentiment-of-individual) |

## Threshold Tuning

Defaults above are starting points. Tune to:

- **Cohort size.** A 7-day no-login is meaningful for a 6-week cohort; for a 6-month program it might be a 21-day window.
- **Modality.** Async cohorts run 2–3x longer login windows than synchronous.
- **Audience seniority.** Senior leaders log in less by absolute count but show up live; weight live attendance higher in the routing table.
- **Holiday windows.** Suppress all logistical thresholds during cohort-relevant holidays; flag in calendar.

Document your tuned thresholds in `context/project.md` so the agent does not fall back to defaults.

## Severity Classification

For an individual signal, severity follows:

| Severity | Description | Default response cadence |
|---------|-------------|--------------------------|
| Low | Single signal slightly past threshold | T+0 light nudge; T+72h re-attempt with format change; stop |
| Medium | Signal well past threshold OR multiple low signals stacking | T+0 nudge; T+72h re-attempt; T+5–7d manager nudge if consent allows |
| High | Hard miss (no submission, two consecutive misses, pulse <2/5) OR Affective | T+0 human-authored facilitator note; no automated chain |

For cohort scope, the equivalent severity table:

| Severity | Description | Default response |
|---------|-------------|------------------|
| Low | Single cohort signal at threshold | Cohort-friendly Slack check-in |
| Medium | Two signals at threshold OR 1 well past | Run a one-question pulse + format change |
| High | Pulse mean <3, or attendance <50% for two sessions | Run `prompts/silent-cohort-revival.md` end-to-end |

## Source-Quality Caveats

Every signal has a known noise pattern. The agent should know them:

- **LMS login** does not equal engagement; learners can keep tabs open. Combine with asset-open or submission for confidence.
- **Live attendance** is influenced by time zone shifts, daylight savings, and personal-calendar patterns; weekly comparisons beat single-session reads.
- **Forum activity** is dominated by power posters; cohort-mean post counts mask the silent majority. Use median + active-poster ratio.
- **Pulse means** with N <8 are noise; report distribution and themes, not the mean.
- **Help-channel volume** can spike for content reasons (a broken video) — investigate root cause before nudging individuals.

## Confounders to Always Check Before Triggering

Before any `/at-risk-outreach` chain, confirm none of these:
- Public holiday or org-wide PTO window
- Org-wide incident (outage, layoff, news event) in the last 72h
- Known cohort-affecting event (a course-content release with known issues)
- Calendar freeze window from `context/constraints.md`
- The learner has a documented life event suspending outreach

If any apply, suppress the chain or pause for the documented period.

## Reporting Cadence (where signals show up to whom)

| Signal owner | Audience | Cadence | Format |
|--------------|----------|---------|--------|
| Producer | Facilitator | Daily | One-line dashboard summary |
| Facilitator | Internal cohort log | After every session | Recap log |
| L&D admin | Sponsor | Module + midpoint | Recap email + readout |
| L&D lead | Quarterly business review | Quarterly | Roll-up readout |

Build the dashboard once per cohort scale. Below ~50 learners a sheet is fine; above, invest in a Power BI / Looker / Tableau view.

## Privacy Floor

- Never share an individual learner's behavioral trace with their line manager without prior consent disclosed at enrollment.
- Aggregate at cohort or sub-cohort level for any sponsor or executive view; individual-level reporting requires named consent.
- Do not retain behavioral traces beyond the org policy; default to delete 12 months after cohort close.
- Pulse free-text is pseudonymized at aggregation; if a quote could identify the writer, paraphrase or omit.
- Do not use engagement signals as performance evidence for HR processes — that is a different consent regime.
