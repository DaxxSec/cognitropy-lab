# /jammer-flag — Bayesian Classifier for Jammer Activity

Detect narrowband, sweep, and follower-jammer interference inside an FHSS hop set. Each per-dwell decision is reported as a posterior; downstream tooling can threshold as appropriate.

## Inputs

- IQ capture (with SigMF metadata)
- Hop-set prior or `channel_path.npy` (so the agent knows the legitimate channel grid)

## Steps

### 1. Build "expected" energy model
For the legitimate FHSS link, the expected per-channel energy is:
- High on `c_t^MAP` (legitimate dwell channel)
- Low elsewhere (just `λ_noise`)

Any deviation from this is candidate jammer activity.

### 2. Narrowband jammer detection
- Compute time-averaged energy per channel over the full capture: `\bar{e}_k`.
- Subtract the legitimate contribution: `\bar{e}_k^{adj} = \bar{e}_k - duty_k * λ_signal`, where `duty_k` is the fraction of dwells using channel `k`.
- Channels with `\bar{e}_k^{adj}` significantly above noise floor → narrowband jammer candidates.
- Bayesian test: `P(channel_k jammed | data) = ...` using a Gamma likelihood on the residual energy.

### 3. Sweep jammer detection
- Take an FFT of `\bar{e}_k(t)` (energy on each channel as a function of time).
- A sweep jammer produces a spectral peak at the sweep period.
- Bayesian test: posterior over `(sweep_rate, sweep_bandwidth)`. If posterior on `sweep_rate > 0` has > 0.7 mass, flag.

### 4. Follower jammer detection
Hardest of the three. Indicators:
- Energy on `c_t^MAP` shows a *bimodal* SNR distribution: legitimate burst at start of dwell, jammer at end.
- Per-dwell SNR ratios (start half / end half) cluster bimodally.
- Time-frequency characteristic: jammer follows the hop with a 10–100 µs delay.

Bayesian test: Gaussian mixture model on the start/end SNR ratio. Two components → follower jammer is suspected. One component → no follower.

### 5. Combined posterior
For each dwell `t`, output:
```
P(no jammer at t)
P(narrowband at channel k jamming dwell t)
P(sweep jammer crossing dwell t)
P(follower jammer at dwell t)
```

### 6. Output

Write `outputs/<engagement>/jammer-flag.json`:

```
{
  "narrowband_jammers": [
    {
      "channel_idx": 14,
      "freq_hz": 2416000000,
      "P_jammed": 0.93,
      "estimated_jammer_power_dbm": -52.1
    }
  ],
  "sweep_jammers": [],
  "follower_jammer_posterior": {
    "P_active": 0.04,
    "estimated_delay_us": null
  },
  "per_dwell_summary": {
    "dwells_with_any_jamming": 142,
    "total_dwells": 1598,
    "fraction_jammed": 0.089
  }
}
```

Plot a per-dwell jammer-activity heatmap to `outputs/<engagement>/figs/jammer-heatmap.png`.

### 7. Escalation

**Follower jammer detection is sensitive.** Active follower-jamming requires a sophisticated SDR-equipped adversary. If `P_active > 0.5`:
- Document in `work-log/`.
- Recommend the user notify the system operator and / or relevant CERT.
- Do not publish without operator review — false positives against AFH-adapting legitimate systems are common.

## Output

Per-dwell jammer posteriors and a summary classification. Hand to `/report-findings`.
