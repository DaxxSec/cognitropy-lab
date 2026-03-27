# /compare — Kit Comparison

Compare two or more phishing kits to identify shared infrastructure, code reuse, actor overlap, or kit evolution over time.

## Expected Input
- Paths to two or more phishing kit directories or analysis reports
- Optional: hypothesis to test (e.g., "same actor?" or "fork of kit X?")

## Workflow

### 1. Metadata Comparison
For each kit, extract and compare:
- File counts and types
- Directory structure similarity
- Total size
- Timestamps (creation, modification)
- Archive format and compression

### 2. Structural Diff
- Compare directory trees — what's shared, added, removed?
- Identify template vs. customized files
- Map structural evolution if kits appear to be versions of the same base

### 3. Code Comparison
- Diff key files (index.php, login pages, exfil handlers)
- Identify shared code blocks (copy-paste patterns)
- Compare obfuscation techniques — same method? Same tool?
- Compare variable naming conventions and coding style
- Check for shared comments or author markers

### 4. IOC Overlap
- Cross-reference all extracted IOCs
- Identify shared: email addresses, domains, IPs, Telegram accounts, API keys
- Map infrastructure overlap (shared hosting, ASN, registrar)

### 5. TTP Comparison
- Compare targeted brands
- Compare evasion technique repertoire
- Compare credential harvesting depth
- Compare victim redirect behavior
- Compare exfil methods and data formats

### 6. Evolution Analysis (if kits appear related)
- What changed between versions?
- Were evasion techniques upgraded?
- Did exfil destinations change?
- Were new brands or data types added?
- Does the progression suggest a single developer or a forked ecosystem?

## Output Format
Save to `outputs/comparison-[YYYY-MM-DD]-[kit1]-vs-[kit2].md` with:
- Side-by-side metadata table
- Overlap matrix (IOCs, code, structure, TTPs)
- Venn diagram (text-based) of shared vs. unique elements
- Conclusion with confidence: Same actor / Same family / Unrelated
- Visual diff excerpts for key files

Log in `work-log/`.
