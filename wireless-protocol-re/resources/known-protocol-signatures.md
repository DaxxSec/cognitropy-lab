# Known Protocol Signatures — Quick Reference

## 315 MHz Band (US)

| Protocol | Modulation | Data Rate | Preamble | Sync | Notes |
|----------|-----------|-----------|----------|------|-------|
| Garage door (fixed code) | OOK | 1–3 kbps | Varies | None | 8–12 bit codes, easily replayed |
| Garage door (rolling code) | OOK | 2 kbps | Short pulse train | Device-specific | KeeLoq or similar rolling code |
| Car keyfob (older) | OOK | 1–2 kbps | Repeated preamble | Varies | Fixed or rolling code |
| Tire pressure (TPMS) | FSK/OOK | 4.8–19.2 kbps | Varies | Varies | Manchester encoded, CRC-8 |

## 433 MHz Band

| Protocol | Modulation | Data Rate | Preamble | Sync | Notes |
|----------|-----------|-----------|----------|------|-------|
| Oregon Scientific v2.1 | OOK Manchester | 1024 bps | 0xFF x 6 | 0xA | 32-bit, nibble-encoded |
| Oregon Scientific v3 | OOK | 1024 bps | 0xFF x 6 | 0x5 | Similar structure to v2.1 |
| Acurite 5n1 | OOK PWM | ~600 bps | 3 sync pulses | 0x01 | Weather station, CRC-8 |
| LaCrosse TX | OOK | 1.2 kbps | Varies | 0x0A | Temperature/humidity |
| Honeywell 5800 | OOK | 8 kbps | Long preamble | Device code | Security sensor |
| EV1527 | OOK | ~2 kbps | Long low pulse | 20-bit ID | Universal remote encoder |
| PT2262 | OOK | ~1 kbps | Sync pulse | 8 tri-state bits | Common remote encoder |
| Fine Offset WH2 | OOK PWM | ~1 kbps | 8x short pulses | Fixed | Weather, temp/humidity |

## 868/915 MHz Band

| Protocol | Modulation | Data Rate | Preamble | Sync | Notes |
|----------|-----------|-----------|----------|------|-------|
| LoRaWAN | CSS (Chirp) | 0.3–50 kbps | 8 upchirps | 2 downchirps | Spread factor 7–12 |
| Zigbee | DSSS O-QPSK | 250 kbps | 8 bytes 0x00 | 0xA7 | IEEE 802.15.4 |
| Z-Wave | FSK | 9.6/40/100 kbps | Preamble bytes | SOF | Home automation |
| SigFox | DBPSK | 100 bps UL | Short | Fixed | Ultra-narrowband |
| Wireless M-Bus | 2-FSK/4-FSK | 4.8–100 kbps | Varies by mode | Mode-dependent | Smart metering, EN 13757 |
| EnOcean | ASK | 125 kbps | Short | Fixed | Energy harvesting sensors |

## 2.4 GHz Band

| Protocol | Modulation | Data Rate | Preamble | Sync | Notes |
|----------|-----------|-----------|----------|------|-------|
| Bluetooth LE | GFSK | 1 Mbps | 1 byte (0xAA) | 0x8E89BED6 | 37/38/39 adv channels |
| Wi-Fi (802.11b) | DSSS | 1–11 Mbps | Long/Short | PLCP | 14 channels |
| Wi-Fi (802.11n/ac) | OFDM | Up to 600 Mbps | HT/VHT | L-STF | 20/40/80 MHz |
| Zigbee | DSSS O-QPSK | 250 kbps | 8 bytes 0x00 | 0xA7 | Channels 11–26 |
| Nordic ESB | GFSK | 1–2 Mbps | Configurable | Configurable | nRF24L01+ |
| ANT+ | GFSK | 1 Mbps | 8 bytes | Fixed | Sports/fitness sensors |

## Common Encoding Schemes
- **Manchester:** Each bit encoded as transition (0=low-high, 1=high-low or inverse)
- **PWM:** Pulse width indicates bit value (wide=1, narrow=0 or inverse)
- **NRZ:** No return to zero, direct bit mapping
- **Differential Manchester:** Transition at start of each bit period, mid-period transition encodes data
- **4b/6b:** 4 data bits encoded as 6 symbols (used in some proprietary protocols)
