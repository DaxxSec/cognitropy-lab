# Predictive Maintenance → Vetting Mapping

A compact translator for analysts and reliability engineers.

| PdM concept | Vetting equivalent | Implemented here by |
|---|---|---|
| Asset criticality | Mission criticality (1-5) | baseline.md field |
| FMEA failure modes | SEAD 4 guidelines A-M | sead-4-adjudicative-guidelines.md |
| Sensor catalog | CE data source categories | continuous-vetting-triggers.md |
| Condition index | Weighted composite risk score | risk-scoring-rubric.md |
| Trending | Scan-over-scan delta | scan-index.json |
| P-F interval | Time between first anomaly and disqualifying event | implicit — drives scan interval |
| Maintenance regime | Action category (extend, rescan, inquiry, investigation) | action-decision-tree.md |
| Work-order | Inquiry / investigation ticket | CE alert + adjudicative memo |
| Reliability-centered maintenance (RCM) | Whole-person concept | adjudicative workflow |
| CMMS | This workspace + DISS/NBIS (user-side) | workspace is the *planning* layer |

## Why the analogy works

Both disciplines are about **allocating scarce human intervention capacity across a population of assets/subjects whose condition degrades unevenly over time.** Both have:
- Observable indicators with lag between "signal" and "bad outcome."
- Costly interventions that should be applied where the marginal risk reduction is highest.
- Regulatory floors (mandatory calendar checks, mandatory periodic reinvestigations) that must be preserved even when the data says skip.

## Where the analogy breaks

- **Humans are not pumps.** Self-report, due process, and the right to a Personal Appearance have no equivalent in reliability engineering.
- **Model bias is more dangerous.** A wrongly scored bearing gets replaced early, at a cost of a few hundred dollars. A wrongly scored subject can lose a career. The scoring rubric must be conservative and transparent.
- **The P-F interval for insider threats can be near zero** in some cases — unlike equipment, humans can decide to act adversarially on short notice. Condition-based doesn't replace *reactive* — it complements it.
