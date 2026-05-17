# Electromagnetic Field Mapping — Workflows

Methodology, in the form of decision trees. The triage tree is the central organising structure for every other workflow.

## Top-Level Triage Tree

The agent enters this tree the moment a non-trivial reading shows up. Each node is decided by a single observable — never by hypothesis.

```
ANOMALOUS READING
│
├─ A. Persistent on re-measure?
│   ├─ No  → transient — log, continue
│   └─ Yes → B
│
├─ B. Same magnitude on re-measure with probe swapped or rotated?
│   ├─ No  → probe / orientation artefact — recalibrate, retry
│   └─ Yes → C
│
├─ C. Near-field (r < 2D²/λ for suspected emitter)?
│   ├─ Yes → use separate E + H probes; go to D
│   └─ No  → far-field; isotropic or calibrated antenna; go to D
│
├─ D. Narrowband, harmonic family, or wideband?
│   ├─ Single line                 → INTENTIONAL emitter — go to E
│   ├─ Harmonic family (f, 2f, …)  → SWITCHING / DIGITAL source — go to F
│   ├─ Wideband decade-spanning    → ARCING / CORONA / CONDUCTED — go to G
│   └─ Burst, low duty cycle       → check TSCM signature list — go to H
│
├─ E. Intentional → cross-reference allocation table
│   ├─ ISM / licensed band hit     → identify operator / service, log, compare to limit
│   └─ Off-band                    → unauthorised emitter — escalate per scope
│
├─ F. Switching / digital → harmonic spacing implies fundamental
│   ├─ Spacing matches known clock → device candidate list — go to /isolate-emi-culprit
│   └─ Spacing novel               → bench investigation; near-field map
│
├─ G. Arcing / corona / conducted
│   ├─ Outdoor 50/60 Hz lines      → corona — power utility issue, not an exposure issue
│   ├─ Indoor wiring               → mains noise — current clamp at panel
│   └─ Equipment cabinet           → arcing contact — maintenance ticket
│
└─ H. Burst / low duty cycle
    ├─ Disappears with AC cut      → line-powered covert emitter — TSCM follow-up
    ├─ Off-band continuous-when-on → covert emitter — TSCM follow-up
    └─ Matches Wi-Fi / BT beacon   → authorised consumer kit — log and continue
```

`/triage-source` walks this tree end-to-end on a single anomaly. Every branch produces a falsifiable measurement that decides the next step.

## Survey Lifecycle Workflow

A complete survey has five phases. The agent runs them in order and refuses to skip ahead.

### Phase 1 — Scope and Plan

1. Confirm survey type with the user (occupational safety / general-public / EMC pre-screen / TSCM / fringe-field).
2. Pin the standard (ICNIRP 2020, IEEE C95.1-2019, FCC OET-65, IEC 62232, CISPR 32, IEC 61786, IEC 60601-2-33).
3. Inventory probes, antennas, and instruments; verify calibration.
4. Walk the site or review the layout; mark exclusion zones; identify expected dominant sources.
5. Run `/survey-plan` to produce the grid, parameter table, and dwell budget.
6. Get a written sign-off on the scope before fieldwork.

### Phase 2 — On-Site Capture

1. Set up the coordinate frame at the site origin; verify with a control point measurement.
2. Re-zero / calibration-verify each probe.
3. Walk the grid, recording each row immediately. Use a structured form, not freehand notes.
4. For each anomalous reading, branch into the triage tree (`/triage-source`).
5. Photograph the site, the exclusion zones, the probe in measurement position. The photographs are part of the deliverable.
6. End-of-day: back up raw data, verify CSV row counts, verify timestamps make sense.

### Phase 3 — Office Reduction

1. Ingest CSV into the analysis environment; sanity-check ranges and units.
2. Apply probe / antenna-factor corrections per the calibration certificate.
3. Re-classify readings by band, by zone, by source class.
4. Run `/interpolate-isofield` for the spatial map(s).
5. Run `/check-exposure-compliance` for the compliance verdict (occupational / general-public surveys) or `/isolate-emi-culprit` for the EMC bisection.

### Phase 4 — Report

1. Draft the report from the prompts in `prompts/`.
2. Include: scope, standard, instruments + cal IDs, methodology, maps, tables of exposure quotients, photographs, uncertainty discussion, verdict, mitigation recommendations.
3. Cross-check the report against the survey-plan sign-off; any deviation is flagged in the report.
4. Peer review before sign-off — a second engineer rechecks at least the highest-EQ rows.

### Phase 5 — Sign-Off and Archive

1. Sign-off line on the report (technician + reviewing engineer + safety officer).
2. Archive raw data, plans, maps, and report under `outputs/archive/<date>-<site>/`.
3. Diary the next periodic re-survey if the program requires one.

## EMC Bisection Workflow (Phase 3 variant)

Used by `/isolate-emi-culprit` when the survey is EMC rather than safety.

1. Lock the analyser on the failing frequency family.
2. List candidate emitters with their known fundamental clocks.
3. Power-down bisection: confirm the candidate by ≥ 10 dB attribution.
4. Near-field probe confirmation: same candidate is also the local hot-spot.
5. Identify the coupling path (cable common-mode, enclosure aperture, ground bounce).
6. Apply one mitigation at a time; verify; iterate.
7. Document source → path → emission chain.

## LF Magnetic Workflow (Power-Frequency Variant)

For 50 / 60 Hz magnetic surveys around transformers, switchgear, MRI fringe fields, residential / occupational exposure.

1. Use 3-axis ELF probe (`B` in µT or mT). Single-axis probes underestimate true magnitude.
2. Walk a fixed-height grid (typically 1 m, the IEC 61786 reference height for general population exposure).
3. For MRI fringe fields, measure at 5 G (0.5 mT) and 200 G (20 mT) isocontours specifically; IEC 60601-2-33 controls signage placement.
4. Time-average per the standard's window (often 24-hour rolling for some occupational regimes).
5. Compare against ICNIRP 2010 (LF) or IEEE C95.6 reference levels — note these are nerve-stimulation limits, not thermal.
6. Plot isofield contours with `/interpolate-isofield`; mark the limit line.

## TSCM Workflow Variant

When the survey is a counter-surveillance sweep, the triage tree branches differently at node D and H.

1. Pre-sweep: enumerate authorised emitters (Wi-Fi APs, BT devices, cordless phones, smart-building radios). These are filtered out of the anomaly list.
2. Wide spectral scan with peak detector and persistent display — covert emitters often appear briefly.
3. Cross-reference any unmatched signal against the allocation table (`context/references.md`).
4. Disappearance test: cut AC, recheck. A line-powered emitter falls off; a battery-powered one persists for hours.
5. Localise by directional antenna DF and proximity probing.
6. Document under the engagement's authorised-scope file; do **not** demodulate captured content.

## Decision Points That Always Require Human Review

- Crossing or approaching an exposure limit (any EQ ≥ 0.8 row).
- Discovering an unauthorised emitter on-premises.
- Detecting a previously-undocumented transmitter installation.
- Any survey where the calibration cert lapses between planning and fieldwork.
- Any TSCM finding before reporting to the client.
