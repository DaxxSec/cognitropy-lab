# Satellite Comms Tools Reference

## SDR Software

### GNURadio
- **What it is:** Visual signal processing framework using flowgraphs
- **Install:** `sudo apt install gnuradio` or `pip install gnuradio`
- **Key blocks for satellite:** RTL-SDR Source, NBFM Demod, Costas Loop, Symbol Sync, Correlation Estimator
- **Satellite extension:** gr-satellites (100+ satellite decoders)
- **URL:** https://www.gnuradio.org

### gr-satellites
- **What it is:** GNURadio OOT module for amateur satellite decoders
- **Install:** `pip install gr-satellites`
- **Usage:** `python -m satellites NOAA-18 --wavfile recording.wav --samp-rate 48000`
- **Supported:** AX.25, CCSDS, CubeSat protocols, 100+ satellites
- **URL:** https://gr-satellites.readthedocs.io

### SatDump
- **What it is:** All-in-one satellite signal decoder and imagery processor
- **Supports:** NOAA APT/HRPT, Meteor-M2 LRPT, FengYun, MetOp, and more
- **Install:** Pre-built binaries at https://github.com/SatDump/SatDump
- **Live mode:** `satdump live noaa_apt --source rtlsdr --frequency 137.9125e6`

### Gqrx
- **What it is:** SDR receiver application (Linux/macOS)
- **Use for:** Initial signal identification, IQ file recording, audio output to decoders
- **URL:** https://gqrx.dk

### SDR# (SDRSharp)
- **What it is:** SDR receiver application (Windows)
- **Plugins:** ATC, ACARS, APRS available
- **URL:** https://www.sdrsharp.com

---

## Protocol Tools

### Direwolf
- **What it is:** Software AX.25 TNC — decodes AFSK1200/4800, produces KISS frames
- **Install:** `sudo apt install direwolf`
- **Usage:** Pipe audio from receiver: `direwolf -c sdr.conf -r 48000 -D 1`
- **Features:** APRS decode/encode, iGate, digipeater
- **URL:** https://github.com/wb2osz/direwolf

### KISS-TNC and AX.25 Linux
- **ax25-tools:** `sudo apt install ax25-tools` — provides `axlisten`, `axcall`
- **Listen to AX.25:** `axlisten -a`
- **KISS over TCP:** Connect Direwolf to any AX.25 application via KISS on TCP port 8001

### YAMCS (Yet Another Mission Control System)
- **What it is:** Open-source mission control system — handles CCSDS TC/TM
- **Features:** Telemetry display, command history, parameter archives, alarms
- **URL:** https://yamcs.org
- **Use case:** Full ground station software for cubesat missions

### OpenSatCom / Lithium
- **OpenSatCom:** Collection of cubesat communication protocol tools
- **CCSDS libraries:** `libccsds3` for Space Packet handling

---

## Orbital Prediction

### GPredict
- **What it is:** GUI satellite tracking and pass prediction
- **Install:** `sudo apt install gpredict`
- **Features:** Real-time tracking, pass prediction, Doppler correction via Hamlib
- **URL:** http://gpredict.oz9aec.net

### Predict
- **What it is:** CLI satellite pass predictor
- **Install:** `sudo apt install predict`
- **Usage:** `predict -t 25544` (ISS NORAD ID)

### Heavens-Above
- **URL:** https://www.heavens-above.com
- **Use for:** Quick web-based pass prediction

### Celestrak
- **URL:** https://celestrak.org
- **Use for:** TLE downloads, SOCRATES (conjunction analysis)
- **API:** `https://celestrak.org/SOCRATES/query.php?INTDES=1998-067A&TYPE=b&RANGE=10&DIR=0`

---

## Python Libraries

### skyfield
- **Install:** `pip install skyfield`
- **Use for:** Precise orbital calculations, pass prediction, Doppler
- **Docs:** https://rhodesmill.org/skyfield/

### pyorbital
- **Install:** `pip install pyorbital`
- **Use for:** Simpler pass prediction, satellite position

### construct
- **Install:** `pip install construct`
- **Use for:** Declarative binary protocol parsing (AX.25, CCSDS frames)
- **Docs:** https://construct.readthedocs.io

### bitstring
- **Install:** `pip install bitstring`
- **Use for:** Bit-level manipulation of satellite frames

### crcmod
- **Install:** `pip install crcmod`
- **Use for:** CRC calculation (CRC-CCITT for AX.25/CCSDS)
- **Usage:** `crc_fn = crcmod.predefined.mkCrcFun('crc-ccitt-false')`

---

## Standards and References

| Standard | Document | Download |
|---|---|---|
| AX.25 v2.2 | APRS protocol reference | http://www.aprs.org/doc/APRS101.PDF |
| CCSDS TC frames | CCSDS 232.0-B-4 | https://public.ccsds.org |
| CCSDS TM frames | CCSDS 132.0-B-3 | https://public.ccsds.org |
| CCSDS Space Packet | CCSDS 133.0-B-2 | https://public.ccsds.org |
| CCSDS Security | CCSDS 352.0-B-2 | https://public.ccsds.org |
| DVB-S2 | ETSI EN 302 307-1 | https://www.etsi.org |
| AIS | ITU-R M.1371-5 | https://www.itu.int |

---

## TLE Sources

| Source | URL | Update Frequency |
|---|---|---|
| Celestrak | https://celestrak.org/SOCRATES/ | Multiple times daily |
| Space-Track | https://www.space-track.org | Official USSPACECOM source |
| AMSAT | https://amsat.org/keps/ | Amateur satellites focused |
| N2YO | https://www.n2yo.com | Web tracking + TLEs |
