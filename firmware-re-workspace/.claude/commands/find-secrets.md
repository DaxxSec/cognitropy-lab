# /find-secrets — Hardcoded Credentials & Secret Hunting

Systematically search extracted firmware for hardcoded credentials, API keys, certificates, private keys, tokens, and other sensitive material.

## Prerequisites
- Filesystem extracted (run `/extract-fs` first)
- Path to extracted root filesystem

## Inputs
Ask: What is the path to the extracted firmware root? (e.g., `outputs/squashfs-root/`)

---

## Scan Pipeline

### Phase 1: Password & Credential Files

```bash
ROOT=[extracted_root]

# Shadow and passwd files
find "$ROOT" -name "shadow" -o -name "shadow-" -o -name "passwd" -o -name "passwd-" 2>/dev/null | while read f; do echo "=== $f ==="; cat "$f"; done

# Web server passwords
find "$ROOT" -name ".htpasswd" -o -name "htpasswd" 2>/dev/null | xargs cat 2>/dev/null

# Database credentials
find "$ROOT" -name "*.conf" -o -name "*.cfg" -o -name "*.ini" -o -name "*.xml" 2>/dev/null | xargs grep -il "password\|passwd\|credential" 2>/dev/null

# Config files with inline credentials
grep -r "password\s*[:=]" "$ROOT"/etc/ 2>/dev/null | grep -v "^Binary"
grep -r "passwd\s*[:=]" "$ROOT"/etc/ 2>/dev/null | grep -v "^Binary"
```

### Phase 2: Cryptographic Key Material

```bash
# PEM-format keys and certificates
find "$ROOT" -name "*.pem" -o -name "*.key" -o -name "*.crt" -o -name "*.cer" -o -name "*.p12" -o -name "*.pfx" -o -name "*.pub" 2>/dev/null

# DER-format certificates (binary)
find "$ROOT" -name "*.der" 2>/dev/null

# SSH keys
find "$ROOT" -name "id_rsa" -o -name "id_dsa" -o -name "id_ecdsa" -o -name "id_ed25519" 2>/dev/null
find "$ROOT" -name "authorized_keys" -o -name "known_hosts" 2>/dev/null
find "$ROOT" -name "dropbear_*_key" -o -name "dropbear_rsa_host_key" 2>/dev/null

# For each PEM found, check if it's a private key
# openssl x509 -in [cert.pem] -text -noout
# openssl rsa -in [key.pem] -check -noout
```

### Phase 3: Hardcoded Passwords in Binaries

```bash
# Strings dump from web server binary
strings "$ROOT"/usr/bin/httpd 2>/dev/null | grep -iE "password|passwd|secret|admin|root|default" | head -30

# All SUID binaries
find "$ROOT" -perm /6000 -type f 2>/dev/null | xargs -I{} strings {} | grep -iE "password|passwd|key|secret" | head -20

# Common default credential patterns
strings "$ROOT"/usr/bin/* 2>/dev/null | grep -E "^[a-zA-Z0-9!@#$%^&*]{4,16}$" | sort | uniq -c | sort -rn | head -30
```

### Phase 4: API Keys & Tokens

```bash
# Common API key patterns
grep -rE "[A-Za-z0-9]{20,}" "$ROOT"/etc/ 2>/dev/null | grep -v "^Binary"

# AWS-style keys
grep -rE "(AKIA|ASIA)[A-Z0-9]{16}" "$ROOT"/ 2>/dev/null | grep -v "^Binary"

# Generic hex keys (symmetric encryption keys)
grep -rE "[0-9a-fA-F]{32,64}" "$ROOT"/etc/ 2>/dev/null | grep -v "^Binary" | head -20

# JWT tokens
grep -rE "eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+" "$ROOT"/ 2>/dev/null | grep -v "^Binary"
```

### Phase 5: Wireless & Network Credentials

```bash
# WiFi PSK / WPA keys
grep -r "wpa_passphrase\|psk\s*=\|password\s*=" "$ROOT"/etc/wpa_supplicant* 2>/dev/null
grep -r "PreSharedKey\|PSK\|passphrase" "$ROOT"/etc/ 2>/dev/null | grep -v "^Binary"

# VPN credentials
find "$ROOT" -name "*.ovpn" -o -name "*.conf" 2>/dev/null | xargs grep -l "auth\|password" 2>/dev/null

# SNMP community strings
grep -r "community\|COMMUNITY" "$ROOT"/etc/ 2>/dev/null | grep -v "^Binary"
```

### Phase 6: Web Interface Secrets

```bash
# Web scripts (CGI, PHP, Lua, etc.)
find "$ROOT"/www/ "$ROOT"/htdocs/ "$ROOT"/webroot/ 2>/dev/null -name "*.cgi" -o -name "*.php" -o -name "*.lua" | xargs grep -iE "password|secret|key|token|admin" 2>/dev/null | grep -v "^Binary" | head -30

# JavaScript files
find "$ROOT" -name "*.js" 2>/dev/null | xargs grep -iE "apikey|api_key|secret|password|token" 2>/dev/null | grep -v "^Binary" | head -20
```

---

## Reporting Secrets Found

For each secret found, document using this format:

```markdown
### SECRET-001
**Type:** [Hardcoded password / Private key / API token / WiFi PSK / etc.]
**Location:** `[file path within extracted filesystem]`
**Content:** `[value or redacted preview — use [REDACTED] for actual creds in reports]`
**Severity:** [Critical / High / Medium / Low]
**Impact:** [what an attacker could do with this]
**Evidence:**
```
[brief terminal output showing the finding]
```
**Remediation:** [remove hardcoded credential; use key management; rotate key]
```

---

## Save Output

Save full secrets inventory to `outputs/[target]-secrets-[date].md`
Flag all Critical and High findings immediately for inclusion in `/write-report`
Log to `work-log/[date].md`
Update `context/project.md` key findings section
