# /derivative-design

Design a daughter sauce off a signed-off mother emulsion, expressed as a controlled delta with a review scoped to just that delta.

## Inputs

- The signed-off mother (cite its formula ID and sign-off certificate).
- The target daughter and its flavour/use intent (e.g. aïoli, béarnaise, rémoulade).
- Constraints from reviewers (allergen limits, stability floor, intended service conditions).

## Steps

1. Confirm the mother is actually **signed off** — a daughter cannot be built on an unvalidated base.
2. Read the `references.md` mother→daughter map; express the daughter purely as additions/substitutions/ratio tweaks (the delta).
3. Check the delta against the emulsion budget: aqueous additions (tomato, citrus, herb purée) reduce stability — add as paste, reduce first, or compensate with emulsifier.
4. Predict the delta's impact on each rubric criterion; flag anything that needs fresh evidence (usually flavour + any stability change).
5. Scope the review: a duo-trio vs the mother for the flavour delta, plus `/stability-assay` only if the addition is aqueous. Don't re-validate the mother.
6. Draft the normalised daughter formula referencing the mother and hand it to `/review-round`.

## Output

`outputs/derivative-<daughter>-from-<mother-id>.md`: the delta specification, normalised daughter formula, predicted rubric impacts, the scoped review plan, and an updated family-tree entry.

## Notes

- The whole point of the mother technique is leverage — keep the daughter's review narrow to the delta, or you lose the efficiency.
- Watery additions are the #1 way a derivative breaks a stable mother; treat them with suspicion.
