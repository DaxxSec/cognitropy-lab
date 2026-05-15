# Renewable Energy Siting Analysis — Core Concepts

Background the agent should read before any analysis. Two-vocabulary framework — capacity-planning metrics anchor every verdict, puppetry movement-mechanics terms structure the *walk*.

## 1. Articulation Graph Vocabulary

Every portfolio is decomposed into an articulated body. The hybrid vocabulary makes a class of error visible that "blocks on a one-line diagram" hides.

- **Joint (`J-id`)** — one generating or storing asset. Atom of the graph. A wind farm is *one* joint regardless of how many turbines it contains. Two adjacent wind farms with different POIs are *two* joints. Joints carry: technology, nameplate (MW), location (lat/lon and bus), coupling (AC / DC / DC-coupled / standalone), and a starting capacity credit.
- **Linkage (`L-id`)** — one transmission or distribution segment, from bus to bus. Carries: voltage class, normal rating, emergency rating, current loading, queue cluster status.
- **Drive (`D-id`)** — one control lever: curtailment authority, storage dispatch authority, DR authority, frequency response obligation. Drives are `binding` (FERC-filed OATT curtailment, tolling agreement) or `non-binding` (cooperative DR).
- **Resource shed (`shed_id`)** — group of joints whose centerlines (resource series) are likely to be correlated. Defined by a MERRA-2 / WIND Toolkit cell, or by proximity radius (30 km wind, 50 km solar). Sympathetic motion lives at the shed level.
- **Centerline** — the joint's raw resource-intensity timeseries. For wind, hub-height wind speed (m/s); for PV, plane-of-array GHI/DNI; for hydro, inflow (m³/s); for geothermal, gradient (°C/km). Centerlines are the *input* to the power-curve mapping.
- **Heartline frame vs asset frame** — borrowed from puppetry. Asset frame reports the joint as seen from its own coordinate system (annual CF). Heartline frame reports the joint as seen from the load's coordinate system (capacity credit during net-load peak). The two diverge — a 0.42 wind annual CF can earn a 0.13 capacity-coincident credit.
- **Slack** — headroom on a linkage or in a drive. Linkage slack = `1 − loading_pct`. Storage slack = SOC distance from the closer of 5% or 95%. When slack closes, motion stops.
- **Lead and follow** — the pairing of a variable-renewable joint (lead) with a firm or storage joint (follower) so the system can absorb forecast error and ramp.
- **Weight transfer** — the diurnal and seasonal hand-off of active capacity between joints, written as a ramp-coordination schedule.
- **Sympathetic motion** — unwanted correlated ramping across joints in a shared resource shed. The silent ELCC killer.

## 2. Capacity Planning Metrics

The puppetry frame is the *walk*; the verdict cites these.

- **Capacity factor (CF)** — `annual energy / (nameplate × 8760)`. Most-quoted, least useful for capacity decisions. Typical year-15 lifetime averages (CONUS): onshore wind 0.30-0.50, fixed-tilt PV 0.18-0.24, single-axis-tracking PV 0.22-0.30, CSP-with-storage 0.40-0.55, run-of-river hydro 0.30-0.50, reservoir hydro 0.20-0.40, geothermal binary 0.85-0.92, geothermal flash 0.90-0.95.
- **Capacity credit / capacity value** — the firm capacity equivalent the asset earns. Always less than nameplate for variable renewables. Computed as ELCC in modern ISO methodologies.
- **Effective Load Carrying Capability (ELCC)** — the additional load the system can serve with a given resource added, at constant LOLE. ISO-specific and **portfolio-saturating**: the marginal ELCC of the 1000th MW of solar in a system is far below the 1st MW.
- **Loss of Load Expectation (LOLE)** — expected number of days/year (or hours/year, depending on convention) when load exceeds available capacity. NERC consensus target: 1-in-10-years (0.1 day/year). ISO-NE and PJM use a slightly different formulation (LOLH).
- **Expected Unserved Energy (EUE)** — total MWh of unserved load per year under the planning case. A complementary metric to LOLE; EUE captures the *depth* of shortfall, LOLE captures the *frequency*.
- **Loss of Load Probability (LOLP)** — probability of a load-loss event in a given period. The integrand under LOLE.
- **Ancillary services** — regulation, spinning reserve, non-spinning reserve, frequency response, voltage support, black start. Each market product carries its own product definition and dispatch obligation; ELCC for energy/capacity does not transfer.
- **Forecast error** — day-ahead, hour-ahead, and 5-minute-ahead deviations between predicted and realised output. P95 hourly forecast error sizes operating reserves and storage followers; ISOs publish reference values per resource type.
- **Ramp budget** — the BA's BAL-001-2 ACE-budget envelope, BAL-003-2 frequency response obligation, plus the ISO's ramp products (CAISO Flexible RA, MISO Ramp Capability Product, NYISO Operating Reserve). A weight-transfer plan must close inside these budgets.

## 3. Resource Data — Provenance Tiers

Tier 1 (highest fidelity, smallest sample): **in-house met-mast / SODAR / LiDAR campaigns** — site-specific, 1-3 years, used for finance closure. Carry irreducible inter-annual variability.

