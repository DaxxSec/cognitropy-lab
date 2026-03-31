# Workflows

This document defines the core workflows SATCOM-SIM uses to handle user requests. Each workflow is a step-by-step process that produces a concrete output artifact.

---

## Workflow 1: Link Budget Simulation

**Trigger:** User asks about whether a link will close, signal strength, margin, or link budget.

### Step 1: Gather Parameters
Ask for or infer:
- Satellite orbital regime (LEO ~550km, MEO ~20,000km, GEO ~35,786km)
- Uplink or downlink (or both)
- Frequency band (UHF 400-450 MHz, S-band 2-4 GHz, X-band 8-12 GHz, etc.)
- Transmit power (dBW or dBm)
- Transmit antenna gain (dBi) or antenna type
- Receive antenna type and gain
- Target bit rate and modulation scheme
- Required BER or Eb/N0 target

### Step 2: Compute Free-Space Path Loss
```python
import numpy as np
def fspl(freq_hz, distance_m):
    c = 3e8
    wavelength = c / freq_hz
    return 20*np.log10(4 * np.pi * distance_m / wavelength)

# Example: ISS at 550km altitude, elevation 30°
# Slant range at 30° elevation ≈ 1,100 km
freq = 437.5e6  # Hz (70cm amateur band)
slant_range = 1100e3  # meters
loss = fspl(freq, slant_range)
# Result: ~141 dB
```

### Step 3: Account for Additional Losses
| Loss Source | Typical Value | Notes |
|---|---|---|
| Atmospheric absorption | 0.3–3 dB | Frequency and elevation dependent |
| Rain fade | 0–10 dB | Worst case for X-band and above |
| Polarization mismatch | 0–3 dB | Circular vs linear |
| Pointing loss | 0–3 dB | Tracking accuracy |
| Cable/connector losses | 0.5–2 dB | Ground station hardware |
| Ionospheric scintillation | 1–6 dB | Worse at low frequencies, high solar activity |

### Step 4: Compute Received Power
```
Prx (dBW) = Ptx + Gtx - FSPL - Lother + Grx
```

### Step 5: Compute Noise Floor
```python
def noise_power(noise_temp_k, bandwidth_hz):
    k = 1.38064852e-23  # Boltzmann constant
    return 10*np.log10(k * noise_temp_k * bandwidth_hz)  # dBW

# Typical RTL-SDR system noise temp: ~500-1000 K
# Professional LNA-equipped receiver: ~100-300 K
noise = noise_power(500, 9600)  # 9600 bps bandwidth
```

### Step 6: Compute Margin
```
C/N0 = Prx - N0  (dBHz)
Eb/N0 = C/N0 - 10*log10(bit_rate)
Margin = Eb/N0_actual - Eb/N0_required
```

### Step 7: Output Link Budget Table
Produce a complete table:
```
LINK BUDGET: ISS 437.5 MHz Downlink (Elevation: 30°)
================================================================
Transmit Power (Ptx)                     +0.5 dBW   (3.2 W)
Transmit Antenna Gain (Gtx)              +0.0 dBi   (dipole)
EIRP                                     +0.5 dBW
----------------------------------------------------------------
Free-Space Path Loss (FSPL)             -141.2 dB
Atmospheric Loss                          -0.5 dB
Pointing Loss                             -1.0 dB
Total Path Loss                         -142.7 dB
----------------------------------------------------------------
Receive Antenna Gain (9-ele Yagi)        +12.0 dBi
Received Power                          -130.2 dBW
----------------------------------------------------------------
System Noise Temperature                    500 K
Noise Bandwidth                           9,600 Hz
Noise Power (N)                         -154.4 dBW
----------------------------------------------------------------
C/N Ratio                                +24.2 dB
Required Eb/N0 (BPSK, BER=1e-5)          +9.6 dB
Required C/N (9600 bps)                  +49.4 dBHz
Actual C/N0                              +64.0 dBHz
LINK MARGIN                             +14.4 dB   ✅ CLOSES
================================================================
```

---

## Workflow 2: Protocol Frame Decoding

**Trigger:** User provides a hex string, binary capture, or frame bytes and wants to understand what it is.

### Step 1: Identify the Protocol
Look for telltale signatures:
- `7E` byte = AX.25 flag (HDLC framing)
- `0x1ACFFC1D` = CCSDS sync marker (first 4 bytes of TM transfer frame)
- `$GPGGA` = NMEA (GPS, used in some satellite systems)
- KISS frame: starts with `C0`, ends with `C0`
- DVB-S2 BBFRAME: starts with sync word after demodulation

