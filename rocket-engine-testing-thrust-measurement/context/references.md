# Rocket Engine Testing Thrust Measurement — Reference Tables

Compact lookup data. Defer to MIL-STD-882E, JCGM 100, ASTM E74, AFSPCMAN 91-710, and NFPA 55 for binding values.

## MIL-STD-882E Risk Matrix (5×4)

```
                  I (Catastrophic)   II (Critical)   III (Marginal)   IV (Negligible)
A (Frequent)        HIGH                HIGH            SERIOUS         MEDIUM
B (Probable)        HIGH                HIGH            SERIOUS         MEDIUM
C (Occasional)      HIGH                SERIOUS         MEDIUM          LOW
D (Remote)          SERIOUS             MEDIUM          MEDIUM          LOW
E (Improbable)      MEDIUM              MEDIUM          LOW             LOW
```

## Severity Definitions (MIL-STD-882E §4.3.4 paraphrased)

| Cat | Personnel | Asset / Mission | Environment |
|---|---|---|---|
| I (Catastrophic) | Fatality, permanent total disability | Program loss > $10M, mission failure with severe consequence | Irreversible severe damage |
| II (Critical) | Permanent partial disability, hospital for ≥3 | Loss > $1M, mission failure | Reversible significant |
| III (Marginal) | Injury requiring lost workdays | Loss > $100K, mission degradation | Reversible moderate |
| IV (Negligible) | Minor injury, no lost workdays | Loss < $100K, minimal mission impact | Minimal |

## Probability Bands (MIL-STD-882E §4.3.5 paraphrased)

| Lvl | Word | Per-event quantitative | Per-mission interpretation |
|---|---|---|---|
| A | Frequent | > 10⁻¹ | Continuously experienced |
| B | Probable | 10⁻¹ to 10⁻² | Will occur several times |
| C | Occasional | 10⁻² to 10⁻³ | Sometime in life of item |
| D | Remote | 10⁻³ to 10⁻⁶ | Unlikely but possible |
| E | Improbable | < 10⁻⁶ | Assume not experienced |
| F | Eliminated | n/a | Incapable of occurrence |

## Residual-Risk Acceptance Authority (mapped)

| Band | DoD authority | Commercial test site analog |
|---|---|---|
| HIGH | Service Acquisition Executive (cannot be ALARP-justified for fire authorization) | CEO + range safety officer + customer; rarely accepted |
| SERIOUS | PEO / Program Executive Officer | Director of test ops + range safety officer |
| MEDIUM | Program Manager | Test conductor + responsible engineer |
| LOW | Routine acceptance | Routine acceptance |

## ALARP Decision Threshold

Documentation required to accept residual risk in MEDIUM band:

- Hazard description with cited severity definition.
- Current likelihood with rationale.
- Listed alternative mitigations rejected, with cost/benefit comparison.
- "Grossly disproportionate" justification (typically: mitigation $ or schedule cost > 5–10× risk-reduction value).

## Typical Load-Cell Specs (Aerospace Strain-Gauge)

| Parameter | Typical | Best |
|---|---|---|
| Combined linearity + hysteresis + non-repeatability | 0.10% FS | 0.025% FS |
| Thermal sensitivity coefficient | 0.005% / °C reading | 0.0008% / °C reading |
| Thermal zero coefficient | 0.005% / °C FS | 0.0015% / °C FS |
| Safe overload | 150% FS | 200% FS |
| Ultimate overload | 300% FS | 500% FS |
| Bridge resistance | 350 Ω | 700 Ω (lower self-heating) |
| Output sensitivity | 2 mV/V | 3 mV/V |
| Recommended cal interval | 12 months | 6 months (mission-critical) |

## ASTM E74 Class Definitions (Force-Measuring Instrument Calibration)

| Class | Lower-load limit error | Upper-load limit error | Use |
|---|---|---|---|
| AA | ±0.025% | ±0.025% | Best-in-class transfer standards |
| A | ±0.05% | ±0.05% | Aerospace qualification |
| B | ±0.25% | ±0.25% | Development testing |
| C | ±0.5% (specified per program) | ±0.5% | Limited use; production-only |

