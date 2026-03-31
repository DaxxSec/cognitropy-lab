# Tools & Software

## Core Python Stack
| Package | Purpose | Install |
|---------|---------|---------|
| `numpy` | Array math, linear algebra | `pip install numpy` |
| `scipy` | Optimization, special functions, stats distributions | `pip install scipy` |
| `pymc` | Bayesian inference, MCMC sampling (NUTS) | `pip install pymc` |
| `arviz` | Posterior diagnostics, trace plots, summary stats | `pip install arviz` |
| `matplotlib` | Plotting, visualization | `pip install matplotlib` |
| `pandas` | Data wrangling, time series | `pip install pandas` |
| `geopandas` | Spatial data, shapefiles, watershed boundaries | `pip install geopandas` |
| `xarray` | Gridded data (rainfall, terrain) | `pip install xarray` |

## Hydraulic Modeling Software
| Tool | Domain | Integration |
|------|--------|-------------|
| **HEC-RAS** | 1D/2D open channel, floodplain | Python via `rascontrol` or CLI batch mode |
| **EPANET** | Water distribution networks | Python via `wntr` (Water Network Tool for Resilience) |
| **SWMM** | Stormwater, combined sewers | Python via `pyswmm` |
| **HEC-HMS** | Rainfall-runoff modeling | CLI batch mode |

## Data Sources
| Source | What | Access |
|--------|------|--------|
| USGS NWIS | Streamflow, stage, water quality | `dataretrieval` Python package |
| NOAA Atlas 14 | Precipitation frequency estimates | Web download, hdsc.nws.noaa.gov |
| NHDPlus | Stream network, catchment boundaries | `pynhd` Python package |
| 3DEP | LiDAR elevation data | `py3dep` Python package |
| FEMA NFHL | Flood hazard layers | FEMA Map Service Center API |

## Recommended MCP Servers
- **filesystem** — Read/write local data files, HEC-RAS project files
- **fetch** — Pull USGS data, NOAA precipitation grids
- **postgres/sqlite** — Store and query asset inventories, monitoring data
- **brave-search** — Look up design standards, case studies, regional parameters

## Environment Setup
```bash
# Create conda environment
conda create -n hydraulics python=3.11
conda activate hydraulics

# Install core stack
pip install numpy scipy pandas matplotlib pymc arviz

# Install hydraulic tools
pip install wntr pyswmm dataretrieval geopandas

# Optional: HEC-RAS automation (Windows only, requires HEC-RAS installed)
pip install rascontrol
```
