# Powertrain Control Module Reprogramming — Reference Tables

Compact lookup data. Defer to the linked upstream sources for full specs.

## Protocols & standards

| Standard | Layer | What it covers |
|---|---|---|
| SAE J1962 | Physical | OBD-II 16-pin connector |
| ISO 11898 | Physical/Link | CAN bus |
| ISO 15765-2 | Transport | Diagnostics over CAN (ISO-TP / DoCAN) |
| ISO 14229 (UDS) | Application | Diagnostic & programming services (incl. SecurityAccess, RequestDownload) |
| ISO 14230 (KWP2000) | Application | Legacy keyword-protocol services |
| SAE J1979 / ISO 15031-5 | Application | OBD-II modes (Mode 09 CAL-ID/CVN, Mode 01 readiness) |
| SAE J2534-1/-2 | API | PC↔VCI pass-thru programming interface |

## Key UDS services (ISO 14229) used in a flash

| SID | Service | Role in reprogramming |
|---|---|---|
| 0x10 | DiagnosticSessionControl | Enter programming session |
| 0x27 | SecurityAccess | Seed/key unlock (licensed) |
| 0x34 | RequestDownload | Begin transfer of new data to module |
| 0x36 | TransferData | Stream the cal/OS blocks |
| 0x37 | RequestTransferExit | End transfer |
| 0x31 | RoutineControl | Erase memory, checksum/verify routines |
| 0x11 | ECUReset | Reset into the new image |

## Identifier glossary

| ID | Source | Meaning |
|---|---|---|
| VIN | Mode 09 PID 02 / label | 17-char vehicle identity (ISO 3779); decodes market |
| CAL-ID | Mode 09 PID 04 | Calibration identification (part-number-like) |
| CVN | Mode 09 PID 06 | Calibration Verification Number (integrity hash) |
| Strategy / OS | OEM (Ford/GM) | Executable control-code identifier |
| ECU HW/SW # | UDS DID F18C/F195 etc. | Hardware & software part numbers |

## Emissions regime → region map (for `/region-cal-map`)

| Regime | Region | Notes for cal selection |
|---|---|---|
| EPA Tier 3 | USA (federal) | Federal certification; 87+ AKI typical |
| CARB LEV III | California (+ §177 states) | Stricter; EO required for aftermarket parts |
| Euro 6d / Euro 7 | EU / UK | RDE testing; 95/98 RON; different OBD monitors |
| China 6a/6b | China | Among strictest; distinct OBD logic |
| Bharat Stage VI | India | 2020+; distinct fuel & monitor set |
| (Off-road) | n/a | Not road-certified; bench/motorsport/closed-course only |

## Fuel grade quick reference

| Market term | Approx. octane | Notes |
|---|---|---|
| Regular (US) | 87 AKI (~91 RON) | (R+M)/2 method |
| Premium (US) | 91–93 AKI | High-altitude US regular can be 85–86 AKI |
| Euro 95 | 95 RON | Baseline EU |
| Euro 98 / Super | 98 RON | Premium EU |
| E85 | flex | Requires flex-fuel calibration |

> AKI ≈ RON − ~4–5. Spark/knock tables assume a specific grade — geography changes the grade.

## Altitude / BARO bands (for `/altitude-compensation`)

| Band | Elevation | Approx. ambient pressure | Cal concern |
|---|---|---|---|
| Sea level | 0–500 m | ~101 kPa | Baseline |
| Moderate | 500–1,500 m | ~85–95 kPa | Mild enrichment/spark trim |
| High | 1,500–2,500 m | ~75–85 kPa | High-altitude variant often warranted |
| Very high | 2,500–3,500 m+ | <75 kPa | Boost limit, thermal, derate behaviour critical |

## Common tooling (reference, not endorsement)

- **J2534 VCIs:** OEM-spec pass-thru devices (various vendors) for emissions-legal reprogramming.
- **OEM apps:** Ford FDRS, GM SPS2/ACDelco TDS, Mopar wiTECH, etc. (subscription).
- **Calibration/editor tooling + definitions:** platform-specific (XDF/DAMOS/A2L definitions make tables human-readable).
- **Checksum/CVN:** tool-integrated or platform-specific correction routines.

## Upstream Catalogues

- **NASTF Vehicle Security / SDRM** — https://wp.nastf.org/ — legitimate OEM reprogramming & security access.
- **NHTSA vPIC VIN decoder API** — https://vpic.nhtsa.dot.gov/api/ — VIN → make/model/plant/market.
- **EPA air enforcement (tampering/defeat devices)** — https://www.epa.gov/enforcement/air-enforcement
- **CARB aftermarket parts / Executive Order search** — https://ww2.arb.ca.gov/our-work/programs/aftermarket-performance-parts
- **SAE J2534 standard** — https://www.sae.org/standards/content/j2534/1_201712/
- **ISO 14229 (UDS)** — https://www.iso.org/standard/72439.html

## Operating Cheat-Sheet

- Stable supply **13.0–13.5 V** before any read or flash; abort under ~12.5 V.
- **Archive first** (Mode 09 IDs + full read + hash) — no exceptions.
- A changed cal **must** be re-sealed (checksum/CVN) or it is rejected.
- Wrong-market cal → readiness monitors won't complete; fix the cal, don't mask the codes.
- Security-gateway vehicles need authenticated access (NASTF/AutoAuth) — licensed only.
