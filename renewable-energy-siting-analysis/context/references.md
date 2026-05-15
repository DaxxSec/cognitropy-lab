# Renewable Energy Siting Analysis — Reference Tables

Compact lookup data the agent reaches for during a walk. Cite the upstream source on the face of every output.

## Table R-1 — Default ELCC class ratings by technology (year-15 portfolio)

Rough cross-ISO defaults for the *starting* capacity credit assigned at A-6. ISO-specific class ratings supersede these.

| Technology              | Default ELCC | High-penetration ELCC | Source / Notes |
|-------------------------|--------------|------------------------|----------------|
| Onshore wind            | 12-18%       | 6-12%                  | PJM 2026-27 BRA, MISO PRA, NYISO ICAP |
| Offshore wind           | 30-45%       | 20-30%                 | NYISO offshore class, ISO-NE FCM |
| Fixed-tilt PV           | 30-45%       | 8-20%                  | PJM, CAISO RA — drops fast with penetration |
| Tracking PV             | 35-55%       | 12-25%                 | PJM, CAISO RA |
| 4-hour Li battery       | 90-95%       | 60-80%                 | All ISOs at low penetration; saturates |
| 8-hour Li battery       | 95-100%      | 80-95%                 | Recently introduced classes |
| CSP w/ 6h storage       | 80-95%       | 70-85%                 | CAISO, PNM IRP |
| Run-of-river hydro      | 40-60%       | 30-50%                 | MISO, BPA — drought-sensitive |
| Reservoir hydro         | 85-95%       | 80-90%                 | BPA, NYISO |
| Geothermal binary       | 92-97%       | 90-95%                 | CAISO firm class |
| Demand response (firm)  | 70-90%       | 60-85%                 | PJM DR products, varies by call |

## Table R-2 — Capacity factor envelopes by technology / class (lifetime average)

| Technology                          | Excellent | Average | Marginal | REJECT below |
|-------------------------------------|-----------|---------|----------|---------------|
| Onshore wind, IEC Class I           | 0.45+     | 0.38    | 0.28     | 0.22 |
| Onshore wind, IEC Class II          | 0.42+     | 0.34    | 0.25     | 0.20 |
| Onshore wind, IEC Class III         | 0.38+     | 0.30    | 0.22     | 0.17 |
| Offshore wind, fixed-bottom         | 0.50+     | 0.42    | 0.34     | 0.28 |
| Offshore wind, floating             | 0.55+     | 0.45    | 0.38     | 0.30 |
| Solar PV, fixed-tilt CONUS          | 0.22+     | 0.19    | 0.16     | 0.12 |
| Solar PV, single-axis tracking      | 0.28+     | 0.24    | 0.20     | 0.16 |
| CSP w/ storage                      | 0.50+     | 0.45    | 0.38     | 0.30 |
| Run-of-river hydro                  | 0.50+     | 0.40    | 0.30     | 0.20 |
| Geothermal binary                   | 0.90+     | 0.88    | 0.82     | 0.75 |

## Table R-3 — Reanalysis source bias (rough corrections)

| Source         | Resolution     | Bias (wind)                              | Bias (irradiance)            |
|----------------|----------------|------------------------------------------|------------------------------|
| MERRA-2        | ~50 km hourly  | +3-7% flat / -5-10% complex terrain      | n/a                          |
| ERA5           | ~31 km hourly  | +1-4% flat / -3-8% complex terrain       | -1-3% global                 |
| WIND Toolkit   | 2 km 5-min     | ±2-5% site-specific                       | n/a                          |
| NSRDB          | 4 km 30-min    | n/a                                      | -1-2% arid / +2-5% maritime  |
| Met-mast / SODAR | site-specific | reference (subject to seasonal sampling) | reference                    |

Always pair reanalysis with a measurement-based correction when available; pure-reanalysis production forecasting is fine for screening, not for finance.

## Table R-4 — Shed-saturation curves (ELCC class derating)

ISO-published illustrative curves showing how marginal ELCC declines as installed shed nameplate rises. Use the actual ISO curve for the relevant footprint; this table is a rough guide.

| Shed nameplate / load peak | Solar marginal ELCC | Wind marginal ELCC |
|----------------------------|---------------------|--------------------|
| < 5%                       | 45-55%              | 18-22%             |
| 5-15%                      | 35-45%              | 14-18%             |
| 15-30%                     | 20-35%              | 10-14%             |
| 30-50%                     | 10-20%              | 6-10%              |
| > 50%                      | 5-10%               | 4-6%               |

## Table R-5 — Forecast error references (day-ahead, hourly P95)

