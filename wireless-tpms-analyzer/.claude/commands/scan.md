# Scan

Plan or analyze a TPMS capture session.

## Usage

Run `/scan` to get a customized capture plan, or paste your capture output for review.

## What I'll do

**If you're planning a capture:**
- Ask for your region (NA/EU/Asia) and hardware (RTL-SDR, HackRF)
- Provide the exact rtl_433 command for your setup
- Recommend antenna type, SDR gain settings, and capture duration
- Explain what to expect in the output

**If you have capture results:**
- Summarize how many unique sensors were detected
- Identify any unrecognized protocols (raw/unknown output)
- Flag anomalies (unexpected frequencies, unusually low signal, missing sensors)
- Suggest next steps (decode, identify, or RE if unknown)

## Quick Reference

```bash
# NA vehicles (315 MHz) — real-time with JSON logging
rtl_433 -f 315M -s 250k -F json -F kv 2>&1 | tee session-$(date +%Y%m%d).log

# EU/Asia vehicles (433.92 MHz)
rtl_433 -f 433.92M -s 250k -F json | tee session-$(date +%Y%m%d).json

# Save raw IQ for offline RE of unknown protocols
rtl_sdr -f 315000000 -s 250000 -n 10000000 capture-$(date +%Y%m%d-%H%M).cu8

# Power scan to find active frequencies
rtl_power -f 300M:450M:100k -g 40 -i 10 -1 power_survey.csv
```

## Tips for Better Captures

- Drive or roll the vehicle — sensors activate above ~10 km/h and transmit every 60–90 seconds
- Parking lot laps work well; even rolling a stationary vehicle a few feet will trigger some sensors
- Gain setting: start at `-g 40`, reduce if you see overload artifacts
- If using HackRF: `hackrf_transfer -r capture.cs8 -f 315000000 -s 2000000 -l 40 -g 40`
