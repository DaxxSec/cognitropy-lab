# Identify

Identify a TPMS sensor's manufacturer, protocol, and vehicle compatibility from decoded data or physical markings.

## Usage

Provide any of:
- Decoded sensor ID and packet data (from rtl_433 or `/decode`)
- Physical markings on the sensor (FCC ID, part number, valve stem label)
- Vehicle year/make/model (I can suggest likely OEM suppliers)
- Signal characteristics (frequency, modulation, symbol rate)

## What I'll determine

1. **Manufacturer** — Schrader, Continental, Huf, Pacific Industries, Sensata, or aftermarket
2. **Protocol variant** — specific decoder module in rtl_433 if supported
3. **Vehicle OEM applications** — which makes/models this sensor was factory-fitted to
4. **OBD relearn requirements** — what procedure the ECU needs after sensor replacement
5. **Aftermarket compatibility** — compatible replacement part numbers if relevant
6. **FCC ID lookup** — I'll direct you to the FCC filing if an ID is available

## FCC ID Pattern Examples

TPMS sensors must have FCC authorization. The FCC ID is usually printed on the sensor body:
- Schrader: typically `KR5S180144206` format
- Continental: typically `KR5S120123456` format
- Search at: `https://fccid.io/[FCC-ID]` for RF test reports and block diagrams

## Sensor Body Markings to Note

If you have the physical sensor, photograph or note:
- FCC ID (required on all US devices)
- Part number (P/N)
- Date code
- Frequency marking (e.g., "433.92 MHz" or "315 MHz")
- Manufacturer logo
