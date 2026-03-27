# Firmware RE Workflows
<!-- Reference for the agent — detailed methodology for each analysis stage -->

## Stage 1: Initial Triage

### 1.1 File Identification
Run these in order to characterize the binary:
```bash
file firmware.bin
xxd firmware.bin | head -20            # Check magic bytes manually
strings firmware.bin | head -50        # Quick string survey
binwalk firmware.bin                   # Entropy + signature scan
binwalk -E firmware.bin                # Entropy graph (high entropy = compressed/encrypted)
```

**Decision tree:**
- High uniform entropy throughout → likely encrypted; need key recovery before proceeding
- Mixed entropy with recognizable signatures → packed/compressed; proceed to extraction
- Low entropy with clear strings → possibly uncompressed; check architecture
- Bootloader magic (U-Boot, etc.) → multi-stage firmware; map partitions first

### 1.2 Architecture Identification
```bash
binwalk -A firmware.bin                # CPU opcode scan
strings firmware.bin | grep -i "mips\|arm\|x86\|xtensa\|mipsel\|powerpc"
strings firmware.bin | grep -i "linux\|busybox\|uboot\|vxworks\|rtos"
```

**Common embedded architectures:**
| Arch | Endian | Common Devices |
|---|---|---|
| MIPS32 LE | Little | Atheros, MediaTek routers |
| MIPS32 BE | Big | Older Broadcom, Cavium |
| ARM (v5-v7) | Little | Most modern IoT, smartphones |
| ARM Cortex-M | Little | Automotive ECU, microcontrollers |
| PowerPC | Big | Older Cisco, DOCSIS cable modems |
| x86/x64 | Little | Gateways, NAS, x86 IoT |
| Xtensa | Little | ESP8266, ESP32 |
| Renesas RX/RL78 | Little | Automotive, industrial |
| Infineon TriCore | Little | Automotive ECU (Bosch, Continental) |

---

## Stage 2: Filesystem Extraction

### 2.1 Binwalk Extraction
```bash
binwalk -e firmware.bin                # Auto-extract
binwalk -Me firmware.bin               # Recursive extraction (matryoshka)
ls -la _firmware.bin.extracted/        # Review what was found
```

### 2.2 Manual SquashFS Extraction
```bash
# Standard squashfs
unsquashfs squashfs.img

# Non-standard/vendor squashfs (Broadcom, TP-Link, etc.)
sasquatch squashfs.img

# Check squashfs header manually
xxd squashfs.img | head -5
# Look for: sqsh, hsqs, qshs, shsq (different endianness/vendor variants)
```

### 2.3 JFFS2 Extraction
```bash
# Create MTD block device simulation
modprobe mtdram total_size=65536 erase_size=256
modprobe mtdblock
dd if=jffs2.img of=/dev/mtd0
mount -t jffs2 /dev/mtdblock0 /mnt/jffs2

# Or use jefferson
jefferson -d output_dir/ jffs2.img
```

### 2.4 UBIFS Extraction
```bash
ubireader_extract_images firmware.bin
ubireader_extract_files ubifs.img
```

### 2.5 Dealing with Encrypted Firmware
Strategies when firmware appears encrypted:
1. Find older unencrypted version; compare structure to understand layout
2. Search vendor SDK leaks or GPL source releases
3. Look for key material in bootloader (often earlier in the file)
4. JTAG/UART extraction of running device to get plaintext
5. Differential analysis: flash two versions and compare hardware reads

---

## Stage 3: Filesystem Analysis

### 3.1 Automated Scanning (firmwalker)
```bash
firmwalker /path/to/extracted/root
# Reports: passwords, keys, config files, web server files, binary setuid files
```

### 3.2 Manual Priority Targets
```bash
# Credentials & secrets
find . -name "*.conf" -o -name "*.cfg" -o -name "*.ini" | xargs grep -i "password\|passwd\|secret\|key\|token\|credential"
find . -name "shadow" -o -name "passwd" -o -name ".htpasswd"
find . -name "*.pem" -o -name "*.key" -o -name "*.crt" -o -name "*.p12"

# Web interface
find . -path "*/www*" -o -path "*/htdocs*" -o -path "*/webroot*"

# Binaries of interest
find . -name "httpd" -o -name "telnetd" -o -name "dropbear" -o -name "lighttpd"
find . -perm /6000 -type f                              # SUID/SGID binaries
find . -name "*.sh" | xargs grep -l "eval\|exec\|system"

# Init system
find . -name "rc.d" -o -name "init.d" -o -name "S??*" | head -20
cat ./etc/inittab 2>/dev/null
cat ./etc/rc.local 2>/dev/null
```

