# Core Workflows — Wireless Protocol RE

## Workflow 1: Optimized Spectrum Discovery

**Goal:** Efficiently scan a wide frequency range and catalog all active signals.

### Steps
1. **Define scan range** — Get target frequency range, step size, and dwell time from user
2. **Apply weighted scheduling** — Prioritize ISM bands and known-active ranges using the weighted interval scheduling algorithm
3. **Configure SDR** — Set sample rate, gain, and antenna parameters
4. **Execute sweep** — Run `hackrf_sweep` or `rtl_power` with optimized parameters
5. **Parse results** — Identify peaks above noise floor, cluster nearby frequencies
6. **Score signals** — Apply priority scoring (novelty, strength, duty cycle, complexity)
7. **Generate discovery report** — Sorted list of signals with recommended analysis order
8. **Log to work-log/** — Record scan parameters, conditions, and results

### Decision Points
- If scan range > 10x SDR bandwidth: use sweep mode with band prioritization
- If known devices expected: front-load those frequencies in the schedule
- If time-constrained: apply epsilon-greedy dwell time optimization

## Workflow 2: Signal Decode Pipeline

**Goal:** Take an unknown signal from raw IQ to decoded protocol frames.

### Steps
1. **Load IQ capture** — Verify sample rate, center frequency, format (complex float32 or int8)
2. **Visual inspection** — FFT and waterfall analysis to confirm modulation type
3. **Modulation identification**
   - OOK/ASK: amplitude envelope shows binary pattern
   - FSK: instantaneous frequency shows discrete levels
   - PSK: constellation diagram shows phase clusters
   - OFDM: wide flat spectrum with subcarrier structure
4. **Demodulation** — Apply appropriate demodulator, output raw bitstream
5. **Bit synchronization** — Identify symbol rate, align to bit boundaries
6. **Frame detection** — Search for preamble/sync word patterns
7. **Field mapping** — Compare multiple frames to identify:
   - Static fields (device ID, protocol version)
   - Counter fields (incrementing values)
   - Payload fields (sensor data, commands)
   - Checksum/CRC fields (validate with known polynomials)
8. **CRC identification** — Try common CRC algorithms against frame data
9. **Document protocol** — Write frame specification to `outputs/`
10. **Log session** — Record all parameters and findings in `work-log/`

### Decision Points
- If modulation unclear: use Inspectrum for visual analysis before proceeding
- If CRC doesn't match known algorithms: try bit reversal, byte swapping, non-standard init values
- If protocol matches known: use `rtl_433` or URH's existing decoders to validate

## Workflow 3: Protocol State Machine Mapping

**Goal:** Build a complete state machine model of a wireless protocol's behavior.

### Steps
1. **Collect diverse captures** — Need multiple interaction types (startup, data, ack, error, shutdown)
2. **Classify frame types** — Group decoded frames by structure and command fields
3. **Identify transitions** — Map which frame types follow which others
4. **Build state diagram** — States = device modes, Transitions = frame exchanges
5. **Identify timing** — Measure inter-frame intervals, timeout behaviors
6. **Model error handling** — How does the protocol handle lost frames, CRC errors, timeouts?
7. **Document state machine** — Mermaid diagram + text specification
8. **Validate** — Replay captures against the model, verify all transitions are covered

### Output Format (Mermaid Example)
```
stateDiagram-v2
    [*] --> Idle
    Idle --> Sync: preamble_detected
    Sync --> RxHeader: sync_word_match
    RxHeader --> RxPayload: valid_header
    RxHeader --> Idle: invalid_header
    RxPayload --> Validate: frame_complete
    Validate --> Process: crc_ok
    Validate --> Idle: crc_fail
    Process --> Ack: command_processed
    Ack --> Idle: ack_sent
```

## Workflow 4: Comparative Protocol Analysis

**Goal:** Compare a captured signal against known protocol databases and signatures.

### Steps
1. **Extract signal parameters** — Frequency, modulation, symbol rate, bandwidth, frame structure
2. **Search known databases** — Check rtl_433 protocol list, Sigidwiki, FCC ID database, IEEE/ETSI specs
3. **Compute similarity scores** — For each candidate match:
   - Frequency match (exact, harmonic, or within ISM band)
   - Modulation match (type and parameters)
   - Symbol rate match (within +/-5%)
   - Frame structure similarity (preamble length, sync word, payload size)
4. **Rank candidates** — Sort by composite similarity score
5. **Validate top candidates** — Apply known decoder, check for valid output
6. **Report findings** — Known protocol match or "novel protocol" classification

### Similarity Scoring
```
match_score = (
    freq_match * 0.15 +
    mod_match * 0.25 +
    rate_match * 0.25 +
    frame_match * 0.35
)
```
Where each component is 0.0 (no match) to 1.0 (exact match).
