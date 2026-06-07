# Rt Estimation Brief

## Purpose

A focused request to estimate the time-varying reproduction number correctly — the right date axis, a stated serial interval, no pre-smoothing, and an honest truncation caveat. Use when Rt is the specific deliverable.

## Prompt Template

```
Estimate the time-varying effective reproduction number for this series, avoiding the standard Rt pitfalls.

- **Series & path:** [file path; counts or line list]
- **Date axis available:** [onset / specimen / report — note if only report date]
- **Reporting delay:** [distribution / triangle available? deconvolve to onset?]
- **Serial / generation interval:** [mean, SD, parametric form, source]
- **Estimation window τ:** [default 7 days; or specify]
- **Population / sub-strata:** [if Rt is wanted by region/age/variant]
- **Snapshot date:** [data vintage]

Please:
1. Confirm/realign to the onset or infection date axis (deconvolve the delay if it's report date).
2. Nowcast the recent truncated window.
3. Discretise the serial interval and propagate its uncertainty.
4. Run EpiEstim/epyestim with window τ — do NOT pre-smooth the input.
5. Report Rt with 95% CrI, the last window whose CI excluded 1, and the truncation caveat.
6. Flag if EpiNow2 (joint delay + nowcast + Rt) would be the more appropriate tool here and why.
```

## Expected Output

- Rt time series with CrI ribbon and the Rt=1 reference.
- The serial interval, window, and date axis used (stated explicitly).
- The date the CI last crossed 1, with the right-truncation caveat on the final window.
- A note on whether bare EpiEstim or full EpiNow2 was the right choice given the delays.
