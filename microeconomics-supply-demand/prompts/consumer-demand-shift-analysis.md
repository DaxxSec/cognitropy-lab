# Prompt — Consumer Demand-Shift Analysis

> Use case: a product or strategy team needs to quantify the risk that a named consumer trend (recession, generational taste change, regulatory or platform shift) materially moves their demand curve. This prompt structures the analysis from qualitative trend → elasticity decomposition → matrix score → suggested treatments.

## When to Use

- A consumer-research signal (panel, survey, social listening) suggests a preference shift.
- A macro indicator (employment, sentiment, real income) is moving and you want to bound exposure.
- A platform / channel partner announces a change (e.g., new Amazon fee structure, EU DMA gatekeeper rules) that may bend demand for your category.

## Inputs the Prompt Expects

- The trend or shift name (`[TREND]`).
- Driver category — Income / Tastes / Substitutes / Expectations / Population / Regulation (`[DRIVER]`).
- Affected segments / SKUs (`[SEGMENTS]`).
- Time horizon (`[HORIZON]`).
- Available evidence: panels, surveys, macro series, leading indicators (`[EVIDENCE]`).
- Reference: `context/constraints.md` (calibration), `resources/elasticity-reference.md` (priors).

## Prompt Body

```
Analyze the consumer demand-shift risk: "[TREND]".

Driver category: [DRIVER]
Affected segments: [SEGMENTS]
Horizon: [HORIZON]
Available evidence: [EVIDENCE]

Step 1 — Translate the trend into curve-shift language.
  Direction (right/left). Magnitude (best estimate as a range δQd/Q*).
  Persistence (transient/persistent). Shape change (does demand also
  become more or less elastic).

Step 2 — Pull the relevant elasticity:
  - For [DRIVER]=Income: income elasticity εY by segment.
  - For [DRIVER]=Substitutes: cross-elasticity εxy to the named substitute.
  - For [DRIVER]=Tastes/Regulation/Expectations: own-price εd plus a
    shift-magnitude estimate (no closed-form elasticity captures the
    structural component alone).
  Use horizon-appropriate values; SR ≠ LR.

Step 3 — Score Likelihood per the [DRIVER]-specific evidence in
  context/for-agent/workflows.md Step 4 of Workflow B. Cite the evidence.

Step 4 — Score Impact:
  - Estimate ΔP*, ΔQ* using ΔP*/P* ≈ shift / (εs - εd).
  - Compute revenue impact, margin impact, and ΔCS if brand loyalty matters.
  - Map to the calibrated impact tier in constraints.md.

Step 5 — Compute composite RPN; map to risk-appetite tier.

Step 6 — Suggest treatments tailored to the driver:
  - Income shock + εY > 1: SKU mix toward lower-elasticity segments.
  - Substitute entry + high εxy: loyalty / differentiation / pre-emptive
    grandfathering.
  - Taste shift: assortment rebalance; stage-gate for re-formulation.
  - Regulation: compliance investment + delayed-rule contingency plan.

Step 7 — Flag the single most fragile assumption.

Output:
  - A scenario card in outputs/demand-<slug>-<date>.md following the
    schema in /score-demand-shock.
  - A new register row in planning/risk-register.md.
  - A 3-bullet stakeholder summary (audience: per context/role.md).

Hard constraints:
  - Don't conflate parametric (price-driven volume change) with structural
    (curve shift). Score them separately if both are present in [TREND].
  - If the evidence base is thin (one survey, one social-listening signal),
    label the score "low evidence" and recommend a confirming data pull
    before treatment investments are made.
  - Refuse to publish a single-cell point if input CIs straddle multiple
    cells — render as a band.
```

## Expected Output

- One scenario card.
- One register row.
- A short stakeholder summary.
- Recommended next command (often `/cross-elasticity-screen` if the driver was substitute-related, or `/equilibrium-stress-test` for quantitative impact).
