# Method-Selection Consult

## Purpose

Given a new liquid, recommend the appropriate spherification method and a starting recipe — the "appropriateness criteria" consult. Use before making the first pilot batch of an unfamiliar base.

## Prompt Template

```
You are an appropriateness consult for spherification method choice, using the
decision tree in context/workflows.md (Workflow 3) and the recipe table in
context/references.md.

I want to spherify:

- **Liquid:** [DESCRIBE]
- **pH:** [VALUE / "unknown"]
- **Calcium / dairy:** [HIGH-CA? DAIRY? / "no"]
- **Alcohol %:** [VALUE / "0"]
- **Viscosity:** [THIN / MEDIUM / SYRUPY]
- **Desired result:** [CAVIAR / LARGE SPHERE / RAVIOLI-YOLK], [SERVE-NOW / MAKE-AHEAD]

Please:
1. Recommend basic / reverse / frozen-reverse and explain WHY for this liquid.
2. Give a starting recipe (alginate %, calcium salt + %, bath-time band, buffer/viscosity adds).
3. Note the single property that would flip the recommendation.
4. List the top two risk flags (acid, dairy, alcohol, air, hard water) to watch on the pilot.
```

## Expected Output

- A method choice with an explicit, property-driven rationale.
- A concrete starting recipe ready to pilot.
- The decision's sensitivity (what change flips it) and the pilot's watch-list.
