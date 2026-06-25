# /select-mcu

Choose a microcontroller with a weighted cost-benefit matrix, after filtering on hard requirements — the highest-leverage decision in the project, since it fixes flash/RAM, peripherals, power, and per-unit cost for the product's life.

## Inputs

- Hard requirements (must-have peripherals, min flash/RAM, power floor, temperature, certifications)
- Candidate MCU list with datasheet figures and distributor price at the expected volume
- Criterion weights (e.g. unit cost, flash/RAM headroom, power, peripheral fit, ecosystem)

## Steps

1. Apply the **hard filters** — drop any candidate that fails a must-have. These are not scored, they gate.
2. Define the **weighted criteria** and their weights; default ~ cost 30 / memory 20 / power 20 / peripherals 15 / ecosystem 15.
3. Score each surviving candidate 1–5 per criterion from datasheet + price data; compute the weighted total.
4. Cross-check the leader against **NRE vs COGS** at the real volume (cheap part + big dev effort can lose at low volume).
5. Reserve flash/RAM/pin headroom and record the full matrix.

## Output

`outputs/projects/<name>/mcu-matrix.md` — the hard-filter results, the weighted matrix with scores, the recommended part, and the NRE-vs-COGS sanity note.

## Notes

- Ties break toward the **more mature ecosystem** (lower NRE risk) unless volume makes the COGS delta dominate.
- Never relax a hard **safety/certification** requirement to fit a cheaper part — relax a soft one or add an external component instead.
