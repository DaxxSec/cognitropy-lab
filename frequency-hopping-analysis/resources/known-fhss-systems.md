# Reference — Known FHSS Systems

Quick-reference catalogue of common hopping systems, their parameters, and analysis notes. Used by `/hop-set-prior --system` and during prior elicitation.

## Civilian / Commercial

### Bluetooth Classic (BR/EDR)
- Band: 2.4 GHz ISM (2402–2480 MHz)
- K: 79 channels at 1 MHz spacing
- Hop rate: 1600 hops/s (1600 hops in connection state, 3200 hops/s in inquiry/page substates)
- Dwell: 625 µs (no guard)
- Modulation: GFSK (BR), π/4-DQPSK + 8-DPSK (EDR)
- Sequence: deterministic given LAP (Lower Address Part, 24 bits) and CLK (28-bit master clock); Bluetooth Core Spec § 2.6 Vol 2 Part B
- Recovery: LAP recoverable from any 32+ consecutive observed hops (gr-bluetooth, ubertooth)
- Authoritative reference: Bluetooth Core Spec 5.4

### Bluetooth Low Energy (BLE) data
- Band: 2.4 GHz ISM
- K: 37 data channels (channels 0–36 in BLE numbering) + 3 advertisement channels (37, 38, 39)
- Channel mapping: data channel index → freq = 2402 + 2*(channel_index) MHz, with the three advertisement channels at 2402 (37), 2426 (38), 2480 (39)
- Hop rate: per connection event, ranging from 1 hop / 7.5 ms to 1 hop / 4 s
- Sequence: `c_{n+1} = (c_n + hopIncrement) mod 37`, hopIncrement ∈ {5, 6, ..., 16}; AFH overlay blacklists noisy channels
- Recovery: hopIncrement is one of 12 values; brute-force trivial. Channel-map blacklist requires longer observation.

### Wireless M-Bus (WMBus) Mode N
- Band: 169.4–169.5 MHz (EU)
- K: 8 channels at 12.5 kHz spacing starting at 169.40625 MHz
- Hop rate: ~30 hops/s
- Dwell: ~33 ms
- Sequence: table-driven, periodic, public spec (EN 13757-4)

### LoRa Channel Hopping (US 902–928)
- Band: 902–928 MHz US ISM
- K: up to 64 uplink channels at 200 kHz spacing
- Hop rate: ~1 hop / 400 ms (very slow)
- Sequence: region-defined, specified in LoRaWAN Regional Parameters
- Note: often misclassified as fixed-frequency because the hop rate is so slow.

### Honeywell Wireless Fire Panels (433/868 MHz)
- Various proprietary protocols. Usually 10–20 channels, ~10 hops/s, weakly random sequences.
- Public RE work exists on rtl_433 and various conference talks.

### MBT (Multi-Band Trunking, public-safety in some jurisdictions)
- Out of scope without explicit authorisation. Receiving public-safety encrypted comms is illegal in many jurisdictions.

## Industrial / Mil

### SINCGARS (US Army VHF)
- Band: 30–88 MHz
- K: 2320 channels at 25 kHz spacing
- Hop rate: ~100 hops/s
- Dwell: 10 ms
- Sequence: cryptographic
- **Out of scope without DOD authorisation.** Reception of mil tactical traffic is restricted; this workspace will not analyse it without proof of authorisation.

### Have Quick (USAF UHF anti-jam voice)
- Band: 225–400 MHz UHF
- K: hundreds of channels
- Hop rate: ~100 hops/s
- Sequence: cryptographic
- **Out of scope without USAF authorisation.**

### Civilian Aviation TCAS / ADS-B
- Not FHSS. ADS-B is fixed at 1090 MHz; TCAS uses 1030/1090 MHz fixed.
- Listed here so the agent doesn't misclassify them.

## Toys / Hobby

### Hobby R/C 2.4 GHz (DSM2, DSMX, FrSky, Spektrum, FlySky, etc.)
- Band: 2.4 GHz ISM
- K: typically 23 (DSM2), 23 (DSMX), or up to 80 (FrSky-V8)
- Hop rate: 100–500 hops/s depending on protocol
- Dwell: 2–10 ms
- Sequence: protocol-specific; DSMX uses a pseudo-random sequence seeded by the bound transmitter ID
- Public RE: deviation-tx project, multiprotocol-tx-module project

## Out-of-Scope Defaults

By default the agent declines to analyse:

- Cellular (LTE, 5G NR) — not FHSS, but listed to prevent confusion
- Public-safety encrypted (P25 with DES/AES) — Wiretap Act protected
- Mil tactical (SINCGARS, Have Quick, Link 16) — without explicit authorisation
- GMR / Iridium / Inmarsat satellite voice — Wiretap Act protected

## Reference Hop-Rate Histogram

For prior elicitation, a histogram of hop rates across known systems:

```
~1 hops/s   :  GMR-1 (sat phone)
~30 hops/s  :  WMBus mode N
~100 hops/s :  SINCGARS, Have Quick, hobby R/C
~500 hops/s :  Some FrSky variants
1600 hops/s :  Bluetooth Classic (connection)
3200 hops/s :  Bluetooth Classic (inquiry/page)
```

Most civil FHSS systems sit in the 30–3200 hops/s window. Anything outside that should trigger extra scrutiny.
