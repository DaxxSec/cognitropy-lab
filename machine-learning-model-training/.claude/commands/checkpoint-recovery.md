# /checkpoint-recovery

Restore a run from a checkpoint with *full*, deterministic state so the resumed curve is continuous — after a crash, preemption, or node failure.

## Inputs

- Path to the target checkpoint (and its recorded step / token count)
- The checkpoint's contents (what state it actually saved)
- Current parallelism layout vs the layout the checkpoint was saved in
- The run config + framework/CUDA/driver versions

## Steps

1. **Validate the checkpoint** against the completeness checklist in `references.md`: weights, optimizer state, scheduler/step, RNG, dataloader position, global step, versions. Flag anything missing — that is your discontinuity risk.
2. **Confirm layout compatibility.** If parallelism degrees changed (TP/PP/ZeRO/FSDP), reshard the checkpoint to the new layout before loading; never load a sharded checkpoint into a different layout directly.
3. **Restore everything, not just weights.** Load optimizer moments, LR-scheduler step, all RNG states (Python/NumPy/framework/per-device CUDA), and the dataloader/sampler offset.
4. **Test-restore in a dry run** (1–10 steps) and confirm the loss picks up *on the previous trajectory* — a visible jump means incomplete state restoration.
5. **Resume the full run** and confirm the first checkpoint after resume writes and re-reads cleanly.
6. **Record the recovery point** (step, checkpoint hash) in the incident log.

## Output

`outputs/incident-<id>-recovery.md`: which checkpoint, what state was restored vs missing, the resharding step (if any), and the dry-run continuity check result.

## Notes

- A continuous loss curve across the resume is the acceptance test — a step-discontinuity almost always means optimizer or RNG state was dropped.
- Keep at least the last *two* good checkpoints; the most recent one may be the corrupt/post-incident one.
- Bitwise determinism on GPU is best-effort; aim for *trajectory* continuity, and log enough to re-derive if not.
