# Domain Knowledge — Frequency Hopping Analysis with Bayesian Inference

This file is the agent's reference text on FHSS theory, Bayesian inference for hop-state recovery, and known reference systems. Read it on demand from CLAUDE.md; do not duplicate its content elsewhere.

## 1. FHSS Fundamentals

### 1.1 Definition

A frequency-hopping spread-spectrum (FHSS) system transmits a narrowband signal whose center frequency changes over time according to a known (to the legitimate receiver) hop sequence. Unlike direct-sequence spread spectrum (DSSS), the *instantaneous* signal is narrowband — only the time-averaged spectrum looks wide.

Key parameters:

- **Hop set** `F = {f_1, f_2, ..., f_K}` — the K candidate channel center frequencies.
- **Hop rate** `R_h` — hops per second.
- **Dwell time** `T_d ≈ 1 / R_h` (modulo guard intervals between hops).
- **Hop sequence** `c_1, c_2, ...` — `c_t ∈ {1..K}`, the channel index at dwell `t`.
- **Sequence type** — pseudo-random (PN), table-driven, adaptive (AFH), or unknown.

A receiver that cannot synchronise to the sequence sees, on any single channel, only `1/K` of the bursts and large gaps in between.

### 1.2 Why this matters for analysis

The fundamental observation is that **on a single channel, an FHSS signal looks like a low duty-cycle burst signal with the wrong timing**. Operators routinely misclassify FHSS as encrypted-fixed-frequency or as bursty-noise. The first job of this workspace is to get past that misclassification.

### 1.3 Common hop-set design choices

- **Channel spacing.** Typically equals the modulated bandwidth + guard band. Bluetooth = 1 MHz spacing, 1 MHz BW, 0 guard. WMBus mode N = 100 kHz spacing.
- **Channel count.** Constrained by the regulator-allocated band. Bluetooth uses 79 of 79 (full band). BLE uses 40, 37 of which carry data, 3 are advertisement-only.
- **Hop rate.** Regulators set floors and ceilings: FCC Part 15.247 demands minimum 50 ms / channel for non-AFH 2.4 GHz FHSS, fewer for "digitally modulated" systems.
- **Sequence design.** PN sequences (m-sequences, Gold codes) for cryptographic-style hopping; lookup tables (Bluetooth) for deterministic but pseudo-random-looking; AFH layers a "blacklist" on top to skip jammed channels.

## 2. Reference Systems

| System | Band | Hop set size K | Hop rate | Dwell | Sequence | Notes |
|--------|------|------:|---:|---:|---|---|
| Bluetooth Classic BR/EDR | 2.4 GHz ISM | 79 | 1600 hops/s | 625 µs | LAP-derived (deterministic given LAP, CLK) | Sequence reversible from any 32+ consecutive observations |
| Bluetooth Low Energy (BLE) data | 2.4 GHz ISM | 37 (data) + 3 (adv) | up to 1 hop/conn-event (~7.5 ms+) | ~1.25 ms minimum | hopIncrement (5–16) + AFH map | AFH map adapts to environment |
| WMBus mode N (smart meters EU) | 169 MHz | 8 | ~30 hops/s | 33 ms | Table-driven, periodic | Public spec |
| LoRa channel hopping (US 902–928) | 902–928 MHz | up to 64 channels | ~1 hop / 400 ms | 400 ms | Region-defined | Very slow; often misclassified as fixed |
| GMR-1 (sat phone) | L-band | varies | ~1.6 hops/s | 600 ms | Cryptographic | Out of scope: protected by Wiretap Act in US |
| SINCGARS (US Army VHF tactical) | 30–88 MHz | 2320 | 100 hops/s | 10 ms | Cryptographic | Out of scope without DOD authorisation |
| Honeywell wireless fire panels | 433/868 MHz | varies | ~10 hops/s | 100 ms | Proprietary, often weakly random | Public studies exist |

**Calibration target.** Bluetooth Classic in inquiry mode is the right calibration target: cheap to generate (any phone), parameters are public, the sequence is reversible, and `gr-bluetooth` provides ground truth. If your analyser does not recover the LAP and hop sequence on a Bluetooth Classic capture, it is broken — fix it before unknown captures.

