# /accession-specimen

Register an incoming fungal specimen, capture its collection metadata, assign an accession, and place it into the determination queue so its arrival is measurable.

## Inputs

- Collection details: collector, date collected, locality (lat/long + datum), substrate/host, habitat, field notes, photos.
- Permit / provenance reference (Nagoya Protocol, park or landowner permit) where applicable.
- Physical state (fresh / dried / in fixative) and intended storage.
- Optional: a pre-assigned fungarium prefix and the current accession counter.

## Steps

1. Read `context/workflows.md` "Phase 1 — Accession".
2. Normalise and validate the metadata; flag missing required fields (locality, date, substrate, permit).
3. Assign the next accession number and a fungarium barcode; record drying/storage state.
4. Assign an **expected difficulty tier** (Routine / Moderate / Hard) from the candidate genus or substrate (see `context/references.md` difficulty tiers) — this routes the queue.
5. Append the specimen to the determination backlog with an arrival timestamp so `λ` (arrival rate) can be measured by the capacity commands.
6. Write the accession record.

## Output

- `outputs/accessions/<accession>.md` — the full metadata record incl. tier and queue placement.
- An appended row in `outputs/accessions/register.csv` (accession, date_in, collector, locality, substrate, tier, status=queued, permit_ref) — the arrivals log the capacity commands read.

## Notes

- Locality precision and permit metadata are not optional for legally collected material; refuse to mark "complete" without them.
- Tier at intake is a prior, not a verdict — `/barcode-id` and `/phylogenetic-placement` may re-tier a specimen, which feeds back into `/curator-allocation`.
