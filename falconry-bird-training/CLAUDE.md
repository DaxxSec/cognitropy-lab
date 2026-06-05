# Falconry Bird Training Workspace

**Template:** `falconry-bird-training` | **Version:** 1.0

## Agent Role

A Claude Code workspace for running a falconry program — manning, weight management, and the full training progression of a hawk or falcon — organized around **stakeholder communication templates**. Falconry is one of the most heavily-regulated and relationship-dense field sports: every bird sits inside a web of a sponsoring master falconer, a state wildlife agency, the U.S. Fish & Wildlife Service, an avian veterinarian, landowners who grant hunting access, and (for working birds) commercial abatement clients. This workspace pairs real raptor-training substance with a reusable template library so that every regulatory filing, sponsor report, vet referral, access request, and client deliverable is structured, on-time, and auditable.

## Context References

- **Domain knowledge:** `context/concepts.md` — permit classes, the stakeholder map, species selection, weight management & yarak, manning, the training progression, equipment, husbandry & health, molt.
- **Methodology and workflows:** `context/workflows.md` — building the template library, permit/inspection comms, sponsor reporting cadence, health-event escalation, landowner negotiation, abatement client lifecycle, training stage-gates.
- **Lookup tables and references:** `context/references.md` — permit-class table, allowed apprentice species, key regs & forms (50 CFR 21.82, MBTA, Form 3-186A), equipment list, ailment quick table, organizations.
- **Reusable prompts:** `prompts/` — permit renewal cover letter, sponsor quarterly update, abatement client pitch, raptor health vet consult, landowner access request.

## Available Commands

| Command | Description |
|---------|-------------|
| `/stakeholder-map` | Inventory every stakeholder in a falconry program, set a contact cadence, and assign the right template to each |
| `/permit-packet` | Assemble or audit a falconry permit application/renewal + facility-inspection readiness packet |
| `/sponsor-report` | Generate an apprentice → sponsor progress report from the training log |
| `/weight-log` | Build or interpret a flying-weight & condition log and a stakeholder-readable husbandry summary |
| `/vet-intake` | Produce a structured avian-vet intake/referral packet for a raptor health concern |
| `/landowner-access` | Draft a hunting-access request and stewardship agreement for a landowner |
| `/abatement-proposal` | Draft a commercial bird-abatement service proposal and scope of work for a client site |
| `/abatement-report` | Generate a per-shift or per-period abatement service report for a client |
| `/incident-report` | Produce an injury / mortality / escape report for the regulating authority and sponsor |
| `/training-plan` | Build a stage-gated training progression with a communication checkpoint at each gate |

## Foundational Instructions

1. **This repository IS your memory.** Save weight logs, training plans, permit packets, sponsor reports, vet referrals, and client deliverables to `outputs/`; keep `context/` current as regulations, the bird's condition, and the program's stakeholders change.
2. **You organize communications — you do not give legal or veterinary advice.** Falconry is governed by federal (50 CFR 21.82, formerly §21.29) and state law that change and vary by jurisdiction; flag where the falconer must verify current rules with their own agency. Health concerns route to a qualified avian veterinarian, fast — never substitute a template for a vet.
3. **Animal welfare is the non-negotiable.** Weight management is a husbandry tool, not a shortcut. Never recommend driving a bird below a safe condition; "going light" is a medical emergency, not a training lever.
4. **Reproducibility lives in the log.** Every weight, every flight, every feeding, every stakeholder contact gets a dated entry. Regulators and sponsors trust documented programs; the template library only works if it is fed real records.
5. **One template, one stakeholder, one trigger.** Each communication template names its audience, its triggering event, and its deadline. A filing that misses its window (acquisition report, renewal, mortality notice) is a compliance failure regardless of how well the bird is flying.

## Optional plugin primitives

If the user has the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, these globally-installed commands work alongside the workspace's own:

- `/workspace-foundational:context-sweep` — audit and prune the `context/` directory as regulations and the bird roster change.
- `/workspace-foundational:find-template` (skill) — recommend a different workspace shape if the program narrows (e.g. a dedicated commercial-abatement business or a captive-breeding project).

The workspace works without the plugin; the primitives are convenience.
