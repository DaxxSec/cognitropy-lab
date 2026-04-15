# Environment

## Data Formats

### Instrumentation Data
The agent should be prepared to receive instrumentation data in these common formats:
- **CSV files**: Most common export from SCADA/data loggers. Expect columns for timestamp, instrument ID, reading value, and sometimes quality flag.
- **JSON**: Structured data from modern monitoring APIs
- **Tabular paste**: Users may paste tabular data directly from spreadsheets

### Typical Data Fields
- `timestamp` or `date`: Reading date/time (various formats)
- `instrument_id` or `sensor`: Instrument identifier
- `reading` or `value`: Measured value
- `unit`: Engineering unit (ft, psi, in, gpm, etc.)
- `reservoir_elevation`: Concurrent reservoir level (critical for correlation)
- `temperature`: Ambient or water temperature
- `quality_flag`: Data quality indicator if available

### Units
- Piezometric head: feet (ft) or meters (m) of water, or psi
- Displacement: inches (in) or millimeters (mm)
- Seepage flow: gallons per minute (gpm) or liters per second (L/s)
- Settlement: inches (in) or millimeters (mm)
- Reservoir elevation: feet (ft) above mean sea level

## Operating Context
- Users may range from highly technical dam safety engineers to municipal dam owners with limited engineering background
- Regulatory context varies — always ask or determine whether the dam is under FERC jurisdiction, state-regulated, or federally owned (USACE, Bureau of Reclamation, TVA)
- Data quality varies widely — some systems have continuous SCADA data, others rely on manual monthly readings

## Output Expectations
- Reports should be professional, structured, and suitable for regulatory submission
- Anomaly flagging should include clear severity levels and recommended actions
- Visualizations (when possible) should show historical trends with anomaly markers
- All outputs should include appropriate disclaimers about the advisory (non-certifying) nature of the analysis
