# collection-survey-intake

## Purpose

Turn a messy, free-text collection survey or accession note into a structured digitization-candidate record carrying exactly the attributes the optimization commands need (extent, material, condition, rights, demand, decay flags). Use it at intake, before anything can be prioritized or scheduled.

## Prompt Template

```
You are a digitization-program analyst preparing material for an optimization-driven scanning queue.

Here is the raw survey / accession information for one or more lots:

- **Collection / lot description:** [PASTE FREE-TEXT SURVEY OR NOTES]
- **Known extent (if any):** [BOXES / VOLUMES / LINEAR FEET / ITEM COUNT]
- **Material types present:** [E.G. BOUND VOLUMES, LOOSE SHEETS, PHOTOGRAPHS, ACETATE NEGATIVES]
- **Anything known about condition:** [E.G. "smells of vinegar", "brittle", "mold spotting"]
- **Rights / access status:** [CLEARED / RESTRICTED / UNKNOWN / DONOR TERMS]
- **Demand signal:** [REQUESTS, EXHIBITION PLANS, RESEARCH INTEREST, OR NONE]

Please:
1. Split the input into discrete lots and, for each, estimate extent in **images** (state the per-unit assumption).
2. Assign a **condition grade** (pristine / stable / fragile / at-risk / unstable) and list any **decay markers** you can infer (vinegar syndrome, sticky-shed, brittle paper, mold) — flag safety hazards (nitrate, active mold).
3. Normalize **rights** to cleared / restricted / unknown, and **demand** to high / medium / low, noting what's missing.
4. Output a structured table (one row per lot) with columns: lot, material, est. images, condition grade, decay flags, rights, demand, blockers.
5. List which lots are **not schedulable yet** and exactly what must be resolved first.
```

## Expected Output

- A per-lot candidate table ready to feed `/triage-fragile-condition` and `/plan-digitization-queue`.
- Explicit assumptions behind every image estimate (so the numbers are auditable).
- A "blocked / needs resolution" list separating schedulable from non-schedulable lots.
