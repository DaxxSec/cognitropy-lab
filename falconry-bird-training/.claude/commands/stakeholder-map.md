# /stakeholder-map

Inventory every stakeholder in a falconry program, set a contact cadence, and assign each the right communication template — the organizing spine of this workspace.

## Inputs

- Program profile: permit class (apprentice/general/master), state, bird roster.
- Whether the falconer sponsors an apprentice, does commercial abatement, or both.
- Existing contacts: sponsor, state coordinator, avian vet, landowners, clients.

## Steps

1. Read the stakeholder table in `context/concepts.md`.
2. List every stakeholder that actually applies to this program — drop the ones that don't (e.g. no abatement → no client row).
3. For each, record the **document type**, the **trigger** (annual date / per-event / on-demand), and the hard **deadline** where one exists (renewal date, 3-186A 10-day window, mortality reporting).
4. Assign each stakeholder a command (`/permit-packet`, `/sponsor-report`, `/vet-intake`, `/landowner-access`, `/abatement-*`, `/incident-report`) and a `prompts/` template.
5. Set a contact cadence for relationship stakeholders (sponsor monthly/quarterly; landowner per season; client per shift).
6. Add a reminder for every dated deadline.

## Output

`outputs/stakeholder-map-YYYY-MM-DD.md`: a table of stakeholder → document → trigger → deadline → command → template, plus a calendar list of every dated obligation for the next 12 months.

## Notes

- Re-run whenever the program changes (new bird, new client, became a sponsor, moved states).
- Missing deadlines is the #1 compliance failure — this map exists to make them impossible to forget.
