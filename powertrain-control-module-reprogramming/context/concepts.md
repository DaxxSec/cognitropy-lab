# Powertrain Control Module Reprogramming — Core Concepts

Background the agent should read before acting. Optimised for fast recall. The framing throughout is **conservation**: the factory calibration is an irreplaceable *specimen*, and every operation either preserves, fits, maps, or restores it.

## Module taxonomy — what you are reprogramming

| Module | Controls | Common names |
|---|---|---|
| **PCM** | Engine **and** transmission together | Powertrain Control Module |
| **ECM / ECU** | Engine only | Engine Control Module / Unit |
| **TCM** | Transmission only | Transmission Control Module |
| **EMS** | Engine management (Euro term) | Engine Management System |
| **BCM / SGW** | Body / Security Gateway (gates access) | Body Control Module / Security Gateway |

A "PCM" on a GM truck and an "ECM" on a Euro diesel do the same job: run real-time control loops from sensor inputs against **calibration tables** stored in non-volatile flash.

## Anatomy of a module image (the "specimen")

A read image typically contains, in distinct flash regions:

- **Bootloader** — tiny, write-protected loader that brings the module up and handles recovery flashing. Corrupting this is what truly *bricks* a module (vs. a recoverable bad cal).
- **Operating system / strategy** — the executable control code (Ford "strategy," GM "OS," Bosch software number). Rarely changed in tuning; changes here demand exact hardware match.
- **Calibration region** — the editable parameter set: **tables/maps** (2-D/3-D: fuel, spark/ignition advance, boost target/limit, VVT/cam phasing, torque management, transmission shift schedules & line pressure, EGR, fan/thermal), **scalars** (rev limit, fuel cut, fan-on temp), and **switches/flags** (feature enable, monitor enable). This is the "skin" a calibrator works on.
- **VIN / options / immobilizer** region — vehicle-specific identity; mismatches here cause no-start / immobilizer faults.
- **Checksum / CVN region** — integrity values the bootloader/OS validate before accepting or running the cal.

## Identifiers (the specimen's provenance)

