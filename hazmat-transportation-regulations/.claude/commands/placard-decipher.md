# /placard-decipher

Decode the placards, labels, marks, and ADR orange-plate Kemler/HIN code visible on a transport unit, then reconcile the deciphered hazards against the shipping paper.

## Inputs

- A photo or careful description of the placards, labels, package marks, and orange plate.
- The shipping paper / declaration for the same shipment (for reconciliation).
- Mode and jurisdiction (placarding rules differ by mode).

## Steps

1. Inventory every visible symbol: placard class/colour/number, subsidiary labels, UN-spec packaging marks, lithium/limited-quantity/environmentally-hazardous marks.
2. Decode the orange plate: split into HIN (upper) and UN number (lower); decode the HIN per the Kemler rules in `context/references.md` (first digit primary hazard, doubled = intensified, leading X = water-reactive).
3. Translate each symbol into the hazard it asserts (class, division, subsidiary risk).
4. Reconcile the visible hazards against the shipping paper's declared class/UN/PG.
5. Flag any placard present without a matching declared line, or any declared line without its required placard/label.

## Output

A placard decode record at `outputs/placard-<ref>-<date>.md`: an inventory of symbols, the decoded hazards, the orange-plate interpretation, and a reconciliation verdict against the paper.

## Notes

- The *visible* hazard governs an emergency responder's first action — a placard/paper mismatch is safety-critical, not cosmetic.
- A residue/empty placard or a "DANGEROUS" mixed-load placard has its own rules; don't read it as the substance placard.
