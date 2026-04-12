# Tools & Integrations

## SDR Capture Tools

### hackrf_transfer
- **Purpose:** Raw IQ capture/playback with HackRF
- **Key flags:** `-r` (receive), `-t` (transmit), `-f` (frequency), `-s` (sample rate), `-a` (amp enable), `-l` (LNA gain), `-g` (VGA gain)
- **Example:** `hackrf_transfer -r capture.raw -f 433920000 -s 2000000 -a 1 -l 32 -g 30`

### hackrf_sweep
- **Purpose:** Fast wideband spectrum scanning
- **Key flags:** `-f` (freq range), `-w` (bin width), `-1` (one-shot)
- **Example:** `hackrf_sweep -f 400:450 -w 100000 -1 > sweep.csv`

### rtl_sdr
- **Purpose:** Raw IQ capture with RTL-SDR
- **Key flags:** `-f` (frequency), `-s` (sample rate), `-g` (gain)
- **Example:** `rtl_sdr -f 433920000 -s 2048000 -g 40 capture.raw`

### rtl_power
- **Purpose:** Spectrum scanning with RTL-SDR
- **Example:** `rtl_power -f 400M:450M:100k -g 40 -i 10 -e 1h scan.csv`

## Analysis Tools

### GNU Radio Companion (GRC)
- **Purpose:** Visual DSP flowgraph design and execution
- **Key blocks:** osmocom Source, Low Pass Filter, Quadrature Demod, Clock Recovery MM, Binary Slicer
- **Integration:** Python API for scripted analysis

### Universal Radio Hacker (URH)
- **Purpose:** End-to-end protocol analysis (capture, decode, analyze)
- **Features:** Automatic modulation detection, bit-level protocol analysis, fuzzing, simulation
- **Best for:** Simple OOK/ASK/FSK protocols, keyfobs, remotes

### Inspectrum
- **Purpose:** Visual IQ file analysis
- **Features:** Spectrogram view, amplitude/frequency/phase plots, cursor measurements
- **Best for:** Initial modulation identification, symbol timing measurement

### rtl_433
- **Purpose:** Decode known ISM band protocols
- **Protocols:** 200+ supported (weather stations, TPMS, smart meters, etc.)
- **Example:** `rtl_433 -f 433920000 -R 0 -S all` (unknown mode, save all signals)

### SigDigger
- **Purpose:** Spectrum analyzer and signal analyzer
- **Features:** Real-time FFT, waterfall, signal detection, channel inspection

## Post-Processing Tools

### Python Scientific Stack
- `numpy` — Array operations, FFT, signal math
- `scipy.signal` — Filters, resampling, spectral analysis
- `matplotlib` — Plotting (spectrogram, constellation, eye diagram)
- `scapy` — Packet crafting and analysis (after protocol decode)

### CyberChef
- **Purpose:** Data transformation, encoding/decoding, CRC calculation
- **URL:** https://gchq.github.io/CyberChef/

### Wireshark (with custom dissectors)
- **Purpose:** Packet-level protocol analysis after decode
- **Custom dissectors:** Lua scripts for proprietary protocols

## Databases & References
- **Sigidwiki:** https://www.sigidwiki.com — Signal identification database
- **rtl_433 protocols:** https://github.com/merbanan/rtl_433 — Known protocol decoders
- **FCC ID lookup:** https://fccid.io — Device registration and RF specs
- **Wireless frequencies:** https://www.ntia.doc.gov/page/2011/united-states-frequency-allocation-chart
