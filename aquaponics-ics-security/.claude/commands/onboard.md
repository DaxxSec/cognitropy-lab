# /onboard — Site Initialization

Initialize this workspace for a specific aquaponics site security engagement.

## Steps
1. Ask the user to describe their aquaponics system:
   - System type (NFT, DWC, media bed, hybrid)?
   - Scale: total water volume, stocking density, production area?
   - Species (tilapia, trout, catfish, other)?
   - Automation level: fully automated, semi-automated, manual with monitoring?
   - Any known internet-connected components?

2. Ask for technical infrastructure overview:
   - Do they have network diagrams?
   - Any known PLCs, HMIs, or SCADA systems?
   - Cloud platforms in use?
   - Remote access arrangements (VPN, TeamViewer, etc.)?

3. Establish engagement scope:
   - Assessment type: new system design review, existing system audit, incident response, or compliance check?
   - Any specific concerns or recent incidents that prompted this assessment?
   - Available maintenance windows for active testing?

4. Create a site profile document:
   - Save to `planning/site-profile.md`
   - Include biological system overview, technical inventory stub, engagement scope, key contacts, maintenance window schedule

5. Generate an initial risk hypothesis based on the information provided:
   - Identify the top 3 likely risk areas based on their profile
   - Recommend which workflow to run next

Reference: `context/for-agent/workflows.md` — Workflow 1
