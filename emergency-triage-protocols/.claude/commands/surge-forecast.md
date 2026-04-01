# /surge-forecast — ED Surge Capacity & Resource Forecasting

## Purpose
Predict emergency department surge capacity needs, staffing requirements, and supply demand based on historical patterns, current census, and anticipated patient influx. Supports surge activation decisions and resource planning.

## When to Use
- Planning for anticipated surge (flu season, weather event, major event)
- Real-time decision support during active surge (next 12–24 hours)
- Capacity validation and bottleneck identification
- Resource allocation and staffing surge planning
- Mutual aid requests and patient diversion decisions

## Duration
10–30 minutes depending on forecast complexity

## Input Required

I'll ask you to provide or confirm:

### 1. Current ED State
- **Current census:** Number of patients currently in ED
- **Current capacity:** Total ED beds available
- **Percentage occupied:** (Can calculate from above)
- **Current acuity mix:** % ESI-1, ESI-2, ESI-3, ESI-4/5 (approximate)
- **Arrival rate:** Patients arriving per hour currently

### 2. Historical Baseline (from facility data or I can use defaults)
- **Average daily census:** (e.g., 80 patients/day)
- **Busiest hour(s):** (e.g., 10 AM–2 PM peak arrival)
- **Acuity distribution:** Typical % by ESI level
- **Seasonal patterns:** (e.g., winter flu surge, summer trauma)
- **Day-of-week effects:** (Mondays busier than Sundays, etc.)

### 3. Anticipated Event / Surge Trigger
- **Event type:** (e.g., flu outbreak, heat wave, major accident, scheduled event in town)
- **Expected timeline:** (e.g., starts tomorrow, building over 1 week)
- **Expected patient influx:** Additional patients expected (e.g., "200 additional patients over 24 hours")
- **Acuity of incoming patients:** (e.g., higher acuity due to trauma, or lower due to worried-well)

### 4. Facility Constraints
- **Surge bed capacity:** Total beds available including surge areas (recovery room, observation unit, hallways, etc.)
- **Critical care (ICU) beds:** Limited vs. high availability
- **Staffing availability:** How many additional nurses, physicians, technicians can be called in?
- **Known resource limitations:** (e.g., limited transport, supply chain delays, staffing shortages)

### 5. Time Horizon
- **Forecast window:** Next 24 hours? 1 week? 1 month?
- **Forecast frequency:** Updated every hour (real-time) or daily?

## How Forecasting Works

**Step 1: Establish Baseline**
I calculate your normal ED pattern:
- Normal daily volume (80 patients/day = ~3.3 patients/hour average)
- Adjusted for time-of-day (peak hours 10 AM–2 PM, low overnight)
- Adjusted for day-of-week (Mondays higher, Sundays lower)
- Adjusted for seasonal effects (flu season, trauma patterns)

**Step 2: Project Forward**
Based on historical trends + anticipated event:
- If no event: Expect normal pattern for this time of day/week/season
- If event anticipated: Add influx on top of baseline

**Step 3: Calculate Resource Needs**
From projected census:
- Bed occupancy (current + forecast)
- Staffing surge (nurses, physicians, technicians)
- Supply demand (IV fluids, dressings, medications)
- Transport needs (ambulances, beds available)

**Step 4: Identify Thresholds & Escalation Points**
When does your facility surge protocol activate?
- Green: 0–80% capacity (routine operations)
- Yellow: 80–100% (Phase 1 surge, +20% staffing)
- Orange: 100–120% (Phase 2 surge, +40% staffing)
- Red: 120%+ (Phase 3 surge, +60%+ staffing)

**Step 5: Recommend Actions**
- Activate surge protocol at recommended time
- Calculate specific staffing/supply needs
- Identify bottlenecks and mitigations
- Recommend patient diversion or mutual aid triggers

## Example Forecast

