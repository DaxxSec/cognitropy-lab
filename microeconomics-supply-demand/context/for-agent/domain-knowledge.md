# Domain Knowledge — Microeconomic S&D + Risk Scoring Matrices

This is the agent's working reference. It is intentionally dense; the agent should re-read sections relevant to the active scenario before publishing a score.

## Part 1 — Supply and Demand: The Core Apparatus

### 1.1 Demand Function

Quantity demanded is a function of own price `P`, prices of related goods `P_r`, income `Y`, preferences `T`, expectations `E`, and population `N`:

```
Qd = D(P, P_r, Y, T, E, N)
```

In partial equilibrium analysis, we hold all but `P` fixed and write `Qd = D(P)`. A *change in P* moves us along the curve (parametric risk). A *change in any other argument* shifts the curve (structural risk). This distinction is the spine of the workspace's risk decomposition.

### 1.2 Supply Function

Quantity supplied is a function of own price, input prices `W`, technology `A`, expectations `E`, taxes/subsidies `τ`, and number of producers `M`:

```
Qs = S(P, W, A, E, τ, M)
```

Same parametric/structural distinction applies — a price move walks along the curve; an input cost move (`W↑`) shifts the curve leftward.

### 1.3 Market Equilibrium

Equilibrium price `P*` and quantity `Q*` satisfy `D(P*) = S(P*)`. Comparative statics asks: when an exogenous parameter changes, how do `P*` and `Q*` move? The signs and magnitudes are direct inputs to impact scoring.

| Shift | ΔP* | ΔQ* | Mnemonic |
|---|---|---|---|
| Demand ↑ (rightward) | + | + | Both up |
| Demand ↓ (leftward) | − | − | Both down |
| Supply ↑ (rightward) | − | + | Cheaper, more |
| Supply ↓ (leftward) | + | − | Costlier, less |

Magnitudes depend on elasticities; see §1.5.

### 1.4 Surplus

- **Consumer surplus (CS)**: area between demand curve and price, up to Q*.
- **Producer surplus (PS)**: area between price and supply curve, up to Q*.
- **Total welfare**: CS + PS (in partial-equilibrium, no externalities).
- **Deadweight loss (DWL)**: welfare destroyed by a tax, quota, price ceiling/floor, or other wedge.

For the workspace, `ΔCS` and `ΔPS` under a scenario become candidate impact magnitudes — denominated in the user's revenue or margin units after a calibration step.

### 1.5 Elasticity (the single most important concept here)

Elasticity = % change in one variable / % change in another. It is *unitless*, which is what makes it the bridge between economics and risk scoring.

**Own-price elasticity of demand:**
```
εd = (ΔQd/Qd) / (ΔP/P)
```

| Range | Label | Risk implication |
|---|---|---|
| `εd = 0` | Perfectly inelastic | Price moves don't affect Qd; supply-shock impact on revenue ≈ ΔP × Q (large) |
| `0 > εd > -1` | Inelastic | Revenue moves with price (price ↑ → revenue ↑) |
| `εd = -1` | Unit elastic | Revenue invariant to price |
| `εd < -1` | Elastic | Revenue moves opposite price (price ↑ → revenue ↓) |
| `εd → -∞` | Perfectly elastic | Any price ↑ destroys all demand (commodity-like) |

**Cross-price elasticity of demand:**
```
εxy = (ΔQx/Qx) / (ΔPy/Py)
```
- `εxy > 0` ⇒ substitutes (Pepsi/Coke).
- `εxy < 0` ⇒ complements (printers/ink).
- `εxy ≈ 0` ⇒ unrelated.

**Income elasticity of demand:**
```
εY = (ΔQ/Q) / (ΔY/Y)
```
- `εY < 0` ⇒ inferior good (demand falls as income rises).
- `0 < εY < 1` ⇒ normal necessity.
- `εY > 1` ⇒ normal luxury.

**Own-price elasticity of supply:**
```
εs = (ΔQs/Qs) / (ΔP/P)
```
Always ≥ 0 in standard models. Higher εs ⇒ supply responds easily ⇒ supply-shock impact on price is *smaller*.

**Equilibrium price impact under a curve shift** — useful approximation for `/equilibrium-stress-test`:

