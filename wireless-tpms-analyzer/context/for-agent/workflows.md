# Workflows

## Workflow 1: First Capture — Identify Active Sensors

**Goal:** Discover and log all TPMS sensors broadcasting from a vehicle.

1. **Setup hardware** — RTL-SDR with 1/4-wave monopole antenna. Position within ~5m of the vehicle.
2. **Visual sweep** — Open GQRX or SDR# tuned to 315 MHz (NA) or 433.92 MHz (EU). Set bandwidth to 1 MHz. Drive or roll the vehicle to trigger sensor transmissions.
3. **Run rtl_433** — `rtl_433 -f 315M -s 250k -F json` (NA) or `rtl_433 -f 433.92M -s 250k -F json` (EU). Capture for 5–10 minutes while driving slowly.
4. **Review output** — Each decoded packet should show model, ID, pressure, temperature. Note any unrecognized sensors (will show as raw data).
5. **Correlate to wheels** — If 4 unique sensor IDs appear, verify against vehicle's TPMS screen or OBD reader. Note which ID maps to which wheel position.
6. **Log session** — Record sensor IDs, vehicle info, frequency, and capture date in `work-log/session-log.md`.

---

## Workflow 2: Decode Known Protocol from rtl_433 JSON

**Goal:** Fully interpret an rtl_433 decoded TPMS packet.

1. Paste JSON output into chat, e.g.:
   ```json
   {"model":"Schrader-EG53MA4","type":"TPMS","id":"0x8C32A1","pressure_PSI":32.25,"temperature_C":24,"flags":0,"mic":"CHECKSUM"}
   ```
2. Agent identifies protocol, extracts fields, verifies checksum logic, converts units if needed.
3. Explain any flags or anomaly values (e.g., `0xFF` pressure = sensor fault, battery low flag meaning).
4. Cross-reference ID against any previously logged sensors.

---

## Workflow 3: Reverse Engineer an Unknown Protocol

**Goal:** Decode a sensor that rtl_433 shows as raw/unknown.

1. **Capture IQ file** — `rtl_sdr -f 315M -s 250k -n 5000000 capture.cu8`
2. **Open in inspectrum** — Identify burst timing, preamble pattern, symbol boundaries.
3. **Estimate symbol rate** — Measure pulse width in inspectrum. Symbol rate ≈ 1 / pulse_width.
4. **Extract bits in URH** — Import file, set modulation type and sample rate. Use "Autodetect parameters" as starting point, then refine.
5. **Identify structure** — Look for: long preamble (alternating 0/1), sync word (fixed pattern before data), data payload, checksum.
6. **Field analysis** — Check for 24–32 bit sequence that repeats across packets = sensor ID. Look for byte that increments ≈ with temperature. Check byte against PSI/kPa conversion tables.
7. **Checksum reverse engineering** — Collect 6+ packets, vary only one variable, XOR/CRC brute force with Python script.
8. **Write flex decoder** — Once fields are mapped, create rtl_433 flex decoder config. Test against capture.
9. **Submit to rtl_433** — If confirmed working, open a GitHub issue/PR to add the new device.

---

## Workflow 4: Sensor Swap / Wheel Rotation Tracking

**Goal:** Verify all 4 new sensors are broadcasting after a tire swap (e.g., summer/winter changeover).

1. Run `rtl_433 -f 315M -F json | tee seasonal-swap-$(date +%Y%m%d).json`
2. Drive for 10 minutes above walking pace (sensors typically activate above ~10 km/h).
3. Filter output: `cat seasonal-swap-*.json | jq '.id' | sort | uniq`
4. Compare the 4 unique IDs against your documented sensor inventory.
5. If any ID is missing, that sensor may be faulty, not learned by ECU, or on a different frequency.
6. Cross-check against OBD TPMS monitor to confirm ECU agreement.

---

## Workflow 5: Protocol Documentation Report

**Goal:** Produce a structured report on a TPMS protocol for sharing/archiving.

1. Use `/report` slash command to initiate.
2. Provide: sensor model/FCC ID, capture frequency, decoded sample packets, field mapping table.
3. Agent generates formatted report with: protocol overview, frequency/modulation parameters, packet structure diagram, field definitions with conversion formulas, checksum algorithm, sample decoded packets, known vehicle applications.
4. Save to `outputs/protocol-[sensor-model]-[date].md`.
