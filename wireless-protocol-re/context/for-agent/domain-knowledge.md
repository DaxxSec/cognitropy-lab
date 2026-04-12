# Domain Knowledge — Wireless Protocol Reverse Engineering

## Wireless Protocol Fundamentals

### Signal Layers (OSI-Aligned)
1. **Physical Layer** — Frequency, modulation, bandwidth, power
2. **Data Link Layer** — Framing, sync words, preambles, CRC/checksums
3. **Network Layer** — Addressing, routing (if applicable)
4. **Application Layer** — Payload encoding, command structures, state machines

### Common Modulation Schemes
- **ASK/OOK** — On-Off Keying: simplest, used in cheap remotes, keyfobs, weather sensors
- **FSK** — Frequency Shift Keying: 2-FSK, 4-FSK, GFSK — Bluetooth, TPMS, pagers
- **PSK** — Phase Shift Keying: BPSK, QPSK, 8-PSK — Wi-Fi, satellite, some IoT
- **OFDM** — Orthogonal Frequency Division Multiplexing — Wi-Fi, LTE, DVB-T
- **LoRa** — Chirp Spread Spectrum — LoRaWAN IoT devices
- **DSSS** — Direct Sequence Spread Spectrum — GPS, Zigbee, older Wi-Fi

### Common ISM Band Allocations
| Band | Frequency | Common Uses |
|------|-----------|-------------|
| 315 MHz | 314.5–315.5 MHz | Keyfobs, garage doors (US) |
| 433 MHz | 433.05–434.79 MHz | Weather stations, remotes (EU/US) |
| 868 MHz | 868–870 MHz | LoRa, smart meters (EU) |
| 915 MHz | 902–928 MHz | LoRa, Zigbee, smart meters (US) |
| 2.4 GHz | 2400–2483.5 MHz | Wi-Fi, Bluetooth, Zigbee, microwave |
| 5.8 GHz | 5725–5875 MHz | Wi-Fi 5/6, radar, FPV drones |

## Reverse Engineering Methodology

### Phase 1: Signal Discovery
1. Wideband spectrum scan to identify active frequencies
2. Record waterfall data for temporal activity patterns
3. Identify center frequency, bandwidth, and duty cycle
4. Catalog all discovered signals with timestamps

### Phase 2: Signal Characterization
1. Determine modulation type (FFT shape, instantaneous frequency, constellation)
2. Measure symbol rate / baud rate
3. Identify preamble and sync word patterns
4. Estimate signal-to-noise ratio
5. Check for frequency hopping or spread spectrum

### Phase 3: Demodulation & Bit Recovery
1. Configure demodulator for identified modulation
2. Extract raw bitstream
3. Identify byte boundaries and framing
4. Look for known patterns: preamble, sync, length, payload, CRC
5. Record multiple transmissions to identify static vs. dynamic fields

### Phase 4: Protocol Analysis
1. Compare multiple captures to identify field boundaries
2. Map static fields (device ID, command codes) vs. dynamic (counters, sensor data)
3. Identify CRC/checksum algorithm (CRC-8, CRC-16, CRC-CCITT, etc.)
4. Build a protocol state machine
5. Document the complete frame structure

### Phase 5: Validation
1. Cross-reference with known protocol databases (Sigidwiki, rfhunt)
2. Verify CRC calculations match
3. Confirm field meanings through controlled experiments
4. Document edge cases and error conditions

## Resource Optimization Algorithms

### 1. Bandwidth-Constrained Spectrum Scheduling
**Problem:** Limited instantaneous bandwidth (e.g., 20 MHz) but need to cover a wide range (e.g., 300 MHz–6 GHz).

**Approach — Weighted Interval Scheduling:**
- Assign priority weights to frequency bands based on expected signal density
- Use a greedy algorithm to schedule non-overlapping capture windows
- Maximize total weight (information gain) per unit time

```
Algorithm: WEIGHTED_SPECTRUM_SCHEDULE
Input: bands[] with {center_freq, bandwidth, priority, expected_signals}
Output: ordered capture schedule

1. Sort bands by priority / bandwidth ratio (descending)
2. For each band in sorted order:
   a. If band doesn't overlap with scheduled bands -> schedule it
   b. Else -> defer to next available slot
3. Return schedule with estimated completion time
```

### 2. Adaptive Dwell Time Optimization
**Problem:** How long to monitor each frequency before moving on?

**Approach — Multi-Armed Bandit (Epsilon-Greedy):**
- Treat each frequency band as an "arm"
- Reward = number of unique signals detected per unit time
- Explore new bands with probability epsilon, exploit best-known bands with probability 1-epsilon
- Dynamically adjust epsilon based on discovery rate

### 3. Signal Priority Queuing
**Problem:** Multiple signals detected simultaneously — which to analyze first?

**Approach — Priority Queue with Dynamic Scoring:**
```
score = (novelty * 3) + (signal_strength * 1) + (duty_cycle * 2) + (complexity * 2)

Where:
- novelty: 0-1 (1 = no match to known protocols)
- signal_strength: 0-1 (normalized SNR)
- duty_cycle: 0-1 (higher = more active = more data)
- complexity: 0-1 (higher modulation order = more interesting)
```

### 4. Capture Storage Optimization
**Problem:** Raw IQ data is massive (e.g., 20 Msps x 8 bytes = 160 MB/s).

**Approach — Triggered Capture with Compression:**
- Squelch-based triggering: only record when signal power exceeds threshold
- Apply decimation when full bandwidth isn't needed
- Use zstd compression on IQ files (typical 2-4x compression on RF data)
- Implement circular buffer with event-based snapshotting

### 5. Parallel Analysis Pipeline
**Problem:** Decoding is CPU-intensive; how to allocate compute resources?

**Approach — DAG-Based Task Scheduling:**
- Model the decode pipeline as a directed acyclic graph
- Identify parallelizable stages (e.g., multiple signals can be demodulated simultaneously)
- Use topological sort to determine execution order
- Allocate CPU cores proportional to estimated stage duration

## CRC Algorithm Reference

Common CRC polynomials found in wireless protocols:

| Name | Polynomial | Width | Init | Used In |
|------|-----------|-------|------|---------|
| CRC-8 | 0x07 | 8 | 0x00 | Simple sensors |
| CRC-8/MAXIM | 0x31 | 8 | 0x00 | 1-Wire, iButton |
| CRC-16/IBM | 0x8005 | 16 | 0x0000 | Modbus, USB |
| CRC-16/CCITT | 0x1021 | 16 | 0xFFFF | X.25, Bluetooth |
| CRC-16/KERMIT | 0x1021 | 16 | 0x0000 | Many ISM devices |
| CRC-32 | 0x04C11DB7 | 32 | 0xFFFFFFFF | Ethernet, ZIP |

## Key Tools & Their Roles

| Tool | Role | Notes |
|------|------|-------|
| GNU Radio | Signal processing, demodulation | Block-based DSP, Python/C++ |
| Universal Radio Hacker (URH) | Protocol analysis, bit-level decode | Best for simple OOK/FSK |
| Inspectrum | Visual IQ analysis | Excellent for modulation ID |
| rtl_433 | Decode known ISM protocols | 200+ protocols supported |
| SigDigger | Spectrum analysis, signal hunting | Qt-based, good waterfall |
| baudline | Signal analysis, FFT | Detailed spectral views |
| Wireshark | Packet analysis (after decode) | With custom dissectors |
| CyberChef | Bit/byte manipulation | CRC calc, encoding conversion |
| hackrf_sweep | Fast spectrum scanning | Uses HackRF sweep mode |
