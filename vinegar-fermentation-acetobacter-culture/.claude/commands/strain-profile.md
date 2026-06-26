# /strain-profile

Build or update a profile for an AAB genus/strain — optimal temperature, ethanol tolerance, acetic-acid tolerance, overoxidation tendency, and cellulose output — from references and your own observations.

## Inputs

- Genus/strain identifier (e.g. `Komagataeibacter europaeus`, or "wild mother, lineage M-3").
- Any reference data (culture-collection datasheet, paper, DOI).
- Your own batch observations for this strain if available.

## Steps

1. Read `context/references.md` (AAB genera table, culture collections) and `context/concepts.md` §1.
2. Gather documented traits: optimal T range, ethanol tolerance, acetic-acid tolerance, overoxidation behavior, cellulose/pellicle production, preferred substrate.
3. Reconcile published data with your own `measured` observations; note where they diverge.
4. Derive practical implications: max safe starting ABV, harvest-window risk (overoxidation), suitability per production method, expected mother behavior.
5. Tag each trait with its confidence (`published` vs `measured` vs `inferred`).
6. Write/refresh `outputs/kb/microbiology/strain-<id>.md` and link it from `_index.md`.

## Output

- `outputs/kb/microbiology/strain-<id>.md` — a structured strain profile with confidence-tagged traits and practical implications.
- A summary in chat (best use, ABV ceiling, overoxidation risk).

## Notes

- *Komagataeibacter* strains tolerate higher ethanol/acidity and overoxidize less — favored for high-acidity submerged work.
- *Gluconobacter* favors sugary, lower-acidity substrates; don't expect it to drive a 6%+ vinegar.
- Names changed: `Acetobacter xylinum` → `Komagataeibacter xylinus`; cross-reference old literature accordingly.