```
BASELINE SETUP:
Your facility: 100 beds, average 80 patients/day (3.3/hour)
Current: 70 patients in ED (70% capacity)
Current acuity: 15% ESI-1, 35% ESI-2, 40% ESI-3, 10% ESI-4/5
Arrival rate: 3/hour currently, normal for 2 PM

SCENARIO: Heat wave expected tomorrow, peak 105°F
Historical surge in heat: +40% volume, higher acuity (heat exhaustion, dehydration)

FORECAST (24-hour window):
Time         Forecast     Capacity  Acuity        Surge Status
3 PM–6 PM    85 patients  85%       40% ESI-2     GREEN (routine)
6 PM–9 PM    95 patients  95%       45% ESI-2     YELLOW (activate Phase 1)
9 PM–12 AM   100 patients 100%      50% ESI-2     ORANGE (activate Phase 2)
12 AM–3 AM   105 patients 105%      50% ESI-2     ORANGE (Phase 2 continue)
3 AM–6 AM    95 patients  95%       45% ESI-2     YELLOW (Phase 1 only)
6 AM–9 AM    120 patients 120%      55% ESI-2     RED (activate Phase 3)
9 AM–12 PM   130 patients 130%      60% ESI-2     RED (Phase 3 continue)

STAFFING SURGE RECOMMENDATION:
Baseline: 20 nurses, 4 physicians, 8 technicians

Phase 1 (80–100% capacity): +20% staffing
  Nurses: 20 × 1.2 = 24 (add 4)
  Physicians: 4 × 1.2 = 4.8 → 5 (add 1)
  Technicians: 8 × 1.2 = 9.6 → 10 (add 2)

Phase 2 (100–120% capacity): +40% staffing
  Nurses: 20 × 1.4 = 28 (add 8)
  Physicians: 4 × 1.4 = 5.6 → 6 (add 2)
  Technicians: 8 × 1.4 = 11.2 → 12 (add 4)

Phase 3 (120%+ capacity): +60% staffing
  Nurses: 20 × 1.6 = 32 (add 12)
  Physicians: 4 × 1.6 = 6.4 → 7 (add 3)
  Technicians: 8 × 1.6 = 12.8 → 13 (add 5)

SUPPLY DEMAND PROJECTION:
Phase 1: +20% increase in typical supply consumption
  IV fluids (normal 40 liters/day): +8 liters/day
  Dressings/bandages (normal 100 units/day): +20 units/day
  Medications (antiemetics, antipyretics): +20%

Phase 2–3: +40–60% increase
  Increased acuity = more medications, procedures, lab tests

RECOMMENDATION:
✓ Alert to prepare surge areas by 5 PM
✓ Call-in Phase 1 staffing by 6 PM
✓ Call-in Phase 2 staffing by 10 PM (prepare for Phase 3)
✓ Order additional IV fluids, dressings, ice (heat emergency)
✓ Coordinate with other hospitals for potential diversion
✓ Consider restricting elective admissions starting 10 PM
✓ Prepare for possible mutual aid request if Phase 3 needed
```

## Forecast Accuracy & Confidence

I'll provide confidence level for each forecast:

| Time Horizon | Confidence | Use Case |
|--------------|-----------|----------|
| **Next 1–2 hours** | 85–95% | Real-time decisions, immediate surge activation |
| **Next 6–12 hours** | 70–85% | Staffing surge planning, supply ordering |
| **Next 24 hours** | 60–75% | Contingency planning, mutual aid prep |
| **Beyond 24 hours** | < 60% | Trend monitoring, not actionable forecast |

## Real-Time Surge Tracking

During an actual surge, I can:

1. **Monitor vs. Forecast:**
   - Compare actual arrivals to forecast
   - Adjust forecast based on actual trends
   - Alert if surge exceeds predictions

2. **Escalation Triggers:**
   - Alert when surge reaches Phase 1 threshold
   - Recommend Phase 2 activation when appropriate
   - Trigger Phase 3 protocol if needed

3. **Resource Reallocation:**
   - Recommend staffing adjustments based on actual vs. forecast
   - Suggest supply distribution changes
   - Identify bottlenecks needing intervention

## Advanced Forecasting Features

### Multi-Day Surge Planning
For events lasting multiple days:
- Hour-by-hour forecasting across the entire event
- Resource fatigue planning (staff breaks, rest periods)
- Supply chain replenishment needs
- Mutual aid coordination schedule

### Scenario Comparison
Compare potential outcomes:
- If we activate Phase 2 at different times, what happens?
- If supply runs out, how does that impact surge management?
- If staff call-in takes 1 hour vs. 30 minutes, what's the difference?

### Resource Optimization
Find the best allocation:
- Minimum staffing needed to maintain safety
- Most efficient bed utilization
- Cost optimization (staff hours, supply usage)
- Wait time and throughput metrics

### Sensitivity Analysis
How sensitive is forecast to assumptions?
- What if arrival rate is 20% higher than expected?
- What if acuity is worse (more ESI-2) than typical?
- What if transport capacity is reduced?
- How much does uncertainty affect surge activation timing?

## Output & Recommendations

After forecasting, I provide:

1. **Forecast Summary:**
   - Hour-by-hour census projection
   - Surge activation timing and phases
   - Confidence intervals

2. **Staffing Plan:**
   - Specific numbers by role and phase
   - Call-in timing recommendations
   - Availability checks if possible

3. **Supply Analysis:**
   - Additional supplies needed
   - Ordering recommendations and lead times
   - Critical items at risk of stockout

4. **Actions & Decisions:**
   - When to activate surge protocol
   - When to activate patient diversion
   - When to request mutual aid
   - When to restrict elective admissions

5. **Contingency Plans:**
   - If surge exceeds forecast
   - If resources become unavailable
   - If supply chains disrupted

## Using Forecast for Planning

### Pre-Surge Planning
- Run forecast for anticipated event (flu season, major gathering in town)
- Validate staffing surge procedures can be executed
- Pre-position supplies
- Alert staff to potential surge date/time

### Real-Time Surge Management
- Compare actual to forecast every 1–2 hours
- Adjust activations if actual differs from forecast
- Request resources early if trending above forecast
- Escalate if forecast exceeded

### Post-Surge Review
- Compare actual vs. forecast accuracy
- Identify forecast assumptions that were wrong
- Adjust baseline models for future accuracy
- Update surge activation thresholds if needed

---

**Last Updated:** 2026-04-01
