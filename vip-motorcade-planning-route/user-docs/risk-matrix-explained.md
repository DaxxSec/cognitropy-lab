# Risk Matrix Explained — Why 5×5, How to Calibrate, How It's Abused

A user-facing reference for the *thinking* behind the matrix this workspace runs on. Read once when you start using the workspace; revisit when you find yourself disagreeing with a score.

## Why a Matrix at All

A motorcade route choice is fundamentally a *comparison* problem: of three plausible routes, which do we run, which is the alternate, which is the abort? Comparing routes by feel — "this one looks better" — works for an experienced detail leader on familiar ground, but it doesn't survive:

- a personnel change (the next planner doesn't have your context),
- a contracting-office audit ("why this route?"),
- a change in threat conditions (yesterday's "looks fine" is today's "obviously the worst option"),
- the post-incident question ("did we know about this?").

The matrix is what makes those questions answerable.

## Why 5×5 (Not 3×3, Not 7×7)

- **3×3 collapses too much.** Almost every credible motorcade hazard ends up "Medium / Medium." The matrix loses its ability to discriminate between "manageable" and "veto."
- **7×7 invites false precision.** No human analyst meaningfully distinguishes 0.42 likelihood from 0.46 likelihood. The extra resolution is noise that sounds like signal.
- **5×5 is the inflection point.** Each axis fits five tier definitions a planner can write in a sentence each. The product (1–25) maps cleanly onto five risk bands (Low / Moderate / High / Very High / Extreme). It's wide enough to be useful and narrow enough to be honest.

This is consistent with practice across ISO 31000, MIL-STD-882E, and most safety-critical industries. The shape of the matrix isn't an aesthetic choice — it's a calibration choice.

## Likelihood Anchors — Why Each Tier Has a Definition

The L tier definitions in `resources/5x5-risk-matrix.md` are written so each tier requires a *specific anchor*: a documented actor, a documented capability, a dated indicator. A score is a *finding* — it has a rationale that can be challenged. A score without a rationale is decoration.

The most common failure of L scoring is **anchorlessness**: an analyst writes "L=3, possible" because they're worried but cannot say *what* they're worried about. The discipline of "no L≥3 without a named actor" forces the analyst to either pin down what they're worried about (good) or admit they're stretching (also good).

## Impact Anchors — Why Casualty Mechanism, Not Story

The I tier is principal-centric: it asks what the worst plausible outcome to the principal *and the detail* is, not what the press story will look like. This is deliberate. Press stories follow consequences; consequences follow casualty mechanisms. Score the casualty mechanism.

A common mis-score: rating "embarrassing public scuffle" as I=3 because the story would be bad. That is a Significant if it produces a forced abort or principal injury; otherwise it's a Minor (I=2). Conflating the press impact with the casualty impact pulls the matrix off-axis.

## The Inherent / Residual Distinction

This is the single most important habit the workspace tries to build:

- Score **inherent first** (no mitigations).
- Apply each mitigation explicitly to L, I, or both, with rationale.
- Score **residual**.
- Sign off on **residual**.

Why bother with the inherent score? Because it's the *uncountermeasured* number, the one that shows you what would happen if every mitigation simultaneously failed. A route with inherent 20 (Extreme) and residual 9 (Moderate) is a route living entirely on its mitigations — when one of them fails, you're back at 20. A route with inherent 9 and residual 6 is intrinsically lower-risk. Both might be operationally acceptable today; one is far more brittle than the other.

The brief always shows both numbers to surface that brittleness.

## Common Abuse Patterns

### 1. Center Drift
"Everything is L=3, I=3." This is the matrix-version of "no opinion." Refuse it. Demand an anchor for every L≥3 and I≥3.

### 2. Mitigation Theatre
Adding a vehicle does not necessarily reduce ambush *likelihood* — it may reduce *impact*. Be precise about which axis each mitigation affects. Adding mitigations that don't actually move the residual is theatre, and worse, eats budget that could go to mitigations that *would* move it.

### 3. Average-Down
"Average residual is 6, so we're fine." Routes are not the average of their segments. The motorcade has to traverse every segment, including the worst one. Roll-up uses **max residual** plus a tail-risk count of High+ segments — never an average.

### 4. Reverse Engineering
"We've decided to go with River Road, so let me write up the matrix to support it." The order matters: score, then choose. If the choice has been made for non-risk reasons (principal preference, host-nation political demand), document that fact in the decision file. Don't pretend the matrix justified it.

### 5. Number Worship
A residual of 12 (High) with a clear, attributable mitigation plan is operationally safer than an 8 (Moderate) with no plan and no attention. Numbers serve the brief; the brief doesn't serve the numbers.

### 6. Stale Baseline
A baseline older than 14 days has decayed: actors and indicators move faster than that. The workspace's `/risk-score` will refuse to score against an expired baseline. This is a feature, not friction.

## Calibration — Did the Matrix Actually Work?

After every movement, the `/after-action` flow asks: did predicted residual match observed exposure?

- If predicted Moderate, observed felt Moderate: the matrix is calibrated for that hazard.
- If predicted Moderate, observed High (closer to a real attempt than expected): re-anchor that hazard's L tier or capture a missed indicator.
- If predicted High, observed Low (the segment turned out boring): are we over-mitigating? Over-counting indicators? Over-anchoring on a stale incident?

The drift is acceptable up to ±1 band. Beyond that, the anchor definitions need to change, and the recalibration is logged in `planning/calibration-log.md`. This is what keeps the matrix honest over months of use.

## What the Matrix Doesn't Do

- It doesn't estimate cost, political sensitivity, or principal preference. Those go in `/route-compare`'s weights, not in the matrix.
- It doesn't model rare-but-systemic hazards (1-in-10⁵ events). Those are noted as "black-swan considerations" in the brief but kept out of the matrix to avoid flooding it with low-probability noise.
- It doesn't replace operator judgement. It structures the conversation between operator and contracting office; it doesn't make the decision.

## Reading List

- `resources/5x5-risk-matrix.md` — the card.
- `context/for-agent/domain-knowledge.md §1` — methodology.
- `resources/doctrine-references.md` — standards bibliography.
- ISO 31000:2018 §6 — the canonical "establish context → identify → analyse → evaluate → treat" loop the workspace mirrors.
