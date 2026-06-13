# /data-pipeline-incident-runbook

Respond to a data-integrity incident discovered mid-run: a corrupt/missing shard, tokenizer or preprocessing drift, label drift, or eval-set leakage.

## Inputs

- The symptom (read error / crash on a shard, distribution shift, suspicious metric jump, or a leakage finding)
- The data manifest: shard list, snapshot hash/version, tokenizer + preprocessing version
- Which steps/shards were consumed since the suspected onset
- The eval sets that must stay uncontaminated

## Steps

1. **Classify the data incident:** corruption (crash/skip), drift (tokenizer/normalisation change), imbalance (resume re-read/skip), or leakage (eval contamination). Each has a different blast radius.
2. **Quarantine.** Isolate the offending shard(s) or data version; stop consuming the bad data without killing a recoverable run if avoidable.
3. **Quantify exposure.** How many steps/tokens saw the bad/contaminated data? This sets severity and whether you can continue, must roll back, or must restart.
4. **Decide continue vs roll back vs restart.** Minor late-run corruption → repair shard + resume. Material leakage → roll back to before exposure or accept + disclose.
5. **For leakage specifically:** measure overlap between training data and eval sets, record the contaminated examples, and flag for the **model card** — this is a disclosure obligation, not just a fix.
6. **Repair & resume** via `/checkpoint-recovery`, and add a pre-flight data-validation check so the class can't recur silently.

## Output

`outputs/incident-<id>-data.md`: incident class, exposure quantified, the continue/rollback/restart decision with rationale, and any model-card disclosure note.

## Notes

- A non-deterministic dataloader that doesn't restore its position re-reads/skips data on resume — treat that as a data incident, fixed in `/checkpoint-recovery`.
- Tokenizer drift is silent: pin the tokenizer + preprocessing version in the run config and hash it.
- Leakage decisions are stakeholder decisions — escalate rather than quietly continuing.
