# Domain Knowledge

This document gives the agent deep domain knowledge about satellite communication protocols, RF link physics, and related security considerations.

---

## Satellite Orbital Regimes

### Low Earth Orbit (LEO)
- Altitude: 160–2,000 km (typical cubesats: 400–600 km)
- Orbital period: ~90–120 minutes
- Pass duration from ground: 5–15 minutes (varies with elevation)
- Path loss: ~130–145 dB at 437 MHz
- Doppler shift: up to ±10 kHz at VHF/UHF per pass
- Key advantage: Lower path loss, lower latency
- Key challenge: Short contact windows, high Doppler rate

### Medium Earth Orbit (MEO)
- Altitude: 2,000–35,786 km
- Examples: GPS/GNSS constellations (20,200 km)
- Orbital period: ~2–24 hours
- Path loss: ~155–165 dB at GPS L1 (1.57542 GHz)
- Longer visibility windows than LEO

### Geostationary Orbit (GEO)
- Altitude: 35,786 km (Clarke orbit)
- Fixed position relative to Earth surface
- Path loss: ~196 dB at Ku-band (12 GHz)
- Latency: ~240 ms one-way
- No Doppler (for stationary observers)
- Examples: Weather satellites, broadcasting satellites

### Highly Elliptical Orbit (HEO)
- Examples: Molniya orbit (apogee ~40,000 km, perigee ~1,000 km)
- Provides long dwell time over high-latitude regions
- Significant Doppler variation during orbit

---

## Protocol Stack Overview

### Layer Model for Satellite Communications
```
Application Layer    (Telemetry/Telecommand data, mission payloads)
         |
Protocol Layer       (CCSDS Space Packet, AX.25 UI/connected)
         |
Framing Layer        (CCSDS TM/TC Transfer Frames, HDLC frames)
         |
Data Link Layer      (Synchronization, coding, ARQ)
         |
Physical Layer       (Modulation, FEC coding, RF)
```

---

## AX.25 Protocol

AX.25 is the standard data-link layer protocol used by amateur radio satellite operators. Based on HDLC, designed for packet radio.

### Frame Types
- **UI (Unnumbered Information)** — Most common for amateur satellites, no acknowledgment
- **I-frame (Information)** — Connected mode, reliable delivery with sequence numbers
- **S-frame (Supervisory)** — RR (Ready Receive), RNR (Receive Not Ready), REJ (Reject)
- **U-frame (Unnumbered)** — SABM (connect), DISC (disconnect), DM, UA, FRMR

### Address Field Format
Each address field is 7 bytes: 6 bytes callsign (ASCII left-shifted by 1 bit) + 1 byte SSID/flags.

SSID byte:
- Bits 7-5: Always 011 for compliance
- Bit 4: C/H bit (Command/Response or Has-been-repeated)
- Bits 3-1: SSID (0-15)
- Bit 0: Extension bit (0 = more addresses follow, 1 = last address)

### APRS (Automatic Position Reporting System)
APRS is an application-layer protocol that runs over AX.25. Common on amateur satellites.
- Position: `!DDMM.mmN/DDDMM.mmW>`
- Status: `>status text`
- Object: `;<name>    *DDHHMMzDDMM.mmN/DDDMM.mmW>`

Popular APRS-capable satellites: ARISS/ISS (145.825 MHz downlink), PSAT, LAPAN-A3

---

## CCSDS (Consultative Committee for Space Data Systems)

CCSDS defines the de facto standard protocols for spacecraft commanding and telemetry. Used by NASA, ESA, JAXA, and most cubesat operators following professional standards.

### Key Standards
- **CCSDS 131.0-B-5** — TM Synchronization and Channel Coding
- **CCSDS 132.0-B-3** — TM Space Data Link Protocol (TM Transfer Frames)
- **CCSDS 231.0-B-4** — TC Synchronization and Channel Coding
- **CCSDS 232.0-B-4** — TC Space Data Link Protocol (TC Transfer Frames)
- **CCSDS 133.0-B-2** — Space Packet Protocol
- **CCSDS 352.0-B-2** — Space Data Link Security Protocol

### TM Transfer Frame (Telemetry, downlink)
- Sync marker: `1ACFFC1D` (hex) — always present before each frame
- Frame length: Fixed per mission (typically 892 or 1115 bytes for standard missions)
- Contains: Primary header (6 bytes), secondary header (optional), data, optional error control

### TC Transfer Frame (Telecommand, uplink)
- Frame length: Variable, max 1024 bytes
- Includes: Spacecraft ID, Virtual Channel ID, Frame Sequence Number
- FEC: Optional CRC-CCITT (2 bytes)
- Security: Optional encryption/authentication via CCSDS 352

### Space Packet
Higher-level packet format carried inside transfer frames:
- Primary header: 6 bytes (version, type, APID, sequence flags, length)
- APID (Application Process Identifier): 11 bits, identifies the destination application on the spacecraft
- Secondary header: Optional (timestamps, etc.)
- Data: Variable up to 65536 bytes

---

