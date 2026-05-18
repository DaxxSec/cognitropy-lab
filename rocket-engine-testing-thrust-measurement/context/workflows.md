# Rocket Engine Testing Thrust Measurement — Decision-Tree Workflows

These are the named decision trees the workspace runs on. Every command in `.claude/commands/` walks one of these trees and produces a traced verdict. Trees are named with a single-letter prefix (T, R, U, A, S, C); nodes are numbered (T-1, T-2, ...) with sub-branches (T-1-a, T-1-b). When a command emits a verdict or matrix cell, it cites the terminal node so the path is reproducible.

## 1. Test-Readiness Risk Tree (`T-*`)

Used by `/test-readiness-risk`. Walks every failure mode identified in the test card through the MIL-STD-882E 5×5 matrix.

```
T-0 INTAKE
 ├─ test card present? -- if no → REJECT, no fire authorization without a test card.
 ├─ engine FMEA / FMECA present? -- if no → REJECT, score is undefined.
 ├─ propellants and inventory documented? -- if no → REJECT.
 └─ measurement objective documented? (development / acceptance / qualification) -- required.

T-1 ENUMERATE FAILURE MODES
 └─ For each row in the FMEA, tag it with: failure mode name, immediate effect, MEOP impact.
    Output: ordered list FM_1 .. FM_n.

T-2 SEVERITY (per failure mode)
 ├─ Could it cause fatality / permanent disability / catastrophic asset loss? → I (Catastrophic)
 ├─ Could it cause hospitalization (≥3) / asset loss > $1M / mission failure? → II (Critical)
 ├─ Could it cause lost workdays / asset loss > $100K / mission degradation? → III (Marginal)
 └─ Else → IV (Negligible)
    Decision must cite an MIL-STD-882E §4.3.4 definition, not engineering judgment alone.

T-3 LIKELIHOOD (per failure mode)
 ├─ Vendor MTBF / heritage data? → quantitative band per concepts.md §"MIL-STD-882E"
 ├─ Comparable-engine experience? → cite test count + observed rate
 └─ Engineering judgment only → require explicit rationale + uncertainty acknowledgment;
    default to one band more frequent than judgment intuition (anti-optimism bias).

T-4 CELL ASSIGN
 └─ Plot (severity × likelihood) → cell ∈ {1A..4E}. Map cell to band {LOW, MEDIUM, SERIOUS, HIGH} per concepts.md table.

T-5 MITIGATION (per cell with band ≥ MEDIUM)
 ├─ Named mitigation (redline, procedure, hardware change, exclusion zone)?
 ├─ Mitigation reduces severity OR likelihood? (severity reduction preferred; likelihood reduction acceptable with engineering basis).
 └─ Post-mitigation cell → re-plot; emit pre/post pair.

T-6 ALARP GATE
 ├─ Post-mitigation cell in HIGH? → REJECT(T-6-a). HIGH must be mitigated down before fire authorization.
 ├─ Post-mitigation in SERIOUS? → require documented residual-risk acceptance by the named authority in the range ops manual.
 ├─ Post-mitigation in MEDIUM? → require ALARP justification (cost of further mitigation grossly disproportionate to benefit).
 └─ Post-mitigation in LOW? → routine acceptance, captured in matrix.

T-7 VERDICT
 └─ All post-mitigation cells ≤ SERIOUS with proper sign-off → GO_CANDIDATE.
    Any HIGH unmitigated → NO_GO.
    Any SERIOUS without authority sign-off → NO_GO_PENDING_SIGNOFF.
    Output: pre-mitigation matrix, post-mitigation matrix, sign-off block, GO_CANDIDATE / NO_GO disposition.
```

Each emitted matrix cell carries: failure-mode id, severity (I–IV), likelihood (A–E), band, mitigation, residual band, signoff authority, ALARP rationale.

## 2. Redline-Set Tree (`R-*`)

Used by `/redline-set`. Operates on the DAQ channel list and the FMEA outputs from `T-*`.

