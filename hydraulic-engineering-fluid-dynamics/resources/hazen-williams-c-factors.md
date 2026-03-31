# Hazen-Williams C-Factor Reference

C-factors for use in pressurized pipe flow analysis. Higher C = smoother pipe = less friction.

## C-Factor by Material and Age

| Material | New | 10 yr | 20 yr | 30 yr | 40 yr | 50+ yr |
|----------|-----|-------|-------|-------|-------|--------|
| PVC | 150 | 150 | 145 | 140 | 140 | 135 |
| HDPE | 150 | 150 | 145 | 140 | 140 | 135 |
| Ductile Iron (lined) | 140 | 135 | 130 | 125 | 120 | 115 |
| Ductile Iron (unlined) | 130 | 118 | 108 | 100 | 95 | 85 |
| Cast Iron (lined) | 130 | 125 | 120 | 115 | 110 | 105 |
| Cast Iron (unlined) | 130 | 110 | 95 | 85 | 75 | 65 |
| Steel (lined) | 140 | 135 | 130 | 125 | 120 | 115 |
| Steel (unlined) | 140 | 125 | 110 | 100 | 90 | 80 |
| Concrete (prestressed) | 140 | 138 | 135 | 130 | 125 | 120 |
| Asbestos Cement | 140 | 135 | 130 | 125 | 120 | 115 |

## Factors Affecting C-Value Degradation
- **Water quality**: Aggressive water (low pH, high dissolved O₂) accelerates corrosion
- **Tuberculation**: Iron bacteria create deposits that reduce effective diameter AND roughness
- **Biofilm**: Reduces C by 5-15 in warm-water systems
- **Mineral deposits**: Calcium carbonate scale in hard-water areas
- **Velocity**: Low-velocity pipes accumulate sediment faster

## Bayesian Prior Recommendations
- Known material AND age: Normal(C_table, σ=10) — moderate confidence in table value
- Known material, unknown condition: Normal(C_table, σ=20) — wider uncertainty
- Unknown material AND age: Uniform(60, 150) — minimally informative
- After C-factor testing (hydrant flow tests): use test results to update prior via `/calibrate`

## Conversion: C-Factor to Manning's n
Approximate equivalence for full-pipe flow:
n ≈ 1.067 × D^0.04 / (C × R^0.04)

Where D = diameter (ft), R = hydraulic radius (ft). This is approximate — use with caution for partial flow.

## Sources
- AWWA M14: Backflow Prevention and Cross-Connection Control
- AWWA M32: Computer Modeling of Water Distribution Systems
- Walski, T.M. et al. (2003). Advanced Water Distribution Modeling and Management. Haestad Press.
