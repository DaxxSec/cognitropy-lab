# /glaze-hazard-screen

Screen a glaze recipe for toxic materials, food-safety leaching risk, and waste-water disposal implications before any food-contact use or sale.

## Inputs

- The glaze recipe by material and percentage (e.g. "EPK 22%, silica 28%, Gerstley borate 18%, frit 3134 24%, colorant X 8%").
- Intended use: food-contact surface vs. decorative-only.
- Firing schedule (cone) and application method (dip/spray/brush).

## Steps

1. Parse the recipe into constituent materials; map each against `context/references.md` → glaze hazardous-material table.
2. Flag hazardous constituents: lead, barium carbonate, cadmium-bearing stains, lithium carbonate, manganese dioxide, soluble copper/cobalt/chrome colorants, and free silica content.
3. For **food-contact** ware: identify leach risks (lead, cadmium, soluble fluxes). Do **not** clear it on recipe inspection — require an ASTM C738/C895 acid-leach test, and recommend a stable liner glaze on the food surface if the decorative glaze is suspect.
4. For **studio safety:** note respirable silica and any fume hazard (manganese), with dust controls (wet methods, HEPA, ventilation; OSHA PEL 50 µg/m³).
5. For **waste:** flag soluble heavy metals in rinse/slurry — no drain disposal; specify settle-and-reclaim or hazardous-waste handling per local rules.

## Output

`outputs/glaze-screen-<name>-YYYY-MM-DD.md`: a constituent hazard table, a food-safety verdict (PASS / TEST-REQUIRED / FAIL with reasons), dust/fume controls, and waste-disposal guidance.

## Notes

- This command is a gate, not just analysis: a suspect food-contact glaze does not advance to production on inspection alone — the leach test is the gate.
- "Lead-free" on the label is not the same as "leach-safe" — underfiring or a bad melt can leach even nominally safe glazes; cite the cone and melt.
