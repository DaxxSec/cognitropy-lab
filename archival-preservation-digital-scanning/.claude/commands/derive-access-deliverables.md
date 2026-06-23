# /derive-access-deliverables — Build the access/dissemination pipeline

Define and batch-produce the public-facing deliverables derived from preservation masters — access copies, IIIF tile pyramids, OCR/transcription, and thumbnails — so the digitized collection is usable, not just safely stored.

## Inputs

- Preservation masters (untouched) and their capture profile.
- Access requirements: target viewer/platform (IIIF/Mirador, a DAMS, a discovery layer), expected screen sizes, and whether full-text search is needed.
- Rights/access status per lot (drives what may be published vs. dark-archived).

## Steps

1. **Confirm rights gating.** Filter to lots cleared for public access; route restricted material to a dark-access derivative set or exclude it. Rights status from `/plan-digitization-queue` is authoritative — never publish a lot whose rights are unresolved.
2. **Generate access copies.** From masters, produce sRGB JPEG (or lossy JPEG2000) access images at the agreed long-edge pixel size, with sensible quality/size tradeoff for the platform.
3. **Tile for deep zoom.** Produce IIIF Image API-compatible tiled pyramids (and a IIIF Presentation manifest binding pages into a navigable object) so users can pan/zoom without downloading masters.
4. **Run OCR / HTR where applicable.** For text-bearing material, generate OCR (print) or HTR (handwriting) with word-level coordinates for in-image search; capture confidence and flag low-confidence pages for review.
5. **Make thumbnails and add to the manifest.** Generate consistent thumbnails and wire derivatives + OCR + manifest into the access record.
6. **Batch and verify.** Run the pipeline as a reproducible batch (record parameters), then spot-check derivatives for color, completeness, and manifest correctness before publishing.

## Output

`outputs/access-deliverables-<collection>/` with access JPEGs, IIIF tiles + manifest, OCR/HTR text with coordinates, and thumbnails, plus `outputs/access-pipeline-<collection>.md` recording the parameters, OCR confidence summary, rights-gating decisions, and verification spot-check. Derivatives are reproducible from masters at any time — they are disposable; the masters are not.

## Notes

- Derivatives are regenerable; masters are not. Optimize derivatives freely for delivery — never "save space" by degrading or discarding a master.
- IIIF is the lever that lets users explore high-resolution material without ever touching (or downloading) the preservation master — it's both an access win and a preservation control.
- OCR confidence is metadata: surface low-confidence pages rather than presenting bad text as authoritative. Searchability without honesty about quality misleads researchers.
