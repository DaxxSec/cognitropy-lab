# Flood Model — Bayesian Flood Frequency Analysis

Generate flood probability models using Bayesian estimation of extreme value distribution parameters, with honest uncertainty quantification on return-period estimates.

## Required Inputs
1. **Annual maximum series** — Peak flow records (cfs or m³/s) with water years
   - OR: USGS gage number (I'll pull data via `dataretrieval`)
2. **Regional information** (optional) — USGS regional skew coefficient, nearby gage data
3. **Stationarity assessment** — Any known land use changes, regulation changes, or climate trends

## Analysis Steps
1. Retrieve or ingest annual maximum flow series
2. Exploratory analysis: time series plot, check for trends (Mann-Kendall), identify PILF (Bulletin 17C)
3. Fit Bayesian GEV distribution via MCMC:
   - Priors: weakly informative on location/scale, informative on shape if regional data available
   - Incorporate USGS regional skew as prior information (B17C compatible)
4. Convergence diagnostics (R-hat, ESS, trace plots)
5. Generate return-period flood quantiles with 90% credible intervals
6. Optional: fit non-stationary model (time-varying location parameter) to test for trend
7. Compare Bayesian estimates to standard B17C frequentist analysis
8. Produce flood frequency curve with uncertainty envelope

## Output Artifacts
- `outputs/flood-model/flood_frequency_curve.png` — Q vs. return period with credible bands
- `outputs/flood-model/posterior_parameters.csv` — GEV parameter posteriors
- `outputs/flood-model/aep_table.csv` — Annual exceedance probability table (10%, 4%, 2%, 1%, 0.2%)
- `outputs/flood-model/flood_report.md` — Narrative report suitable for regulatory submission

## Usage
```
/flood-model
```
Provide your annual maximum series data or a USGS gage number.
