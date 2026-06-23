# Emulsion Formula Review Prompt

## Purpose

Use this prompt to run a peer review of a submitted emulsion-sauce formula against the workspace rubric and issue an accept / revise / reject verdict with reasoning.

## Prompt Template

```
You are a reviewer on an emulsion-sauce peer-review panel. Review the formula below against the workspace rubric (stability, texture, flavour balance, reproducibility, safety). Be a skeptic, not a cheerleader.

I am submitting a formula for review:

- **Sauce / mother:** [mayonnaise / hollandaise / vinaigrette / daughter — name it]
- **Intended use:** [dip / dress / coat / hold-for-service]
- **Normalised formula:** [paste the ratio + baker's-% form, or the raw recipe to normalise first]
- **Egg source:** [pasteurised? raw?]
- **Process variables:** [oil-addition rate, shear method, temperature, total time]
- **Reproducibility evidence:** [how many preparers × replicates, with variable logs?]
- **Panel calibration status:** [calibrated? agreement statistic?]

Please:
1. Run the safety gate first; if it fails, stop and reject with the reason.
2. Score each rubric criterion and justify the score against an observable anchor.
3. Check the reproducibility gate (≥2 preparers × ≥2 replicates) — flag if unmet.
4. List graded defects (0–4) by class and apply the override rule.
5. Issue a verdict (sign-off / minor revise / major revise / reject) and, for any revise, the exact delta to re-test.
```

## Expected Output

- A safety-gate result (pass/fail with reason).
- A per-criterion rubric score table with justifications.
- A reproducibility-gate finding.
- A graded defect list and the override-rule outcome.
- A clear verdict with the scoped delta for re-review.
