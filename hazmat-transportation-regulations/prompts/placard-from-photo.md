# Placard From Photo

## Purpose

Decode the placards, labels, marks, and ADR orange-plate Kemler code visible in a photo of a transport unit, and reconcile them against the shipping paper. Use at the dock or roadside with eyes on the vehicle.

## Prompt Template

```
You are the dangerous-goods documentation agent. Decipher the visible markings below and reconcile them with the declaration.

- **Mode / jurisdiction:** [ROAD | RAIL | SEA | AIR; region]
- **Photo / description of markings:** [ATTACH PHOTO OR DESCRIBE: placard colours/numbers, labels, orange plate numbers, package marks]
- **Orange plate (if visible):** upper = [HIN/KEMLER], lower = [UN NUMBER]
- **Shipping paper declares:** [DECLARED UN / CLASS / PG, OR "unknown"]

Please:
1. Inventory every visible symbol and decode each into the hazard it asserts.
2. Decode the orange plate: interpret the HIN (first digit = primary hazard, doubled = intensified, leading X = water-reactive) and confirm the UN number.
3. List the hazards the markings collectively assert.
4. Reconcile against the shipping paper: flag any placard without a matching declared line, or any declared line missing its required placard/label.
5. Give a reconciliation verdict and flag any safety-critical mismatch (the visible hazard governs emergency response).
```

## Expected Output

- A symbol inventory with per-symbol decode.
- The orange-plate (HIN + UN) interpretation.
- A reconciliation verdict against the paper, with any mismatch flagged as safety-critical.
