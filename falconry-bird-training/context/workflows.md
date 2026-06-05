# Falconry Bird Training — Workflows and Methodology

Step-by-step procedures the agent uses to run a falconry program, all framed through **stakeholder communication templates** — the technique this workspace is built on. Each workflow ends in a document a specific stakeholder receives. `concepts.md` says what things are; this file says what the agent does with them.

## Workflow 1: Building the stakeholder communication template library

**Goal:** Stand up a one-template-per-stakeholder library, each tied to a trigger and a deadline, before the program needs any of them under pressure.

### Steps

1. Run `/stakeholder-map` to enumerate every stakeholder for this program (see the table in `concepts.md`).
2. For each stakeholder, name the **document type** (renewal letter, sponsor report, vet intake, access request, abatement report, incident report).
3. For each document, record the **trigger** (annual date, per-event, on-demand) and the **deadline** (e.g. 3-186A within 10 days; renewal before expiry).
4. Set a **contact cadence** for relationship stakeholders (sponsor monthly/quarterly; landowner once per season; client per shift).
5. Map each document to its source data in the repo — most read from the weight/training log in `outputs/`.
6. Save the library index to `outputs/stakeholder-map-YYYY-MM-DD.md` and add reminders for every dated deadline.

### Decision Points

- If the program has no abatement work → drop the client templates; don't pad the library.
- If the falconer is a Master sponsoring an apprentice → add the reciprocal sponsor-oversight templates (you receive reports, not just send them).
- If the state uses an electronic permit/reporting portal → note that the template feeds the portal fields, not a mailed form.

## Workflow 2: Permit application / renewal and inspection-readiness

**Goal:** Produce a clean, complete packet the state coordinator can approve without a back-and-forth, plus a facility that passes inspection.

### Steps

1. Confirm the **class** (apprentice/general/master) and the **state** — pull the requirements from `references.md` and the state agency, not from memory.
2. Assemble identity, permit numbers, sponsor attestation (apprentices), and species request.
3. Run the **facility checklist**: mews dimensions, perch type (bow/block, padded), bath pan, weathering area, safety/double-door entry, predator-proofing, ventilation (aspergillosis prevention).
4. Photograph the facility from the angles an inspector checks; store in `outputs/`.
5. Draft the cover letter (`prompts/permit-renewal-cover-letter.md`) summarizing the program and any changes since last renewal.
6. Verify deadlines: file renewals **before** expiry; never let a permit lapse with a bird in possession.

### Decision Points

- If a facility item fails → fix it before requesting inspection; a failed inspection costs weeks.
- If switching species or adding a bird → confirm the new species is allowed at your class/state and that possession limits aren't exceeded.
- If moving states → you may need a new permit under the destination state's rules; don't assume reciprocity.

## Workflow 3: Apprentice–sponsor reporting cadence

**Goal:** Keep the sponsor informed and the apprenticeship defensible with regular, structured progress reports drawn from the log.

### Steps

1. Agree the cadence and format with the sponsor up front (monthly or quarterly is typical).
2. Run `/weight-log` to summarize the period: weight band, response trend, flights, hunts, feedings.
3. Run `/sponsor-report` to assemble flights flown, milestones reached (first creance flight, first free flight, first slip on quarry), equipment changes, and any concerns.
4. Flag open questions for the sponsor explicitly — the report is also a request for guidance.
5. Send via `prompts/sponsor-quarterly-update.md`; archive the sent report in `outputs/`.

### Decision Points

- If progress has stalled (no advance through the gates) → make that the headline, not a footnote; ask for a field session.
- If a welfare concern appears → escalate immediately, don't wait for the next scheduled report.

## Workflow 4: Health-event escalation

**Goal:** Turn a husbandry observation into a fast, useful vet referral, and meet any mortality-reporting obligation.

### Steps

1. On any concerning sign (going light, fluffed/reluctant, mouth lesions, labored breathing, vomiting, lameness), stop and assess — do not fly the bird.
2. Run `/vet-intake` to compile: weight trend (last 7–14 days), recent diet (pigeon/dove = frounce risk), mute and casting appearance/timing, housing/ventilation, onset and progression.
3. Send the intake to the avian vet via `prompts/raptor-health-vet-consult.md` and call ahead — raptors hide illness until late.
4. If the bird dies → run `/incident-report`; mortality of a permitted raptor is typically reportable to the state/USFWS within the reporting window, and the band may need to be returned/reported.

### Decision Points

- If "going light" with no obvious cause → assume disease (frounce, aspergillosis, parasites) until the vet rules it out.
- If mouth lesions after feeding pigeon → frounce is the leading differential; the vet may treat presumptively.
- If a recent facility change preceded respiratory signs → aspergillosis from spores/damp is on the list; describe the housing in detail.

## Workflow 5: Landowner access negotiation and stewardship

**Goal:** Secure documented hunting access and keep the relationship healthy for future seasons.

### Steps

1. Identify the ground and the quarry it holds (rabbit, squirrel, game birds).
2. Run `/landowner-access` to draft the request: who you are, what falconry is (and isn't — no firearms, low impact), dates/season, courtesy, and liability acknowledgment.
3. Offer something in return where appropriate (squirrel/rabbit control is genuine value to many landowners).
4. Get permission in writing; record quarry, boundaries, and any no-go zones.
5. Close the season with a thank-you and a brief account of how it went — this is what renews access.

### Decision Points

- If the landowner is wary → lead with the low-impact, no-firearm nature of falconry and offer a single trial outing.
- If multiple parties hold the land → confirm you have permission from the right one; tenant vs. owner matters.

## Workflow 6: Commercial abatement client lifecycle

**Goal:** Win, deliver, and document abatement work so contracts renew — and stay inside permit conditions.

### Steps

1. Confirm you hold the **abatement/commercial endorsement** before pitching anything.
2. Scope the site with `/abatement-proposal`: target species (starlings, gulls, pigeons), the asset being protected (vineyard at veraison, airfield, landfill, feedlot), operating hours, number of birds, and safety constraints.
3. Set deliverables: a service cadence and a per-shift `/abatement-report` showing sorties, dispersal efficacy, target counts, and conditions.
4. Pitch with `prompts/abatement-client-pitch.md`; on signing, schedule the program around the asset's risk window.
5. Report every shift; summarize monthly; review efficacy and renew.

### Decision Points

- If the target species or location implicates protected species or sensitive habitat → confirm the work is permissible and within permit/wildlife-control rules before proceeding.
- If efficacy is low → adjust bird/sortie pattern and say so in the report; clients renew on honesty plus results, not spin.

## Workflow 7: Training stage-gates with communication checkpoints

**Goal:** Advance the bird through the progression and tie each gate to the stakeholder who should hear about it.

### Steps

1. Run `/training-plan` to lay out gates: manning → jump-to-fist → creance → free flight → entering → conditioning.
2. Define each gate's **exit criterion** in terms of weight band + response (e.g. "flies 50 ft to the fist on the creance, 3 sessions running, at flying weight").
3. Attach a **comms checkpoint** to each gate: first creance flight and first free flight → sponsor report; entering on quarry → milestone note; any setback → log entry, possibly vet.
4. Run `/weight-log` daily; the plan reads response against weight to decide readiness to advance.
5. Do not advance on weight alone — advance on demonstrated, repeated response at a safe weight.

### Decision Points

- If response is poor but weight is at the band → manning/trust gap, not a weight problem; hold the gate, more company and fist time.
- If tempted to drop weight to force the next gate → stop; re-read `concepts.md` weight section, check for illness, consult the sponsor.
- If the bird enters cleanly → shift focus from food-response training to fitness and quarry experience.
