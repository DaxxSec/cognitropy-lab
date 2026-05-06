# /hop-detect — Detect FHSS Activity in a Capture

Decide whether a wideband IQ capture is hopping, fixed, or noise-only, and produce a posterior on hop rate. This is the cheap triage pass that runs first on every new capture.

## Inputs

- IQ capture path (with SigMF metadata)
- Optional: `--prior <system>` to pin a known target (e.g. `bluetooth-classic`, `ble`, `wmbus-n`)

## Steps

### 1. Load and inspect the capture
- Read SigMF metadata; verify sample rate and center frequency.
- Reject if no SigMF sidecar — instruct the user to populate it.
- Compute total duration and storage; warn if < 100 ms (likely too short).

### 2. Estimate noise floor
- Take the first 10 ms of the capture.
- If the user has annotated a quiet region in SigMF, use that instead.
- Compute per-channel `λ_noise` from FFT bins.

### 3. Wideband activity FFT
- 1024-point FFT, 50% overlap, full duration.
- Compute time-frequency energy matrix.
- Plot a quick spectrogram into `outputs/<engagement>/figs/quick-spectrogram.png`.

### 4. Hopping-vs-fixed discrimination
Two-hypothesis Bayesian test:
- `H_fixed`: signal energy concentrated on one or a few channels for the entire capture.
- `H_hopping`: signal energy alternates between channels at some rate.

Likelihood under each hypothesis: per-channel duty cycle distribution. Under `H_fixed`, expect `duty(top-channel) > 0.7`. Under `H_hopping`, expect `duty(top-channel) ≈ 1/K` for `K` candidate channels.

Compute `P(H_hopping | data)` and `P(H_fixed | data)` with a flat prior over hypotheses (or user-supplied prior).

### 5. Hop rate posterior
If `P(H_hopping) > 0.3`:
- Compute autocorrelation of the time-frequency energy matrix collapsed across channels.
- Peaks in the autocorrelation at lag `τ` correspond to candidate hop periods `T_d = τ`.
- Use the autocorrelation peaks as initial samples; run NUTS in PyMC over `R_h ~ log-uniform(0, 5)` with the channel-energy likelihood.
- Report posterior mean ± 95% CI.

### 6. Output

Write to `outputs/<engagement>/hop-detect.json`:

```
{
  "capture": "...",
  "P_hopping": 0.94,
  "P_fixed": 0.05,
  "P_unclear": 0.01,
  "hop_rate_posterior": {
    "mean": 1601.3,
    "median": 1600.8,
    "ci_lower_95": 1592.1,
    "ci_upper_95": 1610.2,
    "mode_count": 1
  },
  "duty_estimate": 0.998,
  "notes": "..."
}
```

Append a line to `work-log/<date>.md`. If `P_hopping` is in [0.3, 0.7] (uncertain), emit a warning recommending a longer capture.

## Output

A posterior on whether the capture is hopping and, if so, on hop rate. Hands off to `/hop-set-prior` and `/dehop-bayes` when confidence > 0.9.
