# Continuous Vetting Triggers (reference)

A catalog of signal categories that can arrive from a CV enrollment, mapped to SEAD 4 guidelines with a default severity. Treat severity as analyst guidance — agency policy is authoritative.

## Criminal signals → Guideline J (and possibly E, G, H, D)
| Event | Default severity |
|---|---|
| Arrest — misdemeanor, no conviction | moderate |
| Arrest — felony, any disposition | high |
| Conviction — misdemeanor | moderate |
| Conviction — felony | high |
| Warrant — active | high |
| Restraining / protective order | moderate |
| Court martial (military) | high |

## Financial signals → Guideline F
| Event | Default severity |
|---|---|
| Credit score drop > 75 pts in 12 mo | low |
| Credit score drop > 150 pts in 12 mo | moderate |
| Bankruptcy Ch. 7 | moderate |
| Bankruptcy Ch. 13 | low-moderate |
| New collection account > $5k | moderate |
| Tax lien — federal | high |
| Tax lien — state | moderate |
| Unexplained large deposit > $10k | moderate (ask) |

## Terrorism / foreign → Guideline B, C, A
| Event | Default severity |
|---|---|
| Watchlist nominal match (unconfirmed) | high (verify before action) |
| Foreign travel to high-risk country (unreported) | high |
| New foreign financial interest | moderate |
| Close foreign contact (unreported) | moderate |

## Public records → varies
| Event | Guideline(s) | Severity |
|---|---|---|
| Civil litigation | F, E | low-moderate |
| Divorce with significant financial stress | F, E | low |
| Adverse press / news | E, L | moderate |

## Self-report (SEAD 3) → varies, presence of timely self-report is mitigating
| Event | Guideline(s) |
|---|---|
| Arrest / citation | J, and source guideline |
| New foreign contact | B |
| New foreign travel | B/C |
| Change in marital / cohabitation status | B (if foreign), E |
| Medical mental-health | I (voluntarily, often mitigating) |
| Financial hardship | F |

## Employer / facility → Guideline K, M, E
| Event | Severity |
|---|---|
| Classified spillage — inadvertent | moderate |
| Classified spillage — repeated | high |
| Attempted policy circumvention | moderate-high |
| Observation by coworkers of concerning behavior | moderate |

---

## Severity to Action Mapping (default)
| Severity | Default action |
|---|---|
| low | Carry into next scheduled scan; no out-of-cycle action. |
| moderate | Documented inquiry in case file; consider accelerating next scan. |
| high | Out-of-cycle inquiry or investigation; consider adjudicator referral. |

Defaults are agency-tunable in `risk-scoring-rubric.md`.
