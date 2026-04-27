# Risk Matrix Templates and Calibration Reference

Templates for the three matrix dimensionalities the workspace supports, plus the threshold tables that map continuous economic inputs (elasticity, surplus delta, ΔP*) to discrete tiers.

## 1. Matrix Templates

### 1.1 — 3×3 Screening Matrix

For fast triage, not for register publication.

|              | Impact L (1) | Impact M (2) | Impact H (3) |
|---|---|---|---|
| Likelihood H (3) | 3 (Y) | 6 (A) | 9 (R) |
| Likelihood M (2) | 2 (G) | 4 (Y) | 6 (A) |
| Likelihood L (1) | 1 (G) | 2 (G) | 3 (Y) |

Bands: 1–2 Green, 3–4 Yellow, 5–6 Amber, 7+ Red. Adjust per `constraints.md`.

### 1.2 — 5×5 Default Matrix (recommended)

|              | I=1 | I=2 | I=3 | I=4 | I=5 |
|---|---|---|---|---|---|
| L=5 | 5  | 10 | 15 | 20 | 25 |
| L=4 | 4  | 8  | 12 | 16 | 20 |
| L=3 | 3  | 6  | 9  | 12 | 15 |
| L=2 | 2  | 4  | 6  | 8  | 10 |
| L=1 | 1  | 2  | 3  | 4  | 5  |

Default bands: 1–4 Green, 5–9 Yellow, 10–15 Amber, 16–25 Red. Override in `constraints.md`.

### 1.3 — 7×7 Granular Matrix

Use only when there are genuinely 7 distinguishable tiers per axis. Most teams cannot defend a 7×7 calibration; default to 5×5.

|     | I=1 | I=2 | I=3 | I=4 | I=5 | I=6 | I=7 |
|---|---|---|---|---|---|---|---|
| L=7 | 7 | 14 | 21 | 28 | 35 | 42 | 49 |
| L=6 | 6 | 12 | 18 | 24 | 30 | 36 | 42 |
| L=5 | 5 | 10 | 15 | 20 | 25 | 30 | 35 |
| L=4 | 4 |  8 | 12 | 16 | 20 | 24 | 28 |
| L=3 | 3 |  6 |  9 | 12 | 15 | 18 | 21 |
| L=2 | 2 |  4 |  6 |  8 | 10 | 12 | 14 |
| L=1 | 1 |  2 |  3 |  4 |  5 |  6 |  7 |

Suggested bands: 1–8 Green, 9–18 Yellow, 19–32 Amber, 33+ Red.

### 1.4 — FMEA-Style L × I × D (1–125)

When using AIAG-VDA FMEA for L × I × D, the cube is conceptually:
```
RPN = Severity (I) × Occurrence (L) × Detection (D)
```
Range 1–125 (5×5×5). Common bands:
- 1–24: Green
- 25–49: Yellow
- 50–99: Amber
- 100–125: Red

Note: AIAG-VDA recommends Action Priority (AP — High/Medium/Low) over RPN for new analyses; the workspace supports both. Cite which method the user chose in the scenario card.

## 2. Elasticity → Tier Threshold Tables

### 2.1 Own-Price Elasticity of Demand (`εd`) — used as price-sensitivity *impact* when scoring potential price actions

| εd range | Tier | Label |
|---|---|---|
| `εd > -0.5` | 1 | Very inelastic |
| `-1.0 < εd ≤ -0.5` | 2 | Inelastic |
| `-1.5 < εd ≤ -1.0` | 3 | Near-unit |
| `-2.5 < εd ≤ -1.5` | 4 | Elastic |
| `εd ≤ -2.5` | 5 | Very elastic |

### 2.2 Cross-Price Elasticity (`εxy`) — substitution-risk axis

| εxy range | Tier | Label |
|---|---|---|
| `εxy < 0.1` | 1 | Negligible substitution |
| `0.1 ≤ εxy < 0.3` | 2 | Weak substitution |
| `0.3 ≤ εxy < 0.7` | 3 | Moderate substitution |
| `0.7 ≤ εxy < 1.5` | 4 | Strong substitution |
| `εxy ≥ 1.5` | 5 | Severe substitution |

For complements (`εxy < 0`), use the same magnitude bands with the "complement-loss" label.

### 2.3 Income Elasticity (`εY`) — macro-cycle vulnerability axis

| εY range | Tier | Label |
|---|---|---|
| `εY < 0` | 1–2 (depending on |εY|) | Inferior good — counter-cyclical (low risk in recession, possible benefit) |
| `0 ≤ εY < 0.5` | 1 | Insensitive necessity |
| `0.5 ≤ εY < 1.0` | 2 | Normal necessity |
| `1.0 ≤ εY < 1.5` | 3 | Mild luxury |
| `1.5 ≤ εY < 2.5` | 4 | Luxury |
| `εY ≥ 2.5` | 5 | Highly cyclical |

### 2.4 Supply Elasticity (`εs`) — supply-rigidity axis

| εs range | Tier | Label |
|---|---|---|
| `εs > 2.0` | 1 | Highly elastic — small price impact from supply shocks |
| `1.0 < εs ≤ 2.0` | 2 | Elastic |
| `0.5 < εs ≤ 1.0` | 3 | Moderate |
| `0.1 < εs ≤ 0.5` | 4 | Inelastic |
| `εs ≤ 0.1` | 5 | Highly inelastic — large price impact from any supply shock |

Note: SR εs typically much smaller than LR εs. Re-tier when horizon changes.

### 2.5 Equilibrium Price Impact (`|ΔP*/P*|`) — for stress-test impact mapping

| `|ΔP*/P*|` | Tier | Label |
|---|---|---|
| `< 2%` | 1 | Negligible |
| `2–5%` | 2 | Minor |
| `5–10%` | 3 | Moderate |
| `10–25%` | 4 | Major |
| `> 25%` | 5 | Severe |

Override per industry — commodities tolerate larger swings; subscription pricing does not.

## 3. Calibration Worked Example

A direct-to-consumer specialty coffee brand, $40M annual revenue, 14 SKUs:

- **Likelihood horizon:** 1–4 quarters.
- **Impact unit:** annualized revenue.
- **Impact tiers** (anchored): T1 < $200K · T2 $200K–$1M · T3 $1M–$3M · T4 $3M–$8M · T5 > $8M.
- **Likelihood tiers** (anchored to historical Q-over-Q events of comparable magnitude in the last 8 years): T1 < 5% · T2 5–20% · T3 20–50% · T4 50–80% · T5 > 80%.
- **Risk-appetite bands:** as default.
- **Notes:** "Tier 4 anchored against the 2020 ground-coffee margin compression event; tier 5 reserved for events without precedent in our history (e.g., a category-wide regulatory ban)."

This example is illustrative; the user's `/calibrate-scale` invocation produces the live version in `context/constraints.md`.

## 4. Anti-Patterns to Refuse

- **Color without numbers.** A red cell with no numeric tier in it is not a risk score.
- **Implicit log scales without disclosure.** If tier-2 = $1M and tier-3 = $5M, document that the scale is geometric, not linear.
- **Single-digit summaries presented as decisive.** RPN = 12 sounds precise; without the L and I components, it isn't.
- **Cross-horizon aggregation.** Quarterly and 24-month risks cannot share a matrix without distortion.
