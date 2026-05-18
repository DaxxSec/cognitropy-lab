# Rocket Engine Testing Thrust Measurement — Core Concepts

Background the agent should read before scoring any matrix cell or signing off on an uncertainty budget. Optimised for fast recall by a ground-test propulsion reviewer; not a substitute for MIL-STD-882E, JCGM 100, or ASTM E74.

## The Thrust Stand as a Measurement System

A liquid-rocket engine sits on a thrust stand that is, mechanically, a load path: the engine bolts to a thrust frame, the thrust frame transmits force to one or more load cells, and the load cells transmit to ground. Two common topologies:

- **Vertical thrust stand** — engine fires downward into a thrust mount; load cells sit between thrust mount and a structural mass. Used for upper-stage and small engine tests (e.g. RL10, ESA Vinci sub-scale, SpaceX Raptor sub-scale, ULA / Aerojet Rocketdyne hot-fires at SSC).
- **Horizontal thrust stand** — engine fires horizontally into a thrust block; load cell(s) measure axial force, with secondary cells for side-load / pitch / yaw. Used for booster-class engines (RS-25 at SSC B-2, Merlin at McGregor, Vulcain at Lampoldshausen).

In both cases the **measurand** is the axial thrust `F_axial` produced by the engine — but the load cells measure the *force their mount transmits*, which is `F_axial` minus tare loads and any spurious transmission paths. Spurious paths include propellant feed-line stiffness, gimbal hydraulic preload, and thermal expansion of plumbing across a long burn. The art of thrust measurement is decomposing those.

### Load Cells and Their Failure Modes

Strain-gauge load cells are the workhorse for thrust measurement; piezo cells appear in transient-thrust work. Key spec ranges for a typical aerospace strain-gauge cell (Interface 1010-series, Honeywell Sensotec Model 41, Lebow 3173-series):

| Parameter | Typical aerospace spec |
|---|---|
| Combined nonlinearity + hysteresis + non-repeatability | 0.05% – 0.10% of full scale |
| Thermal sensitivity coefficient | 0.0008% – 0.005% / °C of reading |
| Thermal zero coefficient | 0.0015% – 0.005% / °C of FS |
| Safe overload | 150% of FS |
| Ultimate overload (mechanical failure) | 300% – 500% of FS |
| Bridge resistance | 350 Ω (most common) or 700 Ω |
| Output at FS | 2 mV/V or 3 mV/V |
| Bridge excitation | 5–10 V DC, regulated |

Cells used in thrust measurement live in a hostile environment: cryogenic boil-off, hot gas plume reflection off the flame deflector, vibration from chamber-pressure oscillation, and side-load events during gimbal sweeps. Each environmental load is a failure-mode candidate.

### Calibration Chain

A thrust reading credibility traces back to NIST (or the national-metrology-institute equivalent) through ASTM E74:

1. **NIST primary deadweight calibration** — deadweight machines at NIST's Force Group calibrate transfer standards (proving rings, transfer cells) traceable to mass + g. NIST SP 250-39 documents the service. Top of chain.
2. **Transfer standard** (proving ring or transfer load cell) — a deadweight-calibrated artifact the test site uses on-site to verify production cells.
3. **In-situ calibration of the working load cell** — the test site applies known forces via a proving ring, hydraulic calibration cylinder, or in-line deadweight; the cell's output is fit to the known force per ASTM E74 (Class A, AA, or B depending on the residuals).
4. **Production thrust reading** — the working cell measures engine thrust during fire.

Any break in the chain — expired NIST cert on the transfer standard, expired in-situ cal on the working cell, overload event since last cal, environmental excursion outside calibrated range — invalidates the thrust reading. The risk-matrix consequence is `2A` (likelihood frequent if calibration administration is sloppy, severity II marginal because the data is unusable but the test is not unsafe).

## Uncertainty Budgeting (JCGM 100 / GUM)

Thrust uncertainty is a propagation problem. JCGM 100 (the GUM) defines two input types and the combination rule:

- **Type-A uncertainty** — evaluated by statistical analysis of repeated observations (e.g. standard deviation of N independent calibration cycles).
- **Type-B uncertainty** — evaluated by any other means (manufacturer spec, prior measurement, judgment with rationale). Default distribution: rectangular (±a divided by √3) unless a better one is justified.

For thrust `F` derived from a chain of inputs `x_i` with sensitivities `c_i = ∂F/∂x_i`, the combined standard uncertainty is:

