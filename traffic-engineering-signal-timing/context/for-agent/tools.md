# Tools & Integrations

## Capacity & Coordination

### Synchro / SimTraffic (Trafficware / Cubic)
- **Purpose:** HCM-based capacity, signal coordination optimizer, microsimulation of finalist plans
- **Inputs:** `.syn` file (network), volumes, signal phasing
- **Optimizers:** CycleLength, Splits, Offsets — solve sequentially
- **Limit:** uses HCM 6 by default (verify HCM 7 add-on); proprietary file format

### HCS (Highway Capacity Software, McTrans)
- **Purpose:** authoritative HCM 7 reference implementation
- **Best for:** independent verification of Synchro / Vistro outputs
- **Files:** `.xhs` per intersection

### TRANSYT-7F (McTrans, FHWA-derived)
- **Purpose:** macroscopic coordination optimization with Performance Index objective
- **Strength:** classic platoon dispersion + bandwidth optimization
- **Use here:** offset solver for the eco-weighted bandwidth objective

### Vissim (PTV)
- **Purpose:** microscopic simulation; second-by-second vehicle traces for MOVES drive-cycle export
- **Inputs:** `.inpx` network, signal logic via VAP/VisVAP or external API
- **Output:** trajectory `.fzp` files → operating-mode bins

### AIMSUN Next
- **Purpose:** mesoscopic + microscopic; commonly used for big networks
- **Strength:** SCATS/SCOOT emulation built-in

### SUMO (Eclipse, open-source)
- **Purpose:** microsimulation; free; programmable via TraCI Python API
- **Strength:** scriptable for batch Pareto search; well-suited to optimization loops
- **Outputs:** FCD (floating-car data) per second per vehicle

### PuLP (Python)
- **Purpose:** linear programming for offset / bandwidth optimization
- **Use here:** in-process LP for the multi-band coordination objective

## Emissions

### EPA MOVES4 (2024)
- **Purpose:** authoritative project-level emissions for SIP/CMAQ submittals
- **Scale:** national / county / project
- **Inputs:** Project-level needs link table (link-ID, length, speed, road-type, source-type frac), drive-schedule (operating-mode bin distribution OR second-by-second), meteorology
- **Output:** g/hr per pollutant per source-type per process per link
- **Run mode:** GUI for one-off, command-line MOVESLooper for batch
- **Caveat:** California uses CARB EMFAC2021 instead

### CMEM (UC Riverside)
- **Purpose:** modal emissions, second-by-second engine-load based
- **Use here:** fast inner-loop for Pareto search; resource-friendly
- **Implementation:** the CMEM modal coefficients are seeded in `resources/cmem-modal-fuel-rates.md`

### EMFAC2021 (CARB, California-only)
- **Purpose:** CA-specific mobile-source emissions; required for any CA project conformity
- **Output:** mass emissions per pollutant per fleet/year/area

## Data Acquisition

### ATSPM (Automated Traffic Signal Performance Measures)
- **Origin:** UDOT open source; widely deployed (FDOT, GDOT, ITD, MnDOT, cities)
- **Reports:** Purdue Coordination Diagram, Approach Volume, Split Monitor, Pedestrian Delay, Yellow + Red Actuations
- **Database:** typically SQL Server (UDOT) or Postgres (later forks); 10 Hz event records
- **Use here:** primary baseline data source; query directly via `mcp__postgres` if available

### NEMA / NTCIP Event Logs
- **Format:** EnumeratedEventCode + EventParam + Timestamp at 10 Hz
- **Codes:** 0–10 phase, 21–24 ped, 81–82 detector, 90–91 split monitoring
- **Retrieval:** controller-dependent; typically pulled via central system or SD card

### Counts / Volumes
- **Permanent counters:** local agency ATR (Automatic Traffic Recorders), HPMS submission
- **Project counts:** TMC vendors (Quality Counts, Idax, Miovision, Counting Cars)
- **Bluetooth/Wi-Fi re-ID:** TrafficCast, Acyclica, Iteris ClearGuide for travel-time

## Reporting

### Mermaid / Matplotlib
- **Purpose:** time-space diagrams, Pareto frontiers, emissions stack charts
- **Output:** PNG/SVG inline in `outputs/`

### NEPA / CEQA Templates
- **FHWA CE template:** [FHWA NEPA Documentation Toolkit](https://www.environment.fhwa.dot.gov/)
- **CARB CEQA Air Quality Handbook** (CA only)

## Optional MCP Servers (Configure in `.mcp.json`)

- **filesystem** — read controller exports (.csv, .syn), write timing plans
- **shell** — invoke MOVES4 batch, SUMO, TRANSYT-7F runs
- **python** — Pareto search, plot generation, time-space diagrams
- **postgres** — direct ATSPM database query
- **sqlite** — local cache of event-log slices
