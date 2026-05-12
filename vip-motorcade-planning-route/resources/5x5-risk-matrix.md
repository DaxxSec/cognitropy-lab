# The 5×5 Risk Matrix — Reference Card

The canonical scoring matrix used throughout this workspace. Print as a wallet card.

## Likelihood (L)

| L | Tier | Anchor — only assign if … |
|---|------|---------------------------|
| 1 | Rare | No credible actor has both intent and capability against this principal in this AOR. |
| 2 | Unlikely | Capable or intentional actors exist, but no specific targeting; hazard at base rate only. |
| 3 | Possible | Intent + capability both present; principal's profile or window matches actor's pattern. |
| 4 | Likely | Specific dated indicator within 90 d, OR principal in actor's known operating area during sensitive window. |
| 5 | Almost Certain | Active, dated, specific threat against this principal or near-identical principal here, OR similar successful attack within 30 d. |

## Impact (I)

| I | Tier | Anchor |
|---|------|--------|
| 1 | Negligible | Brief delay, no injury, no story. |
| 2 | Minor | Detail-level injury or vehicle damage; principal undisturbed. |
| 3 | Significant | Forced abort; minor principal injury; press story; protocol breach. |
| 4 | Critical | Critical principal injury, principal capture, KIA among detail. |
| 5 | Catastrophic | Principal killed; mass casualty; geopolitical incident. |

## Risk Bands (L × I)

```
Impact →
              I=1   I=2   I=3   I=4   I=5
L=5 Almost     5     10    15    20    25
L=4 Likely     4      8    12    16    20
L=3 Possible   3      6     9    12    15
L=2 Unlikely   2      4     6     8    10
L=1 Rare       1      2     3     4     5

  Low: 1-4   Moderate: 5-9   High: 10-14
  Very High: 15-19   Extreme: 20-25
```

## Operating Stance per Band

| Band | Stance |
|------|--------|
| Low | Acceptable. Document mitigations performed. |
| Moderate | Acceptable; default ceiling for an approved leg. |
| High | Detail-leader sign-off + named segment-specific countermeasure. |
| Very High | Written contracting-office sign-off; re-engineer if at all possible. |
| Extreme | Veto. Re-route. |

## Inherent vs Residual

- Score **inherent first** (no mitigations).
- Apply each mitigation explicitly against L, I, or both, with rationale.
- Score **residual**.
- The detail leader signs off on **residual**, not inherent.

## Common Anchors for Mitigation Effects

| Mitigation | L impact | I impact | Notes |
|------------|----------|----------|-------|
| Hardened (B6+) principal vehicle | — | I-1 to I-2 against ASLT/IED | Reduces casualty severity, not attack likelihood |
| CAT vehicle in motorcade | — | I-1 against complex ambush | Extends survivability window, not avoidance |
| Advance team sweep within 30 min | L-1 against IED | — | Sweep horizon decays past 30 min |
| Counter-surveillance running | L-1 against complex / kidnap | — | Reduces actor's pre-attack confidence |
| Route closure with police escort | L-1 to L-2 against crowd / lone-actor | I-1 against crowd-surge | Increases motorcade visibility (cost) |
| Crowd line in place | L-2 against crowd-surge | I-1 | Only at venue/dwell points |
| Low-profile (unmarked) motorcade | L-1 against most | — | Trades visibility for response capability |
| Randomized timing (±15 min) | L-1 against pre-positioned attack | — | Effective only if pattern-of-life is broken broadly |

## Things the Matrix Does NOT Capture

- **Rare-but-systemic hazards** (e.g. 1-in-10⁵ events) — handle separately as "black-swan considerations" in the brief, not via the matrix.
- **Reputational risk to the unit** — rolled into the principal-impact axis only when consequences accrue to the principal.
- **Cost / political cost of countermeasures** — handled in `/route-compare` weights, not in the matrix.

## Calibration Cadence

- Re-anchor L and I tier definitions every quarter, or after any movement where predicted vs actual residual drifts > 1 band on three consecutive legs.
- Document recalibrations in `planning/calibration-log.md`.