```
u_c²(F) = Σ (c_i · u(x_i))²    (assuming uncorrelated inputs)
```

For correlated inputs (common with multi-cell stands where all cells share a power supply), the cross-covariance terms must be included. Expanded uncertainty `U = k · u_c(F)`, with `k=2` for ~95% coverage (the convention for aerospace TRRs).

### Typical Inputs to a Thrust Uncertainty Budget

| Source | Typical contribution (% of reading) | Notes |
|---|---|---|
| Load-cell linearity + hysteresis | 0.05% – 0.15% | From ASTM E74 fit residuals. Lives on the cal cert. |
| Amplifier / signal-conditioner noise | 0.01% – 0.10% | Includes excitation regulation. Type-A if measured with shorted bridge. |
| ADC quantization | <0.01% with 24-bit DAQ | Negligible for modern systems. |
| Thermal sensitivity drift | 0.05% – 0.40% | Function of stand thermal excursion across burn. Dominant for long burns. |
| Alignment (axial tilt) | 0.05% – 0.30% | `cos θ` factor; 1° tilt = 0.015% loss but compounds with side-load coupling. |
| Side-load cross-talk | 0.05% – 0.50% | Vector decomposition; binding if gimbal sweep is active. |
| Tare drift (thermal expansion) | 0.05% – 0.50% | Cryogenic propellant feed line growing/shrinking against thrust frame. |
| Excitation supply regulation | 0.01% – 0.05% | Negligible with regulated DC supply; can be large with un-regulated. |
| Flexure / restraint stiffness | 0.05% – 0.30% | If thrust frame is over-constrained, parasitic load paths bleed thrust. |

The combined standard uncertainty `u_c` is the root-sum-of-squares of the row contributions. The expanded uncertainty `U_95 = 2·u_c` is the reported figure. The measurement objective (development burn allows ~2%; flight-qualification fire typically demands ≤0.5%) defines the pass/fail.

## MIL-STD-882E Risk Matrix

Risk severity (one axis):

| Category | Label | Definition (paraphrased from MIL-STD-882E §4.3.4) |
|---|---|---|
| I | Catastrophic | Could result in fatality, permanent total disability, irreversible severe environmental damage, or program loss > $10M (typical threshold). |
| II | Critical | Could result in permanent partial disability, injuries requiring hospitalization for ≥ 3 personnel, reversible significant environmental damage, or loss > $1M. |
| III | Marginal | Could result in injury requiring lost workdays, reversible moderate environmental damage, or loss > $100K. |
| IV | Negligible | Could result in injury not requiring lost workdays, minimal environmental damage, or loss < $100K. |

Risk probability (the other axis):

| Level | Label | Frequency descriptor | Quantitative (per-event) |
|---|---|---|---|
| A | Frequent | Likely to occur often in the life of the item. | > 10⁻¹ |
| B | Probable | Will occur several times in the life of the item. | 10⁻¹ to 10⁻² |
| C | Occasional | Likely to occur sometime in the life of the item. | 10⁻² to 10⁻³ |
| D | Remote | Unlikely but possible to occur. | 10⁻³ to 10⁻⁶ |
| E | Improbable | So unlikely that occurrence may be assumed not to be experienced. | < 10⁻⁶ |
| F | Eliminated | Hazard incapable of occurrence. | n/a |

The matrix:

```
                  I (Catastrophic)   II (Critical)   III (Marginal)   IV (Negligible)
A (Frequent)        HIGH                HIGH            SERIOUS         MEDIUM
B (Probable)        HIGH                HIGH            SERIOUS         MEDIUM
C (Occasional)      HIGH                SERIOUS         MEDIUM          LOW
D (Remote)          SERIOUS             MEDIUM          MEDIUM          LOW
E (Improbable)      MEDIUM              MEDIUM          LOW             LOW
```

Residual-risk acceptance authority is a function of the band: LOW = program manager, MEDIUM = PEO/director, SERIOUS = service component, HIGH = service acquisition executive. For commercial test sites the analogous authority chain is documented in the range operations manual.

### ALARP

"As Low As Reasonably Practicable" — the principle that residual risk in MEDIUM / SERIOUS bands must have a documented decision that the cost (schedule, $, mass, complexity) of further mitigation is grossly disproportionate to the benefit. HIGH risks may **not** be ALARP-justified; they must be mitigated down to SERIOUS or lower before fire.

