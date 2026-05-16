# Vehicle Crash Test Interpretation — Core Concepts

Background the agent reads before acting on a test. Optimised for fast recall.

## Injury Criteria (Per Body Region)

Crash testing reports occupant load as scalar criteria computed from time histories. Each criterion has a regulatory threshold and an associated injury-risk curve (logistic in most cases) that maps the scalar to a probability of injury at a given Abbreviated Injury Scale (AIS) level. **Risk curves are the likelihoods in this workspace's Bayesian model**; thresholds alone are not.

### Head
- **HIC15** — Head Injury Criterion over a 15 ms window. Computed as `max{(t2-t1) · [1/(t2-t1) · ∫a(t)dt]^2.5}` where `a(t)` is head resultant acceleration in g, t2-t1 ≤ 15 ms.
  - FMVSS 208 threshold: HIC15 ≤ 700 (50th male), ≤ 700 (5th female), ≤ 570 (6yo), ≤ 390 (3yo).
  - Risk curve (Mertz 2003): P(AIS 3+ head) = Φ((ln HIC15 - 7.45) / 0.73).
- **BrIC** (Brain Injury Criterion) — angular velocity-based; relevant for THOR-50M. P(AIS 4+) = 1 - exp(-(BrIC/0.987)^2.84).

### Neck
- **Nij** — Combined axial force / bending moment criterion. `Nij = Fz/Fzc + My/Myc` evaluated at upper neck. FMVSS 208 threshold ≤ 1.0.
  - Critical intercepts (Fzc, Myc) vary by occupant size: 50th male = (6806 N, 310 Nm), 5th female = (4287 N, 155 Nm).
- **Nkm** — Neck injury criterion (rear impact / whiplash), used by EuroNCAP rear-impact and BioRID assessments.

### Chest
- **Chest deflection** — Peak sternum-to-spine displacement, measured by chest potentiometer (Hybrid III) or IR-TRACC (THOR-50M).
  - FMVSS 208 threshold: ≤ 63 mm (50th male, Hybrid III); ≤ 52 mm (5th female).
  - Risk (Kuppa 2004): P(AIS 3+ chest) = 1 / (1 + exp(10.3 - 0.140 × age - 0.122 × deflection_mm)).
- **Peak chest acceleration (3 ms clip)** — FMVSS 208 ≤ 60 g for any 3 ms continuous interval.

### Pelvis / Femur / Tibia
- **Femur axial force** — FMVSS 208 ≤ 10 kN.
- **Tibia index** — EuroNCAP / IIHS lower-leg metric, combining axial force and bending moment.
- **Pelvis acceleration** — Used in side-impact tests (FMVSS 214) — peak ≤ 130 g (or pelvic combined force per ECE R95).

## Crash Test Modes

| Mode | Speed / Configuration | Regulation | Notes |
|------|----------------------|-----------|-------|
| Full-width frontal rigid | 35 mph (56 km/h) into rigid wall | FMVSS 208 | High vehicle-deceleration, low intrusion. |
| ODB (Offset Deformable Barrier) | 40 mph, 40% overlap, deformable face | UNECE R94 | Offset loading — intrusion matters. |
| MPDB (Moving Progressive Deformable Barrier) | 50 km/h closing each side | EuroNCAP 2020+ | Replaces ODB for EuroNCAP frontal; measures compatibility. |
| Small-overlap frontal | 40 mph, 25% overlap, rigid | IIHS | Bypasses crush structure — challenging for restraints. |
| Oblique | 90 km/h, 15° angle, 35% overlap | NHTSA / Euro NCAP | Combines small-overlap with rotation. |
| Side mobile barrier | 50 km/h, AE-MDB | UNECE R95 / FMVSS 214 | Tests B-pillar integrity, side airbags. |
| Side pole | 32 km/h, vehicle side into pole | FMVSS 214 / EuroNCAP | Curtain airbag-critical. |
| Rear impact | 16-20 mph rear-into-stationary | EuroNCAP whiplash | BioRID dummy, neck criteria dominate. |