---

## Stage 4: Binary Analysis (Disassembly)

### 4.1 Ghidra Workflow
1. Create new project → Import binary → let auto-analysis run
2. Check Memory Map: identify .text, .data, .bss, mapped MMIO regions
3. Symbol table: look for debug symbols (lucky!) or function name strings
4. Cross-references: find all callers of dangerous functions first
5. Bookmarks: mark interesting locations as you discover them

**Priority functions to find:**
- `system()`, `popen()`, `exec*()` — command injection risk
- `strcpy()`, `sprintf()`, `gets()` — buffer overflow risk
- `scanf()`, `sscanf()` with `%s` — stack overflow risk
- `eval()` in script engines — injection risk
- Custom crypto implementations — usually broken

### 4.2 radare2 Quick Workflow
```bash
r2 -A firmware.elf           # Auto-analyze
afl                          # List functions
pdf @ main                   # Disassemble main
iz                           # Strings
ii                           # Imports
iE                           # Exports
/c system                    # Find calls to system()
```

### 4.3 Bare-Metal Firmware (No OS)
When analyzing microcontroller/ECU firmware without OS:
1. Identify interrupt vector table (typically at 0x00000000 or 0x08000000 for ARM Cortex-M)
2. Map peripheral base addresses from datasheet
3. Find main() by following reset vector
4. Identify UART/debug output functions (common first target)
5. Map communication protocol handlers (CAN, LIN, UDS for automotive)

---

## Stage 5: Vulnerability Discovery

### 5.1 Command Injection Hunting
```bash
# In web scripts / CGI
grep -r "system\|popen\|exec\|passthru\|shell_exec" www/ --include="*.cgi" --include="*.sh"
grep -r "\$(" www/ --include="*.sh"            # Bash command substitution
grep -r "os\.system\|subprocess" . --include="*.py"

# In C binaries — look in Ghidra for calls to system() with user-controlled strings
```

### 5.2 Hardcoded Credentials
```bash
# Default passwords
grep -r "admin\|password\|12345\|default\|guest\|root" etc/ --include="*.conf"
strings binaries/httpd | grep -E "admin|password|secret"

# SSH keys
find . -name "authorized_keys" -o -name "id_rsa" -o -name "id_dsa"

# TLS certificates and private keys
openssl x509 -in found_cert.pem -text -noout    # Inspect certificates
openssl rsa -in found_key.pem -check             # Verify private key
```

### 5.3 Memory Corruption
```bash
# Static: checksec on binaries
checksec --file=./usr/bin/httpd

# Look for:
# - No canary → stack overflows exploitable
# - No ASLR/PIE → ROP chains easier
# - RWX segments → shellcode injection possible
# - Partial RELRO → GOT overwrite possible
```

### 5.4 Crypto Weaknesses
- Hardcoded IV or key in AES/DES implementations
- Use of MD5 or SHA1 for password hashing (no salt)
- ECB mode encryption (patterns visible)
- Custom/homebrew crypto routines
- Certificate pinning bypass opportunities

---

## Stage 6: Emulation (Optional)

### 6.1 User-Space Emulation
```bash
# Copy QEMU static binary into firmware root
cp $(which qemu-mipsel-static) ./squashfs-root/
sudo chroot squashfs-root/ /qemu-mipsel-static /bin/sh

# Or run specific binary
qemu-mipsel-static -L ./squashfs-root ./squashfs-root/usr/bin/httpd
```

### 6.2 Full-System Emulation (FirmAE)
```bash
# FirmAE automates full-system emulation for many router firmwares
sudo ./run.sh -r [brand] firmware.bin
# Provides network access to emulated device
```

---

## Stage 7: Reporting

### Report Structure
1. **Executive Summary** — what was found, severity overview
2. **Target Information** — device, firmware version, analysis date
3. **Methodology** — tools used, analysis stages completed
4. **Findings** — each vulnerability with:
   - Title and unique ID (e.g., FW-001)
   - CVSS score (if applicable)
   - CWE mapping
   - Technical description
   - Evidence/PoC
   - Impact
   - Remediation recommendation
5. **Appendices** — extracted artifacts, tool outputs, hashes

### Work Log Format
Each session entry in `work-log/YYYY-MM-DD.md`:
```
## Session: YYYY-MM-DD HH:MM
### Objective
### Commands Run
### Findings
### Next Steps
```
