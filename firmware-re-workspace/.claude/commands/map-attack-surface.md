# /map-attack-surface — Attack Surface Enumeration

Enumerate all services, interfaces, entry points, and communication channels exposed by the device. Build a comprehensive attack surface map before deep-dive analysis.

## Inputs
Ask: Path to extracted filesystem root?

---

## Network Services

### Listening Services
```bash
ROOT=[extracted_root]

# From config files
grep -r "port\s*=" "$ROOT"/etc/ 2>/dev/null | grep -viE "^#|report" | grep -v "^Binary"
grep -r "listen\|bind\|port" "$ROOT"/etc/ 2>/dev/null | grep -v "^Binary" | grep -v "^#" | head -30

# Hardcoded ports in binaries
strings "$ROOT"/usr/sbin/httpd 2>/dev/null | grep -E "^[0-9]{2,5}$" | sort -u
```

### Web Interface
```bash
# Web server type and version
strings "$ROOT"/usr/sbin/httpd 2>/dev/null | grep -iE "server:|version|boa|httpd|uhttpd|nginx|lighttpd|mini_httpd|goahead"

# Web root
find "$ROOT" -name "*.html" -o -name "*.htm" -o -name "*.cgi" -o -name "*.php" -o -name "*.lua" 2>/dev/null | head -20
find "$ROOT" -path "*/www*" -maxdepth 5 | head -20

# All CGI endpoints
find "$ROOT" -name "*.cgi" | sed 's|'"$ROOT"'||'

# API endpoints
grep -r "api\|/cgi-bin\|/goform" "$ROOT"/www/ 2>/dev/null | grep -v "^Binary" | grep -oE '"/[a-zA-Z/._?=-]+"' | sort -u | head -30
```

### Remote Access Services
```bash
# SSH
find "$ROOT" -name "sshd_config" -o -name "dropbear_*" 2>/dev/null | xargs cat 2>/dev/null | grep -E "^(Port|PermitRoot|PasswordAuth|PubkeyAuth)"

# Telnet
grep -r "telnetd" "$ROOT"/etc/ 2>/dev/null

# FTP
find "$ROOT" -name "*ftp*conf*" 2>/dev/null | xargs cat 2>/dev/null

# TFTP
grep -r "tftpd\|tftp" "$ROOT"/etc/ 2>/dev/null
```

### Network Management & Protocols
```bash
# SNMP
find "$ROOT" -name "snmpd.conf" 2>/dev/null | xargs cat 2>/dev/null

# UPnP
find "$ROOT" -name "*.xml" | xargs grep -l "upnp\|UPnP\|rootdevice" 2>/dev/null

# SSDP/mDNS/Bonjour
grep -r "ssdp\|mdns\|avahi\|bonjour" "$ROOT"/etc/ "$ROOT"/usr/ 2>/dev/null | grep -v "^Binary"

# MQTT (IoT)
grep -r "mqtt\|mosquitto" "$ROOT"/etc/ "$ROOT"/usr/ 2>/dev/null | grep -v "^Binary"

# RTSP/ONVIF (cameras)
grep -r "rtsp\|onvif" "$ROOT"/etc/ "$ROOT"/usr/ 2>/dev/null | grep -v "^Binary"
```

---

## Local Interfaces

### USB
```bash
strings "$ROOT"/usr/lib/*.so 2>/dev/null | grep -iE "usb|hiddev|gadget" | head -20
grep -r "usb\|gadget" "$ROOT"/etc/ 2>/dev/null | grep -v "^Binary"
```

### Serial / UART / Debug
```bash
grep -r "ttyS\|ttyUSB\|ttyAMA\|serial" "$ROOT"/etc/ 2>/dev/null | grep -v "^Binary"
grep -r "getty\|console" "$ROOT"/etc/inittab 2>/dev/null
```

### JTAG / SWD
```bash
# Usually not in firmware — check PCB physically
# But may find references in bootloader
strings "$ROOT"/../bootloader.bin 2>/dev/null | grep -iE "jtag|debug|openocd" | head -10
```

---

## Inter-Process Communication

```bash
# Shared memory, named pipes, sockets
find "$ROOT" -name "*.conf" | xargs grep -l "socket\|pipe\|shm\|semaphore" 2>/dev/null

# D-Bus (uncommon in embedded but possible)
find "$ROOT" -name "*.service" -o -name "*dbus*" 2>/dev/null

# NVRAM/environment variable IPC (very common in consumer routers)
grep -rn "nvram_get\|nvram_set\|getenv\|setenv" "$ROOT"/usr/lib/*.so 2>/dev/null | grep -v "^Binary" | head -20
```

---

## Attack Surface Map Output

Generate a structured map:

```markdown
## Attack Surface Map
**Target:** [device name]
**Date:** [date]

### External Network Interfaces
| Service | Protocol | Port | Authentication | Notes |
|---|---|---|---|---|
| Web Interface | HTTP/HTTPS | 80/443 | Password | GoAhead 2.x |
| SSH | SSH | 22 | Password/Key | Dropbear |
| Telnet | Telnet | 23 | None | CRITICAL — unauthenticated |
| SNMP | UDP | 161 | Community string | "public" default |
| UPnP | HTTP/SSDP | 1900/UDP | None | XML device description exposed |

### Local Interfaces
| Interface | Type | Notes |
|---|---|---|
| UART | Serial 115200 8N1 | U-Boot accessible, may drop to shell |
| JTAG | 10-pin header | CPU debug access |
| USB | USB-A host port | Mounts FAT volumes, firmware update |

### Key Entry Points for Further Analysis
1. **[Service/Component]** — [why it's interesting]
2. ...

### Recommended Analysis Priority
1. [highest priority attack surface]
2. [second priority]
3. ...
```

Save to `outputs/[target]-attack-surface-[date].md`
Log to `work-log/[date].md`
