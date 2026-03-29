# Report

Generate a structured protocol analysis or session summary report.

## Report Types

### Session Summary
A log of what was captured in a given session: sensors detected, signal quality, anomalies, and next steps.

### Protocol Analysis Report
A detailed technical document suitable for sharing with the rtl_433 community or as personal reference. Includes:
- Protocol overview and regulatory context
- Frequency and modulation parameters
- Packet structure diagram (ASCII art or table)
- Field definitions with conversion formulas
- Checksum algorithm specification
- Sample decoded packets
- Known vehicle OEM applications
- Notes on protocol variations

### Sensor Inventory Report
A summary of all TPMS sensors discovered across one or more vehicles, with wheel position mapping and seasonal rotation history.

## Usage

Tell me which type you need and provide:
- Session logs, captured packet JSON, or protocol notes
- Vehicle info if relevant (year/make/model)
- Intended audience (personal reference, community submission, security research)

## Output

Reports are saved to `outputs/` with a timestamped filename:
- `outputs/session-[date].md`
- `outputs/protocol-[sensor-model]-[date].md`
- `outputs/sensor-inventory-[vehicle]-[date].md`
