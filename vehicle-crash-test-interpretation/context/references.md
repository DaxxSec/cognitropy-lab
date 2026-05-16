# Vehicle Crash Test Interpretation — Reference Tables

Compact lookup data. Defer to upstream regulations and risk-curve papers for full derivations.

## Regulatory Thresholds — FMVSS 208 (Frontal Occupant Protection)

| Criterion | 50th Male | 5th Female | 6yo Child | 3yo Child |
|-----------|-----------|------------|-----------|-----------|
| HIC15 | ≤ 700 | ≤ 700 | ≤ 700 | ≤ 570 |
| HIC36 | ≤ 1000 | ≤ 1000 | — | — |
| Neck Nij | ≤ 1.0 | ≤ 1.0 | ≤ 1.0 | ≤ 1.0 |
| Neck Fz tension | ≤ 4170 N | ≤ 2620 N | ≤ 1490 N | ≤ 1130 N |
| Chest deflection | ≤ 63 mm | ≤ 52 mm | ≤ 40 mm | ≤ 34 mm |
| Chest accel 3 ms | ≤ 60 g | ≤ 60 g | ≤ 60 g | ≤ 55 g |
| Femur force | ≤ 10 kN | ≤ 6.8 kN | — | — |

## Regulatory Thresholds — UNECE R94 (Frontal Offset)

| Criterion | Threshold |
|-----------|-----------|
| HPC (Head Performance Criterion, ~HIC36) | ≤ 1000 |
| Neck shear (Fx) | ≤ 1.9 kN @ 0 ms, ≤ 1.2 kN @ 25–35 ms, ≤ 1.1 kN @ 45 ms |
| Neck tension (Fz) | ≤ 3.3 kN @ 0 ms, ≤ 2.9 kN @ 35 ms, ≤ 1.1 kN @ 60 ms |
| Neck moment My | ≤ 57 Nm extension |
| Thorax compression | ≤ 50 mm |
| Viscous criterion (V*C) | ≤ 1.0 m/s |
| Femur force | ≤ 9.07 kN @ 0 ms, ≤ 7.58 kN @ 10 ms |
| Tibia compression | ≤ 8 kN |
| Tibia index | ≤ 1.3 |

## CFC Filter Classes (SAE J211)

| Class | Frequency Response | Channels |
|-------|-------------------|----------|
| CFC 60 | -3 dB at 100 Hz | Vehicle structural acceleration (crash pulse) |
| CFC 180 | -3 dB at 300 Hz | Chest deflection, chest acceleration |
| CFC 600 | -3 dB at 1000 Hz | Belt forces, head acceleration for HIC |
| CFC 1000 | -3 dB at 1650 Hz | Neck loads, high-bandwidth head acceleration, femur force |

## Injury Risk Curves (Likelihoods)

| Body Region | Curve Family | Functional Form | Source |
|-------------|--------------|-----------------|--------|
| Head AIS 3+ | Mertz 2003 | P = Φ((ln HIC15 - 7.45) / 0.73) | SAE 2003-22-0009 |
| Head AIS 4+ | BrIC (THOR) | P = 1 - exp(-(BrIC/0.987)^2.84) | Takhounts 2013 |
| Neck | Eppinger Nij | P(AIS 3+) = 1/(1+exp(3.227 - 1.969·Nij)) | NHTSA 99-3960 |
| Chest AIS 3+ (Hybrid III) | Kuppa 2004 | P = 1/(1+exp(10.3 - 0.140·age - 0.122·defl_mm)) | NHTSA Kuppa Report |
| Chest AIS 3+ (THOR) | NHTSA THOR | P = 1/(1+exp(12.597 - 0.05861·age - 1.568·Rmax)) | NHTSA THOR Cert 2018 |
| Femur AIS 2+ | Kuppa | P = 1/(1+exp(5.7949 - 0.5196·F_kN)) | NHTSA 99-3960 |

## ATD Reference Data

| ATD | Mass | Height | Cost (approx) | Cert Cycle |
|-----|------|--------|---------------|-----------|
| Hybrid III 50M | 78 kg | 1.75 m | USD 150k | 12 mo / 50 tests |
| Hybrid III 5F | 49 kg | 1.51 m | USD 150k | 12 mo / 50 tests |
| Hybrid III 95M | 100 kg | 1.88 m | USD 160k | 12 mo / 50 tests |
| THOR-50M | 78 kg | 1.75 m | USD 750k | 6 mo / 30 tests |
| WorldSID 50M | 75 kg | 1.74 m | USD 600k | 12 mo / 50 tests |
| BioRID II | 76 kg | 1.78 m | USD 200k | 12 mo / 50 tests |

## Public Test Databases (Prior Sources)

- **NHTSA Vehicle Crash Test Database** — https://www.nhtsa.gov/research-data/research-testing-databases — full channel data for thousands of FMVSS-equivalent tests.
- **Euro NCAP test results archive** — https://www.euroncap.com/en/results — published rating data and per-test summaries (channel data not public).
- **IIHS Vehicle Ratings** — https://www.iihs.org/ratings — categorical ratings, photo + video, no raw channels.
- **NCAP Test Files (NHTSA)** — https://www.nhtsa.gov/file-downloads — bulk download of test reports.

## Upstream Standards

- **SAE J211 / 1, 2** — Instrumentation for Impact Test (parts 1: instrumentation, part 2: photographic instrumentation).
- **ISO 6487** — Road vehicles — Measurement techniques in impact tests — Instrumentation.
- **ISO 13232** — Motorcycles — Test and analysis procedures for research evaluation of rider crash protective devices.
- **ISO/MME format** — Multi-Media file format used to bundle channels + video + dummy info.

## Regulation Citation Anchors

- **FMVSS 208** — 49 CFR § 571.208 — Occupant crash protection.
- **FMVSS 214** — 49 CFR § 571.214 — Side impact protection.
- **FMVSS 301** — 49 CFR § 571.301 — Fuel system integrity.
- **UNECE R94** — Uniform provisions concerning the approval of vehicles with regard to the protection of the occupants in the event of a frontal collision.
- **UNECE R95** — Lateral collision.
- **UNECE R137** — Frontal collision with focus on restraint systems.
- **Euro NCAP Adult Occupant Protection Protocol v9.x** — pinned per assessment year.
- **IIHS Vehicle Research Test Protocols** — small-overlap (2012, revised 2024), moderate-overlap (1995, revised 2022).

## Operating Cheat-Sheets

**SAE J211 Sign Convention.** Vehicle: +X forward, +Y right (passenger side, USA convention), +Z down. Head accel: same. Polarity mistakes manifest as wrong-signed Nij (a flexion that looks like extension) — sanity-check by inspecting kinematics video.

**ISO-MME directory layout.** Top: `Test_<ID>.mme`. Channel files: `<channel-code>.[chn|001|002]`. Video: `<test-id>_<view>.mp4` paired with photo log.

**Pulse "in-family" features.** Frontal rigid 35 mph passenger car: peak ~40 g, time-to-peak 35-55 ms, duration ~120 ms, ΔV 55 km/h. Anything outside ±20% on peak or ±15% on duration is a red flag.

**Sampling rate.** Standard 10 kHz acquisition, 20 kHz for HIC and Nij channels — anti-alias filter at half the sample rate.
