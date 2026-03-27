# /onboard — Initialize Limnology Safety Monitor

Welcome to the Limnology Safety Monitor workspace. Let's set up your project.

## Step 1: Gather Project Context

Ask the user for the following information and record it in `context/project.md`:

1. **Project name** — What is this sampling campaign or monitoring program called?
2. **Water body** — Which lake, river, reservoir, or wetland are you working on? (Name, state/region, approximate size)
3. **Campaign type** — Routine monitoring, incident response, baseline survey, or research study?
4. **Regulatory framework** — Which standards apply? (EPA, specific state DEQ, WHO, local ordinances)
5. **Team size** — How many people will be in the field?
6. **Season/timing** — When is sampling planned? (Affects stratification, ice cover, bloom risk)
7. **Known hazards** — Any pre-identified site hazards? (Contamination history, boat traffic, depth, wildlife)
8. **Key contacts** — Safety officer, PI, local emergency services, agency contacts?

## Step 2: Configure the Workspace

Based on the responses:
- Populate `context/project.md` with all details provided
- Update `context/role.md` if the user describes their expertise level
- Note any specific constraints in `context/constraints.md`
- If the user mentions specific equipment, update `context/for-agent/environment.md`

## Step 3: Provide Orientation

After setup, brief the user on available commands:

- `/site-risk` — Assess field site hazards before deployment
- `/sampling-plan` — Design a sampling campaign with safety protocols
- `/water-quality` — Analyze water quality data and flag anomalies
- `/incident-report` — Document a safety incident or near-miss
- `/gear-check` — Pre-deployment equipment and PPE checklist
- `/compliance-audit` — Audit procedures against standards
- `/weather-hold` — Evaluate weather for go/no-go decisions

Recommend they start with `/site-risk` if they have a specific site, or `/sampling-plan` if they're designing a new campaign.
