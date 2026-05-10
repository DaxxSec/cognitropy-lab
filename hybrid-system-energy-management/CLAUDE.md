# Hybrid System Energy Management Workspace

**Template:** `hybrid-system-energy-management` | **Version:** 1.0

## Agent Role

A Claude Code workspace for designing, evaluating, and tuning energy-management strategies (EMS) for hybrid electric powertrains — HEV, PHEV, MHEV — across parallel, series, and power-split architectures, **using Bayesian probability assessment**: explicit priors over driver intention, route load, battery state-of-health, and model parameters; posterior updates from telemetry; and credible-interval-aware decisions about torque split, SOC trajectory, and mode arbitration.

## Context References

- **Domain knowledge:** `context/concepts.md` — architectures, EMS strategy families, Bayesian framing, battery models, validation cycles, common pitfalls.
- **Methodology and workflows:** `context/workflows.md` — torque-split design, SOC-trajectory planning, posterior updates from telemetry, cycle evaluation, ECMS tuning.
- **Lookup tables and references:** `context/references.md` — standards, datasets, tools, EMS strategy comparison.
- **Reusable prompts:** `prompts/` — Bayesian SOC/SOH estimation, drive-cycle evaluation, MPC tuning, torque-split policy design.

## Available Commands

| Command | Description |
|---------|-------------|
| `/torque-split-design` | Design or tune the torque-split policy for a given architecture, with prior-over-driver framing |
| `/soc-trajectory-plan` | Plan the SOC reference trajectory for a known route (PHEV utility-factor / CS mode) |
| `/posterior-update` | Update battery SOH, capacity, or driver-intention posteriors from new telemetry |
| `/cycle-evaluate` | Run a controller against WLTP / CLTC / FTP-75 / HWFET / ARTEMIS and report fuel / emissions / SOC |
| `/ecms-tune` | Tune the ECMS equivalence factor *s* (or A-ECMS adaptation law) for a route distribution |
| `/mpc-horizon-tune` | Pick MPC prediction horizon + terminal cost weights given a posterior over trip lengths |
| `/wear-vs-fuel-pareto` | Compute and plot the Pareto frontier of fuel consumption vs. battery wear |

## Foundational Instructions

1. **This repository IS your memory.** Save tuned controllers, posterior summaries, simulation logs, and Pareto reports to `outputs/`; refresh `context/` as the domain understanding deepens.
2. **State the prior explicitly before producing a posterior.** A Bayesian EMS recommendation without a documented prior is a point estimate in disguise.
3. **Distinguish aleatoric from epistemic uncertainty.** Drive-cycle randomness (aleatoric) and model/parameter ignorance (epistemic) motivate different mitigations — robust MPC for aleatoric, active learning for epistemic.
4. **Always quote SOC, fuel consumption, and emissions in the certification cycle's units** (WLTP class 3b, CLTC, EPA FTP-75). Mixing cycles silently makes comparisons meaningless.
5. **Production EMS must satisfy ISO 26262.** Bayesian layers run *advisory* to a safety-rated supervisor; never propose changes that compromise the certified emissions envelope without a formal recalibration plan.

## Optional plugin primitives

If the user has the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, these globally-installed commands work alongside the workspace's own:

- `/workspace-foundational:context-sweep` — audit and prune the `context/` directory as the workspace ages.
- `/workspace-foundational:find-template` (skill) — recommend a different workspace shape if the project narrows (e.g. battery-prognostics-only, MPC-controller-only).

The workspace works without the plugin; the primitives are convenience.
