# Environment: Power Grid Management Workspace

## Analyst Environment Profile

*Populate via `/onboard`. Default assumptions until then:*

**Work Context:** US electric utility (IOU, muni, coop, or federal) or ISO/RTO; analyst is internal or a consultant with NDA access. Non-US deployments (ENTSO-E region, Australia NEM, ERCOT-adjacent markets) are secondary but supported.

**Tooling Environment:** Mixed. Most utilities run a combination of:
- ESRI ArcGIS (Enterprise or Pro) as the authoritative GIS
- An EMS (Siemens Spectrum, GE / Alstom e-terra, Hitachi ABB Network Manager, OSI monarch)
- A DMS for distribution (OSI, Schneider ADMS, GE PowerOn, Oracle NMS)
- OMS for outage management (separate or DMS-integrated)
- Power-systems analysis tools (PSS/E, PowerWorld, PSLF at the bulk level; CYME / Synergi / OpenDSS at the distribution level)
- CIM-based integration layers in more modernized utilities

Python with `geopandas`, `networkx`, `pandapower`, `pandas`, and `shapely` is commonly available on the analyst side even when the authoritative tools are commercial.

## Notes for Grid Spatial Analyst

- The analyst's tooling stack is a strong signal of what outputs will actually be used. Ask which tool they will reproduce the work in before prescribing a workflow.
- Default to standards-based interchange formats (CIM, GeoJSON, GeoPackage) when describing data flows, because they survive tool migrations.
- Many utilities have a "GIS of record" separate from the "model of record" for planning. Reconciling those is a recurring source of analytical pain — acknowledge it when it comes up.
- Regulatory filing deadlines, storm season, wildfire season, and load seasonal peaks all shape what is operationally relevant at any given time. The agent should be aware of seasonality when proposing project timing.
- Cyber-physical analysis increasingly overlaps traditional spatial analysis — the same asset geography that supports reliability analysis also supports attack-surface reasoning. Treat as related but distinct domains.