- **VIN** (ISO 3779) — 17 chars; WMI (1–3), VDS (4–9), VIS (10–17). Decodes make/model/plant/**market**.
- **CAL-ID** (Calibration Identification) — OBD-II **Mode 09 PID 04**; the calibration's part-number-like ID.
- **CVN** (Calibration Verification Number) — **Mode 09 PID 06**; a hash/checksum the OEM uses to prove the cal is unaltered. A changed cal **must** have a recomputed, valid CVN/checksum or it is rejected (or flagged as tampered).
- **Strategy / OS code** — Ford strategy (e.g. `K2…`), GM OS + cal segment part numbers, Bosch `MED/EDC` software number.
- **ECU HW/SW numbers** — printed on the module label and reported over UDS (e.g. ISO 14229 DID `F18C`/`F195`).

## Access & programming protocols

- **Physical:** OBD-II **J1962** 16-pin connector; CAN bus (ISO 11898). Bench access via module connector, or **boot mode / BDM / JTAG** for recovery and locked modules.
- **Transport:** **ISO 15765-2** (DoCAN / ISO-TP) carries diagnostics over CAN.
- **Diagnostic/programming services:** **UDS — ISO 14229** (`DiagnosticSessionControl 0x10`, `SecurityAccess 0x27` seed/key, `RequestDownload 0x34`, `TransferData 0x36`, `RequestTransferExit 0x37`, `RoutineControl 0x31` for erase/checksum), and legacy **KWP2000 (ISO 14230)**.
- **Pass-thru:** **SAE J2534** — the standardized PC↔VCI API that U.S. law requires OEMs to support for emissions-related reprogramming. The OEM app drives the flash; the J2534 device is the bridge.
- **Security gateways:** Newer vehicles (e.g. FCA **SGW**) require authenticated access (NASTF/AutoAuth) before the PCM will accept writes — legitimate access only.

## The conservation taxonomy (taxidermy → calibration)

The discipline of preserving a biological specimen maps cleanly onto preserving a calibration:

| Taxidermy concept | Calibration analogue |
|---|---|
| **Specimen** | The factory calibration as it left the OEM |
| **Study skin / archived mount** | The read-and-hashed stock image in `outputs/specimens/` |
| **The form** (mannikin fitted to the animal's anatomy) | The vehicle's **hardware configuration** — injector flow, turbo, MAF/MAP range, trans model — that a cal must fit |
| **Mounting** | Writing a cal that is correctly fitted to that form |
| **Reference collection** | The library of known-good cals by model/year/market |
| **Provenance / accession record** | VIN, CAL-ID, CVN, market, reflash log |
| **Restoration of a damaged mount** | Un-bricking / recovering a corrupt module from the archive |
| **Reversibility** | The ability to re-flash the original specimen at any time |

The single rule that falls out of this framing: **never alter a specimen you have not first preserved.** Archive-first is to calibration what documenting-before-skinning is to taxidermy.

## The geographic / spatial dimension (today's technique)

A calibration is regional. The *same* engine ships with materially different cals depending on **where it operates**:

- **Emissions regime** — EPA Tier 3 / CARB LEV III (US), Euro 6d/7 (EU/UK), China 6, Bharat Stage VI (India), each with different OBD monitor sets, EGR/SCR strategy, and readiness logic.
- **Fuel grade** — 87 AKI regular vs 91–93 premium (US) vs 95/98 RON (EU) vs E85-flex; spark and knock strategy differ.
- **Altitude / barometric** — high-altitude variants change fueling, spark, boost limit, and thermal/fan behaviour vs. sea-level cals (BARO compensation maps).
- **Climate** — cold-region cold-start enrichment, block-heater logic, thermal management.
- **Market feature flags** — left/right-hand drive, regional speed limiters, telematics/regulatory features.

So `/region-cal-map` treats cal selection as a **spatial query**: given a vehicle's operating geography (jurisdiction, elevation band, fuel availability), which cal variant is correct *and legal*? A "gray-market" mismatch (a Euro ECU on a US car) is a spatial error that surfaces as failed readiness monitors, CELs, or derate.

## Common Failure Modes

- **Bricked by under-voltage** — battery sagged below ~12.2 V mid-flash; bootloader or OS partially written → no comms. Recoverable only if the specimen was archived. The #1 preventable disaster.
- **No stock backup** — calibrator edited live without an intake read; the only factory copy is now gone. The cardinal sin.
- **Wrong form** — a cal meant for different injectors/turbo/trans is mounted; symptoms are persistent lean/rich codes, mis-shifts, phantom faults chased for days.
- **Checksum/CVN mismatch** — edited cal not re-sealed; module rejects the flash or runs in a fault/limp mode and flags tamper.
- **Region mismatch** — wrong-market cal; OBD readiness never completes, or monitors throw, or emissions controls behave wrong for the local fuel/altitude.
- **Security-gateway lockout** — attempting to write through an SGW without authenticated access; write rejected (and unauthorized bypass is illegal).
- **VIN/immobilizer mismatch** — replacement module not married to the vehicle → no-start.

## Operating Constraints

- **Clean Air Act §203(a)(3)** (US) prohibits tampering with emissions controls and the manufacture/sale of defeat devices; **CARB** enforces in CA; **EU Reg. 715/2007 + UNECE**, UK, and others equivalent. Emissions-defeat cals for road vehicles are out of scope — `/emissions-legality-gate` enforces this.
- **Legitimate lanes:** OEM/TSB recalibration, replacement-module programming, bricked-module restoration, diagnostics, and dedicated off-road/motorsport/closed-course/bench-research.
- **Power & timing are physical constraints:** a flash needs a stable 13.0–13.5 V supply and an uninterrupted session; treat both as hard preconditions.
- **Access must be licensed:** NASTF SDRM, OEM reprogramming subscriptions, AutoAuth for gateways — not stolen algorithms.
