# Ablation Study Design

## Purpose

Use when you need to justify a fusion-layer or strategy change to a calibration / management audience. Designs the smallest replay matrix that would credibly answer the underlying question without spending months on a sprawling sweep.

## Prompt Template

```
You are designing a fusion-EMS ablation study. Apply the workflow in `.claude/commands/cycle-replay.md` and the drive-cycle catalogue in `references.md`.

Study question:
- **Hypothesis / change under evaluation:** [e.g. "adding V2X SPaT improves urban regen energy capture by >5% with no drivability cost"]
- **Audience:** [research / calibration leadership / regulator / customer]
- **Available drive library:** [WLTP 3b / CLTC-P / FTP-75 / HWFET / US06 / custom RDE routes / fleet-collected drives — list what you can replay against]
- **Compute budget:** [variant-runs available per study]
- **Time budget:** [days available for the full study]
- **Decision criteria:** [what KPI thresholds would constitute a go / no-go for the change]

Please:
1. Decompose the hypothesis into testable sub-claims (typically 2–4).
2. Design the minimum ablation matrix (variants × drives) needed to evaluate each sub-claim with reasonable statistical power; justify why a smaller matrix is insufficient and why a larger matrix is overkill.
3. Identify the confounders the matrix must control for (cycle mixing, vehicle variant, weather regime, etc.) and how the matrix controls each.
4. Specify the report structure tuned to the audience — what they need to see first, what supporting evidence they will likely ask for, and what level of statistical detail is appropriate.
```

## Expected Output

- Decomposition of the hypothesis into sub-claims.
- A specific (variants × drives) matrix with run counts.
- A confounder control plan.
- An audience-tuned report outline.
- An estimated compute / time cost for the full matrix.
