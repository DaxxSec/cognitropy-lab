# /undeclared-crib

Crib-drag a plain-language commodity description for the dangerous goods it implies but the declaration may omit — sliding known-hazard cribs along the "general cargo" text to expose undeclared dangerous goods.

## Inputs

- The plain-language goods / commodity description (or packing list) from the paper.
- The declaration's actually-declared UN numbers / classes (to check for omission).
- Mode (the undeclared rules that bite differ — air is strictest, esp. lithium batteries).

## Steps

1. Tokenise the commodity description into goods nouns and modifiers.
2. Crib-drag against the known-hazard crib list in `context/references.md` ("power bank" → UN 3480; "aerosol" → UN 1950; "perfume/nail polish" → UN 1266; "pool shock" → 5.1; "dry ice" → UN 1845; "paint/thinner" → UN 1263).
3. For each crib hit, determine whether the hazard is actually declared on the paper.
4. Where a crib hits but nothing is declared → FLAG undeclared; cite the mode's rule and any quantity-exemption that might apply.
5. Prioritise known embargo-dodge targets (lithium batteries, fireworks, fuels) for physical verification regardless of declared quantity.

## Output

An undeclared-DG report at `outputs/undeclared-<ref>-<date>.md`: each crib hit, whether it is declared, the applicable rule/exemption, and an escalation recommendation.

## Notes

- A crib hit is a *suspicion*, not proof — small consumer quantities may be excepted. FLAG to verify, don't auto-FAIL, unless the mode prohibits outright.
- The point is the omission: a hazard plainly implied by the goods description but absent from the declaration is the highest-value finding this workspace produces.
