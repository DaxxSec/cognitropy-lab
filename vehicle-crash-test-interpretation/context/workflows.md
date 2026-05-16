# Vehicle Crash Test Interpretation — Workflows and Methodology

Procedures tied to today's technique: **Bayesian probability assessment**. Every workflow's goal is a posterior, not a point estimate.

## Workflow 1: Single-Test Bayesian Interpretation

**Goal:** Convert one full-vehicle crash test, channel by channel, into a defensible posterior over occupant injury and regulatory compliance.

### Steps

1. **Channel intake.** Ingest the test ISO-MME / TDMS / CSV exports. Confirm channel count matches expected ATD schema (Hybrid III 50M ≈ 52 channels; THOR-50M ≈ 150). Reject the test if channel count is short.
2. **Run `/pulse-anomaly-check`.** Hard gate: if posterior P(in-family) < 0.2, halt. Diagnose the anomaly first; resume only after analyst clears it.
3. **Run `/dummy-bias-prior` for each dummy serial** in the test (drivers and passengers usually use different serials).
4. **Run `/injury-posterior` per occupant.** Use the dummy-specific prior, the SAE J211-conformant filtered channels, and the canonical risk-curve likelihoods (Mertz / Eppinger / Kuppa for Hybrid III; THOR-specific curves for THOR-50M).
5. **Run `/restraint-likelihood` per occupant.** Compare observed kinematics against the per-mode normal-restraint family and the degradation library.
6. **Run `/regulation-compare` per occupant per regulation** (FMVSS 208, UNECE R94, etc.). Output posterior P(compliant) and per-criterion margin.
7. **Produce the briefing.** Use `prompts/injury-risk-briefing.md` to turn the posteriors into a one-page summary; if `/restraint-likelihood` flagged degradation, also invoke `prompts/restraint-teardown-narrative.md`.
8. **Archive.** Snapshot `outputs/<test-id>/` to long-term storage; the posterior is frozen with the prior in force.

### Decision Points

- If `/pulse-anomaly-check` returns P(in-family) ∈ [0.2, 0.5]: continue but flag prominently in all downstream artefacts. The test may still be informative, but treat the result as low-confidence.
- If `/restraint-likelihood` returns P(degraded) > 0.3: invoke the teardown narrative; recommend a physical post-test inspection if not already scheduled.
- If `/regulation-compare` returns P(compliant) ∈ [0.5, 0.8]: do **not** publish a compliance claim. Recommend retest, re-elicit prior, or analyst override.

## Workflow 2: Consumer Rating Bundle (NCAP / IIHS)

**Goal:** Combine the per-test posteriors across a rating-protocol bundle into a credibility interval over the published rating.

### Steps

1. Confirm the rating bundle is complete (Euro NCAP Adult Occupant requires ≥ 7 tests; IIHS Top Safety Pick requires 6).
2. For each test in the bundle, run Workflow 1 through `/regulation-compare`.
3. Run `/star-rating-confidence` with the full bundle and the rating-protocol version.
4. Inspect the posterior over rating outcomes.
5. **Publish only if** the median rating has > 60% posterior mass. Otherwise the rating is statistically fragile; recommend a test re-shoot.

### Decision Points

- If a single test in the bundle has anomalous pulse (`/pulse-anomaly-check` < 0.5): that test is the weakest link. Decide between (a) holding the bundle and re-running that test, (b) publishing with explicit caveats in the methodology section.
- If the comparator vehicle's rating is published with no posterior reporting (industry default): note the apples-to-oranges comparison in the deliverable.

## Workflow 3: Regulatory-Impact Analysis (Threshold Change)

**Goal:** Estimate the impact of a proposed regulation revision on the lab's historical fleet without re-running physical tests.

### Steps

1. For each archived test in the database (pre-frozen posteriors from Workflow 1), re-run `/regulation-compare` with the **proposed** threshold as an override.
2. Pool the per-test P(compliant) values into a fleet-level distribution.
3. Compute the median and 5/95 of the P(compliant) under both current and proposed thresholds.
4. Use `prompts/regulatory-impact-memo.md` to generate the regulator-facing memo.

## Methodology Phases

The Bayesian update procedure is the **single methodology** every command implements. Codified once here so commands stay terse.

### Phase 1 — Prior elicitation
Per channel: from dummy certification history, build a Gaussian over the systematic bias (`/dummy-bias-prior`). Per body region / occupant: from the lab's prior-test fleet, build a Beta or LogNormal over the criterion. Per regulation: from agency-published risk curves, build the likelihood (deterministic function of the criterion).

### Phase 2 — Channel-level Bayesian update
For each measured criterion, update the prior with the channel reading + dummy-bias prior using NUTS sampling. Produce posterior samples over the criterion's true value (not the measurement).

### Phase 3 — Injury-risk transformation
Pass posterior samples of the criterion through the canonical risk curve (Mertz / Eppinger / Kuppa / THOR-specific). Output is the posterior over P(AIS k+ | data).

### Phase 4 — Compliance projection
Compare posterior to regulatory threshold. Output posterior P(criterion ≤ threshold | data). For multi-criterion regulations, compute the joint posterior over **all** criteria within threshold using the correlated posterior samples (not the product of marginals).

### Phase 5 — Reporting
Lead with median + 5/95 credibility interval. Plot the posterior density with the regulatory threshold marked. Cite the regulation revision. Cross-reference `/restraint-likelihood`.

The discipline of this methodology is what the workspace exists to preserve: **the posterior, not the point, is the deliverable.**
