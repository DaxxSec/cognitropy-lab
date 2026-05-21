# Biomechanical Engineering — Prosthetics — Reference Tables

Lookup data the agent reaches for during fitting, SPC, fatigue testing, R&R, recall response. Compact by design — defer to cited upstream sources for full text.

## ISO / ANSI / FDA Standards

| Standard | Scope | Current revision |
|---|---|---|
| ISO 10328 | Lower-limb prosthesis structural testing (static + ultimate) | 2016 |
| ISO 22675 | Foot/ankle cyclic fatigue testing | 2016 |
| ISO 22523 | External limb prostheses + orthoses general requirements | 2006 |
| ISO 14971 | Risk management for medical devices | 2019 |
| ISO 13485 | QMS for medical devices | 2016 (Amd 1:2021) |
| ANSI/RESNA WC-1, WC-2, WC-3 | Wheelchair and seating | Various, see resna.org |
| ANSI/RESNA ED-1 | Electronic devices for ADL | 2013 |
| FDA 21 CFR 820 | US Quality System Regulation (QSR) | Current as of 2024 |
| FDA 21 CFR 806 | Medical device corrections and removals (recalls) | Current |
| EU MDR 2017/745 | EU Medical Device Regulation | In force since 2021 |

## ISO 22675 Load Levels (per user weight category)

Reference for foot/ankle fatigue testing. The agent must select load level per the target user-population's 95th-percentile weight (not mean).

| Load level | User category | Max user weight |
|---|---|---|
| P3 | Low activity, low weight | 60 kg |
| P4 | Low-moderate | 80 kg |
| P5 | Moderate-high | 100 kg |
| P6 | High | 125 kg |

Components labelled for max weight >125 kg need custom load levels with full justification + manufacturer documentation.

## K-Level (Functional Classification — Medicare CMS K-Codes)

US Medicare classification driving component approval / reimbursement. Each K-level has corresponding component restrictions per the L-code schedule.

| K-Level | Description |
|---|---|
| K0 | Non-ambulator; no transfer / locomotion ability with prosthesis |
| K1 | Household ambulator; limited indoor walking, fixed-cadence |
| K2 | Limited community ambulator; uneven terrain, low-level environmental barriers |
| K3 | Unlimited community ambulator; variable cadence, environmental barriers, vocational/therapeutic activity |
| K4 | Active adult, child, or athlete; high-impact, stress, energy demands |

K3 + K4 typically eligible for microprocessor knees, dynamic-response feet; K1 + K2 generally restricted to mechanical components.

## Cp/Cpk Interpretation Bands

| Cp/Cpk | DPMO at centre | Interpretation |
|---|---|---|
| <1.00 | >2,700 | Process incapable — producing nonconforming parts |
| 1.00 | 2,700 | At-spec; ~3σ process |
| 1.33 | 63 | Capable; ~4σ; common manufacturing target |
| 1.50 | 6.8 | Highly capable |
| 1.67 | 0.6 | Very highly capable; ~5σ |
| 2.00 | 0.002 | World-class; Six Sigma target |

Note: DPMO calculated assuming process is exactly centred. Cpk < Cp means off-centre; total DPMO will be higher than Cp-only would suggest.

## AIAG Gauge R&R Acceptance Bands

| % Study Variation (R&R) | AIAG band | Action |
|---|---|---|
| < 10% | Acceptable | Use for SPC / capability analysis |
| 10% – 30% | Marginal | Acceptable depending on cost / criticality |
| > 30% | Unacceptable | Improve before further use |

| Number of Distinct Categories (NDC) | Verdict |
|---|---|
| ≥ 5 | System discriminates adequately |
| < 5 | Inadequate; can't reliably classify parts |

## PROM Scoring + Reliability Cheat-Sheet

