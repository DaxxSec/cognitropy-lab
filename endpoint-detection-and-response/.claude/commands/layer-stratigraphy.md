# /layer-stratigraphy — Order the Intrusion's Strata

Reconstruct the deposition order of an intrusion's components the way a conservator reads a garment's documented layers (shift → kirtle → gown → accessories): initial access → execution → persistence → privilege escalation → defense evasion → C2.

## Inputs

- The trusted-artifact set and provenance chains.
- Persistence telemetry (registry Run keys, services, scheduled tasks, WMI subscriptions, startup folders).
- Any known deletions (USN/$LogFile recovered) that mark missing strata.

## Steps

1. **Assign each artifact a stratum** by ATT&CK tactic (access, execution, persistence, priv-esc, evasion, C2).
2. **Order strata by deposition time**, corroborated against the trusted timeline — the bottom stratum is initial access.
3. **Recover negative impressions**: where a layer was deleted, infer its prior existence from references in surviving layers (a loader that calls a now-absent stage). Tag the inferred layer `INFERRED`.
4. **Map persistence mechanisms** and mark which strata survive a reboot — these are the ones that matter for containment.
5. **Draw the section diagram**: a vertical strata view from initial access to C2, with deposition timestamps and confidence per layer.

## Output

`outputs/stratigraphy-<incident>-<date>.md`: an ordered strata diagram (bottom = first deposited), a per-layer table (artifact · tactic · deposition time · survives-reboot · confidence), and a list of inferred-but-deleted layers.

## Notes

- Order of discovery ≠ order of deposition; never let query order set the strata.
- A gap between strata is a documented lacuna for `/reconstruct-timeline`, not something to paper over.