### Step 2: Parse the Frame Structure
Use construct or manual parsing. Example for AX.25:
```python
from construct import *

# AX.25 UI Frame (simplified)
AX25Address = Struct(
    "callsign" / Array(6, Byte),
    "ssid" / Byte,
)

AX25Frame = Struct(
    "dest" / AX25Address,
    "source" / AX25Address,
    "control" / Byte,
    "pid" / Byte,
    "info" / GreedyBytes,
)

# Decode (after stripping flag bytes and CRC)
frame_bytes = bytes.fromhex("your_hex_here")
parsed = AX25Frame.parse(frame_bytes)

# Decode callsign (AX.25 shifts each char left by 1 bit)
def decode_callsign(addr_bytes):
    return ''.join(chr(b >> 1) for b in addr_bytes[:6]).strip()
```

### Step 3: Annotate Each Field
Produce an annotated breakdown:
```
AX.25 UI Frame Analysis
========================
Raw hex: 82A0A4A6A840 9C6094A8A040 03 F0 ...
                         ↑              ↑
                    Src addr      Ctrl  PID

DESTINATION: W6XYZ-1
  82 A0 A4 A6 A8 40 = "W6XYZ " (each byte >> 1)
  40 = SSID byte → SSID=0, C-bit=0 (not command)

SOURCE: N6ABC-0
  9C 60 94 A8 A0 40 = "N6ABC " (each byte >> 1)
  40 = SSID byte → SSID=0, H-bit=0 (not repeated)

CONTROL: 03 = UI frame (unnumbered information)
PID: F0 = No layer 3 protocol

INFO FIELD (APRS payload):
  "!3723.10N/12152.36W>ISS Gateway"
  → APRS position report at 37°23.10'N, 121°52.36'W
```

### Step 4: Validate CRC
For AX.25, verify the CRC-CCITT (FCS):
```python
import crcmod
crc_fn = crcmod.predefined.mkCrcFun('crc-ccitt-false')
payload = frame_bytes[:-2]  # strip 2-byte FCS
fcs = frame_bytes[-2:]
computed = crc_fn(payload)
# Compare computed to fcs (little-endian)
```

---

## Workflow 3: Scenario Test Design

**Trigger:** User wants to test a protocol implementation, ground station software, or communication system.

### Step 1: Define the System Under Test (SUT)
- What component is being tested? (Ground station uplink, satellite modem, protocol stack)
- What is the interface? (Binary socket, serial port, audio, IQ stream)
- What protocol version and configuration?

### Step 2: Define Test Objectives
- Nominal operation: Does it work in ideal conditions?
- Edge cases: Does it handle boundary conditions correctly?
- Error handling: Does it degrade gracefully?
- Performance: Does it meet timing requirements?
- Security: Does it reject invalid or malicious frames?

### Step 3: Generate Test Vector Suite

**Nominal Cases:**
1. Valid UI frame with minimal payload
2. Valid UI frame with maximum allowed payload
3. Valid sequence of numbered I-frames (AX.25 connected mode)
4. Command frame followed by acknowledgment

**Edge Cases:**
5. Frame with maximum length information field (256 bytes AX.25)
6. Frame with empty information field
7. Callsign with SSID=15 (maximum)
8. Repeated frame (via digipeater)

**Error Cases:**
9. Frame with invalid CRC → SUT should discard
10. Truncated frame (missing FCS) → SUT should discard
11. Frame with unknown PID → SUT should handle gracefully
12. Back-to-back frames with no gap → timing stress test

**Security Cases:**
13. Frame claiming to be from a privileged callsign (spoofed source)
14. Replay of a previously valid command frame
15. Oversized frame exceeding maximum frame length

### Step 4: Define Expected Outcomes
For each test vector, define:
- Expected SUT action (accept/reject/specific response)
- Observable indicator (output on socket, log entry, acknowledgment frame)
- Pass/fail criterion

### Step 5: Produce Test Plan Document
```
SCENARIO TEST PLAN: AX.25 Protocol Stack — v1.0
============================================================
Test ID: AX25-TC-001
Description: Valid UI frame, minimum payload
Pre-conditions: SUT initialized, listening on port 8001
Input: 7E [dest][src] 03 F0 41 [FCS] 7E
Expected Output: Frame logged with correct source/dest
Pass Criterion: Log entry contains decoded callsigns within 100ms
Expected Result: PASS
------------------------------------------------------------
Test ID: AX25-TC-009
Description: Frame with invalid CRC
Pre-conditions: SUT initialized
Input: 7E [dest][src] 03 F0 41 FF FF 7E (corrupted FCS)
Expected Output: Frame silently discarded, error counter incremented
Pass Criterion: No output frame, error_count++ observable
Expected Result: PASS (correct rejection)
============================================================
```

---

## Workflow 4: Orbital Pass Simulation

**Trigger:** User asks about when a satellite is visible, Doppler shift, or timing of communication windows.

