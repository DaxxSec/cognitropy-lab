# Tools & Integrations

How the agent interacts with the external SDR + analysis tooling. The agent does not retype these commands from memory — it consults this file.

## SDR Capture Commands

### HackRF One
```
hackrf_transfer \
    -f <center_hz> \
    -s <sample_rate_hz> \
    -a 0 \
    -l <lna_gain_0_to_40_step8> \
    -g <vga_gain_0_to_62_step2> \
    -r <out.iq> \
    -n <total_samples>
```
Max sample rate ~20 MS/s usable; instantaneous BW ~20 MHz. Not enough for full Bluetooth-Classic analysis; use for narrowband ISM.

### USRP B210 / X310
```
uhd_rx_cfile \
    -f <center_hz> \
    -r <sample_rate_hz> \
    -g <gain_db> \
    -A "TX/RX" \
    -N <total_samples> \
    <out.iq>
```
B210 = 56 MS/s real-time; X310 = 200 MS/s with a 10 GbE host. X310 is the right choice for full-band 2.4 GHz Bluetooth Classic capture.

### BladeRF 2.0
```
bladeRF-cli -e "set frequency rx <hz>; set samplerate rx <hz>; set bandwidth rx <hz>; set gain rx <db>; rx config file=<out.iq> format=bin n=<samples>; rx start; rx wait; rx stop"
```

## Channelization

Use the workspace's `resources/bayesian-likelihood-models.md` reference implementation. It provides:

- `channelize_pfb(iq, fs, K, channel_bw, taps)` — polyphase filterbank → `(T, K)` energy matrix
- `channelize_fft(iq, fs, fft_size, hop_size)` — FFT-based, simpler but more leakage; use for quick triage
- `compute_energies(channels, integration_window)` — windowed energy detector

## GR-Bluetooth (calibration ground truth)

```
git clone https://github.com/greatscottgadgets/gr-bluetooth
cd gr-bluetooth && mkdir build && cd build && cmake .. && make && sudo make install
```

Validate with:
```
gr_btclassify --input-file calibration.iq --sample-rate 80000000
```
Output: list of identified Bluetooth Classic packets with LAP, channel, timestamp. The agent uses this as ground truth to validate the Bayesian dehopper's MAP path.

## URH (downstream demodulation)

After `/dehop-bayes` produces `dehopped.iq` (single-channel, decimated to channel BW):

```
urh --capture dehopped.iq --sample-rate <channel_bw>
```
Use URH's modulation analyser, then auto-decode preamble/sync/CRC.

## PyMC Inference

The workspace uses PyMC 5+ for the hyperparameter posterior. Reference model in `resources/bayesian-likelihood-models.md`. Key pattern:

```python
import pymc as pm
import numpy as np

with pm.Model() as fhss_model:
    log_R_h = pm.Uniform("log_R_h", lower=0, upper=5)   # log10 hops/s
    R_h = pm.Deterministic("R_h", 10**log_R_h)
    duty = pm.Beta("duty", alpha=8, beta=2)              # T_d / (T_d + T_g)
    K = pm.Categorical("K", p=K_prior)

    # Marginalised likelihood over c_t (Viterbi-equivalent)
    pm.Potential("loglik", forward_loglik(energies, R_h, duty, K))

    trace = pm.sample(2000, tune=1000, chains=4)
```

`forward_loglik` is a numba-compiled forward-pass HMM likelihood. Don't try to write it inline in PyMC's symbolic graph — it won't compile.

## File / Pickle Conventions

- IQ captures: `.iq` raw + `.sigmf-meta` sidecar
- Posteriors: `outputs/<engagement>/posterior.npz`
- MAP path: `outputs/<engagement>/channel_path.npy`
- Reports: `outputs/<engagement>/report.md`

Never pickle PyMC traces directly across versions; export with `arviz.to_netcdf` for portability.

## Plotting

Use `arviz.plot_posterior` for hyperparameters and a custom spectrogram-overlay function (in `resources/`) for the per-dwell channel posterior. Save to `outputs/<engagement>/figs/`.

## When a tool is unavailable

If the user lacks any of the above (no GPSDO, no URH installed, no PyMC), the agent must:

1. Note the limitation in `work-log/` for the current session.
2. Suggest the cheapest substitute (FFT channelizer instead of PFB; SciPy MAP optimisation instead of full PyMC NUTS).
3. Flag the report's credibility intervals as "approximate" rather than "Bayesian".

Never silently degrade — always surface the substitution.
