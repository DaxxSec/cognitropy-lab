# Repair Mortar Specification

## Purpose

Use when you have a characterised original and need a buildable, compatible repair-mortar spec — softer, more porous and more vapour-open than the substrate, with acceptance criteria and curing constraints.

## Prompt Template

```
You are specifying a compatible repair mortar for historic masonry. Compatibility before strength; match equal-or-softer, never harder.

I have a characterised original and a repair context:

- **Original mortar:** [binomial name, binder class, HI, binder:aggregate, aggregate grading/mineralogy/colour]
- **Substrate:** [unit type, strength, porosity if known]
- **Exposure:** [orientation, driving-rain severity, parapet/chimney/below-DPC, frost]
- **Salts / moisture:** [known salt loading, sources]
- **Constraints:** [appearance match, programme, budget, local materials]

Please:
1. Specify the aggregate first (grading curve, mineralogy, colour) to replicate the original.
2. Choose a binder no harder than the original; justify against the binder phylogeny (must be in or below the original's clade).
3. Give proportions by volume, water demand, any pozzolan/gauge, and application/joint profile.
4. Define acceptance criteria vs the substrate (strength below the unit, capillarity above, vapour μ ≤ unit) with standards and target values.
5. Specify curing and the weather window; flag anything that lands in the maintenance schedule.
```

## Expected Output

- Aggregate specification with grading curve.
- Binder + proportions + pozzolan/gauge, with a phylogeny justification.
- Mixing/application/joint-profile notes.
- Acceptance table: property, target, standard (EN 1015-11/-18/-19, EN 12370/12371).
- Curing and weather-window constraints; test-panel recommendation.