Cite the ASTM E74 fit residuals on every calibration record.

## JCGM 100 Coverage Factors (k)

| k | Coverage probability (~Gaussian) | Use |
|---|---|---|
| 1 | 68% | Combined standard uncertainty `u_c` |
| 2 | 95.45% | **Default for aerospace TRR reporting** |
| 2.576 | 99% | Critical safety reports |
| 3 | 99.73% | Conservative engineering |

For low effective degrees of freedom (`ν_eff < 30`), use Welch-Satterthwaite to derive a higher k.

## Typical Thrust Uncertainty Budget Contributions

| Term | Type | Typical % of reading | Notes |
|---|---|---|---|
| Load-cell linearity + hysteresis | B | 0.05–0.15 | From ASTM E74 fit. |
| Amplifier noise + excitation regulation | A | 0.01–0.10 | Measure with shorted bridge. |
| ADC quantization | B | < 0.01 | 24-bit DAQ; negligible. |
| Thermal sensitivity | B | 0.05–0.40 | Dominant for long burns. |
| Axial alignment | B | 0.05–0.30 | `cos θ` factor; survey-based. |
| Side-load cross-talk | B | 0.05–0.50 | Binding with gimbal. |
| Tare drift (thermal) | B | 0.05–0.50 | Cryo line growth. |
| Flexure / restraint parasitic | B | 0.05–0.30 | Over-constrained mount. |

`u_c = sqrt(Σ contributions²)`; `U_95 = 2·u_c`.

## Propellant Class Quick Reference (NFPA 55 / DOT)

| Propellant | NFPA 704 health / flammability / instability | Cryo? | TNT-eq (unconfined liquid mix) | Plume primary product |
|---|---|---|---|---|
| LOX / RP-1 | 3 / 0 / 0 (LOX) + 0 / 2 / 0 (RP-1) | LOX yes | 0.10–0.20 | H₂O + CO₂ |
| LOX / CH₄ (methalox) | 3 / 0 / 0 + 1 / 4 / 0 | both yes | 0.15–0.25 | H₂O + CO₂ |
| LOX / LH₂ | 3 / 0 / 0 + 0 / 4 / 0 | both yes | 0.05–0.10 (large fireball) | H₂O |
| MMH / NTO (N₂O₄) | 4 / 3 / 3 + 4 / 0 / 1 | no | 0.05–0.15 | NOₓ + H₂O (toxic) |
| 90% H₂O₂ / kerosene | 1 / 0 / 3 + 0 / 2 / 0 | no | 0.05–0.10 | H₂O + O₂ + CO₂ |

Always confirm against site-specific propellant data sheets. TNT-eq is reference, not gospel.

## Common Redlines (typical operating envelope)

| Parameter | Typical setpoint (basis) | Severity if violated | Independent abort path required? |
|---|---|---|---|
| Chamber pressure rise rate (start) | > 1.5–2.0× nominal slope | I (chamber breach) | Yes |
| Chamber pressure absolute (steady) | > 110% nominal | I | Yes |
| Manifold ΔP (injector) | > 120% nominal | II (instability precursor) | No |
| Turbopump speed | > certified speed | I (rotor uncontainment) | Yes |
| Bearing temperature | > material limit | II–III (bearing wear) | No |
| Cooling-jacket inlet T | > material limit | I (burn-through) | Yes |
| Mount vibration RMS | > 1.5× nominal RMS | II (instability indicator) | No |
| Gimbal actuator load | > rated load | III | No |
| Loss of redline signal | NaN / out-of-range | severity of failure it protected | Yes (default ABORT) |

## Standoff & Range-Safety Cheat-Sheet (mnemonic; site-specific values bind)

