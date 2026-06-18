# /dsc-landmarks

Extract the characteristic temperatures every downstream capacity model needs — Tg, Tx, Tp, Tm, Tl — and the derived ΔTx and supercooled-liquid region from a differential scanning calorimetry (DSC) scan.

## Inputs

- DSC heat-flow vs temperature data (CSV preferred), or a description of the peak/step positions if no raw file.
- Heating rate β (K/min) and sample mass (mg) — both shift apparent temperatures and peak shape.
- Alloy nominal composition (at%) and any prior thermal/mechanical history, if known.

## Steps

1. Read `context/concepts.md` §5 for the on-heating event order and `references.md` for the DSC cheat-sheet.
2. Identify the **glass transition Tg** — the endothermic baseline step. If no step is visible, flag the sample as possibly already crystalline and stop before trusting GFA math.
3. Locate the **crystallization exotherm**: onset **Tx** (tangent construction) and peak **Tp**. Note any twin/shoulder peaks → multistage crystallization (record each).
4. Locate the **melting endotherm(s)**: solidus **Tm** and **liquidus Tl** (the GFA-parameter input — use Tl, not Tm).
5. Compute **ΔTx = Tx − Tg** and describe the supercooled-liquid region (the TPF working zone).
6. State the temperature convention (onset vs peak) and log β + mass so the result is reproducible and comparable across scans.

## Output

`outputs/dsc-landmarks-<alloy>-YYYY-MM-DD.md`: a table of Tg, Tx, Tp, Tm, Tl, ΔTx; the supercooled-liquid width; β and sample mass; convention used; flags (no Tg, multistage exotherm, suppressed exotherm → partial crystallinity). Feeds `/gfa-assess`, `/kissinger-kinetics`, and `/tpf-window`.

## Notes

- Apparent Tg and Tx **rise with heating rate** — only compare landmarks measured at the same β, and record β beside every value.
- A small or absent crystallization exotherm in a sample you believed glassy means it was already partly crystalline — cross-link to `/amorphicity-qa`.
- ASTM E1356 covers Tg by DSC; calibrate the instrument (ASTM E967/E968) before quoting absolute temperatures.
