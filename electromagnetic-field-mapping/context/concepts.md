# Electromagnetic Field Mapping — Core Concepts

Background the agent should read before acting on tasks in this domain. Compact recall over exhaustive theory.

## Field Regions: Near and Far

A radiating source has three field regions, defined by distance `r` from the source, source largest dimension `D`, and wavelength `λ`:

| Region | Boundary | Behaviour | Probe choice |
|---|---|---|---|
| Reactive near-field | `r < λ / (2π)` | E and H not in plane-wave ratio; stored energy dominates | Separate E-field and H-field probes; isotropic broadband **fails** |
| Radiating near-field (Fresnel) | `λ/(2π) ≤ r < 2D²/λ` | Field shape still evolving; pattern not yet asymptotic | Calibrated near-field probe + spectral analyser |
| Far-field (Fraunhofer) | `r ≥ 2D²/λ` | Plane-wave: `E = η₀ · H`, `η₀ ≈ 377 Ω` | Antenna with calibrated antenna factor, or broadband isotropic |

For an idealised dipole (`D ≈ λ/2`), the far-field boundary is roughly `r ≥ λ/2`. For a 1 m parabolic at 24 GHz (`λ = 12.5 mm`), `2D²/λ ≈ 160 m`. The boundary scales linearly with `D²` — easy to underestimate for large-aperture transmitters.

## Field Quantities and Units

| Quantity | Symbol | SI unit | Common alt unit |
|---|---|---|---|
| Electric field strength | E | V/m | dBµV/m (`20·log₁₀(E [µV/m])`) |
| Magnetic field strength | H | A/m | (rare) |
| Magnetic flux density | B | T (tesla) | G (gauss), 1 G = 100 µT; mT for LF safety |
| Power density (far-field) | S | W/m² | mW/cm² (1 W/m² = 0.1 mW/cm²) |
| Specific Absorption Rate | SAR | W/kg | — |

In far-field RF: `S = E² / η₀ = η₀ · H²`. Useful sanity check: `27.7 V/m` ↔ `2 W/m²` ↔ `0.2 mW/cm²` (ICNIRP general-public level, 400 MHz – 2 GHz).

## Probe Taxonomy

- **Broadband isotropic E-field probe** (e.g. Narda EHP-50, NBM-550 + EHP probes) — survey-grade, integrates over a frequency band. Easy to use, low spatial resolution, no spectral information. Best for general-public RF safety in known transmitter environments.
- **Broadband isotropic H-field probe** — same but for magnetic field. Mandatory in the near-field of LF and ISM transmitters where E doesn't predict H.
- **3-axis ELF magnetic probe** (e.g. Narda ELT-400) — DC to ~30 kHz, calibrated for power-frequency magnetic surveys.
- **Calibrated antenna + spectrum analyser** — narrowband, frequency-resolved. Log-periodic (200 MHz – 3 GHz), biconical (30 – 300 MHz), horn (1 – 40 GHz), discone (broadband DF). Antenna factor `AF [dB/m]` converts measured `Vrx [dBµV]` to `E [dBµV/m]`: `E = Vrx + AF + cable_loss`.
- **Near-field loop probes** (H-field) — graduated diameters 5 mm / 10 mm / 30 mm for PCB-scale mapping. Orientation matters: loop normal selects the H-field component sampled.
- **Stub / dipole E-field near-field probes** — for finding voltage hot-spots over board traces and connectors.

## Detector Modes (for spectrum-analyser surveys)

| Detector | Use case |
|---|---|
| Peak | TSCM, transient hunting, identifying impulsive emitters |
| Quasi-peak (QP) | CISPR / FCC Part 15 emissions compliance — weights pulse repetition |
| RMS (root-mean-square) | RF safety surveys, thermal-zone limits, average-power-limited services |
| Average | Time-averaged emissions in narrower windows |

Modern CISPR 16-1-1 receivers offer all four — always document which was used.

## ISM / Common Allocation Highlights

| Band | Use | Typical sources to expect |
|---|---|---|
| 50 / 60 Hz | Mains | Transformers, wiring, motors — LF magnetic dominates |
| ~9 kHz – 150 kHz | Low-frequency ISM, AM longwave | Switching converters, inductive chargers |
| 13.56 MHz | RFID / NFC | Access cards, inductive heating |
| 27.12 MHz | ISM | Industrial heating, citizens band |
| 40.68 MHz | ISM | Industrial RF heating |
| 88 – 108 MHz | FM broadcast | High EIRP towers |
| 433.92 MHz | ISM (Europe) | Garage doors, key fobs, low-power telemetry |
| 868 MHz | ISM (Europe) / LoRa | IoT |
| 902 – 928 MHz | ISM (US) | LoRa, RFID, IoT |
| 2.40 – 2.50 GHz | ISM worldwide | Wi-Fi, Bluetooth, microwave ovens (leakage), cordless |
| 5.15 – 5.85 GHz | ISM / U-NII | Wi-Fi 5/6 |
| 5G NR n77/n78 (3.3 – 4.2 GHz) | Telecom | Mid-band cellular |
| 24 / 60 / 77 GHz | mmWave radar / 5G | Automotive radar, FWA, point-to-point |

