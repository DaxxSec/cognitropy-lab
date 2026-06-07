# /fit-compartmental

Fit an SEIR-type mechanistic model to an incidence series and recover interpretable parameters — R0, latent and infectious periods — with quantified uncertainty.

## Inputs

- An incidence series, preferably deconvolved to **infection dates** (see `/nowcast` and backcasting in `context/workflows.md`).
- Model structure (SEIR default; add D when fitting deaths; SEIRS for waning) and population size N.
- Prior knowledge / fixed parameters for identifiability (e.g. fix latent period from `context/references.md`).
- Inference method preference (least-squares/MLE vs particle filter / HMC) and the fitting window.

## Steps

1. Read `context/workflows.md` "Workflow 7: Compartmental model fitting".
2. Specify the **observation model**: negative-binomial on incident infections × ascertainment fraction, with the reporting delay folded in.
3. Choose inference:
   - **Least-squares / MLE** (`optim`) — fast deterministic fit on the growth-to-peak window.
   - **Particle filter / pMCMC** (`pomp`) or **HMC** (Stan/numpyro) — stochastic dynamics + full posteriors.
4. Address identifiability: if the likelihood is flat over a parameter, fix it from priors and record the choice.
5. Fit over the chosen window; recover β, γ, σ → derive **R0 = β/γ**, latent (1/σ) and infectious (1/γ) periods.
6. Run a **posterior-predictive check**: simulate from the fit and overlay on the data; inspect residuals.
7. Write parameters (posteriors/CIs), the fit overlay, and diagnostics to `outputs/`.

## Output

`outputs/seir-fit-<stream>-<snapshot-date>.md` + figure: model structure, inference method, parameter estimates with CIs/posteriors (R0, latent, infectious periods, ascertainment), the fit-vs-data overlay, and what was fixed for identifiability.

## Notes

- Latent period (SEIR's E→I) ≠ incubation period (infection→symptoms) — keep them distinct.
- Fit to infection dates, not report dates; otherwise recovered rates absorb the reporting delay.
- Deterministic ODE fits understate uncertainty in small-number early outbreaks — use a particle filter there.
- Compartmental fits give *mechanism and R0*; for the live trend call, lean on `/estimate-rt`.