### Step 1: Get TLE Data
Either user provides TLE or agent notes where to get it:
- Celestrak: https://celestrak.org/SOCRATES/
- Space-Track: https://www.space-track.org (requires login)
- AMSAT: https://amsat.org/keps/

Example TLE (ISS):
```
ISS (ZARYA)
1 25544U 98067A   24001.50000000  .00001000  00000+0  10000-4 0  9993
2 25544  51.6450  100.0000 0001000  90.0000 270.0000 15.50000000000001
```

### Step 2: Compute Pass Parameters
```python
from skyfield.api import load, EarthSatellite, Topos
from skyfield import almanac

ts = load.timescale()
tle_line1 = "1 25544U 98067A   24001.50..."
tle_line2 = "2 25544  51.6450  100.0000..."
satellite = EarthSatellite(tle_line1, tle_line2, 'ISS', ts)

# San Jose, CA
observer = Topos(latitude_degrees=37.338, longitude_degrees=-121.886)

# Find passes over next 24 hours
t0 = ts.now()
t1 = ts.tt_jd(t0.tt + 1.0)
times, events = satellite.find_events(observer, t0, t1, altitude_degrees=10.0)
```

### Step 3: Compute Doppler Shift Profile
```python
def doppler_profile(satellite, observer, t_start, t_end, freq_hz, n_points=100):
    c = 299_792_458  # m/s
    times = ts.tt_jd(np.linspace(t_start.tt, t_end.tt, n_points))
    shifts = []
    for t in times:
        diff = satellite - observer
        topo = diff.at(t)
        _, _, _, _, _, range_rate = topo.frame_latlon_and_rates(observer)
        # range_rate in km/s, positive = moving away
        doppler = -freq_hz * range_rate.km_per_s * 1000 / c
        shifts.append(doppler)
    return shifts

# For ISS at 437.525 MHz, expect +/-4 kHz during a pass
```

### Step 4: Produce Pass Report
```
ORBITAL PASS SIMULATION: ISS (437.525 MHz)
Observer: San Jose, CA (37.338°N, 121.886°W)
================================================================
NEXT PASS: 2026-03-30 14:23:15 UTC

Phase           | Time (UTC)   | Elevation | Azimuth | Doppler
----------------|--------------|-----------|---------|--------
AOS (Acquire)   | 14:23:15     |  10.0°    | 315° NW | +4.2 kHz
Max Elevation   | 14:26:41     |  62.3°    | 205° SW | +0.1 kHz
LOS (Loss)      | 14:30:08     |  10.0°    |  95° E  | -4.1 kHz

Pass Duration: 6 min 53 sec
Peak Elevation: 62.3° (EXCELLENT — high pass)
Max Doppler: ±4.2 kHz (compensate in GNURadio)
Usable Window (>15°): 14:24:12 to 14:29:10 (4 min 58 sec)

Protocol Timing Notes (9600 bps, AX.25):
  • AOS + 60s: Begin uplink attempts
  • AOS + 90s to LOS - 90s: Optimal uplink/downlink window
  • Apply Doppler pre-compensation: set center freq to 437.521 MHz
    at AOS, 437.525 at max elevation, 437.529 at LOS
================================================================
```

---

## Workflow 5: Protocol Security Audit

**Trigger:** User asks about security vulnerabilities in a satellite protocol or implementation.

### Step 1: Characterize the Protocol
- Authentication mechanism (if any)
- Encryption (if any)
- Frame numbering / anti-replay mechanism
- Command vs. telemetry directionality
- Access control model

### Step 2: Apply Threat Model (STRIDE)
For satellite protocols, STRIDE maps as:

| Threat | Satellite Context |
|---|---|
| **S**poofing | Forging ground station callsign / uplink address |
| **T**ampering | Modifying frames in transit (low elevation multipath opportunity) |
| **R**epudiation | Denying that a command was sent (logging integrity) |
| **I**nformation Disclosure | Receiving/decoding unencrypted telemetry |
| **D**enial of Service | Jamming or flooding the command uplink |
| **E**levation of Privilege | Sending privileged commands without authorization |

### Step 3: Analyze Specific Vulnerabilities

**AX.25 (Classic Amateur Satellite Protocol):**
- No authentication — any station can forge any callsign
- No encryption — all frames readable by anyone with an SDR
- No anti-replay — replaying a valid command frame is trivial
- No command authorization — if you know the frame format, you can command
- Risk: Medium for amateur satellites (usually accepted), High for commercial if mistakenly used

**Unprotected CCSDS TC:**
- CCSDS provides a security layer (CCSDS 352.0-B-2) but it's optional
- Without security layer: same issues as AX.25 plus higher reliability framing
- With MAP (Multiplexing Access Point) IDs: some isolation between command streams
- Risk: High if security layer not implemented

