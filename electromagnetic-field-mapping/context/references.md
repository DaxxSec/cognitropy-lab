# Electromagnetic Field Mapping — References

Lookup data the agent reaches for during tasks. Compact by design — defer to upstream sources for fuller specs.

## ICNIRP 2020 Reference Levels (Whole-Body, Time-Averaged)

| Frequency | E (V/m) — General Public | E (V/m) — Occupational | H (A/m) — Gen. Public | S (W/m²) — Gen. Public |
|---|---|---|---|---|
| 0.1 – 30 MHz | 83 / √f_MHz | 167 / √f_MHz | 0.73 / f_MHz | — (use E,H) |
| 30 – 400 MHz | 27.7 | 61.4 | 0.073 | 2 |
| 400 – 2000 MHz | 1.375 · √f_MHz | 3 · √f_MHz | 0.0037 · √f_MHz | f_MHz / 200 |
| 2 – 300 GHz | 61.4 | 137 | 0.16 | 10 |

Averaging time: 30 minutes whole-body (general public, < 6 GHz), 6 minutes local (occupational, < 6 GHz), shorter above 6 GHz. Always check the standard for the body-zone partition.

## IEEE C95.1-2019 (Selected ERLs for Whole-Body, Unrestricted = Public)

| Frequency | E (V/m) | S (W/m²) | Avg time |
|---|---|---|---|
| 100 kHz – 1.34 MHz | 614 | — | 30 min |
| 1.34 – 30 MHz | 823 / f_MHz | — | 30 min |
| 30 – 300 MHz | 27.5 | 2 | 30 min |
| 300 – 3000 MHz | 1.585 · √f_MHz | f_MHz / 300 | 30 min |
| 3 – 30 GHz | 87 | 20 | 30 min |
| 30 – 100 GHz | 87 | 20 | adaptive |

Restricted-environment (= occupational) ERLs are ~3 – 5× higher. Use the standard tables; the above is an aide-mémoire.

## FCC OET-65 MPE (Selected; General Population / Uncontrolled)

| Frequency | E (V/m) | H (A/m) | S (mW/cm²) | Avg time |
|---|---|---|---|---|
| 0.3 – 1.34 MHz | 614 | 1.63 | (100) | 30 min |
| 1.34 – 30 MHz | 824/f | 2.19/f | 180/f² | 30 min |
| 30 – 300 MHz | 27.5 | 0.073 | 0.2 | 30 min |
| 300 – 1500 MHz | — | — | f/1500 | 30 min |
| 1.5 – 100 GHz | — | — | 1.0 | 30 min |

## Common Antenna Factors (Aide-Mémoire, Always Use Cal Curve)

| Antenna | Typical band | AF ranges (dB/m) |
|---|---|---|
| Biconical (e.g. ETS-Lindgren 3110B) | 30 – 300 MHz | 8 – 20 |
| Log-periodic (e.g. ETS 3148B) | 200 MHz – 3 GHz | 15 – 28 |
| Horn (e.g. R&S HF906) | 1 – 18 GHz | 22 – 36 |
| Discone (TSCM survey) | 25 – 3000 MHz | 12 – 30 |

## Probe Catalogue

| Probe | Type | Frequency | Notes |
|---|---|---|---|
| Narda NBM-550 + EHP-50 | Broadband isotropic E | 100 kHz – 6 GHz | Survey-grade, easy use |
| Narda ELT-400 | 3-axis ELF magnetic | 1 Hz – 30 kHz | Power-frequency safety |
| Narda EHP-200A | Wideband E + H | 9 kHz – 30 MHz | LF / MF coverage |
| Wandel & Goltermann EFA-300 | 3-axis B + E | 5 Hz – 32 kHz / 40 Hz – 32 kHz | Power-frequency |
| Beehive 100-series near-field H loops | H-field PCB | 30 MHz – 3 GHz | Diameters 6 mm / 12 mm / 25 mm |
| Beehive 100C E-field stub | E-field near | 30 MHz – 3 GHz | Voltage hot-spots |
| Rohde & Schwarz HZ-15 set | Near-field E + H | 100 kHz – 3 GHz | Bench EMC |

## Conversion Quick Reference

- 1 G (gauss) = 100 µT
- 1 µT (in air, far-field) ↔ ~0.8 A/m
- `E_dBµV/m = 20·log₁₀(E_V/m · 10⁶)`
- Plane-wave: `S [W/m²] = E² / 377 = 377 · H²`
- Plane-wave: `E [V/m] = 19.41 · √(S [mW/cm²])`

## EMI Mitigation Effectiveness (Typical Aide-Mémoire)

| Mitigation | Typical dB reduction | Frequency range |
|---|---|---|
| Snap-on ferrite (mix 31) | 6 – 15 dB | 1 – 300 MHz |
| Snap-on ferrite (mix 43) | 6 – 12 dB | 100 MHz – 1 GHz |
| Shielded cable (replacing unshielded) | 20 – 40 dB | broadband |
| Common-mode choke (board) | 20 – 30 dB | 30 MHz – 1 GHz |
| Conductive gasket on enclosure seam | 10 – 30 dB | 100 MHz – 18 GHz |
| Ventilation-aperture honeycomb | 20 – 60 dB | dependent on cell size |

## Upstream Standards and Resources

- **ICNIRP** — [icnirp.org](https://www.icnirp.org/) — RF (2020) and LF (2010) guideline PDFs.
- **IEEE Standards Store** — [standards.ieee.org](https://standards.ieee.org/) — C95.1, C95.6, 149.
- **FCC OET Bulletins** — [fcc.gov/general/oet-bulletins-line](https://www.fcc.gov/general/oet-bulletins-line) — OET-65, OET-69.
- **IEC Webstore** — [webstore.iec.ch](https://webstore.iec.ch/) — 62232, 61786, 60601-2-33.
- **CISPR (IEC)** — same store — CISPR 11, 16, 22, 32, 35.
- **ITU Radio Regulations** — [itu.int/pub/R-REG](https://www.itu.int/pub/R-REG-RR) — Article 5 allocation tables.
- **NIST EMF Calibration Services** — [nist.gov/calibrations](https://www.nist.gov/calibrations) — primary-standards traceability.
- **Sigidwiki** — [sigidwiki.com](https://www.sigidwiki.com/) — community signal-identification reference.

## Detector Cheat-Sheet (CISPR 16-1-1)

- **Peak** — instantaneous maximum; reads highest. TSCM, transient hunting.
- **Quasi-peak (QP)** — charge / discharge time constants weight by repetition rate (CISPR weighting). Default for EMC compliance < 1 GHz.
- **Average** — linear average over measurement bandwidth. Used alongside peak for FCC Part 15 Subpart C / B above 1 GHz.
- **RMS-Avg** — RMS detection then average over time. Common for RF-safety surveys.
