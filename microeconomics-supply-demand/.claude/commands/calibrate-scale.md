# /calibrate-scale — Anchor the Likelihood and Impact Scales to the User's Business

The single highest-leverage step in the workspace. Anchors the 1–5 (or 1–3 / 1–7) likelihood and impact tiers to *the user's* base rates and units, so every subsequent score is comparable.

## Required Inputs

Walk the user through these sequentially. Skip a section only if the user's `constraints.md` already has a calibration that's still valid.

### Likelihood anchors
For the time horizon set in `context/project.md`, ask:
1. **Tier-1 (Rare):** "What probability range for an event over <horizon> would feel 'rare' to you? Most analysts use < 5%."
2. **Tier-2 (Unlikely):** "How about 'unlikely'? — typically 5–20%."
3. **Tier-3 (Possible):** "...'possible'? — typically 20–50%."
4. **Tier-4 (Likely):** "...'likely'? — typically 50–80%."
5. **Tier-5 (Almost certain):** "...'almost certain'? — typically > 80%."

Confirm the ranges; let the user adjust. Anchor each tier to a **microeconomic example** from the watchlist (e.g., "tier 4 = 'a normal-magnitude harvest shortfall (within ±1σ)'").

### Impact anchors
Ask the user to pick the most decision-relevant impact unit(s):
- **Revenue (annualized $)** — most common.
- **Margin (bps or $)** — when fixed costs are large.
- **Units sold** — for capacity-constrained markets.
- **Operational disruption (days)** — for supply-chain heavy.

For each chosen unit, set 5 thresholds:
1. **Tier-1 (Negligible):** "What dollar (or unit) impact is so small you wouldn't escalate?"
2. **Tier-2 (Minor):** "... noticeable but absorbed in normal variance?"
3. **Tier-3 (Moderate):** "... triggers re-planning?"
4. **Tier-4 (Major):** "... triggers executive escalation and budget revision?"
5. **Tier-5 (Severe):** "... triggers strategic re-alignment, customer impact, regulatory disclosure?"

If using L × I × D, also calibrate detectability:
- **Tier-1:** "Forward / leading indicator gives you ≥ 60-day warning."
- **Tier-3:** "Quarterly review or survey would catch it."
- **Tier-5:** "Visible only after price/quantity has moved (sales data)."

### Risk-appetite bands
Map RPN ranges to color tiers and required actions:
- **Green** (e.g., 1–4 on 5×5): "Monitor in next quarterly review."
- **Yellow** (5–9): "Document treatment plan; assign owner."
- **Amber** (10–15): "Treatment plan + executive notification within 30 days."
- **Red** (16–25): "Immediate treatment + board-level disclosure."

Confirm and adjust per the user's escalation norms.

## Procedure

### Step 1 — Capture the answers in `context/constraints.md`
Update the four scale tables in place. Stamp the date and append a one-paragraph rationale beneath each table ("Anchored against historical Q4 demand declines of 8% (2020) and 5% (2024); tier-3 set to bracket those.").

### Step 2 — Re-score affected scenarios
For each existing scenario card in `outputs/`, re-evaluate the tier mapping under the new scale. If a tier shifts, *do not edit the old card* — write a new dated card and append a "drift" note.

### Step 3 — Append a drift summary to `work-log/<YYYY-MM-DD>.md`
List each re-scored scenario with old tier → new tier and the reason (anchor change, not a re-evaluation of the underlying evidence).

### Step 4 — Update `planning/risk-register.md`
Replace tier values for affected rows; ensure the change is visible in the next `/draft-risk-register` run as a "calibration drift" rather than a substantive risk movement.

## Notes

- **Calibration is not a one-time event.** Re-run this command at least annually, or when a major business change (acquisition, currency, market entry) shifts the units' meaning.
- **Common pitfall:** anchoring impact to the *firm's* size at calibration time but not adjusting as the firm grows. A $5M tier-3 impact on a $100M firm is moderate; on a $5B firm, it's noise.
- **Refusal condition:** if the user wants to score scenarios before calibrating, the agent declines and runs this command first. Uncalibrated scoring is theater.
