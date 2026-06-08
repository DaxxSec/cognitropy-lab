# New Material Cut Design

## Purpose

Use when you have a piece of rough in a material you don't have a go-to chart for, and you want an optimized, cuttable design from first principles — angles, table, and the machine check — in one pass.

## Prompt Template

```
You are the faceting-optimization agent. Design an optimized cut for new rough.

I have a piece of rough to facet:

- **Material / RI:** [MATERIAL, RI e.g. spessartine garnet, 1.79]
- **Dispersion (if fire matters):** [VALUE or "unknown"]
- **Mohs hardness:** [VALUE]
- **Rough shape / yield priority:** [e.g. shallow tabular — favor yield / blocky — favor brilliance]
- **Intended outline:** [round brilliant / oval / emerald / other]
- **Machine condition (latest):** [spindle TIR µm, lap flatness µm, or "see outputs/"]

Please:
1. Compute the critical angle and minimum pavilion main for this RI.
2. Recommend an optimized pavilion main (plateau-center) and a crown main balancing fire vs brilliance for this dispersion.
3. State the table % and the hold tolerance the design needs.
4. Run the angle-error budget against my machine condition and give a GO/CAUTION/NO-GO verdict.
5. If NO-GO, name the dominant error source and the maintenance to do first.
```

## Expected Output

- Critical angle, minimum and recommended pavilion main.
- Crown main + table % with the fire/brilliance rationale.
- Required hold tolerance.
- Tolerance-budget verdict with the dominant source called out.
- Saved design + budget files under `outputs/`.
