# /entry-dedup-merge — Detect Duplicates and Propose Canonical Merges

Find emitter entries that describe the same signal under different names or from different captures, and propose a single canonical merged entry.

## Inputs

- The KB at `outputs/kb/`
- Optional: a frequency tolerance (default: overlap of `freq_range`, or center frequencies within the larger entry's bandwidth) and a name-similarity threshold

## Steps

1. **Block candidates.** Group entries that could be duplicates: overlapping frequency ranges, or same service + region + similar bandwidth. (Blocking first avoids an all-pairs comparison.)
2. **Score similarity.** Within each block, compare center frequency, bandwidth, modulation, service, and name/identification. Produce a 0–1 duplicate score; flag pairs above threshold.
3. **Decide the relationship.** For each flagged pair classify: `duplicate` (same emitter, merge), `variant` (same system, different mode/channel — link, don't merge), or `coincidental` (different emitters that happen to be near in frequency — keep separate, add a disambiguation note).
4. **Build the merge proposal.** For true duplicates pick the canonical entry (highest confidence / richest provenance), union the provenance and citations, take the most recent measurements, and preserve both histories. Keep the surviving `id`; record the absorbed `id` as an alias.
5. **Emit proposals for review.** Write merge proposals without destroying anything; apply only on confirmation, then leave a tombstone redirect at the absorbed entry's path.

## Output

`outputs/dedup-proposals-<date>.md`: each proposed merge with the chosen canonical entry, the merged field set, alias mapping, and the rationale. On approval, an updated canonical entry + tombstone redirect for the absorbed one.

## Notes

- Never silently delete — always leave an alias/tombstone so old citations (in the FAQ, query log) still resolve.
- Adjacent-channel emitters of the same system are *variants*, not duplicates; merging them loses real structure. Link with `related` instead.
- Re-run after large ingests, which are the main source of duplicate drafts being promoted twice.
