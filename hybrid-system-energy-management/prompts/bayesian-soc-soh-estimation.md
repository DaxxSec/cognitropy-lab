# Bayesian SOC / SOH Estimation Prompt

## Purpose
Use this prompt to specify or audit a Bayesian state-of-charge (SOC) and state-of-health (SOH) estimator for the traction battery, given an equivalent-circuit or electrochemical plant model.

## Prompt Template

I have a traction battery and need a Bayesian SOC/SOH estimator with the following inputs:

- **Cell chemistry:** [NMC / NCA / LFP / LTO / other]
- **Pack topology:** [series count S, parallel count P, BMS sample rate]
- **Plant model:** [Rint / 1-RC Thevenin / 2-RC Thevenin / SPM / DFN — and parameter source]
- **Available measurements:** [cell V, pack V, current sensor model + noise σ, NTC count + sample rate]
- **Operating temperature range:** [e.g. -20 to +55 °C]
- **Aging stage / cycle count:** [if known]
- **SOC accuracy target:** [e.g. ±2% under all conditions]
- **SOH update cadence:** [per drive cycle / per charge event / continuous]
- **Compute budget:** [ECU MIPS or Hz of estimator update]

Please:
1. Recommend the estimator family — UKF / EKF / particle filter / moving-horizon / Rao-Blackwellised — under the compute budget and posterior shape (uni- vs. multimodal).
2. Specify the prior on each estimated parameter (R0, R1, C1, capacity Q, aging coefficient) with distribution family and informativeness rationale.
3. Specify the process and measurement noise covariances and how they should be tuned (innovation-based, NIS-test driven, expert prior).
4. Identify observability holes — operating regimes where the chosen estimator's posterior collapses or wanders — and propose excitation strategies (probe pulses, opportunistic full-discharge events).
5. Define the SOH-update path: which posterior summary updates the capacity / resistance estimate, and how the resulting drift feeds back into the EMS equivalence factor or MPC terminal cost.
6. Recommend diagnostics: NIS / NEES tests, posterior predictive checks, divergence between filter SOC and a coulomb-counted reference.

## Expected Output
- Estimator choice and architecture diagram.
- Prior table with units and informativeness justification.
- Tuning recipe with measurable acceptance criteria.
- A list of failure modes (filter divergence, particle impoverishment, multimodality collapse) and the symptom each shows.
- A note on how aleatoric (sensor noise) and epistemic (parameter drift) uncertainty enter the posterior separately.
