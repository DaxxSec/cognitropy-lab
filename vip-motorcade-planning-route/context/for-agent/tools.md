# Tools & Integrations

Practical tool references for route planning, scoring, and brief generation. The agent does not assume any specific stack — it adapts to what the user has.

## GIS & Route Drawing

- **QGIS** (open source, recommended for OPSEC) — load OSM extracts (Geofabrik), draw segments as line features, attribute them with the matrix scores. Plugins: QuickOSM, MMQGIS, MapSwipe Tool.
- **ArcGIS Pro** — if the unit is already on Esri. Use Network Analyst for travel-time variance.
- **Google Earth Pro** (offline-capable) — useful for line-of-sight terrain analysis but high OPSEC cost (account, history, query logs); avoid for sensitive work.
- **gpsbabel** — convert between GPX, KML, GeoJSON, CSV. Useful for piping route data between tools.

## Offline / Field Maps

- **Organic Maps** (iOS / Android, OSM-based) — fully offline; preferred for principal-side staff.
- **OsmAnd** (Android, advanced OSM editor) — supports custom GPX overlays.
- **Gaia GPS** — strong topo / off-road; useful for rural and overland legs.
- **Maps.me** — simple offline; reduced feature set since 2022 but still functional.

## COP / ATAK

- **ATAK-CIV / iTAK / WinTAK** — civil-tier Team Awareness Kit. Useful for live-running an advance team across an urban AOR. Requires server (TAK Server / FreeTAKServer) and proper data discipline (no live position data leaving local network without encryption).
- **Civilian alternatives:** Briar / Element (Matrix) for encrypted location-share when ATAK overkill.

## Risk-Matrix Implementations

- **Spreadsheet-native:** the matrix is trivially a Google Sheet / Excel — but those leak metadata. For sensitive work use offline LibreOffice Calc and never sync.
- **Python (`risk_matrix.py` reference):** simple `(L, I) → band` + roll-up calculations. The agent will write a small, self-contained script if the user wants programmatic scoring (no external deps; stdlib only).
- **Markdown tables:** for briefs, render the matrix as a markdown table with cell-level color via emoji/text codes. Pandoc → PDF preserves formatting for the printed brief.

## Threat-Baseline Inputs

- **OSAC** ([osac.gov](https://www.osac.gov/)) — Overseas Security Advisory Council. Daily summaries, AOR threat assessments. Membership required for full access.
- **U.S. State Travel Advisories** ([travel.state.gov](https://travel.state.gov/)) — open. Country-tier risk pegs.
- **UK FCDO Travel Advice** ([gov.uk/foreign-travel-advice](https://www.gov.uk/foreign-travel-advice)) — open.
- **ACLED** ([acleddata.com](https://acleddata.com/)) — political violence / protest incident dataset. Useful for AOR conflict density.
- **GDELT** — global event database; high noise but useful for trend signals.
- **Host-nation police blotter / press** — case-by-case.
- **Embassy RSO daily security message** — when the principal is a USG-protected entity.

## Comms

- **Encrypted handheld VHF/UHF (Motorola APX series / Sepura SC-series / TASSTA TS / TETRA where lawful)** — primary on-net.
- **Cellular fallback:** WhatsApp/Signal voice acceptable for non-time-critical traffic; Signal preferred for messaging.
- **Satellite:** Iridium for true high-threat overseas; Inmarsat for slower data.

## Brief Generation

- **Pandoc** — convert `outputs/*.md` to PDF for printed briefs. Default template is fine; for branded briefs, use a unit LaTeX template.
- **wkhtmltopdf / weasyprint** — alternatives if Pandoc/LaTeX is too heavy.
- **Print discipline:** generate, print, sign, distribute, *destroy unused copies* per unit policy.

## What the Agent Will and Won't Touch

- The agent will draft markdown briefs, scoring sheets, and decision logs.
- The agent will compute risk-matrix products and roll-ups, and call out arithmetic errors in the user's manual scoring.
- The agent **will not** automatically pull from any external service without an explicit, sanctioned tool call from the user. This is to keep the OPSEC posture deterministic — every external query is a deliberate decision.
- The agent **will not** geocode real principal addresses against an online service; the user supplies geocoded waypoints from their offline GIS.
