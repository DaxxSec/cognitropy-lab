# RF Spectrum Analysis — Workflows and Methodology

The agent's procedural playbook. The unifying loop is **Baseline → Assess → Chart → Intervene → Reassess** (BACIR), borrowed from clinical Plan-Do-Study-Act but mapped to spectrum reality. Each workflow below corresponds to a phase of that loop.

## The BACIR loop

```
   ┌──────────────────────────────────────────────────┐
   │                                                  │
   ▼                                                  │
[Baseline]──▶[Symptom Assess]──▶[Chart]──▶[Intervene]──┘
                  ▲                            │
                  │                            │
                  └──────[Reassess]◀───────────┘
```

The loop is run continuously, not as a project that ends. Most spectrum issues don't have a discharge; they have a *stability range*.

## Workflow 1: New-Site Baseline Establishment

**Goal:** Move a previously unmeasured site from "no information" to a defensible SPC-ready baseline within one week.

### Steps

1. **Site walk.** Identify candidate measurement locations: away from local interferers (microwave, fluorescent lighting, USB-3 cables), with line-of-sight to bands of interest, with secure mains power.
2. **Antenna and receiver lock.** Choose one antenna per band of interest; fix gain to a non-AGC value; document everything. Photograph the install.
3. **Pilot capture (1–2 hours).** Verify the recording chain, check for receiver overload by sweeping gain in 3 dB steps, validate FFT/window choices.
4. **Production capture (≥24h, target 168h).** Invoke `/spectrum-baseline-survey`.
5. **Limit derivation and emitter catalogue.** Compute control limits per channel; list persistent emitters with provisional severity tier (most start Tier 1 or 2; persistent emitters can be Tier 2 with `Distress=0` if no system is affected).
6. **Manifest review.** Confirm with site stakeholders that the captured window is representative.

### Decision Points

- If gain compression detected in pilot → lower gain, raise antenna attenuation, redo pilot.
- If a known intermittent event missed the capture window (weekly maintenance, monthly testing) → extend capture or annotate the gap.
- If site has substantial diurnal/weekly cycles → 168h baseline mandatory; 24h is wrong.

## Workflow 2: Triage of an Inbound Interference Complaint

**Goal:** Move from "user says their Wi-Fi is slow" to a graded, charted, and triaged item with a recommended intervention rung in under 4 hours.

### Steps

1. **Capture the complaint structure.** What service, what band/channel, when noticed, what's the impact (ESAS-style: pain location, onset, character, severity).
2. **Receiver-side rule-out.** Sweep gain, switch antenna, swap SDR or analyser. 30–60% of complaints terminate here as measurement artefacts.
3. **Run `/symptom-assess`** against the existing baseline.
4. **Run `/control-chart-build`** on the most relevant metric (typically packet-loss rate for Wi-Fi, noise floor for narrow-band devices, peak power for licensed-band complaints).
5. **Run `/intervention-ladder`** with the symptom record. Choose a rung; document deviation if any.
6. **Communicate.** A 4-paragraph summary to the complainant with: confirmation/denial of cause, severity tier, intervention plan, re-assessment date.

### Decision Points

- If Tier ≥3 AND distress includes safety-critical or compliance-critical → also trigger `/spectrum-mdt-handoff` for the same subject.
- If receiver-side rule-out succeeds → close as artefact, document why, train the reporter.
- If chart is OOC but `/symptom-assess` is Tier 1 → invest in monitoring (`/longitudinal-track`); do not intervene yet.

## Workflow 3: Quarterly Capability Review

**Goal:** Defensible quarterly statement of "is this site's spectrum process capable of supporting its dependent applications?"

### Steps

1. **Stability gate.** Run `/control-chart-build` on the primary metric for the quarter. If OOC, resolve before continuing.
2. **Capability computation.** `/process-capability-report` against the application SLA / regulatory limit. Report both Cpk (short-term) and Ppk (long-term).
3. **Trajectory roll-up.** `/longitudinal-track --window since-quarter-start --all-active` for context.
4. **MDT brief.** `/spectrum-mdt-handoff` with the capability verdict as the decision frame.
5. **Re-baseline if step 1 produced sustained OOC that resolved via intervention.** New stable conditions deserve new limits.

### Decision Points

- If Cpk < 1.00 and root cause is environmental (cannot be eradicated within budget) → renegotiate the spec; document.
- If Cpk ≥ 1.33 and trending flat → reduce monitoring cadence (de-escalation is a legitimate output).

## Workflow 4: Out-of-Control Investigation

**Goal:** When a chart flags special-cause variation, isolate the cause within one assessment cycle.

### Steps

1. **Verify the WE-rule trigger.** Cross-check on a second metric (e.g., if noise floor flagged, check occupancy and peak-count). Single-metric flags can be artefact; concordant multi-metric flags rarely are.
2. **Inventory recent changes.** Site changes (new equipment, antenna moves, neighbour changes), measurement-chain changes (firmware updates, cable swaps), environmental changes (weather, HVAC, seasonal). Tabulate.
3. **Hypothesis differential.** Generate 2–4 candidate special causes, with evidence weight.
4. **Targeted probe.** Choose a measurement that discriminates between top hypotheses (e.g., directional antenna sweep to localise; narrow-RBW capture to discriminate co-channel vs adjacent-channel; turn off suspect device and re-measure).
5. **Conclude.** Identified → log to symptom record, choose intervention rung. Inconclusive → extend monitoring, increase capture density.

### Decision Points

- If the OOC pattern is **rule 7 (over-control)** — 15 consecutive points within 1σ — the operator may be over-controlling; investigate before re-baselining.
- If only one chart, in one channel, has a single rule-1 violation and all other indicators are clean → label `isolated-blip`, watch.

## Trajectory classification (used by `/longitudinal-track`)

- **stable-low:** mode tier ≤ 1 over window AND max tier ≤ 2.
- **stable-elevated:** mode tier = 2 over window AND max tier ≤ 3.
- **improving-post-intervention:** intervention marker present AND tier decreased by ≥1 step within 4 weeks AND held.
- **worsening:** tier increased by ≥1 step in the most-recent third of the window.
- **relapsing-remitting:** ≥2 tier changes ≥2 steps in the window with no intervention between them.
- **data-gap:** no `/symptom-assess` in the most-recent ⅓ of the window; classify by last-known tier and flag.

## Methodology Phases (BACIR detail)

### Phase 1 — Baseline
Establish measurement chain, fix conditions, capture ≥25 subgroups, derive limits, catalogue persistent emitters. Output: `outputs/baseline-<site>-<date>/`.

### Phase 2 — Symptom Assessment
Multidimensional severity grade on the four axes; rule out measurement artefact; produce a structured record. Output: `outputs/symptoms/<id>.md`.

### Phase 3 — Charting
Build SPC chart on the relevant metric, apply WE rules, overlay symptom and intervention markers. Output: `outputs/charts/<id>.{png,json,md}`.

### Phase 4 — Intervention
Map tier to ladder rung; choose action; commit to success criteria and re-assessment date. Output: `outputs/interventions/<id>.md`.

### Phase 5 — Reassessment
Re-run `/symptom-assess` (and refresh the chart) on the same subject at the planned interval; update the trajectory; loop back to phase 4 or step down.

The BACIR loop is the workspace's organising principle. Most one-shot deliverables (audit reports, MDT briefs, capability statements) are *snapshots* of the loop, not replacements for it.
