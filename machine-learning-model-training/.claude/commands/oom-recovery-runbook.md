# /oom-recovery-runbook

Diagnose an out-of-memory failure (CUDA or host) and bring the run back without losing progress.

## Inputs

- The OOM error + stack trace (which op/phase: forward, backward, optimizer step, eval?)
- Memory budget facts: model params, batch size, sequence length, precision, parallelism (ZeRO/FSDP stage, TP/PP degrees)
- Whether OOM is at step 0 (config too big) or mid-run (growth/fragmentation/leak)
- Latest checkpoint path

## Steps

1. **Localise the OOM.** When did it fire — at startup (static budget exceeded) or mid-run (activation growth on a long batch, fragmentation, an eval pass, or a leak)? The phase in the trace tells you which term blew up.
2. **Estimate the memory breakdown** (params + grads + optimizer states + activations + fragmentation) and identify the dominant term.
3. **Apply the OOM mitigation ladder** (from `references.md`), smallest change first: reduce per-device batch (raise grad-accum to keep global batch) → activation checkpointing → ZeRO/FSDP stage up → shorten/pack sequences → bf16 → optimizer offload → add tensor/pipeline parallelism (reshard checkpoint).
4. **If mid-run only on long batches:** add a max-length guard or sequence packing rather than shrinking the whole run.
5. **Check for a leak** if memory climbs monotonically: an accumulating Python list of tensors, an eval pass that doesn't `no_grad`/free, or retained graphs.
6. **Resume** via `/checkpoint-recovery` and verify memory headroom stays above the floor for a full epoch/checkpoint interval.

## Output

`outputs/incident-<id>-oom.md`: where it fired, the dominant memory term, the mitigation chosen and *why that rung of the ladder*, and the post-fix headroom.

## Notes

- Reducing batch without grad-accumulation changes the effective global batch — and thus the learning dynamics. Compensate.
- `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` can mitigate fragmentation-driven OOM.
- Changing parallelism degree usually requires resharding the checkpoint — don't assume a hot resume works across layouts.