```
ΔP*/P* ≈ (shift_size) / (εs - εd)
```
where `εd < 0` so `(εs - εd) > 0`. The agent should walk the user through this when reporting stress-test outputs.

### 1.6 Time-Horizon Effects on Elasticity

Critical for matrix calibration:

- **Short run:** elasticities are *smaller* (less time to substitute, retool, switch). A 90-day matrix should use SR elasticities.
- **Long run:** elasticities are *larger* (consumers find substitutes, producers add capacity). A 24-month matrix should use LR elasticities.
- Mixing horizons silently is the most common scoring error in this workspace.

### 1.7 Common Failure Modes (Microeconomics Side)

- **Cobweb dynamics** — supply lags create oscillating equilibria (agriculture). A static comparative-statics score under-states variability.
- **Giffen / Veblen goods** — upward-sloping demand. Rare, but flag if user is in luxury or staple-of-poor-households markets.
- **Network effects** — demand depends on installed base; static elasticity is misleading.
- **Hysteresis** — demand doesn't return to baseline after a shock (brand damage from substitution).
- **Strategic interaction** — oligopoly responses (Cournot, Bertrand) make own-price elasticity endogenous; for ≤4-firm markets, flag this and use ranges, not points.

## Part 2 — Risk Scoring Matrices

### 2.1 Anatomy of a Matrix

A risk matrix is a 2D grid:

- **Rows = likelihood tiers** (1–5 typical), each anchored to a probability range *over a defined horizon*.
- **Columns = impact tiers** (1–5 typical), each anchored to a magnitude range in the user's units.
- **Cells = risk scores** = combination of tiers (most commonly L × I, sometimes L + I; FMEA adds D for L × I × D).
- **Color tiers** = risk-appetite bands mapping score ranges to action requirements.

### 2.2 Scoring Formulas

| Formula | Range (5×5) | When to use |
|---|---|---|
| L × I (RPN) | 1 – 25 | Default for ISO 31000-style operational risk |
| L × I × D (FMEA) | 1 – 125 | When detection lead-time is critical (commodity desks, IT incident management) |
| L + I | 2 – 10 | Discouraged; only if a target GRC tool requires it |

### 2.3 Calibration Anchors

A matrix is only as good as its anchors. Common anti-patterns:

- **"High" with no number.** Forces interpretation; produces inconsistency across analysts.
- **Anchors borrowed from another business.** A $10M revenue company and a $10B revenue company cannot share an impact scale.
- **Mismatched horizons.** A "Likely (50–80%)" row applied to "next year" and "next decade" measures different worlds.
- **Implicit log-scale.** If tier-2 = $1M and tier-3 = $5M, that's already a log-ish scale; analysts should know.

The workspace forces anchor declaration in `context/constraints.md` and refuses to score until they're populated.

### 2.4 Heat Map Color Conventions

Default 5×5 mapping (mirrors COSO ERM):

| RPN | Tier | Color |
|---|---|---|
| 1–4 | Low | Green |
| 5–9 | Medium-low | Yellow |
| 10–15 | Medium-high | Amber |
| 16–25 | High | Red |

These should be overridden by the user's risk appetite bands in `constraints.md`.

### 2.5 Risk Register Schema (ISO 31000-aligned)

Each register row contains:

| Field | Description |
|---|---|
| ID | Stable identifier (R-2026-001 format) |
| Title | Short scenario name |
| Cause | Upstream driver(s) — usually a curve-shift parameter |
| Event | The market state change |
| Consequence | Downstream impact in the user's units |
| Inherent L | Likelihood before treatment |
| Inherent I | Impact before treatment |
| Inherent RPN | L × I (or L × I × D) |
| Existing controls | Hedges, alternate suppliers, contractual price collars |
| Residual L / I / RPN | After existing controls |
| Treatment plan | Avoid / Reduce / Transfer / Accept |
| Owner | Single named person |
| Review date | When the row gets re-scored |
| Assumption / model risk | The single most fragile assumption |
| Microeconomic anchor | The elasticity, surplus, or curve-shift evidence |

The "microeconomic anchor" column is what differentiates this workspace from a generic operational risk register.

### 2.6 Common Failure Modes (Risk-Matrix Side)

