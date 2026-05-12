# /score-demand-shock — Score a Demand-Side Disruption

Score a single named demand-side scenario on the calibrated risk matrix. Mirror of `/score-supply-shock` for events that shift the demand curve.

## Required Inputs

1. **Scenario title** — short noun phrase (e.g., "U.S. mild recession 2026", "Private-label entrant at -25%", "EU-wide sugar tax").
2. **Driver category** — pick one (or more):
   - **Income (Y)** — recession, wage-growth surprise, transfer payment change.
   - **Tastes (T)** — preference shift, generational change, viral trend.
   - **Substitute / complement prices (P_r)** — competitor pricing move, complement availability change.
   - **Expectations (E)** — anticipated stockout, inflation expectations.
   - **Population (N)** — segment shrink/grow.
   - **Regulation** — labeling, age restriction, tax/subsidy.
3. **Affected segments** — which customer segments / SKUs see the shift.
4. **Expected duration** — transient or persistent.
5. **Time horizon** — confirm against `context/project.md`.
6. **Best-guess elasticity** — own-price `εd` (how much does Qd respond to P), and the relevant cross-elasticity (`εxy` for substitute-driven, `εY` for income-driven).

## Procedure (follows Workflow B in `context/for-agent/workflows.md`)

### Step 1 — Decompose into curve mechanics
- Direction of demand-curve shift (right = expansion, left = contraction).
- Magnitude (`δQ_d / Q*` as a range).
- Persistence.
- Shape change (does demand also become *more* or *less* elastic?).
- Driver category from above (drives Step 4 evidence).

### Step 2 — Pull supply-side parameters
Supply elasticity `εs` for the affected market, with horizon adjustment.

### Step 3 — Estimate equilibrium response
`ΔP*/P* ≈ shift_size / (εs - εd)`. Sign of `ΔP*` follows the demand direction (down-shift → price down).

Estimate:
- `ΔP*` range
- `ΔQ*` range
- Revenue impact = `ΔP* × Q*` + own-firm volume effect
- Margin impact (more sensitive than revenue if the firm has high fixed costs)
- Consumer surplus change `ΔCS` (only relevant if brand loyalty / customer lifetime value is at stake)

### Step 4 — Score Likelihood (driver-specific evidence)
- **Income-driven** → recession-probability indicators (yield curve, NBER nowcasts, employment data); tier maps to consensus probability of mild/severe recession.
- **Substitute-driven** → substitute pricing moves; substitute launch calendars; analogous historical entries.
- **Taste-driven** → search-volume trends, social-listening, panel surveys.
- **Regulation-driven** → bill stage in legislative pipeline (introduced / committee / passed / signed / rule-making); each stage maps to a tier.
- **Expectations-driven** → consumer/business surveys, futures.

### Step 5 — Score Impact
Map revenue + margin range to calibrated tier in `constraints.md`. Bands welcome.

### Step 6 — Score Detectability (if L × I × D mode)
- Forward markets / leading consumer indicator → D = 1.
- Quarterly survey would catch → D = 3.
- Visible only after sales decline → D = 5.

### Step 7 — Compute composite RPN and tier.

### Step 8 — Suggest treatments
Driver-tailored:
- **Income shock + εY > 1 (luxury)** → diversify SKU mix toward lower-elasticity segments; consider promotional throttle.
- **Substitute entry + high εxy** → loyalty programs; differentiate; pre-emptive grandfathering for top-decile customers.
- **Taste shift** → assortment rebalancing; stage-gate for re-formulation.
- **Regulation** → compliance investment + scenario plan for delayed rule-making.

### Step 9 — Write the scenario card
`outputs/demand-<slug>-<YYYY-MM-DD>.md` mirroring the supply-shock card structure but with the demand-side fields (driver category, segment list, ΔCS section if applicable).

### Step 10 — Append register row + work-log entry.

## Output

Report back: scenario card path, final RPN and tier, single most fragile assumption, suggested next command.
