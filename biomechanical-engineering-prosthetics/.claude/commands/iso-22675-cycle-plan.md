# /iso-22675-cycle-plan

Plan an ISO 22675 cyclic fatigue testing protocol for a foot/ankle component — load profile, cycle count, instrumentation, accept/reject criteria, sampling plan.

## Inputs

- **Component under test** — manufacturer, model, K-classification (K1–K4), max user weight (kg), max activity level (low/moderate/high impact).
- **Intended user population** — target K-level, weight distribution (median, 95th pctile), age range, activity profile.
- **Test loading condition** (per ISO 22675): condition I (max-condition, principal loads) typically required; condition P (proof load) for design validation; load level by user category P3/P4/P5/P6.
- **Sample size** — typically n=3 components per test, but 5+ for high-risk first-of-kind designs.
- **Acceptance threshold** — minimum cycle count without failure or measurable degradation. ISO 22675 default: 2,000,000 cycles for foot units, 3,000,000 cycles for ankle-feet. Site-specific stricter criteria allowed.

## Steps

1. Read `context/references.md` "ISO standards table" for the relevant ISO 22675 load-level table (P3, P4, P5, P6 per user weight bracket) and apply to the target population's 95th percentile weight.
2. Compose the loading profile: heel-strike phase (heel pad load + dorsiflexion moment), midstance, toe-off (forefoot load + plantarflexion moment + torsion). Each cycle = one full gait cycle equivalent.
3. Specify rig instrumentation: load cells at the proximal coupling, strain gauges on the structural keel, displacement transducer for compliance measurement, temperature sensor (component temp creeps with cycling).
4. Define inspection cadence: visual + dimensional inspection at 100k, 500k, 1M, then every 500k thereafter. Note any change in compliance (>10% from baseline = caution flag).
5. Define failure criteria: (a) structural fracture, (b) compliance change >25% from baseline, (c) crack length >5mm in any structural element, (d) failure of attachment hardware.
6. Specify environmental conditions per ISO 22675 §6.4 — typically 23°C ± 2°C, 50% ± 5% RH for standard; thermal cycling option (-10°C to +40°C) for cold-climate qualification.
7. Calculate test duration: at ISO-default 1 Hz cycle rate, 2M cycles ≈ 23 days continuous; 3M ≈ 35 days. Plan for test rig downtime + inspection windows.
8. Document test protocol as `outputs/iso-22675-protocols/<component-id>/<YYYY-MM-DD>-protocol.md` with full traceability: standard revision, load level rationale, sample serial numbers, rig calibration certs, environmental settings, inspection schedule, accept/reject criteria.

## Output

A markdown protocol document at `outputs/iso-22675-protocols/<component-id>/<YYYY-MM-DD>-protocol.md` containing: component identification, ISO 22675 revision cited, user-population rationale, load profile (numerical + waveform description), sample selection (n, serial numbers, lot), rig setup + calibration, inspection schedule, accept/reject criteria, environmental conditions, projected test duration. Ready to hand to a test lab as a Statement of Work.

## Decision points

- **If target user 95th-percentile weight exceeds the highest ISO load level (P6, ~125 kg user)** → either restrict the component's max-user-weight labelling OR run a custom load level (with full justification documented and IRB-equivalent review if patient-facing claims will follow).
- **If component has a known wear-out failure mode at sub-2M cycles** → document the expected wear-out cycle count and required service-life replacement schedule explicitly; this can be acceptable if the service interval is shorter than the wear-out point with margin.
- **If sample size n=3 is insufficient for statistical confidence on a high-risk first-of-kind design** → bump to n≥5 and apply a binomial-CI test for proportion-failing.

## Notes

- ISO 22675:2016 is the current revision as of authoring. Confirm latest at iso.org before each new test — minor amendments occur.
- Cycle rate higher than 1 Hz reduces test duration but can introduce thermal artefacts (component temp creeps). 1 Hz is the ISO default for a reason.
- Pair every ISO 22675 test with an ISO 10328 static-strength validation — they answer different questions (fatigue life vs. ultimate strength).
- Document chain-of-custody for tested samples; some failures are only diagnosable post-test via destructive sectioning, which requires preserving the part as-tested.
