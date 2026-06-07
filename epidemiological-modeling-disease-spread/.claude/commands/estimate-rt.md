# /estimate-rt

Estimate the time-varying effective reproduction number Rt from an incidence series using the Cori instantaneous method (EpiEstim / epyestim), with a stated serial interval and an honest truncation caveat.

## Inputs

- Incidence series on the **onset or infection** date axis (run `/build-epicurve`, and `/nowcast` the tail, first).
- **Serial / generation interval**: mean, SD, and parametric form — or a discretised distribution (see `context/references.md`).
- Estimation **window** τ (days; default 7) and any window-uncertainty preference.
- Whether to propagate **serial-interval uncertainty** (recommended) and the count model (Poisson/NB).

## Steps

1. Read `context/workflows.md` "Workflow 1: Time-varying Rt estimation".
2. Confirm the date axis is onset/infection — if it is report date, deconvolve the delay or switch to EpiNow2.
3. Discretise the serial interval (`epitrix`+`distcrete` / epyestim) to the series' time step.
4. Configure EpiEstim `make_config` (`si_distr` or uncertain-SI with `mean_si`/`std_si` priors); set the sliding window τ.
5. Run `estimate_R`; obtain Rt with 95% credible intervals per window. **Do not pre-smooth the input series.**
6. Cross-check with `/growth-rate`'s r → Rt conversion on the exponential segment.
7. Flag the final window as right-truncation-sensitive; report the most recent window whose CI is fully above or below 1.
8. Write estimates + figure to `outputs/`.

## Output

`outputs/rt-<stream>-<snapshot-date>.md` + figure: Rt time series with CrI ribbon and the Rt=1 line, the serial interval and window used, the date the CI last crossed 1, the truncation caveat, and a one-line verdict (growing / plateau / declining + confidence).

## Notes

- Misspecifying the serial interval biases Rt: too short compresses toward 1, too long exaggerates swings. State the distribution every time.
- Estimating on report date instead of onset shifts Rt forward in time by the reporting delay — a classic error.
- Smoothing before EpiEstim distorts timing and intervals (Gostic et al. 2020); let the Bayesian window absorb noise.
- For substantial/variable delays, prefer **EpiNow2** (joint delay + nowcast + Rt) over bare EpiEstim.
