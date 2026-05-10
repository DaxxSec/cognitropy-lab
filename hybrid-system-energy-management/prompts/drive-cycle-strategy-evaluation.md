# Drive-Cycle Strategy Evaluation Prompt

## Purpose
Use this prompt to compare two or more EMS strategies on a set of certification or real-world drive cycles, with explicit credible intervals on the headline metrics.

## Prompt Template

I want to compare hybrid energy-management strategies on a battery of drive cycles:

- **Strategies under test:**
  - A: [name, brief description, key hyperparameters]
  - B: [name, brief description, key hyperparameters]
  - (optional) C, D…
- **Reference benchmark:** [DP offline-optimal solution available? yes/no]
- **Cycle set:** [WLTC class 3b / CLTC-P / FTP-75 / HWFET / ARTEMIS triple / list of fleet-log paths]
- **Initial SOC handling:** [single point / sweep over {20, 40, 60, 80}% / posterior over SOC0]
- **Vehicle simulator:** [Autonomie / FASTSim / GT-SUITE / custom Simulink model — and version]
- **Number of stochastic seeds:** [if any strategy is stochastic; otherwise N/A]
- **Output metrics required:** [CS-mode L/100 km, MPGe, terminal SOC, NOx if available, battery throughput Ah, peak C-rate, NVH proxy if any]
- **Aging cost included?** [yes — model name + weight; or no]

Please:
1. Lay out the experimental matrix (strategies × cycles × initial conditions × seeds) and flag if it is too large for the stated compute budget.
2. Recommend statistical handling: which metrics need Monte Carlo over the stochastic disturbance, which need Bayesian posterior summaries, which can stay deterministic.
3. Define the headline tables: per-cycle with 95% credible intervals, and an aggregate that respects the cycle-mix utility weights (SAE J2841 for PHEV).
4. Specify one or two Pareto frontiers worth plotting — typically fuel-vs-aging or fuel-vs-NVH — and the dominance criterion to use.
5. Identify configurations where strategy ranking is likely to flip, and propose targeted runs that resolve the ambiguity.
6. Sketch the report structure (executive summary → cycle-by-cycle → frontier → caveats) so the result is reviewable by a calibration engineer who was not in the loop.

## Expected Output
- Experimental matrix as a checklist.
- Metric definitions with units, cycle scope, and uncertainty handling.
- Mock headline table (1–2 lines populated to illustrate format).
- Plot list with axes and reference lines (e.g. DP benchmark).
- Open questions that need engineering input before runs start.
