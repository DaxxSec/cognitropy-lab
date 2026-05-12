# Reference — Channelizer Design Notes

The polyphase filterbank (PFB) at the heart of the FHSS analyser turns one wideband IQ stream into K narrowband channel streams. Picking the wrong filter parameters silently degrades every downstream posterior. This document captures the design choices that matter and the reasons.

## 1. Why a PFB and not K parallel mixers + LPFs?

Computational cost. K parallel mixer-and-decimate operations cost `O(K * N)` per input sample. A PFB reduces this to `O(K * log K * N)` for an FFT-based PFB or `O(K * M)` for a tap-`M` PFB, where M is filter length per leg (typically ~20 for modest K, vs. N samples for the full convolution).

For 79-channel Bluetooth-Classic at 80 MS/s: parallel mixers ≈ 6.3 GOps/s; PFB ≈ 100 MOps/s. PFB is the only way to keep up in real time on a typical workstation.

## 2. Channel BW = modulated BW + guard

Set channel BW to the modulated bandwidth plus a guard. For Bluetooth Classic GFSK at 1 Mbps with modulation index 0.32, occupied BW ≈ 1 MHz; channel grid is at 1 MHz spacing with 0 guard, so the right channel BW is exactly 1 MHz.

For systems with overlapping channels (rare in practice), increase guard to allow rejection of the adjacent channel. For systems with explicit guard intervals (most mil systems), set channel BW to occupied BW only.

**Mistake to avoid:** setting channel BW too narrow truncates the signal and reduces SNR; setting it too wide invites adjacent-channel leakage.

## 3. Filter prototype design

Three choices: window method, Parks-McClellan equiripple, Kaiser. The dehopper uses Parks-McClellan equiripple because it gives the cleanest stop-band:

```python
import scipy.signal as sig
N = 1024  # filter length per leg
attenuation_db = 60
transition_bw = 0.1  # in fractional Nyquist
taps = sig.remez(N, [0, 0.5 - transition_bw, 0.5, 1.0],
                 [1, 10**(-attenuation_db/20)],
                 weight=[1, 100])
```

**60 dB stop-band rejection is the floor.** At 50 dB, leakage from the active channel into adjacent channels is enough to fool the energy detector at low SNR.

**1024 taps is the floor for K = 79 channels.** Fewer taps blur the channel boundaries; more taps don't help significantly past 1024.

## 4. Window choice (FFT-based PFB)

If using an FFT-based PFB rather than a tap-array PFB, the window dominates leakage:

| Window | Sidelobe (dB) | Main lobe width | Leakage trade-off |
|--------|--------------:|----------------:|-------------------|
| Rectangular | -13 | narrowest | terrible — adjacent-channel ghost detections |
| Hann (Hanning) | -32 | moderate | OK for high-SNR |
| Blackman | -58 | wider | good |
| Blackman-Harris | -92 | widest | excellent, recommended |

Default: Blackman-Harris.

## 5. Integration window (per-dwell energy)

The energy detector integrates `|channel|^2` over `N_int` samples per dwell:

```
N_int = round(0.8 * dwell_samples)
```

The 0.8 factor leaves a margin for guard intervals and dwell-edge ambiguity. Specifically:

- Too short (`N_int << dwell_samples`) → noisy estimate, wide per-dwell posterior.
- Too long (`N_int >= dwell_samples`) → smear across hop boundary, posterior bias.

After `/dwell-estimate` produces a tight posterior on `T_d`, **re-run `/dehop-bayes` with the updated `N_int`**. This is the dominant accuracy improvement after first-pass dehopping.

## 6. Decimation factor

The PFB decimates by `K` (one sample per channel per `K` input samples). For Bluetooth Classic at 80 MS/s and K = 79:

```
sample_rate_per_channel = 80e6 / 79 ≈ 1.01 MS/s
samples_per_dwell = 1.01e6 * 625e-6 ≈ 633 samples/dwell
```

Comfortable. Plenty of samples to integrate.

For a system with more channels (Bluetooth + adjacent ISM at 5 MHz spacing → 16 channels at 80 MS/s = 5 MS/s/channel), check that samples-per-dwell ≥ 50 — fewer and the energy detector becomes noisy.

## 7. Boundary alignment

The PFB places channel centers at `f_center + (k - K/2) * channel_BW`. Verify this matches the target system's channel grid:

- Bluetooth Classic: channel 0 at 2402 MHz, 1 MHz spacing → tune SDR to 2441.5 MHz, K = 79
- BLE: channels are at irregular offsets (0–36 plus 37, 38, 39); use a non-uniform PFB or a uniform PFB with mapping.
- WMBus mode N: 8 channels at 12.5 kHz spacing starting at 169.40625 MHz.

If the PFB grid is misaligned by even half a channel, signal energy spreads across two adjacent channels and the dehopper sees ghost hops.

## 8. Real-world pitfalls

### LO drift
SDR LO at room temperature drifts ~1 ppm/°C over short timescales. At 2.4 GHz, 1 ppm = 2.4 kHz, which is small compared to 1 MHz Bluetooth channel BW. But over a 1-hour capture, drift can reach 50–100 kHz, enough to bias the channelizer slowly. **Use GPSDO**.

### DC spike (zero-IF SDRs)
HackRF and BladeRF have a DC IQ-imbalance spike at the LO frequency. The PFB will show a bright ghost channel at the DC frequency. Either tune off-center (bias the LO 5–10 MHz away) or filter out the DC bin in post.

### Image rejection
Single-conversion SDRs reject the image by ~50–60 dB. If the target band is near a strong out-of-band signal that gets imaged in, the channelizer will see it as a fake hop. Use a SAW filter on the input.

### Quantization noise
HackRF is 8-bit ADC; USRP B210 is 12-bit; X310 is 14-bit. At low SNR, 8-bit quantization noise is the floor. Bluetooth analysis at -90 dBm receive levels needs ≥ 12-bit ADC.

## 9. Validation

Always validate the channelizer with a known-tone test:

```
1. Inject a CW tone at known frequency `f_tone` near a target channel center.
2. Run PFB. Verify:
   - Channel containing f_tone has > 30 dB more energy than adjacent channels.
   - Adjacent-channel leakage matches the filter's stop-band rejection.
3. If leakage exceeds the filter spec, the PFB has a bug — usually wrong channel BW or wrong taps.
```

Run this validation any time the channelizer parameters change.

## 10. Reference flowgraph

A complete GR flowgraph for the dehopper is in `cognitropy-server/` (not part of this workspace). The flowgraph chains: file source → IQ-rate-conversion → PFB → energy detector → channel-energy file sink. The Bayesian inference runs offline on the energy file output.
