# /dwell-estimate — Posterior on Dwell Time and Guard Intervals

Produce a posterior on dwell time `T_d` and guard interval `T_g` from a capture. Useful when `/dehop-bayes` succeeds but downstream demodulation fails — the channelization may be smearing across hops because the dwell estimate was off.

## Inputs

- IQ capture (with SigMF metadata)
- Optional: existing channel path from `/dehop-bayes`

## Steps

### 1. If a channel path exists, use it
- For each dwell `t`, find the start and end times by edge-detecting the energy on `c_t^MAP`.
- Each dwell yields one observation `(start_t, end_t)`.
- Aggregate into a posterior on `T_d` (the average dwell).

### 2. If no channel path, use auto-correlation
- Compute the auto-correlation of the wideband energy collapsed across channels.
- Sharp peaks at lag `τ` correspond to candidate `T_d`.
- Width of the peak gives an empirical CI.

### 3. Bayesian model
```
T_d ~ Gamma(α, β)            # weak prior; default α=2, β=0.001 → mean 2 ms
T_g ~ Beta(α, β) * T_d       # guard as fraction of dwell, default Beta(1,9) → ~10%
duty = T_d / (T_d + T_g)

For each observed (start, end):
    observed_dwell = end - start
    observed_dwell ~ Normal(T_d, jitter_sigma)
```

`jitter_sigma` is estimated from the spread across observed dwells.

### 4. Inference
- PyMC NUTS, 2000 samples, 1000 tune, 4 chains.
- Convergence: R-hat < 1.01, ESS > 400.

### 5. Outputs

Write `outputs/<engagement>/dwell-estimate.json`:

```
{
  "T_d_posterior": {"mean_us": 624.8, "ci_95": [621.2, 628.4]},
  "T_g_posterior": {"mean_us": 0.0, "ci_95": [0.0, 0.5]},
  "duty_posterior": {"mean": 1.0, "ci_95": [0.998, 1.0]},
  "jitter_sigma_us": 0.6,
  "n_observed_dwells": 1598,
  "notes": "Calibration capture; matches Bluetooth Classic 625 µs dwell."
}
```

### 6. Diagnostics
- Plot posterior corner plot in `outputs/<engagement>/figs/dwell-corner.png`.
- Plot histogram of observed dwells with posterior overlay.
- Flag if `duty_posterior.mean < 0.5` — the system has substantial guard intervals (uncommon for civil systems; possible for adaptive / mil-style).

## Output

A posterior on dwell timing. Used by `/dehop-bayes` to set the channelizer integration window correctly on a re-run. If this command's posterior CI is much tighter than the one from `/hop-detect`, re-run `/dehop-bayes` with the tighter dwell to get a cleaner per-dwell channel path.
