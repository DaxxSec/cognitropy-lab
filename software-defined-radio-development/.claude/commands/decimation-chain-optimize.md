# /decimation-chain-optimize

Optimize a multi-stage decimation / resampling chain for minimum compute at the target output rate.

## Inputs

- **Input sample rate** + **target output sample rate** (or rational resample ratio).
- **Passband + transition bandwidth + stopband attenuation** requirements.
- **Available compute budget** (cycles/sample or % of one core).
- **Constraints** — integer-only decimation? rational resample needed? latency ceiling?

## Steps

1. Read `context/concepts.md` "Multirate DSP" + `context/references.md` "Decimation cheat-sheet".
2. Compute the total decimation factor D = input_rate / output_rate; factor D into stages (e.g. D=200 → 10×5×4 or 8×5×5).
3. For each candidate factorization, estimate filter cost: a single-stage decimator needs a long filter at the input rate (expensive); a multi-stage chain lets early stages use short filters and later stages run at reduced rate (cheap).
4. Apply the standard multirate result — for large D, a cascade of 2-4 stages with the sharpest filter LAST (at the lowest rate) minimizes total multiply-accumulates.
5. Consider a CIC (Cascaded Integrator-Comb) first stage for very large D — multiplier-free, then compensate with an FIR cleanup filter.
6. Consider half-band filters for /2 stages — ~half the taps are zero, so ~2× cheaper.
7. Consider polyphase decomposition for rational resampling (P/Q).
8. Compute total MACs/sample for the optimized chain vs. the naive single-stage; report the speedup.
9. Write the optimized chain to `outputs/decimation/<chain-id>.md` with stage list, per-stage rate + taps, total compute, and GNU Radio block mapping.

## Output

A markdown decimation-chain spec at `outputs/decimation/<chain-id>.md` containing: factorization rationale, per-stage (decimation factor, filter type, tap count, sample rate, MACs/sample), total compute vs. naive baseline + speedup, GNU Radio block mapping (`rational_resampler`, `fir_filter_xxx`, `cic_decimator`, half-band), latency estimate.

## Decision points

- **If D is large (>50)** → CIC first stage + FIR compensation usually wins on compute.
- **If D has a large prime factor** → that stage is unavoidably costly; consider whether the target rate can be nudged to a more factorable ratio.
- **If latency matters more than compute** → fewer stages (shorter group delay) may beat the minimum-MAC chain.

## Notes

- The canonical result (Harris, *Multirate Signal Processing*): put the sharpest, longest filter at the LOWEST rate. Early stages do coarse decimation with cheap filters.
- Half-band filters are nearly free for /2 stages — exploit them whenever a factor of 2 appears.
- CIC droop must be compensated; budget for the FIR cleanup filter in the total.
- Always verify the optimized chain meets the original passband/stopband spec — a cheaper chain that fails the filter mask is not an optimization.
