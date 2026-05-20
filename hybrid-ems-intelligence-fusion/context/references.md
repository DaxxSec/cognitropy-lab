# Hybrid EMS — Multi-Source Intelligence Fusion: Reference Tables

Lookup data the agent reaches for during tasks. Compact by design — defer to upstream sources for fuller specs.

## Drive Cycles (Canonical Benchmark Set)

| Cycle | Region | Duration | Mean / Max Speed | Notes |
|---|---|---|---|---|
| **WLTP class 3b** | EU + many others | 1800 s | 46.5 / 131 km/h | Replaces NEDC; required for EU type approval. |
| **WLTP class 3a** | EU | 1800 s | similar | Lower-power variant; rare in modern vehicles. |
| **CLTC-P** | China | 1800 s | 28.96 / 114 km/h | Mandatory for China type approval since 2021. |
| **EPA FTP-75** | USA | 1874 s | 34.1 / 91.2 km/h | Urban dynamometer driving schedule. |
| **EPA HWFET** | USA | 765 s | 77.7 / 96.4 km/h | Highway cycle. |
| **EPA US06** | USA | 596 s | 77.9 / 129.2 km/h | Aggressive driving supplement. |
| **JC08** | Japan (legacy) | 1204 s | 24.4 / 81.6 km/h | Replaced by WLTP for newer vehicles. |
| **NEDC** | EU (legacy) | 1180 s | 33.6 / 120 km/h | Deprecated 2017; included for historical comparison only. |
| **RDE** | EU on-road | 5400–10800 s | route-dependent | Real Driving Emissions; PEMS-instrumented route, not a cycle. |
| **ARTEMIS Urban / Road / Motorway** | EU research | varies | varies | Closer to real-world; useful for fusion-stack stress. |

## Per-Source Default TTLs and Variance Priors

| Source | TTL | σ_default (kW) | Notes |
|---|---|---|---|
| Static map (road class, posted speed) | n/a | 0.5 | Trust very high once vetted. |
| HD-map elevation | n/a | 1.0 (slope-derived) | < SRTM. |
| OSM SRTM elevation | n/a | 3.0 (slope-derived) | Canopy bias; degraded in forests. |
| Live traffic | 5 min | 5.0 | Coverage-dependent. |
| V2X SPaT | 2 s | 0.5 | Adversarial input. |
| V2X BSM | 200 ms | 2.0 | Adversarial input. |
| Weather (wind) | 30 min | 1.5 (via aero) | Strongest impact at highway speeds. |
| Weather (T_ambient) | 30 min | 0.3 (via aux + battery) | Bigger impact at extremes. |
| Driver-style fingerprint | n/a | 2.0–4.0 | Wider band for new drivers. |
| Telematics history | 6 months | 3.0 | Degrades with seasonality. |
| Fleet learning | 1 month | 1.5 | Often the most calibrated. |

## V2X Message Set (SAE J2735)

| Message | Acronym | Update Rate | Typical Use in Fusion |
|---|---|---|---|
| Basic Safety Message | BSM | 10 Hz | Other-vehicle speed / heading for traffic prediction. |
| Signal Phase and Timing | SPaT | 10 Hz | Intersection countdown → predicted stop / launch. |
| MAP | MAP | 1 Hz | Intersection geometry, lane layout. |
| Roadside Alert | RSA | event | Incident / lane closure. |
| Probe Vehicle Data | PVD | event | Aggregated probe data. |
| Traveler Information | TIM | 1 Hz | Variable speed limit, construction. |

## EMS Strategy Cheat-Sheet

| Strategy | Online? | Optimal? | Compute Cost | Production Maturity |
|---|---|---|---|---|
| Rule-based | yes | no | very low | very high |
| ECMS | yes | near-optimal* | low | high |
| A-ECMS | yes | near-optimal | low–medium | high |
| Deterministic MPC | yes | optimal w/ perfect prior | medium | medium–high |
| Robust MPC | yes | conservative-optimal | medium | medium |
| Stochastic MPC | yes | distributional-optimal | high | medium |
| Tube MPC | yes | near-optimal w/ guarantees | medium–high | low–medium |
| Offline DP | no | global optimum | very high | benchmark only |
| RL policy | yes (inference) | varies | very low (inference) | research-grade |

*ECMS optimality depends entirely on `s_eq` quality.

## Battery Model Reference (Equivalent Circuit, Rint / Thevenin)

For each cell:

- `V_terminal = OCV(SOC) − I · R_int(SOC, T, SOH)`
- Thevenin extension adds RC pair(s) for transient response.
- `P_chg_max(SOC, T, SOH)`, `P_dis_max(SOC, T, SOH)` from cell datasheet + DCIR map.
- Wear proxy: Ah-throughput (cumulative) and cumulative `|I|^β` (β ∈ [1.5, 2.5]).

## Upstream Catalogues and Toolchains

- **Argonne Autonomie** — https://www.anl.gov/taps/autonomie — vehicle simulation reference platform.
- **AVL CRUISE / CRUISE M** — https://www.avl.com/cruise-m — commercial powertrain modelling toolchain.
- **GT-SUITE Hybrid** — https://www.gtisoft.com/gt-suite/ — production EMS development environment.
- **MATLAB Powertrain Blockset / Sensor Fusion and Tracking Toolbox** — https://www.mathworks.com/products/powertrain-blockset.html
- **filterpy** — https://github.com/rlabbe/filterpy — Bayesian filters in Python.
- **pgmpy** — https://github.com/pgmpy/pgmpy — probabilistic graphical models in Python.
- **pyro / pymc** — probabilistic programming, useful for fusion uncertainty propagation.
- **cantools** — https://github.com/cantools/cantools — DBC-driven CAN log decode.
- **OpenStreetMap + SRTM** — https://www.openstreetmap.org / https://srtm.csi.cgiar.org — open road + elevation.
- **HERE Routing / Traffic API** — https://www.here.com/platform/routing — commercial routing + traffic.
- **TomTom Traffic Flow API** — https://developer.tomtom.com/traffic-api — commercial traffic.
- **NREL FASTSim** — https://github.com/NREL/fastsim — open-source powertrain efficiency simulator.

## Regulations and Standards (Bookmark)

| Standard | Domain | Use |
|---|---|---|
| ISO 26262 | Functional safety (automotive) | Hazard analysis, ASIL classification of fusion + EMS chain. |
| ISO/SAE 21434 | Cybersecurity (vehicles) | Threat analysis of V2X + cloud feeds. |
| UN R155 | Cybersecurity and CSMS | Regulatory compliance for connected vehicles in UNECE markets. |
| UN R156 | Software Updates and SUMS | OTA EMS updates. |
| ISO 23150 | Sensor-fusion data model | Common reference for source data structures. |
| SAE J2735 | V2X message set | Direct reference for SPaT, BSM, MAP, etc. |
| SAE J1979 / ISO 15031 | OBD-II protocols | Fault observability path. |
| WLTP / GTR 15 | Drive cycle + test method | Type approval. |
| RDE (EU 2017/1151 + amendments) | Real driving emissions | On-road validation. |
| GDPR Art. 4 + Art. 22 | Personal data + automated decisions | Driver profile / fingerprint handling. |
