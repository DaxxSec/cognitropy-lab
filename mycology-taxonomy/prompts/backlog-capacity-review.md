# Backlog Capacity Review

## Purpose

Use this prompt for a periodic (weekly/monthly) capacity review of the determination pipeline — to find the bottleneck, project the backlog, and decide where to add capacity before a deadline forces a scramble.

## Prompt Template

```
You are a fungarium pipeline manager. Run a capacity review of our determination backlog and tell me where it's failing.

Here is the pipeline state:

- **Arrivals:** [λ specimens/week, and variability if known]
- **Stages & service rates:** [accession μ, sequencing μ, curation μ — per difficulty tier if available]
- **Servers per stage:** [curators c, sequencer slots/plates per cycle]
- **Current backlog (WIP):** [per stage]
- **Current mean turnaround:** [overall and per tier if known]
- **Deadline / target:** [clear-by date, or "steady state"]

Please:
1. Compute utilization ρ per stage and identify the bottleneck (Theory of Constraints).
2. Flag any stage at ρ ≥ 0.85 (danger) or ρ ≥ 1 (unbounded growth).
3. Project the backlog trajectory and clearance date under current capacity; compare to the deadline.
4. Use Erlang-C / Kingman as appropriate given the variability; state which and why.
5. Give 2–3 concrete capacity scenarios (add a curator to the bottleneck, change batch size/cadence, smooth arrivals) with their effect on clearance and turnaround.
6. Recommend one action and quantify its impact.
```

## Expected Output

- Per-stage ρ table, named bottleneck, and a danger-zone flag.
- Projected backlog curve and clearance date vs deadline (gap in weeks).
- Scenario comparison with quantified effect on clearance/turnaround.
- A single prioritised recommendation with its numeric impact and any cost/turnaround tradeoff.
