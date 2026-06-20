# Capacity Investment Decision

## Purpose

Use when a studio is about to buy equipment (a wheel, a second kiln, a drying cabinet) and needs the choice grounded in marginal-throughput and marginal-footprint math instead of intuition.

## Prompt Template

```
You are advising a studio on a capacity investment. Use the bottleneck/delay analysis: only capacity added at the controlling constraint buys throughput. Weigh both marginal throughput and marginal footprint.

Current state:
- **Bottleneck stage & its X:** [STAGE, X from /throwing-saturation-flow]
- **Arrival rate / green ratio:** [q, λ]
- **Candidate investments:** [A: second kiln — cost, capacity added], [B: extra wheel — cost], [C: drying cabinet — cost]
- **Goal:** [maximize output / hit a ship deadline / lower per-piece footprint]
- **Grid CO₂e factor:** [VALUE]

Please:
1. Confirm the bottleneck and compute current per-piece delay.
2. For each candidate, recompute capacity → new X → new delay; report throughput gained.
3. Reject any candidate that targets a non-bottleneck stage and explain why it buys nothing.
4. Report marginal throughput per dollar AND per kg CO₂e; give a ranked recommendation with payback.
```

## Expected Output

- The confirmed bottleneck and current delay per piece.
- A per-candidate table: capacity added, new X, delay removed, throughput gained.
- Explicit rejection of non-bottleneck-targeting options.
- A ranked recommendation with both cost and footprint efficiency and a payback estimate.
