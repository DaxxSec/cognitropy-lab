# Standards and References Guide — Power Grid Management (Spatial)

A curated list of standards, data sources, and references the analyst will reach for most often. Organized by scope.

---

## US Bulk-Power Reliability (NERC)

- **NERC Reliability Standards** — nerc.com/pa/Stand/Pages/ReliabilityStandards.aspx
  - TPL-001 (Transmission System Planning Performance Requirements)
  - FAC-003 (Transmission Vegetation Management)
  - FAC-008 (Facility Ratings)
  - PRC-004 (Protection System Misoperation Identification)
  - CIP-002 through CIP-014 (Cyber and Physical Security)
- **NERC Event Analysis reports** — nerc.com/pa/rrm/ea/Pages/EA-Program.aspx — public post-event reports with geographic scope noted.

## US Distribution Reliability

- **IEEE Std 1366** — Guide for Electric Power Distribution Reliability Indices (SAIDI, SAIFI, etc.)
- **IEEE Std 1547** and **1547.1** — DER Interconnection and Testing
- **State Public Utility Commission filings** — many PUCs publish annual reliability metrics geographically
- **APPA, NRECA reliability databases** — for munis and coops

## Design, Safety, Construction

- **IEEE C2 / NESC (National Electrical Safety Code)** — clearances, grounding, overhead and underground practices
- **ASCE Manual 74** — transmission line structural loading
- **IEEE Std 81** — earth resistance measurement
- **IEEE Std 693** — seismic design of substations
- **NERC FAC-008 / FAC-009** — facility ratings methodology

## European and International

- **ENTSO-E Operational Handbook** — europe-wide operating policies
- **IEC 60826** — loading and strength of overhead lines
- **IEC 61850** — substation communication
- **ISO/IEC 27019** — information security for process control in the energy industry

## Data Models and Formats

- **IEC 61968 / 61970 / 62325 (CIM)** — standards-new.iec.ch
- **MultiSpeak** — multispeak.org — distribution-focused integration spec
- **OGC standards** — ogc.org — WMS, WFS, WCS, GeoPackage, GeoJSON, KML, Simple Features
- **CF Metadata Conventions** — cfconventions.org — for NetCDF climate data

## Cyber-Physical Security

- **NIST SP 800-82** — Guide to Industrial Control Systems (ICS) Security
- **DOE C2M2** — Cybersecurity Capability Maturity Model (energy sector)
- **E-ISAC** — eisac.com — Electricity Information Sharing and Analysis Center
- **CISA ICS-CERT advisories** — cisa.gov/uscert/ics
- **IEC 62351** — power system communication security
- **NERC CIP-013** — supply chain risk management

## Spatial Data Sources (US)

- **USGS National Map** — nationalmap.gov — topography, hydrography, boundaries
- **FEMA NFHL** — msc.fema.gov — flood hazard layer
- **NOAA / NWS** — weather.gov/documentation — forecast and observation APIs
- **NIFC Integrated Reporting of Wildland-Fire Information (IRWIN)** — nifc.gov — wildfire data
- **LANDFIRE** — landfire.gov — fuel models
- **USGS 3DEP** — 3dep.usgs.gov — LiDAR-derived elevation
- **HIFLD Open** — hifld-geoplatform.opendata.arcgis.com — critical infrastructure geography (public portions)

## Spatial Data Sources (Global)

- **Copernicus / Sentinel Hub** — sentinel-hub.com — free Sentinel-1/2/3 imagery
- **Landsat Collections (USGS)** — earthexplorer.usgs.gov
- **OpenStreetMap** — openstreetmap.org — free vector basemap
- **Global Energy Monitor Power Plant Tracker** — globalenergymonitor.org — coarse global generation geography

## Reports Worth Reading (Spatial Emphasis)

- **NERC State of Reliability** (annual) — nerc.com — aggregate reliability trends with regional breakdown
- **EIA Form 860 / 861 / 923** — eia.gov — utility and plant-level data; 860 has plant coordinates
- **CAISO / ERCOT / PJM / MISO / NYISO / ISO-NE annual reports** — ISO-specific reliability and operational summaries
- **RAIB-equivalent reports for grid (NTSB, CSB)** — when investigations involve grid assets

## Training and Community

- **IEEE Power & Energy Society** — pes-gm conferences, free standards drafts for members
- **CIGRÉ** — cigre.org — international technical working groups; exceptional breadth of technical papers
- **EPRI** — epri.com — Electric Power Research Institute; many free reports
- **OpenDSS Community** — sourceforge.net/projects/electricdss
- **Python for Grid Analysis** — the `pandapower` project documentation is a good self-study resource
