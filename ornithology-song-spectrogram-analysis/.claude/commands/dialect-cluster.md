# /dialect-cluster

Cluster recordings of one species into geographic dialects or song variants — infraspecific classification — and test whether the boundary is real or a sampling artifact.

## Inputs

- Geotagged recordings of the focal species across a region, each measured
- The clustering character set (song-structure characters that vary geographically)
- A geographic resolution (how finely to bin localities)

## Steps

1. Build a song-similarity matrix (spectrographic cross-correlation or character-distance) across all recordings.
2. Cluster (hierarchical / k-medoids) into candidate acoustic classes; inspect the dendrogram for natural cut height.
3. Map each acoustic class onto geography; a true **dialect** shows a spatial boundary, not just acoustic clusters scattered everywhere.
4. Plot key characters against geographic distance to separate **clinal** (gradual) from **dialectal** (stepped) variation.
5. Report classes as infraspecific only; flag any that would need genetic/morphological corroboration before taxonomic weight.

## Output

`outputs/dialects/<species>/analysis.md` — the proposed dialect classes, a map of their distribution, the clinal-vs-stepped verdict, and sampling caveats.

## Notes

- Song sharing among neighbors (matched countersinging) creates within-population clusters that are *not* dialects — control for it.
- Never promote a dialect to species rank on acoustics alone; voice is evidence, corroboration is required.
