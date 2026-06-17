# /campaign-typology — Match TTPs to Known Campaign Families

Classify the reconstructed intrusion against known campaign families and ATT&CK groups — comparative typology, the way costume historians place a garment within a regional/period style family by its discriminating features.

## Inputs

- The reconstructed TTP set (from the timeline) with ATT&CK technique IDs.
- Bespoke material markers (from `/material-fingerprint`) and geospatial infrastructure features (from `/geo-spread-map`).
- A reference corpus (MITRE ATT&CK Groups, internal threat-intel, prior cases).

## Steps

1. **Build the feature vector**: discriminating TTPs, bespoke tooling markers, infrastructure patterns, victimology — exclude commodity features that match everyone.
2. **Score candidates**: for each known family compute overlap, weighting discriminating techniques far above commodity ones.
3. **Require discriminators**: demand at least one strongly-discriminating shared TTP before promoting a match — shared use of a public tool is not a match.
4. **Rank hypotheses** with similarity scores and confidence bands (HIGH > 0.85, MEDIUM 0.6–0.85, LOW < 0.6).
5. **State the alternative**: for the top hypothesis, list what would falsify it and what a copycat/false-flag would look like.

## Output

`outputs/typology-<incident>-<date>.md`: ranked family hypotheses with scores and confidence, the specific discriminating TTPs driving each, and an explicit "what would refute this" section.

## Notes

- Don't force-fit to a famous group because it is famous — that is typology forcing, the classic attribution error.
- Geolocation and commodity tooling are context, never the basis of a match.
