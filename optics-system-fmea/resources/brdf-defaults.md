# BRDF Reference Defaults

Use these values when the user does not have measured BRDF data. Validate against vendor datasheet for final design.

| Material | BRDF @ 30° (1/sr) | Notes |
|---|---|---|
| Acktar Magic Black | 0.005 | Vacuum-compatible, low outgassing |
| Vantablack VBx2 | 0.0001 | Best available, fragile, expensive |
| Chemglaze Z306 (black paint) | 0.015 | Widely used in space |
| Martin Optical black | 0.01 | Space-qualified |
| Anodize black (commercial) | 0.05 | Cheap, adequate for VIS |
| Bare aluminum (polished) | 0.8 | Do NOT use in optical path |
| Bare aluminum (machined) | 0.3 | Avoid near detector |
| Bead-blasted black | 0.03 | Common baffle treatment |

## Coating Strategy
- First-surface baffles: choose < 0.02 BRDF when signal-to-flare matters.
- Secondary surfaces: 0.05 is often fine.
- Always ask about outgassing / vacuum compatibility for space.
