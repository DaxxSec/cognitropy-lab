# Common OBD-II Fault Codes for Performance Platforms

Quick reference for OBD-II codes commonly encountered on tuned and modified vehicles. Includes generic codes and platform-specific interpretations for common performance platforms.

---

## How to Read This Reference

Each entry includes:
- **Code:** Standard OBD-II or platform-specific code
- **Description:** What the ECU detected
- **Common Causes (Tuned Vehicle):** Why this appears specifically on modified cars
- **Priority:** How urgently to address this

---

## Fuel System Codes

| Code | Description | Common Causes on Modified Cars | Priority |
|------|-------------|-------------------------------|----------|
| P0171 | Fuel System Lean (Bank 1) | Injectors undersized for boost, fuel pump failing, boost leak, MAF calibration issue | HIGH |
| P0172 | Fuel System Rich (Bank 1) | Injectors oversized, fueling map over-calibrated, stuck injector | Medium |
| P0174 | Fuel System Lean (Bank 2) | Same as P0171 on V engines | HIGH |
| P0201–P0208 | Injector Circuit (Cylinder N) | Bad injector, injector driver failure, wiring | High |
| P0261–P0272 | Injector Low/High Voltage | Injector wiring or driver fault | High |
| P0087 | Fuel Rail Pressure Low | Fuel pump failing (common on high-HP builds), clogged filter, FPR issue | HIGH |
| P0088 | Fuel Rail Pressure High | FPR stuck or miscalibrated | High |
| P0190–P0194 | Fuel Rail Pressure Sensor | Sensor failure, wiring | Medium |

---

## Boost / Intake Codes

| Code | Description | Common Causes on Modified Cars | Priority |
|------|-------------|-------------------------------|----------|
| P0299 | Turbocharger Underboost | Boost leak (most common), wastegate stuck open, BOV leaking, cracked pipe | High |
| P0234 | Turbocharger Overboost | Boost controller fault, stuck wastegate, MAP sensor issue | HIGH |
| P0101 | MAF Sensor Range/Performance | MAF can't read modified air volume, dirty MAF, intake leak | High |
| P0102 | MAF Low Input | MAF failure, wiring, intake configuration incompatible | High |
| P0103 | MAF High Input | Same as above | High |
| P0113 | IAT Sensor High (hot) | Normal if IAT actually hot; sensor failure if not | Low-Med |
| P0068 | MAP/TPS Correlation | MAP sensor issue, boost leak, sensor calibration | Medium |
| P0106 | MAP Sensor Range | MAP sensor failure, hose disconnected | High |

---

## Ignition / Misfire Codes

| Code | Description | Common Causes on Modified Cars | Priority |
|------|-------------|-------------------------------|----------|
| P0300 | Random Misfire | Lean condition, bad plug, ignition failing under boost, fuel delivery | HIGH |
| P0301–P0308 | Cylinder N Misfire | Same as P0300 but isolated to one cylinder | HIGH |
| P0351–P0358 | Ignition Coil Circuit | Coil failure (common at high boost — plugs and coils wear faster) | High |
| P0325 | Knock Sensor 1 Circuit | Knock sensor wiring or failure — IMPORTANT to fix; ECU can't protect engine | HIGH |
| P0330 | Knock Sensor 2 Circuit | Same as P0325 on Bank 2 | HIGH |

> ⚠️ P0325/P0330 are critical — if the knock sensor circuit is open, the ECU cannot detect detonation and will NOT pull timing. Do not make WOT pulls with these active.

---

## Oxygen Sensor / Emissions Codes

| Code | Description | Common Causes on Modified Cars | Priority |
|------|-------------|-------------------------------|----------|
| P0420 | Catalyst Efficiency Below Threshold | No catalytic converter (catless or test pipe) — this is expected on de-catted cars | Low (expected) |
| P0430 | Catalyst Efficiency (Bank 2) | Same — expected on de-catted V engines | Low (expected) |
| P0130–P0167 | O2 Sensor Codes | Sensor failure, wiring, or sensor in a location that doesn't work for your exhaust | Varies |
| P0131 | O2 Sensor Low Voltage (B1S1) | Pre-cat narrowband failing, check wiring | Medium |
| P0132 | O2 Sensor High Voltage (B1S1) | Rich condition or sensor stuck | Medium |
| P0138 | O2 Sensor High Voltage (B1S2) | Post-cat sensor saturated by rich exhaust | Low (expected) |

---

## AVCS / VVT / Cam Codes (Subaru-Specific)

| Code | Description | Common Causes | Priority |
|------|-------------|---------------|----------|
| P0011 | Cam Timing Over-Advanced (Bank 1) | AVCS solenoid dirty, AVCS oil pressure issue, cam gear worn | High |
| P0012 | Cam Timing Over-Retarded (Bank 1) | Same as P0011 | High |
| P0021/P0022 | Bank 2 AVCS equivalent | Same, Bank 2 | High |

---

## Transmission / Speed Codes

| Code | Description | Common Causes on Modified Cars | Priority |
|------|-------------|-------------------------------|----------|
| P0720 | Output Speed Sensor | Speed sensor failure, wiring — common after transmission work | Medium |
| P0740 | Torque Converter Clutch | TCC solenoid issue; common after tune changes on automatics | Medium |
| P0700 | Transmission Control System | TCM fault — see transmission-specific codes | Medium |

---

## Freeze Frame Data — What to Record

When a fault code appears, always record the freeze frame data:
- **RPM at fault**
- **Load / TPS at fault**
- **Engine temp at fault**
- **Vehicle speed at fault**
- **Short-term and long-term fuel trims (STFT / LTFT)**
- **MAP / boost at fault**

This context is critical for diagnosis. A P0171 at idle vs. at WOT have very different causes.

---

## General Troubleshooting Principle for Modified Cars

**Before chasing sensor codes on a modified car, check:**
1. Is there a boost leak? (causes multiple false-positive codes)
2. Is the MAF calibrated for your intake? (causes lean codes)
3. Is the tune correct for your current hardware? (all codes can result from bad calibration)
4. Are the injectors matched to the fuel map? (size mismatch = lean or rich codes)

Many codes on modified cars are symptoms of tuning issues, not hardware failures. Fix the root cause in the calibration before replacing sensors.
