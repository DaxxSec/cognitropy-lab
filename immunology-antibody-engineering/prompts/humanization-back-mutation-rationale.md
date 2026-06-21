# Humanization Back-Mutation Rationale

## Purpose

Justify a humanization back-mutation set — explain *why* each restored parental residue is needed and what it trades against humanness. Use when defending a humanized variant panel or teaching a trainee the logic behind a minimal graft.

## Prompt Template

```
You are explaining a humanization design as a senior antibody engineer to a trainee.

I have a humanization case:

- **Parental VH / VL (non-human):** [VALUE]
- **Chosen human germlines:** [IGHV..., IGKV.../IGLV...]
- **Straight-graft affinity vs parental:** [VALUE — e.g. 8× loss]
- **Candidate back-mutations:** [list of positions/identities, or "propose them"]
- **Humanness floor & affinity-loss budget:** [VALUE]

Please:
1. Classify each candidate back-mutation by mechanism: VH/VL-interface, Vernier-zone, canonical-structure-determining, or other.
2. Rank them by expected affinity recovery and explain the structural reasoning for each.
3. Propose a minimal set that meets the affinity-loss budget and a "fewest-mutations" alternative.
4. Estimate the humanness and immunogenicity trade for each set (OASis/Hu-mAb direction).
5. Flag any back-mutation that re-introduces a sequence liability and recommend the resolution.
```

## Expected Output

- A per-mutation mechanism + rationale table, ranked by expected effect.
- A minimal back-mutation set and a fewest-mutations alternative.
- The humanness/affinity trade made explicit for each.
- Any liability re-introduction flagged with a fix.
