# Agent Environment

## Data Sources
_How sensor data enters the workspace:_

- **Manual entry:** Paste readings directly into chat during `/scan` command
- **CSV export:** From controller software (e.g., Neptune Apex, Reef Pi, Home Assistant)
- **Formatted log:** See `work-log/` for historical session data
- **API/webhook:** If using automated monitoring, point to exported data files here

## Sensor Calibration Notes
- pH probes drift — note last calibration date in `context/project.md`
- Ammonia colorimetric kits: liquid API kits preferred over strip tests
- DO meters: calibrate to atmospheric saturation before each session
- Temperature: cross-check probe with calibrated thermometer periodically

## Data Format for `/scan`

Preferred input format (paste into chat):
```
Date: YYYY-MM-DD HH:MM
pH: X.X
Temp: XX.X °C
NH3: X.XX ppm
NO2: X.XX ppm
NO3: XX ppm
DO: X.X mg/L
EC: XXXX μS/cm (optional)
TDS: XXXX ppm (optional)
Flow: [normal/reduced/stopped] (optional)
Fish behavior: [normal/surface/lethargic/off-feed] (optional)
Notes: [any observations]
```

CSV format (for baseline and trend analysis):
```csv
timestamp,pH,temp_c,nh3_ppm,no2_ppm,no3_ppm,do_mgl,ec_us,notes
2026-03-01 08:00,7.1,28.2,0.05,0.02,18,7.3,,
```

## Work Log Convention
Each session entry in `work-log/` should include:
- Date and time of readings
- All measured parameters
- Any interventions made
- Observations (fish behavior, plant appearance, equipment status)
- Follow-up items

## Outputs
- Health reports → `outputs/health-report-YYYY-MM-DD.md`
- Baseline files → `outputs/baseline-YYYY-MM-DD.md`
- Incident reports → `outputs/incident-YYYY-MM-DD-[description].md`