- **False precision.** L=3, I=4 → RPN=12 looks scientific; it's an ordinal × ordinal product. Document the underlying ranges.
- **Risk inversion (Cox 2008).** Two risks with the same RPN may have very different actionable profiles (low-L/high-I vs. high-L/low-I). The workspace forces both axes to be reported, never just the product.
- **Anchoring bias.** Analysts under-score scenarios they have no historical experience with; the workspace's `/score-supply-shock` and `/score-demand-shock` flows include a "what would have to be true for this to be a higher tier" prompt to mitigate.
- **Score creep.** Re-scoring the same risk in successive reviews tends to drift toward the median. The workspace stamps every score with date + assumption, making drift visible.

## Part 3 — Bridge: How Microeconomics Populates the Matrix

This is the *point* of the workspace. The mappings below are the agent's translation layer.

### 3.1 Likelihood Anchors from Microeconomic Evidence

| Evidence type | Likelihood signal |
|---|---|
| Historical frequency of analogous shocks (last 10y) | Direct base-rate input |
| Futures curve / forward markets pricing the event | Implied probability — calibrate against historical realized |
| Observable leading indicator already moving (PMI, search volume, port congestion) | Bumps L by 1 tier |
| εs near zero in short run + plausible supply shock | High L for sharp price response |
| εd near zero + plausible demand shift | High L for sharp price response |
| Structural curve-shift driver already in regulation/legal pipeline | High L conditional on rule taking effect |

### 3.2 Impact Anchors from Microeconomic Evidence

| Evidence type | Impact signal |
|---|---|
| `ΔP* × Q*` under stress test | Direct revenue impact estimate |
| `ΔCS` for B2C with brand-loyalty implications | Add brand-damage column |
| `ΔPS` for own-firm | Direct margin impact |
| Deadweight loss under intervention scenario | Used for regulatory-impact assessments |
| Cross-elasticity high to a substitute that's about to enter | Impact tier ≥ 3 by default |
| Income elasticity > 1 + recession scenario | Impact tier ≥ 3 by default |

### 3.3 Detectability Anchors (FMEA mode)

| Evidence type | Detectability |
|---|---|
| Forward / futures market gives ≥ 60-day signal | D = 1 (easy) |
| Quarterly demand survey would show shift | D = 3 (moderate) |
| Visible only after price/quantity has already moved (sales data) | D = 5 (hard) |

### 3.4 Treatment Recommendations from Elasticity Profile

| Profile | Recommended treatment |
|---|---|
| `εd` near 0 + supply-shock risk | Hedge / multi-source / inventory build (price will pass through but volume holds) |
| `εd` very negative + demand-shock risk | Diversify SKU mix toward lower-elasticity segments; consider grandfathering prices |
| `εxy` high to known substitute | Differentiate / loyalty programs; monitor substitute pricing as leading indicator |
| `εY` > 1 + macro downside | Stress-test EBIT under a 5–10% income decline scenario |
| `εs` near 0 + likely demand spike | Pre-allocate capacity / supply contracts; large `ΔP*` likely |

## Part 4 — Reading List the Agent Should Cite Precisely

When the agent invokes a methodology, it cites the specific source — not just "best practice."

- **ISO 31000:2018** — risk register structure, treatment vocabulary.
- **IEC 31010:2019 §B.29** — risk matrix construction; §B.5–B.10 — scenario analysis; §B.13 — Bow-tie (use for cause-event-consequence decomposition).
- **NIST SP 800-30 Rev. 1** — qualitative and semi-quantitative scoring tiers (Appendix I).
- **COSO ERM Framework (2017)** — risk-appetite vocabulary and heat-map norms.
- **Cox, L.A. Jr. (2008)** — *"What's Wrong with Risk Matrices?"* Risk Analysis 28(2). Read before publishing any matrix; the workspace mitigates the named failure modes but cannot eliminate them.
- **Marshall, Hicks, Slutsky, Tirole, Varian** — see README.
- **Berry, Levinsohn, Pakes (1995)** — BLP demand estimation, when the user has share data and wants to estimate cross-elasticities empirically.
- **Goolsbee & Petrin (2004)** — applied elasticity estimation example (cable TV substitution); useful prior for B2C goods.
- **Hausman (1996)** — applied estimation of price indexes / elasticities for differentiated goods.
