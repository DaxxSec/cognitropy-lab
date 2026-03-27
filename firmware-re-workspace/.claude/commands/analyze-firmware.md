# /analyze-firmware — Structured Firmware Analysis

Perform a systematic, staged analysis of a firmware binary. This command runs through the full analysis pipeline from triage to findings summary.

## Prerequisites
- Workspace onboarded (`/onboard` completed)
- Firmware file accessible on your filesystem
- At minimum: `file`, `strings`, `xxd` available

---

## Inputs to Gather

Ask the user:
1. What is the path to the firmware file?
2. Has this firmware been analyzed before in this workspace? (check `context/project.md` and `work-log/`)
3. Any specific focus for this session? (e.g., "focus on web interface", "look for backdoors", "quick triage only")

---

## Analysis Pipeline

Execute these stages in order. After each stage, summarize findings before moving on. Ask the user if they want to continue, skip, or deep-dive on any finding.

### Stage 1: File Identification
```bash
file [firmware_path]
sha256sum [firmware_path]
ls -lh [firmware_path]
xxd [firmware_path] | head -30
strings [firmware_path] | head -100
```
**Document:** file type, size, magic bytes, any obvious strings

### Stage 2: Entropy Analysis
```bash
binwalk [firmware_path]
binwalk -E [firmware_path]
```
**Interpret results:**
- Provide entropy graph analysis
- Identify compressed/encrypted regions
- Map out partitions/sections if multi-part firmware
- Flag if fully encrypted (pivot to key recovery strategy)

### Stage 3: Architecture & OS Identification
```bash
binwalk -A [firmware_path]
strings [firmware_path] | grep -iE "linux|busybox|uboot|vxworks|freertos|openwrt|ddwrt|mips|arm|xtensa|powerpc"
strings [firmware_path] | grep -iE "version|kernel|build|compiled"
```
**Determine and document:** CPU architecture, endianness, OS/RTOS type, bootloader

### Stage 4: Extraction
Follow the extraction workflow from `context/for-agent/workflows.md` Stage 2.
```bash
binwalk -Me [firmware_path] -C outputs/extracted/
ls -la outputs/extracted/
```
Report what was successfully extracted.

### Stage 5: Filesystem Survey
```bash
find outputs/extracted/ -maxdepth 3 -type d
find outputs/extracted/ -name "etc" -o -name "www" -o -name "usr" | head -20
```
Describe the filesystem layout and identify key directories.

### Stage 6: Quick Wins Scan
Run these rapid-result checks:
```bash
# Version and build info
find outputs/extracted/ -name "version*" -o -name "buildinfo*" -o -name "revision*" 2>/dev/null | xargs cat 2>/dev/null | head -30

# Network config
find outputs/extracted/ -name "*.conf" | xargs grep -l "ip\|network\|dns\|gateway" 2>/dev/null | head -10

# Obvious credentials
grep -r "password\s*=\s*" outputs/extracted/etc/ 2>/dev/null | head -20
find outputs/extracted/ -name "shadow" 2>/dev/null | xargs cat 2>/dev/null

# Key files
find outputs/extracted/ -name "*.pem" -o -name "*.key" -o -name "*.crt" 2>/dev/null
```

### Stage 7: Initial Findings Summary

Produce a structured summary:

```markdown
## Firmware Analysis — Initial Findings
**Target:** [device/firmware name]
**Date:** [date]
**Analyst:** [user name]

### Identification
- Architecture: [arch] [endianness]
- OS/RTOS: [name + version if found]
- Bootloader: [name + version if found]
- Compression: [types found]

### Structure
- [describe partitions/filesystems found]

### Quick Findings
- [list any credentials, keys, version strings, notable configs found]

### Recommended Next Steps
1. [suggested follow-on command]
2. [suggested follow-on command]
```

---

## Post-Analysis Actions

1. Save findings summary to `outputs/[target-name]-initial-[date].md`
2. Log session to `work-log/[date].md`
3. Update `context/project.md` with findings summary and next steps
4. Suggest appropriate follow-on commands:
   - Found web interface? → `/map-attack-surface`
   - Found credentials? → `/find-secrets` for deeper search
   - Ready for vuln hunting? → `/vuln-hunt`
   - Have report to write? → `/write-report`
