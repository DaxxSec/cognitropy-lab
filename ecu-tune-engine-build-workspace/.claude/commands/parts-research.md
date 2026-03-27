# /parts-research — Parts Compatibility & Upgrade Research

Research parts for your specific application — compatibility, expected gains, reliability trade-offs, and sourcing.

---

## When to Use This Command
- Planning an upgrade and want to understand your options
- Evaluating a specific part before purchasing
- Checking if a part is compatible with your engine, ECU, or existing mods
- Comparing two competing parts for your application

---

## What to Tell Me

1. **What you're trying to achieve:** (e.g., "I want more top-end power," "my fuel pump is limiting boost," "I need better intercooling")
2. **Specific part in mind (if any):** (name, part number, or description)
3. **Budget range:** (or just confirm your budget from constraints.md)
4. **Any constraints:** (must retain emissions equipment, OEM fitment preference, etc.)

---

## Research Process

For each candidate part, I'll evaluate:

### Fitment & Compatibility
- Does it physically fit your chassis / engine bay?
- Does it require supporting modifications to install?
- Any known clearance issues, hose routing changes, or bracket fabrication needed?

### Performance Impact
- Expected improvement over your current setup
- At what power level does this part become the limiting factor?
- Does this part unlock other upgrades, or does it require others first?

### Reliability & Quality
- Known failure modes or quality control issues
- Community reputation (common in builds like yours?)
- Warranty and support from the manufacturer

### Supporting Mods Required
- What else needs to change for this part to work correctly and safely?
- Will this change require a retune?

### Budget Assessment
- Price range across reputable vendors
- Does it fit within constraints.md budget?
- Is there a meaningful quality difference at a higher price point?

---

## Output Format

For each part researched:

```
## [Part Name / Category]

**Recommended Option:** [Brand / Model / Part Number]
**Alternative(s):** [If applicable]
**Price Range:** [$XX – $XX]
**Fitment:** [Plug-and-play / Minor mods / Significant mods required]
**Expected Gain:** [Description of improvement]
**Supporting Mods Required:** [List]
**Retune Required:** [Yes / No / Recommended]
**Known Issues:** [Any common problems]
**Verdict:** [Buy / Skip / Consider if budget allows]
```

---

## Platforms with Deep Reference Data

This workspace has the most detailed data for:
- Subaru EJ/FA/FB engines (STI, WRX, Forester XT)
- Mitsubishi 4G63 / 4B11 (Evo VIII-X)
- Honda K-series / B-series
- GM LS / LT family
- Nissan RB / SR / VR38
- Ford Coyote / EcoBoost
- MegaSquirt-based standalone applications

For other platforms, research will rely on general principles and available spec data.
