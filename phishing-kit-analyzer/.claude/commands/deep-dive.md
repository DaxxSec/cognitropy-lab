# /deep-dive — Full Static Analysis

Perform a comprehensive static analysis of a phishing kit, dissecting every component to understand the full credential harvesting pipeline.

## Expected Input
- Path to extracted phishing kit directory (run /triage first if not yet done)
- Optional: prior triage report for context

## Workflow

Follow the full Phase 2 methodology in `context/for-agent/workflows.md`:

### 1. Directory & File Mapping
- Generate complete file tree with types, sizes, and modification timestamps
- Identify all entry points (index files, login pages, landing pages)
- Flag suspicious files: web shells, encoded blobs, unexpected binaries
- Build a timeline from file timestamps

### 2. Frontend Analysis (HTML/CSS/JS)
For each HTML page:
- Identify which brand/service is being cloned
- Map all form fields — what data is being harvested?
- Trace form submission flow (action URL, method, JS handlers)

For each JavaScript file:
- Deobfuscate if needed (document methodology)
- Map anti-bot/anti-researcher checks
- Identify browser fingerprinting
- Trace redirect logic (where does victim go after submitting?)
- Note any external resource loads

### 3. Backend Analysis (PHP/Server-side)
For each PHP file:
- Map the credential processing pipeline step by step
- Identify data enrichment (what does the kit add to stolen creds? IP? UA? Geo?)
- Trace ALL exfiltration paths — primary AND hidden
- Check for admin panels or kit management interfaces
- Identify anti-researcher protections (IP blocklists, UA filters, htaccess rules)
- Look for kit author backdoors (secondary exfil to a different recipient)

### 4. Exfiltration Deep-Dive
- Document primary exfil method with full technical detail
- Document any secondary/hidden exfil
- Extract the exact data format sent to the attacker
- List ALL exfil destinations (emails, Telegram chats, URLs, file paths)

### 5. Evasion Technique Catalog
For each technique found, document:
- Technique name and category
- Code location and implementation
- Effectiveness assessment
- Detection opportunity it creates

### 6. Vulnerability Assessment
- Can the kit's admin panel be accessed? (weak/default creds)
- Does the exfil mechanism leak data? (insecure Telegram, open directories)
- Are there code injection points in the kit itself?

## Output Format
Save full analysis to `outputs/analysis-[YYYY-MM-DD]-[kit-name].md` with all sections above.
Create a summary in `outputs/analysis-[YYYY-MM-DD]-[kit-name]-summary.md` for quick reference.
Log in `work-log/`.
