# Dialect Boundary Analysis

## Purpose

Decide whether a set of geotagged recordings represents distinct dialects and where any boundary lies — separating stepped (dialectal) from gradual (clinal) variation. Use with `/dialect-cluster` outputs.

## Prompt Template

```
You are an avian bioacoustician analyzing geographic song variation. Classify the variation as clinal or dialectal, and never promote a dialect to species rank on acoustics alone.

Dataset:
- **Recordings:** [N RECORDINGS, with locality + key song characters each]
- **Region / geography:** [DESCRIBE TRANSECT OR AREA]
- **Clustering result (if any):** [ACOUSTIC CLASSES FROM /dialect-cluster]

Please:
1. Map acoustic classes onto geography and state whether a spatial boundary exists.
2. Plot the discriminating character against distance — is the change stepped (dialect) or gradual (cline)?
3. Rule out song-sharing among neighbors as the source of within-population clusters.
4. Report the infraspecific classes and state explicitly what corroboration would be needed for any taxonomic claim.
```

## Expected Output

- A geography-mapped class distribution
- A clinal-vs-dialectal verdict with the character-vs-distance evidence
- A control for neighbor song-sharing
- A statement of required corroboration for taxonomic weight
