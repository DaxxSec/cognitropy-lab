# Regulatory Impact Memo

## Purpose

Use when a regulator (NHTSA, UNECE WP.29, EuroNCAP committee) proposes a threshold revision and the lab needs to estimate the impact across its historical test database — without re-running tests. The memo answers: "Under the proposed rule, what fraction of the lab's historical fleet would still pass, and with what posterior probability?"

## Prompt Template

```
You are the lab's regulatory liaison preparing a one-page memo to the regulator's docket. The memo must rest on Bayesian reanalysis of historical tests, not on point estimates.

Proposal:
- **Regulation:** [FMVSS_208 | UNECE_R94 | EuroNCAP_AOP | OTHER]
- **Threshold to revise:** [CRITERION_NAME] (e.g. chest deflection, HIC15, Nij)
- **Current threshold:** [VALUE_AND_UNIT]
- **Proposed threshold:** [VALUE_AND_UNIT]
- **Lab database scope:** [E.G. ALL_FRONTAL_RIGID_TESTS_2020_TO_2026]

Available analyses:
- `/regulation-compare` has been re-run for each historical test under both thresholds.
- Per-test posterior compliance probabilities are at [PATH_TO_RESULTS_BUNDLE].

Please:
1. State the posterior P(compliant | data) median and 5/95 percentile across the lab's historical fleet under the **current** threshold.
2. State the posterior P(compliant | data) median and 5/95 percentile under the **proposed** threshold.
3. Compute and report ΔP(compliant) — the regulatory-impact estimate. Whose fleet shifts most?
4. Identify the failure mechanism (which body region / criterion / occupant position) driving the impact.
5. Provide one paragraph of policy interpretation: is the threshold change capturing a real injury-risk gap, or is it shifting margins that the dummy / pulse noise already obscures?
```

## Expected Output

- Three numeric statements: P(comply | current), P(comply | proposed), ΔP, all as median [5/95].
- A named driver mechanism.
- One paragraph of interpretation grounded in the posterior comparison, not in editorial opinion.
- No claim that does not trace back to a per-test posterior in the bundle.
