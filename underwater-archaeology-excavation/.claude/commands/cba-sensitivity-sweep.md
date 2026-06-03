# /cba-sensitivity-sweep

Stress-test a completed cost-benefit analysis against its key assumptions, so the recommendation is presented with its robustness, not as a single fragile number.

## Inputs

- A completed CBA (from `/insitu-vs-excavate`) with its component costs and benefits.
- The assumptions to vary: discount rate, conservation cost multiple, threat probability, significance weighting, weather downtime, day-rates.
- Plausible ranges (low / central / high) for each assumption.

## Steps

1. Identify the **decision variable** — the quantity whose sign flips the recommendation (usually net present value or the benefit-cost ratio).
2. Run a **one-at-a-time** sweep: vary each assumption across its range holding others central; record the decision variable.
3. Build a **tornado chart** (ordered by impact) to show which assumptions actually move the decision.
4. For the top drivers, run a small **scenario / Monte Carlo** pass: sample jointly and report the probability the recommendation holds.
5. Identify any **switching point** — the assumption value at which preserve flips to excavate (e.g. "excavation only wins if the discount rate exceeds 5%").
6. State whether the recommendation is **robust** (holds across plausible ranges) or **fragile** (flips), and if fragile, recommend buying information (a cheap evaluation phase) before committing.
7. Keep aleatoric and epistemic uncertainty separate in the report.

## Output

`outputs/cba-sensitivity-<site>-YYYY-MM-DD.md`: the tornado of drivers, the switching points, the scenario/Monte-Carlo probability the recommendation holds, and a robust/fragile verdict with a next step.

## Notes

- The discount rate and the conservation-cost multiple are almost always among the top drivers — sweep them first.
- A recommendation with no sensitivity analysis collapses the first time a funder questions an assumption; this command is what makes it defensible.
- If the result is fragile, the rational move is often a cheap evaluation phase to shrink the driving uncertainty, not a coin-flip commitment.
