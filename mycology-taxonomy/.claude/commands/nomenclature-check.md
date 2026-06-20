# /nomenclature-check

Validate a proposed binomial against MycoBank and Index Fungorum — resolving status, synonymy, priority, authorship, and One Fungus = One Name — before any determination is published or labelled.

## Inputs

- The proposed binomial(s) and the authorship as currently written.
- The determination context (from `/barcode-id` / `/phylogenetic-placement`) and the circumscription intended.
- Optional: a draft species list / report to audit in bulk.

## Steps

1. Read `context/concepts.md` "Nomenclature essentials" and `context/references.md` "Nomenclatural quick-reference".
2. Look up each name in MycoBank and Index Fungorum; record the registration identifier and the listed authorship.
3. Determine current status: accepted / synonym / illegitimate (later homonym, superfluous) / invalid; resolve to the **correct** name by priority and any conservation.
4. Check authorship and basionym formatting (`Genus species (BasionymAuthor) CombiningAuthor`); fix common errors.
5. Apply **One Fungus = One Name** (ICN Art. 59): flag any anamorph/teleomorph dual name and replace with the single accepted name.
6. Confirm a registration ID exists for any post-2013 name; note if absent (invalid).

## Output

- `outputs/determinations/<accession>-nomenclature.md` (or `outputs/reports/namecheck-<date>.md` for a bulk audit) — per name: input → validated name + authorship, current status, registration ID, synonymy collapsed, and any error fixed.

## Notes

- *Validly published*, *legitimate*, and *correct* are three independent checks — pass all three before publishing.
- Legacy datasets are riddled with retired dual names; resurrecting one is the most common nomenclatural error this command exists to catch.
- When a name resolves to a synonym, record the accepted name *and* the synonym used so downstream records stay traceable.
