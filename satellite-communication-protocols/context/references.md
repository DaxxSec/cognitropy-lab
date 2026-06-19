# Satellite Communication Protocols — Reference Tables

Compact lookup data for link design. Defer to ITU-R, CCSDS, and DVB specs for full detail.

## Frequency Bands (Earth–space)

| Band | Range (GHz) | Typical use | Rain susceptibility | Notes |
|------|-------------|-------------|---------------------|-------|
| L | 1–2 | MSS, GNSS, IoT | negligible | crowded, low rate |
| S | 2–4 | TT&C, NASA near-Earth | very low | |
| C | 4–8 | fixed satellite, broadcast | low | rain-robust, large dishes |
| X | 8–12 | military, gov, deep-space (8.4) | low | |
| Ku | 12–18 | DTH, VSAT, broadband | moderate | mainstream commercial |
| Ka | 26.5–40 | HTS broadband, feeders | high | wide bandwidth, needs ACM |
| Q/V | 33–75 | feeder links, future HTS | severe | diversity/ACM essential |
| Optical | ~193 THz (1550 nm) | ISL, feeders (FSO) | cloud = opaque | µrad beams, no licensing |

## DVB-S2X MODCOD Sample (AWGN, ~PER 1e-5)

| MODCOD | Spectral eff. (b/s/Hz) | Req. Es/N₀ (dB) | ≈ dB from Shannon |
|--------|------------------------|-----------------|-------------------|
| QPSK 1/4 | 0.49 | −2.85 | ~0.8 |
| QPSK 1/2 | 0.99 | 1.0 | ~0.8 |
| QPSK 3/4 | 1.49 | 4.03 | ~0.9 |
| 8PSK 3/4 | 2.23 | 7.91 | ~0.9 |
| 16APSK 3/4 | 2.97 | 10.21 | ~1.0 |
| 32APSK 3/4 | 3.70 | 12.73 | ~1.1 |
| 64APSK 5/6 | 4.93 | 16.05 | ~1.3 |

(Full table: 100+ points in DVB-S2X — this is a representative spine for Pareto sketches.)

## Aberration ↔ Impairment Crosswalk

| Optical aberration | Link impairment | Symptom on constellation | Corrector |
|--------------------|-----------------|--------------------------|-----------|
| Spherical | Oscillator phase noise | symmetric rotational blur | clean LO, carrier loop, pilots |
| Coma | Group-delay / amplitude ripple | ISI tails, asymmetry | linear equalizer |
| Astigmatism | IQ gain/phase imbalance | axis-dependent stretch | IQ calibration |
| Defocus | Carrier / Doppler offset | whole-constellation slip | frequency tracking |
| Field distortion | HPA AM/AM, AM/PM | outer-ring warp (APSK) | backoff, predistortion (DPD) |
| Extinction | Rain / gaseous absorption | uniform SNR loss + noise rise | margin, ACM, lower band |
| Atmospheric seeing | Scintillation | rapid fading | diversity, interleaving, "adaptive optics" |

## Key Equations Cheat-Sheet

| Quantity | Formula |
|----------|---------|
| Antenna gain | `G = η·(πD/λ)²` |
| −3 dB beamwidth | `θ ≈ 70·λ/D` (deg) ↔ diffraction `1.22 λ/D` (rad) |
| FSPL | `92.45 + 20log₁₀(d_km) + 20log₁₀(f_GHz)` dB |
| EIRP | `P_tx − L_feed + G_tx` (dBW) |
| Figure of merit | `G/T = G_rx − 10log₁₀(T_sys)` (dB/K) |
| Carrier-to-noise-density | `C/N₀ = EIRP − FSPL − L_atm + G/T + 228.6` (dB-Hz) |
| Shannon capacity | `C = B·log₂(1+SNR)`; `η_max = log₂(1+SNR)` |
| Shannon-limit Eb/N₀ | `(2^η − 1)/η`; → −1.59 dB as η→0 |
| Étendue (optics) | `G = n²·A·Ω` (conserved invariant) |
| Strehl (capacity) | `η_ach / η_max` |
| Rain specific atten. | `γ_R = k·R^α` (dB/km), ITU-R P.838 coeffs |
| Boltzmann | `k = −228.6 dBW/Hz/K` |

## Cost-Benefit Metrics

| Metric | Use |
|--------|-----|
| $ / dB | compare aperture vs power vs G/T vs software correctors |
| $ / bit (or /Mbps) | compare MODCOD points and CCM vs ACM |
| $ / nine | marginal cost of each availability step (convex) |
| dB-per-dollar | rank levers; buy from the top to the knee |
| Pareto frontier | non-dominated (efficiency, SNR) or (availability, cost) set |
| TCO / opportunity cost | static margin paid forever vs ACM/diversity lifetime cost |

## Upstream Catalogues & Standards

- **ITU-R P.618** — Earth-space propagation / rain attenuation — https://www.itu.int/rec/R-REC-P.618
- **ITU-R P.676 / P.840 / P.531** — gaseous, cloud, ionospheric scintillation — https://www.itu.int/rec/R-REC-P
- **ITU-R P.838** — rain specific-attenuation coefficients (k, α) — https://www.itu.int/rec/R-REC-P.838
- **DVB-S2X (ETSI EN 302 307-2)** — MODCOD/ACM standard — https://www.dvb.org/standards/dvb-s2x
- **CCSDS 401.0-B / 131.0-B / 141–142** — RF & modulation, channel coding, optical comms — https://public.ccsds.org
- **SatNOGS DB** — open satellite frequency/telemetry catalogue — https://db.satnogs.org
- **Smith, *Modern Optical Engineering*** — étendue, Strehl, aberrations, f-number (the optics half of the bridge)
