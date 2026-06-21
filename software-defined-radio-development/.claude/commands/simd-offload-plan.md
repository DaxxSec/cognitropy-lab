# /simd-offload-plan

Plan SIMD / VOLK / GPU offload allocation for compute-heavy blocks (filters, FFTs, demodulators) after algorithmic optimization has been exhausted.

## Inputs

- **Profiling result** from `/throughput-profile` identifying the compute-bound block(s).
- **Decimation optimization status** — confirm `/decimation-chain-optimize` has already minimized the algorithmic work (offload is the last resort, not the first).
- **Host capabilities** — CPU SIMD support (SSE4/AVX2/AVX-512/NEON), GPU (CUDA/OpenCL), core count.
- **Block details** — what the hot block does (FIR filter, FFT, polyphase channelizer, demod).

## Steps

1. Read `context/concepts.md` "VOLK + SIMD" + "GPU offload tradeoffs".
2. Confirm algorithmic optimization is exhausted — offloading an unnecessarily-expensive algorithm just makes a bad design fast; fix the algorithm first.
3. Check VOLK first (cheapest win): is the hot block using VOLK kernels? Run `volk_profile` to select optimal kernels for the host CPU; many GNU Radio blocks auto-use VOLK if profiled.
4. Verify the host's SIMD level (`volk_profile` reports AVX2/AVX-512/NEON availability) — ensure VOLK is using the widest available.
5. For blocks not VOLK-accelerated → consider a custom VOLK-using block, or rewrite the hot loop with explicit SIMD intrinsics.
6. For very large FFTs / massively parallel work → evaluate GPU offload (gr-fosphor for display, custom CUDA/OpenCL blocks for FFT). Weigh PCIe transfer latency — GPU only wins if compute >> transfer cost.
7. Estimate the speedup per option (VOLK AVX2 ≈ 4-8× on float ops; GPU varies wildly with transfer overhead) vs. implementation cost.
8. Recommend the offload plan in cost/benefit order: VOLK profiling (free) → wider SIMD → custom SIMD block → GPU (last, highest effort).
9. Write the plan to `outputs/offload/<block>-<YYYY-MM-DD>.md`.

## Output

A markdown offload plan at `outputs/offload/<block>-<YYYY-MM-DD>.md` containing: confirmation that algorithmic optimization is exhausted, host SIMD/GPU capability, VOLK kernel status of the hot block, ranked offload options (VOLK profiling → wider SIMD → custom block → GPU) with estimated speedup + implementation cost each, recommendation, and PCIe-transfer-vs-compute analysis if GPU is considered.

## Decision points

- **If VOLK isn't profiled on this host** → run `volk_profile` first; it's free and often the entire fix.
- **If the host lacks AVX2/AVX-512** → SIMD speedup is limited; the bigger lever may be a faster CPU or GPU.
- **If considering GPU but the block is small** → PCIe round-trip latency likely exceeds the compute saved; GPU only wins for large, sustained, parallel workloads.

## Notes

- Order of operations: algorithm (`/decimation-chain-optimize`) → VOLK profiling → wider SIMD → custom SIMD → GPU. Never jump to GPU first.
- `volk_profile` is the single highest-ROI command in SDR optimization — it benchmarks every kernel on the actual host and picks the fastest. Run it on every new machine.
- GPU offload has a real latency floor from PCIe transfers; it's for throughput, not low-latency control loops.
- AVX-512 can downclock the CPU on some chips — measure end-to-end, not just the kernel microbenchmark.
