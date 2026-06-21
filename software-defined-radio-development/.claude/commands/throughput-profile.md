# /throughput-profile

Profile a running flowgraph or DSP pipeline; identify the bottleneck block and quantify headroom against the target rate.

## Inputs

- **Flowgraph** — `.grc` or Python flowgraph + its current sample rate.
- **Target sample rate** the pipeline must sustain.
- **Host** — CPU model, core count, current load.
- **Symptoms** — overruns (`O`), underruns (`U`), dropped samples, or just "want to know headroom."

## Steps

1. Read `context/workflows.md` "Throughput profiling".
2. Enable GNU Radio performance counters (`GR_CONF_PERF_COUNTERS` or `--enable-perf-counters`); run `gr-perf-monitorx` for live per-block work/throughput.
3. Run the flowgraph at the target rate over a defined measurement window (e.g. 60 s); record overrun/underrun count.
4. Per block, capture: % of time the block is the work-bottleneck, average work() time, input/output buffer occupancy.
5. Identify the bottleneck block — the one with the highest work-time share OR the one whose output buffer is chronically full (downstream can't keep up) / input buffer chronically empty (it's starving downstream).
6. Cross-check system-level with `perf top` / `htop` — is it actually CPU-bound, or is it USB/IO-bound (check `usbtop`)?
7. Distinguish bottleneck classes: compute-bound (a block's work() dominates), IO-bound (USB/PCIe link saturated), scheduler-bound (buffer sizes causing thrash), or single-core-bound (one block can't parallelize).
8. Quantify headroom: at target rate, what fraction of available compute is used? What's the max sustainable rate before overruns?
9. Write the profile to `outputs/profiles/<flowgraph>-<YYYY-MM-DD>.md` with bottleneck identification + recommended remediation command.

## Output

A markdown profile report at `outputs/profiles/<flowgraph>-<YYYY-MM-DD>.md` containing: measurement window, overrun/underrun count, per-block work-time table, identified bottleneck + its class (compute/IO/scheduler/single-core), headroom at target rate, max sustainable rate, and the recommended next command (`/decimation-chain-optimize`, `/simd-offload-plan`, `/buffer-tune`, or `/hardware-select`).

## Decision points

- **If bottleneck is compute-bound in a filter/FFT** → `/decimation-chain-optimize` then `/simd-offload-plan`.
- **If bottleneck is IO-bound (USB/PCIe saturated)** → reduce sample rate, or `/hardware-select` for a faster link (USB3 / PCIe / 10GbE).
- **If overruns persist but no block is CPU-saturated** → scheduler/buffer issue; `/buffer-tune`.
- **If one block pins a single core at 100% while others idle** → single-core-bound; `/simd-offload-plan` or split the block.

## Notes

- Profile BEFORE optimizing. The intuitive bottleneck is often wrong — measure which block actually dominates.
- Overruns (`O`) = source producing faster than flowgraph consumes (RX can't keep up). Underruns (`U`) = sink starving (TX path can't feed fast enough). Different fixes.
- USB 2.0 caps ~35-40 MB/s effective; an 8-bit IQ HackRF at 20 Msps = 40 MB/s is right at the edge. Many "CPU" problems are actually USB problems.
- A clean 0-overrun run for 60 s at target rate with >20% headroom is the bar for "this is solid."