## 3. Bayesian Model for Hop-State Recovery

### 3.1 Why Bayesian, not maximum-likelihood

Two hard cases break MLE:

1. **Partial observation.** With finite SDR bandwidth, you may only see `K' < K` of the channels at a time. MLE assigns zero likelihood to the unseen channels and erroneously reports the system uses only `K'`. A Bayesian prior with mass on "channel exists but was not in band" handles this naturally.
2. **Low SNR / collisions.** A burst at 6 dB SNR may be detected on the wrong channel due to spectral leakage. MLE on the raw detector picks the leakage channel; Bayesian inference, with a likelihood that models leakage explicitly, picks the correct one ~90% of the time.

The other reason: every parameter we report (hop rate, K, dwell) feeds downstream analysis. Reporting them as point estimates without uncertainty silently corrupts every later calculation. Posteriors with credibility intervals are the only honest interface.

### 3.2 Generative model

For dwell `t = 1..T`, candidate channel `k = 1..K`:

```
θ = (R_h, T_d, T_g, K)         ~ structured prior (see 3.3)
s ∈ {pn, table, afh, unknown}  ~ Categorical(prior over sequence types)
seed                           ~ uniform over seed space, conditioned on s
c_t                            = f(s, seed, t)             if s ∈ {pn, table}
                               ~ Markov(c_{t-1}, A_AFH)    if s = afh
                               ~ Uniform({1..K})           if s = unknown

For each (t, k):
    e_{t,k} ~ Exponential(λ_signal)  if c_t = k
            ~ Exponential(λ_noise)   else
    where (λ_signal, λ_noise) are estimated from quiet/loud portions of the capture
```

`e_{t,k}` is the channelizer's energy detector output for channel `k` in dwell window `t`. The Exponential model arises from squared magnitude of complex Gaussian noise (chi-squared with 2 dof = Exponential after scaling).

### 3.3 Priors

- **Hop rate `R_h`.** Log-uniform from 1 hop/s to 10⁵ hops/s by default. If the user specifies a target system, narrow this drastically (e.g. `R_h ~ Normal(1600, 50)` for Bluetooth).
- **Dwell `T_d`.** Soft constraint `T_d * R_h ∈ (0.5, 1.0)` (the rest is guard time). Beta prior on duty.
- **K.** Discrete uniform on `{2, 3, ..., 256}`. If the band is known (e.g. 2.4 GHz ISM), restrict to plausible values (79 for Bluetooth Classic, 40 for BLE, etc.).
- **Sequence type `s`.** `Categorical([0.4, 0.3, 0.2, 0.1])` for `[pn, table, afh, unknown]` is a reasonable uninformative starting point; updates as data arrives.
- **`(λ_signal, λ_noise)`.** Estimated up-front from a quiet (no-signal) portion of the capture and a known-loud portion. Treat as fixed during inference unless the capture is unstable.

### 3.4 Inference

Two layers:

1. **Per-dwell channel posterior** (`p(c_t | e_{t,:}, θ)`). For `s = unknown` and uniform prior on `c_t`, this is just the per-channel softmax of energies. For `s ∈ {pn, table, afh}`, it's a hidden-Markov forward-backward pass.
2. **Hyperparameter posterior** (`p(θ, s, seed | e)`). PyMC-driven NUTS for `θ`; explicit enumeration over `s` and (where small) `seed`; importance sampling otherwise.

The MAP path over `(c_1, ..., c_T)` is a Viterbi pass given the MAP `θ`. The marginal posterior on `c_t` is the forward-backward smoothed marginal.

### 3.5 Reporting

- Hop rate: posterior mean ± 95% CI.
- K: posterior mode + posterior over `K = K_mode ± 2`.
- Sequence type: posterior over the four-element categorical.
- Per-dwell channel: MAP path overlaid on a spectrogram, with low-confidence dwells flagged.
- Failure modes: if posterior is multimodal on `R_h` or `K`, *report all modes*. Multimodality usually means the capture was too short or the prior was wrong.

## 4. Channelization

The energy detector `e_{t,k}` requires channelizing the wideband IQ stream into `K` narrow channels at the same rate as the hop. Polyphase filterbank (PFB) is the right tool — it's mathematically equivalent to running K parallel mixers + low-pass filters, but ~K times cheaper.

