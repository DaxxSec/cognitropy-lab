# Prompt — Rewrite a Vague Objective into a Bayesian-Evidenceable One

## Purpose
Turn a fuzzy, non-observable objective ("understand recursion") into a measurable objective that
carries a prior and a defined evidence model, so it can be assessed Bayesianly.

## Prompt Template
```
You are an instructional designer using evidence-centered, Bayesian assessment.

Rewrite this objective so it is measurable and evidenceable:
  "{{VAGUE_OBJECTIVE}}"

Cohort / context: {{COHORT_CONTEXT}}
Intended Bloom level: {{BLOOM_LEVEL}}

Produce:
1. The rewritten objective in ABCD form (Audience, Behavior=observable verb, Condition, Degree),
   where the Degree is a threshold a posterior can clear.
2. The Bloom level and why the verb matches it.
3. 1–2 assessment item sketches that elicit that exact level, each with a starting slip and guess
   estimate (P(wrong|mastered), P(right|¬mastered)).
4. A starting prior Beta(α, β) with a one-line justification and its source type.
Reject any verb that is not observable; explain the replacement.
```

## Expected Output
A measurable ABCD objective, its Bloom level, aligned item sketches with slip/guess, and a
justified Beta prior — ready to drop into `/build-skill-graph` and `/map-evidence`.
