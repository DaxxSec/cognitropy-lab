# /ioc-extract — IOC Extraction & Formatting

Extract all Indicators of Compromise from a phishing kit and format them for sharing, ingestion, or blocking.

## Expected Input
- Path to phishing kit directory OR a completed analysis report
- Optional: desired output format override
- Optional: TLP marking override

## Workflow

### 1. Extraction Pass
Systematically extract every indicator type:

**Network Indicators:**
- Email addresses (exfil recipients, admin contacts, kit author emails)
- URLs (exfil endpoints, redirect destinations, resource loads, C2)
- Domain names (hosting, exfil, spoofed brands)
- IP addresses (hardcoded IPs, blocklist entries — note: IPs in blocklists are inverted intel)

**Infrastructure Indicators:**
- Telegram bot tokens and chat IDs
- API keys (geolocation services, email APIs, URL shorteners)
- Server paths and directory structures

**File Indicators:**
- Kit archive hash (MD5, SHA1, SHA256)
- Individual file hashes for high-value files
- Filenames that are distinctive/trackable

**Identity Indicators:**
- Kit author aliases/handles
- Hardcoded admin credentials (reuse indicator)
- Language/locale hints
- Unique code signatures (variable names, comments)

### 2. Deduplication & Validation
- Remove duplicate indicators
- Validate format (proper IP ranges, valid email syntax, etc.)
- Separate confirmed-malicious from informational
- Tag each IOC with confidence level per analyst preference

### 3. Contextualization
For each IOC, add:
- Type classification
- Where in the kit it was found
- Role (exfil destination, evasion, infrastructure, attribution)
- First-seen date
- Confidence level
- Recommended action (block, monitor, investigate)

### 4. Format & Output
Generate in the analyst's preferred format(s):

**STIX 2.1 Bundle** → `outputs/iocs-[date]-[kit]-stix.json`
**MISP Event JSON** → `outputs/iocs-[date]-[kit]-misp.json`
**CSV** → `outputs/iocs-[date]-[kit].csv`
**Plain Markdown** → `outputs/iocs-[date]-[kit].md`

Include TLP marking in all outputs.
Log extraction in `work-log/`.
