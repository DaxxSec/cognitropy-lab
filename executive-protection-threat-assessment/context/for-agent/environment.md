# Operating Environment

> Populated by `/onboard`. Records the detail's tooling, vehicle inventory, and the geographic operating envelope.

## Detail composition

- **Headcount:** _e.g. 6 (1 detail leader, 1 advance, 2 shift, 2 drivers)._
- **Shift pattern:** _e.g. 12-on/12-off; full coverage / partial coverage._
- **Medical capability:** _TCCC-trained / EMT-B / paramedic / none._
- **Counter-surveillance assets:** _embedded SD operator yes/no; pre-deployable yes/no._
- **Comms platform:** _branded handheld with encryption / cellphone-only / tier-3 SatCom available._

## Vehicle inventory

For each available vehicle, record:
- Class (per `resources/crash-energy-reference.md`)
- Curb mass (kg)
- Hardening level (none / B4 / B6 / B7 BR / classified)
- Runflat capability
- Special features (smoke, ram bumper, intercom, hidden compartment for medical)
- Driver assigned and EVOC certifications

Example:
```
V1 — Lead — Chevy Suburban (full-size SUV, 2700 kg, B4, runflats) — Driver: Smith, EVOC L3
V2 — Principal — Cadillac Escalade (full-size SUV, 2750 kg, B6, runflats) — Driver: Jones, EVOC L4
V3 — Chase — Chevy Tahoe (full-size SUV, 2600 kg, none, runflats) — Driver: Diaz, EVOC L3
```

## Geographic envelope

- **Country / region of work:** _list of countries the detail currently operates in._
- **Permissive vs. semi-permissive vs. non-permissive ratings:** _per current State Dept / FCDO travel advisories._
- **Local LE liaison:** _named contact / unit / coordination cadence._
- **Hospital pre-coordination:** _which Level 1 / Level 2 trauma centres are pre-coordinated for the engagement geography._

## Compute & data

- **Tooling on hand:** _Google Earth Pro / ArcGIS / QGIS / OnX / GMaps Pro tier._
- **Threat-feed subscriptions:** _OSAC tier / commercial intel feed / none._
- **Workspace platform:** _local Mac/Linux/Windows; Cowork session; remote VM._
- **Storage:** _encrypted-at-rest, retention policy._

## Allowed sources

- **OSINT:** _list of vetted, ToS-compliant feeds._
- **Closed sources:** _LE liaison reports the detail can lawfully receive; any caveats._
- **Forbidden sources:** _explicit list of feeds the detail does NOT use (e.g. unvetted dark-web brokers, scraped social platforms in violation of ToS)._
