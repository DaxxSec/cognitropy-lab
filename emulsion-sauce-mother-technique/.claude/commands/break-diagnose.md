# /break-diagnose

Diagnose a broken, curdled, or separated emulsion and prescribe the repair or restart pathway — and feed the root cause back into the next review round.

## Inputs

- Symptom description (greasy/oily, curds/grains, weeping, thin) and the sauce type (cold mayo/aïoli vs warm hollandaise).
- The process so far: oil-addition rate, ratio, temperature reached, emulsifier used.
- Whether re-whisking re-blends it (diagnostic for creaming vs true break).

## Steps

1. Read `context/workflows.md` "Break diagnosis and repair" decision tree.
2. Classify: **creamed** (separated but droplets intact, re-blends) vs **broken/coalesced** (won't re-blend) vs **thermal curdle** (warm sauce, grains/scramble).
3. For creamed: simply re-emulsify; not a true failure — note and move on.
4. For broken cold sauce: start a fresh base (water/fresh yolk/spoon of intact mayo) and whisk the broken sauce in slowly, drop by drop, to re-stabilise the released oil.
5. For thermal curdle: drop temperature off-heat (cold water/ice) and re-whisk if mild; restart on a new yolk base if severe.
6. Assign the **root cause** (oil too fast / oil-crowded ratio / wrong temperature / too little emulsifier) and record it so `/formula-normalize` fixes the variable, not the symptom.

## Output

`outputs/break-<formula-id>-YYYY-MM-DD.md`: failure classification, repair pathway attempted and result (recovered / discarded), assigned root cause, and the specific variable change recommended for the next round.

## Notes

- Most "broken" mayo is actually creamed — try re-whisking before discarding.
- A repaired batch is still a *failed* batch for review purposes; log the failure even if the sauce is salvaged.
