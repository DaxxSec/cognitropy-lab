# /safety-review

Review a recipe or finished batch for food-safety and labeling compliance — minimum acidity floor, pasteurization, "mother"/raw claims, and prohibited health claims.

## Inputs

- Recipe or batch details: substrate, measured acidity, whether filtered/pasteurized, intended use (personal / gift / sale).
- Target jurisdiction (default US FDA).
- Proposed label text or product claims, if any.

## Steps

1. Read `context/concepts.md` §8 (regulatory floors) and the README "Legal & Ethical" section; pull current standards via web if the jurisdiction is unusual.
2. **Acidity check:** compare measured titratable acidity against the jurisdiction floor (US FDA ≥4%, many regional ≥5–6%) with a safety margin; flag below-floor product as not legally "vinegar."
3. **Stability check:** assess whether the product needs pasteurization for the intended distribution (raw mother-containing vinegar keeps fermenting / throws sediment).
4. **Claims check:** flag any health/therapeutic claim (cures, detoxes, treats) as non-compliant without substantiation; confirm "raw"/"with the mother"/"unfiltered" are used descriptively only.
5. **Allergen/ingredient check:** note allergen sources (e.g. malt/gluten, sulfites in wine base) that require disclosure.
6. Produce a pass/fail per item with required fixes; write the review to `outputs/`.

## Output

- A compliance checklist (acidity / stability / claims / allergens) with pass/fail and required corrections, in chat.
- `outputs/safety/<batch-id>-review-YYYY-MM-DD.md`.

## Notes

- This is craft guidance, **not** regulatory or legal authority — direct the user to confirm with their food-safety regulator before commercial sale.
- Titratable acidity (not pH) is the number that determines legal status.
- When in doubt about a health claim, omit it — the KB should tag such statements `practitioner-lore`, and FAQs must never present them as medical advice.
