# RPN Rubric (AIAG-VDA 2019 adapted for optical systems)

## Severity (S) — impact IF the mode occurs
| S | Description |
|---|---|
| 10 | Safety: injury, eye damage, fire, or regulatory non-compliance |
| 9 | Loss of mission-critical function; total image loss |
| 8 | Major performance loss; out of spec by > 2× |
| 7 | Major performance loss; out of spec by 1–2× |
| 6 | Noticeable degradation; user sees the issue |
| 5 | Minor degradation; marginal user impact |
| 4 | Cosmetic / minor; no functional impact |
| 3 | Barely perceptible |
| 2 | Almost imperceptible |
| 1 | No effect |

## Occurrence (O) — probability of failure cause
| O | Description | Rate |
|---|---|---|
| 10 | Near-certain | > 1 in 2 |
| 9 | Very high | 1 in 3 |
| 8 | High | 1 in 8 |
| 7 | Moderately high | 1 in 20 |
| 6 | Moderate | 1 in 80 |
| 5 | Low-moderate | 1 in 400 |
| 4 | Low | 1 in 2,000 |
| 3 | Very low | 1 in 15,000 |
| 2 | Remote | 1 in 150,000 |
| 1 | Almost impossible | ≤ 1 in 1,500,000 |

## Detection (D) — ability to detect cause/mode before shipment
| D | Description |
|---|---|
| 10 | No known detection |
| 9 | Very remote chance of detection |
| 8 | Possible only with special test |
| 7 | Difficult; process audit required |
| 6 | Moderately difficult |
| 5 | Moderate; in-line inspection possible |
| 4 | Moderately easy; automated inspection |
| 3 | Easy; 100% inspection |
| 2 | Very easy; SPC detects immediately |
| 1 | Certain; poka-yoke prevents occurrence |

## RPN Action Thresholds
- **RPN ≥ 200**: mandatory redesign / process change
- **100 ≤ RPN < 200**: action required
- **RPN < 100**: document, monitor
- **Any S = 10**: action regardless of RPN (safety gate)
