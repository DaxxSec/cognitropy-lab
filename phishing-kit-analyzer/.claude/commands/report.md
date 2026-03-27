# /report — Generate Analysis Report

Generate a structured, stakeholder-ready analysis report from completed analysis work.

## Expected Input
- Kit name or path to completed analysis in `outputs/`
- Target audience: Technical / Executive / Mixed
- Optional: specific sections to include or exclude

## Workflow

### 1. Gather Source Material
- Load triage report (if exists): `outputs/triage-*-[kit-name].md`
- Load deep-dive analysis (if exists): `outputs/analysis-*-[kit-name].md`
- Load IOC extraction (if exists): `outputs/iocs-*-[kit-name].*`
- Load attribution assessment (if exists): `outputs/attribution-*-[kit-name].md`
- Check `work-log/` for session notes

### 2. Assemble Report
Follow the report structure from `context/for-agent/workflows.md` Phase 5:

#### Executive Summary (2-3 sentences)
What was found, what's the risk, what should be done.

#### Kit Metadata Table
| Field | Value |
|-------|-------|
| Kit Name | |
| Archive Hash (SHA256) | |
| File Count | |
| Date Analyzed | |
| Analyst | |
| TLP Marking | |

#### Targeted Brand(s) & Credential Types
What's being phished and what data is harvested.

#### Technical Analysis Summary
Condensed findings from the deep-dive — credential flow, backend logic, key code snippets.

#### Exfiltration Method Detail
How stolen data leaves the kit and where it goes.

#### Evasion Techniques
Table of anti-analysis techniques with detection opportunities.

#### IOC Table
Formatted indicator table with types, values, confidence, and recommended actions.

#### Attribution Assessment
Who's behind it (if determinable), with confidence level and evidence summary.

#### Recommendations
Specific, actionable steps: blocking rules, detection signatures, credential resets, abuse reports.

#### Appendices
- Deobfuscated code excerpts
- Full file listing
- Raw IOC list
- Timeline of analysis

### 3. Format for Audience
- **Technical**: Include code snippets, full IOC details, detection rule suggestions
- **Executive**: Lead with business impact, minimize jargon, focus on risk and action
- **Mixed**: Technical appendices with executive summary up front

## Output Format
Save to `outputs/report-[YYYY-MM-DD]-[kit-name].md`
If executive version requested, also save `outputs/report-[YYYY-MM-DD]-[kit-name]-exec.md`
Log in `work-log/`.
