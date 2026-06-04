# /segregation-conflict

Traffic-analyse a co-loaded set of dangerous goods against the segregation table — finding the collective hazard that no single-line check can see, because each item is individually legal but the *combination* is prohibited.

## Inputs

- The full set of UN numbers / classes / divisions to be co-loaded (one container, vehicle, or hold).
- The transport mode (the segregation table differs: IMDG codes 1–4, HMR §177.848, ADR mixed-loading).
- Codebook edition.

## Steps

1. Decode each item to its class/division and subsidiary risk.
2. Build the pairwise co-load matrix of all items in the load.
3. For each pair, look up the segregation requirement in the mode's segregation table (away from / separated from / separated by compartment / longitudinally separated; or "X = prohibited").
4. Flag every pair whose required separation is not satisfiable in the planned stow, and every outright-prohibited pair.
5. Highlight classic reaction conflicts even when the table is borderline: oxidizers (5.1) with flammables (3/4), acids (8) with cyanides/sulfides (toxic-gas evolution), water-reactives (4.3) with anything wet.

## Output

A segregation report at `outputs/segregation-<load>-<date>.md`: the co-load matrix, the conflicting pairs with their required separation, and a load verdict (`compatible` / `requires re-stow` / `prohibited`).

## Notes

- Segregation is a property of the *whole load*, so re-run it whenever an item is added — a late addition can make a previously-clean load illegal.
- Treat a prohibited pair as documentation-OOS-equivalent: the load must not move as planned.
