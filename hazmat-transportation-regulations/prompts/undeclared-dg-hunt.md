# Undeclared Dangerous Goods Hunt

## Purpose

Expose dangerous goods hidden inside a benign-sounding commodity description by crib-dragging the text against known-hazard cribs. Use when the goods description hints at hazards the declaration may omit — the single highest-value check for air cargo.

## Prompt Template

```
You are the dangerous-goods documentation agent. Crib-drag the commodity description below for dangerous goods that are implied but possibly undeclared.

- **Mode / jurisdiction:** [AIR | SEA | ROAD | RAIL; region]
- **Commodity / goods description:** [PASTE THE PLAIN-LANGUAGE DESCRIPTION OR PACKING LIST]
- **Actually declared on the paper:** [LIST DECLARED UN NUMBERS / CLASSES, OR "none — general cargo"]
- **Declared quantity / packaging (if any):** [VALUE]

Please:
1. Tokenise the description and slide it against the known-hazard crib list (lithium batteries, aerosols, perfume, oxidizers, dry ice, paints, fuels, magnetized cargo).
2. For each crib hit, give the likely UN number / class and whether it is actually declared.
3. For any hit that is implied but undeclared, cite the mode's rule and note any quantity exemption that might apply.
4. Recommend a disposition per hit: CLEARED / FLAG-VERIFY / ESCALATE-PHYSICAL.
5. Prioritise embargo-dodge targets (lithium batteries, fireworks, fuels) regardless of stated quantity.
```

## Expected Output

- A crib-hit table: matched term → likely UN/class → declared? → applicable rule/exemption.
- A per-hit disposition recommendation.
- An overall escalation recommendation for the shipment.
