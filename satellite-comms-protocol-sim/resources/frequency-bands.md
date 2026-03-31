# Satellite Frequency Band Reference

## ITU Frequency Bands for Satellite Services

### VHF (30–300 MHz)
- **Amateur satellite:** 144–146 MHz (APRS downlinks, ISS)
- **NOAA APT/HRPT:** 137–138 MHz
- **Meteor-M2 LRPT:** 137.1 MHz
- **Receiver:** RTL-SDR with dipole, easily received
- **Path loss at 50 km altitude, 90° elevation (MHz):** ~112 dB

### UHF (300 MHz–3 GHz)
- **Amateur cubesat primary:** 435–438 MHz
- **Amateur cubesat secondary:** 145.8–146 MHz
- **NOAA HRPT downlink:** ~1700 MHz (L-band)
- **GPS L1:** 1575.42 MHz
- **GPS L2:** 1227.6 MHz
- **Iridium:** 1616–1626.5 MHz
- **Inmarsat L-band:** 1525–1660.5 MHz
- **Receiver:** RTL-SDR (up to 1.7 GHz), HackRF (to 6 GHz)

### S-Band (2–4 GHz)
- **NASA/ESA ground station uplinks:** 2.025–2.12 GHz
- **Satellite TT&C (telemetry, tracking, command):** 2.2–2.29 GHz
- **ISS S-band:** 2.216 GHz (video), 2.287 GHz (data)
- **Cubesat science downlinks:** 2.2–2.4 GHz (higher rate)
- **Receiver:** HackRF, USRP, dedicated dish required

### X-Band (8–12 GHz)
- **Earth Observation downlinks:** 8025–8500 MHz
- **NOAA HRPT alternate:** 8345 MHz
- **Military/government:** 7.25–7.75 GHz (space-Earth), 7.9–8.4 GHz (Earth-space)
- **Receiver:** Dish antenna + X-band LNA + HackRF or SDRplay
- **Challenge:** Higher path loss, requires larger antennas

### Ku-Band (12–18 GHz)
- **FSS (Fixed Satellite Service):** 10.7–12.75 GHz (downlink), 14–14.5 GHz (uplink)
- **DBS broadcasting:** 11.7–12.5 GHz
- **VSAT:** Two-way broadband
- **Typical dish size:** 60–120 cm for GEO

### Ka-Band (26.5–40 GHz)
- **High-throughput LEO:** 26.5–40 GHz
- **Starlink:** 10.7–12.7 GHz (Ku), 37.5–42.5 GHz (Ka) downlink
- **Rain fade sensitive** — significant attenuation in precipitation
- **Requires precision pointing** — very narrow beamwidth

---

## Amateur Satellite Frequency Allocations

| Region | UHF Uplink | UHF Downlink | Notes |
|---|---|---|---|
| Primary | 435–438 MHz | 435–438 MHz | Cross-band common |
| Secondary | 145.8–146 MHz | 145.8–146 MHz | APRS/voice |
| S-band (licensed) | 2.4–2.45 GHz | 2.4–2.45 GHz | Science missions |

**Key regulatory requirement:** Must accept interference from primary services in shared allocations.

---

## Path Loss at Common Satellite Frequencies

At 550 km altitude, 90° elevation (minimum path loss):
| Frequency | FSPL |
|---|---|
| 137 MHz (NOAA) | ~113 dB |
| 437 MHz (amateur) | ~126 dB |
| 1575 MHz (GPS L1) | ~138 dB |
| 2.2 GHz (S-band) | ~142 dB |
| 8.1 GHz (X-band) | ~154 dB |

At 550 km altitude, 10° elevation (maximum path loss from geometry):
Add ~7-10 dB to all values above.

---

## SDR Hardware Coverage

| Hardware | Frequency Range | RX/TX | Notes |
|---|---|---|---|
| RTL-SDR (RTL2832U) | 24 MHz – 1.766 GHz | RX only | $25, ideal starter |
| Airspy Mini | 24 – 1800 MHz | RX only | Higher dynamic range |
| HackRF One | 1 MHz – 6 GHz | RX + TX | Amateur-licensed TX |
| USRP B200 | 70 MHz – 6 GHz | RX + TX | Professional grade |
| LimeSDR Mini | 10 MHz – 3.5 GHz | RX + TX | Good price/performance |
| SDRplay RSP1A | 1 kHz – 2 GHz | RX only | Good sensitivity |

**For satellites:**
- NOAA/Meteor/weather: RTL-SDR sufficient
- Amateur cubesats (UHF): RTL-SDR sufficient
- S-band/X-band: HackRF + dish + LNA required
- Transmitting: HackRF with valid amateur license
