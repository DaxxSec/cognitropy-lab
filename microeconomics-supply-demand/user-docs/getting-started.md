# Getting Started

Welcome. This workspace turns supply-and-demand analysis into structured, defensible risk scores. Whether you're a sourcing manager, a pricing committee member, a risk analyst, or a strategy lead, the goal is the same: take the questions you'd normally answer with a narrative ("are we exposed to this?") and answer them with a calibrated matrix cell instead.

## In Five Minutes

1. **Run `/onboard`.** Twelve questions. Skip what doesn't apply. The agent populates `context/project.md`, `context/role.md`, and `context/constraints.md`.
2. **Run `/calibrate-scale`.** This is the single most important step in the whole workspace. Without it, every score afterward is theater. Don't skip it; the agent will refuse to score until it's done.
3. **Run `/score-supply-shock` or `/score-demand-shock`** for the first scenario on your watchlist. The agent walks you through curve mechanics → elasticity → equilibrium response → likelihood and impact tiering → composite RPN → suggested treatments.
4. **Iterate.** Each scenario card lands in `outputs/`. The running register grows in `planning/risk-register.md`.
5. **When you're ready to share, run `/draft-risk-register`.** Produces a clean ISO 31000-aligned register snapshot in `outputs/risk-register-<date>.md`, plus CSV/slide variants if you asked for them in onboarding.

## The Core Concept

Most risk matrices fail because their cells are populated by gut feel. The 1–5 likelihood and 1–5 impact tiers get assigned based on what the analyst worries about today, not based on evidence. The result: matrices that look rigorous, are entirely fictional, and produce false confidence.

This workspace fixes that with one move: **elasticity is the bridge.**

- "Likelihood" gets anchored to historical base rates over the same horizon as your matrix. The calibration anchors live in `context/constraints.md`.
- "Impact" gets anchored to *your* business's units (revenue, margin, days of disruption), with thresholds that you set during `/calibrate-scale`.
- "Severity" of any specific scenario then gets *derived* from the elasticity-driven `ΔP*` and `ΔQ*` predictions, not invented.

The result is a register where every row says, in effect: "we expect X to happen with probability anchored to historical base rate Y, the consequence is bounded by elasticity ε with confidence interval Z, and the cell is therefore (L=3, I=4) → score 12 → amber tier." That's auditable.

## What Each Command Does (Plain English)

- **`/onboard`** — Sets up the workspace.
- **`/calibrate-scale`** — Anchors the matrix axes to your business.
- **`/score-supply-shock`** — Score one supply-side scenario.
- **`/score-demand-shock`** — Score one demand-side scenario.
- **`/elasticity-risk-matrix`** — Score a *portfolio* (many SKUs at once) on two elasticity axes; produces a heat map.
- **`/equilibrium-stress-test`** — Quantitative "what if": perturb the supply/demand system and report ΔP*, ΔQ*, surplus changes, deadweight loss.
- **`/cross-elasticity-screen`** — Score substitution risk across a basket of own-products and candidate substitutes.
- **`/draft-risk-register`** — Consolidate everything into one register.

## How Long Does Each Take?

- `/onboard`: 5–10 minutes of conversation.
- `/calibrate-scale`: 15–30 minutes (this is where you do real thinking about your business's units).
- `/score-supply-shock` or `/score-demand-shock`: 10–20 minutes per scenario.
- `/elasticity-risk-matrix`: 30 minutes if you have data; 10 minutes with literature priors.
- `/equilibrium-stress-test`: 20 minutes per scenario.
- `/cross-elasticity-screen`: 20–40 minutes depending on basket size.
- `/draft-risk-register`: 5 minutes (mostly mechanical).

## What If You Have No Data?

You can run the workspace fully in qualitative mode using literature priors. The `resources/elasticity-reference.md` file aggregates published elasticity estimates by category with citations. Your scores will be weaker but useful for triage, and the workspace will mark them as "low evidence" so you don't mistake triage for measurement.

When the stakes go up, invest in real estimation: pull internal price/quantity data and let the agent run a log-log regression. The workspace's quality scales with the data you bring it.

## What If You're New to Risk Frameworks?

That's fine. Tell the agent during `/onboard` (Q8) and it will scaffold the ISO 31000 register fields and define terms as they appear. The workspace is built so that the *methodology* is durable in the files; you don't need to remember it between sessions.

## What If You're New to Microeconomics?

Also fine. The agent will explain elasticity, surplus, equilibrium concepts as they appear. The `context/for-agent/domain-knowledge.md` file is the reference; it's dense, but you don't have to read it cover-to-cover. The agent reads what it needs and surfaces the relevant pieces.

## The Hard Constraints (Worth Reading Once)

- **No price coordination with competitors.** Antitrust hard line. The agent will refuse.
- **No financial / investment advice.** This produces analytical scaffolding for risk assessment, not buy/sell recommendations.
- **No silent cross-horizon aggregation.** Quarterly and 24-month risks live on different matrices.
- **No single-cell answers when input CIs straddle multiple cells.** The matrix shows ranges, and the agent will say so.
- **No score creep without re-anchoring.** If you re-score the same risk later, the workspace dates it and surfaces drift.

## Where to Look When Something Surprises You

- A score feels off → check `context/constraints.md` for the calibration anchors. Probably they need to move.
- An elasticity prior feels wrong → check `resources/elasticity-reference.md` for the source citation; if it's > 10 years old, re-estimate.
- A treatment recommendation feels generic → check whether the elasticity profile in the scenario card matched the treatment-mapping table in `context/for-agent/domain-knowledge.md` §3.4.
- The register has a gap → run `/draft-risk-register` and read the gap report at the top.

## Help and Iteration

The workspace is designed to be edited. If a calibration anchor needs to change, change it. If a slash command needs more steps for your specific situation, add them. The files are yours.

Welcome aboard.
