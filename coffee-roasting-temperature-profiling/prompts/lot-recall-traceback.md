# Lot Recall Traceback

## Purpose

Use when a roasted SKU draws a quality complaint or recall: reconstruct the genealogy from bag back to source and scope the affected inventory as tightly as the evidence allows. Pairs with `/track-green-lot` (reverse view), `/match-profile-batch`, and Workflow D.

## Prompt Template

```
You are a traceability/recall agent in the coffee-roasting-temperature-profiling workspace.
Read context/workflows.md (Workflow D) and context/concepts.md ("Roast defects", "traceability hierarchy") first.

Investigate this complaint:

- **SKU / product:** [VALUE]
- **Roast date / batch ID / lot ID from packaging:** [VALUE]
- **Reported issue:** [e.g. baked & flat, sour, moldy/musty]
- **Available evidence:** [roast logs, batch match scores, cupping notes, green QC for the lot]
- **Scope question:** [recall this batch? this lot? this SKU run?]

Please:
1. Reconstruct SKU/batch → profile version → green lot(s) → importer/exporter → farm/station.
2. Assess the implicated batch: in-tolerance? what defect signature (curve + cup)?
3. Decide execution (one batch) vs green-quality (whole lot) by pulling the lot's other batch match scores.
4. Scope the recall to the tightest defensible boundary and list affected roasted inventory + SKUs.
5. Recommend corrective action (re-dial profile / reject remaining green / re-train) and any certification-claim impact.
```

## Expected Output

- A full genealogy from bag to source (with ICO mark / lot IDs).
- A defect classification: execution (batch-scoped) vs green quality (lot-scoped), with evidence.
- The tightest defensible recall scope and the list of affected roasted inventory/SKUs.
- Corrective actions and any chain-of-custody / certification-claim impact.