| Hazard | Severity I distance (mnemonic) | Source |
|---|---|---|
| Overpressure (5 psi lethality) | scales as (W_TNT-eq)^(1/3) · 1.0 m/kg^(1/3) | AFMAN 91-201 / KTW eqn |
| Overpressure (2.3 psi injury) | scales as (W_TNT-eq)^(1/3) · 1.6 m/kg^(1/3) | AFMAN 91-201 |
| Fragmentation worst-credible | site-survey; typical 100–500 m for booster class | Stand-specific |
| LOX pool fire radius | √(spill volume / k_pool) | NASA-STD-5018 / NFPA 55 |
| Toxic plume (MMH/N₂O₄) | downwind concentration model (AEGL/ERPG) | EPA AEGL tables |

Always run the site-specific model. The above are only for sanity-checking.

## Standards & Catalogues

- **MIL-STD-882E — System Safety** — https://www.dau.edu/cop/armyesoh — DoD risk-matrix definitions (the canonical 5×5).
- **JCGM 100:2008 — Evaluation of Measurement Data – Guide to the Expression of Uncertainty in Measurement (GUM)** — https://www.bipm.org/en/publications/guides — type-A / type-B / combined / expanded.
- **ASTM E74 — Calibration and Verification for Force-Measuring Instruments** — https://www.astm.org/e0074-18.html — primary load-cell calibration practice.
- **ASTM E4 — Practices for Force Verification of Testing Machines** — https://www.astm.org/e0004-21.html — companion to E74.
- **AIAA G-145-2019 — Guide to Test Uncertainty in Aerospace Ground-Test Facilities** — https://www.aiaa.org/publications/standards — aerospace GUM adaptation.
- **NIST SP 250-39 — Force Calibration Service** — https://www.nist.gov/calibrations — top of force traceability chain.
- **NFPA 55 — Compressed Gases and Cryogenic Fluids Code** — https://www.nfpa.org/55 — propellant proximity standards.
- **AFMAN 91-710 — Range Safety User Requirements** — https://www.faa.gov/space — flight + ground test range-safety baseline.
- **AFMAN 91-201 — Explosives Safety Standards** — https://www.dau.edu — overpressure standoff equations.
- **NASA-STD-5018 — Strength Design and Verification Criteria** — https://standards.nasa.gov — broader NASA-STD-50xx propulsion suite hub.
- **KSC-DE-512 — Design Engineering Standards (Test Stands)** — Kennedy Space Center design documents — internal NASA reference, cite by document control number.
- **ECSS-Q-ST-40C — ESA System Safety** — https://ecss.nl — European MIL-STD-882 analog with mostly compatible severity / probability scales.
- **DOT 49 CFR Parts 100–185 — Hazardous Materials Regulations** — https://www.ecfr.gov/current/title-49 — propellant transport / storage classes.

## DAQ Hot-Fire Channel List (typical baseline)

| Channel | Sample rate (Hz) | Range | Purpose |
|---|---|---|---|
| Axial thrust (load cell A) | 5,000–10,000 | 0 – FS thrust | Primary thrust measurement |
| Axial thrust (load cell B redundant) | 5,000–10,000 | 0 – FS thrust | Redundant primary |
| Side load Y / Z | 1,000 | ± 10% FS | Alignment & gimbal characterization |
| Chamber pressure P_c | 10,000–50,000 | 0 – 1.5× nominal | Combustion stability + redline |
| Injector manifold P (fuel + ox) | 5,000 | 0 – 1.5× nominal | Injector ΔP + redline |
| Turbopump speed | 10,000 | 0 – 1.5× rated | Pump health + redline |
| Bearing temperatures | 100 | -200 °C – +600 °C (per pump) | Bearing health + redline |
| Cooling-jacket inlet / outlet T | 100 | -250 °C – +500 °C | Jacket health + redline |
| Cooling-jacket ΔP | 1,000 | 0 – 1.5× nominal | Flow-rate inference |
| Mount accelerometers (3-axis) | 10,000–50,000 | ± 10 g typical | Vibration + instability sensing |
| Tank pressures (fuel + ox) | 100 | 0 – 1.5× nominal | Autogenous pressurization |
| Valve position feedback | 200 | 0 – 100% | Sequencer verification |
| Time tag (GPS or master clock) | per channel | UTC | Cross-channel sync |
