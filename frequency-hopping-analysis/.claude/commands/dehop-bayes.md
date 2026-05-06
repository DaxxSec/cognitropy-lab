# /dehop-bayes — Bayesian Dehopper

Run the Bayesian dehopper on an IQ capture: produce a per-dwell channel posterior, a Viterbi MAP path, and a dehopped baseband stream ready for downstream demodulation.

## Inputs

- IQ capture (with SigMF metadata)
- Hop-set prior (from `/hop-set-prior`, or auto-built if missing)
- Hop rate posterior (from `/hop-detect`)
- Optional: `--seq <type>` to constrain sequence type (`pn`, `table`, `afh`, `unknown`)

## Steps

### 1. Validate inputs
- Capture has SigMF; sample rate sufficient for the hop set (channel BW × K ≤ sample rate).
- Hop-rate CI from `/hop-detect` is < 10% of mean. If wider, recommend running `/hop-detect` on a longer capture first.

### 2. Channelize
- Build a polyphase filterbank with `K` channels matching the prior's channel grid.
- Filter design: 1024-tap Hanning-windowed prototype, ≥ 60 dB sidelobe rejection.
- Output: `channels[t, k]` complex IQ at the channel sample rate (= sample_rate / K).

### 3. Energy detector
- Compute `e[t, k] = |channels[t, k]|^2` integrated over a window of `0.8 * dwell_estimate` samples.
- Estimate `λ_signal` and `λ_noise` from quiet/loud regions of the capture.

### 4. Forward-backward inference
- For each dwell window `t`, compute likelihood `L[t, k] = p(e[t, :] | c_t = k, θ)` using the Exponential model from `domain-knowledge.md` §3.2.
- Run forward-backward HMM smoothing with the hop-set prior as the per-step prior and either:
  - Uniform transition matrix if `--seq unknown`
  - Markov kernel `A_AFH` if `--seq afh` (estimate kernel from data)
  - Deterministic transition `c_{t+1} = f(seed, t+1)` if `--seq pn` or `table` (enumerate seeds)

### 5. Viterbi MAP path
- After forward-backward gives marginals, also compute the global MAP path over `(c_1, ..., c_T)` via Viterbi.
- The MAP path is what gets used to dehop the IQ stream.

### 6. Hyperparameter inference
- Fix MAP path; run PyMC NUTS over `θ = (R_h, T_d, T_g, K)` with the channel-energy likelihood marginalising over per-dwell channel.
- Report posterior with 95% CIs.

### 7. Build dehopped IQ stream
- For each dwell `t`, take the per-channel IQ slice `channels[t, c_t^MAP]`.
- Concatenate into a single-channel IQ stream at channel sample rate.
- Write `outputs/<engagement>/dehopped.iq` and a SigMF sidecar.

### 8. Diagnostics
- Per-dwell posterior entropy. High-entropy dwells → low confidence; mark them in a quality mask.
- Posterior predictive check: simulate energies from the model and compare to observed.
- If posterior predictive divergence > threshold (default KL > 0.5), warn that the model may be misspecified.

### 9. Output

Write `outputs/<engagement>/dehop/`:
- `posterior.npz` — full forward-backward marginals
- `channel_path.npy` — MAP per-dwell channel index
- `quality_mask.npy` — per-dwell confidence (1 - entropy / log K)
- `dehopped.iq` + `dehopped.sigmf-meta`
- `hyperparameter_posterior.nc` (arviz NetCDF)
- `figs/spectrogram_with_path.png`
- `figs/posterior_corner.png`
- `summary.json` — high-level numbers (hop rate posterior, dwell, K, posterior coverage)

## Output

A fully dehopped IQ stream with per-dwell quality mask, ready for `/sequence-id` or downstream protocol decoding (URH, rtl_433, custom GR flowgraph).

## Failure handling

If the posterior predictive check fails:
1. Try `--seq unknown` if you used a constrained type — maybe the system isn't what you thought.
2. Try a different channelization (offset boundaries by 1/2 channel BW) to rule out leakage.
3. Try a shorter integration window to rule out adaptive hopping mid-capture.
4. If all fail, mark the engagement "not recoverable from this capture" and recommend a longer capture or a different SDR.