**Recommendation Pattern:**
```
Finding: [ID] - [Title]
Severity: Critical / High / Medium / Low / Informational
Protocol: [Protocol name and version]
Description: [What the vulnerability is]
Attack Scenario: [How an attacker would exploit it]
Evidence: [Test vector or proof of concept at frame level]
Remediation: [What to do about it]
References: [CCSDS Blue Book, CVE, research paper]
```

### Step 4: Produce Security Assessment Report
Structured document with:
1. Executive Summary
2. Scope and Methodology
3. Findings (sorted by severity)
4. Risk Matrix
5. Remediation Roadmap

---

## Workflow 6: CCSDS Frame Construction

**Trigger:** User needs to construct or validate CCSDS protocol frames.

### CCSDS TC Transfer Frame Structure
```
Bits:
0-1:   Transfer Frame Version Number (always 00)
2:     Bypass Flag (0 = type-A, 1 = type-B)
3:     Control Command Flag (0 = data, 1 = control)
4-9:   Reserved (000000)
10-19: Spacecraft ID (10 bits, 0-1023)
20-21: Virtual Channel ID (2 bits, 0-3)
22-29: Frame Length - 1 (8 bits, making total max 1024 bytes)
30-37: Frame Sequence Number (8 bits, wraps 0-255)
38+:   Data Field (variable)
Last:  Frame Error Control (CRC-CCITT, 2 bytes) - if enabled
```

```python
from construct import *
import struct

CCSDS_TC_Frame = BitStruct(
    "version" / BitsInteger(2),        # Always 0b00
    "bypass_flag" / Flag,
    "control_cmd_flag" / Flag,
    "reserved" / BitsInteger(6),       # Always 0b000000
    "spacecraft_id" / BitsInteger(10), # 0-1023
    "vcid" / BitsInteger(2),           # Virtual Channel ID
    "frame_length_minus1" / BitsInteger(8),
    "frame_sequence_number" / BitsInteger(8),
    "data" / GreedyBytes,
)

def build_tc_frame(spacecraft_id, vcid, sequence_number, data, include_fec=True):
    import crcmod
    header = 0
    header |= (0b00 << 30)           # Version
    header |= (0 << 29)              # Bypass flag
    header |= (0 << 28)              # Control cmd flag
    header |= (spacecraft_id << 18)  # SCID
    header |= (vcid << 16)           # VCID
    frame_len = 5 + len(data) + (2 if include_fec else 0)
    header |= ((frame_len - 1) << 8) # Frame length - 1
    header |= sequence_number        # FSN

    frame = struct.pack('>I', header) + b'\x00' + data

    if include_fec:
        crc_fn = crcmod.predefined.mkCrcFun('crc-ccitt-false')
        crc = crc_fn(frame)
        frame += struct.pack('>H', crc)

    return frame
```

---

## Workflow 7: SDR Signal Analysis Guidance

**Trigger:** User describes or provides an SDR capture and wants to identify or decode it.

### Step 1: Initial Signal Characterization
Ask for / look for:
- Center frequency
- Sample rate
- Observed bandwidth of signal
- Modulation appearance (tone, spread, FM deviation, etc.)
- Any context (time, location, orbital pass timing)

### Step 2: Identify Modulation
Common satellite signal signatures:
| Modulation | Spectral Shape | Bandwidth | Common Use |
|---|---|---|---|
| BPSK | Two-lobe sinc-like | ≈ symbol rate | CCSDS downlinks |
| QPSK | Two-lobe sinc | ≈ symbol rate/2 | DVB-S, higher data rate |
| FSK/AFSK | Two discrete tones | ~3 kHz | APRS, AX.25 audio |
| MSK | Rounded spectrum | ≈ symbol rate | Higher efficiency than FSK |
| GFSK | Gaussian-shaped | Compact | Weather satellites |

### Step 3: Suggest GNURadio Flowgraph
For AX.25 / APRS reception:
```
RTL-SDR Source (437.5 MHz, 2.4 Msps)
    → Frequency XLAT Filter (center on signal, decimate to 48 ksps)
    → NBFM Demodulate
    → Low-pass Filter (3 kHz)
    → AFSK1200 Decoder (DIREWOLF via audio)
    → AX.25 Frame Output
```

For BPSK satellite:
```
RTL-SDR Source (freq, samp_rate)
    → Frequency XLAT Filter (decimate, shift to baseband)
    → Root Raised Cosine Filter (matched filter)
    → Costas Loop (carrier recovery)
    → Symbol Sync Block (clock recovery)
    → Differential Decoder (if DBPSK)
    → Correlation and Sync
    → Protocol-specific frame decoder
```

### Step 4: Produce Tuning Guide
Specific settings for known satellites that the agent provides based on the target satellite.
