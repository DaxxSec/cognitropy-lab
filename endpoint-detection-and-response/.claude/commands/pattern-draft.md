# /pattern-draft — Draft Reproducible Detection Rules

Turn the most durable indicators of attack into detection rules — the "cutting pattern" that lets the SOC reproduce the detection on the next garment. Outputs portable Sigma plus the native EDR query.

## Inputs

- The reconstructed IOAs/TTPs (prefer behavioral over atomic — they survive cosmetic change).
- The telemetry source each behavior is visible in (Sysmon EID, EDR table, event log).
- Target platform(s) for the native query (Defender KQL, Elastic EQL, Splunk SPL, CrowdStrike).

## Steps

1. **Select durable IOAs**: favor parent-child process patterns, command-line structure, and sequence-of-events over hashes/IPs that an actor rotates cheaply.
2. **Specify the logic**: define the detection condition, the required telemetry fields, and the time/sequence window.
3. **Write Sigma**: author a valid Sigma rule (title, status, logsource, detection, condition, level, tags with ATT&CK IDs).
4. **Translate**: render the native query for each target platform.
5. **Estimate false-positive surface**: name the benign behaviors that resemble the rule and add tuning exclusions; suggest an Atomic Red Team test to validate.

## Output

`outputs/detections-<incident>-<date>.md`: one block per rule containing the Sigma YAML, the native-query translation(s), required telemetry source, ATT&CK mapping, false-positive notes, and a validation test reference.

## Notes

- A rule keyed on a hash or IP detects only this one wearing; key on behavior to catch the pattern.
- Document the telemetry prerequisite — a rule that needs unlogged data is a pattern with no cloth.
