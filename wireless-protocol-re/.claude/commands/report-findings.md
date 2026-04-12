# /report-findings — Generate RE Findings Report

Generate a structured reverse engineering report for documentation, sharing, or responsible disclosure.

## Required Inputs
- Target device/signal description
- All analysis performed
- Key findings and conclusions

## Report Sections

1. **Executive Summary** — Target ID, key findings, risk assessment, recommendations
2. **Target Profile** — Device description, FCC ID, manufacturer specs, frequency/power
3. **Signal Characteristics** — Frequency, bandwidth, modulation, symbol rate, pattern, power
4. **Protocol Specification** — Frame structure, field descriptions, CRC, state machine, timing
5. **Analysis Methodology** — Hardware, software, capture params, techniques, optimization approach
6. **Security Assessment** (if applicable) — Encryption, replay vulnerability, authentication, improvements
7. **Appendices** — Capture file refs, flowgraphs, scripts, full decode examples

Save to `outputs/re-report-{target}-{date}.md`.
