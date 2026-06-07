# Aberration Investigation

## Purpose

Use when a routine-surveillance signal has been flagged (by `/detect-aberration` or a public dashboard) and you need to decide whether it is a genuine emerging outbreak, a seasonal expectation, or a data artifact.

## Prompt Template

```
A surveillance signal has been flagged as anomalous. Investigate whether it's a real aberration.

- **Disease / syndrome:** [notifiable disease, syndromic indicator]
- **Series & path:** [recent counts + historical baseline data]
- **Flagged period:** [which week(s)/day(s) and observed vs expected if known]
- **History depth:** [years of baseline; established vs novel disease]
- **Known confounders:** [recent reporting changes, lab onboarding, holidays, a new case definition]
- **Strata:** [is the signal in a specific region/age/setting?]

Please:
1. Rebuild the baseline (exclude past outbreaks; account for seasonality + trend; negative-binomial).
2. Re-run the appropriate detector (Farrington for history / EARS for short baseline / CUSUM for drift) and confirm/deny the flag.
3. Decompose the recent series to separate the spike from day-of-week and seasonal structure.
4. Rule out data artifacts (reporting catch-up, duplicate records, definition change, small-cell volatility).
5. If the signal survives, characterise it: magnitude, onset, affected strata, and an Rt/growth read if counts permit.
6. Recommend an action triage: investigate / monitor / dismiss-as-artifact, with the reasoning.
```

## Expected Output

- A confirm/deny verdict on the flag, with observed-vs-expected and exceedance.
- The decomposition isolating the spike from artifacts.
- An artifact-rule-out checklist with findings.
- If real: a characterisation (size, timing, strata, early Rt) and an action recommendation with rationale.
