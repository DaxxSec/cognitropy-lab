# Software Defined Radio Development — Reference Tables

Lookup data the agent reaches for during SDR work. Compact by design — defer to cited upstream sources for full text.

## Hardware Spec Matrix

| Device | Freq range | Inst. BW | Max sample rate | ADC bits | Duplex | Link | ~Cost |
|---|---|---|---|---|---|---|---|
| RTL-SDR v3/v4 | 24 MHz–1.7 GHz | 2.4 MHz | 3.2 Msps (2.4 stable) | 8 | RX only | USB 2.0 | $30 |
| Airspy R2/Mini | 24 MHz–1.8 GHz | 10/6 MHz | 10 Msps | 12 | RX only | USB 2.0 | $100-170 |
| HackRF One | 1 MHz–6 GHz | 20 MHz | 20 Msps | 8 | Half | USB 2.0 | $300 |
| PlutoSDR (ADALM) | 325 MHz–3.8 GHz* | 20 MHz | 61 Msps | 12 | Full | USB 2.0 | $230 |
| LimeSDR | 100 kHz–3.8 GHz | 61.44 MHz | 61.44 Msps | 12 | Full | USB 3.0 | $300 |
| BladeRF 2.0 micro | 47 MHz–6 GHz | 56 MHz | 61.44 Msps | 12 | Full | USB 3.0 | $540 |
| USRP B210 | 70 MHz–6 GHz | 56 MHz | 61.44 Msps | 12 | Full | USB 3.0 | $1500 |
| USRP X310 | DC–6 GHz | 160 MHz | 200 Msps | 14 | Full | 10GbE/PCIe | $5000+ |

*PlutoSDR frequency range expandable via firmware hack to ~70 MHz–6 GHz.

## Link Throughput Limits

| Link | Practical throughput | Max IQ rate (int8) | Max IQ rate (int16) |
|---|---|---|---|
| USB 2.0 | ~35-40 MB/s | ~18-20 Msps | ~9-10 Msps |
| USB 3.0 | ~350-400 MB/s | ~175 Msps | ~90 Msps |
| 1 GbE | ~110 MB/s | ~55 Msps | ~27 Msps |
| 10 GbE | ~1.1 GB/s | ~550 Msps | ~275 Msps |
| PCIe 3.0 x4 | ~3.5 GB/s | very high | very high |

IQ rate = throughput / (bytes_per_sample × 2). int8 = 2 bytes/IQ-sample; int16 = 4 bytes/IQ-sample.

## Decimation Cheat-Sheet

| Scenario | Recommended approach |
|---|---|
| Small D (2-10) | Single FIR decimator, or half-bands if power-of-2 |
| Medium D (10-50) | 2-3 stage FIR cascade, sharpest filter last |
| Large D (>50) | CIC first stage + FIR compensation/cleanup |
| Factor of 2 stage | Half-band filter (~2× cheaper, half taps zero) |
| Rational P/Q | Polyphase `rational_resampler` |
| Variable / fractional | Polyphase arbitrary resampler (`pfb_arb_resampler`) |

## GNU Radio Block Reference (commonly used)

| Block | Purpose |
|---|---|
| `osmocom Source` / `soapy_source` | SDR hardware source |
| `Frequency Xlating FIR Filter` | tune + filter + decimate in one (very common) |
| `Rational Resampler` | P/Q rate conversion |
| `Low Pass Filter` / `Band Pass Filter` | FIR filtering |
| `FFT` / `Log Power FFT` | spectral analysis |
| `Polyphase Channelizer` | split wideband into N channels |
| `Quadrature Demod` | FM/FSK demod |
| `Costas Loop` | carrier recovery for PSK |
| `Symbol Sync` / `Polyphase Clock Sync` | timing recovery |
| `File Sink` / `File Source` | IQ capture/replay |
| `QT GUI Sink` / `QT GUI Waterfall` | display (desktop only — replace for headless) |

## Profiling / Tooling

| Tool | Use |
|---|---|
| `volk_profile` | Benchmark + select optimal SIMD kernels (run first!) |
| `gr-perf-monitorx` | Live per-block work/throughput |
| GNU Radio performance counters | Per-block stats (`--enable-perf-counters`) |
| `perf top` | System-level CPU hotspots |
| `htop` | Per-core load |
| `usbtop` | USB bus throughput |
| `hackrf_info` / `uhd_usrp_probe` / `SoapySDRUtil` | Device identification + capabilities |

## Upstream Catalogues

- **[GNU Radio wiki](https://wiki.gnuradio.org/)** — block reference, tutorials, performance counters.
- **[PySDR (pysdr.org)](https://pysdr.org/)** — Marc Lichtman's free SDR+DSP textbook in Python.
- **[VOLK (libvolk.org)](https://www.libvolk.org/)** — SIMD kernel library + `volk_profile` docs.
- **[SoapySDR wiki](https://github.com/pothosware/SoapySDR/wiki)** — vendor-neutral hardware abstraction.
- **[Ettus UHD manual](https://files.ettus.com/manual/)** — USRP driver + application notes.
- **[rtl_433 device list](https://github.com/merbanan/rtl_433)** — 200+ decoded ISM protocols (reference for decode targets).
- **[sigidwiki.com](https://www.sigidwiki.com/)** — signal identification database.
- **[GQRX](https://gqrx.dk/)** / **[SDR++](https://www.sdrpp.org/)** — reference receiver applications.

## Sample-Rate Quick Math

- Captured bandwidth (complex IQ) = sample rate. (NOT rate/2.)
- File size = rate × bytes_per_sample × 2 × seconds. (e.g. 2.4 Msps × int16 × 2 × 60 s = ~576 MB/min)
- FFT bin width = rate / FFT_size. (e.g. 2.4 Msps / 4096 = 586 Hz/bin)
- FFT latency ≈ FFT_size / rate. (e.g. 4096 / 2.4 Msps = 1.7 ms)

## Vocabulary Disambiguation

- **"Bandwidth"** — RF bandwidth of a signal vs. instantaneous bandwidth of the SDR (capture window) vs. link bandwidth (USB/PCIe). Always specify which.
- **"Rate"** — sample rate (Msps) vs. symbol/baud rate (modulation) vs. bit rate. Context-dependent.
- **"Decimation"** — downsampling-with-filter; not the same as plain downsampling (which aliases).
- **"Sink" / "Source"** — GNU Radio terms (data out / data in), opposite of intuitive "source = origin" only in that a File Sink writes and a File Source reads.
