# Prompt — Commodity Supply-Chain Screen

> Use case: a procurement or supply-chain analyst needs a quick triage of upstream commodity exposures before diving into per-input scoring. This prompt produces a prioritized worksheet of supply-side risks across the basket of inputs that feed a product line.

## When to Use

- Quarterly sourcing review.
- After a notable shock to one input (price spike, port disruption, regulatory change), to check what *else* might be exposed via correlation.
- Before a contract negotiation cycle, to identify which inputs are the leverage points.

## Inputs the Prompt Expects

- Product line or SKU family in scope (`[PRODUCT_LINE]`).
- List of major inputs feeding it, with rough cost-share weights (`[INPUT_LIST]`).
- Time horizon for the screen (`[HORIZON]`).
- Whether you have access to forward/futures markets for any of these inputs (`[FORWARD_MARKETS]`).
- Reference: `context/constraints.md` (calibration), `resources/elasticity-reference.md` (priors).

## Prompt Body

```
Run a commodity supply-chain risk screen for [PRODUCT_LINE] over [HORIZON].

Inputs to screen, with cost-share weights:
[INPUT_LIST]

Forward markets available for: [FORWARD_MARKETS]

For each input:
  1. Classify input-supply elasticity tier (1–5) using literature priors from
     resources/elasticity-reference.md if no internal data exists. Cite the
     prior.
  2. Identify the top 1–2 supply-shock scenarios specific to that input
     (weather, regulation, geopolitical, capacity). Pull from the watchlist
     in context/project.md if any apply; add new ones as needed.
  3. For each scenario, score quick-and-dirty Likelihood × Impact on the
     calibrated 5×5 in context/constraints.md. Use ranges, not points.
  4. Rank inputs by max(RPN) across their scenarios.

Output:
  - A markdown table: input | cost-share | top scenario | L | I | RPN | tier
  - The top-3 inputs by RPN get full /score-supply-shock cards generated
    in outputs/.
  - A 3-bullet executive summary suitable for the next sourcing meeting.

Hard constraints:
  - No competitor / supplier price coordination recommendations.
  - Flag any input where the literature prior is older than 2015 — those
    scores are "low evidence" and need re-estimation before publication.
  - Note any input that is a complement to another in the basket
    (e.g., flour + sugar in baking) — joint shocks score differently
    from independent ones.
```

## Expected Output

A two-page markdown brief with:
- Ranked input table.
- Top-3 input scenario cards (or stubs for the user to complete).
- Executive summary.
- Recommendations for the next two scoring commands to run.
