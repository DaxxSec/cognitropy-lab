# motorcade-config-decision

## Purpose

Use when finalizing the motorcade configuration for a trip increment. Structures the decision against threat tier, available assets, route topology, and jurisdictional rules.

## Prompt Template

```
Acting as the advance planner finalizing motorcade configuration for a trip increment.

Increment context:

- **Trip + increment ID:** [VALUE]
- **Threat tier (for this increment):** [T1-T4]
- **Protectee characteristics:** [single principal / delegation / family present / medical considerations]
- **Visit visibility:** [overt / low-profile]
- **Origin → destination route summary:** [primary route name, distance, estimated transit time]
- **Route topology:** [high civilian density urban / open road / tunnel-bridge intensive / parade route]
- **Available own assets:** [vehicle count, agent count, CAT availability]
- **Available host-nation assets:** [escort vehicle count, motorcycle officers, military if applicable]
- **Available medical:** [co-located / standoff EMS / air-EMS standby]
- **Jurisdictional rules:** [host-nation weapons-in-vehicles, vehicle type restrictions, escort-speed limits]
- **Hospital pre-positioning band (per /route-recon-report):** [Excellent / Good / Acceptable / Marginal / Unacceptable]

Please:
1. Select base motorcade template from references.md per threat tier; document rationale.
2. Adjust for route topology — what specific modifications to base template?
3. Adjust for protectee characteristics — delegation / family / medical implications?
4. Adjust for visibility profile — what configuration changes for low-profile vs overt?
5. Adjust for available-vs-required assets — flag gaps and propose remediation (request augmentation? restructure increment?).
6. Identify deviation triggers — what would cause an upgrade mid-trip (threat-tier escalation, comms loss, etc.)?
7. Recommend rehearsal scope — what specifically needs to be rehearsed?
8. Identify named POCs in jurisdiction matrix who must agree to the configuration.
```

## Expected Output

- Selected base motorcade template
- Adjustments table per axis (topology, protectee, visibility)
- Asset gap analysis + remediation proposal
- Deviation triggers
- Rehearsal scope
- POC sign-off requirements

## Notes

- Motorcade configuration must be signed off by Detail Leader + RSO + host-nation liaison before activation.
- Rehearsal is non-negotiable for new formations or new routes; do not skip under time pressure.
- Configuration changes mid-trip require explicit authorization from the documented decision authority (typically Detail Leader).
- Document the actual configuration in the deviation log if it diverges from planned (and revise plan for next-trip baseline).
