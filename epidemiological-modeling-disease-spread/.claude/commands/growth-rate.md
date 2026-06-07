# /growth-rate

Estimate the epidemic growth rate r, convert it to doubling/halving time, and map r → Rt via the generation interval — a fast, communicable read of epidemic speed and a cross-check on `/estimate-rt`.

## Inputs

- An incidence series (preferably nowcast-corrected) and the **window** plausibly in exponential phase.
- **Generation interval** (mean μ, shape k or SD) for the r → Rt conversion.
- Count model (Poisson / negative-binomial — NB if overdispersed).

## Steps

1. Read `context/workflows.md` "Workflow 2: Growth rate and doubling time".
2. Select the exponential window; confirm log-linearity visually (a curving log-plot means r is not constant — stop and use Rt + decomposition).
3. Fit `log(count) ~ time` via a Poisson/NB GLM with log link (or robust log-linear regression); recover **r** and its CI.
4. Compute **doubling time = ln(2)/r** (halving time if r < 0) with CI propagated from r.
5. Convert to Rt with the Euler-Lotka relation; for a gamma generation interval: `R = (1 + rμ/k)^k`. Report Rt + CI.
6. Compare the converted Rt to the renewal-based Rt from `/estimate-rt` as a consistency check.
7. Write results to `outputs/`.

## Output

`outputs/growth-rate-<stream>-<snapshot-date>.md`: the window used, r ± CI, doubling/halving time ± CI, the generation interval and converted Rt ± CI, and a one-line speed statement ("doubling every ~X days; Rt ≈ Y").

## Notes

- r is only constant in early growth — extrapolating it past susceptible depletion or behaviour change overstates the epidemic.
- If the r CI spans 0, report "no clear growth/decline" and the slope CI; do not quote a doubling time.
- The r → Rt mapping is sensitive to the generation-interval **shape**, not just its mean — a more dispersed interval gives a larger Rt for the same r.
