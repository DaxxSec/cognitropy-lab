# Software Defined Radio Development — Core Concepts

Background the agent should read before acting on flowgraph design, decimation optimization, profiling, or deployment tasks. Tuned for fast recall.

## SDR Architecture

An SDR moves the analog/digital boundary as close to the antenna as practical: RF front-end (LNA, mixer, filters) → ADC → digital signal processing in software. The host receives a stream of complex (IQ) baseband samples and does all demodulation/decoding in software.

### Signal path (receive)

```
Antenna → LNA → Mixer (tune) → Anti-alias filter → ADC → [USB/PCIe] → Host DSP
```

- **IQ (complex) sampling** — captures both amplitude and phase; sample rate R captures R Hz of bandwidth centered on the tuned frequency (not R/2 — that's real sampling).
- **Tuning** — the front-end mixer shifts the band of interest to baseband (zero-IF) or a low IF before the ADC.
- **DC offset + IQ imbalance** — zero-IF receivers have a DC spike + IQ gain/phase imbalance; correct in software (DC block, IQ balance).

## DSP Fundamentals

### Key relationships

| Quantity | Relationship |
|---|---|
| Captured bandwidth | = sample rate (for complex IQ) |
| Nyquist | signal bandwidth must be < sample rate |
| FFT bin width | sample_rate / FFT_size |
| FFT latency | ≈ FFT_size / sample_rate |
| FIR filter cost | taps × sample_rate MACs/sec |
| Decimation savings | every block after /D runs at 1/D the rate |

### Multirate DSP

- **Decimation (/D)** — low-pass filter then downsample; the filter prevents aliasing. Cost dominated by the filter at the *input* rate.
- **Interpolation (×I)** — upsample then low-pass; for TX paths.
- **Rational resampling (P/Q)** — polyphase filter; GNU Radio `rational_resampler`.
- **Multi-stage cascade** — for large D, cascade stages with the sharpest filter LAST (lowest rate) to minimize total MACs. (Harris.)
- **CIC filters** — multiplier-free integrator-comb, ideal for large-D first stage; needs FIR droop compensation.
- **Half-band filters** — for /2 stages; ~half the taps are zero → ~2× cheaper.

### Modulation/demodulation (common)

- **AM/FM** — envelope / quadrature demod; cheap.
- **ASK/OOK, FSK, GFSK** — amplitude/frequency keying; common in ISM devices.
- **PSK/QAM** — phase/amplitude constellations; need carrier + timing recovery (Costas loop, polyphase clock sync).
- **OFDM** — FFT-based; Wi-Fi, LTE, DVB.

## Sample-Rate / Bandwidth / CPU Tradeoffs

The central resource triangle:

- **Higher sample rate** → wider captured bandwidth, but more CPU, more USB/PCIe throughput, bigger files.
- **More taps / bigger FFT** → sharper filters / finer resolution, but more compute + latency.
- **Earlier decimation** → less downstream compute, but the early filter runs at the high input rate.

Every flowgraph decision trades within this triangle. The resource-optimization discipline is making those tradeoffs explicit and measured.

## GNU Radio Scheduler + Buffers

- **Block-based dataflow** — each block's `work()` consumes input items, produces output items; the scheduler runs blocks across threads/cores.
- **Buffers** — ring buffers between blocks; auto-sized but tunable (`set_min_output_buffer`). Bursty blocks need bigger buffers to ride out work-time variance.
- **Backpressure** — a slow downstream block fills its input buffer, throttling upstream. The fullest-buffer block is often the bottleneck.
- **Overruns (`O`)** — source produces faster than the graph consumes (RX can't keep up).
- **Underruns (`U`)** — sink starves (TX can't be fed fast enough).
- **Parallelism** — the scheduler spreads blocks across cores, but a single expensive block can't be split without manual SIMD/GPU work.

## VOLK + SIMD

- **VOLK** (Vector-Optimized Library of Kernels) — hand-optimized SIMD kernels for the math GNU Radio blocks use (multiply, FFT butterflies, filtering).
- **`volk_profile`** — benchmarks every kernel on the actual host CPU and picks the fastest (SSE/AVX2/AVX-512/NEON). Free, highest-ROI optimization. Run on every machine.
- **Speedup** — float SIMD typically 4-8× over scalar on AVX2.
- **GPU offload** — for very large parallel work (big FFTs); but PCIe transfer latency means it only wins when compute >> transfer.

## Hardware Capability Tiers

| Device | Freq range | Inst. BW | ADC bits | Duplex | Link |
|---|---|---|---|---|---|
| RTL-SDR v3/v4 | 24 MHz–1.7 GHz | 2.4 MHz | 8 | RX only | USB 2.0 |
| HackRF One | 1 MHz–6 GHz | 20 MHz | 8 | Half | USB 2.0 |
| PlutoSDR | 325 MHz–3.8 GHz | 20 MHz | 12 | Full | USB 2.0 |
| LimeSDR | 100 kHz–3.8 GHz | 61 MHz | 12 | Full | USB 3.0 |
| BladeRF 2.0 | 47 MHz–6 GHz | 56 MHz | 12 | Full | USB 3.0 |
| USRP B210 | 70 MHz–6 GHz | 56 MHz | 12 | Full | USB 3.0 |
| USRP X310 | DC–6 GHz | 160 MHz | 14 | Full | 10GbE/PCIe |

## Common Failure Modes

- **USB 2.0 throughput cap** — ~35-40 MB/s effective; 20 Msps × int8 × 2 = 40 MB/s is at the edge. Many "CPU" problems are USB problems.
- **Single-stage decimation for large D** — does 4×+ more MACs than a multi-stage cascade.
- **No early decimation** — running expensive blocks at full input rate instead of post-decimation.
- **VOLK not profiled** — leaving 4-8× SIMD speedup on the table.
- **USB autosuspend killing the SDR mid-run** — #1 embedded-SDR failure.
- **Thermal throttling on Pi/SBC** — works for 10 minutes, throttles under sustained load.
- **8-bit ADC for weak-near-strong signals** — insufficient dynamic range; a strong adjacent signal masks the weak one.
- **GPU offload on small blocks** — PCIe round-trip latency exceeds the compute saved.

## Operating Constraints

- **Transmit licensing** — TX requires licensing/authorization; default receive-only unless TX is confirmed authorized.
- **Spectrum + privacy law** — FCC Part 15/97, ETSI, local equivalents; some reception is legally restricted regardless of technical capability.
- **Reproducibility** — document hardware, driver + GNU Radio version, sample rate, gain, decimation chain for every result.
