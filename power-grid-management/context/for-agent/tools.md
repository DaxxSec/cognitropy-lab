# Tools: Power Grid Management Workspace

## GIS Platforms

- **ESRI ArcGIS Pro / ArcGIS Enterprise** — dominant in utilities. Proprietary; strong interoperability with utility data models (Electric Utility Network, Geometric Network).
- **QGIS** — open-source; strong for ad-hoc analysis, PyQGIS scripting, cross-checking ESRI results.
- **PostGIS** — open-source spatial database. Core for repeatable analytical pipelines. `ST_Buffer`, `ST_Intersection`, `ST_Distance`, `ST_Union`, `ST_Within` cover most operational spatial queries.
- **GeoServer** — OGC-compliant web map/feature service; useful for sharing analytical results across teams.
- **Mapbox / MapLibre** — web mapping; vector tiles for large datasets.

## Power-Systems Analysis Tools

### Bulk / Transmission
- **PSS/E (Siemens)** — industry-standard load-flow, short-circuit, dynamics.
- **PowerWorld Simulator** — load-flow + visualization; strong educational use.
- **GE PSLF** — load-flow, dynamics; common at ISOs.
- **EMTP / PSCAD** — electromagnetic transient simulation (protection settings, insulation coordination).

### Distribution
- **Eaton CYME** — distribution load-flow, short-circuit, reliability, DER integration.
- **DNV Synergi Electric** — distribution analysis and planning.
- **OpenDSS (EPRI)** — open-source distribution system simulator.

### Open-source Python
- **pandapower** — power-systems network modeling and analysis.
- **GridLAB-D** — distribution and DER co-simulation.
- **networkx** — graph analysis for topology-only questions.
- **geopandas + shapely + rasterio** — spatial analysis stack.

## Data Formats

### Spatial / GIS
- **Shapefile** — legacy but universal; 2 GB limit, no native Unicode, multiple sidecar files.
- **GeoJSON** — text-based, good for web / small-to-medium datasets, weak for very large.
- **GeoPackage (.gpkg)** — SQLite-based; modern, single-file, supports both vector and raster.
- **Esri File Geodatabase (.gdb)** — proprietary; authoritative format in ESRI-centric utilities.
- **GeoParquet** — emerging columnar format; good for analytical pipelines.

### Raster
- **GeoTIFF** — universal.
- **NetCDF** — scientific / climate / weather data with CF Conventions.
- **Cloud-Optimized GeoTIFF (COG)** — modern format for cloud-hosted imagery.

### Grid Data Models
- **CIM (IEC 61968/61970)** — Common Information Model for the electric utility industry. RDF/XML or JSON serialization. Core standard for EMS/DMS/GIS integration.
- **PSS/E .raw** — load-flow case files.
- **PSLF .epc / .sav** — load-flow and dynamics case files.
- **IEEE Common Format for Data Exchange** — interoperability between power-systems tools.

### Outage / Time-Series
- **OSIsoft PI / AVEVA PI** — dominant historian in utilities.
- **PQDIF** — Power Quality Data Interchange Format.
- **COMTRADE** — Common Format for Transient Data Exchange (protective relay records).

## Satellite / Imagery Sources

- **USGS Landsat** — 30 m multispectral, free, long historical record.
- **Sentinel-2 (ESA)** — 10 m multispectral, free, 5-day revisit.
- **Planet Labs** — commercial, sub-meter daily revisit.
- **Maxar / Airbus** — commercial high-resolution.
- **GOES / Himawari** — weather / fire-hot-spot detection.
- **NIFC / MODIS Active Fire** — wildfire perimeters and hot-spots.

## Weather and Environmental

- **National Weather Service (NWS) APIs** — forecast zones, watches/warnings, observations.
- **MRMS (Multi-Radar Multi-Sensor)** — high-resolution precipitation/radar.
- **NOAA HRRR** — hourly model data at ~3 km resolution.
- **USGS NHD / WBD** — hydrography / watershed boundaries.
- **LANDFIRE** — fuel models for fire behavior modeling.

## Safety-Critical Working Practices

- **Change control.** Any work that modifies a production GIS or EMS model is subject to the utility's change-control process. Analytical workspaces like this one are for *reasoning*, not for producing production-model changes.
- **Data provenance.** Every analysis output should carry the as-of date of each input layer and the tool version used.
- **Redaction before sharing.** See `context/constraints.md` for the redaction checklist.
- **Reproducibility.** Prefer pipelines (PostGIS SQL, Python notebooks) over point-and-click workflows for anything that will be referenced in a report or regulatory filing.