Full plans: ITU Radio Regulations Article 5; national tables (FCC Part 2 Subpart B, Ofcom UK FAT, EU ECC ERC Report 25).

## Standards Landscape (Compliance)

| Standard | Frequency / scope | What it limits |
|---|---|---|
| ICNIRP 2020 RF Guidelines | 100 kHz – 300 GHz | Public + occupational E, H, S, SAR, energy density |
| ICNIRP 2010 LF Guidelines | 1 Hz – 100 kHz | Internal E-field (nerve stimulation) |
| IEEE Std C95.1-2019 | 0 Hz – 300 GHz | DRL (dosimetric reference) + ERL (exposure reference) |
| IEEE Std C95.6-2002 | 0 – 3 kHz | LF nerve stimulation |
| FCC OET-65 | 300 kHz – 100 GHz | MPE, restricted vs. unrestricted (≈ occupational vs. public) |
| IEC 62232 | RF base stations | Site survey methodology |
| IEC 61786-1 / -2 | DC / LF | Measurement procedures |
| CISPR 32 / EN 55032 | Multimedia equipment EMC | Emission limits 9 kHz – 6 GHz |
| FCC Part 15 / Part 18 | US emissions / ISM | Conducted + radiated limits |
| IEC 60601-2-33 | MRI | 5 G / 0.5 mT safety zones |

ICNIRP 2020 and IEEE C95.1-2019 mostly agree on values but differ in averaging, body-zone partitioning, and peak-power criteria. Always cite the edition that the survey is governed by.

## TSCM Signatures

Counter-surveillance scans look for emitters that don't appear in any allocation table or that present unusual duty cycles. Hallmarks of a covert / unauthorised emitter:

- Burst-modulated low duty cycle (audio is sent only when a voice is present).
- Off-band carrier just outside a popular ISM band (to dodge casual scans).
- Frequency-hopping over a band that wouldn't be used by consumer kit there.
- Disappearance when AC power to the room is cut (line-powered bug) — record before/after spectrum.
- Reaction to a "nonlinear junction" probe (active electronics show non-linear harmonics).

Detection of an authorised emitter (Wi-Fi AP, Bluetooth keyboard) is **not** a finding; cross-reference the allocation table first.

## Common Failure Modes

- **Wrong probe in the near-field** — using a broadband isotropic E-field probe inside `r < λ/(2π)` reports plausible-looking numbers that bear no relation to actual exposure.
- **Detector / averaging mismatch** — using peak detection on an RF-safety survey reads high; using average on a CISPR pre-compliance reads low. Both produce defensible-looking reports that fail re-test.
- **Polarization undersampling** — single-orientation reading on a circularly-polarised or cross-pol-dominant source misses up to 3 dB.
- **Calibration drift / lapsed cert** — probes drift; a 12-month-overdue cert invalidates the survey under most occupational programs.
- **Forgotten antenna factor** — far-field readings without `AF` correction can be off by 20 – 40 dB at the edges of the antenna's range.
- **Grid too coarse** — a lobe 2 m wide undersampled at 5 m spacing simply isn't on the map.
- **Cable common-mode contamination in EMC** — what looks like a PCB emitter is the cable acting as the antenna. Without a current clamp this is easy to misdiagnose.
- **Single-spot compliance verdict** — a survey is the spatial envelope, not the worst single sample's twin. Re-measure peaks before signing off.

## Operating Constraints

- **PPE and dosimetry for high-intensity work.** Personnel approaching active transmitters above the occupational limit need either dosimeters, time-in-zone protocols, or RF-protective suits. The agent surfaces this constraint; the safety officer enforces it.
- **Authorization to scan.** Property authorization is mandatory for safety surveys; signal-intercept law applies to TSCM (US: 18 USC §2511; UK: Investigatory Powers Act 2016; EU: ePrivacy Directive transpositions). Demodulating content of a captured signal is jurisdictionally limited — the workspace does **not** demodulate intercepted communications.
- **Reporting.** If the survey reveals an exposure overrun, occupational safety reporting law typically requires written notification within a defined window (OSHA / UK HSE / equivalent). Surface the deadline early.
