# /lineage-trace — Material Provenance Trace

Walk material provenance forward (rod lot → finished pieces) or backward (failed piece → upstream inputs). Surface correlations between specific upstream lots / batches and downstream failure clusters.

## Two Modes

### Mode A: Forward (input-anchored)
Given a color rod lot, melt batch, or cullet source, produce the list of every batch record that consumed it and every piece those batches produced. Used when investigating a known-bad input.

### Mode B: Backward (failure-anchored)
Given a failed piece (or a cluster of failed pieces), walk back through the batch records to enumerate every upstream input each one shared. Used when investigating an unknown cause.

## Procedure

### 1. Resolve the Anchor
- **Forward:** user supplies a lot ID, supplier+lot, or melt batch number
- **Backward:** user supplies a piece ID or a list of piece IDs

### 2. Index Walk
Walk `work-log/INDEX.md` (or, if missing, scan all `work-log/<date>*.md` files). For each batch record:
- **Forward:** if any input matches the anchor, include the batch
- **Backward:** if the batch produced a target piece, harvest its full input list

Forward yields a set of batches → set of pieces.
Backward yields a set of pieces → set of batches → union of inputs across them.

### 3. Cross-Tabulation
Build a small table:
- **Forward output:** input | batches consuming it | pieces produced | failed pieces among those (with crack mode if known) | failure rate
- **Backward output:** for each failed piece, the inputs it shared with at least N − 1 of the other failed pieces (N = total failures in the cluster). The shared-inputs row at the top of the matrix is the high-suspicion cause.

### 4. Statistical Sanity Check
A correlation in the table is suggestive, not confirmatory. Print, for each suspected input:
- Times the input appeared in failed pieces (numerator)
- Times it appeared overall (denominator)
- Times the *competing inputs* appeared in failed pieces, for context
- A short note: "weak signal — needs more data" / "moderate signal — recommend a controlled test" / "strong signal — recommend pulling lot from rotation pending follow-up"

### 5. Recommended Action
Based on the strength of the correlation:
- **Weak:** keep using the input, log the suspicion to `outputs/lineage-watch/<input-id>.md` and revisit in 30 days
- **Moderate:** run a controlled test — same form, same artist, alternate input vs. suspect input, three pieces each, 30-day shelf check
- **Strong:** pull the input from rotation; notify supplier if the suspicion is supplier-side (cane lot, melt run); document in `outputs/lineage-watch/<input-id>.md`

### 6. Outputs
- Print a summary table to the conversation
- Write a full report to `outputs/lineage-traces/<anchor-id>-<date>.md`
- If the trace produces an actionable recommendation (Mode A confirmed bad input, Mode B identified a strong shared cause), update the `## Known-Bad Pairings` section of `resources/failure-mode-taxonomy.md` to encode the lesson

## Example Use

> "Pull every piece that used Effetre cobalt rod lot R-2026-04-Effetre-Cobalt and show me which ones cracked."

Mode A. The agent enumerates the four batches that included that lot, surfaces eleven pieces produced from those batches, of which four cracked within 30 days — failure rate 36% vs. studio baseline 4%. Strong signal. Recommendation: pull the lot, contact supplier, log to `outputs/lineage-watch/`.
