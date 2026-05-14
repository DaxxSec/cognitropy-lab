# Roller Coaster Design Forces Physics — Core Concepts

Background the agent should read before walking any decision tree. Optimised for fast recall by a ride-dynamics reviewer, not as a substitute for the standards documents.

## Coordinate Frames and Sign Conventions

Forces on a roller coaster are reported in one of two body-fixed frames:

- **Track frame** — origin at the vehicle's chassis reference point, axes fixed to the vehicle:
  - `+x` = forward (longitudinal, along velocity)
  - `+y` = right (lateral)
  - `+z` = down through the wheels (vertical w.r.t. the vehicle)
  Sign convention varies by vendor. The convention adopted here is **right-handed, gravity-positive-z** (so a stationary train on level track reads `(0, 0, +1g)`). Simulator data exported in "physics" mode (NoLimits 2 default) follows this; "biomechanics" mode flips `z`. Always confirm.
- **Heartline frame** — origin at the rider's sternal notch, typically 1.05–1.15 m above the wheel plane. Same axis labels, but the rotation arm from chassis to heartline matters: lateral-g at the heart is **not** lateral-g at the chassis when bank-angle ≠ 0.

**Why this matters.** A track-frame "0.2g lateral" on a 60° banked curve is essentially 0g lateral at the heartline (gravity has rotated into the lateral axis). Conversely, a track-frame 0.1g lateral on an *unbanked* curve is the full 0.1g at the heart — and that's the one that knocks heads against an OTSR. Decision-tree node `H-1` always asks: *what frame is this reported in?* before trusting a number.

## Force Envelopes (ASTM F2291 §6.4)

ASTM F2291 expresses limits as **acceleration-vs-duration curves** in three axes plus a combined-vector limit. Approximate values (consult the standard for binding numbers):

| Axis | Peak (short, <0.2s) | Sustained (>2s) | Sign |
|---|---|---|---|
| Vertical `+z` (eyeballs-down, "pulling Gs") | ~6 g | ~3 g | Compresses the spine; usually the binding limit at pullouts. |
| Vertical `-z` (eyeballs-up, "airtime") | ~-2 g | ~-1 g | Lifts the rider; binding limit at airtime hills and overbanks. |
| Lateral `±y` (eyeballs-side, "side-G") | ~2 g | ~1.5 g | Slides the rider; binding limit on unbanked or wrong-banked curves. |
| Longitudinal `+x` (eyeballs-back) | ~5 g | ~2.5 g | Launches; binding on linear-induction-motor / LSM launches. |
| Longitudinal `-x` (eyeballs-forward) | ~-3.5 g | ~-2 g | Braking; binding on magnetic brake fins, station brakes. |
| Combined vector | ~6 g | — | Vector sum √(ax² + ay² + az²). |

Numbers above are **mnemonics**, not citations. The standard specifies the limit curve as a piecewise function of duration; use `context/references.md` for the binding values.

## Heartline Geometry

The "heartline" is the locus traced by the rider's heart (or sternal notch, depending on the era of the standard) as the train follows the track. Modern coasters are often designed *heartline-first*: the engineer specifies the path the heart should take, then derives the track centerline by offsetting downward by ~1.1 m along the local body-z axis.

Implications:
- A **zero-g roll** is designed so the heartline goes straight while the train rotates around it — the rider feels free-fall, the wheels do all the work.
- A **heartline cam** is a roll whose centerline rotates *around the rider's chest*, not around the track. NoLimits 2 distinguishes "heartline" vs "track-axis" rolls explicitly.
- The longer the rotation arm (taller train, shorter rider), the more dramatic the divergence between track-frame and heartline-frame forces.

## Jerk (Third Derivative of Position)

Jerk `j = da/dt` is what whips the rider's head. The envelope check sees a peak; the jerk audit sees the *slope* of the approach to that peak. There is no widely-adopted jerk standard, but **in-house limits commonly used**:

- **Sustained jerk:** ≤ 2 g/s sustained over more than 0.5 s.
- **Transient jerk:** ≤ 5 g/s for spikes < 0.2 s.
- **Lateral-jerk:** ≤ 1.5 g/s — head mass on the C7 fulcrum is the binding factor.

A pullout that goes from 0g to 5g in 0.3 s carries a jerk of ~16 g/s — likely outside any in-house limit even if the *peak* g is acceptable. This is why jerk gets its own decision tree.

## Restraint Classes

| Class | Description | Typical use |
|---|---|---|
| **None** | Wrist tether or none | Kiddie coasters, family rides with `-z ≥ 0g`, no inversions, lateral ≤ 0.5g. |
| **Lap-bar (single)** | Single fold-down lap bar | Family / starter coasters, `-z ≥ -0.5g`, no inversions, lateral ≤ 1.0g. |
| **Lap-bar (individual ratchet)** | Per-seat ratcheting lap bar | Airtime coasters, `-z` to ~-1.5g, no inversions. |
| **OTSR (over-the-shoulder restraint)** | Fixed shoulder yoke | Loopers, mid-90s convention; high lateral-g tolerated; head-banging risk. |
| **Soft vest / Mack-style OTSR** | Compliant shoulder restraint | Modern inverting coasters; mitigates head-bang while retaining shoulder containment. |
| **Individual hydraulic** | Per-seat hydraulic restraint with bleed | High-G launch coasters; B&M / Intamin. |

The restraint-class decision tree (workflows §2) asks three questions in order: *is there an inversion?*, *is `-z` below -1.0g?*, *is lateral above 1.0g?* Each answer routes to a class.

## Common Failure Modes

- **Frame confusion.** Sim reports track-frame; reviewer assumes heartline. Verdict is meaningless. Always tree-node `H-1` first.
- **Peak chasing.** Envelope check passes because peaks are below limits, but cumulative dose (rms over the element) is high. Watch sustained-band nodes.
- **Banking-too-late.** Banking ramps in *during* the turn instead of before; lateral spikes at curve entry. Common on retracked sections.
- **Jerk in the transitions, not in the elements.** Airtime hill itself is fine, but the entry transition has a 12 g/s spike. Envelope check passes; rider complaints arrive.
- **Restraint over-engineering.** OTSR specified on an element that doesn't need it; introduces head-banging risk where a lap-bar would have been safer.
- **Heartline drift.** Sim updated but heartline reference height never adjusted; forces look right at the chassis but are wrong at the chest.

## Operating Constraints

- ASTM F2291 §6.4 and EN 13814 Annex G are minima — never relax.
- In-house operator limits, when stricter than the standard, are binding for that ride.
- Restraint downgrade requires a documented decision-tree walk attached to the change order; no verbal approvals.
- All decision-tree walks must be reproducible from raw simulator output (no manual smoothing of force traces before envelope check).
- Pediatric / geriatric / pregnancy carve-outs are operator policy questions, not engineering judgment; flag for AHJ.
