# Constraints, Boundaries, Conventions

> Populated by `/onboard`. Defaults below; tighten or relax during onboarding.

## Hard Rules

1. **Append-only sealed vintages.** Never overwrite a sealed parquet or its raw response. Re-pulls of identical bytes are noops; re-pulls of differing bytes always create a new dated file.
2. **Forecast inputs must precede decision time.** A forecast tagged with decision date `D` may only depend on vintages with `retrieved_utc <= D`. The agent must enforce this when assembling backtest matrices.
3. **No publishing without a sealed bundle.** External numbers ship only via `/release-forecast` output bundles.
4. **Embargo respect.** A series under press embargo at retrieval is sealed with `embargoed_until: <timestamp>`. Releases refuse to include such a series before the embargo lifts.
5. **No silent transformation.** Every transformation (log diff, seasonal adjustment, stationarity differencing, outlier treatment) is recorded in the run manifest with a parameter dict.

## Soft Conventions

- Quarterly growth is reported at **annualised rates** by default (US convention). EU work uses **QoQ non-annualised** as the default; the manifest records the convention per series.
- Seasonal adjustment: prefer the source's published SA series unless explicitly auditing the SA process. Custom SA via X-13ARIMA-SEATS is allowed but always sealed and labeled `sa_method: "x13" | "stl" | "source"`.
- Real vs. nominal: every series carries `units` in its manifest. Mixing real and nominal series silently is forbidden.
- Currency: real GDP series are stored in their native chained-currency units; the manifest records the base year.

## Publication & Disclosure

- Methodology disclosure is mandatory for `audience: client | public | regulator`. The cover note must name the model class, vintage cutoff, and any judgmental adjustments.
- Conflict-of-interest disclosure: if the user trades products linked to the published forecast, the cover note must include the firm's standard disclosure block (the firm provides this; the agent inserts it from `resources/disclosure-block.md` if present).
- Forecast revisions: revisions to a published forecast are themselves published numbers. They go through `/release-forecast` and inherit the same custody rules.

## Data Licensing Defaults

- **FRED / ALFRED:** redistributable per FRED Terms of Use; attribute "Federal Reserve Bank of St. Louis."
- **OECD:** non-commercial reuse with attribution; commercial republishing requires permission. Manifest tags `license: "OECD"`.
- **Eurostat:** generally open; manifest tags `license: "Eurostat"`.
- **BEA:** US Government Work, public domain; attribution recommended.
- **Bloomberg / Refinitiv:** not redistributable. Sealed locally for analysis only; never included in a public release bundle.

## What the Agent Refuses

- Refuse to publish a forecast whose lineage has any unsealed input.
- Refuse to overwrite a sealed manifest entry.
- Refuse to retro-fit a model to a published forecast (you can refit on new data; you cannot rewrite history).
- Refuse to bundle Bloomberg/Refinitiv-derived series in a `public` audience release bundle.
