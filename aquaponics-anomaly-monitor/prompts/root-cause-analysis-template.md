# Root Cause Analysis Prompt Template

Use when a parameter is out of range and you need to find the underlying cause.

---

**Prompt:**

```
Help me diagnose why [PARAMETER] is [VALUE] — it should be around [NORMAL VALUE].

Timeline:
- Last known normal reading: [VALUE] on [DATE]
- When I first noticed the problem: [DATE/TIME]
- Current reading: [VALUE]

Other parameters:
pH: 
NH3: 
NO2-: 
NO3-: 
DO: 
Temp: 

Recent events (check all that apply):
- [ ] Added new fish on [date]
- [ ] Changed feeding amount/schedule on [date]
- [ ] Did a water change on [date] — how much: ___
- [ ] Cleaned filter or media on [date]
- [ ] Used any medication/treatment: [name]
- [ ] Power outage or equipment failure: [details]
- [ ] Temperature change (seasonal, heater issue): ___
- [ ] Other: ___

Fish behavior: [normal/surfacing/lethargic/off-feed/gasping/hiding]
Any fish deaths: [yes/no — if yes, how many, when found]
Plant appearance: [normal/yellowing/wilting/other]

What I've already tried: [if anything]
```

Please provide a ranked differential diagnosis, ask any clarifying questions, and recommend a treatment plan with the most likely cause.
```
