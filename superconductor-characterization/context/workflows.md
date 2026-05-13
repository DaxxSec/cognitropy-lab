# Superconductor Characterization — Workflows and Methodology

Step-by-step procedures and decision trees the agent uses while operating the characterization lab as a capacity-constrained service system. Tied to today's technique (capacity planning models) so every workflow ends with a queue / cryogen / magnet impact.

## Workflow 1: Sample-to-Result Pipeline

**Goal:** Move a sample from intake to a signed, IEC-compliant test report with a known per-sample capacity cost.

### Steps

1. **Intake.** Use `prompts/new-sample-intake-spec.md` to capture sample ID, material class, geometry, contact configuration, expected Tc/Jc/Hc2, priority tier (P0/P1/P2), and target deliverable date.
2. **Triage measurement plan.** Choose modalities from `concepts.md → Measurement Modalities`. Tc-only → R(T). Jc binning → V-I in field. Anisotropy R&D → `/jc-anisotropy-map`. RF screening → `/microwave-q-screen`. Combine where service-time variance can be reduced by batching.
3. **Capacity check.** Run `/sample-queue-plan` against the current backlog with the new sample added. If ρ > 0.80, escalate: defer P2 work or open a parallel cryostat. Run `/lhe-budget`; if forecast inventory drops below 15 % inside the procurement lead-time, throttle or order.
4. **Mounting and thermal anchoring.** Mount on the sample holder with a thermometer no more than 1 mm from the active region; route I-leads through heat-sinks to minimise self-heating; verify contact resistance at 300 K below the project spec (typically <1 µΩ·cm² for high-current samples).
5. **Cooldown.** Follow the cryostat-specific schedule from `references.md → Cryostat cooldown protocols`. Stop at intermediate temperatures only when prescribed (e.g. 77 K dwell for HTS to verify diamagnetic onset).
6. **Measure.** Run the chosen command (`/tc-sweep-protocol`, `/jc-anisotropy-map`, `/microwave-q-screen`); log every instrument setting; archive raw data into `outputs/<sample-id>/raw/` and reduced data into `outputs/<sample-id>/reduced/`.
7. **Warm-up, unload, archive.** Vent slowly to avoid condensation; archive the dataset with a hash; release the cryostat back to the queue.
8. **Report.** Generate the test report referencing the relevant IEC 61788 part, with uncertainty budget. Include the actual capacity cost (hours, helium L, magnet hours) so the planner is updated.
9. **Refresh capacity model.** Update the service-time history file under `outputs/_capacity/service-times.csv`; rerun `/sample-queue-plan` with the corrected E[S] for the next planning cycle.

### Decision Points

- If contact resistance at 300 K is above spec: re-mount before cooldown; do not "see what happens at low T."
- If the cryostat fails to reach base temperature: abort the run, schedule maintenance, mark the cryostat unavailable in the queue plan.
- If the measurement reveals an outlier Tc/Jc inconsistent with the material class: re-measure on a second technique before reporting; spurious Tc shifts often trace to contamination or mis-identified sample.

## Workflow 2: Capacity Planning Loop

**Goal:** Keep the lab inside sustainable utilisation while meeting customer commitments. Run weekly, after every incident, and before any new intake batch.

### Steps

1. **Refresh inputs.** Pull last week's actual arrival rate, service-time samples, and cryogen burn. Update C_s² with the new variance.
2. **Forecast demand.** Apply Holt-Winters or linear-trend on λ(t) for the next 2–4 weeks; flag seasonal effects (fiscal-year-end intake spikes).
3. **Run `/sample-queue-plan` for the planning horizon.** Output utilisation ρ, queue length L, lead time W per priority tier.
4. **Run `/lhe-budget` for the same horizon.** Output inventory(t), procurement trigger, per-measurement helium cost ranking.
5. **Run `/magnet-ramp-schedule` for the same horizon.** Output slack percentage per week and per magnet.
6. **Identify the binding constraint.** Cryostat-hours, magnet-hours, helium, or operator? Build the capacity report around that single bottleneck.
7. **Take one of four actions.** (a) Accept the plan as-is. (b) Add a parallel cryostat or shift to a closed-cycle alternative. (c) Defer P2 work. (d) Order more helium / book more operator hours.
8. **Publish.** Update the weekly throughput review using `prompts/weekly-throughput-review.md`; circulate to lab leads.

### Decision Points

- If ρ > 0.85 forecast for any week: do not accept new P2 work; offer alternative timelines.
- If LHe inventory crosses 15 % threshold inside procurement lead-time: order immediately; do not gamble.
- If magnet slack < 10 % and a single quench would unwind the week: pre-train the magnet over the weekend and document the contingency plan.

