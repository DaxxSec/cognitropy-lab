# Upholstery Frame Restoration — Workflows and Methodology

Step-by-step procedures the agent runs. The unifying technique is **quality control statistical methods**: every workflow ends in a data-backed decision (in/out of control, capable/incapable, accept/reject, keep/repair/replace), and `concepts.md` supplies the "why."

## Workflow 1: Intake → measure → chart → capability → disposition (the spine)

**Goal:** turn one incoming bare frame into a measured, dispositioned, charted unit of process output.

### Steps

1. **Intake & document.** Photograph the frame from all faces; open a traveler (`/restoration-traveler`). Record piece type, period, wood species (if known), and the conservation status (antique/significant vs. utility).
2. **Define the quality characteristics.** Choose the few that matter for *this* piece: squareness (diagonal difference), seat-opening width/depth, leg-length spread, joint gap, racking deflection under a reference load, wood MC. Set datum faces.
3. **Verify the measurement system FIRST.** If the gauge/jig for any characteristic hasn't been studied, run `/gage-rr`. If %R&R > 30%, fix the method before any frame data is trusted.
4. **Measure to the traveler.** Record value, instrument, operator, MC, ambient RH/temp. One row per characteristic.
5. **Plot on the running chart.** Add today's frame to the I-MR (or DNOM) chart for each tracked characteristic (`/control-chart`). Apply Western Electric rules.
6. **Branch on control state** (decision points below).
7. **If in control, assess capability** of the characteristic vs. the piece's tolerance (`/process-capability`) — but only as a process-level question, not a pass/fail for this single object.
8. **Disposition the frame:** grade joints (`/joint-integrity-grade`), write repair specs (`/joint-repair-spec`), and record keep/repair/replace per member with the ethics rationale.

### Decision Points

- If a chart shows an **out-of-control signal** → stop adding frames to the baseline; launch the OCAP (Workflow 4) to find the assignable cause.
- If the **measurement is suspect** (value far from history, no physical reason) → re-measure / re-run gage R&R before believing it.
- If the frame is **antique/significant** → conservation ethics gate every disposition: repair-before-replace, reversible adhesives only, retain originals.
- If MC is **outside the glue-up window** → defer joinery; condition the wood and chart it (`/moisture-spc`) until it settles.

## Workflow 2: Standing up a control chart for a characteristic

**Goal:** establish trustworthy control limits before using the chart to make decisions.

### Steps

1. Collect a **baseline** of ≥ 20–25 individual measurements of the characteristic from frames produced under normal conditions (this may span weeks in a low-volume shop — that's expected).
2. Compute the **moving ranges** (|xᵢ − xᵢ₋₁|) and M̄R; compute X̄.
3. Set limits: I chart `X̄ ± 2.66·M̄R`; MR chart `UCL = 3.267·M̄R`, `LCL = 0`.
4. Plot the baseline; **purge** any points with a *known* assignable cause and recompute (document each purge).
5. Once the baseline is clean and in control, **freeze the limits** and switch to monitoring mode — new frames are compared to fixed limits, not constantly recomputed.

### Decision Points

- If baseline can't be brought into control by removing documented special causes → the process itself is unstable; address root variation (jig, method, environment) before charting is meaningful.
- If frame types are too dissimilar to share a chart → switch to a **DNOM** (deviation-from-nominal) chart so mixed jobs populate one chart.

## Workflow 3: Gage R&R study (crossed, AIAG)

**Goal:** know how much of observed variation is the measurement system before trusting any frame data.

### Steps

1. Select **10 representative frames** spanning the range of the characteristic, **3 operators**, **2–3 trials** each, measured **blind and in random order**.
2. Compute **Repeatability (EV)** from within-operator trial ranges and **Reproducibility (AV)** from operator averages.
3. Compute **GRR = √(EV² + AV²)**, **Part Variation (PV)**, **Total Variation (TV)**.
4. Report **%GRR = GRR/TV** and **ndc = 1.41·(PV/GRR)**.
5. Verdict: %GRR < 10% accept; 10–30% marginal (acceptable depending on cost/criticality); > 30% reject the measurement method — fix the jig, datum, or operator technique.

### Decision Points

- If reproducibility (AV) dominates → operator technique/datum ambiguity; standardize the method and re-train.
- If repeatability (EV) dominates → the gauge/jig itself is noisy; improve fixturing or instrument resolution (need resolution ≤ 1/10 of tolerance).

## Workflow 4: Out-of-Control Action Plan (OCAP)

**Goal:** convert a chart signal into a found-and-removed assignable cause.

### Steps

1. **Confirm the signal** against the Western Electric/Nelson rule that fired; rule out a measurement error first (re-measure).
2. **Bracket the change in time** — what changed at/around the signal: new restorer, new glue lot, humidity swing, new jig, different wood source.
3. **Run a cause analysis** — 5-Whys and a fishbone across the 6 Ms (Method, Machine/jig, Material/wood+glue, Measurement, Man/restorer, Mother-nature/RH).
4. **Verify the cause** by reproducing/removing it; confirm the chart returns to control.
5. **Update the standard** (traveler checklist, jig spec, glue-up MC window) so the cause can't recur; log it in `outputs/`.

### Decision Points

- If the cause is the **measurement system** → return to Workflow 3.
- If the cause is **environmental (RH/MC)** → couple to `/moisture-spc` and add an environmental control or a conditioning step.

## Workflow 5: Acceptance decision for a batch

**Goal:** accept/reject a lot (incoming trade frames, or a batch of re-glued joints) without 100% inspection.

### Steps

1. Set **lot size N**, **AQL**, and **inspection level** (default General II).
2. Look up **n (sample size)** and **Ac/Re (accept/reject numbers)** from ANSI/ASQ Z1.4 (`/sampling-plan`).
3. Draw the sample at random; inspect against the defect definition.
4. **Accept if defectives ≤ Ac; reject if ≥ Re.** Record the OC-curve implication (producer's/consumer's risk).

### Decision Points

- If defects cluster by cause → feed `/defect-pareto`, don't just reject the lot.
- For irreplaceable/antique pieces → sampling does **not** apply; inspect 100% (sampling is for replaceable batches only).

## Methodology Phases (DMAIC mapping)

The shop's continuous-improvement loop maps to **DMAIC**:

### Phase 1 — Define
Pick the characteristic and tolerance that matter for the piece/period; open the traveler.

### Phase 2 — Measure
Validate the gauge (gage R&R), then collect baseline data with full metadata (MC, RH, operator, datum).

### Phase 3 — Analyze
Chart for stability (I-MR/DNOM), then capability (Cp/Cpk); Pareto the defect causes.

### Phase 4 — Improve
Run OCAP on signals; standardize jigs, glue-up MC windows, datum schemes.

### Phase 5 — Control
Freeze limits, monitor, keep the traveler discipline so gains hold and the conservation record stays complete.
