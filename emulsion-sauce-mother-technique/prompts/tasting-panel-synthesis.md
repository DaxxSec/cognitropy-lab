# Tasting Panel Synthesis Prompt

## Purpose

Use this prompt to turn raw blind-panel scores into a defensible sensory verdict — including whether the panel itself was reliable enough to trust.

## Prompt Template

```
You are synthesising blind tasting-panel data into review-ready evidence. Check panel reliability before interpreting preference; a difference from an uncalibrated panel is not evidence.

I have panel results to synthesise:

- **Test type:** [triangle / duo-trio / QDA descriptive / 9-point hedonic]
- **Samples & blinding:** [sample codes, single- or double-blind]
- **Reference / comparison:** [baseline mother or competing formula]
- **Raw data:** [paste picks/ratings per reviewer]
- **Panel calibration status:** [agreement statistic from last calibration]

Please:
1. Confirm the panel meets the agreement threshold; if not, flag the data as unreliable and stop.
2. Run the right analysis: binomial significance for discrimination, means + spread (+ agreement) for descriptive/hedonic.
3. State plainly whether the formulas are distinguishable, and if so, how and which is preferred.
4. Separate "detectably different" from "preferred" — report both, don't conflate them.
5. Give a one-line verdict the review round can cite.
```

## Expected Output

- A panel-reliability check (pass/fail with the statistic).
- The correct statistical analysis with the result.
- A clear distinguishability finding and, where valid, a preference finding.
- A citable one-line sensory verdict.
