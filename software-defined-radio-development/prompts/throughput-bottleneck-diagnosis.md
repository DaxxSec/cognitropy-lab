# throughput-bottleneck-diagnosis

## Purpose

Use when a flowgraph is dropping samples (overruns/underruns) or you need to know its headroom. Structures the diagnosis to find the ACTUAL bottleneck and classify it before optimizing the wrong thing.

## Prompt Template

```
Acting as the SDR development engineer diagnosing a throughput bottleneck.

Flowgraph context:

- **Flowgraph:** [path or description + block list]
- **Current sample rate:** [VALUE]
- **Target sample rate to sustain:** [VALUE]
- **Symptoms:** [overruns O / underruns U / dropped samples / want-headroom]
- **Host:** [CPU model, core count, current load]
- **SDR hardware + link:** [device + USB2/USB3/PCIe]
- **Profiling data available:** [gr-perf-monitorx output / perf top / htop / usbtop, or "need to collect"]

Please:
1. If profiling data isn't collected, specify exactly what to run (perf counters, gr-perf-monitorx, usbtop) and over what window.
2. From the data, identify the bottleneck block (highest work-time share OR chronically full/empty buffer).
3. Cross-check system level — is it actually CPU-bound, or USB/IO-bound?
4. Classify the bottleneck: compute-bound / IO-bound / scheduler-bound / single-core-bound.
5. Quantify headroom at the target rate + the max sustainable rate before overruns.
6. Route to the correct remediation: /decimation-chain-optimize, /simd-offload-plan, /buffer-tune, or /hardware-select.
```

## Expected Output

- Profiling collection plan (if data not yet gathered)
- Identified bottleneck block + buffer evidence
- Bottleneck classification (compute / IO / scheduler / single-core)
- Headroom at target + max sustainable rate
- Specific remediation command recommendation

## Notes

- Profile BEFORE optimizing — the intuitive bottleneck is usually wrong.
- Overruns (RX can't keep up) and underruns (TX starving) have different fixes — don't conflate.
- USB 2.0 caps ~35-40 MB/s; many "CPU" problems are actually the USB link saturating. Check `usbtop`.
- The bar for "solid": 0 overruns for 60 s at target rate with >20% headroom.