```
R-0 INTAKE
 ├─ DAQ channel list (signal, range, sample rate, abort latency).
 ├─ FMEA-linked failure modes that an abort can prevent.
 └─ Controller abort architecture (software-only vs. independent hardware path).

R-1 CANDIDATE REDLINES (per channel)
 ├─ Channel monitors a parameter tied to ≥1 severity I or II failure mode? → candidate redline.
 ├─ Channel is too noisy or too slow for redline use? → R-1-a: reject as redline, flag for monitoring instead.
 └─ Channel measurement noise vs. trip threshold: SNR ≥ 5 for redline use; else require filtering before R-2.

R-2 THRESHOLD VALUE
 ├─ Set from physics-based limit (e.g. MEOP, pump certified speed, bearing material limit)? → preferred.
 ├─ Set from prior-test data + margin? → acceptable; cite margin rationale (typically 3σ above observed nominal).
 └─ Set from engineering judgment? → require justification + sensitivity analysis.

R-3 REDLINE LATENCY
 ├─ Total time from sensor exceeding threshold to safe state achieved (sense + decide + actuate).
 ├─ Latency × parameter rate-of-rise during failure mode ≤ catastrophic margin? -- if no → R-3-a: redline ineffective, escalate to hardware-interlock path.
 └─ Independent abort path required for severity I redlines? -- if yes and absent → REJECT(R-3-b).

R-4 PER-REDLINE LIKELIHOOD × SEVERITY OF MISS
 └─ Score the likelihood and severity of *failing to trip* (false negative). Required to size confidence in the redline's protective value.

R-5 PER-REDLINE LIKELIHOOD × SEVERITY OF FALSE TRIP
 └─ Score the likelihood and severity of tripping when it shouldn't (false positive — premature scrub).
    A test ended by a false-positive abort is cheaper than a missed redline. Asymmetry must be visible in the matrix.

R-6 LOSS-OF-SIGNAL POLICY
 ├─ If channel goes invalid (NaN, out-of-range, wire break), default action = ABORT? → preferred for severity I.
 └─ Default = HOLD or REVERT? → acceptable only for non-I-severity redlines.

R-7 VERDICT
 └─ Output: per-redline table (channel, threshold, latency, miss-cell, false-trip-cell, loss-of-signal policy, abort path).
    Aggregate matrix view: redline coverage of severity I failure modes ≥ 100% required.
```

## 3. Thrust Uncertainty Budget Tree (`U-*`)

Used by `/thrust-uncertainty-budget`. JCGM-100-aligned.

```
U-0 INTAKE
 ├─ load-cell datasheet + most recent ASTM E74 cal cert.
 ├─ amplifier / signal-conditioner spec + measured noise floor.
 ├─ DAQ ADC spec (bits, range, sample rate).
 ├─ alignment data (axial-tilt budget per stand survey).
 ├─ thermal environment data (stand thermal sweep across burn duration).
 ├─ side-load cells present? gimbal sweep during fire? -- yes → include cross-talk term.
 └─ measurement objective tolerance (e.g. ≤ 0.5% k=2 for qualification).

U-1 IDENTIFY INPUTS
 └─ Enumerate every term in concepts.md §"Typical Inputs" that applies; mark each as type-A or type-B.

U-2 ASSIGN INPUT STANDARD UNCERTAINTY
 ├─ Type-A: standard deviation of N observations / √N.
 ├─ Type-B with manufacturer ±a spec, no distribution stated: rectangular, u = a/√3.
 ├─ Type-B with Gaussian basis: u = stated σ.
 └─ Cite source per row (cert page, datasheet page, in-house test report).

U-3 SENSITIVITY COEFFICIENTS
 └─ For thrust derived from cell output: c_F-wrt-cell ≈ 1 (with calibration applied).
    For alignment tilt θ: c_F-wrt-θ ≈ -F · sin(θ) (linearized at small angle).
    For thermal coefficient α: c_F-wrt-T = α · F.
    Document each derivative.

U-4 CORRELATION CHECK
 ├─ Multi-cell stand sharing one excitation supply? → cells correlated; include covariance term.
 ├─ Per-cell independent supplies + cabling? → assume uncorrelated; cite the basis.
 └─ Tare and reading from same cell on same day → correlated through cell zero; include.

U-5 COMBINED STANDARD UNCERTAINTY
 └─ u_c² = Σ(c_i · u(x_i))² + 2 · Σ_{i<j} c_i c_j ρ_{ij} u(x_i) u(x_j)
    Output u_c in units of N or % of reading.

U-6 EXPANDED UNCERTAINTY
 └─ U = k · u_c, default k=2 for ~95% coverage (effective degrees of freedom > 30; else use Welch-Satterthwaite to derive k).

U-7 COMPARE TO OBJECTIVE
 ├─ U ≤ objective tolerance → PASS.
 ├─ U > objective tolerance → REWORK, with sensitivity analysis identifying dominant term(s).
 └─ U dominated by a single term contributing > 50% of u_c² → flag for targeted mitigation, not blanket re-engineering.

U-8 OUTPUT
 └─ JCGM-100 budget table: source, type, value, distribution, c_i, contribution to u_c².
    Combined u_c, expanded U_95, PASS/REWORK against objective, dominant terms, recommendations.
```

## 4. Anomaly Risk-Score Tree (`A-*`)

Used by `/anomaly-risk-score`. Operates on a post-test anomaly entry from the test log.

