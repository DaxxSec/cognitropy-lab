# Derivative Sauce Brief Prompt

## Purpose

Use this prompt to design a daughter sauce from a signed-off mother as a controlled delta, with a review scoped to only what changed.

## Prompt Template

```
You are designing a daughter sauce off a validated mother emulsion. Express it as a delta and keep the review narrow — the mother is already proven.

I want to derive a daughter sauce:

- **Signed-off mother:** [formula ID + which mother]
- **Target daughter:** [aïoli / rémoulade / béarnaise / choron / maltaise / other]
- **Flavour / use intent:** [what it's for, what it should taste like]
- **Reviewer constraints:** [allergen limits, stability floor, service conditions]
- **Candidate additions:** [garlic / herb reduction / tomato / citrus / pickle / etc.]

Please:
1. Express the daughter purely as additions/substitutions/ratio tweaks (the delta) from the mother.
2. Check the delta against the emulsion budget; flag any aqueous addition that threatens stability and how to compensate.
3. Predict the delta's impact on each rubric criterion.
4. Propose the scoped review (which sensory test vs the mother, whether a stability assay is needed).
5. Output the normalised daughter formula referencing the mother.
```

## Expected Output

- The delta specification (additions/substitutions/ratios) from the mother.
- An emulsion-budget check with compensation for any watery additions.
- Predicted rubric impacts.
- A scoped review plan (delta-only).
- The normalised daughter formula and a family-tree entry.
