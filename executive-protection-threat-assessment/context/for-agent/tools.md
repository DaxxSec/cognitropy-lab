# Tools & Integrations

This file describes the external tools, data sources, and reference databases the agent should reach for during the workflows. Configure access in `environment.md`.

## Mapping & GIS

| Tool | Use | Cost / access |
|------|-----|---------------|
| Google Earth Pro | Aerial imagery for chokepoint / venue advance | Free |
| ArcGIS / QGIS | Route geojson authoring, layer overlays | ArcGIS commercial; QGIS free |
| OpenStreetMap (Overpass API) | Programmatic feature extraction (intersections, narrow streets, bridges) | Free, attribution required |
| OnX / Gaia GPS | Off-road / rural exfil planning | Subscription |

## Crash-test reference data

| Source | What it gives you | Notes |
|--------|------------------|-------|
| NHTSA NCAP database | Vehicle-specific frontal/side test results, star ratings, dummy injury values | Free, US-market vehicles |
| IIHS small-overlap, side, roof-strength ratings | Cabin intrusion measurements (cm) at multiple measurement points | Free; key for §2.5 of domain knowledge |
| Euro NCAP test reports | EU-market vehicles, MPDB and far-side test data | Free; complements NHTSA for European inventory |
| ASTM F2656 / PAS 68 / IWA 14-1 ratings | Bollard / barrier crash ratings — what attacker mass × velocity is stopped | Vendor cut-sheets list ratings |

## Risk assessment frameworks

| Source | Use |
|--------|-----|
| NIST SP 800-30 r1 | Risk assessment methodology (likelihood × impact, evidence grading) |
| ISO 31000 | Generic risk management vocabulary |
| ASIS PSP body of knowledge | EP-specific risk assessment |
| FEMA RMS-series publications | Vehicle-borne and IED attack mitigation reference |
| DHS CISA — Vehicle Ramming Attack Mitigation | Bollard / barrier reference |

## OSINT (lawful, ToS-compliant only)

| Source | Use | Cautions |
|--------|-----|----------|
| OSAC (US State Department) | Country-level threat picture, sector reporting | Membership required for some content |
| Local LE public liaison releases | Crime trend, recent incidents | Cite specific bulletin number |
| FCC ID / equivalent | Identify communications equipment by FCC ID | Lookup only |
| FCO / FCDO travel advisories | Geographic-permissiveness rating | Update regularly |
| Reputable news (mainstream wire services) | Specific incident reports | Cross-source two outlets before grade B |

## Forbidden / discouraged

The agent does **not** use:
- Scraped social media in violation of platform ToS
- Purchased "skip-trace" data of dubious provenance
- Unauthorised access to LE / closed databases
- Doxxing services or "people search" databases that aggregate without consent

If a piece of information can only come from such a source, the workspace marks it "unattainable lawfully" rather than fabricating an evidence anchor.

## Local helpers (Python)

The workspace ships no code, but the agent will *write* the following helpers ad hoc when needed (with the `python` MCP server):

- **delta_v.py** — perfectly-inelastic ΔV calculator with attacker/protected mass and closing speed inputs
- **ke_partition.py** — kinetic-energy partitioner for the protected vehicle
- **bollard_lookup.py** — given attacker class & closing speed, return required F2656/PAS-68/IWA-14-1 rating
- **matrix_render.py** — render the 5×5 matrix as a Mermaid heatmap from a YAML cell list

Each helper is < 50 lines and lives transiently in `outputs/` for traceability.

## Comms / liaison

- Encrypted detail comms (e.g. Signal, branded handheld with secure mode) — for live coordination, *not* for storing the workspace's analytic outputs
- Pre-arranged hospital MoU (where applicable)
- LE liaison contact card in `outputs/` (codename only)
