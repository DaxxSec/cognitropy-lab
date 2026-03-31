# parse-telemetry

Parse and analyze satellite telemetry frames, producing human-readable field breakdowns and health assessments.

When this command is invoked:

1. **Get the telemetry data** — Ask for:
   - Raw frame data (hex, binary, or base64)
   - Protocol/format (CCSDS TM, AX.25 beacon, SatDump output JSON, APRS telemetry, etc.)
   - Satellite name or model if known (this helps infer the telemetry structure)
   - Any ICD (Interface Control Document) or field definition the user has

2. **Parse frame headers**:
   - Strip framing (sync marker, CCSDS TM primary header, or AX.25 header)
   - Identify packet type (science data, housekeeping, beacon, etc.)
   - Decode sequence count and timestamp if present

3. **Parse telemetry payload** using available field definitions:
   - If the satellite has public telemetry definitions (ISS, NOAA, many amateur cubesats), apply them
   - Common telemetry fields: battery voltage, temperature sensors, power consumption, attitude data, memory status, uptime counter
   - If no field definitions available, present raw bytes with likely interpretations (two's complement int16, IEEE 754 float, etc.)

4. **Produce annotated telemetry report**:
   ```
   TELEMETRY FRAME ANALYSIS
   Satellite: [Name]  |  Packet type: Housekeeping  |  Seq: 1,247
   ================================================================
   FIELD                  | RAW   | VALUE    | STATUS
   -----------------------|-------|----------|--------
   Battery Voltage        | 0x2F4 | 7.56 V   | ✅ Nominal (7.2-8.4 V)
   Battery Temp           | 0x1A  | 26°C     | ✅ Nominal (-5 to 45°C)
   Solar Panel +X Power   | 0x089 | 137 mW   | ✅ Nominal
   CPU Temperature        | 0x23  | 35°C     | ✅ Nominal
   Memory Free            | 0xFFE | 65,534 B | ⚠️  Low
   Uptime                 | ...   | 14d 3h   | ✅
   ================================================================
   SUMMARY: 5/6 parameters nominal. Memory free is low.
   ```

5. **Flag anomalies** — Any values outside expected ranges should be clearly highlighted with:
   - The expected range
   - The actual value
   - Possible causes
   - Recommended follow-up

6. **Provide context** — For well-known satellites, note what this telemetry suggests about the satellite's health and operational state.
