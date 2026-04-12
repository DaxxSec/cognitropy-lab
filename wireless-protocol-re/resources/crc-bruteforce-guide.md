# CRC Bruteforce & Identification Guide

## When to Use This Guide
After extracting raw frame data, you need to identify the CRC/checksum algorithm protecting the frame. This is often the hardest part of protocol RE.

## Step 1: Isolate the Checksum Bytes
1. Capture multiple frames from the same device
2. Identify which bytes change between identical-length frames
3. The last 1–4 changing bytes are usually the checksum
4. The checksum should change even when payload is similar

## Step 2: Try Common Algorithms (In Order of Likelihood)

### Simple Checksums
```
# Additive checksum (sum of all payload bytes, truncated)
checksum = sum(payload_bytes) & 0xFF  # 8-bit
checksum = sum(payload_bytes) & 0xFFFF  # 16-bit

# XOR checksum
checksum = 0
for byte in payload_bytes:
    checksum ^= byte
```

### CRC-8 Variants
Try these polynomials with init=0x00 first, then init=0xFF:
- 0x07 (CRC-8 standard)
- 0x31 (CRC-8/MAXIM — very common in ISM devices)
- 0x9B (CRC-8/WCDMA)
- 0xD5 (CRC-8/DVB-S2)

### CRC-16 Variants
Try these polynomials:
- 0x8005, init=0x0000 (CRC-16/IBM — Modbus, USB)
- 0x1021, init=0xFFFF (CRC-16/CCITT — X.25, Bluetooth)
- 0x1021, init=0x0000 (CRC-16/KERMIT — very common in ISM)
- 0x8005, init=0xFFFF (CRC-16/MODBUS)
- 0x1021, init=0x1D0F (CRC-16/AUG-CCITT)

## Step 3: Bit Order Variations
If standard polynomials don't match, try:
1. **Reverse bit order** within each byte (reflect input)
2. **Reverse byte order** of the CRC result
3. **XOR the result** with 0xFF or 0xFFFF (final XOR)
4. **Different data range** — CRC might not cover all bytes (try excluding preamble, sync, or the CRC itself)

## Step 4: Automated Tools

### reveng (CRC RevEng)
```bash
# Provide hex strings of complete frames (with CRC)
reveng -w 8 -s DEADBEEF01 DEADBEEF02 DEADBEEF03
reveng -w 16 -s DEADBEEFCAFE01 DEADBEEFCAFE02
```

### Python crcmod
```python
import crcmod

# Try common CRC-16 algorithms
for poly in [0x18005, 0x11021]:
    for init in [0x0000, 0xFFFF]:
        for rev in [True, False]:
            crc_fn = crcmod.mkCrcFun(poly, initCrc=init, rev=rev)
            result = crc_fn(payload)
            if result == expected_crc:
                print(f"Match: poly={hex(poly)} init={hex(init)} rev={rev}")
```

### CyberChef
Use the CRC operation with different parameters. Good for quick manual testing.

## Step 5: Validation
Once you find a match:
1. Verify against at least 5 different frames
2. Confirm which bytes are included in the CRC calculation
3. Document the complete CRC specification:
   - Polynomial
   - Width (8, 16, 32)
   - Init value
   - Input reflection (yes/no)
   - Output reflection (yes/no)
   - Final XOR value
   - Byte range included in calculation

## Common Gotchas
- Some protocols compute CRC over the **length byte** but not the preamble/sync
- Manchester-encoded data: CRC is computed on the **decoded** bytes, not the raw bits
- Some devices use a **lookup table** with a non-standard polynomial
- Nibble-ordered protocols (Oregon Scientific) need nibble-swapping before CRC
- Some protocols include the **device ID** in the CRC but not in the visible frame
