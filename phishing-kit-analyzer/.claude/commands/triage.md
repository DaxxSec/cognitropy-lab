# /triage — Quick Kit Assessment

Perform a rapid triage of a phishing kit archive to determine threat level, kit family, and whether a deep-dive is warranted.

## Expected Input
- Path to a phishing kit archive (ZIP, TAR, RAR) or extracted directory
- Optional: context on where/how the kit was obtained

## Workflow

### 1. Archive Metadata
- Record filename, file size, hash (MD5 + SHA256)
- Note compression type and any password protection
- Check for nested archives

### 2. File Listing
- Extract or list the full directory tree
- Count files by type (PHP, HTML, JS, CSS, images, text, other)
- Flag unusual files (executables, encoded blobs, shell scripts)
- Note total file count and largest files

### 3. Kit Family Identification
- Compare directory structure and key filenames against `resources/common-kit-signatures.md`
- Check for known kit author signatures (README files, comments, version strings)
- Identify targeted brand(s) from HTML content, images, and form actions

### 4. Quick IOC Sweep
- Grep for email addresses (exfil recipients)
- Grep for URLs and domains
- Grep for IP addresses
- Grep for Telegram bot tokens (`bot[0-9]+:`)
- Grep for API keys and tokens
- Grep for base64-encoded strings (potential hidden config)

### 5. Exfiltration Method ID
- Identify primary exfil: PHP mail(), Telegram API, file_put_contents, cURL to remote endpoint
- Check for secondary/hidden exfil (kit author backdoors)

### 6. Threat Level Assessment
Rate as **Critical / High / Medium / Low** based on:
- Brand targeted (financial = higher)
- Sophistication of evasion techniques
- Novelty (known kit = lower, novel = higher)
- Active exfil destinations (still live = higher)
- Presence of backdoors or secondary exfil

### 7. Triage Verdict
Classify as:
- **DEEP-DIVE RECOMMENDED** — Novel, sophisticated, or targeting your org
- **IOC EXTRACT ONLY** — Known kit, just pull indicators and archive
- **LOW PRIORITY** — Generic, outdated, or broken kit

## Output Format
Save triage summary to `outputs/triage-[YYYY-MM-DD]-[kit-name].md` with:
- Kit metadata table
- Threat level badge
- Kit family (if identified)
- Targeted brand(s)
- Exfil method summary
- Quick IOC list
- Recommended next action
- Log entry in `work-log/`
