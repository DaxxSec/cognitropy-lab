# /identify-target — Architecture & Target Identification

Determine the CPU architecture, operating system, endianness, bootloader, and format of an unknown firmware binary.

## Inputs
Ask: What is the path to the firmware file you want to identify?

---

## Identification Pipeline

Run all of these and synthesize the results:

### Step 1: File-Level Identification
```bash
file [firmware]
xxd [firmware] | head -30
strings [firmware] | head -100
ls -lh [firmware]
sha256sum [firmware]
```

### Step 2: Signature Scanning
```bash
binwalk [firmware]
binwalk -A [firmware]    # CPU opcode signatures
binwalk -E [firmware]    # Entropy analysis
```

### Step 3: String-Based Clues
```bash
strings [firmware] | grep -iE "linux version|kernel|uname"
strings [firmware] | grep -iE "mips|arm|x86|xtensa|powerpc|sparc|sh4|m68k"
strings [firmware] | grep -iE "busybox|openwrt|ddwrt|lede|freertos|vxworks|threadx|nucleus"
strings [firmware] | grep -iE "u-boot|grub|cfe|redboot|barebox"
strings [firmware] | grep -iE "buildroot|buildtime|compiled|version [0-9]"
strings [firmware] | grep -iE "gcc|clang|glibc|uclibc|musl|newlib"
```

### Step 4: Vendor / Brand Identification
```bash
strings [firmware] | grep -iE "copyright|vendor|manufacturer|model|product|device"
strings [firmware] | grep -iE "broadcom|qualcomm|atheros|mediatek|realtek|marvell|ralink"
strings [firmware] | grep -iE "cisco|linksys|netgear|asus|tplink|dlink|ubiquiti|mikrotik"
```

---

## Architecture Reference

Once you have clues, confirm architecture:

### MIPS
```bash
# Check byte patterns consistent with MIPS32 LE instruction encoding
python3 -c "
import sys
data = open('[firmware]','rb').read()
# MIPS LE: common opcodes like addiu, lw, sw start at certain byte patterns
# Look for 0x8f (lw), 0x24 (addiu) in first nibble of 4-byte words
nop_le = data.count(b'\x00\x00\x00\x00')
print(f'Null dwords: {nop_le}')
"
```

### ARM
```bash
# ARM Thumb2 or ARM32 — binwalk -A is usually sufficient
# ARM32 LE: instructions often end in \xe? (condition field)
# ARM Cortex-M (Thumb2): look for vector table at start (0x08000000 for STM32)
```

### x86/x64
```bash
# Clear from file command + binwalk usually
# Look for PE, ELF, or raw x86 with 0x55 0x89 0xe5 (push ebp; mov ebp, esp) pattern
```

---

## Synthesis: What to Report

After running the above, produce a structured identification card:

```markdown
## Target Identification
**Firmware File:** [filename]
**File Size:** [size]
**SHA256:** [hash]
**Date Identified:** [today's date]

### Architecture
- **CPU:** [MIPS32 / ARM Cortex-A / ARM Cortex-M / x86_64 / PowerPC / Xtensa / Unknown]
- **Endianness:** [Little Endian / Big Endian / Unknown]
- **ABI/ISA variant:** [e.g., MIPS32r2, ARMv7-A, Thumb2]

### Operating System / RTOS
- **OS:** [Linux / VxWorks / FreeRTOS / ThreadX / eCos / Bare Metal / Unknown]
- **Libc:** [glibc / uClibc / musl / newlib / Unknown]
- **Init System:** [BusyBox / systemd / init / Unknown]
- **Kernel Version:** [if found]

### Firmware Structure
- **Format:** [raw binary / ELF / PE / uImage / CHKSUM / Unknown]
- **Compression:** [gzip / lzma / xz / lzo / none / encrypted]
- **Filesystem:** [SquashFS / JFFS2 / UBIFS / CRAMFS / ext2 / none]
- **Sections identified:** [list from binwalk]

### Bootloader
- **Type:** [U-Boot / CFE / BootROM / GRUB / Custom / None detected]
- **Version:** [if found]

### Vendor / Brand
- **Likely vendor:** [based on strings/signatures]
- **Likely model:** [if found in strings]
- **Build date:** [if found]

### Recommended Next Steps
- [e.g., "Extract SquashFS with sasquatch"]
- [e.g., "Load in Ghidra with MIPS32 LE processor spec"]
- [e.g., "Architecture is unclear — recommend JTAG extraction for confirmation"]
```

---

## Save Output

Save the identification card to `outputs/[target]-identification-[date].md`
Update `context/project.md` with confirmed architecture and OS.
Log to `work-log/[date].md`.
