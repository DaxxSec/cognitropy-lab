# Biodeterioration Assessment

## Purpose

Use when surveying biological colonisation on masonry — to identify the organisms taxonomically and read their distribution as a bioindicator of the moisture/exposure regime, before recommending any treatment.

## Prompt Template

```
You are assessing biological colonisation on historic masonry. Identify the taxa, then interpret them as moisture bioindicators — cause-first, biocide-last.

I have a colonisation survey:

- **Building / elevations:** [orientation, height bands, materials]
- **Observed colonisation:** [per zone: growth form, colour, coverage %, texture]
- **Lab/ITS (if any):** [confirmed genera]
- **Known defects / moisture sources:** [copings, sills, downpipes, splash, run-off]
- **Decay context:** [recession, capillarity, salts if known]
- **Constraints:** [protected lichens, surface friability, access]

Please:
1. Identify the colonisers to genus where possible (note where lab confirmation is needed).
2. Map their distribution by zone and interpret the moisture regime each indicates.
3. Localise the likely moisture source the biology is tracking.
4. Distinguish cosmetic colonisation from biodeterioration that needs action.
5. Recommend cause-first remediation; treat biocide as a last resort with ecological/heritage caveats.
```

## Expected Output

- Colonisation map: zone → taxa → coverage % → growth form.
- Moisture-regime interpretation per zone.
- Localised likely source(s) of wetting.
- Cosmetic-vs-damaging verdict.
- Cause-first action plan; biocide caveats (protected species, friability, returns if cause unfixed).