```
A-0 INTAKE
 ├─ Anomaly type (instability tone, leak, hard start residue, sensor dropout, hung start, valve mis-seq, hardware).
 ├─ Time-on-test when observed; duration of anomaly.
 ├─ Engine state at observation (start transient, main stage steady, throttle, shutdown).
 ├─ Sensor data window (force, P_c, P_manifold, T_bearing, V_rms).
 └─ Damage / wear assessment from post-fire borescope or teardown.

A-1 IMMEDIATE-INJURY GATE
 ├─ Personnel injury or fatality? → IMMEDIATE_HOLD; route to safety board investigation regardless of A-tree outcome.
 └─ None → continue.

A-2 ASSET LOSS GATE
 ├─ Hardware loss (chamber breach, pump rotor, stand damage)? → severity I default unless detailed teardown demotes.
 ├─ Engine continued operation acceptable post-test (borescope clean, no spec exceedance)? → severity III/IV candidate.
 └─ In between → continue with provisional severity from observed metrics.

A-3 PATTERN CLASSIFY
 ├─ Combustion instability → A-3-a: chug / buzz / screech sub-branch from concepts.md §"Common Failure Modes".
 ├─ Leak → A-3-b: propellant, pressurant, working fluid; quantity gate.
 ├─ Hard / hung start → A-3-c: ignition delay statistics + chamber-P rise rate.
 ├─ Sensor dropout → A-3-d: redline-relevant or monitoring-only? Redline-relevant pre-trip → severity bump.
 ├─ Hardware (valve, bearing, seal) → A-3-e: replace-and-rerun vs. design-change branch.
 └─ Software / sequencer fault → A-3-f: root-cause to controller + escalate to flight-critical software review.

A-4 LIKELIHOOD OF RECURRENCE
 ├─ Anomaly explained by a transient (cold-soak, single-shot fluid hammer)? → likelihood D-E.
 ├─ Anomaly explained by a design feature (injector pattern, valve geometry)? → likelihood A-B for next fire absent change.
 └─ Anomaly unexplained → default to one band more frequent than gut estimate (anti-optimism bias).

A-5 CELL ASSIGN + DISPOSITION
 ├─ Cell in HIGH → SCRUB (next test halted pending design / procedural change + fresh T-* review).
 ├─ Cell in SERIOUS → HOLD (next test halted pending mitigation + named authority sign-off).
 ├─ Cell in MEDIUM → PROCEED_WITH_MITIGATION (named mitigation in next test card).
 └─ Cell in LOW → PROCEED (capture for trending; if 3+ same-type events in trailing 5 tests, promote to SERIOUS).

A-6 OUTPUT
 └─ Anomaly entry: classification, severity basis, likelihood basis, cell, disposition, mitigation list, sign-off requirement.
    Append to outputs/anomalies/<test-id>-<index>.md.
```

## 5. Range-Safety Matrix Tree (`S-*`)

Used by `/range-safety-matrix`.

```
S-0 INTAKE
 ├─ Stand layout map with personnel positions (control room, observation points, fire department staging).
 ├─ Propellant inventories on hand (mass per propellant).
 ├─ Stand structural geometry (blast walls, deflector geometry, fragment containment).
 └─ Wind / weather constraints policy.

S-1 PROPELLANT TNT-EQUIVALENT
 └─ Compute TNT-equivalent for each propellant (NFPA 55 / DOD 6055.09-M for explosives; specific factors per propellant).
    LOX/RP-1: typical 0.10–0.20 TNT-eq for unconfined liquid mix; confined burst higher.
    LOX/CH4: similar order.
    LOX/LH2: lower bulk TNT-eq, higher fireball.
    Cite source per row.

S-2 OVERPRESSURE FOOTPRINT
 ├─ Compute 1 psi, 2.3 psi, 5 psi standoffs (lethality progression; AFMAN 91-201 baselines).
 ├─ Plot against personnel positions; if any position inside 2.3 psi → severity II at minimum.
 └─ If inside 5 psi → severity I.

S-3 FRAGMENTATION FOOTPRINT
 ├─ Worst-credible fragment mass × velocity from chamber breach or pump rotor.
 ├─ Footprint per stand geometry (containment walls, blast deflector angle).
 └─ Severity per any position within footprint.

S-4 FIRE-SPREAD FOOTPRINT
 ├─ Combustible inventory within X m of the stand.
 ├─ Cryo pool spread radius (geometry + slope-of-pad analysis).
 └─ Severity per any flammable position within spread.

S-5 PLUME / TOXICITY FOOTPRINT
 ├─ Combustion products (steam from H2/O2, CO+CO2+H2O from HC/O2, plus stand-material decomposition).
 ├─ HF / N2O4 / hydrazine products if hypergolic.
 └─ Downwind populated standoff per local AHJ + AFMAN 91-201 baseline.

S-6 LIKELIHOOD OVERLAY
 └─ For each hazard, use the FMEA-derived likelihood of the failure that produces it (chamber breach: D/E for flight-heritage, B/C for development engine).
    Combine with severity from S-2..S-5 to produce a matrix cell per hazard per personnel position.

S-7 VERDICT
 ├─ Any personnel position with cell ≥ SERIOUS → NO_GO_LAYOUT, recommend repositioning or evacuation.
 ├─ Any cell at MEDIUM → ALARP justification required, document mitigation (move personnel, add shielding, restrict inventory).
 └─ All LOW → routine.
```

