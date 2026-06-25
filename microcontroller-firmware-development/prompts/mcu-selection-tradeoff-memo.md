# MCU Selection Trade-off Memo

## Purpose

Turn a set of requirements and candidate parts into a defensible MCU recommendation, with the weighted cost-benefit matrix and the NRE-vs-COGS reasoning made explicit for a design review.

## Prompt Template

```
You are an embedded firmware engineer writing an MCU selection memo for a design review.

I have a selection problem:

- **Product / volume / lifetime:** [WHAT IT IS, UNITS/YEAR, YEARS]
- **Hard requirements (must-haves):** [PERIPHERALS, MIN FLASH/RAM, POWER FLOOR, TEMP, CERTS]
- **Candidate MCUs + datasheet figures + price @volume:** [LIST]
- **Criterion weights:** [E.G. COST 30 / MEMORY 20 / POWER 20 / PERIPH 15 / ECOSYSTEM 15]

Please:
1. Apply the hard filters and list which candidates survive and why others were cut.
2. Build the weighted scoring matrix and compute totals.
3. Recommend a part, and sanity-check it against NRE vs COGS at the stated volume.
4. State the headroom reserved and any hard requirement that constrained the choice.
```

## Expected Output

- The hard-filter pass/fail list
- A weighted matrix with per-criterion scores and totals
- A single recommendation with the NRE-vs-COGS check shown
- The reserved flash/RAM/pin headroom and the binding constraint
