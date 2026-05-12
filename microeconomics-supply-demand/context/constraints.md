# Constraints, Calibration, and Risk Appetite

> Populated by `/onboard` and `/calibrate-scale`. The agent reads this every time it scores anything; updates here are the highest-leverage tuning lever in the workspace.

## Scoring Scale

Which matrix dimensionality?

- [ ] 3×3 (Low / Med / High on each axis) — fast, suitable for screening
- [ ] **5×5 (1–5 on each axis)** — recommended default; widely supported by GRC tools
- [ ] 7×7 (rare; only when you genuinely have 7 distinguishable tiers)

`[populate via /calibrate-scale]`

Composite score formula:

- [ ] L × I (RPN, 1–25 on a 5×5)
- [ ] L × I × D (Detectability — FMEA-style, 1–125 on 5×5×5; use when "warning lead time" matters, e.g., commodity desks)
- [ ] L + I (additive — discouraged; only if your GRC tool requires it)

## Likelihood Scale (anchored)

The most-skipped step in risk scoring. Anchor each tier to a base-rate range *for the time horizon set in `project.md`*. The numbers below are illustrative — replace with your calibration.

| Tier | Label | Base rate (per the horizon in `project.md`) | Microeconomic anchor |
|---|---|---|---|
| 1 | Rare | < 5% | Requires an unprecedented S/D shock outside historical envelope |
| 2 | Unlikely | 5–20% | Has occurred 1–2× in 10y of comparable conditions |
| 3 | Possible | 20–50% | Occurs in roughly 1 of every 3 comparable horizons |
| 4 | Likely | 50–80% | Has occurred in most comparable horizons; demand/supply elasticity supports a pronounced response |
| 5 | Almost certain | > 80% | Already underway, or structural curve shift already documented |

`[populate via /calibrate-scale]`

## Impact Scale (anchored)

Anchor each tier to *your* business's units, not generic descriptors. "High" is meaningless; "$2–5M EBIT impact" is calibratable.

| Tier | Label | Revenue Impact (annualized) | Margin Impact (bps) | Operational |
|---|---|---|---|---|
| 1 | Negligible | < $X | < Y bps | Routine handling |
| 2 | Minor | $X – $X | Y – Y bps | Notable but absorbed |
| 3 | Moderate | $X – $X | Y – Y bps | Triggers re-planning |
| 4 | Major | $X – $X | Y – Y bps | Triggers escalation; budget revision |
| 5 | Severe | > $X | > Y bps | Strategic re-alignment, customer impact, regulatory exposure |

`[populate via /calibrate-scale]`

## Detectability Scale (only if using L × I × D)

| Tier | Label | Microeconomic anchor |
|---|---|---|
| 1 | Easily detected | Leading indicator (futures curve, PMI, search trends) gives ≥ 60-day warning |
| 3 | Moderately detected | Detected by quarterly review; ≤ 30-day warning |
| 5 | Hard to detect | Visible only after equilibrium has shifted (price/quantity already moving) |

`[populate via /calibrate-scale]`

## Risk Appetite Bands

Once a cell is scored, what action does the score force? Anchor the bands to your appetite.

| RPN range (5×5, L×I) | Tier | Mandatory action |
|---|---|---|
| 1–4 | Green | Monitor in next quarterly review |
| 5–9 | Yellow | Document treatment plan; assign owner |
| 10–15 | Amber | Treatment plan + executive notification within 30 days |
| 16–25 | Red | Immediate treatment + board-level disclosure |

`[populate via /calibrate-scale]`

## Methodological Constraints

These are non-negotiable rules the agent must follow:

1. **Never score without a stated assumption.** If elasticity is unknown, the cell is a *range*, not a point — and the assumption must say "literature prior, source: X" or "internal estimate, CI [a, b]."
2. **Never aggregate scores across horizons.** Quarterly and 24-month risks live on different matrices.
3. **Never compute a composite RPN that mixes parametric and structural risk in the same row.** Structural risks (curve shifts) are scored separately from movements along the curve.
4. **Never present a single-cell answer when the input CIs straddle multiple cells.** Render the range; flag the analyst's choice if they want a point.
5. **Never recommend cross-firm coordination on price.** This is an antitrust hard line. If a user asks for it, refuse and explain.

## Out-of-Scope Use Cases

The workspace is not the right tool for:

- **Macroeconomic / general equilibrium analysis.** Use a CGE or DSGE framework.
- **Personal investment advice.** This produces analytical scaffolding, not buy/sell recommendations.
- **Pricing across competitors / market division.** Antitrust hard line (above).
- **Quantitative VaR / CVaR financial risk modeling.** This workspace produces ordinal matrix scores, not parametric loss distributions. Pair with a quant-risk model if you need both.
