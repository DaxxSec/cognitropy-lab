# SIEM Rule Development — Core Concepts

Background the agent reads before acting. This workspace develops SIEM detection rules **through the analytical lens of ionospheric HF propagation modeling**: a detection only "gets through" reliably when its operating point sits inside a usable window, the same way an HF circuit is only open when the working frequency sits between the LUF and the MUF. Optimised for fast recall, not exhaustive theory.

## The governing analogy

A radio operator planning an HF circuit does not just transmit and hope. They predict — for a given path, time of day, season, and solar/geomagnetic state — the band of frequencies that will actually carry signal above the noise, then operate at the **Frequency of Optimum Transmission (FOT)** inside that band. Detection engineering deserves the same discipline. A detection rule has an operating point (its threshold/sensitivity), a noise floor (the benign event rate), a required signal-to-noise margin, and a reliability that varies with the time of day and the state of the environment. Tune it like a circuit, not like a coin flip.

## Detection engineering taxonomy

- **Detection types** — *atomic/IOC* (hash, IP, domain — brittle, the base of the Pyramid of Pain), *behavioral* (sequences of actions, e.g. `whoami` after a service-creation), *threshold/aggregation* (N failed logons in M minutes), *anomaly/statistical* (deviation from a baseline), *correlation* (multiple analytics across sources).
- **Rule formats** — Sigma (vendor-neutral YAML, the lingua franca), Splunk SPL, Elastic EQL / KQL / ES|QL, Microsoft Sentinel KQL, Suricata (network), YARA (files), Snort.
- **MITRE ATT&CK** — the coverage map. Tactics → techniques (e.g. T1110 Brute Force, T1059 Command and Scripting Interpreter, T1078 Valid Accounts). Every rule should declare the technique(s) it detects.
- **The confusion matrix** — TP, FP, FN, TN. **Precision = TP/(TP+FP)** (how much of what fires is real), **Recall/TPR = TP/(TP+FN)** (how much of what is real fires). Alert fatigue is precision collapse: when FP load exceeds analyst capacity, *all* alerts get muted — the detection-engineering equivalent of a circuit dropping below the LUF.
- **Pyramid of Pain** (Bianco) — detecting TTPs costs the adversary more than detecting hashes/IPs. Prefer behavioral analytics over atomic IOCs where telemetry allows.

## Ionospheric HF propagation taxonomy

- **Layers** — D (60–90 km, daytime only, *absorbs* HF, worse at low freq, absorption ∝ 1/f²), E (90–150 km), F1 (150–220 km, daytime), **F2** (220–400 km, the main refractor, present day and night).
- **foF2 / critical frequency** — the highest frequency the F2 layer reflects at vertical incidence. Drives everything above it.
- **MUF (Maximum Usable Frequency)** — for a path, ≈ foF2 × obliquity (M-factor). **Above the MUF the signal penetrates the layer and escapes to space — the receiver hears nothing ("skip").**
- **LUF (Lowest Usable Frequency)** — **below the LUF, D-layer absorption and the noise floor swamp the signal — SNR too low to copy.**
- **FOT / OWF (Frequency of Optimum Transmission)** — ≈ 0.85 × MUF. The sweet spot: high enough to clear absorption, with margin below the MUF so normal day-to-day variation doesn't push the path closed.
- **Usable window** — `LUF < f < MUF`; FOT lives inside it.
- **Noise floor** — atmospheric (QRN), galactic, and man-made (QRM) noise the signal must exceed. Required **SNR** depends on the mode (CW needs little, SSB voice ~38–48 dB-Hz).
- **Solar drivers** — F10.7 cm flux (SFI) and Sunspot Number (SSN): higher → higher foF2 → higher MUF.
- **Geomagnetic disturbance** — K-index (0–9, per 3 h) and A-index. High K = geomagnetic storm = ionospheric disturbance, extra absorption, degraded (esp. polar) paths.
- **Transients** — Sporadic-E (Es): sudden intense E-layer ionization, unpredictable openings. Gray-line: enhancement along the dawn/dusk terminator. SWF/SID: short-wave fadeout from a solar flare.
- **Prediction tools** — VOACAP, ITU-R P.533 / REC533, ITURHFProp, proppy. They output MUF, **reliability (REL)** = the % of days the circuit SNR meets the required SNR, and predicted signal/SNR per hour.

## The crosswalk (the workspace's central model)