| Technology       | Forecast error P95 hourly | Source |
|------------------|---------------------------|--------|
| Onshore wind     | 12-18% nameplate          | NREL Wind Forecasting Improvement Project; ERCOT, MISO operations data |
| Solar PV         | 6-10% nameplate (clear)   | NSRDB analysis; CAISO operations data |
| Solar PV         | 18-30% nameplate (cloudy) | same |
| Hydro inflow     | 4-12% nameplate           | BPA, TVA operations |
| Aggregated portfolio | 5-12% nameplate       | ISO-published reserve product sizing |

## Table R-6 — Reliability targets by region

| Region    | LOLE target          | Source                                  |
|-----------|----------------------|------------------------------------------|
| All NERC  | 1 day in 10 years (0.1/yr) | NERC consensus / IEEE Std 859        |
| PJM       | 0.1 LOLE             | PJM Manual 20                            |
| MISO      | 0.1 LOLE             | MISO PRA Manual                          |
| ISO-NE    | 0.1 LOLE             | ISO-NE FCM                               |
| NYISO     | 0.1 LOLE             | NYSRC IRM                                |
| CAISO     | Planning Reserve Margin 15-17% | CPUC RA                          |
| ERCOT     | Operating Reserve Demand Curve (no formal LOLE) | ERCOT |

## Table R-7 — Network upgrade dollar ranges (rough, per ISO cluster study)

| Voltage class | Typical network upgrade $/MW interconnecting |
|---------------|-----------------------------------------------|
| 69 kV         | $50-150k                                       |
| 138 kV        | $100-400k                                       |
| 230 kV        | $200-800k                                       |
| 345 kV        | $400-1,500k                                     |
| 500 kV / 765 kV | $800-3,000k                                  |

## Upstream catalogues and standards

- **NERC Reliability Standards** — https://www.nerc.com/pa/Stand/Pages/ReliabilityStandardsUnitedStates.aspx — TPL-001-5, BAL-001-2, BAL-003-2, PRC-024-3, PRC-029-1.
- **FERC Order 2023** — https://www.ferc.gov/news-events/news/order-2023 — interconnection process reform.
- **NREL WIND Toolkit** — https://www.nrel.gov/grid/wind-toolkit.html
- **NREL NSRDB** — https://nsrdb.nrel.gov/
- **NASA MERRA-2** — https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/
- **ECMWF ERA5** — https://www.ecmwf.int/en/forecasts/dataset/ecmwf-reanalysis-v5
- **EIA Form 860 (capacity) / Form 923 (generation)** — https://www.eia.gov/electricity/data/eia860/
- **EIA Form 930 (hourly load)** — https://www.eia.gov/electricity/gridmonitor/
- **NREL ReEDS Standard Scenarios** — https://www.nrel.gov/analysis/standard-scenarios.html
- **NREL ATB cost / performance** — https://atb.nrel.gov/
- **USGS gauges** — https://waterdata.usgs.gov/nwis/sw — hydrology inflow series
- **FAA Form 7460-1** — https://oeaaa.faa.gov/ — obstruction evaluation
- **USFWS Eagle Take program** — https://www.fws.gov/program/eagle-management — incidental take permits
- **PJM RPM / ELCC** — https://www.pjm.com/markets-and-operations/rpm
- **MISO PRA** — https://www.misoenergy.org/planning/resource-adequacy/
- **CAISO RA** — http://www.caiso.com/planning/Pages/ReliabilityRequirements/Default.aspx
- **ISO-NE FCM** — https://www.iso-ne.com/markets-operations/markets/forward-capacity-market

## Choreography → Capacity-planning vocabulary crosswalk

For analysts reading the workspace cold. The puppetry term is the methodology; the capacity-planning term is what the verdict cites.

| Puppetry term         | Capacity-planning term                  |
|-----------------------|------------------------------------------|
| Joint                 | Generation/storage asset (or unit)       |
| Linkage               | Transmission segment                     |
| Drive                 | Control lever (curtailment, DR, dispatch) |
| Centerline            | Resource-intensity timeseries            |
| Heartline frame       | Load-frame (capacity-coincident view)    |
| Asset frame           | Resource-frame (annual energy view)      |
| Slack                 | Line loading headroom / storage SOC cushion |
| Lead and follow       | Variable-RE + firm/storage pairing       |
| Weight transfer       | Diurnal/seasonal capacity ramp           |
| Sympathetic motion    | Inter-asset ramp correlation             |
| Rehearsal day         | Historical / stress-year backtest        |
| Cue                   | Operational stress event                 |
