# /plan-extraction

Choose the extraction method — logical, full file system (FFS), agent-based, or checkm8 — that the device, lock state, and legal authority actually permit, and produce an acquisition plan. Frame the choice as a hypothesis: "Method X will yield the data class the question needs."

## Inputs

- Device profile (`/identify-device`) and lock-state assessment (`/assess-lock-state`).
- The investigative question / data of interest (Messages? app sandbox? Health? deleted records?).
- Legal scope and available tooling (open vs. commercial).
- Passcode condition.

## Steps

1. Filter methods by **feasibility**: strike anything the SoC/iOS/state forbids (e.g. FFS on BFU; checkm8 on A12+).
2. Filter by **sufficiency**: does the candidate yield the data class the question needs? (Logical/unencrypted misses sandbox + Keychain; encrypted backup adds Keychain/Health; FFS adds system DBs.)
3. Choose the **least-invasive sufficient** method; if logical is the only option, prefer an **encrypted** backup for the extra data.
4. Write the acquisition steps, including the explicit rule **"do not reboot"** for AFU and the order of operations.
5. State the expected completeness (which Data Protection classes you expect to unwrap) so `/verify-extraction` has a target.

## Output

`outputs/extraction-plan-YYYY-MM-DD.md`: chosen method + rationale, rejected methods + reasons, step-by-step acquisition procedure, tool + version to use, expected class coverage, and risks/mitigations.

## Notes

- Least-invasive that answers the question — not the most complete possible. Scope and minimisation matter legally.
- If two methods tie on data but differ on risk to state, pick the one that preserves AFU longest.
