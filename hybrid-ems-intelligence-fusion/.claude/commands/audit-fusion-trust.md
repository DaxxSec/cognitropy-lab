# /audit-fusion-trust — Score Per-Source Reliability and Propose Trust Updates

Score each source against the realised drive (the ground truth), produce per-source reliability metrics, and emit a proposed trust-weight update for use by the next `/fuse-trip-prior` call.

## Inputs

- **Logged drive** — CAN + GPS + V2X + telematics traces for a completed drive (the realised ground truth).
- **Pre-drive prior** — the prior emitted by `/fuse-trip-prior` for this drive (with per-source breakdowns retained).
- **Per-source raw streams** — the inputs that fed the prior, time-aligned.
- **Current trust-weight table** — from `outputs/trust/<vehicle>-<region>.json` (or default uniform if absent).
- **Audit horizon** — typically single-drive, but supports rolling N-drive or full-fleet rollups.

## Steps

### 1. Compute Realised Power Demand
From the CAN log, compute the realised tractive + auxiliary power per sample using the same decomposition as `/fuse-trip-prior`:

`P_realised(s) = P_aero_actual(s) + P_roll(s) + P_grade_actual(s) + P_accel_actual(s) + P_aux_actual(s)`

This is the ground-truth signal each source was implicitly predicting.

### 2. Per-Source Residual Series
For each source, compute the residual between its per-sample prediction and the realised value:

`r_i(s) = μ_i(s) − P_realised(s)`

Aggregate residuals into:

- **Bias** — `mean(r_i)`.
- **RMS error** — `sqrt(mean(r_i²))`.
- **Calibration** — fraction of samples where `P_realised ∈ [μ_i − σ_i, μ_i + σ_i]`; ideal ≈ 0.68 for 1-σ band.
- **Regime breakdown** — same stats split by city / highway / mountain / cold-weather segments.

### 3. Detect Source-Specific Failure Patterns
- **Bias > 2 × RMS** — systematic offset; sign indicates direction. Fixable by recalibration.
- **Calibration < 0.5** — uncertainty is under-estimated. Source should report wider bands.
- **Calibration > 0.85** — uncertainty is over-estimated. Source is more reliable than it claims and is being effectively down-weighted by the fusion stack.
- **Regime-specific spikes** — source unreliable in city / mountain / cold conditions. Encode in regional/conditional trust weights.

### 4. Propose Trust-Weight Updates
Convert residual stats into a proposed update to the trust-weight table:

- Inverse-variance weight where calibration is good.
- Apply Bayesian update (`α=0.1–0.3` per drive) so a single anomalous drive doesn't crash the trust score.
- Emit per-region and per-regime overlays (e.g. lower trust for cloud traffic feed in fringe-coverage region).

### 5. Cross-Check Against `/source-conflict` Log
Sources flagged repeatedly by `/source-conflict` should align with low audit calibration. If a source is consistently conflict-flagged but audit-calibration is good, the gating threshold may be too tight (raise `z_gate`).

### 6. Persist
- Write per-source audit report to `outputs/audits/<vehicle>-<drive-id>.md`.
- Emit proposed trust-weight update to `outputs/trust/<vehicle>-<region>.proposed.json`.
- Do NOT auto-apply to the live trust table — require explicit operator acceptance for any weight change >20%.

## Output

Audit report in `outputs/audits/`, plus a proposed trust-weight delta in `outputs/trust/`. The report includes per-source bias, RMS, calibration, and regime breakdowns, plus a recommendation summary (`accept`, `accept_with_review`, `escalate`).

## Notes

- **Audit results lag the source's current state by the audit window.** If a source was recently re-calibrated upstream, recent drives are not representative; flag the audit as `pre_recal` and exclude or down-weight.
- **Bias and calibration are independent failures.** A source can be unbiased and badly calibrated, or biased but well-calibrated. Treat them as separate axes.
- **Don't roll up audits across vehicle variants without normalisation.** A V2X feed that's reliable for sedans may be unreliable for pickups in the same area because the sedans subscribe to a different city-side stream — keep variants separate.
