# Workflows

## Daily Forecast Build (morning issue cycle)

1. **Ingest overnight weather** (T, HN24, HNW24, wind, RH, pressure trend) from station network.
2. **Sanity-check telemetry** - flag any station with > 3 consecutive flat / frozen readings; recommend PM action.
3. **Pull prior 24h observations** from InfoEx / MIN / field ops.
4. **Update PWL tracker** - for each tracked layer, record today's evidence (ECT result, natural avy activity, propagation distance).
5. **Classify problem types** active today by aspect + elevation band.
6. **Assign likelihood + size** per problem type; derive hazard level per band.
7. **Draft bulletin** using bulletin-template.md:
   - Bottom line
   - Avalanche problem description(s)
   - Travel advice
   - Forecast discussion
   - Weather outlook
8. **Confidence call**: high / moderate / low with one-line justification.
9. **Flag protected data** (InfoEx-only) before handing off for publication.
10. **Append work-log entry** with decisions + uncertainty notes.

## Slope-Scale (tactical) Analysis

1. Record slope parameters: aspect, elevation, slope angle, start zone terrain, runout exposure.
2. Overlay active problem types for that aspect/elevation.
3. Evaluate load (recent wind + snowfall, skier loading, warming).
4. Run through Avaluator / ALPTRUTH / equivalent check.
5. Surface FACETS traps specific to this party / objective.
6. Recommend: go / no-go / mitigate. Always explain what evidence would change the call.

## Mitigation & Predictive-Maintenance Plan

1. Read `resources/pm-schedule-template.md` and flag overdue items.
2. Cross-reference weather outlook - any storm cycle that would demand pre-storm asset check?
3. Propose a 7-day PM + mitigation schedule covering:
   - Snow observation plots
   - Remote weather station calibration windows
   - Explosive inventory + charge function tests
   - DaisyBell / Gazex / Avalauncher readiness
   - RACS battery + comms
4. Flag conflicts between PM windows and forecast control missions.

## Incident Review (FACETS)

1. Record incident vitals: date, location, party size, burial depth, outcome.
2. Reconstruct conditions (weather, bulletin in effect, observations that morning).
3. Reconstruct decision path: objective, route, turnbacks, last decision point.
4. Tag each decision with FACETS traps that appear present.
5. Extract 2-3 actionable lessons; assign to training / ops / bulletin language review.
6. Respect agency peer-review confidentiality until release is approved.
