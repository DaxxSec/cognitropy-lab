# /turnaround-sla

Derive and audit a defensible identification-request turnaround SLA using Little's Law and M/M/c queueing, per difficulty tier, and trace breaches to the bottleneck.

## Inputs

- Pipeline metrics: WIP `L`, arrival rate `λ`, per-stage service rate `μ`, server counts `c`.
- Per-tier targets (routine fast, cryptic slow) and any externally promised turnaround.
- Historical actuals (date_in → date_determined per specimen) for auditing.

## Steps

1. Read `context/concepts.md` "Capacity-planning vocabulary" and `context/workflows.md` "Loop B, Step 5".
2. Compute current mean turnaround with Little's Law (`W = L / λ`) overall and per tier.
3. Use Erlang-C (M/M/c) to estimate the wait component and the turnaround achievable at current capacity; apply Kingman when variability is high.
4. Set a per-tier SLA that current capacity can actually meet (with the safety buffer), not an aspirational number.
5. Audit historical actuals against the SLA; compute breach rate per tier.
6. For breached tiers, trace to the bottleneck stage (from `/backlog-forecast`) and recommend the specific capacity change to restore compliance.

## Output

- `outputs/capacity/turnaround-sla-<date>.md` — current `W` per tier, recommended SLA per tier, breach rate, bottleneck attribution for breaches, and corrective recommendation.

## Notes

- An SLA the pipeline can't meet at current `ρ` is a promise to break — derive it from the queue model, don't pick a round number.
- Per-tier SLAs are honest; a single blended SLA hides that cryptic complexes legitimately take longer and routine taxa could be faster.
- This command closes Loop B — a breach feeds back to `/backlog-forecast` → `/curator-allocation` / `/sequencing-capacity-plan`.