## Common Failure Modes in Liquid Rocket Engine Hot-Fire

- **Hard start.** Ignition delay long enough that accumulated propellants flash to a chamber overpressure pulse exceeding nominal MEOP. Severity I if chamber breach; severity II if the engine survives. Likelihood A on a new injector with limited heritage; D on a well-characterized one.
- **Hung start.** Igniter lights, but main-stage transition fails to reach nominal chamber pressure. Propellants pool, ignite asymmetrically, drive lateral loads. Severity II–III, likelihood B on cold-soaked starts.
- **Chug-mode combustion instability.** Low-frequency (~10–200 Hz) chamber-pressure oscillation, typically tied to feed-system / chamber coupling. Damaging to plumbing fatigue life; usually not catastrophic on a single burn but a NO-GO for cumulative service.
- **Buzz-mode / pop-mode instability.** Intermediate-frequency (200–1000 Hz) tones from injector / chamber coupling. Often indicative of a marginal injector pattern.
- **Screech (high-frequency instability).** > 1000 Hz transverse-mode chamber instability; can rupture chamber walls in <100 ms. Severity I, likelihood A on a new injector pattern, D on a flight-heritage one. The "screech" tone is the canonical example of an instability that the redline must catch.
- **Cooling-jacket burn-through.** Regenerative-cooling failure leading to chamber-wall melting at the throat. Severity I; likelihood is engine-specific (a stuck check valve in the cooling-jacket line is plausible-but-rare).
- **Turbopump overspeed.** Loss of downstream load (propellant valve closes too slow, or main-stage fails to ignite) lets the pump accelerate beyond design speed. Severity I (uncontained rotor failure can shrapnel the entire pump). Likelihood D on a well-tuned controller; B on a development engine without speed-limit logic.
- **Bearing failure.** Cryo-bearing wear, lubricant degradation, or coolant flow loss. Severity II–III; usually annunciates via bearing temperature rise before catastrophic failure, so the redline is the mitigation.
- **Leak (propellant or pressurant).** LOX or LH2 leak at flange / seal / weld. Severity escalates with quantity and location (LH2 fire is usually less violent than an LOX-impingement reaction with hydrocarbons in stand structure). NFPA 55 governs proximity standards.
- **Load-cell overload event.** A side-load excursion during a gimbal sweep, or a hard start, exceeds the cell's 150% safe-overload limit. Span shift typically follows; the cell must be re-calibrated or replaced before any subsequent thrust report.
- **Calibration drift.** Cell's span shifts beyond the ASTM E74 acceptance band between cal intervals. Severity II (data is wrong but the test is not unsafe); likelihood A if cal admin is poor.
- **Tare bookkeeping error.** Pre-fire tare not captured, or captured at wrong thermal state, leading to a thrust offset throughout the burn. Severity II–III.
- **Frame thermal expansion.** Long burns cause the thrust frame to grow against the load cell, biasing thrust positive or negative depending on geometry. The thermal-sensitivity term in the uncertainty budget is the mitigation.
- **Tachometer / DAQ dropout.** Loss of a redline channel mid-burn; the controller must abort if the loss meets the redline-loss criterion.
- **Software / sequencer fault.** Valve mis-sequencing. Severity I–II; mitigation is the controller's deterministic state machine plus an independent abort path.

## Operating Constraints

- **MIL-STD-882E severity definitions are the floor for severity scoring.** Do not redefine "Critical" as "Marginal" because the schedule pressure says so. Documented authority overrides only after a written deviation request.
- **In-house operator limits override published limits when stricter.** Many sites enforce thrust uncertainty budgets tighter than the customer spec; the in-house limit is binding.
- **Calibration intervals are immovable from the manufacturer's stated max.** Cells used past the interval are out-of-cal regardless of how recent the last data looked.
- **No live-fire on a HIGH risk-matrix cell without documented residual-risk acceptance by the authorities named in the range operations manual.** No verbal sign-offs. No "we'll document it after."
- **Independent abort path required for severity I redlines.** A redline whose loss is severity I must be backed by a hardware abort path independent of the primary controller; software-only is not acceptable for I-level redlines.
- **Range safety distances per AFSPCMAN 91-710 are minima.** In-house standoffs may be stricter and are binding when so.
- **Export control (ITAR / EAR) applies to liquid rocket engine data in the United States.** This workspace is for the analytical work; do not store ITAR-controlled detail in uncontrolled environments.
