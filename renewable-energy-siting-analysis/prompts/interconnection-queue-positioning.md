# Interconnection Queue Positioning Brief

## Purpose

After the articulation graph is built but before the cluster-study window opens, produce a positioning brief that names — for each proposed joint — the queue-position-aware risks: cluster cohort, expected network-upgrade allocation, withdrawal-penalty exposure, and the decision points where the project would walk away. The brief sits next to the slack-budget audit and is consumed by the development lead and the IPP's commercial team, not just the engineering team.

## Prompt Template

```
You are a renewable-energy siting analyst working in the renewable-energy-siting-analysis workspace.
You have an articulation graph at outputs/<project_id>/articulation-graph.md and a slack-budget
audit at outputs/<project_id>/slack-budget-<date>.md. Produce an interconnection-queue
positioning brief.

Project: [project_id]
ISO: [iso]
Cluster window: [cluster_label — e.g. "PJM Window 3", "MISO 2026 cycle"]
LGIA template basis: [pro-forma / negotiated]

For each joint in the articulation graph, draft a queue-position section:

1. **Queue-cluster identification** — which cluster the joint sits in, the cluster's MW total,
   and the joint's percentile within it (large queue position is correlated with longer study and
   higher network-upgrade allocation).
2. **Network-upgrade exposure** — pull the slack audit's findings for the linkages this joint
   uses. If linkages saturated > 75% pre-contingency, name them and reference Table R-7 to
   estimate the network-upgrade dollar range.
3. **Cost-allocation framework** — under FERC Order 2023, network upgrades are allocated to the
   triggering joint or pro-rata across cluster. Cite which rule applies.
4. **Withdrawal-penalty exposure** — the deposits / readiness deposits the project would lose if
   it withdraws after each milestone. Each ISO publishes these; quote the relevant ones.
5. **Decision points** — three named decision points where the project would re-evaluate: cluster
   study results, facilities study results, final LGIA terms. For each, the trigger that flips
   the decision from "continue" to "withdraw and re-site."

After the per-joint sections, write a portfolio-level summary:

- Aggregate network-upgrade exposure ($M range).
- Withdrawal-penalty exposure if the portfolio walks at each milestone.
- Earliest commercial-operation date consistent with the cluster-study schedule.
- Recommended capacity-market commitment timing (don't bid capacity until LGIA signed).

Save the brief to `outputs/<project_id>/queue-positioning-<YYYYMMDD>.md`. End with a "decisions
to make in the next 30 days" punch list.
```

## Expected Output

A 2-4 page markdown brief at `outputs/<project_id>/queue-positioning-<YYYYMMDD>.md`. The dollar ranges should be ranges (not point estimates) and explicitly cite the ISO's published cluster-study schedule. The decision-points section is the most-read part of the document; it should name *which* number triggers each walk-away.
