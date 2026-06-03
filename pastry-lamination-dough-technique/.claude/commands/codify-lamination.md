# /codify-lamination

Produce the reproducible "lamination codex" — the diplomatic fair-copy spec record of a laminated dough, complete enough that any baker can reproduce the build exactly.

## Inputs

- Product name and house formula (flour weight; hydration %; butter % of flour or dough weight).
- Fold regimen (or run `/collation-formula` first and reuse its output).
- Target dough and butter temperatures, rest times, proof and bake profile.
- Expected finished crumb description (optional but recommended).

## Steps

1. Record the **materials section**: each ingredient with baker's percentage, plus butter fat % and flour protein % (the "material analysis" layer).
2. Record the **structure section**: lock-in style, the collation formula, and per-turn detail (fold type, rest time, target temps).
3. Record the **process section**: mix → lock-in → turns → shaping → proof (T/RH/time) → bake (temp/time/steam).
4. Record the **expected signature**: layer count, crumb honeycomb, feet/lift, colour — what a correct bake should read like.
5. Add an **allergen + provenance header** (gluten/milk/egg, key batch lots) and a version/date stamp.

## Output

A complete codex at `outputs/codex-<product>-v<N>.md` with materials / structure / process / signature / allergens sections — the canonical record the house archives and the source for spec sheets.

## Notes

- Treat the codex as a *fair copy*: it states the intended build. The *diplomatic transcription* of what actually happened belongs in `/transcribe-bake`, kept separate.
- Bump the version (`v1 → v2`) on any deliberate recipe change so the archive keeps a clean lineage.
