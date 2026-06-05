# Falconry Bird Training Workspace

> Train the hawk, manage the humans — a falconry program workspace built around reusable **stakeholder communication templates** for regulators, sponsors, vets, landowners, and abatement clients.

## What This Workspace Does

Falconry is the art of training a hawk, falcon, or eagle to hunt wild quarry in partnership with a human. But the bird is only half the job. Behind every flying raptor in the United States sits a sponsoring master falconer, a state wildlife agency, the U.S. Fish & Wildlife Service, an avian veterinarian, the landowners whose fields you hunt, and — for those who fly working birds — commercial clients paying for bird-abatement services. Each of those relationships runs on documents: permit applications, facility-inspection records, sponsor progress reports, acquisition/disposition filings, vet referrals, access agreements, service proposals, and incident reports.

This workspace treats **stakeholder communication templates** as the organizing spine of a falconry program. It pairs genuine raptor-training substance — manning, weight management and yarak, creance flights, free flight, entering on quarry, molt and husbandry — with a template library so that every required communication is structured, deadline-aware, and reproducible from the training log. The agent keeps the weight log, plans the training progression, and then turns that record into whatever each stakeholder needs to see.

## Why This Workspace Exists

Most falconers are excellent with their birds and disorganized with their paperwork. The cost of that gap is real: a missed acquisition report (Form 3-186A) or a lapsed permit renewal is a compliance violation; a facility that isn't inspection-ready delays an apprentice's first bird; a vague verbal landowner agreement evaporates the day a neighbor complains; an abatement client who never gets a service report doesn't renew the contract. This workspace codifies the discipline that the sport's regulatory weight demands: one template per stakeholder, each tied to a triggering event and a deadline, all fed from the same dated husbandry log so the bird's welfare and the program's compliance tell a single, consistent story.

## Getting Started

### Prerequisites

- A falconry permit (or an active apprenticeship under a sponsoring General/Master falconer) and knowledge of your **state's** specific regulations — they layer on top of the federal baseline and are frequently stricter.
- A digital gram scale and a habit of weighing the bird before every flight or feeding (this workspace runs on the weight log).
- Your federal/state permit numbers, facility (mews/weathering) details, and the contact info for your sponsor, avian vet, and state falconry coordinator.
- For abatement work: a commercial/abatement endorsement on your permit and any client site details (location, target species, operating hours).

### Quick Start

