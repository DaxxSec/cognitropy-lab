# Batch Postmortem

## Purpose

Use this prompt after a failed, stalled, or unexpectedly excellent batch to extract a structured postmortem and write the durable lessons back into the knowledge base. Turns a one-off outcome into reusable `measured` knowledge.

## Prompt Template

```
You are a vinegar-fermentation analyst running a blameless batch postmortem.

Here is the batch:

- **Batch ID / style:** [VALUE]
- **Substrate & starting ABV/Brix:** [VALUE]
- **Strain / mother lineage:** [VALUE]
- **Method & equipment:** [Orleans / generator / submerged; aeration mode]
- **Temperature history:** [VALUE]
- **Acidity titration timeline:** [date → acidity %]
- **Residual ethanol at harvest:** [VALUE]
- **Outcome & what felt wrong/right:** [VALUE]

Please:
1. Reconstruct the timeline and identify the decisive moment(s) the trajectory was set.
2. Separate root cause from symptoms (aeration / temperature / ABV-vs-tolerance / inoculum / strain / harvest timing).
3. State what to change next batch, as concrete parameter targets.
4. Extract 1–3 atomic, reusable lessons as KB-entry candidates (title, body, taxonomy tag, confidence=measured, provenance=this batch ID).
```

## Expected Output

- A timeline reconstruction with the decisive moments marked.
- Root cause vs. symptoms, separated.
- Concrete parameter changes for the next batch.
- 1–3 KB-entry candidates ready for `/kb-ingest` (tagged `measured`, provenance = this batch).
