# Workflows — Microplastics Sampling & Testing

How an expert actually runs the program, organized around the technique: **predictive maintenance scheduling** keeping a **layered screening** network operational.

## A. End-to-end monitoring pipeline

```
Targeting → Deployment → Collection(+custody) → Prep → Blank audit ─┐
                                                                     ▼
        Primary screen ──referral──▶ Secondary confirm (polymer-id)
                                                                     ▼
                         Concentration report → Anomaly check → Baseline
                                  ▲                                  │
                  QA (recovery, blanks) ──── feeds ──── Maintenance forecast
```

1. **`/risk-target-sites`** — rank candidate sites; pick primary targets + controls.
2. **`/sampler-deployment-plan`** — stations, replicates, apertures, field-blank schedule, throughput.
3. **Collection** — open **`/custody-log`** at the point of sampling; seal and sign.
4. **Prep** — digestion (WPO/KOH, never blanket acid) → density separation (medium denser than targets) → filtration.
5. **`/blank-audit` FIRST** — gate the batch. Quarantine on failure; do not count.
6. **`/screen-sample`** — primary count + referral policy → **`/polymer-id`** on referrals.
7. **`/qa-recovery-spike`** — recovery factors for the method version in use.
8. **`/concentration-report`** — blank- and recovery-corrected result with uncertainty + provenance.
9. **`/contamination-anomaly`** — baseline deviation + watchlist; escalate or update baseline.
10. **`/instrument-maintenance-forecast`** — standing cadence, fed by QA trends.

## B. Risk-based targeting (intelligence-led)

1. Assemble drivers per site (outfall proximity, urban runoff, hydrodynamic accumulation, known sources, decision-value).
2. Normalize, weight, score; impute missing drivers to the median and flag.
3. Enforce coverage: at least one control site; spatial spread across mixing cells.
4. Select to capacity; never trade away replicates at primary targets to add marginal sites.
5. Record the rationale so the targeting is auditable next quarter.

## C. Layered screening (primary → secondary)

The throughput/detection knob lives here.

- **Primary (high-throughput, cheap):** visual sort + Nile Red; counts candidates, classifies morphology/size/color.
- **Referral rules → secondary:**
  - Always refer watchlist morphologies (program-dependent: fibers, beads, TWP).
  - Refer a **size-stratified random subset** (e.g. 10–30%/bin) of the rest → makes the confirmed-plastic fraction and the primary false-positive rate estimable.
  - Refer all ambiguous-signal particles.
- **Secondary (definitive, slow):** µ-FTIR / Raman via `/polymer-id`, with the HQI threshold + band cross-check.
- **Decision tree for a referred particle:**
  ```
  Spectrum quality OK? ── no ──▶ re-acquire (or fluorescence → switch FTIR↔Raman)
        │ yes
  HQI ≥ threshold AND margin ≥ min? ── no ──▶ unresolved → second technique / Py-GC/MS
        │ yes
  Diagnostic bands present & density-consistent? ── no ──▶ reject hit → adjudicate
        │ yes
  Confirm polymer
  ```

## D. Contamination control (runs through everything)

1. Glass/metal labware only; cotton lab coats; no synthetic clothing at the bench.
2. Work in a laminar-flow or filtered-air enclosure; keep samples covered.
3. Procedural + field + air blanks every batch; handle blanks identically to samples.
4. Reagents pre-filtered; check reagent blanks too.
5. `/blank-audit` sets LOD = mean blank + 3·SD; report < LOD honestly.

## E. Predictive-maintenance scheduling loop

Run `/instrument-maintenance-forecast` on a standing cadence (e.g. weekly), not just on failure.

1. **Collect signals:** usage counters (source hours, injections, tow distance), calibration-verification control charts, and the QA early-warnings (blank-load trend ↑, recovery trend ↓).
2. **Estimate RUL** per asset from the nearer of usage budget or drift trajectory.
3. **Schedule by data-risk:** service the asset whose drift most threatens upcoming high-value batches first.
4. **Quarantine** any asset past a hard limit or with an open calibration failure — out of service for reportable work until re-verified.
5. **Close the loop:** after service, re-run a check standard / recovery spike to confirm the fix before resuming reportable runs.

**Why QA feeds maintenance:** the blank and recovery trends are the cheapest condition sensors you have. A creeping polyester-fiber blank load usually means a HEPA cartridge nearing end of life; a sliding dense-polymer recovery usually means an aging density medium or a worn sieve. Catch these in the forecast, not in a ruined batch.

## F. Anomaly escalation (watchlist hit handling)

1. Confirm the result passed `/blank-audit` — rule out lab artifact before any field alert.
2. Compute baseline deviation (season/flow-aware).
3. Scan for watchlist signatures; a hit escalates regardless of total load.
4. Check for a composition shift even at stable total count.
5. Assign tier: `routine` → update baseline; `watch` → re-sample; `alert` → notify + trigger source-attribution sampling; `incident` → lab-contamination root cause (`prompts/contamination-incident-writeup.md`).

## G. Quarterly program review

Use `prompts/monitoring-program-review.md`: pair **detection performance** (confirmed-plastic yield, primary false-positive rate, LODs, recovery) against **network uptime** (instrument calibration history, quarantines, deferred services). A dataset is only as comparable as the network was stable.
