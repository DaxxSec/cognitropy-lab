# Protocol Map

Guided reverse engineering workflow for an unknown or undocumented automotive RF protocol.

## When to use this

Use `/protocol-map` when:
- rtl_433 shows a signal it can't decode (outputs raw bytes or `UNKNOWN`)
- You have a sensor that isn't in the rtl_433 device list
- You want to go beyond the decoder and understand the actual protocol structure

## What I'll walk you through

### Phase 1: Signal Characterization
Provide a `.cu8` / `.cs16` IQ capture or a waterfall/amplitude screenshot. I'll help determine:
- Center frequency and bandwidth
- Modulation type (OOK vs FSK vs other)
- Symbol rate and pulse widths
- Packet timing and repetition rate

### Phase 2: Bit Extraction
Using inspectrum or URH, we'll:
- Set sample rate and modulation parameters
- Extract a clean bit stream
- Identify preamble and sync patterns

### Phase 3: Field Analysis
With a corpus of 6–10 captured packets:
- Identify fixed vs. variable bytes
- Cross-reference against typical TPMS field order (ID | pressure | temp | flags | checksum)
- Apply known pressure/temperature conversion formulas to candidate bytes
- Validate against physical sensor readings if available

### Phase 4: Checksum Reverse Engineering
- Collect packet variants (different pressure values, etc.)
- Isolate checksum byte(s)
- Run CRC brute-force: `python3 -c "import crcmod; ..."`
- Test common automotive checksums: CRC-8/SMBUS, XOR-sum, sum-modulo

### Phase 5: Flex Decoder
Once the protocol is mapped, use `/flex-decoder` to generate the rtl_433 configuration.

## Start Here

To begin, share your capture or describe the sensor (vehicle, FCC ID, frequency you captured it on).
