# /extract-fs — Filesystem Extraction

Guide the user through extracting a filesystem from a firmware blob, handling common formats and vendor quirks.

## Inputs
Ask: What is the path to the firmware blob or firmware binary?
Check `context/project.md` for current target context.

---

## Step 1: Identify Filesystem Type

```bash
binwalk [firmware]              # Look for filesystem signatures
file [firmware]
xxd [firmware] | head -20
```

**Common filesystem signatures to identify:**
| Magic Bytes | Filesystem | Tool |
|---|---|---|
| `68 73 71 73` / `73 71 73 68` | SquashFS (various endianness) | unsquashfs / sasquatch |
| `85 19` | JFFS2 | jefferson |
| `55 42 49 23` | UBIFS | ubireader |
| `1f 8b` | gzip compressed | gzip -d |
| `fd 37 7a 58` | xz compressed | xz -d |
| `42 5a 68` | bzip2 | bzip2 -d |
| `43 72 41 6d` | CRAMFS | mount -t cramfs |
| `27 05 19 56` | U-Boot uImage | binwalk / manual |

---

## Step 2: Extract Based on Type

### SquashFS
```bash
# Standard
unsquashfs -d outputs/squashfs-root/ squashfs.img

# If unsquashfs fails (vendor modifications), try sasquatch
sasquatch -d outputs/squashfs-root/ squashfs.img

# Check squashfs version
xxd squashfs.img | head -3
# s q s h = 0x73717368 → standard LE
# h s q s = 0x68737173 → Big-endian
```

### JFFS2
```bash
# Option 1: jefferson (recommended)
jefferson -d outputs/jffs2-root/ jffs2.img

# Option 2: MTD module (requires root)
modprobe mtdram total_size=65536 erase_size=256
modprobe mtdblock
dd if=jffs2.img of=/dev/mtd0
mkdir -p /mnt/jffs2
mount -t jffs2 /dev/mtdblock0 /mnt/jffs2
cp -a /mnt/jffs2/. outputs/jffs2-root/
umount /mnt/jffs2
```

### UBIFS (on UBI volume)
```bash
# Extract UBI image first
ubireader_extract_images firmware.bin

# Then extract UBIFS
ubireader_extract_files ubifs.img -o outputs/ubifs-root/
```

### YAFFS2
```bash
# yaffshiv or unyaffs
yaffshiv firmware.img
```

### CramFS
```bash
# Mount directly (read-only)
mkdir /mnt/cramfs
mount -t cramfs -o loop cramfs.img /mnt/cramfs
cp -a /mnt/cramfs/. outputs/cramfs-root/
umount /mnt/cramfs
```

### ext2/ext3/ext4
```bash
mkdir -p outputs/ext-root
mount -t ext4 -o ro,loop ext4.img outputs/ext-root
cp -a outputs/ext-root/. outputs/extracted-fs/
umount outputs/ext-root
```

### Compressed blob (no filesystem)
```bash
# gzip
gzip -cd firmware.bin > firmware_decompressed.bin

# LZMA
lzma -cd firmware.bin > firmware_decompressed.bin

# XZ
xz -cd firmware.bin > firmware_decompressed.bin
```

---

## Step 3: Verify Extraction

```bash
ls -la outputs/squashfs-root/         # Should look like a Linux root
ls outputs/squashfs-root/etc/         # etc/ should have config files
ls outputs/squashfs-root/bin/         # bin/ should have busybox, sh, etc.
file outputs/squashfs-root/bin/busybox    # Confirm architecture
```

---

## Step 4: Handle Extraction Failures

### Binwalk found nothing / Fully Encrypted
- Check if firmware requires a signature/key to verify or decrypt
- Look for decryption routine in bootloader portion of firmware
- Search vendor forums, GPL source releases, FCC filings
- Consider UART/JTAG extraction from running hardware

### Binwalk extracted scrambled data
- The vendor may use non-standard compression or encryption
- Try: `binwalk -e --run-as=root` (some extractors need root)
- Try extracting manually with `dd` using the offset from binwalk output:
  ```bash
  # If binwalk shows SquashFS at offset 0x123456
  dd if=firmware.bin of=squashfs.img bs=1 skip=$((0x123456))
  unsquashfs squashfs.img
  ```

### LZMA/XZ false positive
- Common issue with binwalk over-detecting LZMA
- Manually verify offset and size before extracting

---

## Post-Extraction Summary

After successful extraction, document:
- Filesystem type
- Extraction tool used
- Root path in `outputs/`
- Top-level directory listing
- Any extraction errors or anomalies

Update `context/project.md` with extraction results.
Suggest next step: `/analyze-firmware` or `/find-secrets`
