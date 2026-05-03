# Batch Record Card — Canonical Schema

This is the template used by `/batch-log` for every studio session. The schema is deliberately strict — `/lineage-trace` and `/post-mortem` rely on consistent field names to grep through months of records.

## File Path
`work-log/<YYYY-MM-DD><seq>.md` where `<seq>` is `A`, `B`, `C`… for sessions on the same date.

## Template

```markdown
# Batch Record: <YYYY-MM-DD>-<seq>

## Header
- **Batch ID:** <YYYY-MM-DD>-<seq>
- **Artist:** <name>
- **Glass family:** <one of: bullseye-90 | system-96 | effetre-104 | reichenbach-104 | kugler-104 | borosilicate-33>
- **Studio:** <studio identifier from environment.md>
- **Pre-session glory hole soak (°C):** <measured>
- **Pre-session lehr program loaded:** <program ID + summary>
- **Pre-session ambient (°C / RH):** <e.g., 22 / 55>
- **Session start:** <HH:MM local>
- **Session end:** <HH:MM local — populated at closeout>

## Inputs (Lineage Block)

### Base glass
- Source: <melt batch ID OR "fresh from supplier batch <ID>">
- Composition notes: <any cord, devit-prone, etc.>

### Color rods / frit / cane
| # | Color | Supplier | Lot ID | COE | Mass used (g, est) | Prior batch (if leftover) |
|---|-------|----------|--------|-----|---------------------|----------------------------|
| 1 | | | | | | |
| 2 | | | | | | |

## Planned Forms
| # | Form | Spec | Sim verdict | Scenario test summary |
|---|------|------|-------------|------------------------|
| 1 | <name> | planning/form-<slug>-v<n>.md | green/yellow/red | e.g., "7/7 green" or "1 yellow: gather over-mass — accepted" |

## In-Session Log (append-only)

(One entry per significant event. Format: `HH:MM | type | details`)

- HH:MM | gather | piece-1, gather 1, ~320 g
- HH:MM | operation | marver, 5 s
- HH:MM | reheat | piece-1, glory hole 1170 °C
- HH:MM | operation | block, 3 s
- HH:MM | anomaly | piece-1, surface bubble at neck
- HH:MM | lehr load | piece-1, program 96-12mm-standard, position front-left
- ...

## Outcomes (closeout)

| Piece ID | Form | Mass (g) | Geometry h×w×d (mm) | State | Lehr position |
|----------|------|----------|----------------------|-------|---------------|
| | | | | finished/abandoned | |

### Lehr program actually run
- Program ID: <as loaded vs. as planned>
- Controller deviations: <none / list>

### Inventory delta
- Color rod lots: <consumed (g), leftover returned to stock with lot tag>
- Cullet/billet: <approx mass consumed>

## Successional Follow-Ups

(Placeholder rows added at closeout; filled in on the scheduled dates)

| Piece ID | 24h date | 24h obs | 7d date | 7d obs | 30d date | 30d obs | 90d date | 90d obs |
|----------|----------|---------|---------|--------|----------|---------|----------|---------|
| | | | | | | | | |

## Diagnostic Followups

(Populated by `/post-mortem` when a piece fails)

- Piece <id> | <date> | Mode <n>: <name> | Confidence <high/medium/low> | <link to post-mortem file>

## Notes

(Free text for reflection, anomaly explanations, technique experiments.)
```

## Field Conventions

- **`<seq>`:** uppercase letter `A`, `B`, `C`, … per session on the same date
- **Times:** 24-hour `HH:MM`, local
- **Mass:** grams, rounded to nearest 5 g for gathers, nearest 1 g for finished pieces
- **Temperature:** °C; if a measurement is missing or estimated, prefix with `~`
- **Lot IDs:** copy the supplier's printed label exactly; if unlabeled, generate one as `<supplier-short>-<YYYY-MM>-<color>-<n>` and apply a physical label to the rod bundle
- **Piece IDs:** `<batch-id>-piece-<n>`, e.g., `2026-05-03-A-piece-1`

## Why This Strict Schema

A loose record is fine for one session. A loose record across 200 sessions over a year is unsearchable. The schema is the cost of admission for `/lineage-trace` and clustered `/post-mortem` to work.

If a field is genuinely unknowable for a given session (e.g., no pyrometer means no measured glory hole temp), use the literal token `unknown` rather than leaving the field blank — `/lineage-trace` distinguishes "not measured" from "data lost."
