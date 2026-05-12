# Executive Sponsor Quarterly Readout — Ongoing-Program Cadence

## Purpose
Use this prompt for ongoing programs (multiple cohorts per quarter or year) to produce the rolled-up quarterly sponsor readout. The single-cohort `/sponsor-readout` is the input; this prompt aggregates across cohorts and quarters.

## Prerequisites
- All single-cohort readouts from the quarter under review, in `outputs/`
- A baseline target set for the program (Level 1–4 thresholds from `context/project.md`)
- The sponsor's prior readout to compare against
- Permission to anonymize learner artifacts at the program level

## Prompt Template

Generate the quarterly executive readout for {{program_name}} — period {{Qx_YYYY}}. The readout aggregates {{n_cohorts}} cohorts and {{n_learners}} total learners. Use a Kirkpatrick-aligned narrative; the sponsor reads at the executive summary first.

### Section 1 — Executive Summary (≤80 words)
Three bullets:
- Volume + reach: cohorts, learners, completion %, NPS
- Behavior signal: the strongest D+30 evidence across the quarter — one sentence
- Decision asked: the one question this readout puts to the sponsor (continue / scale / adjust / stop)

### Section 2 — Program Health by Kirkpatrick Level (one paragraph each)
- **Level 1 — Reaction:** rolled-up pulse, NPS, one anonymized quote from the strongest cohort and one from the weakest
- **Level 2 — Learning:** pre/post delta range across cohorts; any cohort that under-performed and why
- **Level 3 — Behavior:** the most concrete D+30 evidence; one named application story (with consent); the rate of manager-observed change
- **Level 4 — Results:** the business metric with quarterly trend; explicit attribution caveat

### Section 3 — Cohort Comparisons
A small table — five columns max:

| Cohort | Completion | Pulse mean | D+30 behavior signal | Notes |
|--------|-----------|-----------|---------------------|-------|
| ... | ... | ... | ... | ... |

Notes column carries the *why* — facilitator change, pilot variant, special audience.

### Section 4 — What Worked, What Didn't
Two short lists. Each item:
- The change made
- The signal it moved (or didn't)
- Whether to keep it for next quarter

### Section 5 — Recommendations
Three bullets max. Each is a specific decision with an owner and a by-when.

### Section 6 — Risks Surfaced
The risks the sponsor should know about — capacity, regulatory, competitive, talent. Each risk has a mitigation owner.

### Section 7 — Appendix
- Methodology notes (how Level 3 was measured; attribution caveats for Level 4)
- Source data files (linked to `outputs/` paths)
- Pre-brief notes from the chief of staff
- Version history of this readout

### Render Conventions
- Length target: 2 pages of body + appendix. Sponsors do not read 6-page readouts.
- Visuals capped at four: completion trend, pulse trend, one Level 3 artifact image (anonymized), one Level 4 metric chart with confidence interval
- Plain language; no jargon without a one-line gloss
- Every claim of attribution is flagged with confidence (low / medium / high)
- The "decision asked" is restated identically in the executive summary and the recommendations block — same wording, same metric

## Expected Output

`outputs/quarterly-readouts/{Qx_YYYY}-readout.md` with the seven sections above, plus:
- A 60-word email body (`post-sponsor-recap-email`) referencing the artifact and the one decision asked
- A 5-min Loom script for the facilitator-to-sponsor message
- A pre-brief note for the chief of staff in `outputs/quarterly-readouts/{Qx_YYYY}-prebrief.md`

## Decision Points
- If the program performance is mixed (some cohorts strong, some weak), do not flatten. Surface the variance with the named cause; that is the most useful signal to the sponsor.
- If the program is being asked to scale, the readout is also a capacity argument — include a "to scale to {{Y}} learners we will need {{capacity}}" block.
- If the readout shows a stop recommendation, draft the alternative (where the budget should go) before sharing the recommendation.
- If a particular learner artifact is exceptional and the learner will consent to attribution, ask permission rather than anonymizing — named success stories carry more weight with executives than anonymized ones.
