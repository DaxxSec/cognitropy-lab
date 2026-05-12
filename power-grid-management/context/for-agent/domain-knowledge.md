# Domain Knowledge: Power Grid Management — Spatial Frame

## Discipline Overview

The electric power grid is a real-time system in which generation must match load continuously, with no economically viable storage at utility scale for most of the 20th century and still limited at the beginning of the 2030s. The grid is also inherently geographic — generation, transmission, distribution, and load are located in space, connected by physical conductors that follow terrain and rights-of-way.

Power grid management spans operations (real-time balancing, contingency response, restoration), planning (capacity expansion, asset renewal, interconnection), maintenance (inspection, vegetation, equipment condition), and increasingly cyber-physical security. A spatial lens adds value to all four.

**Core principle for this workspace:** *Where* an asset, event, or decision sits in space frequently constrains *what* it can do. A substation in a wildland-urban interface has different priorities than an urban one. A transmission line through a flood plain has different maintenance needs than one on a ridgeline. The agent is trained to surface this constraint rather than treat the grid as abstract topology.

---

## Grid Segments and Voltage Classes

### Bulk Transmission
- Voltages: 230, 345, 500, 765 kV in North America; 400 kV typical in Europe
- Role: long-distance power transfer between generation and load centers
- Spatial character: long, often remote rights-of-way; typically meshed topology
- Primary reliability framework: NERC TPL, FAC, PRC standards

### Sub-Transmission
- Voltages: 69, 115, 138, 161 kV typically
- Role: regional bulk power delivery, supply to distribution substations
- Spatial character: mixed — some dense, some rural
- Often jointly owned / operated by transmission and distribution entities

### Primary Distribution
- Voltages: 4, 12, 13.8, 25, 34.5 kV common
- Role: carry power from distribution substations to customer transformers
- Spatial character: follows streets and customer density; mostly radial with tie switches
- Governed by state PUC reliability metrics (SAIDI, SAIFI, CAIDI, MAIFI)

### Secondary Distribution
- Voltages: 120/240 V single-phase; 208/120 V and 480/277 V three-phase
- Role: service to end-use customers
- Spatial character: dense, sub-block scale; often not in the authoritative GIS at full fidelity

### Distributed Energy Resources (DER)
- Rooftop solar, utility-scale solar farms, wind farms, community solar, battery storage, EV chargers
- Role: shifting from "load at the edge" to "bidirectional power at the edge"
- Spatial character: highly variable — from single-customer to multi-100 MW plants
- IEEE 1547 governs interconnection requirements

---

## Spatial Data Primer

### Vector Layers Every Grid Analyst Works With

- **Substations** — point features. Typical attributes: voltage in/out, capacity (MVA), ownership, criticality rating (NERC CIP-014 designation), year built.
- **Transmission lines** — line features. Attributes: voltage, conductor type (ACSR, ACCR, ACSS), rating (summer/winter normal/emergency), circuit ID, supporting structures (wood H-frame, steel lattice, monopole).
- **Distribution feeders** — line features with connected network topology (so flow direction makes sense under a given switch configuration). Often have sub-feeders, laterals, taps.
- **Structures (poles, towers)** — point features along lines.
- **Switches, reclosers, fuses, capacitor banks** — point features on distribution.
- **Transformers (both substation and distribution)** — point features. Distribution transformer GIS is sometimes coarse.
- **Service territory / franchise boundary** — polygon features.

### Raster Layers Often Overlaid

- **Digital Elevation Model (DEM)** — slope, aspect, elevation affect vegetation, access, and insulation requirements.
- **Canopy Height Model (CHM)** — from LiDAR; critical for vegetation management.
- **Fire-weather indices** — fuel moisture, Haines index, Red Flag Warning zones.
- **Load density** — customer-weighted or measured MW/mi².
- **Lightning flash density** — multi-year climatology for stroke-prone areas.
- **Flood zones** — FEMA FIRM panels.

### Coordinate Reference Systems

- **WGS84 (EPSG 4326)** — lat/lon; fine for collection, **do not use for distance or area** operations.
- **Web Mercator (EPSG 3857)** — for web mapping display; distorts area and distance with latitude.
- **NAD83 State Plane** — US state-specific, accurate for measurements within one state.
- **UTM** — 6° zones globally, accurate for measurements within one zone.
- **Lambert Conformal Conic / Albers Equal-Area** — for large regional maps.

**Rule of thumb:** Collect and distribute in WGS84; analyze in a projected CRS appropriate to the scope; re-project at the output stage if needed.

---

## Standards Framework

