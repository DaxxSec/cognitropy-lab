# Underwater Archaeology Excavation — Workflows and Methodology

Step-by-step procedures and decision trees the agent uses when running tasks here. Everything is tied to today's technique: **using cost-benefit analysis frameworks**. Where `concepts.md` says *what things are*, this file says *what the agent does with them*.

## Workflow 1: The Project Cost-Benefit Analysis Pipeline

**Goal:** Turn a candidate submerged site into a defensible recommendation — preserve in situ, excavate, or stage further evaluation — with the full ledger exposed.

### Steps

1. **Scope the decision.** State the question precisely ("excavate the whole hull?" ≠ "recover the exposed cargo?"), the options on the table, and the decision-maker (funder, regulator, museum board).
2. **Establish the benefit currency.** Run a significance assessment (`/site-significance-score`). Decide whether benefits will be monetised, scored, or treated as MCDA criteria.
3. **Enumerate lifecycle costs per option.** For each option build: survey/evaluation, fieldwork (`/dive-budget-model`), conservation (`/conservation-cost-forecast`), perpetual curation, and post-excavation/publication. Carry costs to present value with a stated discount rate.
4. **Value the "do nothing" branch.** Run `/threat-decay-model` to estimate expected heritage loss over time in situ — this is the cost of inaction and the core of any rescue justification.
5. **Apply a decision rule.** Net present value / benefit-cost ratio where monetisation holds; weighted MCDA where it does not; expected value under threat for rescue cases.
6. **Run sensitivity analysis.** `/cba-sensitivity-sweep` over discount rate, conservation cost, threat probability, and significance weighting. Report whether the recommendation flips.
7. **Gate on compliance.** `/permit-compliance-check` before recommending any disturbance.
8. **Write the memo.** Save to `outputs/` with assumptions, sources, and the sensitivity result foregrounded.

### Decision Points

- If benefits cannot be defensibly monetised: use MCDA, not a fabricated dollar figure.
- If the recommendation flips under plausible assumptions: report it as *uncertain*, recommend a cheaper evaluation phase to reduce epistemic uncertainty before committing.
- If a threat is imminent and lead time is short: jump to the rescue-excavation branch (Workflow 3).

## Workflow 2: The In-Situ vs. Excavate Decision Tree

**Goal:** Resolve the discipline's central question for a specific site.

### Steps

1. Start from the **in-situ default** (UNESCO 2001 Annex Rule 1) — the burden of proof is on excavation.
2. Ask: **is there a research question answerable only by excavation, or a threat that will destroy the resource anyway?** If neither, preserve in situ and monitor.
3. If yes, build the excavation lifecycle cost and the in-situ management cost (both are non-zero).
4. Compare net benefit of excavation against the *option value* of leaving the site available for future, cheaper, less-destructive technique.
5. Choose, document the justification, and define the recording standard that will offset the irreversibility.

### Decision Points

- If threat is high and rising → favour excavation/rescue or active stabilisation.
- If significance is high but threat is low → favour in-situ preservation + monitoring; the option value is large.
- If conservation cost dwarfs realisable benefit → favour in-situ even if excavation is technically feasible; recover only a diagnostic sample.
- If the site is a war grave or sovereign wreck → ethical/legal constraints may override the CBA entirely.

## Workflow 3: Threat-Driven Rescue Excavation

**Goal:** Justify and scope an excavation forced by imminent loss (development, scour, trawling, looting, climate).

### Steps

1. Characterise the threat: mechanism, probability per year, and lead time to loss (`/threat-decay-model`).
2. Compute **expected heritage loss** = (significance value) × (probability of loss within the planning horizon).
3. Scope the *minimum sufficient* excavation that captures the at-risk value — rescue is triage, not completeness.
4. Prioritise within the rescue scope (`/recovery-prioritization`) because time and budget are fixed.
5. Lock conservation capacity *before* lifting — do not raise what you cannot treat.

### Decision Points

- If lead time < mobilisation time → shift to emergency stabilisation/protection, not excavation.
- If conservation capacity is the binding constraint → recover diagnostic/at-risk material only, record the rest in situ.

## Workflow 4: Survey & Method Selection

**Goal:** Buy the right evaluation and excavation methods on a cost-benefit basis.

### Steps

1. Match the **survey package** to the detection problem (`/survey-method-tradeoff`): exposed structure → side-scan/MBES; buried iron → magnetometer; buried structure/stratigraphy → sub-bottom profiler.
2. Always ground-truth geophysics with targeted diver/ROV inspection before excavation.
3. Select the **excavation method** (`/excavation-method-select`) on the cost ↔ disturbance ↔ recovery-quality trade-off for the sediment and find fragility.
4. Specify the **recording standard** (photogrammetry + context recording) that the method must not compromise.

### Decision Points

- If depth > diver range → ROV/AUV mode; recost the budget from diver-days to vehicle/vessel-days.
- If visibility is near zero → planning frames and DSM control over photogrammetry-only.
- If finds are fragile → hand-fanning near the find, airlift/dredge only for bulk overburden.

## Methodology Phases (canonical project sequence)

### Phase 1 — Desk-Based Assessment (DBA)
Compile archives, charts, prior surveys, and loss records. Cheapest phase; sets significance and threat priors. Output feeds every CBA input.

### Phase 2 — Geophysical & Diver Evaluation
Remote sensing then targeted ground-truthing. Reduces epistemic uncertainty before any expensive commitment. Often the rational stopping point.

### Phase 3 — Trial / Sample Excavation
Small, controlled intervention to test preservation, date, and significance. A cheap option to resolve a CBA that is sensitive to unknowns.

### Phase 4 — Full Excavation (only if justified)
Systematic stratigraphic removal with full recording. Triggered only when Workflow 2 clears the in-situ default.

### Phase 5 — Conservation
The long pole. Begins the moment material is raised and runs for months to decades. Capacity must be secured *before* Phase 4.

### Phase 6 — Post-Excavation, Archive & Curation
Analysis, dating, publication, and perpetual curation of both the archive and the material. The recurring liability the CBA must have already costed.
