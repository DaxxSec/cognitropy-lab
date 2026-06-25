# /graphite-morphology-classify

Classify graphite in a cast-iron micrograph per ASTM A247 / ISO 945-1, quantify nodularity, and read the matrix — the single most diagnostic observation in a cast-iron case.

## Inputs

- As-polished and etched micrographs (state magnification and whether calibrated)
- Intended grade (gray A48, CGI GJV-450, ductile A536) so the result can be scored against the target window
- Section orientation relative to the suspected crack

## Steps

1. Read the **as-polished** image first — judge graphite form before etching attacks its edges.
2. Assign A247 type (I–VII), flake distribution (A–E) and size (1–8); for Mg-treated irons estimate nodularity % by image analysis (ASTM E2567 / ISO 945-4).
3. Etch read: matrix phase fractions (ferrite/pearlite, ASTM E562 point count), and flag unwanted phases — free carbides/chill, steadite network, martensite/decarb.
4. Compare against the intended-grade window; classify as in-window, marginal, or degenerate (chunky, exploded, vermicular-in-ductile, flake reversion from Mg fade).
5. Express the result as a likelihood ratio for the live hypotheses (e.g. degenerate graphite → high LR for process escape) and hand to `/bayes-evidence-update`.

## Output

`outputs/<case-id>/graphite-read.md`: type/size/distribution, nodularity %, matrix fractions, degeneration call, intended-vs-actual verdict, and the LR contribution.

## Notes

- Distinguish true interdendritic Type-D/E graphite (fast cooling) from prep pull-out; the as-polished/etched comparison settles it.
- In a part specified as ductile/CGI, flake or vermicular at the skin points to Mg fade — cross-check residual Mg via `/composition-cross-check`.
