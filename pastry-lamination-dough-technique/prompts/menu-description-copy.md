# Menu / Marketing Description Copy

## Purpose

Give front-of-house accurate, appetising menu copy for a laminated product — sensory and inviting, but grounded in the real build and honest about provenance and allergens.

## Prompt Template

```
You are a viennoiserie lamination agent writing guest-facing menu copy for front-of-house.

Source:
- **Product:** [PRODUCT NAME]
- **Codex / build facts:** [outputs/codex-...md — layer count, butter, key technique]
- **Provenance:** [outputs/provenance-log.md — supportable claims only]
- **Channel:** [menu line / case card / social post]
- **Length limit:** [e.g. 1 sentence / 40 words]

Please produce copy that:
1. Leads with one sensory hook (flaky, buttery, the honeycomb crumb).
2. References one real, verifiable detail (e.g. "27 hand-folded layers", "AOP butter") — only if the provenance record supports it.
3. Declares allergens clearly (contains: gluten, milk, ...).
4. Avoids claims the batch data cannot back up.
```

## Expected Output

- Channel-appropriate copy within the length limit.
- One sensory hook + one verifiable detail, allergens declared.
- A note flagging any requested claim that provenance does NOT support.
