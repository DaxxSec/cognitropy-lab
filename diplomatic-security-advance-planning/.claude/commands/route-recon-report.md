# /route-recon-report

Build a primary + 2 alternate route analysis — chokepoints, hospital pre-positioning timing, IED-hide assessment, time-of-day variation, host-nation traffic plan.

## Inputs

- **Origin and destination** addresses + alternates.
- **Time-of-day windows** for the planned movement (peak / off-peak / overnight).
- **Threat tier** for the increment.
- **Available recon resources** — driven recon time, host-nation police pre-route walks, satellite imagery, prior trip route notes (if recent and reliable).
- **Hospital capability mapping** — Level I/II/III trauma centres in the route's catchment with capability profile (surgery, neuro, pediatric if applicable).
- **Construction / event calendar** — known disruptions during trip window.

## Steps

1. Read `context/concepts.md` "Route reconnaissance" + `context/workflows.md` "Route recon".
2. Identify candidate routes — primary (fastest under normal conditions), Alt-A (alternate avoiding known chokepoints), Alt-B (radical alternate via different highway/corridor).
3. Per route, document chokepoints — bridges, tunnels, narrow streets, controlled intersections, parade routes, civilian-density peaks.
4. Per chokepoint, identify mitigation — host-nation traffic plan (intersection holds, motorcycle leapfrog), pre-route sweep, IED-hide assessment, alternate available within X seconds.
5. Per route, identify hospital pre-positioning — which trauma centre serves the route's worst-case segment, time-to-arrival at peak traffic vs. off-peak, EMS pre-positioning agreement with host-nation EMS.
6. Per route, document IED-hide assessment — abandoned vehicles, dumpsters, construction equipment, vendor stalls, manhole covers. Score density of potential hides per kilometre.
7. Per route, run a time-of-day variation table — primary becomes Alt-A under afternoon traffic? Alt-B becomes primary overnight?
8. Drive each route in person at multiple times of day during the advance window; document observations + photos.
9. Engage host-nation police for traffic plan agreement on primary route.
10. Write recon report to `outputs/route-recons/<trip-id>/<increment-id>-recon.md`.

## Output

A markdown route recon report at `outputs/route-recons/<trip-id>/<increment-id>-recon.md` containing: per-route analysis (chokepoints, hospital pre-positioning, IED-hide assessment, time-of-day variation), drive-recon observations + timestamps + photos, host-nation traffic-plan agreement summary, recommended primary + alternates with switch-criteria.

## Decision points

- **If no route has acceptable chokepoint profile** → motorcade configuration must compensate (additional CAT, motorcycle leapfrog) OR trip increment is restructured.
- **If hospital pre-positioning time exceeds protocol maximum** (typically 15 min ground-EMS, longer for air-EMS in remote areas) → either request medical asset co-located in motorcade OR reduce time-on-route OR cancel increment.
- **If host-nation will not commit to traffic plan** → fall back to motorcycle leapfrog method; document the degraded posture.

## Notes

- Drive recons should cover at least 3 time-of-day samples (peak, off-peak, overnight) in the trip window. Driving once is insufficient — traffic patterns are not stationary.
- Recent prior-trip route notes are useful but not authoritative — construction, ownership changes, and traffic-pattern shifts are common.
- Alt-B exists for situations where Alt-A is also compromised; don't merge it with primary or Alt-A even if seemingly redundant.
- IED-hide assessment is a probabilistic estimate, not a guarantee; it informs threat-tier configuration, doesn't replace it.
