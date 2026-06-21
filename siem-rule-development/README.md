# SIEM Rule Development Workspace

> Detection engineering with the rigor of HF propagation prediction: every rule is a circuit, tuned to its Frequency of Optimum Transmission and triaged by decision tree.

## What This Workspace Does

This is a Claude Code workspace for **developing and tuning SIEM detection rules** — Sigma, Splunk SPL, Elastic EQL/KQL, Microsoft Sentinel KQL — built around one borrowed idea: a detection rule behaves like an HF radio circuit. It only "gets through" reliably when its operating point sits inside a usable window. Set the threshold too loose and the rule drowns in benign noise (a false-positive storm, then alert fatigue) — the detection equivalent of transmitting below the **Lowest Usable Frequency**. Set it too strict and real attacks skip over undetected — operating above the **Maximum Usable Frequency**. The job is to find that window and operate at the **Frequency of Optimum Transmission (FOT)**.

The workspace imports the quantitative discipline ionospheric propagation operators use — noise-floor characterization, required-SNR margins, diurnal/seasonal variation, solar/geomagnetic disturbance indices, and point-to-point prediction before you key the transmitter — and applies it to detection engineering. The build's technique is **decision-tree triage**: every alert is dispositioned through an explicit branching runbook (disturbance check → SNR margin → ATT&CK corroboration → entity criticality), and the branch path becomes tuning feedback for the rule that fired.

## Why This Workspace Exists

Most detection rules are deployed on intuition and tuned by complaint: an analyst drowns in false positives, someone loosens or mutes the rule, and real signal is lost with the noise. Detection engineering has the same structure as HF circuit planning — a noise floor, a usable window, reliability that varies by time of day and environment — but rarely the same rigor. This workspace codifies that rigor into a repeatable lifecycle so thresholds are *predicted and validated* before deployment, adapt to the daily cycle, and are retuned against root-caused environmental drift rather than guesswork.

## Getting Started

### Prerequisites

- A SIEM / log platform with historical query access (Splunk, Elastic, Microsoft Sentinel, or equivalent).
- [Sigma](https://github.com/SigmaHQ/sigma) + [pySigma / sigma-cli](https://github.com/SigmaHQ/pySigma) to author vendor-neutral rules and convert to your backend.
- [MITRE ATT&CK](https://attack.mitre.org/) as the coverage taxonomy (optionally the ATT&CK Navigator).
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) (optional) to generate known-bad markers for backtesting.

### Quick Start

1. Clone this workspace and open it in Claude Code.
2. Run `/draft-detection` for a target ATT&CK technique — it confirms telemetry and writes a Sigma rule with a provisional FOT band.
3. Run `/noise-floor` then `/threshold-band` to measure the benign floor and find the rule's usable LUF↔MUF window.
4. Run `/backtest-rule` to replay the rule against history — the go/no-go gate before production.
5. After deployment, disposition alerts with `/triage-tree` and watch for drift with `/space-weather` + `/tune-rule`.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/draft-detection` | Sigma-first rule + telemetry endpoints + provisional FOT band | Starting a new detection |
| `/noise-floor` | Benign event-rate floor and required SNR | Before tuning any threshold |
| `/diurnal-baseline` | Time-of-day / weekday adaptive baseline | When peak/trough ratio is high |
| `/threshold-band` | LUF/MUF window + FOT operating point | After the noise floor is known |
| `/propagation-forecast` | Reliability curve + blackout windows | Before deploy, to predict behavior |
| `/backtest-rule` | Replay vs historical logs; precision/recall | The production go/no-go gate |
| `/triage-tree` | Decision-tree triage runbook for an alert | Every alert disposition |
| `/space-weather` | K-index score for baseline-perturbing changes | After deploys / incidents |
| `/coverage-map` | ATT&CK coverage + blackout techniques | Coverage audits, gap planning |
| `/tune-rule` | Diagnose drift, retune to FOT | When a rule storms or goes silent |

## Directory Structure

```
siem-rule-development/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # 10 bespoke detection-engineering commands
├── context/
│   ├── concepts.md           # Detection + propagation taxonomy + the crosswalk
│   ├── workflows.md          # 8-phase lifecycle + the triage decision tree
│   └── references.md         # Crosswalk cheat-sheet, K-scale, log IDs, links
├── prompts/                  # 4 reusable prompt templates
└── outputs/                  # Rules, backtests, forecasts, triage records
```

## Example Use Cases

### Stand up a brute-force detection that won't storm
Draft a T1110 rule, characterize the failed-logon noise floor per hour-of-day, set the FOT just below the MUF, forecast the midday blackout window, and backtest against known password-spray activity — all before it touches production.

### Diagnose a rule that suddenly went quiet
A detection stops firing after an EDR rollout. `/space-weather` scores the rollout as a K5 disturbance; `/tune-rule` finds the baseline shifted the operating point above the MUF and resets it to a new FOT — with the rollout named as the root cause.

### Audit ATT&CK coverage and find the blackouts
`/coverage-map` separates genuinely covered techniques from "weak" cells (rules muted below their LUF) and true blackouts (no telemetry at all), then prioritizes the cheapest move to open each high-priority circuit.

## Recommended MCP Servers

- **Filesystem / Git MCP** — version detection rules and triage records in `outputs/` as a detection-as-code repo.
- **HTTP/fetch MCP** — pull live solar/geomagnetic and threat-intel feeds (NOAA SWPC, ATT&CK) to inform the space-weather analogy and coverage priorities.

## Legal & Ethical Considerations

- **Defensive use only.** This workspace authors detections and triage logic — not offensive tooling, not evasion guidance.
- **Log data is sensitive.** Production logs carry PII, credentials, internal hostnames, and IPs. Redact or synthesize before saving anything to `outputs/`; never commit live secrets or raw logs.
- **Authorization.** Backtesting and rule deployment should be run only against systems and log data you are authorized to monitor.

## Technical References

- [MITRE ATT&CK](https://attack.mitre.org/) — the technique taxonomy every rule maps to.
- [SigmaHQ](https://github.com/SigmaHQ/sigma) — vendor-neutral detection rule format + corpus.
- [Elastic detection-rules](https://github.com/elastic/detection-rules) — production EQL/KQL rules with unit tests.
- [Palantir ADS framework](https://github.com/palantir/alerting-detection-strategy-framework) — the Alerting & Detection Strategy template.
- [VOACAP Online](https://www.voacap.com/) — the HF propagation prediction model the workspace's discipline is borrowed from.
- [NOAA SWPC](https://www.swpc.noaa.gov/) — live solar flux and K/A geomagnetic indices (the "space weather" analogy's source).

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
