# Detection From Threat Report

## Purpose

Turn a threat-intel report or a named ATT&CK technique into a deployable detection rule with explicit telemetry endpoints and a provisional FOT threshold band. Use at the start of the lifecycle, before any tuning.

## Prompt Template

```
You are a detection engineer building a SIEM rule, using the propagation-modeling
discipline in context/concepts.md (LUF/MUF/FOT, noise floor, required SNR).

Source material:

- **Threat report / behavior:** [PASTE REPORT OR DESCRIBE BEHAVIOR]
- **ATT&CK technique(s):** [e.g. T1059.001]
- **Available telemetry:** [Sysmon / EDR / Windows Security / cloud audit / proxy / DNS]
- **Target backend:** [Sigma → Splunk SPL / Elastic EQL / Sentinel KQL]
- **Known benign analogs:** [admin scripts, scanners, backup jobs, …]

Please:
1. Confirm which available telemetry actually carries this behavior (name the
   log source + fields). If none does, say so and stop — that's a blackout.
2. Choose the detection type (atomic / behavioral / threshold / correlation)
   and justify it against the Pyramid of Pain.
3. Write the Sigma rule (logsource, detection, condition) and the target-backend query.
4. List expected benign overlaps and a provisional LUF/MUF/FOT band to validate.
5. Map to ATT&CK and propose the backtest plan (window + known-bad source).
```

## Expected Output

- A named log source + required fields (the circuit endpoints), or an explicit blackout call.
- A Sigma rule + backend query.
- A provisional FOT band and a benign-overlap list.
- An ATT&CK mapping and a backtest plan ready for `/backtest-rule`.
