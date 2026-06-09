# /space-check-dams

Design a series of check dams in a gully or concentrated-flow channel: spacing by the head-to-toe rule, the effective grade reduction they achieve, and the storage trapped behind each.

## Inputs

- Channel/gully longitudinal profile: existing bed slope S_existing (%) and length.
- Target **stable (non-erosive) grade** S_stable for the soil/lining.
- Proposed dam effective height H (crest above bed).
- Dam type (loose rock, gabion, log, or temporary wattle/silt) and expected design storm.

## Steps

1. Read `context/concepts.md` "Sediment storage & trap structures" (check dams).
2. Compute series **spacing** so the crest of each downstream dam meets the toe of the next upstream dam after re-grading to S_stable: `L ≈ H / (S_existing − S_stable)` (consistent units).
3. Compute the number of dams over the gully length and the resulting **effective grade** the series imposes (S_stable along the stepped profile).
4. Estimate sediment storage trapped behind each dam (wedge volume from H, spacing, and S_existing − S_stable); sum to series capacity.
5. Size the dam **crest/spillway** notch to pass the design storm over the structure safely; specify downstream apron/scour protection at each toe.
6. Sequence construction downstream-to-upstream (or per standard) and note temporary vs permanent intent.

## Output

`outputs/check-dams/series-<gully>-YYYY-MM-DD.md` — spacing, dam count, effective stabilized grade, per-dam and series storage, crest/spillway notch sizing, scour protection, and construction sequence.

## Notes

- Too-wide spacing leaves bed between dams above the stable grade → continued downcutting; the head-to-toe rule is the constraint, not a suggestion.
- Every dam needs a defined overflow notch and toe apron — unprotected toes scour and the dam undermines.
- Pair with `/size-grassed-waterway` upstream and `/plan-sediment-basin` downstream where concentrated flow continues.