| Instrument | Range | Direction | Within-subject SEM (typical) | MCID (typical) | Source |
|---|---|---|---|---|---|
| PEQ subscales | 0-100 | Higher = better | 6-12 pts per subscale | 8-12 pts (population-dependent) | Legro et al. 1998 + later T-R-T studies |
| PEQ-MS | 0-100 | Higher = better | 8 pts | 8-10 pts | Hafner et al. 2017 |
| AMP-PRO | 0-47 | Higher = better | 2 pts | 3 pts | Gailey et al. 2002 |
| LCI-5 | 0-56 | Higher = better | 2-4 pts | 4 pts | Gauthier-Gagnon 1998 |
| PROMIS-PF (T-score) | 0-100 (μ=50, σ=10) | Higher = better | 2-3 T-pts | 4-6 T-pts | HealthMeasures.net |
| Houghton | 0-12 | Higher = better | 1 pt | 2 pts | Houghton et al. 1992 |

MCIDs are population- and intervention-specific; cite the matching subgroup study every time.

## Component Class Indication by K-Level (Lower-Limb Foot/Ankle)

| Component Type | K1 | K2 | K3 | K4 |
|---|:---:|:---:|:---:|:---:|
| SACH | ✓ | ✓ | — | — |
| Single-axis | ✓ | ✓ | — | — |
| Multi-axis | — | ✓ | ✓ | — |
| Dynamic-response (carbon-fibre) | — | — | ✓ | ✓ |
| Microprocessor (Proprio, Empower) | — | — | ✓ | ✓ |
| High-impact / athletic | — | — | — | ✓ |

Medicare CMS L-code formulary references each component to a specific K-level minimum.

## Upstream Catalogues

- **[FDA MAUDE](https://www.fda.gov/medical-devices/medical-device-recalls)** — US Manufacturer and User Facility Device Experience; primary recall and adverse-event database. Subscribe to RSS feed for proactive monitoring.
- **[ISO Standards Catalogue](https://www.iso.org/standards.html)** — authoritative full-text + revision history.
- **[ANSI/RESNA](https://www.resna.org/)** — Rehabilitation Engineering and Assistive Technology Society standards.
- **[Healthcare Common Procedure Coding System (HCPCS)](https://www.cms.gov/medicare/coding-billing/healthcare-common-procedure-system)** — Medicare L-code formulary for prosthetic components.
- **[International Society for Prosthetics and Orthotics (ISPO)](https://www.ispoint.org/)** — global P&O professional society; consensus statements + outcome-measure guidance.
- **[Amputee Coalition resource library](https://www.amputee-coalition.org/resources/)** — patient-facing references; PEQ + other PROM source documents.
- **[National Limb Loss Resource Center](https://amplitude-media.com/)** — clinician-facing literature curation.
- **[Open-source gait analysis: OpenSim](https://opensim.stanford.edu/)** — Stanford-developed musculoskeletal modelling toolkit.
- **[OpenCap](https://opencap.ai/)** — open-source markerless gait analysis from smartphone video.

## Operating Cheat-Sheets

### When to recompute SPC baseline

- After any component change (foot, knee, liner, sleeve)
- After patient weight change >5% (acute or sustained)
- After walking-aid status change (cane added/removed, etc.)
- After comorbidity event affecting gait (surgery, fall, stroke, neuropathy progression)
- After measurement-system change (new mat, new scanner, software version bump)

### Quick Pareto of common assignable causes (socket-fit ROIs)

1. Limb volume change (seasonal hydration, weight change, post-surgical edema) — 30-40%
2. Liner break-in or wear-out (first 60d after fit; after 6-9mo of use) — 20%
3. Activity-level change (return to work, vacation activity surge) — 15%
4. Sleeve degradation or replacement — 10%
5. Component setting change (e.g. shock-absorbing pylon damping adjustment) — 5-10%
6. Other (gait training, comorbidity, measurement noise) — remainder

## Vocabulary Disambiguation

- **"Alignment"** — in P&O: spatial relationship between socket and ground-contact element (foot or terminal device). Different from manufacturing-alignment of materials in lamination.
- **"Capability"** — in QC: Cp/Cpk (within-subgroup sigma). In clinical: patient's functional capacity (AMP-PRO score). Always specify context.
- **"Trim line"** — proximal edge of socket. Different from "trim" in upholstery / aesthetic finishing of definitive socket.
- **"Suspension"** — how the socket stays on the limb (pin-lock, suction, sleeve, strap). Different from "suspension" in vehicle / mechanical engineering.
