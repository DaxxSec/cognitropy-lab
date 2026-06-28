# Controller Platform Integration Guide

## Purpose

Most aquaponics systems use some form of automated monitoring — from a Raspberry Pi with pH and temperature probes to commercial SCADA systems. This guide covers how to get data out of common controller platforms and into this workspace for analysis.

## Platform Profiles

### Raspberry Pi + Custom Stack

**Prevalence:** Most common in DIY and small commercial systems.

**Typical setup:**
- Raspberry Pi 3/4/5
- Atlas Scientific pH, DO, EC, temperature probes (I2C)
- Data logged to local CSV, SQLite, or InfluxDB
- Optional: Grafana dashboard, MQTT broker

**How to get data into this workspace:**

```bash
# If logging to CSV (most common)
# Copy the latest readings file
scp pi@192.168.1.100:/home/pi/aquaponics/logs/readings.csv ./outputs/

# Then use /scan with CSV reference
/scan readings.csv

# If logging to InfluxDB
# Export last 24 hours to CSV
influx query 'from(bucket:"aquaponics") |> range(start: -24h)' --raw > outputs/readings.csv
```

**Data format expected:**
```csv
timestamp,pH,temp_c,do_mg_l,nh3_ppm,no2_ppm,no3_ppm,ec_us_cm
2026-03-28T08:00:00Z,6.9,27.2,7.1,0.08,0.04,22,850
2026-03-28T09:00:00Z,6.8,27.4,6.9,0.09,0.04,23,860
```

### Blynk IoT

**Prevalence:** Common in hobby and small-scale systems.

**Typical setup:**
- ESP32 or Arduino with Blynk library
- Sensors publish to Blynk virtual pins
- Data viewable in Blynk app/web

**How to get data into this workspace:**

```bash
# Blynk HTTP API — export pin data
# Replace TOKEN and pin numbers with your values
curl "https://blynk.cloud/external/api/get?token=YOUR_TOKEN&V0&V1&V2&V3" \
  -o outputs/blynk-snapshot.json

# For historical data (Blynk Pro plan required)
curl "https://blynk.cloud/external/api/data/get?token=YOUR_TOKEN&pin=V0&period=WEEK" \
  -o outputs/blynk-history.json
```

**Pin mapping (document in `/onboard`):**
| Virtual Pin | Parameter | Unit |
|-------------|-----------|------|
| V0 | pH | - |
| V1 | Temperature | C |
| V2 | DO | mg/L |
| V3 | EC | uS/cm |

### GroPal / FarmBot / Commercial Systems

**Prevalence:** Commercial operations and well-funded research setups.

**Typical setup:**
- Cloud-connected controller with vendor dashboard
- API access varies by vendor and plan tier

**General approach:**
1. Check if your platform has an API (most commercial systems do)
2. Export data as CSV or JSON
3. Place in `outputs/` directory
4. Use `/scan` with the file reference

**Common export paths:**
- GroPal: Settings > Data Export > CSV
- FarmBot: API at `https://my.farm.bot/api/sensor_readings`
- Custom SCADA: Usually Modbus polling to historian — export from historian

### Manual Readings (No Automation)

**Prevalence:** Beginners, educational setups, backup monitoring.

**How to use this workspace without a controller:**

Simply paste your readings directly into `/scan`:

```
/scan
pH: 6.9, Temp: 27.2C, DO: 7.1 mg/L, NH3: 0.08 ppm, NO2: 0.04 ppm, NO3: 22 ppm
```

Or use the structured template in `prompts/anomaly-scan-template.md`.

**Recommendation:** Even with manual testing, log every reading to `work-log/` with timestamp. Trend data is where anomaly detection becomes powerful — a single reading is a snapshot, but a week of readings reveals patterns.

---

## MQTT Integration (Advanced)

Many DIY systems publish sensor data to an MQTT broker. If your system uses MQTT:

```bash
# Subscribe to sensor topic and log to file
mosquitto_sub -h localhost -t "aquaponics/sensors/#" \
  | tee -a outputs/mqtt-log.txt

# Or capture a single snapshot
mosquitto_sub -h localhost -t "aquaponics/sensors/#" -C 1 \
  -o outputs/mqtt-snapshot.json
```

**Standard topic structure (if you're designing your MQTT schema):**
```
aquaponics/sensors/ph
aquaponics/sensors/temperature
aquaponics/sensors/do
aquaponics/sensors/nh3
aquaponics/sensors/no2
aquaponics/sensors/no3
aquaponics/sensors/ec
aquaponics/sensors/flow_rate
aquaponics/alerts/compound_events
```

---

## Security Note

If your controller is network-connected, also consider running the companion workspace: **[Aquaponics ICS Security](../aquaponics-ics-security/)** — it assesses and hardens the automation infrastructure that keeps your fish alive and your crops growing. A compromised controller can kill a system faster than any biological anomaly.
