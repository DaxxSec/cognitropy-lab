# Prompt — Bayesian Curriculum A/B Evaluation Write-up

## Purpose
Write up a Bayesian comparison of a curriculum revision against the prior design — a posterior over
the effect, the ROPE decision, and the probability of improvement — in language a stakeholder can act on.

## Prompt Template
```
You are evaluating a curriculum revision with Bayesian methods. Do not report p-values; report the
posterior, the ROPE decision, and P(improvement).

Inputs:
- Outcome metric: {{OUTCOME_METRIC}}   # e.g. proportion of objectives met, mean posterior mastery
- Control (old design) data: {{CONTROL_DATA}}
- Treatment (revision) data: {{TREATMENT_DATA}}
- ROPE: {{ROPE}}

Produce:
1. The posterior over the effect size (state the prior and model used).
2. The credible interval and how it sits relative to the ROPE.
3. P(effect > 0) and P(effect outside ROPE, positive side).
4. Decision: ADOPT / PRACTICALLY-EQUIVALENT / INCONCLUSIVE, with one sentence of reasoning.
5. Confounds and caveats: cohort differences, attrition, multiple objectives, sample size.
Write for an instructional lead, not a statistician — but keep the numbers honest.
```

## Expected Output
A concise evaluation memo: posterior summary, CI-vs-ROPE, P(improvement), an explicit decision,
and caveats — saved to `outputs/eval-<revision>.md`.
