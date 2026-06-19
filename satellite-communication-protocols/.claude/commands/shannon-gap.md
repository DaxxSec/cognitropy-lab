# /shannon-gap

Compute the link's **Strehl ratio** — its achieved spectral efficiency divided by the theoretical Shannon ceiling for the same SNR and bandwidth. In optics, Strehl is the achieved peak intensity over the diffraction-limited ideal; here it is achieved bits/Hz over the information-theoretic ideal. A perfect modem sits near 1.0; every dB you bleed to impairments drops it.

## Inputs

- The computed `C/N` (or Es/N₀) from `/cascade-budget`
- Allocated bandwidth `B` and symbol rate `R_s`
- The current MODCOD: modulation order, code rate → achieved spectral efficiency `η_ach` (bits/s/Hz)
- The implementation-loss total from `/aberration-audit` (dB)

## Steps

1. Compute the Shannon ceiling: `C_shannon = B·log₂(1 + SNR)`, and the ideal spectral efficiency `η_max = log₂(1 + SNR)` (bits/s/Hz). Use linear SNR; convert from C/N in dB.
2. Compute the **capacity Strehl**: `S = η_ach / η_max`. Report it as a fraction and as the equivalent dB gap from capacity.
3. Compute the **Shannon-limit Eb/N₀**: at the achieved efficiency, the minimum Eb/N₀ is `(2^η − 1)/η`. Compare to the link's actual Eb/N₀ → this is the dB-from-Shannon for the chosen efficiency.
4. Attribute the gap: split the total shortfall into (a) **coding gap** (how far the FEC is from capacity-achieving — modern LDPC/turbo ≈ 0.7–1.5 dB) and (b) **implementation loss** (the `/aberration-audit` aberrations). Rank the impairment contributors by dB.
5. State the regime: **power-limited** (η_max ≫ η_ach, SNR is scarce — buy aperture/power) vs **bandwidth-limited** (η near the ceiling, SNR plentiful — buy bandwidth or higher-order modulation). The regime dictates which lever cost-benefit will favor.

## Output

`outputs/links/<mission-id>/shannon-gap.md` — the Strehl ratio, the dB-from-capacity, the coding-vs-implementation split, the limiting regime, and a one-line recommendation of where the cheapest dB lives.

## Notes

- A Strehl far below 1 isn't always bad — at very low SNR the *absolute* bits gained from closing the gap may be tiny. Always read the gap together with `/cascade-budget`'s margin and the cost-benefit in `/modcod-pareto`.
- The Maréchal criterion (optics: Strehl > 0.8 ↔ RMS wavefront error < λ/14) is the mental anchor: a "diffraction-limited" link keeps total implementation loss under ~1 dB. Above that, an aberration is dominating — go find it.