### US Reliability (NERC)
- **TPL (Transmission Planning):** system performance under various contingencies
- **FAC (Facilities):** ratings, connection requirements, vegetation management (FAC-003)
- **PRC (Protection):** protective relay requirements and misoperation reporting
- **CIP (Critical Infrastructure Protection):** cyber and physical security
  - **CIP-014:** physical security of critical substations
  - **CIP-002 through CIP-013:** BES cyber systems

### International / European
- **ENTSO-E Network Codes:** connection codes, operation codes, market codes
- **IEC 60826:** overhead line loading (wind, ice, combined)
- **IEC 61850:** substation automation and communications

### Design and Safety
- **IEEE C2 / NESC (US National Electrical Safety Code):** clearances, grounding, work practices
- **IEEE 1547 / 1547.1:** DER interconnection and testing
- **IEEE 81:** measuring earth resistance

### Data Modeling
- **CIM (IEC 61968 / 61970 / 62325):** Common Information Model for electrical assets, operations, and markets
- **Multispeak:** alternative distribution-focused integration spec
- **OGC standards (WFS, WMS, WMTS, WCS):** for sharing spatial data over the web

---

## Operational Concepts Worth Having Handy

### Reliability Indices
- **SAIDI** — System Average Interruption Duration Index (minutes per customer per year)
- **SAIFI** — System Average Interruption Frequency Index (events per customer per year)
- **CAIDI** — Customer Average Interruption Duration Index = SAIDI / SAIFI
- **MAIFI** — Momentary Average Interruption Frequency Index
- IEEE 1366 is the reference standard for these indices

### Contingency Vocabulary
- **N-1** — loss of one element (line, transformer, generator)
- **N-1-1** — loss of one element followed by a second loss after system readjustment
- **N-2** — simultaneous loss of two elements
- **Credible contingency** — the set of faults the system must survive per NERC TPL / utility planning criteria

### Restoration Concepts
- **Black start** — restoring a grid from total shutdown using units that can start without grid supply
- **Bottom-up restoration** — building islands around black-start units, then resynchronizing
- **Normally-open tie** — a switch that is open under normal ops but closed under restoration to reconfigure

### DER-Era Concepts
- **Hosting capacity** — how much DER a feeder can accept without voltage/thermal issues
- **Back-feed** — power flowing toward the substation because DER exceeds local load
- **Islanding (DER context)** — inverter-based resources inadvertently supplying a grid segment after the utility source is disconnected; IEEE 1547 requires anti-islanding detection

---

## Historical Events Useful for Spatial Reasoning

- **Northeast Blackout (2003)** — cascading tripping across the US/Canada interconnection. Vegetation contact on a 345 kV line in Ohio initiated it; alarm system failure and inadequate situational awareness let it cascade. Geographic scale: ~50 M customers lost power. Lesson: real-time visibility across the whole interconnection matters; FERC/NERC reliability rules became mandatory after.
- **ERCOT February 2021** — extended sub-freezing temperatures across Texas caused generation fleet to drop below demand; rolling load shed lasted days. Spatial dimension: weatherization of generation assets varied geographically; the physical footprint of the cold snap was the proximate driver.
- **PG&E Camp Fire (2018)** — failure of a transmission line hook caused an ignition that led to the deadliest wildfire in California history. Drove a generation of PSPS (Public Safety Power Shutoff) practices and wildfire risk spatial modeling.
- **Western Interconnection 1996 Blackouts (August 10 and July 2)** — cascading outages across the WECC system; drove investment in transient-stability analysis and RAS (Remedial Action Schemes).
- **Ukraine 2015 and 2016** — coordinated cyber attacks on distribution utilities caused outages for ~230,000 customers (2015) and a substation-level outage in Kyiv (2016). First public confirmation of deliberate cyber-physical attacks on grid SCADA. Spatial lens: the attacker moved through geography as they moved through networks.

Each of these events has extensive public post-mortem material; the agent should direct users to the primary reports (NERC, FERC, RAIB-equivalent national bodies, company 10-Ks, E-ISAC postings) rather than paraphrase secondhand.

---

## Cyber-Physical Intersection

The grid's spatial frame matters to security analysts for several reasons:

1. **Asset blast radius.** When a SCADA RTU is compromised, its physical span (substations + feeders controlled) bounds the impact. Spatial visualization makes this scope immediately clear.
2. **Access path modeling.** Physical security (CIP-014) and cyber security share a geography — the substation fence, the communication microwave path, and the SCADA VLAN all pass through points on a map.
3. **Correlating SIEM / ICS alarms with operational events.** A SCADA anomaly that coincides spatially with a protective relay misoperation is a different signal than either in isolation.
4. **Third-party and supply-chain exposure.** Connected vendor systems, shared rights-of-way, and jointly-owned assets all create spatial dependencies that don't appear on an IT network diagram.

The agent should treat cyber-physical analysis as a first-class workflow, not a side topic — see `context/for-agent/workflows.md` workflow 6.
