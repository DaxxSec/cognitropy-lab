# Getting Started with Wireless TPMS Analyzer

## What You Need

**Hardware (minimum):**
- RTL-SDR dongle (RTL2832U-based, ~$25–40)
- 1/4-wave monopole antenna cut for 315 MHz (~23 cm) or 433 MHz (~17 cm)
- A vehicle with direct TPMS (all US vehicles 2008+, EU vehicles 2014+)

**Hardware (recommended):**
- HackRF One for wideband signal survey and characterization

**Software (Linux/macOS):**

```bash
# Ubuntu/Debian
sudo apt install rtl-sdr rtl-433 inspectrum gqrx-sdr

# macOS (Homebrew)
brew install rtl-sdr rtl_433

# From source (latest features)
git clone https://github.com/merbanan/rtl_433.git
cd rtl_433 && mkdir build && cd build
cmake .. -DENABLE_SOAPYSDR=ON && make -j4
sudo make install
```

For URH (Universal Radio Hacker):
```bash
pip3 install urh
```

## Your First Capture

1. Plug in your RTL-SDR dongle
2. Verify it's recognized: `rtl_test -t`
3. Determine your region's frequency:
   - North America: `315 MHz`
   - Europe/Australia/Asia: `433.92 MHz`

4. Start decoding:

```bash
# North America
rtl_433 -f 315M -s 250k -F json

# Europe/Asia
rtl_433 -f 433.92M -s 250k -F json
```

5. **Drive or roll your vehicle** — TPMS sensors activate above ~10 km/h. Even rolling back and forth in a driveway works. Within 1–2 minutes you should see output like:

```json
{"time":"2026-03-29 10:15:23","model":"Schrader-EG53MA4","type":"TPMS","id":"0x8C32A1",
 "pressure_PSI":32.50,"temperature_C":21,"flags":0,"mic":"CHECKSUM"}
```

6. You found your TPMS sensors! Note the `id` values — these are your unique sensor fingerprints.

## Working with Claude (Signal Ghost)

Once you have output, paste it into a Claude session with this workspace active and use:

- `/onboard` — Get oriented and review your hardware setup
- `/scan` — Get help planning or reviewing your capture
- `/decode` — Deep-dive decode of a specific packet
- `/identify` — Find out which manufacturer made your sensors
- `/protocol-map` — If you have an unknown/raw sensor, begin reverse engineering

## Seasonal Tire Swap Workflow (Common Use Case)

When swapping between summer and winter tires:

1. Before the swap: capture your current sensor IDs and note which set they belong to
2. After the swap: run a new capture to confirm all 4 sensors from the new set are broadcasting
3. Cross-check against your vehicle's TPMS warning light — if it stays on, the ECU hasn't learned the new sensors and needs a relearn procedure
4. Use the `/scan` command and paste both captures — Signal Ghost will diff them and flag any missing or unexpected sensors

## Troubleshooting

| Problem | Solution |
|---|---|
| `rtl_sdr: error opening device` | Check USB connection; may need `sudo` or udev rules |
| No TPMS packets | Roll the vehicle; check you're on the right frequency for your region |
| Packets show `UNKNOWN` | Unknown protocol — use `/protocol-map` |
| Pressure values seem wrong | Wrong conversion formula — use `/decode` and Signal Ghost will diagnose |
| Only 3 sensors found | One sensor may be faulty or still in deep sleep — drive longer |
