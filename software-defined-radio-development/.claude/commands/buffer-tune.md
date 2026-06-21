# /buffer-tune

Size buffer pools and scheduler parameters to eliminate overruns/underruns at the target sample rate.

## Inputs

- **Flowgraph** + target sample rate.
- **Profiling result** from `/throughput-profile` confirming the issue is scheduler/buffer-related, not raw compute.
- **Latency budget** — how much buffering latency is acceptable.
- **Host** — CPU cores, RAM, OS (RT kernel?).

## Steps

1. Read `context/concepts.md` "GNU Radio scheduler + buffers".
2. Confirm via profile that this is a buffer/scheduler problem (no single block CPU-saturated, but overruns/underruns present).
3. Examine the default buffer sizing — GNU Radio auto-sizes buffers; bursty blocks may need larger buffers to ride out work-time variance.
4. Tune `min_output_buffer` / `max_output_buffer` on blocks with bursty or large work() granularity (e.g. block-based demods, file sinks).
5. Consider the output multiple / `set_output_multiple()` on blocks that prefer processing in chunks.
6. Evaluate the latency tradeoff — larger buffers absorb variance but add latency; size to the smallest that achieves 0 overruns at the latency ceiling.
7. For real-time work, consider an RT kernel + `chrt` priority + CPU affinity (`taskset`) to reduce scheduler jitter.
8. Re-run `/throughput-profile` after tuning to confirm 0 overruns + report resulting latency.
9. Write the tuning to `outputs/buffer-tuning/<flowgraph>-<YYYY-MM-DD>.md`.

## Output

A markdown buffer-tuning report at `outputs/buffer-tuning/<flowgraph>-<YYYY-MM-DD>.md` containing: confirmed problem class, buffer-size changes per block (before/after), output-multiple settings, scheduler/affinity/priority changes, resulting overrun count (target: 0) + measured latency, latency-vs-stability tradeoff note.

## Decision points

- **If overruns persist after reasonable buffer enlargement** → the problem is actually compute or IO, not buffers; re-profile.
- **If buffer enlargement fixes overruns but blows the latency budget** → the real fix is reducing compute (`/decimation-chain-optimize` / `/simd-offload-plan`), not bigger buffers.
- **If jitter is the issue (intermittent overruns under system load)** → RT kernel + CPU affinity + isolating cores (`isolcpus`).

## Notes

- Bigger buffers trade latency for stability — they don't add throughput. If you're genuinely compute-bound, no buffer size helps.
- `set_min_output_buffer()` is the main lever for blocks that produce in large bursts.
- CPU affinity (`taskset` / GNU Radio's `set_processor_affinity`) keeps a hot block on a dedicated core, reducing cache thrash + scheduler migration.
- On a non-RT kernel, expect occasional overruns under load; for hard real-time, an RT-PREEMPT kernel is the real fix.
