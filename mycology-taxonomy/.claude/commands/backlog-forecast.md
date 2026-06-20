# /backlog-forecast

Model the determination backlog as a queue and project when it clears (or whether it grows without bound) from measured arrival and processing rates.

## Inputs

- The arrivals log (`outputs/accessions/register.csv`) and a processing log (per-specimen start/finish times), or summary rates.
- Arrival rate `λ` (specimens/week) and its variability; service rate `μ` per stage and per difficulty tier; current backlog `L`.
- Server counts `c` per stage (curators, sequencer slots).
- Optional: a target clear-by date or deadline.

## Steps

1. Read `context/concepts.md` "Capacity-planning vocabulary" and `context/workflows.md` "Loop B, Step 2".
2. Compute utilization `ρ = λ / (c·μ)` per stage; flag any stage with ρ ≥ ~0.85 (danger) or ρ ≥ 1 (unbounded growth).
3. Identify the **bottleneck** (highest ρ) — it sets total throughput (Theory of Constraints).
4. Estimate mean wait with Erlang-C (M/M/c); when arrival/service variability is high, use Kingman's approximation instead of the exponential assumption.
5. Project backlog trajectory over the horizon and the clearance date under current capacity; compare to any deadline.
6. Produce 2–3 what-if scenarios (e.g. +1 curator on the bottleneck, larger batch) with their effect on clearance.

## Output

- `outputs/capacity/backlog-forecast-<date>.md` — per-stage ρ, bottleneck, projected backlog curve, clearance date, deadline gap, and scenario comparison.

## Notes

- ρ ≥ 1 anywhere means the backlog is mathematically guaranteed to grow — no amount of "working harder" fixes a saturated bottleneck; add capacity there.
- Difficulty tiers have different `μ`; a count-based forecast that ignores tiers will be optimistic. Model service rate per tier.
- Feeds `/curator-allocation`, `/sequencing-capacity-plan`, and `/turnaround-sla`.
