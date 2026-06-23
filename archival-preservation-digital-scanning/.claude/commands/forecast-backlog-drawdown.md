# /forecast-backlog-drawdown — Model throughput, backlog, and completion date

Forecast how fast a digitization backlog clears under current (or proposed) capacity, using capacity-planning and queueing math, and answer the recurring questions: "when will we be done?" and "what would another station buy us?"

## Inputs

- Current backlog size (estimated images) and its arrival rate (new accessions added per month, if any).
- Effective service rate: images/hour × productive hours/day × working days/month × number of stations, discounted by a realistic utilization factor (rework, calibration, sick days).
- Optional scenarios to compare: add a station, add a shift, outsource X%, hire an operator.

## Steps

1. **Establish the baseline service rate.** Multiply throughput by productive hours and stations, then apply the utilization discount from `context/references.md` (lab reality is ~60–75% of nameplate, not 100%).
2. **Frame the backlog as a queue.** If accessions keep arriving, model it as M/M/c or M/G/c: check stability (`ρ = λ / (c·μ) < 1`). If `ρ ≥ 1` the backlog never clears at current capacity — say so plainly and size the gap.
3. **Project drawdown.** Compute `months_to_clear = backlog / (service_rate − arrival_rate)`. Plot the cumulative-cleared curve month by month; include a +rework adjustment for the QA reject rate.
4. **Run scenarios.** Re-compute drawdown and steady-state queue length for each proposed change; express results as months saved and Δcost per month saved.
5. **Bound the estimate.** Give optimistic / expected / pessimistic dates from the utilization range, not a single false-precision date.
6. **Identify the binding constraint.** State whether the lab is capacity-bound (need stations/staff), prep-bound (conservation/metadata upstream), or QA-bound (rework loop) — the forecast is only as good as the true bottleneck.

## Output

`outputs/backlog-forecast-<date>.md`: the baseline service rate with assumptions, the stability check, the month-by-month drawdown curve, an optimistic/expected/pessimistic completion window, the scenario comparison table (months saved vs. cost), and the named binding constraint.

## Notes

- Nameplate throughput is the single most over-optimistic number in any digitization plan. Anchor on measured rates the moment you have them.
- A backlog with ongoing accessions is a queue, not a pile — if arrivals exceed service, no finish date exists; the honest output is a stability gap, not a date.
- Pair with `/model-project-cost` when a scenario adds capacity: months-saved only matters against what it costs.
