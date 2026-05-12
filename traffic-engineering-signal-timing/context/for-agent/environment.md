# Environment Setup

> Populated by `/onboard` — replace placeholders with your details.

## Controllers
<!-- Per intersection: make (Econolite, McCain, Siemens, Trafficware, Intelight),
     model (ASC/3, Cobalt, m60, 980, Kadence), firmware version,
     NTCIP 1202 v03A object support level, central system (ATMS, MaxView, Centracs, ATSPM-only). -->

## Detection
<!-- Per approach: presence (loops/video/radar) or count;
     dilemma-zone detection deployed?
     pedestrian pushbutton (audible/APS)?
     bike-specific detection? -->

## Communications
<!-- Fiber / cellular / wireless backhaul per intersection.
     Bandwidth available for high-resolution event log retrieval. -->

## Data Sources
<!-- ATSPM URL/credentials (read-only),
     turning movement count files (CSV/PDF),
     Synchro/HCS files, Vissim/SUMO models if any,
     local MPO HPMS / fleet mix dataset. -->

## Software Stack
<!-- Synchro 11+, Vissim 2024, AIMSUN Next, SUMO 1.20+, HCS 2024, TRANSYT-7F,
     EPA MOVES4, EMFAC2021 (if CA), Python 3.10+ (pandas/numpy/scipy/pulp/matplotlib). -->

## Compute Resources
<!-- Local laptop, agency compute server, AWS instance.
     MOVES4 project-level runs need ~4 GB RAM and SQLite I/O.
     SUMO microsimulation scales with intersection count and run length. -->

## Air-Quality Basin Reference
<!-- EPA non-attainment status by pollutant,
     local air district contact (e.g., SCAQMD, BAAQMD, WMATC),
     latest county-level MOVES default fleet release year. -->