## DVB-S2 (Digital Video Broadcasting — Satellite Second Generation)

DVB-S2 is used by commercial satellite broadcasting and increasingly by high-throughput cubesat downlinks.

- Standard: ETSI EN 302 307-1 (base), EN 302 307-2 (DVB-S2X extensions)
- Modulations: QPSK, 8PSK, 16APSK, 32APSK (S2X adds 64APSK, 128APSK)
- FEC: LDPC + BCH (very powerful, operates near Shannon limit)
- Frame structure: BBFRAME → FECFRAME → PLFRAME
- Roll-off factors: 0.35, 0.25, 0.20 (S2X adds 0.15, 0.10, 0.05)
- Adaptive Coding and Modulation (ACM): adjusts modcod based on link conditions

---

## APRS / Weather Satellites

### NOAA APT (Automatic Picture Transmission)
- Frequency: 137.1 MHz (NOAA-18), 137.9125 MHz (NOAA-19)
- Modulation: FM, 2400 Hz subcarrier, AM image signal
- Line rate: 4 lines/second
- Resolution: ~4 km/pixel
- Receivable with simple V-dipole antenna and RTL-SDR

### NOAA HRPT (High-Resolution Picture Transmission)
- Frequency: ~1700 MHz (L-band)
- Modulation: BPSK at 665.4 ksps
- Requires dish or high-gain antenna + HackRF or USRP

### Meteor-M LRPT
- Frequency: 137.1 MHz
- Modulation: OQPSK at 72 ksps
- Color imagery, higher resolution than APT
- Decodable with RTL-SDR using SatDump

---

## Iridium SBD (Short Burst Data)

Iridium is a LEO satellite phone constellation (66 satellites).

- SBD (Short Burst Data): Small data packets (up to 340 bytes MO, 270 bytes MT)
- Uses Iridium's proprietary L-band (1616–1626.5 MHz) air interface
- Iridium NEXT downlink signals visible with HackRF at ~1626 MHz
- Protocol: Proprietary at air interface, AT commands for modem control
- Common uses: Asset tracking, remote environmental monitoring, maritime AIS

### Iridium Security Note
The original Iridium constellation had no link layer encryption. Researchers demonstrated eavesdropping on Iridium voice/data (2009, Security Researchers Dedected Iridium). NEXT constellation improved this but specifics are not fully public.

---

## AIS (Automatic Identification System)

AIS is used by ships; AIS signals are also received from satellite (S-AIS).

- VHF channels 87B (161.975 MHz) and 88B (162.025 MHz)
- Modulation: GMSK at 9600 bps
- Frame: HDLC-based, NMEA-like content
- Satellite AIS (S-AIS): Received from LEO satellites (EXACT EARTH, SpireGlobal)
- Receivable with RTL-SDR using gr-ais GNURadio module or AIS-catcher

### AIS Frame Structure
```
Flag: 0x7E
MMSI: 9 digits (Maritime Mobile Service Identity)
Position: Lat/Lon in 1/10000 minute
Speed/Course: Over ground
Status: Underway, anchored, not under command, etc.
CRC: CRC-CCITT
Flag: 0x7E
```

---

## Forward Error Correction Schemes

| Code | Application | Coding Gain | Complexity |
|---|---|---|---|
| Reed-Solomon (255,223) | CCSDS legacy TM | ~6 dB | Low |
| Convolutional (r=1/2, k=7) | CCSDS legacy TM, LEO | ~5 dB | Low |
| Concatenated RS+Conv | CCSDS traditional | ~8 dB | Medium |
| LDPC (DVB-S2) | DVB-S2, modern | ~10-11 dB | High |
| Turbo Codes | CCSDS deep space | ~9.5 dB | Very High |
| BCH | DVB-S2 outer code | ~1 dB additional | Medium |

---

## Satellite Security: Key Concepts

### Attack Surfaces
1. **Ground-to-space uplink** — Command injection if unprotected
2. **Space-to-ground downlink** — Eavesdropping if unencrypted
3. **Ground station software** — Traditional software vulnerabilities
4. **Inter-satellite links (ISL)** — Increasingly relevant for LEO constellations
5. **Supply chain** — Component compromise before launch

### Notable Incidents
- **Viasat KA-SAT hack (2022)** — Threat actor wiped modems using management interface vulnerability; affected wind turbines, Ukrainian military
- **Iridium Eavesdropping (2009)** — Security researchers showed L-band Iridium voice interception was possible with ~$1000 in equipment
- **ROSAT (1998)** — Hacker reportedly gained control of ground station pointing; spacecraft pointing toward Sun damaged sensors
- **Galaxy 15 (2010)** — Satellite stopped responding to commands, drifted through GEO arc interfering with other satellites

### CCSDS Security Layer (CCSDS 352.0-B-2)
Provides optional security services for TM/TC transfer frames:
- Authentication only
- Encryption only
- Encryption + Authentication
- Uses AES-256-GCM by default
- Sequence number anti-replay protection
- Key management is external (not defined by CCSDS)
