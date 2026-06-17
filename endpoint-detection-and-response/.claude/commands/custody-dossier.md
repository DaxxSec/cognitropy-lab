# /custody-dossier — Assemble the Defensible Evidentiary Package

Compile the full reconstruction into a court/IR-ready dossier with provenance, a confidence-tagged timeline, a geospatial annex, and a complete chain-of-custody log — the published, defensible record of the find.

## Inputs

- All prior outputs: provenance chains, anachronism sweep, timeline, stratigraphy, fingerprint, geo-spread, typology, condition report, detections.
- The acquisition log: artifact hashes at accession and every transfer since.
- Audience: internal IR, executive, regulator, or counsel (sets tone and redaction).

## Steps

1. **Assemble chain of custody**: every artifact with acquisition SHA-256, source, collector, and transfer history; flag any break.
2. **Write the executive summary**: what happened, scope, confidence, and recommended actions — using only `CONFIRMED`/`INFERRED` material.
3. **Compile the body**: confidence-tagged timeline, provenance chains, anachronism findings, stratigraphy, material fingerprint, and typology hypotheses with scores.
4. **Attach the geospatial annex**: host-cluster map, diffusion sequence, geovelocity exceptions, and C2 supply-line map with resolution/source notes.
5. **Quarantine conjecture**: place all `CONJECTURE` in a clearly labelled appendix so it can never be read as established fact; redact PII per audience.

## Output

`outputs/dossier-<incident>-<date>.md`: a complete report — executive summary, chain-of-custody log, evidence body, detection rules, geospatial annex, and a separated conjecture appendix.

## Notes

- The dossier's credibility rests on the evidence/conjecture wall — never let it leak.
- A custody break does not void the dossier but must be disclosed; hidden breaks do void it.
