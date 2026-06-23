# /assemble-aip-package — Build an OAIS-conformant Archival Information Package

Package QA-passed masters, derivatives, and metadata into an OAIS Archival Information Package (AIP) with structural, descriptive, and preservation metadata plus fixity, so the digital surrogate is ingestible into a trusted repository and survives long-term.

## Inputs

- QA-passed master images and the capture profile used.
- Descriptive metadata for the item/collection (catalog record, finding-aid node, or at minimum title, creator, date, identifier).
- The derivative recipe from the capture profile (access JPEGs, IIIF tiles, OCR/transcription, thumbnails).
- Target repository's ingest spec (BagIt? METS flavor? required PREMIS events?).

## Steps

1. **Generate derivatives.** Produce the access and service derivatives per the recipe (e.g. sRGB JPEG access copies, IIIF-tiled pyramids, OCR text). Keep masters untouched.
2. **Capture technical metadata.** Extract per-file technical metadata (MIX/NISO Z39.87 for still images): dimensions, bit depth, color space, capture device, ICC profile.
3. **Record provenance (PREMIS).** Log preservation events — capture, QA, derivative creation, fixity generation — each with agent, timestamp, and outcome, so the chain of custody is machine-readable.
4. **Assemble structure (METS).** Build the structural map binding masters ↔ derivatives ↔ descriptive ↔ technical ↔ provenance metadata into one navigable package; preserve page/item order.
5. **Compute fixity.** Generate checksums (SHA-256 preferred) for every file and embed them in the package manifest (hand off to `/audit-fixity-integrity` for ongoing verification).
6. **Bag and validate.** Wrap the package per the repository's transfer spec (commonly BagIt), validate against its profile, and produce an ingest-ready bundle plus a human-readable manifest.

## Output

`outputs/aip-<identifier>/` containing masters, derivatives, METS/PREMIS/MIX metadata, and a fixity manifest, plus `outputs/aip-manifest-<identifier>.md` summarizing contents, metadata coverage, fixity algorithm, and validation result. The bundle is repository-ingest-ready.

## Notes

- The AIP, not the loose TIFF, is the preservation object. A master image with no provenance or fixity is an orphan that no future curator can trust.
- Never alter masters during packaging — derivatives and metadata are added *around* the master, which stays bit-for-bit as captured.
- Descriptive metadata can be enriched later; structural integrity and fixity cannot be retrofitted cheaply. Get those right at packaging time.