Practical rules:

- Channel BW ≥ modulated BW + guard. For 1 MHz Bluetooth: 1 MHz channels at 1.05× decimation works.
- PFB taps: target sidelobe rejection ≥ 60 dB to avoid burst leakage between channels.
- Window: prefer Hanning or Blackman over rectangular; rectangular leakage is ~13 dB and creates ghost detections in adjacent channels.
- Integration window: align to expected dwell. Too short = noisy detection, too long = smears across hops.

If the actual hop rate is unknown, run the channelizer at a guess and check the posterior on `R_h`. If the posterior is sharply peaked, you guessed close enough; if it's spread out, re-run with a different integration window.

## 5. Common Failure Modes

### 5.1 Spectral leakage as "ghost hops"
If channel boundaries align with target channel boundaries by coincidence, signal energy spills into adjacent channels and the analyser sees two simultaneous "hops". Diagnosis: posterior over `c_t` is bimodal on adjacent channels for many dwells. Fix: re-channelize with offset boundaries (e.g. shift by 1/2 channel BW) — if the bimodality moves, it was leakage.

### 5.2 SDR clock drift faking a hop
A drifting LO can fake a slow hop if the drift rate matches the channel spacing. Diagnosis: hop pattern is monotonic in frequency over time. Fix: GPS-discipline the SDR, or include a phase reference (a known fixed-frequency tone in band) and subtract its drift.

### 5.3 Aliased hops outside SDR bandwidth
Captures that don't cover the full hop band see only a sub-set of channels. The posterior on `K` will be biased low. Symptom: posterior is peaked at a value that exactly matches the captured band's channel count. Fix: capture the full band or explicitly model "out-of-band" as one extra latent channel.

### 5.4 Collisions and missing dwells
Two hopping radios in the same band collide. The detector sees energy on two channels in one dwell window. The MAP path is wrong but high-confidence. Diagnosis: posterior entropy per dwell — high-entropy dwells are likely collisions. Fix: expand the model to two simultaneous latent emitters; posterior factorisation over `(c_t^A, c_t^B)`.

### 5.5 Adaptive hopping that adapts mid-capture
AFH systems update their channel blacklist every few seconds. A static `A_AFH` Markov kernel will mis-fit the second half of a long capture. Fix: time-varying kernel, or segment the capture and infer `A_AFH` per segment.

## 6. Adversarial / Jammer Detection

The same Bayesian framework extends to detecting hostile interference inside the hop set:

- **Narrowband jammer:** persistent energy on one or a few channels regardless of `c_t`. Likelihood ratio test: `p(e_{t,k} | c_t ≠ k, channel_jammed) / p(e_{t,k} | c_t ≠ k, normal)`.
- **Sweep jammer:** periodic energy that crosses many channels. Identifiable by FFT of `e_{t,k}` over time.
- **Follower jammer:** detects the legitimate hop, retransmits on the same channel with a delay. Identifiable by characteristic SNR pattern (legitimate burst at start of dwell, jammer at end) and by hop-set posterior anomalies.

The `/jammer-flag` command runs all three classifiers and reports per-dwell posteriors of jammer activity.

## 7. Information-Theoretic Limits

You cannot recover what is not in the capture. Hard limits:

- **K observable.** Capture must cover >= K-1 channels (one missing channel can be inferred; two cannot, in general).
- **Dwell observable.** Capture sample rate must give >= 4 samples/dwell to estimate dwell timing.
- **Sequence period.** To identify a sequence of period `P`, capture must cover >= 2P dwells (Nyquist for the sequence).
- **PN seed recovery.** Requires capture length and SNR sufficient to identify >= `2 * register_length` consecutive dwells correctly. Bluetooth's 28-bit hop input -> effectively need ~60 consecutive correct dwells. At 6 dB SNR, that means ~80–100 raw dwells.

Always report these limits in the findings — they are what tells the user why the recovered sequence is or is not predictive.

## 8. Tooling Cross-References

See `tools.md` for command-level integration with `gr-bluetooth`, `URH`, `Inspectrum`, and the workspace's PyMC inference code in `resources/bayesian-likelihood-models.md`.
