# /classify-faults

Build the causal DAG of the stored DTCs — separate the **leader** (root) faults from the **follower** (downstream-consequence) codes triggered by the same problem.

## Inputs

- The DTC set from `/ingest-scan` (stored/pending/permanent)
- The sensor-trust map from `/cross-validate-sensors`
- Freeze-frame conditions for each code (set order, similar conditions = likely common cause)

## Steps

1. List every DTC with its freeze-frame conditions and set order where available.
2. Group codes that set under the **same conditions** — they likely share one cause.
3. Apply known causal chains: e.g. a **misfire (leader)** can set catalyst, lean, and O₂ **followers**; a **vacuum leak (leader)** sets lean-bank followers; a **failed regen (leader)** sets a DPF-efficiency follower.
4. Demote codes whose only support is a Byzantine sensor — they may be artifacts, not real faults.
5. Name the candidate leader(s). Mark followers as "explained by" the leader so they aren't separately chased.

## Output

A causal DAG appended to the ledger: leader(s) → followers, with the reasoning for each edge and a shortlist of candidate root causes to take into `/build-quorum`.

## Notes

- Resist treating every DTC as independent — "ten codes" is usually one or two leaders with a cascade of followers.
- A permanent (Mode 0A) code that has no plausible leader among the others may *be* the leader; weight it accordingly.
