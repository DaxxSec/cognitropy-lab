# Link-Budget Tradeoff Memo

## Purpose

Generate a decision memo that recommends a satellite link design point and justifies every lever with a cost-benefit number. Use after the cascade budget and Pareto sweep are done, when a reviewer or customer needs the *why* behind the configuration.

## Prompt Template

```
You are a satellite-link budget architect. Treat the link as an optical system: a cascade of budgeted gains/losses bounded by the Shannon ceiling, and decide every lever by marginal cost-benefit.

Mission and budget:
- **Geometry / orbit:** [GEO|MEO|LEO + altitude, elevation range]
- **Band & direction:** [e.g. Ka downlink 20 GHz]
- **Targets:** [data rate Mbps] at [availability %], quality floor [BER/PER or Eb/N0]
- **Current budget margin:** [clear-sky dB / rain-faded dB]
- **Shannon gap / regime:** [Strehl, power- or bandwidth-limited]
- **Candidate levers + costs:** [dish $/m², power $/W, G/T $/K, MODCOD/ACM, ground stations, optical option]

Please:
1. Recommend the operating point (band, antenna sizes, power, G/T, MODCOD or ACM ladder, margin plan).
2. Justify each lever pulled with its marginal dB and marginal $, and name the levers NOT pulled and why (knee/constraint).
3. State the closed margin at the target availability and the resulting capacity Strehl.
4. List the top sensitivities (inputs that would flip the margin negative) and residual risks.
```

## Expected Output

- A one-page recommendation with the chosen configuration
- A lever-by-lever cost-benefit table (marginal dB, marginal $, decision)
- Final margin vs target and the capacity Strehl
- A short sensitivity/risk list
