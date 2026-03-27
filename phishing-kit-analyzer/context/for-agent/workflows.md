# Phishing Kit Analysis Workflows

## Core Analysis Methodology

### Phase 1: Initial Triage (5-10 minutes)

1. **Archive inspection** — Note filename, size, hash (MD5/SHA256), file type, compression method
2. **Listing** — Extract file listing without full extraction; note directory structure
3. **Kit family identification** — Check against known signatures in `resources/common-kit-signatures.md`
4. **Threat level assessment** — Based on:
   - Targeted brand(s)
   - Sophistication of lure pages
   - Presence of anti-analysis/evasion code
   - Exfiltration method complexity
   - Whether it's a known kit family or novel
5. **Quick IOC sweep** — Grep for emails, URLs, IPs, Telegram bot tokens, API keys
6. **Triage verdict** — Classify as: Known/Tracked, Novel/Interesting, or Low-Priority/Generic

### Phase 2: Deep Static Analysis (30-60 minutes)

#### 2a. Directory & File Mapping
- Map complete file tree with types and sizes
- Identify entry points (index.html/php, login pages)
- Flag suspicious files (shells, backdoors, encoded blobs)
- Note timestamps for timeline analysis

#### 2b. Frontend Analysis (HTML/CSS/JS)
- Identify targeted brand and cloned login flow
- Map form fields — what credentials are harvested?
- Analyze JavaScript for:
  - Form validation and submission handlers
  - Anti-bot checks (user agent, referrer, IP geolocation)
  - Browser fingerprinting
  - Bot/crawler detection
  - Redirect logic (post-harvest victim destination)
  - Obfuscation techniques used

#### 2c. Backend Analysis (PHP/Server-side)
- Map credential processing pipeline:
  1. Form data reception
  2. Validation/filtering
  3. Formatting/enrichment (IP, user agent, geolocation)
  4. Exfiltration (email, Telegram, file write, remote API)
  5. Victim redirect
- Identify admin panels or kit management interfaces
- Check for backdoors (secondary exfil to kit author)
- Analyze anti-researcher protections:
  - IP blocklists (security companies, bots, crawlers)
  - User agent filtering
  - Referrer checks
  - htaccess rules

#### 2d. Exfiltration Analysis
- Primary exfil method and destination
- Secondary/hidden exfil (kit author backdoors)
- Data format sent to attacker
- What victim data is collected beyond credentials

#### 2e. Evasion Technique Catalog
For each evasion technique found:
- Technique name
- Implementation method
- Effectiveness assessment
- Detection opportunity

### Phase 3: IOC Extraction & Formatting

1. **Email addresses** — Exfil recipients, kit author contacts, admin panel users
2. **URLs** — Exfil endpoints, redirect destinations, resource loads, C2
3. **IP addresses** — Hardcoded IPs, blocklist entries (inverted = actor infrastructure)
4. **Domain names** — Kit hosting, exfil destinations, legitimate domains being spoofed
5. **Telegram** — Bot tokens, chat IDs, channel names
6. **API keys** — Third-party service keys (geolocation APIs, email APIs)
7. **File hashes** — Kit archive hash, individual file hashes for tracking
8. **Credentials** — Hardcoded admin panel passwords (indicator of actor reuse)

Format outputs per analyst preference: STIX 2.1, MISP event JSON, CSV, or plain text.

### Phase 4: Attribution Assessment

Attribution confidence levels:
- **High (70-100%)** — Code-level match with known actor, unique infrastructure overlap, embedded PII
- **Medium (40-69%)** — Shared code patterns, similar TTPs, infrastructure in same ASN/hosting
- **Low (10-39%)** — Generic kit family match, common tooling, circumstantial overlap
- **None (<10%)** — Insufficient data for meaningful attribution

Attribution signals:
1. **Code fingerprints** — Unique variable names, comments (especially in other languages), coding style
2. **Kit metadata** — Author tags, version strings, embedded handles/aliases
3. **Infrastructure patterns** — Hosting preferences, domain registration patterns, SSL cert reuse
4. **Exfil destinations** — Email patterns, Telegram accounts, drop server locations
5. **Anti-analysis lists** — Custom blocklists may reveal actor's awareness of specific researchers
6. **Timestamps** — File creation/modification times, timezone indicators in code

### Phase 5: Reporting

Report structure:
1. Executive Summary (2-3 sentences)
2. Kit Metadata (hash, size, type, date found)
3. Targeted Brand(s) & Credential Types
4. Technical Analysis Summary
5. Exfiltration Method Detail
6. Evasion Techniques
7. IOC Table
8. Attribution Assessment
9. Recommendations (blocking, detection, response)
10. Appendices (deobfuscated code, full file listing, raw IOCs)

## Decision Trees

### "Is this kit worth a deep-dive?"
```
Is it targeting your organization? → YES → Always deep-dive
                                   → NO ↓
Is it a novel/unknown kit family? → YES → Deep-dive for intel value
                                  → NO ↓
Does it use novel evasion techniques? → YES → Deep-dive for detection eng
                                      → NO ↓
Is it linked to a tracked actor? → YES → Deep-dive for attribution
                                 → NO → Triage-only, extract IOCs, archive
```

### "How to handle embedded credentials (victim data)"
```
Found harvested credentials in kit?
→ YES → Are they from your organization's users?
        → YES → Trigger credential reset procedure, escalate per IR playbook
        → NO → Log count and types only; do NOT extract or store actual creds
               → Notify relevant parties if feasible (sector ISAC, abuse contacts)
```
