# SIEM Rule Development — Reference Tables

Compact lookup data. Defer to the upstream catalogues for fuller specs.

## Propagation ↔ detection quick crosswalk

| Propagation term | Detection meaning | Operating rule of thumb |
|---|---|---|
| MUF | Strictest threshold before recall drops | Stay below it or you miss real attacks |
| LUF | Loosest threshold before FP load blows budget | Stay above it or analysts mute the rule |
| FOT | Chosen operating point (≈0.85×MUF) | Default deploy point; strict + margin |
| Noise floor | Benign baseline event rate | Measure before tuning, never after |
| REL % | Detection reliability over conditions | Quote with its time window |
| K-index | Environmental disturbance score | Freeze baselines while K is high |

## Required-confidence → action (SNR-margin analog)

| Deviation vs diurnal baseline | Triage analog | Default action |
|---|---|---|
| < 1·MAD | Below LUF — in the noise | Close-benign, flag for re-baseline |
| 1–3·MAD | Marginal, near FOT | Enrich + queue for analyst |
| 3–6·MAD | Clear signal | Escalate if any corroboration (Q3) |
| > 6·MAD | Strong, well above floor | Escalate; treat as incident candidate |

## Environment disturbance scale (K-index analog)

| Score | Condition | Baseline action |
|---|---|---|
| K0–K2 | Quiet — routine ops | Normal baselining |
| K3–K4 | Active — minor deploy / patch window | Tag affected rules; baseline cautiously |
| K5–K6 | Minor storm — large change / partial outage | Freeze re-baselining on affected sources |
| K7–K9 | Severe storm — major incident / mass change | Full baseline freeze; expect FP surges; do not retune |

## Common Windows detection log sources

| Event ID | Source | Detects |
|---|---|---|
| 4624 / 4625 | Security | Successful / failed logon (T1110, T1078) |
| 4688 | Security | Process creation (command-line if enabled) |
| 4672 | Security | Special privileges assigned (admin logon) |
| 4720 / 4732 | Security | Account created / added to privileged group |
| 1 (Sysmon) | Sysmon | Process creation w/ hashes, parent, cmdline |
| 3 (Sysmon) | Sysmon | Network connection |
| 7 / 8 (Sysmon) | Sysmon | Image load / CreateRemoteThread (injection) |
| 11 (Sysmon) | Sysmon | File create |
| 4104 | PowerShell | Script-block logging (T1059.001) |

## Upstream catalogues — detection

- **MITRE ATT&CK** — https://attack.mitre.org/ — the technique taxonomy every rule maps to.
- **SigmaHQ rules** — https://github.com/SigmaHQ/sigma — vendor-neutral detection rule corpus.
- **pySigma / sigma-cli** — https://github.com/SigmaHQ/pySigma — convert Sigma to SPL/KQL/EQL backends.
- **Elastic detection-rules** — https://github.com/elastic/detection-rules — production EQL/KQL rules + unit tests.
- **Splunk security_content (ESCU)** — https://github.com/splunk/security_content — analytic stories + SPL.
- **MITRE CAR** — https://car.mitre.org/ — Cyber Analytics Repository, pseudocode analytics.
- **Palantir ADS framework** — https://github.com/palantir/alerting-detection-strategy-framework — the Alerting & Detection Strategy template.
- **Atomic Red Team** — https://github.com/redcanaryco/atomic-red-team — known-bad generators for backtesting (Phase 5).
- **Sysmon config (SwiftOnSecurity)** — https://github.com/SwiftOnSecurity/sysmon-config — telemetry baseline.
- **Pyramid of Pain (Bianco)** — http://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html

## Upstream catalogues — propagation (the borrowed rigor)

- **VOACAP Online** — https://www.voacap.com/ — point-to-point HF prediction (MUF, REL, SNR per hour).
- **NOAA SWPC** — https://www.swpc.noaa.gov/ — live solar flux, K/A indices, space-weather alerts.
- **ITU-R P.533** — https://www.itu.int/rec/R-REC-P.533/ — the HF propagation prediction recommendation.
- **proppy / ITURHFProp** — https://soundbytes.asia/proppy — open ITU-R P.533 implementation.

## Cheat-sheet — FOT default
`FOT ≈ 0.85 × MUF`. In detection terms: pick the strictest threshold that still passes backtest recall (the MUF), then back off ~15% toward sensitivity so normal diurnal variation does not push the rule above its MUF and blind it.
