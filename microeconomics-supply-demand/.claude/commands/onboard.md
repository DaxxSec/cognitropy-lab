# /onboard — Initialize the Microeconomics S&D Risk-Scoring Workspace

Welcome. I'll interview you to populate `context/project.md`, `context/role.md`, and `context/constraints.md`. Skip questions that don't apply; nothing here is required to be answered now.

## Interview Flow (12 questions, ~10 minutes)

### 1. Market scope
What market are we scoring? Be as specific as possible — give me the product or product family, geography, channel, and customer segment if relevant.
→ Save to `context/project.md` § Market / Product Scope.

### 2. Time horizon
What's the time window for these scores? (Quarterly / 1–4 quarters / 12–36 months — or your own definition.) If you have multiple horizons in mind, name them all; we'll create separate matrices.
→ Save to `context/project.md` § Time Horizon.

### 3. Decision being informed
What decision will this risk register feed? (Hedging? SKU pricing? Capacity planning? Board reporting?) The decision drives how we present outputs.
→ Save to `context/project.md` § Decision This Will Inform.

### 4. Audience
Who reads the register? (Yourself? Cross-functional team? CFO? Risk committee? Board?) This calibrates vocabulary.
→ Save to `context/project.md` § Stakeholder Audience.

### 5. Data availability
For each, do you have it? (a) Internal price/quantity time series; (b) promotional/discount history; (c) competitor pricing; (d) macro/income data; (e) cost-of-goods history.
→ Save to `context/project.md` § Data Available for Empirical Estimation.

### 6. Watchlist scenarios
Name the scenarios you already worry about. Don't filter. We'll score them all, including the ones you suspect are low-risk — those are usually the most informative.
→ Save to `context/project.md` § Known Watchlist Scenarios.

### 7. Out of scope
What's explicitly not being scored here? (E.g., cyber, FX, employment law.) Documenting this prevents the matrix from being misread.
→ Save to `context/project.md` § Out of Scope.

### 8. Your background
Two parts: (a) familiarity with microeconomics — limited / working / expert; (b) familiarity with risk frameworks — new / one (specify) / multiple. I'll calibrate vocabulary to your level.
→ Save to `context/role.md`.

### 9. Decision rights
What can you decide unilaterally vs. recommend? (E.g., "I can recommend hedge ratios but CFO signs off"; "I can re-price within ±5%.") Affects treatment recommendations.
→ Save to `context/role.md` § Decision Rights.

### 10. Output preference
Markdown registers + heat map PNGs (default)? CSV for GRC import (which tool)? Slide-ready bullets? Long-format for BI?
→ Save to `context/role.md` § Output Format Preference.

### 11. Pushback level
How much should I challenge your scoring? Light (record what you say) / Moderate (probe assumptions, suggest alternatives — recommended) / Aggressive (steelman counter-positions every time).
→ Save to `context/role.md` § How Aggressively Should the Agent Push Back.

### 12. Scoring scale
Which matrix? 3×3 (screening) / **5×5 (default)** / 7×7. And which formula? **L × I (RPN)** / L × I × D (FMEA-style, when detectability/lead time matters) / L + I (only if your GRC tool requires it).
→ Save to `context/constraints.md` § Scoring Scale.

## Post-Onboard Actions

After capturing the answers, I will:

1. **Run `/calibrate-scale`** — anchor the 1–5 likelihood and impact tiers to *your* business's units. This is non-optional; uncalibrated matrices are noise.
2. **Draft `planning/plan.md`** — list the watchlist scenarios from Q6 with placeholder slots for each scoring command they'll require.
3. **Write the Day 1 entry** in `work-log/<YYYY-MM-DD>.md` capturing the onboarding conversation.
4. **Suggest a sequence**: usually start with `/score-supply-shock` or `/score-demand-shock` for the top 3 watchlist scenarios, then `/elasticity-risk-matrix` once you have at least 5 SKU-level elasticity estimates, then `/draft-risk-register` to consolidate.
5. **Flag any data gaps** — if Q5 returned mostly "no," I'll suggest the lowest-effort data acquisitions to unlock empirical scoring.

## Notes

- I will not score anything during `/onboard`. Calibration and the first scenario card start in the next command.
- If you don't know the answer to a question, say "skip" — I'll mark it `[populate later]` and move on.
- The scoring scale (Q12) is the single hardest decision to change later. If unsure, default to 5×5 with L × I; that's the most-tooling-compatible choice.