## Workflow 3: Tc / Jc / Hc Measurement Decision Tree

**Goal:** Pick the right technique(s) for the sample's question.

### Tc — what method?

1. **Tc onset, low Jc film** → DC magnetisation M(T) ZFC. Cheapest, no contacts needed.
2. **Tc, defined criterion (zero R, midpoint, 1 µV/cm)** → Four-probe R(T) via `/tc-sweep-protocol`.
3. **Thermodynamic Tc and gap** → Specific heat C(T) — uses more time but resolves the bulk transition.
4. **Tc in field** → Repeat R(T) at fixed B; report H_c2(T).

### Jc — what method?

1. **Engineering Jc, single value** → Transport V-I at the operating (T, B); use 1 µV/cm criterion (IEC 61788-1/-2/-3 depending on material).
2. **Magnetic Jc, no current leads needed** → M(H) hysteresis loop via Bean model — fast but lower-bound estimate; sensitive to geometry.
3. **Angle-resolved Jc(B, T, θ)** → `/jc-anisotropy-map`. Most expensive; do only if anisotropy is the question.
4. **In-field Jc on long lengths** → Multi-tap reel-to-reel; pre-cool dewar handles 100 m lots.

### Hc2 — what method?

1. **Hc2(T) curve** → R(T) at constant B, sweep B from 0 → Bmax in steps; locate midpoint or 90 % drop.
2. **Hc2(0) extrapolation** → Werthamer-Helfand-Hohenberg (WHH) fit to Hc2(T) measured at T > 0.5 Tc.

### Decision Points

- If a sample needs both Jc(B) and Hc2(T): run V-I at fixed (T, B) and R(B) at fixed T from the same mount in a single cooldown. Cuts service time ≈ 40 %.
- If a sample is precious and one-shot: prefer non-contact magnetic techniques first; transport last.

## Methodology Phases — Characterization Tiers

Every sample passes through a triage tier; only some progress to deeper tiers. The capacity planner uses tier durations as the per-sample E[S].

### Phase 1 — Triage (1–4 h)
Visual inspection, dimensional check, room-T contact-resistance check, 77 K dunk for HTS to confirm diamagnetic onset, or 4.2 K dip-probe for LTS Tc onset. Reject obvious failures here; cheapest filter in the queue.

### Phase 2 — Tier-1 Characterization (4–12 h)
Four-probe R(T) (`/tc-sweep-protocol`) and DC M(T) (ZFC/FC). Establishes Tc, transition width, and qualitative pinning. Most samples stop here.

### Phase 3 — Tier-2 Characterization (12–48 h)
Transport V-I at (T, B) of interest, AC χ(T), and where applicable surface resistance Rs(T) via `/microwave-q-screen`. Establishes Jc, n-value, hysteresis loss class, and microwave performance.

### Phase 4 — Tier-3 Characterization (48–168 h)
Field-angle Jc anisotropy (`/jc-anisotropy-map`), specific-heat C(T, B), low-T penetration depth λ(T). Used for material development, not vendor acceptance.

### Phase 5 — Reporting and Capacity Update
IEC-compliant test report; actual service-time pushed back into the capacity model; sample archived; cryostat released. Always the last step — measurement without reporting is not a deliverable.

## Workflow 4: Quench-Recovery Procedure

**Goal:** Get the magnet back to design field on a defensible schedule without losing the next week's queue.

### Steps

1. **Document.** Record quench voltage trace, time-to-quench, field at quench, last-known training plateau, operator notes. Save to `outputs/_incidents/<date>-quench.md`.
2. **Inspect.** Check coil voltage taps for asymmetry, dump resistor for damage, helium-level instruments for plausibility. Confirm no insulation fault.
3. **Refill.** Recover LHe; refill to the working level. Note total LHe lost — feed into `/lhe-budget` post-mortem.
4. **Re-train.** First ramp at 0.3 × spec rate to (last_quench_field − 1 T), hold 15 min, ramp down. Second ramp at 0.5 × spec rate to last_quench_field; if it holds, ramp to design. If it quenches again, escalate.
5. **Re-plan.** Rerun `/sample-queue-plan` excluding the down-week magnet hours; communicate revised lead times.
6. **Debrief.** Use `prompts/cryostat-incident-debrief.md` to capture root cause and any procedural change.

### Decision Points

- If the same magnet quenches twice within a week at similar fields: stop, inspect for insulation breakdown, contact magnet vendor before further training.
- If the quench voltage trace shows a propagation pattern consistent with a hot spot: cycle thermally before retraining (warm to 50 K, recool).
