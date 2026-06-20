# Glaze Environmental & Safety Review

## Purpose

Use before selling or food-using a glaze: a combined hazard, food-safety leaching, and waste-water review of a recipe or a whole glaze palette.

## Prompt Template

```
You are a ceramics materials-safety reviewer. Screen the following glaze for toxicity, food-contact leaching risk, and waste-water disposal — do not clear food-contact use on recipe inspection alone.

Recipe(s):
- **Name:** [GLAZE NAME]
- **Materials (% by weight):** [MATERIAL: %, MATERIAL: %, ...]
- **Colorant(s):** [OXIDE/STAIN: %]
- **Fired to:** cone [NUMBER] | **application:** [dip/spray/brush]
- **Intended use:** [food-contact surface / decorative-only]

Please:
1. Flag each hazardous constituent (lead, barium, cadmium, lithium, manganese, soluble colorants, free silica) with its limit.
2. Give a food-safety verdict: PASS / TEST-REQUIRED / FAIL, with reasoning; recommend an ASTM C738 leach test and liner-glaze strategy where needed.
3. Specify dust/fume controls for handling and firing.
4. Specify waste-water/disposal handling for rinse and slurry.
```

## Expected Output

- A constituent-by-constituent hazard table.
- A clear food-safety verdict with the test requirement stated.
- Handling/firing safety controls (silica, fumes).
- Waste-disposal guidance (no-drain, settle/reclaim, hazardous-waste).
