# /vuln-hunt — Vulnerability Discovery Workflow

Systematically hunt for exploitable vulnerabilities in firmware binaries and scripts. Covers command injection, buffer overflows, memory corruption, authentication bypass, and insecure configurations.

## Prerequisites
- Filesystem extracted
- Target binary or component identified

## Inputs
Ask:
1. What component do you want to focus on? (web server / specific binary / scripts / all)
2. What vulnerability class are you most interested in? (or "all" for full sweep)

---

## Vuln Class 1: Command Injection

### In CGI/Web Scripts
```bash
ROOT=[extracted_root]

# Bash/sh CGI files
find "$ROOT" -name "*.cgi" -o -name "*.sh" | xargs grep -l "system\|popen\|eval\|exec" 2>/dev/null

# PHP files
find "$ROOT" -name "*.php" | xargs grep -l "system\|exec\|shell_exec\|passthru\|popen\|eval" 2>/dev/null

# Lua files (common in OpenWrt)
find "$ROOT" -name "*.lua" | xargs grep -l "os.execute\|io.popen" 2>/dev/null

# Look for unquoted variable use in dangerous functions
grep -rn "system.*\$\|exec.*\$\|popen.*\$" "$ROOT"/www/ "$ROOT"/htdocs/ 2>/dev/null | grep -v "^Binary"
```

### In Compiled Binaries (Ghidra/radare2)
Hunt for:
- `system(str)` where `str` is user-controlled (HTTP param, NVRAM value, env var)
- `popen()` with user data
- `sprintf/snprintf` building shell commands with user input
- `execl/execv` with user-controlled arguments

Pattern: trace data flow from HTTP parameter → NVRAM read → dangerous function

---

## Vuln Class 2: Buffer Overflows

### Static: checksec
```bash
find "$ROOT" -type f -executable | xargs file 2>/dev/null | grep -i "ELF" | cut -d: -f1 | while read bin; do
  echo "=== $bin ==="
  checksec --file="$bin" 2>/dev/null
done
```

### Binary targets lacking protections
```bash
# Binaries without stack canary
find "$ROOT" -type f | xargs strings 2>/dev/null | grep -c "__stack_chk_fail"
```

### Ghidra: Dangerous function hunt
Search for cross-references to:
- `strcpy(dest, src)` — no bounds check
- `strcat(dest, src)` — no bounds check
- `sprintf(buf, fmt, ...)` — format string + overflow
- `gets(buf)` — always vulnerable
- `scanf("%s", buf)` — no bounds
- `memcpy(dst, src, len)` where `len` is user-controlled

---

## Vuln Class 3: Authentication Bypass

### Hardcoded Backdoor Accounts
```bash
# In shadow/passwd
grep -v "!\|\\*" "$ROOT"/etc/shadow 2>/dev/null   # Accounts with actual passwords set

# In web server
strings "$ROOT"/usr/sbin/httpd 2>/dev/null | grep -iE "admin|root|guest|debug|test" | head -20

# Magic tokens in query strings
grep -rn "debug\|backdoor\|test\|factory\|hidden" "$ROOT"/www/ 2>/dev/null | grep -v "^Binary"
```

### Session Management Issues
```bash
# Predictable session tokens
grep -rn "session\|cookie\|token" "$ROOT"/www/ 2>/dev/null | grep -iE "rand\|time\|md5\|crc" | grep -v "^Binary"

# Missing authentication checks
grep -rn "auth\|login\|password" "$ROOT"/www/ 2>/dev/null | grep -c "check\|verify\|validate"
```

### UART/Console Backdoors
```bash
# Boot args or init that drop to shell without auth
grep -r "ttyS\|console\|serial" "$ROOT"/etc/ 2>/dev/null
grep -r "getty\|agetty\|mgetty" "$ROOT"/etc/inittab 2>/dev/null
```

---

## Vuln Class 4: Insecure Services

### Service Inventory
```bash
# Running services defined in init
cat "$ROOT"/etc/inittab 2>/dev/null
ls "$ROOT"/etc/init.d/ 2>/dev/null
find "$ROOT"/etc/ -name "S??*" | sort 2>/dev/null

# Telnet (unencrypted remote access)
grep -r "telnet\|telnetd" "$ROOT"/etc/ 2>/dev/null

# FTP
grep -r "ftpd\|vsftpd\|proftpd" "$ROOT"/etc/ 2>/dev/null

# SNMP
grep -r "snmpd\|community" "$ROOT"/etc/ 2>/dev/null
```

---

## Vuln Class 5: Insecure Update Mechanisms

```bash
# Firmware update scripts
find "$ROOT" -name "*update*" -o -name "*upgrade*" -o -name "*flash*" 2>/dev/null | xargs file | grep -i "script\|text"

# Look for:
# - No signature verification before flashing
# - HTTP (not HTTPS) update URLs
# - Predictable update server URLs
grep -r "http://\|ftp://" "$ROOT"/etc/ "$ROOT"/usr/lib/ 2>/dev/null | grep -iE "update\|upgrade\|firmware\|download"
grep -rn "wget\|curl" "$ROOT"/etc/ "$ROOT"/usr/sbin/ 2>/dev/null | grep -v "^Binary" | head -20
```

---

## Vuln Class 6: Format String Vulnerabilities

```bash
# In compiled code (Ghidra): find calls to printf/fprintf/syslog
# where format string argument is user-controlled (not a literal string)
# Pattern: printf(user_string) vs printf("%s", user_string)

# Quick static check on web scripts
grep -rn "printf.*\$\|fprintf.*\$" "$ROOT"/www/ "$ROOT"/usr/lib/ 2>/dev/null | grep -v "^Binary"
```

---

## Findings Template

For each vulnerability found:

```markdown
### VULN-[XXX]: [Short Title]
**CWE:** CWE-[number] — [name]
**CVSS Score:** [score] ([vector])
**Severity:** Critical / High / Medium / Low / Informational

**Affected Component:** `[binary or script path]`
**Affected Function/Line:** `[function name or line number]`

**Description:**
[Technical description of the vulnerability]

**Evidence:**
```
[code snippet, disassembly, or command output]
```

**Attack Scenario:**
[How an attacker would exploit this]

**Impact:**
[What an attacker achieves]

**Remediation:**
[Specific fix recommendation]
```

---

## Save Output

Save findings to `outputs/[target]-vulns-[date].md`
Update `context/project.md` key findings
Log to `work-log/[date].md`
Feed into `/write-report` for final report generation
