# Forecaster Environment

Typical tooling stack the agent should assume is available unless `/onboard` says otherwise:

- **InfoEx** (Avalanche Canada / CAA) or equivalent professional observation exchange
- **Snowpilot** for detailed snow profile logging
- **Mountain weather forecast products**: NOAA NWS mountain zones, NBM, HRRR, NAM
- **SNOTEL** (NRCS) automated snow water equivalent + precipitation stations
- **RAWS** (Remote Automated Weather Station network)
- **MADIS** (Meteorological Assimilation Data Ingest System) aggregator
- **Telemetry** from agency-owned weather stations (may be JSON / CSV / vendor dashboard)
- **GIS stack**: QGIS / ArcGIS with slope, aspect, ATES layers
- **Bulletin publication stack**: agency CMS, social media schedulers, phone hotline script

The agent should ask what format telemetry and observations are delivered in, and then keep that assumption in `context/for-agent/tools.md`.
