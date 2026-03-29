# TPMS Frequency and Protocol Reference

## Regional Frequency Standards

| Region | Primary Frequency | Secondary | Regulation |
|---|---|---|---|
| North America (US/Canada) | 315 MHz | — | FCC Part 15.249 |
| Europe | 433.92 MHz | 434.15 MHz (some) | ETSI EN 300 220 |
| Japan | 315 MHz | 433.92 MHz (imports) | ARIB STD-T93 |
| Australia/NZ | 433.92 MHz | — | ACMA |
| China | 433.92 MHz | 315 MHz (older) | MIIT |
| South Korea | 433.92 MHz | — | KCC |

**Note:** Many premium/aftermarket sensors support both 315 and 433.92 MHz. When traveling, the vehicle typically does not switch — you need the domestic-market sensors for reliable ECU matching.

---

## Major OEM Supplier Mapping

| Manufacturer | Common OEM Customers | Primary Protocol | Freq |
|---|---|---|---|
| Schrader Electronics | GM, Ford, Chrysler, Jeep, Toyota (NA) | EG53MA4, various | 315 |
| Continental VDO | VW, Audi, BMW, Mercedes, Porsche | Continental RDKS | 433.92 |
| Huf Electronics | VAG Group, Bentley, Lamborghini | Huf RDKS | 433.92 |
| Pacific Industries | Toyota, Honda, Subaru (JDM) | Pacific-Industries | 315 |
| Sensata (Schrader BERU) | Ford (EU), Alfa Romeo, Fiat | Sensata | 433.92 |
| Lear Corporation | Ford (US), Lincoln | Lear-TPMS | 315 |
| Denso | Toyota, Lexus (global) | Denso-TPMS | 315/433 |
| Nira Dynamics (iTPMS) | Volvo, BMW | Indirect (no RF) | N/A |

---

## rtl_433 Supported Devices (TPMS)

Selected protocols supported as of rtl_433 v21+:

| Device ID | Name | Notes |
|---|---|---|
| 59 | Schrader-EG53MA4 | Most common NA sensor |
| 60 | Schrader-SMD3MA4 | Older Schrader |
| 61 | Schrader-DD | Direct TPMS variant |
| 74 | PMV-107J | Subaru/JDM Pacific Industries |
| 79 | Jansite-TPMS | Aftermarket OBD type |
| 85 | Toyota-TPMS | Toyota NA specific |
| 150 | Abarth-124Spider | Continental protocol variant |
| 166 | Michelin-TPMS | Michelin tire-embedded |
| 168 | Atsumi-TPMS | Honda/Acura NA |
| 186 | Schrader-4B | Cadillac, Buick variant |

Run `rtl_433 -R help` for the complete current list.

---

## Transmission Characteristics

| Parameter | Typical Value |
|---|---|
| Transmission interval (motion) | 60–90 seconds |
| Transmission interval (static LF trigger) | Immediate |
| Packets per transmission | 3–6 repeats |
| Packet duration | 10–50 ms |
| Activation speed threshold | ~7–15 km/h |
| Range (passive capture) | 5–40 m (omni antenna) |
| Range (directional capture) | 100+ m (Yagi, research) |

---

## Pressure Encoding Quick Reference

| Raw byte value | 1/4 kPa scale | kPa direct | 1 PSI scale |
|---|---|---|---|
| 0x80 (128) | 32.0 kPa | 128 kPa (18.6 PSI) | 128 PSI |
| 0xB4 (180) | 45.0 kPa | 180 kPa (26.1 PSI) | 180 PSI |
| 0xC8 (200) | 50.0 kPa | 200 kPa (29.0 PSI) | 200 PSI |
| 0xE0 (224) | 56.0 kPa | 224 kPa (32.5 PSI) | 224 PSI |

**Car tire typical range:** 28–36 PSI (193–248 kPa). Use this to sanity-check your conversion formula.
