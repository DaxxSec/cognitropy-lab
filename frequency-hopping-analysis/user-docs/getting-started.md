# Getting Started — Frequency Hopping Analysis Workspace

This is a hands-on quick start for an RF analyst who has never used a Bayesian dehopper. By the end you'll have a calibrated environment and a confident analysis of one Bluetooth Classic capture.

## What you need

- An SDR with ≥ 80 MHz instantaneous bandwidth (USRP B210 or X310 strongly preferred). HackRF works for narrowband or partial-band study only.
- A modern smartphone (any Bluetooth source).
- Python 3.10+, with the dependencies listed in `context/for-agent/environment.md`.
- ~10 GB free disk space.
- 30 minutes for the first calibration run.

## Step 1 — Workspace onboard

```
cd /path/to/frequency-hopping-analysis
claude
> /onboard
```

The agent walks you through hardware, target, hypotheses, authorisation, and writes the context files. About 5 minutes.

## Step 2 — Calibration

This step is mandatory. Without calibration, the analyser produces confidently-wrong posteriors.

1. Put your phone in Bluetooth pairing mode within 3 m of the antenna.
2. Run the capture command (the agent will print exact syntax for your SDR; for B210):

```
uhd_rx_cfile -f 2441500000 -r 80000000 -g 40 -A "TX/RX" \
             -N 80000000 outputs/calibration-2026-05-06/calibration.iq
```

3. Write the SigMF sidecar (the agent has a template):

```
echo '{
  "global": {
    "core:datatype": "ci16_le",
    "core:sample_rate": 80000000,
    "core:hw": "USRP B210",
    "core:author": "<your-name>",
    "core:description": "Bluetooth Classic calibration capture"
  },
  "captures": [{
    "core:sample_start": 0,
    "core:frequency": 2441500000,
    "core:datetime": "2026-05-06T10:00:00Z"
  }],
  "annotations": []
}' > outputs/calibration-2026-05-06/calibration.sigmf-meta
```

4. Run the calibration pipeline:

```
> /hop-detect outputs/calibration-2026-05-06/calibration.iq
> /hop-set-prior --system bluetooth-classic
> /dehop-bayes outputs/calibration-2026-05-06/calibration.iq
> /sequence-id --system bluetooth-classic
```

5. Cross-validate with gr-bluetooth:

```
gr_btclassify --input-file outputs/calibration-2026-05-06/calibration.iq \
              --sample-rate 80000000 \
              > outputs/calibration-2026-05-06/gr-bluetooth-output.txt
```

6. The agent will compare its MAP path to gr-bluetooth's hop sequence and write `calibration-report.md`.

**Pass criteria** (any failure → don't proceed):
- P(hopping) > 0.95
- Hop rate posterior peaked in [1590, 1610] hops/s
- K = 79 with > 0.9 mass
- Sequence type = "table" > 0.7
- Per-dwell agreement with gr-bluetooth > 90%

## Step 3 — Read the calibration report

```
cat outputs/calibration-2026-05-06/calibration-report.md
```

Things to notice:

- Every parameter is reported as a **posterior**, not a point estimate, with a 95% credibility interval.
- The report says how confident the analyser is — which directly translates to how much you should trust it.
- The cross-validation against gr-bluetooth is the *only* objective ground-truth check the workspace has. Don't skip it.

## Step 4 — Your first unknown signal

After calibration passes, you can analyse an unknown signal with confidence the analyser is working.

```
> Use the unknown-fhss-triage prompt with my capture <path>
```

The agent triages the capture, identifies likely systems, and either:
- Runs the full analysis pipeline if confident, or
- Recommends extending the capture / changing parameters.

Always read the agent's recommendation; don't blindly accept the dehopped output.

## What to do if the agent gives a confident answer that smells wrong

- Check the calibration evidence linked in the report. If it failed, posteriors are unreliable.
- Re-run `/dehop-bayes` with `--seq unknown` to widen the prior and see if the posterior shifts.
- Compare against `resources/known-fhss-systems.md` — does the recovered hop rate match a known system?
- If posterior on K is exactly equal to the SDR's number-of-channels-in-band, your capture didn't cover the full hop range. Re-capture wider.

## Where to go next

- `user-docs/why-bayes-for-fhss.md` — tutorial on why MLE fails on hopping signals
- `context/for-agent/domain-knowledge.md` — full FHSS theory + Bayesian model derivations
- `resources/bayesian-likelihood-models.md` — code references for the dehopper internals
