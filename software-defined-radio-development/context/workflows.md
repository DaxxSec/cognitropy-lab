# Software Defined Radio Development — Workflows and Methodology

Step-by-step procedures the agent uses for SDR development, all framed through the **resource-optimization** lens. Each workflow maps to one or more bespoke commands in `.claude/commands/`.

## Workflow 1: New Application Build (Design → Validate)

**Goal:** Take an SDR application from RF requirements to a validated, resource-budgeted flowgraph.

### Steps

1. **Hardware fit** — if hardware isn't chosen, run `/hardware-select` against frequency/bandwidth/duplex/budget.
2. **Rate budget** — run `/sample-rate-plan`; lock sample rate, format, link-capacity check, storage budget.
3. **Flowgraph design** — run `/flowgraph-design` against a CPU/latency budget; produce block topology with per-stage rates + compute estimate.
4. **Build** — implement in GNU Radio Companion or Python; replace any GUI sinks with appropriate sinks for the target.
5. **Profile** — run `/throughput-profile` at target rate over a 60 s window; confirm 0 overruns + headroom, or identify the bottleneck.
6. **Optimize if needed** — per the bottleneck class: `/decimation-chain-optimize` (algorithm) → `/simd-offload-plan` (SIMD/GPU) → `/buffer-tune` (scheduler).
7. **Re-profile** — confirm the optimization achieved the budget.
8. **Document** — save flowgraph + resource model to `outputs/`.

### Decision points

- **If the design estimate is over budget before building** → redesign on paper (earlier decimation, simpler demod); don't build-then-discover.
- **If profiling shows IO-bound not CPU-bound** → no amount of DSP optimization helps; reduce rate or change hardware link.

---

## Workflow 2: Decimation Chain Optimization

**Goal:** Minimize compute for a multi-stage rate conversion.

### Steps

1. From `/decimation-chain-optimize`: compute total D, factor into stages.
2. Evaluate candidate factorizations; estimate MACs/sample each.
3. Apply the Harris result — sharpest filter last (lowest rate).
4. Use CIC for large-D first stage (+ FIR droop compensation); half-bands for /2 stages.
5. Verify the chain still meets the passband/stopband mask.
6. Map to GNU Radio blocks; report speedup vs. naive single-stage.

### Decision points

- **If a large prime factor appears in D** → that stage is unavoidably costly; consider nudging the target rate to a more factorable ratio.
- **If the cheaper chain fails the filter mask** → not an optimization; back off.

---

## Workflow 3: Throughput Bottleneck Diagnosis

**Goal:** Find the actual bottleneck (not the assumed one) and classify it.

### Steps

1. From `/throughput-profile`: enable performance counters, run at target rate over a defined window.
2. Capture per-block work-time share + buffer occupancy + overrun/underrun count.
3. Cross-check system level (`perf top`, `htop`, `usbtop`).
4. Classify: compute-bound / IO-bound / scheduler-bound / single-core-bound.
5. Route to the correct remediation command per class.

### Decision points

- **Compute-bound** → `/decimation-chain-optimize` then `/simd-offload-plan`.
- **IO-bound** → reduce rate or `/hardware-select` for faster link.
- **Scheduler-bound** → `/buffer-tune`.
- **Single-core-bound** → `/simd-offload-plan` or split the block.

---

## Workflow 4: Buffer / Scheduler Tuning

**Goal:** Eliminate overruns/underruns that are buffer-related (not compute).

### Steps

1. From `/buffer-tune`: confirm via profile that no block is CPU-saturated.
2. Enlarge buffers on bursty blocks (`set_min_output_buffer`); set output multiples where helpful.
3. For real-time: RT kernel + `chrt` priority + CPU affinity + `isolcpus`.
4. Re-profile; confirm 0 overruns + report resulting latency.

### Decision points

- **If overruns persist after enlargement** → it's compute/IO, not buffers; re-diagnose.
- **If buffers fix overruns but blow latency** → reduce compute instead.

---

## Workflow 5: SIMD/GPU Offload (Last-Resort Compute Reduction)

**Goal:** Squeeze more throughput from a compute-bound block after algorithmic optimization is exhausted.

### Steps

1. From `/simd-offload-plan`: confirm `/decimation-chain-optimize` already minimized algorithmic work.
2. Run `volk_profile` on the host (free; often the entire fix).
3. Verify VOLK is using the widest available SIMD (AVX2/AVX-512/NEON).
4. For non-VOLK hot blocks → custom VOLK block or explicit SIMD intrinsics.
5. For massive parallel work → evaluate GPU, weighing PCIe transfer cost.
6. Rank options by cost/benefit; implement cheapest-first.

### Decision points

- **VOLK not profiled** → do that first, measure, reassess.
- **No AVX2/AVX-512** → limited SIMD ceiling; consider hardware.
- **GPU on small block** → transfer latency kills it; skip.

---

## Workflow 6: Headless / Embedded Deployment

**Goal:** Move a validated flowgraph to 24/7 headless operation with auto-recovery.

(Full steps in `/deploy-harden`.)

### Cross-workflow patterns shared across all SDR deployment

- Profile-validate before deploying — a flowgraph at 95% CPU on the desktop will throttle on the embedded target.
- Disable USB autosuspend + pin device by serial — the two most common embedded-SDR failures.
- Quote measured thermal + CPU headroom in the deployment README so the next operator knows the margin.
- Test the full reboot cycle, not just `systemctl start` — boot-order dependencies surface only on cold boot.
