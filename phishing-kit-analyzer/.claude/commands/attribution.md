# /attribution — Kit Attribution Workflow

Attempt to attribute a phishing kit to a known actor, group, or kit family based on code analysis, infrastructure patterns, and behavioral signatures.

## Expected Input
- Path to phishing kit (ideally after /deep-dive has been run)
- Optional: suspected actor or kit family
- Optional: related kits for cross-reference

## Workflow

### 1. Code Fingerprinting
- Extract unique variable names, function names, and coding patterns
- Identify comments (especially non-English — note language)
- Look for author tags, version strings, credits, or "powered by" markers
- Analyze coding style: indentation, naming conventions, error handling patterns
- Check for copy-paste artifacts from other kits or tutorials

### 2. Kit Metadata Analysis
- Check for embedded author handles or aliases
- Look for kit version identifiers
- Analyze file metadata (creation tools, timestamps, timezone hints)
- Check image EXIF data for location or device info
- Look for leftover development artifacts (.git, .vscode, debug files)

### 3. Infrastructure Pattern Analysis
- Exfil email patterns (naming conventions, providers used)
- Telegram account patterns (bot naming, channel naming)
- Hosting preferences (shared hosting, bulletproof, compromised servers)
- Domain registration patterns (if related domains known)
- SSL certificate patterns

### 4. TTP Analysis
- Evasion technique repertoire — which anti-analysis methods?
- Targeted brands and verticals
- Credential harvesting depth (just password? Or also CC, SSN, etc.)
- Victim handling (redirect destination, error page behavior)
- Kit distribution method (if known)

### 5. Cross-Reference
- Compare against `resources/common-kit-signatures.md`
- Compare against previously analyzed kits in `outputs/`
- Check for shared IOCs with known campaigns
- Look for code reuse or fork patterns

### 6. Attribution Assessment
Assign confidence level per `context/for-agent/workflows.md`:
- **High (70-100%)** — Direct code match, unique infrastructure, embedded PII
- **Medium (40-69%)** — Shared patterns, similar TTPs, same hosting/ASN
- **Low (10-39%)** — Generic family match, circumstantial overlap
- **Insufficient (<10%)** — Not enough signal

Document:
- Primary attribution hypothesis
- Supporting evidence (ranked by strength)
- Alternative hypotheses
- Gaps in analysis
- Recommended next steps to increase confidence

## Output Format
Save to `outputs/attribution-[YYYY-MM-DD]-[kit-name].md`.
Update `planning/` if this connects to an ongoing investigation.
Log in `work-log/`.
