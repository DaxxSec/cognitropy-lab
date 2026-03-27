# /onboard — Initialize Wildland Invasive Scout Workspace

## Purpose
Set up your workspace with the field area details, baseline data, and operator profile needed to provide accurate, location-specific guidance.

## Steps

1. **Read existing context files:**
   - `context/project.md`
   - `context/role.md`
   - `context/constraints.md`
   - `context/for-agent/workflows.md`

2. **Ask the operator the following (as a friendly intake interview — one topic at a time):**

   a. **Field Area:** Where are you operating? (state, region, any named landmarks or management unit)
   b. **Biome:** What does the dominant landscape look like? (forest type, grassland, wetland, mixed?)
   c. **Your Role:** Are you a recreational bushcrafter, land manager, guide, homesteader, or something else?
   d. **Primary Goal:** What are you trying to accomplish with this workspace? (monitoring, foraging safety, land management, citizen science, all of the above?)
   e. **Known Threats:** Are there any invasive species you're already aware of in your area?
   f. **Equipment:** Do you have iNaturalist, Gaia GPS, or other field apps? Camera with GPS?
   g. **Experience Level:** How confident are you at field species identification? (none / some / solid / expert)

3. **Based on their answers:**
   - Update `context/project.md` with their field area details
   - Update `context/role.md` with their background
   - Pull the relevant state invasive species watch list from knowledge base (or note that it needs to be manually loaded from their state's invasive species council)
   - Generate a personalized "Top 5 Priority Watch Species" list for their biome and region
   - Create an initial monitoring zone entry in `context/project.md`

4. **Output a Welcome Summary:**
   ```
   ✅ WORKSPACE INITIALIZED

   Field Area: [name]
   Biome: [type]
   Operator Role: [role]
   Primary Goals: [list]

   Priority Watch Species for Your Area:
   1. [species] — [why it's a priority]
   2. [species] — [why it's a priority]
   ...

   Recommended First Actions:
   → Run /field-survey to establish baseline
   → Run /seasonal-baseline to document current conditions

   Available Commands:
   /field-survey    — Run structured invasive survey
   /species-id      — Identify a species from description
   /anomaly-report  — Document something that doesn't belong
   /threat-matrix   — Priority matrix for detected invasives
   /forage-safety   — Cross-check foraging targets
   /camp-eval       — Evaluate a camp site
   /seasonal-baseline — Record/update seasonal baseline
   ```

5. **Save onboarding notes** to `work-log/onboarding-[date].md`