## 6. Calibration-Check Tree (`C-*`)

Used by `/load-cell-calibration-check`. Short and gate-y.

```
C-0 INTAKE
 ├─ Load cell serial, model, FS rating, manufacturer's stated cal interval.
 ├─ Most recent NIST-traceable cal cert per ASTM E74 (date, residuals, class, ambient T).
 └─ Service history since last cal (overload events, environmental exposure, mechanical alterations).

C-1 INTERVAL GATE
 ├─ Cal date + manufacturer interval ≥ today → continue.
 └─ Else → REJECT(C-1-a): cell out of cal. No thrust report until re-cal.

C-2 TRACEABILITY GATE
 ├─ Cert names NIST or accredited NMI? → continue.
 ├─ Cert names a transfer standard with NIST traceability? → continue.
 └─ Else → REJECT(C-2-a): traceability chain broken.

C-3 RESIDUALS GATE
 ├─ ASTM E74 fit residuals ≤ Class A (0.05%) → preferred.
 ├─ Residuals ≤ Class AA (0.025%) → highest grade.
 ├─ Residuals ≤ Class B (0.25%) → acceptable for development; flag for qualification.
 └─ Residuals > 0.25% → REJECT(C-3-a).

C-4 OVERLOAD EVENT
 ├─ Any service-history entry exceeding 100% FS? → require post-event re-cal before continuing.
 └─ Above safe-overload (150% FS) → REJECT(C-4-a): cell suspect; replacement preferred.

C-5 ENVIRONMENTAL FIT
 ├─ Last cal ambient T within ±10 °C of intended fire-stand environment? → continue.
 └─ Else → require thermal-coefficient correction term in U-* budget; flag for U-7.

C-6 OUTPUT
 └─ PASS / REJECT with cited node, plus a risk-cell mapping (calibration drift severity II × likelihood per admin posture).
```

## How the trees compose

- `/test-readiness-risk` walks `T-*`. On a redline-related failure mode, it auto-suggests `/redline-set`. On a thrust-credibility failure mode, it auto-suggests `/thrust-uncertainty-budget` and `/load-cell-calibration-check`.
- `/redline-set` walks `R-*`. Inputs include the FMEA-linked failure-mode list from `T-*`.
- `/thrust-uncertainty-budget` walks `U-*`. Requires `/load-cell-calibration-check` PASS at `C-*` first; otherwise `U-0` rejects.
- `/anomaly-risk-score` walks `A-*`. May invoke `/redline-set` re-run if the anomaly was a redline-miss / false-trip.
- `/range-safety-matrix` walks `S-*`. Inputs from the propellant inventory + stand layout; output feeds the global readiness matrix from `T-*`.
- `/load-cell-calibration-check` walks `C-*`. Hard gate for `U-*` and a contributing cell in `T-*`.

## Phases of a full test-readiness review

### Phase 1 — Data quality (T-0, U-0, C-0)
Confirm test card, FMEA, cal certs, DAQ channel list, propellant inventory. Reject the package, not the engine, if these are absent.

### Phase 2 — Measurement credibility (C-*, U-*)
Validate the load cell is in cal and produce the thrust uncertainty budget. Without this, thrust data has no meaning; the rest of the review is moot.

### Phase 3 — Failure-mode matrix (T-*)
Walk every FMEA row through severity / likelihood / cell / mitigation. Produce the pre- and post-mitigation matrices.

### Phase 4 — Runtime safeguards (R-*)
Design the redline table. Verify every severity I failure mode has redline coverage with adequate latency and an independent abort path.

### Phase 5 — Range-safety overlay (S-*)
Re-compute the personnel-position matrix against the propellant inventory and stand geometry. Adjust personnel positions before adjusting the matrix.

### Phase 6 — Sign-off package
Concatenate matrices, budgets, redline tables, and range overlays into the TRR package. The package is the audit trail; do not summarise away the cell ids or node trails.

### Phase 7 — Post-fire loop (A-*)
After every fire, walk the anomaly log through `A-*`. Update the FMEA-likelihood priors from observed rates; feed back into the next `T-*` pass.
