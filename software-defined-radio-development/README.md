# Software Defined Radio Development Workspace

> A Claude Code workspace for building and optimizing software-defined radio applications across the GNU Radio / SoapySDR ecosystem — framed throughout as **resource optimization**: every flowgraph, decimation chain, and buffer configuration is treated as a constrained optimization over CPU, bandwidth, latency, and memory.

## What This Workspace Does

This workspace turns SDR development from "build a flowgraph and hope it keeps up" into a resource-modeled engineering discipline. Rather than discovering overruns at runtime, it plans the sample-rate/bandwidth/CPU budget up front, optimizes decimation chains for minimum compute, profiles pipelines to find the actual bottleneck block, and sizes buffer pools to a target underrun probability.

The agent guides the full SDR build cycle: hardware selection sized to the RF problem, flowgraph design against a resource budget, decimation-chain optimization, throughput profiling, SIMD/VOLK/GPU offload planning, buffer/scheduler tuning, and headless/embedded deployment hardening.

## Why This Workspace Exists

SDR projects fail in predictable resource ways: a flowgraph that runs fine at 2 Msps falls apart at 20 Msps; a decimation chain does 4× more multiply-accumulates than necessary; a Raspberry Pi deployment thermally throttles after 10 minutes; a USB 2.0 link silently caps the achievable sample rate. These are all resource-modeling failures, and they're all predictable before you hit them. This workspace codifies the discipline: state the budget, model the resource use, measure don't estimate, and keep headroom.

## Getting Started

### Prerequisites

- **SDR hardware** — HackRF One, RTL-SDR v3/v4, USRP B2xx/X-series, BladeRF, LimeSDR, or PlutoSDR.
- **Software stack** — GNU Radio 3.10+, SoapySDR, VOLK, gr-osmosdr or device-specific drivers (UHD for USRP, etc.).
- **Profiling tools** — `perf`, `gr-perf-monitorx` (GNU Radio Performance Monitor), `htop`, `usbtop` for USB throughput.
- **Languages** — Python 3.x (GNU Radio Python API), C++ for custom blocks, optionally CUDA/OpenCL for GPU offload.
- **System** — Linux preferred (real-time-capable kernel ideal for low-latency work); macOS works for receive.

### Quick Start

