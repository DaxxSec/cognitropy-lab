# Flight Rules Quick Reference

> Hard limits per rover platform. These are *operational* numbers (typical planning ceilings), not the mechanical *design* limits. When in doubt, use these; the design limits are headroom for autonomous response, not for tactical planning.

---

## Mars 2020 Perseverance (RTG)

| Parameter | Limit | Source |
|-----------|-------|--------|
| Max drivable slope (operational) | ≤ 25° (sustained); design 30° | Verma et al. 2023, Rankin et al. 2020 |
| Max vehicle tilt | ≤ 25° | M2020 mobility flight rules |
| Max rock height (blind drive) | ≤ ½ wheel diameter ≈ 26 cm | M2020 wheel diameter 52.5 cm |
| Max rock height (AutoNav) | ≤ ⅓ wheel diameter ≈ 17 cm | Enhanced AutoNav stereo limits |
| Top drive speed | ~4.2 cm/s | nominal |
| Single-sol drive distance budget | typically 100–200 m, peak ~300+ m | situational |
| Wheelbase | 2.7 m | for roughness window |

## Mars Science Laboratory Curiosity (RTG)

| Parameter | Limit | Source |
|-----------|-------|--------|
| Max drivable slope (operational) | ≤ 20° routine; up to ~26° demonstrated | Rankin et al. 2020 |
| Max vehicle tilt | ≤ 30° design; ≤ 20° operational | MSL flight rules |
| Max rock height (blind drive) | ≤ ½ wheel diameter ≈ 25 cm | MSL wheel diameter 50 cm |
| Max rock height (AutoNav) | ≤ ⅓ wheel diameter ≈ 17 cm | MSL AutoNav (enhanced) |
| Top drive speed | ~4 cm/s | nominal |
| Single-sol drive distance | typically 30–100 m, peak ~140 m | situational |
| Wheelbase | 1.9 m | for roughness window |
| Notes | Wheel damage from sharp embedded rocks (Hottah-class) is a known concern; planners avoid sharp-clast bedrock segments since ~sol 400 |

## Mars Exploration Rover — Spirit / Opportunity (Solar)

| Parameter | Limit | Source |
|-----------|-------|--------|
| Max drivable slope | ≤ 25° dynamic; design 30° | MER mobility specs |
| Max vehicle tilt | ≤ 25° | MER flight rules |
| Max rock height (blind drive) | ≤ ½ wheel diameter ≈ 13 cm | MER wheel diameter 26 cm |
| Top drive speed | ~5 cm/s | nominal |
| Single-sol drive distance | typically 5–40 m | solar-energy bound |
| Wheelbase | 1.4 m | for roughness window |
| Notes | Solar — north-tilt important in southern winter for charging; **active aeolian terrain forbidden** (Spirit was lost in Troy, sol 1900) |

## Sojourner (Solar, tethered)

| Parameter | Limit | Source |
|-----------|-------|--------|
| Max drivable slope | ≤ 30° | Pathfinder mobility specs |
| Total range from lander | ~12 m tether | Pathfinder mission constraint |
| Notes | Historical reference — not for active planning |

## Rosalind Franklin (ExoMars, Solar) — Reference

| Parameter | Limit | Source |
|-----------|-------|--------|
| Max drivable slope | ≤ 25° | ExoMars rover specs |
| Max rock height | ≤ 13 cm | ExoMars wheel diameter ≈ 25 cm |
| Drilling | up to 2 m sub-surface | ExoMars instrument suite |

---

## Universal Hard Rules (All Platforms)

- **No driving across active sand sheets without explicit project approval.** Spirit was lost this way.
- **No traverses into Special Regions without planetary-protection-officer approval.** RSL, gully alcoves with possible transient water, seasonal CO₂-frost regions.
- **No traverses that strand the rover beyond its next planned comms pass.** A sol with no downlink loses the next sol's planning input.
- **No traverses with unverified parking.** The cadence chord must land on a pixel verified safe-for-overnight (slope, tilt, rock abundance all under per-platform parking thresholds — typically tighter than drive thresholds).
- **No traverses that lock out future strategic flexibility.** When two candidates have similar tactical scores, prefer the one with more pivot waypoints / branch options.

## When to Update This File

- After every anomaly that reveals a missing rule (e.g., wheel damage from a rock class previously assumed safe)
- After a flight-software upgrade that changes AutoNav or hazard-detection capabilities
- After project-level guidance that tightens or relaxes a rule
- Append a dated entry to the bottom rather than rewriting historical numbers
