# /score-supply-shock — Score a Supply-Side Disruption

Score a single named supply-side scenario on the calibrated risk matrix. Produces a scenario card in `outputs/`, appends a row to `planning/risk-register.md`, and updates `work-log/`.

## Required Inputs

Ask the user (or pull from the conversation context):

1. **Scenario title** — short noun phrase (e.g., "Brazil arabica drought 2026", "Midwest wheat harvest below trend").
2. **Driver(s)** — the underlying cause: input cost spike, capacity loss, regulatory shock, weather/climate, geopolitical, technology change.
3. **Affected inputs / capacity** — which inputs are constrained, by what fraction.
4. **Expected duration** — transient (resolves within horizon) or persistent.
5. **Time horizon** — confirm against the horizon set in `context/project.md`. If different, *create a separate scenario card on the matrix for that horizon*; do not merge.
6. **Best-guess supply elasticity** — even a literature-prior range is fine. If unknown, mark as "low-evidence" and recommend acquiring an estimate.

If any of (3), (4), (6) is unknown, record `unknown — assumption: <stated>` and flag in the model-risk column.

## Procedure (follows Workflow A in `context/for-agent/workflows.md`)

### Step 1 — Decompose into curve mechanics
Direction of curve shift, magnitude (`δQ_s / Q*` as a range, not a point), persistence, shape change. Record all four in the scenario card.

### Step 2 — Pull demand-side parameters
Own-price elasticity of demand `εd` for the affected product/segment, with CI. Use horizon-appropriate values (SR vs. LR — see `domain-knowledge.md` §1.6).

### Step 3 — Estimate equilibrium response
First-cut: `ΔP*/P* ≈ shift_size / (εs - εd)`. If both elasticities are small, even a small shock produces a large `ΔP*` — flag.

Estimate:
- `ΔP*` range
- `ΔQ*` range
- Revenue impact = `ΔP* × Q*` (adjusted for pass-through, contracts)
- Margin impact = revenue impact − input-cost increase (if input-cost driven)

### Step 4 — Score Likelihood
Pull from:
- Historical base rate over a comparable window (calibration anchor in `constraints.md`).
- Active leading indicators (port congestion, futures pricing, weather, regulatory pipeline).
- If a leading indicator is already moving, bump L by one tier.

Pick the tier; record the base-rate evidence inline.

### Step 5 — Score Impact
Map the revenue/margin range from Step 3 to the calibrated impact tier in `constraints.md`. If the range straddles two tiers, record both — render as a band on the matrix.

### Step 6 — Score Detectability (only if L × I × D mode)
- Forward markets exist for this input → D = 1.
- Detected via quarterly review → D = 3.
- Visible only post-shock in sales/revenue → D = 5.

### Step 7 — Compute composite RPN
L × I (or L × I × D). Map to the user's risk-appetite band (green/yellow/amber/red).

### Step 8 — Suggest treatments
Map elasticity profile to treatment per `domain-knowledge.md` §3.4:
- Low εd + supply-shock risk → hedge / multi-source / inventory build.
- Low εs + likely demand spike → pre-allocate capacity / supply contracts.
- Pair each treatment with an estimated cost and expected residual L/I if implemented.

### Step 9 — Write the scenario card
Output: `outputs/supply-<slug>-<YYYY-MM-DD>.md` with sections:

```
# Supply Shock Scenario: <title>
**Date scored:** <YYYY-MM-DD> · **Horizon:** <H> · **Scale:** <5x5 L×I>

## Brief
<one paragraph>

## Curve Mechanics
- Shift direction: <left/right>
- Magnitude (δQ_s/Q*): <range>
- Persistence: <transient/persistent>
- Shape change: <none / steeper / flatter>

## Parameters Used
- εs: <range, source>
- εd: <range, source>
- Q*, P*: <baseline>

## Equilibrium Response
- ΔP* range: <±X% to ±Y%>
- ΔQ* range: <range>
- Revenue impact: <$ range>
- Margin impact: <$ range>

## Likelihood
- Tier: <1–5>
- Evidence: <base rate; leading indicators; bump rationale>

## Impact
- Tier: <1–5> (or band <a–b>)
- Mapping: <which calibration row was used>

## (Optional) Detectability
- Tier: <1, 3, 5>
- Rationale: <forward market / quarterly review / post-shock>

## Composite Score
- RPN: <L × I = N>
- Risk appetite tier: <green/yellow/amber/red>

## Suggested Treatments
1. <treatment> — est. cost <$>, residual L/I after: <r_L>, <r_I>
2. ...

## Single Most Fragile Assumption
<one line>

## References
- Source data: <paths>
- Methodology: IEC 31010:2019 §B.29; ISO 31000:2018; <other>
```

### Step 10 — Append register row + log
- Add row to `planning/risk-register.md` with the ISO 31000-aligned schema (`domain-knowledge.md` §2.5).
- Append to `work-log/<YYYY-MM-DD>.md` with timestamp, scenario, score, hardest call.

## Output

The agent reports back in chat:
- Path to the scenario card.
- Final RPN and risk-appetite tier.
- Single most fragile assumption.
- Suggested next command (often `/score-demand-shock` for the demand-side mirror, or `/equilibrium-stress-test` if quantitative impact is needed).
