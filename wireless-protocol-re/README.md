# Wireless Protocol Reverse Engineering Workspace

> An agent workspace for systematically capturing, decoding, and reverse-engineering unknown or proprietary wireless protocols using SDR hardware, with resource optimization algorithms for efficient spectrum analysis.

## What This Workspace Does

This workspace turns your SDR hardware (HackRF, RTL-SDR, USRP, etc.) into a structured protocol reverse engineering lab. Rather than ad-hoc signal hunting, it applies resource optimization algorithms — weighted spectrum scheduling, adaptive dwell time, priority queuing — to minimize wasted scan time and maximize signal identification throughput.

The agent guides you through the full RE pipeline: spectrum discovery, signal characterization, demodulation, bit recovery, frame analysis, CRC identification, protocol state machine mapping, and final reporting.

## Why This Workspace Exists

Wireless protocol RE is a skill that combines RF engineering, digital signal processing, and security analysis. The learning curve is steep, and the process is often inefficient — manually tuning through spectrum, guessing at modulation schemes, and brute-forcing CRC algorithms. This workspace codifies proven methodology and applies algorithmic optimization to the parts of the process that benefit from it most.

## Getting Started

### Prerequisites
- SDR hardware (HackRF One, RTL-SDR v3, or similar)
- Appropriate antenna for your target frequency band
- Software: GNU Radio, Universal Radio Hacker (URH), Inspectrum, rtl_433
- Python 3.x with numpy, scipy, matplotlib
- Legal authorization to analyze target signals

### Quick Start
1. Clone this workspace
2. Run `/onboard` to configure your hardware profile, target devices, and analysis goals
3. Use `/spectrum-sweep` to discover active signals in your frequency range of interest
4. Use `/decode-signal` to walk through decoding a specific signal
5. Use `/protocol-map` to build a state machine model of the decoded protocol
6. Use `/report-findings` to generate a formal findings report

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/onboard` | Initialize workspace with your SDR setup, targets, and goals | First time setup |
| `/capture-plan` | Generate optimized RF capture plan with scheduling algorithms | Before a capture session |
| `/decode-signal` | Step-by-step signal decoding from IQ to protocol frames | After capturing an unknown signal |
| `/protocol-map` | Build protocol state machine from decoded frames | After decoding multiple frame types |
| `/spectrum-sweep` | Optimized spectrum sweep with priority-based scheduling | Signal discovery phase |
| `/compare-known` | Compare signal against known protocol signature database | Quick identification attempt |
| `/report-findings` | Generate structured RE findings report | Documenting completed analysis |

## Directory Structure

```
wireless-protocol-re/
├── CLAUDE.md                          # Agent role and instructions
├── README.md                          # This file
├── CREATION_REPORT.md                 # Workspace creation details
├── context/
│   ├── project.md                     # Your target devices and goals
│   ├── role.md                        # Your experience and tools
│   ├── constraints.md                 # Legal/ethical boundaries
│   └── for-agent/
│       ├── domain-knowledge.md        # RE methodology, optimization algorithms, CRC reference
│       ├── workflows.md              # 4 core workflows with decision trees
│       ├── environment.md            # Your SDR hardware and software setup
│       └── tools.md                  # Tool configurations and command references
├── .claude/commands/
│   ├── onboard.md                    # Workspace initialization
│   ├── capture-plan.md               # Optimized capture planning
│   ├── decode-signal.md              # Signal decoding walkthrough
│   ├── protocol-map.md               # State machine building
│   ├── spectrum-sweep.md             # Optimized spectrum survey
│   ├── compare-known.md              # Known protocol comparison
│   └── report-findings.md           # Findings report generation
├── prompts/
│   ├── unknown-signal-analysis.md    # Template for analyzing unknown signals
│   ├── ism-device-survey.md          # Template for ISM band device surveys
│   └── capture-session-setup.md      # Template for quick capture setup
├── resources/
│   ├── known-protocol-signatures.md  # Protocol fingerprint database
│   ├── sdr-settings-reference.md     # SDR configuration quick reference
│   └── crc-bruteforce-guide.md       # CRC identification methodology
├── planning/                          # Active analysis plans
├── outputs/                           # Generated reports and decoded protocols
├── user-docs/                         # User-facing reference documents
│   ├── getting-started.md            # Quick start guide
│   └── optimization-explained.md     # How the optimization algorithms work
└── work-log/                          # Session logs and capture records
    └── session-log.md                # Session logging template
```

## Core Optimization Algorithms

### 1. Weighted Spectrum Scheduling
Divides a wide frequency range into bands and assigns priority weights based on ISM band overlap, user interest, and historical signal density. Maximizes information gain per unit time.

### 2. Adaptive Dwell Time (Multi-Armed Bandit)
Uses an epsilon-greedy approach to balance exploring new frequency bands vs. spending more time on productive ones. Dynamically adjusts based on signal discovery rate.

### 3. Signal Priority Queuing
Scores discovered signals on novelty, strength, duty cycle, and complexity. Ensures the most interesting/valuable signals get analyzed first.

### 4. Capture Storage Optimization
Squelch-triggered recording, adaptive decimation, and compression to minimize storage waste while preserving all useful data.

### 5. Parallel Analysis Pipeline
DAG-based task scheduling for the decode pipeline, enabling parallel demodulation of multiple signals and efficient CPU allocation.

## Example Use Cases

### IoT Device Security Assessment
Survey all wireless devices in a smart home, identify which use encrypted vs. cleartext protocols, document attack surface for each.

### Automotive Keyfob Analysis
Capture and decode keyfob transmissions, identify rolling code algorithm, assess replay vulnerability, document protocol specification.

### Weather Station Protocol Documentation
Capture transmissions from a weather station, decode sensor data (temperature, humidity, wind), write a complete protocol specification for integration projects.

### Industrial Sensor Monitoring
Identify and decode wireless sensors in an industrial environment (LoRa, Zigbee, proprietary), map communication patterns, assess security posture.

### Unknown Device Investigation
When you find an unknown transmitter, use the systematic methodology to identify its frequency, modulation, protocol, and purpose.

## Recommended MCP Servers

- **filesystem** — For reading/writing IQ capture files and analysis scripts
- **shell** — For running SDR capture commands (hackrf_transfer, rtl_sdr, rtl_433)
- **python** — For custom DSP scripts, CRC bruteforcing, and data analysis

## Legal & Ethical Considerations

- **Authorization:** Only analyze signals you own or have explicit written authorization to test
- **Regulations:** Comply with FCC Part 15/97, ETSI regulations, or your local RF laws
- **Transmission:** Never transmit without proper licensing; this workspace focuses on receive-only analysis
- **Disclosure:** If you discover security vulnerabilities, follow responsible disclosure practices
- **Interference:** Do not jam, spoof, or interfere with any radio service, especially emergency, aviation, or government frequencies

## Technical References

- [GNU Radio Wiki](https://wiki.gnuradio.org/)
- [Universal Radio Hacker Documentation](https://github.com/jopohl/urh)
- [rtl_433 Protocol List](https://github.com/merbanan/rtl_433)
- [Sigidwiki Signal Identification](https://www.sigidwiki.com)
- [FCC ID Lookup](https://fccid.io)
- [CRC RevEng](https://reveng.sourceforge.io/)
