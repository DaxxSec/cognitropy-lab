# /method-select

Recommend a production method — Orleans (surface), generator (beechwood trickle), or submerged (Frings-style acetator) — from a batch's volume, time, quality, and equipment constraints.

## Inputs

- Target volume and frequency (one-off vs. continuous).
- Time budget to finished vinegar.
- Quality priority: aromatic complexity vs. clean high-acidity throughput.
- Equipment on hand (barrels, vessels, aeration pump/acetator, beechwood).
- Whether the style depends on slow barrel character (e.g. traditional wine vinegar).

## Steps

1. Read `context/concepts.md` §4 (methods) and `context/workflows.md` §B (selection decision).
2. Score each method against the constraints (speed, quality, scale, equipment, oxygen-transfer needs).
3. Apply the decision tree; identify the best fit and the runner-up.
4. State the **tradeoffs** explicitly (e.g. submerged = fast + repeatable but less aromatic; Orleans = complex but slow and oxygen-limited).
5. Note the aeration and temperature implications of the chosen method and any equipment gap to close.
6. Optionally record the rationale as a `methods`/`equipment` KB entry.

## Output

- A recommendation with primary + fallback method, scored tradeoffs, and an equipment-gap note, printed to chat.
- Optional `outputs/kb/methods/` entry.

## Notes

- Oxygen-transfer rate, not vessel size, is the real throughput limiter — match aeration to the method.
- Don't push a delicate aromatic style into a submerged acetator just for speed; the character is the product.
- Beechwood generators need re-wetting cadence and airflow tuning; flag that maintenance cost.
