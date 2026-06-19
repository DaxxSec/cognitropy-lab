# /aberration-audit

Catalog the link's impairments as their **optical-aberration analogs** and quantify each as an implementation-loss in dB. An ideal modem produces a diffraction-limited constellation; real hardware smears it the way real glass smears a point-spread function. This command finds which "aberration" is costing the most Strehl and is therefore the cheapest to correct.

## Inputs

- Measured or specified impairments: oscillator phase noise (dBc/Hz mask), group-delay / amplitude ripple, IQ gain/phase imbalance, carrier-frequency and Doppler-rate error, ADC quantization/clipping, nonlinear AM/AM & AM/PM (HPA backoff), adjacent/co-channel interference, scintillation index
- The modulation order and symbol rate (sensitivity scales with both)
- Optionally a measured EVM (%) or constellation capture

## Steps

1. Map each impairment to its aberration analog (see the crosswalk in `context/references.md`): phase noise ↔ **spherical aberration** (symmetric blur of every symbol), group-delay ripple ↔ **coma** (asymmetric ISI tails), IQ imbalance ↔ **astigmatism** (axis-dependent stretch), rain/gas absorption ↔ **extinction**, scintillation ↔ **atmospheric seeing**, HPA nonlinearity ↔ **field-dependent distortion**, frequency offset ↔ **defocus**.
2. Quantify each as an SNR/implementation-loss in dB at the operating point (e.g. integrate the phase-noise mask to an rms phase error → constellation EVM → dB; convert IQ imbalance to image rejection → dB).
3. Combine into a total **implementation loss** (sum the EVM-equivalent noise powers, not the dBs directly) and into an effective **Strehl** to hand back to `/shannon-gap`.
4. Rank aberrations by dB contribution; for each, name its corrector — the satcom analog of an aspheric element or AR coating (e.g. carrier-tracking loop, equalizer, digital predistortion, HPA backoff, IQ calibration, adaptive optics / fast steering for optical).
5. Estimate the **marginal $ / dB** of each corrector so `/aperture-tradeoff` can rank fixing an aberration against simply buying more aperture.

## Output

`outputs/links/<mission-id>/aberration-audit.md` — the impairment→aberration table with per-item dB, the total implementation loss, the resulting Strehl, and a ranked correction list with rough cost per dB recovered.

## Notes

- Combine impairments as **powers**, never by adding dB: two independent 1 dB losses are ≈ 1.8 dB combined for additive-noise-like terms, but phase-noise and additive-noise floors interact non-linearly near high-order MODCODs.
- The cheapest dB is often a *software* corrector (better carrier loop, an extra equalizer tap) — always price the digital fix before recommending a bigger dish.