## Anthropomorphic Test Devices (ATDs)

| ATD | Generation | Used For | Channels |
|-----|-----------|----------|----------|
| Hybrid III 50M | 1970s-current | Frontal; baseline regulatory ATD | ~52 |
| Hybrid III 5F | 1990s | Small-female occupant front | ~52 |
| Hybrid III 95M | 1990s | Large-male occupant front | ~52 |
| THOR-50M | 2010s-current | Frontal; replaces Hybrid III for advanced biofidelity in EuroNCAP / NHTSA | ~150 |
| WorldSID 50M | 2010s-current | Side impact (EuroNCAP, UNECE) | ~90 |
| BioRID II | 1990s-current | Rear-impact whiplash | ~40 |
| Q-series (Q3, Q6, Q10) | 2000s-current | Child occupants | varies |

Every ATD has a **certification schedule** — typically every 12 months or every 50 tests — at which channels are checked against a reference impactor. The lab's certification log feeds `/dummy-bias-prior`.

## Bayesian Probability Assessment — Today's Technique

The technique that ties this workspace together: every numeric injury claim is a **posterior**, not a measurement.

- **Prior**: distribution over the criterion before this test. Sources: dummy certification history (per-channel bias), prior-test fleet distribution (per-vehicle population), regulator-published reference distributions (for anomaly screening).
- **Likelihood**: the canonical injury-risk curve mapping the measured criterion to P(AIS k+ injury). Mertz 2003, Eppinger 1999, Kuppa 2004 for Hybrid III; updated curves for THOR-50M and WorldSID.
- **Posterior**: P(criterion ≤ threshold | data) and P(AIS k+ | data). Reported as median + 5/95 credibility interval. Sampled via MCMC (PyMC, NUTS, target_accept=0.9).

A posterior interval that **straddles** a regulatory threshold is the most important finding this workspace produces — it is the headline that a binary pass/fail report would suppress.

## Common Failure Modes

- **Reporting point estimates only.** Every injury criterion has hidden sensor and pulse-shape uncertainty; collapsing to a single number is statistically dishonest and operationally fragile when retests yield different point estimates.
- **Ignoring dummy bias.** A dummy whose chest potentiometer reads 5% high doesn't fail certification but biases every test it touches. `/dummy-bias-prior` is mandatory.
- **Channel clipping.** A saturated head accelerometer produces a HIC15 that's a lower bound, not an estimate. Clipping must be detected by `/pulse-anomaly-check` before injury analysis.
- **Confusing compliance with safety.** Passing FMVSS 208 does not mean a vehicle is safe in unrepresented modes (oblique, small overlap, rollover, second-row).
- **Stripping uncertainty from publication.** Consumer publications that only report stars hide the credibility interval that distinguishes a robust five-star from a probabilistic five-star.
- **Mixing dummy generations in one analysis.** Hybrid III and THOR-50M produce different chest deflection values for the same physical event — they live in different injury-risk-curve families. Do not pool without an explicit cross-calibration prior.

## Operating Constraints

- **SAE J211 / ISO 6487** govern instrumentation: polarity, sign conventions, filter classes. Every channel deliverable must declare its CFC class (60, 180, 600, 1000) explicitly.
- **CFC filter classes** correspond to channel types: CFC 60 = vehicle structural accel; CFC 180 = chest deflection / chest acceleration; CFC 600 = belt forces, head accel for HIC; CFC 1000 = neck loads, high-bandwidth head accel.
- **Polarity (SAE J211 sign convention)**: +X forward, +Y right (passenger side), +Z down; head acceleration with +Z down means a forward+downward head motion produces +X and +Z. Get this wrong and every Nij calculation is wrong.
- **Regulatory revisions are dated.** FMVSS 208 has had material revisions; EuroNCAP changes protocols yearly. Pin the revision-in-force at the test date for every compliance analysis.
- **Dummy certification window.** ATDs are valid for use within 12 months of certification (or 50 tests, whichever first). Tests with out-of-window dummies are not admissible — `/dummy-bias-prior` will refuse to issue a usable prior.
