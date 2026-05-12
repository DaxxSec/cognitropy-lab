# Operating Environment

Populated by `/onboard`. The agent reads this before recommending tools.

## Hardware / Field Kit

- **Planning workstation:** [Laptop OS, encryption posture, offline GIS installed Y/N]
- **Vehicle comms / OBC:** [Vehicle make-model, OBC fitted, encrypted radio model]
- **Advance team kit:** [Bodycams, RF spectrum scanner, IR camera, surveillance-detection kit]
- **Counter-surveillance assets:** [Static, mobile, technical]

## Software (Detail / Planner Side)

- **GIS:** [QGIS / ArcGIS / Google Earth Pro / paper]
- **Offline maps:** [Organic Maps / OsmAnd / Gaia GPS / printed atlas]
- **GPX/KML editor:** [GPX Studio / Gaia Pro / hand-edited XML]
- **Common Operating Picture:** [WinTAK / iTAK / ATAK-CIV / none]
- **Markdown / brief generation:** [Pandoc → PDF for printed briefs]
- **Comms management:** [Encrypted-radio programming software]
- **OPSEC:** [Disk encryption, signed-image PDFs, sanitized chat policies]

## Connectivity Posture

- **Planning cell:** Always on encrypted network, no movement-day data on personal devices.
- **Field:** Encrypted handheld VHF/UHF primary; cellular fallback (with awareness that cell can be jammed); satellite for overseas Tier-1 work.
- **Backup:** Map-and-compass plus printed brief in every vehicle. The brief survives total comms loss.

## Open-Source Inputs

- U.S. State Dept Travel Advisories
- OSAC daily summaries (where the user holds membership)
- Host-nation MFA travel advisories (UK FCDO, GAC Canada, AusGov DFAT)
- Open-source incident trackers (ACLED for AOR-level conflict density)
- Local press / police blotter for the AOR

The agent never recommends scraping closed government systems or social media at scale; the principle is *publicly accessible, ethically gathered* OSINT only.

## Storage Layout

- `outputs/` — generated briefs and AARs (sanitized).
- `outputs/<window>/sensitive/` — confidential-do-not-sync — true names, addresses, photos. Encrypted disk image when possible.
- `planning/` — active route plans and pivots.
- `work-log/` — chronological session logs.
- Off-workspace: encrypted backup of full sensitive set, retained per the contracting office's retention policy.
