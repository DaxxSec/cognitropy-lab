# /run-healthcheck

Pre-flight and in-flight health audit for a training run: verify launch readiness and define the alert thresholds and SLOs that will page you.

## Inputs

- The run config (model, optimizer, LR/schedule, precision, batch size, parallelism)
- Hardware/fleet facts and the metrics backend (W&B/MLflow/TensorBoard/JSONL)
- Checkpoint cadence and storage location
- Estimated MTBF of the fleet (for checkpoint-interval sizing), if known

## Steps

1. **Pre-flight checklist.** Confirm: checkpoint saves *full* state (use the `references.md` checklist), seeds/versions logged, grad clipping configured, precision sane (prefer bf16 if available), data manifest hashed, disk/quotas sufficient for the run length.
2. **Establish baselines.** From a short warm-up, record nominal throughput, MFU, GPU mem headroom, GPU util, and the grad_norm band.
3. **Set alert thresholds** from the `references.md` table, tuned to *this* run's baselines (EMA bands for loss, grad_norm multiples, throughput % floors, memory headroom floor, heartbeat timeout, checkpoint-age budget).
4. **Define run SLOs / error budget.** E.g. "≥ 90% of baseline throughput", "checkpoint never older than N steps", "zero SEV-1 reaching final eval". Size the checkpoint interval against MTBF and cost-per-step.
5. **Wire the alerts** to the on-call channel and confirm they fire on a synthetic test.
6. **(In-flight mode)** re-run periodically to re-baseline as the loss landscape changes; alerts tuned at step 0 drift.

## Output

`outputs/healthcheck-<run>-<date>.md`: the completed pre-flight checklist, the baseline table, the tuned alert thresholds, and the run SLOs/error budget.

## Notes

- The single highest-leverage pre-flight item is **checkpoint completeness** — most painful incidents are really *recovery* incidents.
- Set thresholds off EMA/baselines, not absolute numbers — a 7B and a 70B run page at different values.
- Run this *before* launch; the cheapest incident is the one your pre-flight prevented.