Tier 2 (medium fidelity, large sample): **reanalysis blended with met-mast** — NREL's WIND Toolkit (7 yr / 5-min / 2 km) and NSRDB (1998-present / 30-min / 4 km), Vortex / 3TIER / DNV bias-corrected products. Year-long met-mast campaigns are commonly used to bias-correct against the long-term reanalysis to produce a 20+ year synthetic series.

Tier 3 (lowest site-fidelity, longest record): **raw global reanalyses** — MERRA-2 (1980-present, ~50 km, hourly), ERA5 (1940-present, ~31 km, hourly), CERRA (Europe, ~5.5 km). Useful for inter-annual variability characterisation, not for primary CF estimation.

The walk *must* state which tier was used for the headline CF. Mixing tiers without disclosure is a hidden bias.

## 4. Losses and Derates

A nameplate is not deliverable. The walk applies the following before reporting CF:

- **Wind**: array (wake) losses 5-15% (function of layout + boundary layer), availability 95-98%, electrical (cable to POI) 1-3%, turbine performance 95-99%, blade icing / dust 1-3%, environmental curtailment (bat / avian / shadow flicker) 0-5%.
- **Solar PV**: module mismatch 1-2%, soiling 1-5% (climate-dependent), DC wiring 1-2%, inverter 1-3%, AC wiring + transformer 1-2%, availability 99%, snow loss 0-5%, year-1 degradation 1-3% (light-induced + initial cells), annual degradation 0.4-0.6% (c-Si) / 0.7-1.0% (thin-film).
- **Hydro**: penstock and turbine efficiency 85-92%, environmental release 5-15% (FERC license-bound), generator + transformer 96-98%.
- **Geothermal**: parasitic loads 10-20% (binary higher than flash), wellfield performance decline 1-3%/year (commonly compensated by makeup wells).

## 5. Common Failure Modes

- **Mistaking CF for capacity credit.** Most-quoted vs most-needed-on-the-stage. The deliverable to a capacity market is capacity credit, not CF.
- **Single-year resource sample.** A 1-year met-mast at a wind site has ±15-20% inter-annual band on annual energy; financing on a 1-year sample is a bet, not an analysis.
- **Stranded joint.** Asset has a clearable POI on the one-line diagram but no path through cluster study with affordable network upgrades. Articulation graph closes; deliverability does not.
- **Sympathetic motion in a thick queue.** Three developers sited in one shed each assume nameplate-class ELCC; cumulative shed ELCC collapses on all three.
- **Storage slack closure.** Battery follower sized to nominal forecast error, not to forecast-error-plus-lead-drop coincidence. Cushion empties before the next renewable peak; the lead joint curtails.
- **Curtailment cap blown.** PPA caps deliverable-curtailment hours per year; the rehearsal predicts curtailment above the cap, and the IPP eats the gap.
- **Drought-year blindness.** Hydro joint's median-year CF is the headline; the 1-in-20-dry-year CF is the operational floor that the system actually depends on.
- **DR-binding-illusion.** Demand response counted as firm capacity without a binding aggregator contract. The drive is non-binding; the obligation is.
- **Heartline-frame omission.** Centerline-only walk reports asset-frame CF; the system buys load-frame capacity credit. The two diverge most for solar (capacity-coincident hours include evening peaks where PV is already off).

## 6. Operating Constraints

- **NERC TPL-001-5** — transmission planning, contingency analysis (n-0, n-1, n-1-1, n-2). Mandatory for planning studies. A linkage failing TPL is not buildable as-is.
- **NERC BAL-001-2** — Real-Power Balancing Control Performance. CPS-1 (12-month frequency-deviation-weighted ACE), BAAL (per-interconnection limits). Weight transfer plans must close inside BAAL.
- **NERC BAL-003-2** — Frequency Response and Frequency Bias. Variable renewables generally provide *limited* primary frequency response; new IBR plant standards (PRC-024-3, PRC-029-1) extend obligations.
- **FERC Order 2023 / interconnection reform** — cluster studies, network upgrade allocation, withdrawal penalties. Changes how queue position drives siting feasibility.
- **NEPA Section 102** — federal environmental review for projects with federal nexus (BLM lands, USACE jurisdictional waters, federal funding). EIS / EA / categorical exclusion path.
- **ESA Section 7** — consultation with USFWS / NMFS on listed species. Eagle Take, MMPA, BGEPA permits as needed. Long lead times (12-36 months).
- **State siting authority** — varies. Some states (NY Article VIII, IL HB 4412, MI PA 233) preempt local zoning; others (TX, FL) leave local control. Preemption is legally available, operationally costly.
- **FAA Part 77** — height obstruction. Wind turbines >200' AGL trigger Form 7460-1 + determination of hazard / no-hazard. Aviation lighting (FAA Advisory Circular AC 70/7460-1) is mandatory; ADLS (aircraft-detection lighting systems) is permitted in many states.
- **Capacity-market deliverability tests** — separate from energy interconnection. PJM Capacity Emergency Transfer Limit (CETL), ISO-NE Network Resource Interconnection Service. A resource energy-interconnected without deliverability cannot bid as capacity.
