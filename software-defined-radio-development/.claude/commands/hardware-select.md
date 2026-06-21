# /hardware-select

Recommend SDR hardware sized to frequency range, bandwidth, duplex mode, dynamic range, and budget.

## Inputs

- **Frequency range** needed (Hz min–max).
- **Instantaneous bandwidth** needed.
- **Duplex** — receive-only, half-duplex, or full-duplex (simultaneous TX+RX).
- **Dynamic range** sensitivity (8-bit OK, or need 12/16-bit for weak-near-strong).
- **Host link** available (USB 2.0, USB 3.0, PCIe, Ethernet).
- **Budget** + **form factor** (desktop, embedded, portable).

## Steps

1. Read `context/references.md` "Hardware spec matrix".
2. Filter the matrix by frequency range — eliminate devices that can't reach the band (e.g. RTL-SDR tops out ~1.7 GHz without a downconverter).
3. Filter by instantaneous bandwidth — RTL-SDR ~2.4 MHz, HackRF ~20 MHz, USRP B210 ~56 MHz, etc.
4. Filter by duplex — HackRF is half-duplex; USRP / LimeSDR / BladeRF / PlutoSDR support full-duplex.
5. Filter by ADC bits / dynamic range — 8-bit (HackRF, RTL) vs 12-bit (USRP, Lime, Pluto, BladeRF).
6. Check link compatibility — high sample rates need USB 3.0 / PCIe / 10GbE, not USB 2.0.
7. Rank surviving candidates by budget + form factor fit.
8. Recommend a primary + fallback with the specific spec tradeoffs called out.
9. Write the recommendation to `outputs/hardware/<app>-<YYYY-MM-DD>.md`.

## Output

A markdown hardware recommendation at `outputs/hardware/<app>-<YYYY-MM-DD>.md` containing: requirement summary, candidate filter table (which devices pass/fail each criterion), primary + fallback recommendation with spec tradeoffs, link/host compatibility note, approximate cost, and any requirement that no single device satisfies (forcing a compromise or multi-device setup).

## Decision points

- **If no single device covers the frequency range** → consider an upconverter/downconverter (e.g. Ham It Up for HF on RTL-SDR) or a multi-device setup.
- **If full-duplex is required** → eliminates HackRF; steers to USRP / Lime / BladeRF / Pluto.
- **If weak-signal-near-strong is the use case** → 8-bit devices will be limited; recommend 12-bit+ even at higher cost.
- **If embedded/portable** → favor PlutoSDR / RTL-SDR / LimeSDR Mini for size + power; USRP X-series is desktop/rack.

## Notes

- The classic starter is RTL-SDR (receive, ~24 MHz–1.7 GHz, 2.4 MHz BW, ~$30) — great for learning, limited for serious work.
- HackRF One is the versatile mid-tier (1 MHz–6 GHz, 20 MHz BW, half-duplex, 8-bit, ~$300) — wide range but limited dynamic range + half-duplex.
- USRP B2xx is the workhorse for serious work (12-bit, full-duplex, 56 MHz BW, USB 3.0) at higher cost.
- Don't over-buy: a spectrum monitor doesn't need a full-duplex 16-bit USRP. Match hardware to the actual RF problem.
