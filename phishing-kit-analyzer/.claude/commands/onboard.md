# /onboard — Workspace Initialization

Welcome to the Phishing Kit Analyzer workspace. I'll gather some context about you and your environment so I can tailor my analysis to your needs.

## Interview Flow

### Step 1: Your Role
Ask the analyst:
1. What is your title/function? (e.g., DFIR Analyst, Threat Intel Researcher, SOC Analyst)
2. How experienced are you with phishing kit analysis specifically? (Beginner / Intermediate / Advanced)
3. What are your primary responsibilities? How does kit analysis fit into your daily workflow?
4. Do you work alone or with a team? Who consumes your analysis outputs?
5. Rate your comfort with: PHP analysis, JavaScript analysis, regex, CyberChef, OSINT tools, STIX/TAXII

**→ Save responses to `context/role.md`**

### Step 2: Project Scope
Ask the analyst:
1. What's the primary objective? (Incident triage / Threat intel production / Detection engineering / Research / All of the above)
2. What types of kits do you typically encounter? (Office 365 clones, banking, custom, etc.)
3. Are you tracking specific actor groups or campaigns?
4. What time period or scope are you focused on?
5. Where do your outputs go? (SIEM, MISP, threat intel platform, reports, Slack)

**→ Save responses to `context/project.md`**

### Step 3: Constraints & Preferences
Ask the analyst:
1. Preferred output format for IOCs? (STIX 2.1 / MISP JSON / CSV / Plain text / Multiple)
2. Report verbosity preference? (Executive summary / Technical detail / Full teardown)
3. Do you tag IOCs with confidence levels? What scale?
4. What's your attribution confidence threshold before naming an actor?
5. Any organizational policies on handling victim credentials found in kits?
6. Default TLP marking for your outputs? (WHITE / GREEN / AMBER / RED)

**→ Save responses to `context/constraints.md`**

### Step 4: Environment
Ask the analyst:
1. What OS are you working on?
2. Which analysis tools do you have? (CyberChef, PHP interpreter, Node.js, Python, hex editor)
3. What threat intel tools/APIs? (VirusTotal, URLScan, MISP, Shodan, AbuseIPDB)
4. Where do you store kits for analysis? What's your working directory?
5. Do you have network access during analysis or are you air-gapped?
6. Any proxy requirements?

**→ Save responses to `context/for-agent/environment.md`**

### Step 5: Confirmation
Summarize everything back to the analyst. Ask for corrections. Save final versions of all context files.

Log the onboarding completion in `work-log/` with the date and a summary.