1. Clone this workspace.
2. Run `/hardware-select` if you haven't picked hardware — sizes a device to your frequency/bandwidth/duplex needs.
3. Run `/sample-rate-plan` to lock the sample-rate / bandwidth / Nyquist budget for your application.
4. Run `/flowgraph-design` to design the flowgraph against a CPU/latency budget.
5. Run `/throughput-profile` once built — find the bottleneck block before optimizing anything.
6. Iterate: `/decimation-chain-optimize`, `/simd-offload-plan`, `/buffer-tune` to hit the budget.
7. Run `/deploy-harden` when moving to a headless/embedded target.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/flowgraph-design` | Design a flowgraph for a target app with a resource budget | Starting a new SDR application |
| `/decimation-chain-optimize` | Optimize a multi-stage decimation/resampling chain | When a filter chain is the compute hotspot |
| `/throughput-profile` | Profile a pipeline; identify bottleneck + headroom | First step before any optimization |
| `/buffer-tune` | Size buffers + scheduler to eliminate over/underruns | When you see `O`/`U` markers at runtime |
| `/sample-rate-plan` | Plan sample-rate / bandwidth / Nyquist budget | At application design time |
| `/hardware-select` | Recommend SDR hardware for the RF problem | Before buying / when repurposing |
| `/simd-offload-plan` | Plan SIMD/VOLK/GPU offload for heavy blocks | When CPU-bound after algorithmic optimization |
| `/deploy-harden` | Prepare for headless/embedded deployment | Moving from desktop to Pi/embedded target |

## Directory Structure

```
software-defined-radio-development/
├── CLAUDE.md                              # Agent role, available commands, foundational instructions
├── README.md                              # This file
├── .claude/commands/                      # 8 bespoke domain commands
│   ├── flowgraph-design.md
│   ├── decimation-chain-optimize.md
│   ├── throughput-profile.md
│   ├── buffer-tune.md
│   ├── sample-rate-plan.md
│   ├── hardware-select.md
│   ├── simd-offload-plan.md
│   └── deploy-harden.md
├── context/
│   ├── concepts.md                        # SDR architecture, DSP fundamentals, rate/bandwidth tradeoffs, failure modes
│   ├── workflows.md                       # Flowgraph design, decimation optimization, profiling, buffer tuning, deployment
│   └── references.md                      # Hardware spec matrix, GNU Radio block reference, DSP libraries
├── prompts/                               # 3 reusable prompts
│   ├── new-flowgraph-design.md
│   ├── throughput-bottleneck-diagnosis.md
│   └── hardware-selection.md
└── outputs/                               # Flowgraphs, profiling reports, resource models, deployment configs
```

## Example Use Cases

### Wideband spectrum monitor on a Raspberry Pi
Build a 2.4 MHz RTL-SDR spectrum monitor that runs headless on a Pi 4 without thermal throttling. `/sample-rate-plan` locks the rate to what USB 2.0 + the Pi's CPU can sustain; `/decimation-chain-optimize` minimizes the FFT/filter compute; `/deploy-harden` sets up systemd + a thermal watchdog.

### 20 Msps capture pipeline on a HackRF
A HackRF at 20 Msps saturates a single core with naive demod. `/throughput-profile` finds the bottleneck (usually the channel filter), `/simd-offload-plan` moves it to VOLK SIMD kernels, and `/buffer-tune` sizes the buffers so the USB transfer never starves.

### Multi-channel receiver on a USRP
Channelize a wide USRP capture into N narrowband streams. `/flowgraph-design` lays out the polyphase channelizer against the core budget; `/decimation-chain-optimize` picks per-channel decimation; throughput profiling confirms headroom across all N channels.

### Low-latency transceiver bring-up on a PlutoSDR
A control-loop application needs <5 ms round-trip. `/sample-rate-plan` + `/buffer-tune` minimize buffering latency while keeping underrun probability acceptable; `/flowgraph-design` keeps the DSP path short.

## Recommended MCP Servers / Tools

- **filesystem** — for `.grc` flowgraphs, IQ capture files, profiling logs, deployment configs.
- **shell** — for invoking GNU Radio (`gnuradio-companion`, `python3 flowgraph.py`), profiling (`perf`, `gr-perf-monitorx`), driver tools (`hackrf_info`, `uhd_usrp_probe`, `SoapySDRUtil`).
- **python** — for custom GNU Radio blocks, NumPy/SciPy DSP analysis, resource modeling scripts.

## Legal & Ethical Considerations

- **Transmit licensing** — transmitting on most bands requires a license (amateur radio license, ISM-band compliance, or experimental authorization). This workspace defaults to receive-only; never advise unlicensed transmission.
- **Spectrum regulations** — FCC Part 15/97 (US), ETSI (EU), or local equivalent govern what you may receive and transmit. Receiving certain communications (e.g. cellular, encrypted) may be restricted by law even when technically possible.
- **Privacy** — decoding communications you are not a party to may violate wiretapping / privacy law; analyze only signals you own, have authorization for, or are publicly documented.

## Technical References

- [GNU Radio](https://www.gnuradio.org/) — the canonical open-source SDR framework.
- [GNU Radio Performance Counters / gr-perf-monitorx](https://wiki.gnuradio.org/index.php/Performance_Counters) — flowgraph profiling.
- [VOLK (Vector-Optimized Library of Kernels)](https://www.libvolk.org/) — SIMD kernel library for GNU Radio.
- [SoapySDR](https://github.com/pothosware/SoapySDR) — vendor-neutral SDR hardware abstraction.
- [Ettus UHD (USRP Hardware Driver)](https://files.ettus.com/manual/) — USRP driver + manual.
- [PySDR: A Guide to SDR and DSP using Python](https://pysdr.org/) — Marc Lichtman's free textbook.
- [Lyons, *Understanding Digital Signal Processing* (3rd ed.)](https://www.pearson.com/) — canonical DSP reference.
- [Harris, *Multirate Signal Processing for Communication Systems*](https://www.routledge.com/) — decimation/interpolation/channelizer reference.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available. The workspace is self-contained without it.
