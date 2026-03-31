# Tools

## Python Simulation Libraries

### Orbital Mechanics
**skyfield** — The go-to Python library for precise orbital calculations
```python
from skyfield.api import load, EarthSatellite, Topos
ts = load.timescale()
satellite = EarthSatellite(line1, line2, 'ISS', ts)
location = Topos('37.33 N', '121.88 W')  # San Jose, CA
t = ts.now()
difference = satellite - location
topocentric = difference.at(t)
alt, az, dist = topocentric.altaz()
```

**pyorbital** — Simpler alternative for pass prediction
```python
from pyorbital.orbital import Orbital
orb = Orbital("ISS", line1=tle_line1, line2=tle_line2)
passes = orb.get_next_passes(datetime.utcnow(), 24, lat, lon, alt)
```

### Protocol Parsing
**construct** — Declarative binary protocol parser, ideal for satellite frames
```python
from construct import *
AX25Frame = Struct(
    "flag" / Bytes(1),
    "dest_addr" / Bytes(7),
    "src_addr" / Bytes(7),
    "control" / Bytes(1),
    "pid" / Bytes(1),
    "info" / GreedyBytes,
)
```

**bitstring** — Bit-level manipulation
```python
import bitstring
bs = bitstring.BitArray(hex='7E9C6094A8A0E06094A8A4E1030')
crc = bs[0:16].uint
```

### Signal Processing
**numpy / scipy** — Core numerical and DSP library
```python
import numpy as np
# Doppler shift calculation
def doppler_shift(f_center, velocity_radial_ms):
    c = 3e8  # speed of light
    return f_center * velocity_radial_ms / c

# BER for BPSK in AWGN
def ber_bpsk(ebn0_db):
    from scipy.special import erfc
    ebn0 = 10**(ebn0_db/10)
    return 0.5 * erfc(np.sqrt(ebn0))
```

**matplotlib** — Visualization
```python
import matplotlib.pyplot as plt
# Plot BER curve, Doppler profile, link margin vs elevation
```

## Command-Line Tools (Reference for Users)

### GNURadio
Primary SDR signal processing framework. Used to build flowgraphs for:
- Receiving satellite signals
- Demodulating BPSK/QPSK/FSK/MSK
- Decoding AX.25, CCSDS frames
- Correlating against known sync words

### gr-satellites
GNURadio out-of-tree module with decoders for 100+ amateur satellites
```bash
# Install
pip install gr-satellites
# Receive and decode GOMX-3
python -m satellites GOMX-3 --wavfile pass_recording.wav --samp-rate 48000
```

### SatDump
All-in-one satellite signal decoder and imagery processor
```bash
satdump live meteor_m2-x_lrpt --source rtlsdr --samplerate 1.2e6 --frequency 137.1e6
```

### predict / GPredict
Pass prediction for ground station scheduling
```bash
predict -t norad_id  # CLI pass prediction
```

### Gqrx / SDR# / SDRangel
SDR receiver front-ends for initial signal identification and recording

### KISS / Direwolf
AX.25 TNC implementations
```bash
direwolf -c sdr.conf -r 48000 -D 1  # decode APRS from audio
```

## Link Budget Formulas (Reference)

```python
def link_budget(
    freq_hz, distance_km, tx_power_dbw, tx_gain_dbi,
    rx_gain_dbi, system_noise_temp_k, bandwidth_hz
):
    import numpy as np
    c = 3e8
    wavelength = c / freq_hz
    distance_m = distance_km * 1000

    # Free-space path loss
    fspl_db = 20*np.log10(4*np.pi*distance_m/wavelength)

    # Received power
    rx_power_dbw = tx_power_dbw + tx_gain_dbi - fspl_db + rx_gain_dbi

    # Noise power
    k_boltzmann = 1.38e-23
    noise_power_dbw = (10*np.log10(k_boltzmann) +
                       10*np.log10(system_noise_temp_k) +
                       10*np.log10(bandwidth_hz))

    # C/N ratio
    cn_db = rx_power_dbw - noise_power_dbw
    return {
        'fspl_db': fspl_db,
        'rx_power_dbw': rx_power_dbw,
        'noise_power_dbw': noise_power_dbw,
        'cn_db': cn_db
    }
```

## Protocol Standards References

| Protocol | Standard Document |
|---|---|
| AX.25 | APRS Protocol Reference v1.0.1; AX.25 v2.2 spec |
| CCSDS TC/TM | CCSDS 232.0-B-4 (TC), CCSDS 131.0-B-5 (TM) |
| CCSDS Space Packet | CCSDS 133.0-B-2 |
| DVB-S2 | ETSI EN 302 307-1 |
| APRS | APRS Protocol Reference v1.0.1 |
| Iridium SBD | Iridium SBD Developer's Guide |
| AIS | ITU-R M.1371-5 |
| KISS | KA9Q TNC-2 spec |
