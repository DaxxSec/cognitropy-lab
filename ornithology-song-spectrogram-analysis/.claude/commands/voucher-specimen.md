# /voucher-specimen

Commit a classified recording as a reference voucher — the bioacoustic analog of a curated museum specimen. A voucher binds determination to evidence so it is reproducible, citable, and falsifiable.

## Inputs

- Accession ID with provenance, element inventory, measurements, and determination
- The confusion check (nearest confusable ruled out)
- A confidence statement and any caveats

## Steps

1. Verify the chain is complete: provenance → inventory → measurements → key path → confusion check. Refuse to voucher if a link is missing.
2. Assemble the dossier: taxon at its supported rank, the diagnostic characters, the key path, the spectrograms, and the recording settings.
3. Record the **nearest confusable** and the character that excludes it.
4. State confidence (e.g. confident / probable / pair-level) and what new evidence would change the determination.
5. File under `outputs/specimens/<accession-id>/voucher.md` and add a one-line entry to the running `outputs/voucher-index.md`.

## Output

`outputs/specimens/<accession-id>/voucher.md` and an appended row in `outputs/voucher-index.md` (accession, taxon, rank, locality, date, confidence).

## Notes

- A voucher is a claim with its evidence attached — never voucher a gestalt ID, and never overwrite a voucher silently; supersede it with a dated revision so the audit trail survives.
- Vouchers feed `/build-repertoire` and the keys; they are the workspace's permanent reference layer.
