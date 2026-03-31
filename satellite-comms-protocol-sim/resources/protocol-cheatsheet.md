# Satellite Protocol Quick Reference Cheatsheet

## AX.25 Frame Structure

```
FLAG | DEST(7) | SRC(7) | [REPEATERS] | CTRL(1-2) | PID(1) | INFO | FCS(2) | FLAG
 7E     7 bytes   7 bytes    0-56 bytes   1-2 bytes   1 byte  var    2 bytes   7E
```

**Address byte encoding:** Each character in callsign is shifted left 1 bit (ASCII << 1). SSID byte: bits 6-4=011, bit 5=C/H, bits 3-1=SSID(0-15), bit 0=extension(0=more addrs, 1=last).

**Control byte (UI frame):** `0x03`
**PID values:** `0xF0` = No L3, `0xCC` = IP, `0xCF` = TheNET, `0x00` = escape

**CRC:** CRC-CCITT (polynomial 0x1021, initial value 0xFFFF), computed over address+control+pid+info

---

## CCSDS TC Transfer Frame

```
Primary Header (40 bits):
[2] Version=00 | [1] Bypass | [1] Ctrl/Cmd | [6] Reserved=000000 |
[10] Spacecraft ID | [2] VCID | [8] Frame Length-1 | [8] Frame Sequence Number
```

**Spacecraft ID:** 10 bits, 0-1023
**VCID:** 2 bits (4 virtual channels)
**FSN:** 8 bits (wraps 0-255)
**Max frame size:** 1024 bytes
**FEC:** Optional CRC-CCITT (2 bytes) at end

---

## CCSDS TM Transfer Frame

```
Primary Header (48 bits):
[2] Version=00 | [10] Spacecraft ID | [3] VCID | [1] OCF flag |
[8] Master Channel Frame Count | [8] Virtual Channel Frame Count |
[16] Data Field Status
```

**Sync marker:** `1A CF FC 1D` (precedes each frame, not part of frame)
**Fixed frame length** — set per mission (typically 892 or 1115 bytes)

---

## CCSDS Space Packet

```
Primary Header (48 bits):
[3] Version=000 | [1] Type (0=TM, 1=TC) | [1] Secondary Header Flag |
[11] APID | [2] Sequence Flags | [14] Packet Sequence Count |
[16] Packet Data Length (data length - 1)
```

**APID:** 11 bits, 0x7FF = idle packet
**Sequence flags:** 11=standalone, 01=first, 00=continuation, 10=last

---

## Link Budget Quick Formulas

```
FSPL (dB) = 20·log₁₀(4π·d·f/c)
         = 20·log₁₀(d_km) + 20·log₁₀(f_MHz) + 32.4

Prx (dBW) = EIRP (dBW) - FSPL (dB) - Lother (dB) + Grx (dBi)
EIRP (dBW) = Ptx (dBW) + Gtx (dBi)

N₀ (dBW/Hz) = 10·log₁₀(k·T) = -228.6 + 10·log₁₀(T_sys)
C/N₀ (dBHz) = Prx - N₀
Eb/N₀ (dB) = C/N₀ - 10·log₁₀(Rb)
Margin (dB) = Eb/N₀_actual - Eb/N₀_required
```

**Required Eb/N0 (BER=1e-5):**
BPSK/QPSK: ~9.6 dB | 8PSK: ~13.5 dB | 16QAM: ~18.3 dB
With LDPC (DVB-S2, rate 1/2): ~1.0 dB | rate 3/4: ~3.5 dB

---

## Doppler Shift

```
Δf = -f₀ · v_radial / c

v_radial (km/s) for ISS at 550km:
  AOS: ~+7 km/s (approaching) → positive Doppler → freq appears higher
  TCA: ~0 km/s
  LOS: ~-7 km/s (receding) → negative Doppler → freq appears lower

Max Doppler at 437.5 MHz: ±10.2 kHz
Max Doppler at 2.4 GHz:   ±56 kHz
Max Doppler at 10 GHz:    ±233 kHz
```

---

## Common Satellite Frequencies (ITU Allocations)

| Band | Frequency | Common Use |
|---|---|---|
| VHF | 144–148 MHz | Amateur downlink (APRS, voice) |
| UHF | 435–438 MHz | Amateur cubesat primary |
| L-band | 1–2 GHz | GPS, Iridium, L-band weather |
| S-band | 2–4 GHz | ISS comms, cubesat science, ground stations |
| X-band | 8–12 GHz | EO satellites, military, science downlinks |
| Ku-band | 12–18 GHz | Commercial broadcasting, VSAT |
| Ka-band | 26.5–40 GHz | High-throughput LEO (Starlink) |

---

## Modulation Schemes

| Modulation | Bits/Symbol | Spectral Efficiency | Common Use |
|---|---|---|---|
| BPSK | 1 | 1 bps/Hz | CCSDS uplinks, PSK-31 |
| QPSK | 2 | 2 bps/Hz | DVB-S, CCSDS TM |
| OQPSK | 2 | 2 bps/Hz | Faster phase transitions |
| 8PSK | 3 | 3 bps/Hz | DVB-S2 high-throughput |
| GFSK | 1 | ~0.5 bps/Hz | Weather sats, IoT |
| MSK | 1 | 1 bps/Hz | GMSK used in Iridium |

---

## AX.25 Callsign Examples (Amateur Satellites)

| Satellite | Callsign | Frequency | Protocol |
|---|---|---|---|
| ISS | RS0ISS | 145.825 MHz | APRS |
| FUNCUBE-1 | AO-73 | 145.935 MHz | AX.25 |
| PSAT | NO-84 | 145.825 MHz | APRS Digi |
| LAPAN-A3 | YB0AO | 145.825 MHz | APRS |
