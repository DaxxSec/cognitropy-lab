# Seasonal Decomposition of Microbiome Signals

## Purpose
Use this prompt when you suspect seasonal cycles are masking (or being mistaken for) management effects, and you need to separate trend from seasonality cleanly before drawing a conclusion.

## Prompt Template

I have a multi-year soil microbiome time-series and I want to decompose it into trend, seasonal, and remainder components:

- **Time-series length:** [e.g., 36 monthly samples across 3 years]
- **Per-sample assays:** [e.g., 16S V4, soil moisture, T, pH, total C/N, soil respiration]
- **Site / plot structure:** [single field / replicated plots / network of farms]
- **Cropping rotation:** [e.g., maize-soy-cover, with dates]
- **Climate context:** [unusual events — drought 2024 summer, late frost 2025]
- **Files:** [ASV/qPCR tables + sensor exports + metadata]

Please decompose by:
1. Choosing the right target series (alpha diversity, CLR-transformed taxon, qPCR copies, respiration) and justifying each.
2. Running STL with appropriate seasonal window (s.window) and trend window (t.window); call out the choice.
3. Reporting the trend slope (post-decomposition) with a Mann-Kendall test on the trend component.
4. Plotting trend / seasonal / remainder and quantifying variance share for each.
5. Cross-referencing remainder spikes against management or weather events to identify true anomalies.
6. Optionally fitting SARIMA on a sufficiently long series and producing a forecast for the next sampling window.

## Expected Output
- Decomposition plots per target metric, with variance shares (trend %, seasonal %, remainder %).
- Trend slope + Mann-Kendall p-value per metric.
- Annotated remainder timeline highlighting unexplained spikes.
- Forecast (point + 80/95% PI) for the next 1–3 sampling dates if SARIMA fits.
- Sampling cadence recommendation: are we over- or under-sampling for the seasonal cycle?
