---
name: stray-light-audit
description: Identify ghost images, scatter paths, and baffle gaps in the current design.
---

# /stray-light-audit

## Steps
1. **Enumerate surfaces**: every optical surface, every mechanical surface in the optical path, window exterior, baffles, vanes.
2. **Critical objects**: surfaces the detector can see (forward trace from detector).
3. **Illuminated objects**: surfaces the source can illuminate (forward trace from source / scene).
4. **Intersect**: the set seen by BOTH = **first-order scatter paths** — the highest-risk offenders.
5. **For each first-order path**, compute:
   - Geometrical config factor (GCF)
   - Assumed BRDF (use `resources/brdf-defaults.md`: black anodize, Acktar, Z306, bare aluminum)
   - Transmitted scatter power / detector signal → flare ratio
6. **Mitigations**: propose baffles, vanes, aperture stops relocation, coating upgrades.
7. **Verify**: cross-check ghost images for refractive systems (first-two surface back-reflection).

## Outputs
- `outputs/stray-light-paths.csv` — paths with GCF, BRDF, flare ratio
- `user-docs/stray-light-report.md` — narrative
- FMEA update: each high-flare path becomes a mode

## Notes
- Non-sequential ray-trace tools (FRED, LightTools, TracePro) do this natively. If user has one, recommend use. If not, the hand analysis above catches 80% of offenders.