1. Clone this workspace.
2. Run `/stakeholder-map` to inventory everyone in your program and assign each a template and a contact cadence.
3. Run `/weight-log` to start (or import) the flying-weight & condition record — every other deliverable reads from it.
4. Run `/training-plan` to lay out the manning → creance → free flight → entering progression with a communication checkpoint at each gate.
5. As events occur, reach for the matching command: `/permit-packet` at renewal, `/sponsor-report` on the agreed cadence, `/vet-intake` on a health concern, `/incident-report` within the reporting window for a loss.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/stakeholder-map` | Inventory all stakeholders, set contact cadence, assign templates | First, and whenever the program's relationships change |
| `/permit-packet` | Assemble/audit a permit application/renewal + inspection-readiness packet | Initial permit, annual renewal, before a facility inspection |
| `/sponsor-report` | Apprentice → sponsor progress report from the training log | On the cadence you and your sponsor agree (monthly/quarterly) |
| `/weight-log` | Build/interpret a flying-weight & condition log + husbandry summary | Daily during training; summarised for any stakeholder |
| `/vet-intake` | Structured avian-vet intake/referral packet | The moment a health concern appears — then call the vet |
| `/landowner-access` | Hunting-access request and stewardship agreement | Securing or renewing access to hunting ground |
| `/abatement-proposal` | Commercial abatement service proposal + scope of work | Pitching a new airport / vineyard / landfill / agriculture client |
| `/abatement-report` | Per-shift or per-period abatement service report | After each abatement shift or on the client's reporting cycle |
| `/incident-report` | Injury / mortality / escape report to authority + sponsor | Immediately on a loss, injury, or escape (mind the reporting window) |
| `/training-plan` | Stage-gated training progression with comms checkpoints | Starting a new bird or resetting after the molt |

## Directory Structure

```
falconry-bird-training/
├── CLAUDE.md                       # Agent role, context refs, command list
├── README.md                       # This file
├── .claude/commands/
│   ├── stakeholder-map.md
│   ├── permit-packet.md
│   ├── sponsor-report.md
│   ├── weight-log.md
│   ├── vet-intake.md
│   ├── landowner-access.md
│   ├── abatement-proposal.md
│   ├── abatement-report.md
│   ├── incident-report.md
│   └── training-plan.md
├── context/
│   ├── concepts.md                 # Permits, stakeholders, species, weight & yarak, training, equipment, health
│   ├── workflows.md                # Template-library build + comms procedures tied to each stakeholder
│   └── references.md               # Permit-class table, regs & forms, equipment, ailments, organizations
├── prompts/
│   ├── permit-renewal-cover-letter.md
│   ├── sponsor-quarterly-update.md
│   ├── abatement-client-pitch.md
│   ├── raptor-health-vet-consult.md
│   └── landowner-access-request.md
└── outputs/                        # Weight logs, training plans, permit packets, reports, agreements
```

## Example Use Cases

### First-bird apprentice onboarding
A new apprentice needs to pass a facility inspection and file for their first red-tailed hawk. `/permit-packet` builds the application + inspection checklist (mews dimensions, perch type, bath pan, weathering area), and `/stakeholder-map` sets the reporting cadence with their sponsor before the bird is even trapped.

### Daily training of a passage red-tail
`/weight-log` tracks response against flying weight day by day; `/training-plan` gates the bird from manning through creance to free flight, and surfaces the moment the bird is sharp-set enough to enter on quarry without being driven dangerously light.

### Commercial vineyard abatement contract
`/abatement-proposal` scopes a starling-dispersal program for a vineyard at veraison; weekly `/abatement-report` deliverables document sorties, dispersal efficacy, and target-species counts so the client sees value and renews.

### Health scare — a bird going light
A bird drops below its expected weight band and is fluffed and reluctant. `/vet-intake` assembles the history (weight trend, mute appearance, casting times, recent diet) into a referral the avian vet can act on immediately — frounce and aspergillosis are on the differential.

### Lost-and-recovered raptor reporting
A bird breaks off after quarry and is recovered two days later via telemetry. `/incident-report` documents the escape and recovery for the state coordinator and sponsor within the reporting window, with the band number and circumstances.

## Recommended MCP Servers

- **filesystem** — read weight-log CSVs, store permit PDFs, photos of the bird/feathers/facility, and write reports to `outputs/`.
- **calendar / reminders** — permit-renewal dates, inspection appointments, molt timing, and the 3-186A 10-day filing window are deadline-driven; surface them before they lapse.
- **gmail / email** — send the stakeholder communications the prompt templates generate (sponsor updates, landowner requests, client reports).
- **pdf** — fill and read state permit forms and Form 3-186A; merge inspection-readiness packets.
- **sqlite / duckdb** — keep the weight log, feeding record, and acquisition/disposition register queryable across seasons.
- **weather** — flying conditions and abatement scheduling depend on wind, temperature, and visibility.

## Legal & Ethical Considerations

- **This workspace organizes communications; it is not legal or veterinary advice.** U.S. falconry is governed by the Migratory Bird Treaty Act and federal rule **50 CFR 21.82** (the 2022 reorganization moved it from §21.29), administered through each **state's** wildlife agency under its own — often stricter — regulations. Verify current requirements with your state coordinator before filing anything.
- **Permits, classes, and species limits are real constraints.** Apprentices may keep one raptor of a permitted species (commonly an American kestrel or red-tailed hawk; states vary). Take from the wild, banding/marking, and acquisition/disposition are all reportable events.
- **Welfare first, always.** Weight management is husbandry, not punishment. A bird that is "going light," fluffed, or off its food needs a vet, not a lower flying weight.
- **CITES and protected species.** Moving certain raptors across borders, or possessing eagles and some falcons, carries additional permit and treaty obligations. Never assist with the illegal take or trade of protected birds.
- **Abatement is regulated work.** Commercial bird-abatement falconry requires the appropriate permit endorsement and must stay inside the conditions of that permit and any local wildlife-control rules.

## Technical References

- [50 CFR Part 21 — Migratory Bird Permits](https://www.ecfr.gov/current/title-50/chapter-I/subchapter-B/part-21) — federal permit framework; falconry standards now at §21.82.
- [USFWS Migratory Bird Program — Falconry](https://www.fws.gov/service/falconry) — federal overview, state-administration model, and forms.
- [North American Falconers Association (NAFA)](https://www.n-a-f-a.com/) — the principal U.S. falconry organization (founded 1961); journals, meets, conservation.
- [International Association for Falconry (IAF)](https://www.iaf.org/) — global federation; UNESCO Intangible Cultural Heritage listing of falconry.
- [The Modern Apprentice](https://www.themodernapprentice.com/) — widely-used free educational resource for apprentice falconers (equipment, manning, weight management).
- [The Archives of Falconry (The Peregrine Fund)](https://peregrinefund.org/archives-of-falconry) — historical and reference archive in Boise, Idaho.
- [Association of Avian Veterinarians (AAV)](https://www.aav.org/) — find an avian vet; clinical resources for raptor health.
- *North American Falconry and Hunting Hawks* — Beebe & Webster (the standard apprentice text).
- *A Hawk for the Bush* and *The Passage Peregrine* — Jack Mavrogordato (classic husbandry/training references).

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available. The workspace is self-contained without it.
