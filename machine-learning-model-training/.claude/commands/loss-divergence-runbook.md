# /loss-divergence-runbook

Stabilise and recover a run whose loss is diverging, spiking, going NaN/inf, or flat-lining from step 0.

## Inputs

- Loss + grad_norm history around the event (a few hundred steps before/after)
- Precision mode (fp16 + loss-scale value, bf16, or fp32), LR + warmup schedule, clip value
- Path to the most recent checkpoints (and their step numbers)
- (Optional) the data batches/indices consumed near the spike

## Steps

1. **Characterise the divergence.** NaN/inf vs finite spike vs slow rise vs flat-from-0 — each has a different cause (see the `concepts.md` failure-mode list). Find the last clean step.
2. **Read the leading indicator.** Inspect `grad_norm`: a spike before the loss event points to optimisation instability; a clean grad_norm with NaN loss points to a numerical/precision issue (fp16 loss-scale collapse) or a bad batch.
3. **Stabilise / kill cleanly.** Stop the burn; preserve the last good checkpoint (never interrupt a checkpoint write).
4. **Apply the mitigation ladder** (from `references.md`), one change at a time: roll back to the pre-spike checkpoint → lower LR / lengthen warmup → confirm grad clipping → fp16→bf16 or fix loss-scale window → skip/inspect offending batches.
5. **Check for a config/code regression.** Diff against the last known-good run if the divergence is new behaviour, not a known instability.
6. **Resume and verify** for 500–1000 steps: loss back on trajectory, grad_norm in-band, no recurrence.

## Output

`outputs/incident-<id>-loss-divergence.md`: characterisation, last clean step, root-cause hypothesis, the mitigation applied, and the verification window result. Feeds `/training-postmortem`.

## Notes

- In fp16, a NaN after thousands of clean steps is *very often* loss-scale collapse — moving to bf16 removes the class.
- Large-model loss spikes are normal; the team playbook (PaLM/OPT/GLM-130B) is rollback + skip-batches + lower-LR, not panic.
- Flat loss from step 0 ≠ divergence: check for frozen params, zero LR, detached graph, or all-padding batches.
