# Powertrain Control Module Reprogramming — Workflows and Methodology

How the conservator actually works. `concepts.md` says *what things are*; this file says *what you do*. Everything is organised around the conservation lifecycle, with today's **geographic/spatial analysis** technique driving calibration selection.

## The conservation lifecycle (the spine)

```
INTAKE ──► PROVENANCE ──► FORM-FIT ──► SPATIAL CAL SELECTION ──► SEAL ──► FLASH ──► VERIFY
  │            │             │                  │                  │        │         │
  └─ archive   └─ VIN/CAL-ID └─ HW part match   └─ region+altitude └─ CVN   └─ rollback└─ readiness
     specimen     /market       (the "form")       (legal cal)       ckm       ready      monitors
                                                                                  │
                                              (on failure at any write) ──► RESTORATION ◄┘
```

Never skip INTAKE. Never reach FLASH without SEAL and a passing legality gate. RESTORATION is always armed because the specimen exists.

## Workflow 1: Specimen intake & archival (read-before-write)

**Goal:** Preserve an exact, verifiable copy of the factory calibration before any change.

### Steps
1. Confirm a **stable power supply** (13.0–13.5 V maintainer) and a known-good interface; abort if voltage is marginal.
2. Establish comms; record **VIN, CAL-ID (Mode 09/04), CVN (Mode 09/06)**, and ECU HW/SW numbers.
3. **Full read** the module (all flash regions if the tool allows; at minimum the calibration region).
4. Compute a **hash** (e.g. SHA-256) of the image; write image + hash + identifiers to `outputs/specimens/<vin-or-serial>-<date>/`.
5. Verify the archive: re-hash the saved file; confirm it matches. Only now is the specimen "accessioned."

### Decision Points
- If the read is partial / the tool can't reach the bootloader: still archive what you have, **flag it as incomplete**, and treat restoration risk as elevated.
- If CVN/CAL-ID can't be read (no comms): you may be looking at an already-damaged module → go to Workflow 4.

## Workflow 2: Geographic / spatial calibration selection (today's technique)

**Goal:** Choose the calibration variant that fits the vehicle's *operating geography* and is legal there.

### Steps
1. Establish the vehicle's **jurisdiction** (registration market → emissions regime: EPA/CARB/Euro/China/BS).
2. Establish the **fuel grade** actually available/used (AKI vs RON, ethanol content).
3. Establish the **elevation band** the vehicle operates across (single site vs fleet spanning altitude).
4. Establish **climate** exposure (cold-start / thermal needs).
5. Query `/reference-collection` for cals matching {model, year, regime, fuel, altitude}; rank by closeness of fit.
6. Run the candidate through `/emissions-legality-gate` before it is ever a flash candidate.

### Decision Points
- If jurisdiction ≠ the cal's origin market (gray-market import): expect readiness/monitor mismatches → pick the correct local-market cal, don't suppress codes.
- If the fleet spans a wide altitude range: prefer a cal with proper **BARO compensation** (Workflow 5) over a fixed sea-level cal.
- If no exact regional match exists in the collection: escalate to OEM/TSB source rather than forcing a near-miss.

## Workflow 3: Hardware-form fitment ("mounting" the cal)

**Goal:** Confirm the calibration matches the vehicle's exact mechanical configuration.

### Steps
1. Inventory the **form**: injector flow rate, MAF/MAP sensor range, turbo/supercharger, transmission model, displacement, cam hardware.
2. Compare the candidate cal's assumed hardware (definition metadata, scaling constants) against the inventory.
3. Flag any axis where cal-assumed ≠ installed (e.g. injector slope/offset, MAF transfer function).
4. Either select a better-fitting cal, or document required scaling corrections (only within legitimate, non-emissions scope).
5. Record fitment verdict in the flash log.

### Decision Points
- If injector or MAF scaling mismatches: **do not flash** until corrected — this is the classic "phantom lean code" trap.
- If trans model differs: TCM/shift tables will be wrong → wrong cal, find the right one.

## Workflow 4: Bricked-module restoration

**Goal:** Bring a non-responsive or corrupt module back using the archived specimen.

### Steps
1. Triage: no comms at all, or comms-but-faulted? Check power/ground and connector first (rule out the trivial).
2. If no comms: attempt **boot mode / bootloader recovery** per the platform (forced bootloader entry, bench/BDM if needed).
3. Restore the **exact archived specimen** (Workflow 1 output) — the original, not a substitute.
4. Re-seal checksums/CVN if the recovery path requires it; re-flash.
5. Verify comms, identifiers, and readiness; re-archive the now-known-good state.

### Decision Points
- If the **bootloader itself** is corrupt: software recovery may be impossible → bench/BDM hardware recovery or module replacement (then Workflow 1 + VIN/immobilizer marry).
- If no specimen was ever archived: you are reconstructing from the reference collection at best — document the (avoidable) provenance break.

## Workflow 5: Altitude / BARO compensation review

**Goal:** Ensure fueling, spark, boost, and thermal behaviour are correct across the operating elevation band.

### Steps
1. Define the elevation band (min/max metres) from operating geography.
2. Pull the BARO/altitude compensation tables (fuel enrichment, spark, boost limit, fan/thermal) from the candidate cal.
3. Check coverage: do the table breakpoints span the actual band, or does the vehicle operate off the edge of the map?
4. Compare against the high-altitude variant in the reference collection where one exists.
5. Recommend the variant (or documented, legal corrections) whose compensation covers the band.

### Decision Points
- If the band exceeds the cal's breakpoints: extrapolation risk (lean/over-boost at altitude) → prefer the high-altitude cal.
- If single fixed site at high altitude: a dedicated high-altitude cal usually beats a sea-level cal with compensation.

## Methodology Phases (gate summary)

### Phase 1 — Preserve
Intake + provenance. No edit happens before a verified specimen exists.

### Phase 2 — Fit
Form fitment (Workflow 3) + spatial/legal selection (Workflows 2 & 5). Decide *which* cal, for *this* hardware, in *this* geography, *legally*.

### Phase 3 — Seal & write
`/checksum-seal` → `/emissions-legality-gate` (must pass) → `/flash-session` with a rollback plan.

### Phase 4 — Verify & archive
Confirm CAL-ID/CVN, drive/monitor readiness, log the event, and file the new known-good state back into the reference collection.