| HF propagation | SIEM detection |
|---|---|
| Circuit (TX → path → RX) | Detection (telemetry source → analytic → alert) |
| Operating frequency | Threshold / sensitivity (the operating point) |
| **MUF** — above it, signal skips over, no copy | **Max usable threshold** — above it, rule too strict → false negatives |
| **LUF** — below it, absorbed into noise | **Min usable threshold** — below it, drowned in benign noise → FP storm, then alert fatigue |
| **FOT (≈0.85×MUF)** | **Optimum threshold band** — best precision with margin against drift |
| foF2 / critical frequency | Detectability of the technique in the available telemetry |
| Noise floor (QRN/QRM) | Benign baseline event rate (the alert noise floor) |
| Required SNR for the mode | Required separation between malicious signal and benign noise |
| Reliability (REL %) | Detection reliability — fraction of attack instances that fire across conditions (recall over time) |
| D-layer absorption (daytime, ∝1/f²) | Alert-storm / high-volume windows that bury true positives |
| Diurnal & seasonal variation | Business-hours / maintenance-window / seasonal event-rate variation → time-aware thresholds |
| Solar flux (SFI / SSN) | Environment "energy": fleet growth, new log sources, active campaigns raising baselines |
| K-index / geomagnetic storm | Operational disturbance (incident, outage, mass change) that wrecks baselines |
| Sporadic-E (transient opening) | Transient anomaly — a one-off spike that briefly makes a quiet rule fire |
| Gray-line enhancement | Shift-change / window-boundary effects where detection behavior shifts |
| VOACAP point-to-point prediction | Backtest / replay a rule against historical logs before deployment |
| Frequency-selection decision tree | **Alert-triage decision tree** (this build's technique) |

## The quantitative bridge — required SNR → FP rate

The propagation framing is not just a metaphor; it gives a usable estimator. For a threshold-style rule keyed on a count metric:

- Let the per-bucket benign floor have center `μ` and robust spread `σ` (use median + MAD, where `σ ≈ 1.4826 × MAD`, robust to spikes).
- Set the operating point (threshold) at `T = μ + k·σ`. The multiplier **k is the SNR margin** — the radio analog of "dB above the noise floor."
- Expected FP load per bucket falls roughly as the tail beyond `k`: at `k≈3` you clear ~99.7% of a well-behaved floor; at `k≈4.5`, ~99.999%. The **LUF** is the smallest `k` whose summed tail across all buckets still fits the FP budget; the **MUF** is the largest `k` at which known-bad still exceeds `T` (recall holds). The **FOT** sits ~15% below the MUF in `k`-space.
- Two corollaries: (1) because `μ` and `σ` vary by hour-of-day, a single global `k` is wrong at peak and trough — hence `/diurnal-baseline`; (2) raising the floor (more telemetry, fleet growth) lifts `μ` and pushes a fixed `T` below its LUF → the rule storms. That is drift, and it is predictable.

## Rule lifecycle states (circuit states)

Every detection is in exactly one state; transitions are the work this workspace tracks:

| State | Circuit analog | Meaning |
|---|---|---|
| **Draft** | Antenna not yet raised | Logic written, telemetry confirmed, threshold provisional |
| **Backtested** | Path predicted (VOACAP run) | Replayed on history; precision/recall + FP budget verified |
| **Deployed (at FOT)** | Circuit open | Live, operating at the optimum point with a diurnal baseline |
| **Drifting** | Path closing | Storming (below LUF) or going silent (above MUF) — needs retune |
| **Blackout** | Band closed | No usable telemetry; no threshold helps (a coverage gap, not a tuning gap) |
| **Retired** | Frequency abandoned | Permanently muted or superseded; removed from the inventory |

## Common failure modes

- **Tuning to the mean, not the tails** — a threshold that works at the average event rate storms during the daily peak and goes blind at the trough. Picking a frequency good at noon that's dead at midnight. Always quote the diurnal envelope.
- **Static thresholds on a non-stationary baseline** — no diurnal baselining → FP storms at peak hours, blind spots overnight.
- **Deploying without a noise floor** — unknown benign rate → unknown SNR → unpredictable FP load on day one.
- **Chasing the MUF** — over-tightening to kill the last false positives until recall collapses (operating above the MUF, "signal skips over").
- **Stuck below the LUF** — a rule so loose it lives permanently in the noise; analysts mute it (alert fatigue) and real signal is lost with it.
- **No prediction before deployment** — skipping the backtest/forecast → the rule storms production unannounced.
- **Baseline poisoning during a storm** — re-baselining during an incident or outage bakes the disturbance into "normal," exactly like calibrating a propagation prediction during a geomagnetic storm.

## Operating constraints

- **Defensive use only.** This workspace produces detections and triage logic. It is not for offensive tooling or evasion.
- **Treat log data as sensitive.** Logs carry PII, credentials, internal hostnames, and IPs. Never paste raw production logs or live secrets into `outputs/` — redact, summarise, or synthesize.
- **Reproducibility.** Every backtest and forecast must pin the log time window, the data-source/index versions, and the rule version. A reliability number without its window is a point estimate in disguise.
