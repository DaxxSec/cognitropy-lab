# /throughput-regression-runbook

Find why a run got slower — dropped tokens/s or samples/s, sagging GPU utilization, or a straggler dragging the collective.

## Inputs

- Throughput now vs the established baseline (and when the drop started)
- Per-rank step times (to spot a straggler) if multi-node
- GPU util + SM efficiency + IO/dataloader stats
- Any recent change: `num_workers`, precision, batch size, data location, fleet composition

## Steps

1. **Quantify and time-anchor.** How much slower, since when, and was there a config/data/fleet change at that boundary? A step-change points to a discrete cause; a slow drift points to thermal/IO/data growth.
2. **Split compute vs input pipeline.** High GPU util but low throughput → small/inefficient kernels; low GPU util → the GPU is *starved* (dataloader IO-bound). Check `num_workers`, prefetch, and data-storage latency.
3. **Hunt the straggler.** In synchronous training the slowest rank sets the pace. Compare per-rank step times; a single hot/slow GPU or a bad NIC stalls every all-reduce.
4. **Check comms.** NCCL retries/timeouts, fabric congestion, or a topology mismatch (NVLink vs PCIe path) degrade all-reduce.
5. **Check the environment.** Thermal throttling, a noisy neighbour on a shared node, or power capping.
6. **Apply the smallest fix, re-measure,** and normalise to MFU so you can tell a genuinely slow run from a smaller-model run.

## Output

`outputs/incident-<id>-throughput.md`: baseline vs current, the bottleneck localised (compute / input / straggler / comms / environment), the fix, and the recovered throughput + MFU.

## Notes

- "GPU util 99%" can still be a starved GPU spinning on a tiny kernel — trust MFU and the input-pipeline stats over raw util.
- Evict a straggler node and let the scheduler reschedule rather than letting one bad GPU tax the whole run.
- Storing data on slow remote storage is a top silent cause; local cache / sharded prefetch usually fixes it.
