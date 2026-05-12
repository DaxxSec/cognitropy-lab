# Prompt — Bluetooth Classic Calibration Run

Use this prompt to run the mandatory calibration before any unknown-signal analysis. Calibration validates that the workspace's Bayesian dehopper recovers ground truth on a known signal.

```
Run a full calibration on Bluetooth Classic.

Setup:
  - Phone in Bluetooth pairing mode within 3 m of the SDR antenna.
  - SDR: USRP B210 or X310 strongly preferred (need ≥ 80 MHz instantaneous BW for full 79-channel coverage). HackRF will work for partial-band (covers ~20 MHz at a time, will only see ~25% of channels).

Capture:
  - Center: 2.441 GHz
  - Sample rate: 80 MS/s
  - Duration: 1 second
  - Gain: 40 dB
  - Output: outputs/calibration-<YYYY-MM-DD>/calibration.iq + .sigmf-meta

Analysis:
  1. /hop-detect calibration.iq
     - Expect: P(hopping) > 0.95
     - Expect: hop rate posterior peaked in [1590, 1610] hops/s
  2. /hop-set-prior --system bluetooth-classic
     - Expect: K = 79, channel grid 2402–2480 MHz at 1 MHz spacing
  3. /dehop-bayes calibration.iq
     - Expect: per-dwell quality > 0.7 for >= 95% of dwells
  4. /sequence-id --system bluetooth-classic
     - Expect: P(s = "table") > 0.7
     - Expect: at least one LAP recovered
  5. Cross-validate against gr-bluetooth ground truth:
     - Run gr_btclassify on the same capture.
     - Compare hop sequence agreement: expect > 90% per-dwell match between Bayesian dehopper MAP path and gr-bluetooth output.

Output:
  - outputs/calibration-<YYYY-MM-DD>/calibration-report.md
  - outputs/calibration-<YYYY-MM-DD>/calibration.json (summary numbers)

Pass criteria: ALL of the above. If ANY fail, do not proceed to unknown-signal analysis. Re-run with diagnostics:
  - Check antenna gain and distance
  - Check SDR clock (use GPSDO if drift suspected)
  - Check PyMC convergence (R-hat < 1.01, ESS > 400)

The calibration directory is referenced by future engagements via outputs/<engagement>/calibration.json.
```

## Why this is mandatory

Calibration is the only honest way to know whether the analyser is broken. A Bayesian model can produce a tight posterior on the wrong answer if the prior or likelihood is misspecified — without ground truth, there's no way to detect that. Bluetooth Classic gives ground truth via gr-bluetooth.

## Frequency of re-calibration

Run a fresh calibration:

- After any SDR hardware change (different unit, different antenna)
- After any PyMC / numpy / Python version change
- After any change to `resources/bayesian-likelihood-models.md`
- At the start of every new physical environment
- At minimum, every 24 h during continuous operation
