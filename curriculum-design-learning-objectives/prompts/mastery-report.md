# Prompt — Learner / Cohort Mastery Report

## Purpose
Generate a clear mastery report from posterior probabilities — per-objective `P(mastery)` with
credible intervals and recommended next steps — for a learner or a whole cohort.

## Prompt Template
```
You are reporting mastery from a Bayesian assessment model. Report probabilities and intervals,
never raw quiz percentages.

Inputs:
- Posteriors per objective: {{OBJECTIVE_POSTERIORS}}   # mean + credible interval + evidence count
- Skill graph: {{SKILL_GRAPH}}
- Decision rule: {{THRESHOLD_AND_CI_FLOOR}}
- Scope: {{LEARNER_OR_COHORT}}

Produce:
1. A per-objective table: P(mastery), credible interval, evidence count, status
   (MET / MORE-PRACTICE / NOT-MET).
2. For a cohort: the distribution of mastery per objective and which objectives the cohort is
   stuck on (lowest mean / widest interval).
3. Recommended next steps, routed through the skill graph (advance vs. re-teach a prerequisite).
4. A caveats line: objectives with thin evidence (wide interval) where the decision is tentative.
Keep uncertainty visible; do not collapse an interval to a single number.
```

## Expected Output
A mastery report (per-objective table + recommendations + caveats), suitable to share with an
instructor or learner, persisted to `outputs/`.
