# /flowgraph-design

Design a GNU Radio flowgraph for a target application against an explicit resource budget (CPU cores, bandwidth, latency, memory).

## Inputs

- **Application** — what the flowgraph does (spectrum monitor, FM receiver, protocol decoder, transceiver, channelizer).
- **RF parameters** — center frequency, bandwidth of interest, expected SNR, modulation if known.
- **Hardware** — SDR device + host (CPU cores, RAM, USB/PCIe link, OS).
- **Resource budget** — max CPU cores available, target end-to-end latency, acceptable underrun probability, memory ceiling.
- **Output destination** — file, network stream, real-time sink, downstream decoder.

## Steps

1. Read `context/concepts.md` "Flowgraph design" + "Sample-rate/bandwidth tradeoffs".
2. Compute the sample-rate budget: minimum rate = bandwidth-of-interest × oversampling factor; check against hardware max and USB/PCIe link capacity.
3. Lay out the block chain: source → (DC-block/IQ-balance) → channel filter + decimation → demod/processing → sink.
4. Per block, estimate compute cost (taps × sample-rate for filters, N·log₂N × rate/N for FFTs) and place against the core budget.
5. Identify which blocks must run at full input rate (expensive) vs. post-decimation (cheap) — push compute downstream of decimation wherever correctness allows.
6. Choose FFT sizes / filter tap counts under the latency constraint (larger FFT = better frequency resolution but more latency).
7. Estimate total CPU load + headroom; if over budget, flag candidates for `/decimation-chain-optimize` or `/simd-offload-plan`.
8. Write the flowgraph spec to `outputs/flowgraphs/<app>/<YYYY-MM-DD>-design.md` with block list, rates per stage, compute estimate, headroom.

## Output

A markdown flowgraph design at `outputs/flowgraphs/<app>/<YYYY-MM-DD>-design.md` containing: application + RF parameters, stated resource budget, block-by-block chain with per-stage sample rate, compute estimate per block, total CPU load + headroom margin, and a `.grc`-ready block topology. Flags for downstream optimization if over budget.

## Decision points

- **If the minimum sample rate exceeds the USB/PCIe link capacity** → reduce bandwidth-of-interest, switch hardware, or move to a host with a faster link.
- **If estimated CPU load exceeds budget before building** → redesign (more aggressive early decimation, simpler demod) rather than building and discovering the overrun.
- **If latency budget conflicts with frequency resolution needs** → surface the tradeoff explicitly; there's no free lunch between FFT size and latency.

## Notes

- The single biggest resource lever is decimating early — every block downstream of a /D decimation runs at 1/D the cost. Get the channel filter + decimation as close to the source as correctness allows.
- Estimate before building. A flowgraph that's 2× over the core budget is cheaper to catch on paper than at runtime.
- GNU Radio's scheduler parallelizes across blocks onto cores; a single very expensive block can't be split across cores without manual work (see `/simd-offload-plan`).
