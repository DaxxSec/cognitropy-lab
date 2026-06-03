# Production Spec Sheet

## Purpose

Turn a lamination codex into a one-page, imperative spec sheet the production line can follow today — the "fair copy" exemplar for bakers, not the archive.

## Prompt Template

```
You are a viennoiserie lamination agent writing a production spec sheet for the line.

Source codex / analysis:
- **Product:** [PRODUCT NAME]
- **Codex file:** [outputs/codex-...md]
- **Batch size / shift:** [N units, which shift]
- **Today's ingredient lots:** [flour lot / butter lot + fat%]
- **Kitchen conditions:** [ambient T / RH]

Please produce a one-page spec sheet that:
1. States the collation formula and target layer count up front.
2. Lists each step imperatively with exact temps, times, and the fold sequence.
3. Calls out the temper window and re-chill trigger for today's butter lot.
4. Declares allergens (gluten/milk/egg/...) in a header.
5. Ends with the expected crumb signature so the baker can self-check.
```

## Expected Output

- A single-page, numbered, imperative procedure with all temps/timings.
- Collation formula + layer count in the header.
- Allergen declaration and today's lot/conditions noted.
- Expected-signature self-check line at the bottom.
