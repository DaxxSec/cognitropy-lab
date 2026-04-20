# Risk Scoring Rubric

Per-guideline score and default weights. Agency-tunable.

## Score scale (per guideline)

| Score | Meaning |
|---|---|
| 0 | No indicators in this guideline; baseline clean. |
| 1 | Historical indicator only; long since mitigated. |
| 2 | Minor ongoing condition with mitigation in place. |
| 3 | Active condition; inquiry recommended. |
| 4 | Multiple disqualifying conditions or one serious; limited mitigation; out-of-cycle action advised. |
| 5 | Disqualifying conditions observed; no meaningful mitigation; refer to adjudicator. |

## Default guideline weights

Weights bias a generic cleared role. Tune per mission.

| Guideline | Default weight | Rationale |
|---|---|---|
| A Allegiance | 3 | Rare but catastrophic. |
| B Foreign Influence | 3 | High base-rate; coercion potential. |
| C Foreign Preference | 2 | Usually documentable and mitigable. |
| D Sexual Behavior | 1 | Unless coercion potential exists. |
| E Personal Conduct | 3 | Candor is load-bearing. |
| F Financial | 3 | Highest single cause of CE alerts. |
| G Alcohol | 2 | |
| H Drugs | 2 | Recent use weighs higher. |
| I Psychological | 1 | Treatment-adherent subjects often mitigated. |
| J Criminal | 3 | |
| K Handling Protected Info | 4 | Direct mission harm. |
| L Outside Activities | 1 | |
| M IT Use | 3 | Especially for privileged roles. |

Composite = Σ (score_i × weight_i) / Σ weight_i, producing a 0.00–5.00 value.

## Thresholds

| Composite | Default interpretation |
|---|---|
| 0.00 – 1.50 | Low concern; extend scan interval. |
| 1.51 – 2.50 | Routine; stick to standard scan cadence. |
| 2.51 – 3.50 | Elevated; shorten scan interval and consider focused inquiry. |
| 3.51 – 4.25 | High; out-of-cycle action. |
| 4.26 – 5.00 | Refer to adjudicator. |

## Trend rules

Compute delta against prior scan.
- `improving`: delta ≤ -0.3
- `stable`: |delta| < 0.3
- `degrading`: delta ≥ 0.3

Two consecutive `degrading` scans shorten the next interval by 50%, regardless of composite band.

## Tuning log

Any change to weights or thresholds must be logged in `work-log/` with rationale.
