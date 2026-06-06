# /specimen-accession

Deposit a characterised mortar as a type specimen ("holotype") in the reference collection so future buildings can be matched against it.

## Inputs

- A completed identification report (from `/characterize-historic-mortar`) with assigned binomial name and confidence.
- Physical fragment storage reference (box/location) and photographs with scale.
- The current collection index (so duplicates and existing taxa are checked).

## Steps

1. Read `context/workflows.md` "Naming and accessioning a type specimen".
2. Check the candidate against existing accessions: if it matches a known taxon within tolerance (`context/references.md` tolerance rule), record it as **additional material** of that accession rather than a new holotype.
3. If new, mint an **accession number** `MRT-YYYY-<day>-NN` — one number = one holotype = one name.
4. Record the holotype data block: binomial name + authority + date; provenance; two-track character set; HI; binder:aggregate; aggregate grading curve; phases; photographs and thin-section image references; physical storage location; determination confidence.
5. Append the accession to the collection index so `/mortar-key` and `/match-compatible-mortar` can retrieve it.

## Output

A specimen record `outputs/accessions/<accession-number>.md` (and an index entry) holding the full holotype data block. This is the permanent reference entry for the named mortar.

## Notes

- One name = one type specimen — never reassign an accession number or rename a holotype; mint a new one instead.
- Record the *determination author* and date like a nomenclatural authority citation; provisional names get a clear `cf.` qualifier.
