# /draft-detection

Draft a new SIEM detection rule (Sigma-first) for a target behavior, declaring its telemetry endpoints and a provisional FOT threshold band — Phase 1 (path survey) of the lifecycle.

## Inputs

- Target behavior or ATT&CK technique ID (e.g. T1110.001 Password Guessing).
- Available log sources / telemetry (Sysmon, EDR, Windows Security, cloud audit, proxy…).
- Target platform/backend (Sigma → Splunk SPL / Elastic / Sentinel KQL).
- Known benign analogs of the behavior (admin scripts, vuln scanners, backup jobs).

## Steps

1. Read `context/concepts.md` (taxonomy) and confirm the technique is *carried* by an available source — no telemetry, no circuit. If absent, stop and route to `/coverage-map`.
2. Pick the detection type (atomic / behavioral / threshold / correlation) using the Pyramid of Pain — prefer behavioral/TTP over IOC where telemetry allows.
3. Write the Sigma `detection:` logic with explicit `logsource`, required fields, and a `condition`.
4. Declare the "endpoints": exact log source + fields the rule depends on, so coverage gaps are visible.
5. Set a *provisional* threshold band (LUF/MUF/FOT) from first principles; mark it as un-validated pending `/threshold-band`.
6. Map the rule to ATT&CK tactic/technique and note expected benign overlaps for later FP triage.
7. Stub the backtest plan (which historical window, which known-bad source) for `/backtest-rule`.

## Output

`outputs/detect-<technique>-YYYY-MM-DD.yml` (the Sigma rule) plus a sibling `.md` metadata card: ATT&CK mapping, log-source endpoints, provisional FOT band, benign-overlap notes, and the backtest plan.

## Notes

- A rule that cannot name its log-source endpoints is not ready — that's an open circuit with no antenna.
- Keep IOC-only rules clearly labeled; they decay fast (bottom of the Pyramid of Pain).
