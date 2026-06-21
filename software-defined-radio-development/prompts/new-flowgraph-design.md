# new-flowgraph-design

## Purpose

Use when starting a new SDR application and you need a resource-budgeted flowgraph design before building. Produces the block topology, per-stage rates, and compute estimate to validate the design on paper first.

## Prompt Template

```
Acting as the SDR development engineer designing a new flowgraph against a resource budget.

Application context:

- **What it does:** [spectrum monitor / FM RX / protocol decoder / transceiver / channelizer]
- **Center frequency / band:** [VALUE]
- **Bandwidth of interest:** [VALUE]
- **Expected SNR / signal conditions:** [VALUE]
- **Modulation (if known):** [VALUE]
- **SDR hardware:** [device + max sample rate + ADC bits + link]
- **Host:** [CPU model, core count, RAM, OS]
- **Resource budget:** [max cores, target latency, acceptable underrun probability, memory ceiling]
- **Output destination:** [file / network / real-time sink / downstream decoder]

Please:
1. Compute the sample-rate budget (min rate from bandwidth × oversampling; check vs hardware max + link capacity).
2. Lay out the block chain source → filtering/decimation → processing → sink, with the sample rate at each stage.
3. Estimate per-block compute (filter taps × rate, FFT N·logN × rate/N) and total CPU load vs. the core budget.
4. Identify which blocks must run at full input rate vs. post-decimation; push compute downstream of decimation where correctness allows.
5. Choose FFT sizes / filter taps under the latency constraint.
6. Report total CPU load + headroom; flag any block needing /decimation-chain-optimize or /simd-offload-plan.
```

## Expected Output

- Sample-rate budget with link-capacity check
- Block-by-block chain with per-stage rates
- Compute estimate per block + total CPU load + headroom
- Flags for blocks needing downstream optimization
- A `.grc`-ready topology description

## Notes

- The biggest resource lever is decimating early — get the channel filter + decimation as close to the source as correctness allows.
- Validate the design fits the budget BEFORE building; a 2×-over design is cheaper to catch on paper.
- If transmitting, confirm TX authorization first — default to receive-only.
