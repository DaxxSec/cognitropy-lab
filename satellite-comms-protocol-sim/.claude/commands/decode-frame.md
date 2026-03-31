# decode-frame

Parse and decode a satellite protocol frame from hex, binary, or base64 input.

When this command is invoked:

1. **Get the frame data** — Ask the user to paste hex bytes, a binary string, or base64-encoded frame data. Also ask which protocol they think it is (or "unknown" if they want the agent to identify it).

2. **Identify the protocol** if unknown:
   - Look for flag bytes (0x7E = AX.25/HDLC)
   - Look for CCSDS sync marker (0x1ACFFC1D)
   - Look for KISS framing (0xC0 start/end)
   - Look for NMEA sentences (starts with $)
   - Look for DVB-S2 BBFRAME structure
   - Note what the signal frequency context was, if known

3. **Parse the frame** using the appropriate structure:
   - Show the raw hex with field boundaries annotated
   - Break down each field: name, byte offset, raw value, decoded meaning
   - For AX.25: decode callsigns (bit shift), control byte, PID, info field
   - For CCSDS: decode spacecraft ID, VCID, FSN, secondary header if present
   - For Space Packets: decode APID, sequence count, packet length

4. **Validate the frame**:
   - Check CRC/FCS and report whether it validates
   - Flag any malformed fields or unusual values
   - Note if frame length doesn't match declared length field

5. **Produce annotated output**:
   ```
   RAW: 7E 82 A0 A4 A6 A8 40 9C 60 94 A8 A0 40 03 F0 ...

   FIELD BREAKDOWN:
   [0]      7E          → AX.25 frame flag
   [1-7]    82A0A4A6A840 → Destination: W6XYZ-0
   [8-14]   9C6094A8A040 → Source: N6ABC-0 (end of address)
   [15]     03          → Control: UI frame
   [16]     F0          → PID: No layer 3 (APRS)
   [17-N]   ...         → Information field (APRS payload)
   [N+1-N+2] XXXX       → FCS: VALID ✅
   ```

6. **Interpret the payload** — If the info field contains APRS, CCSDS Space Packet data, or another recognizable application-layer format, decode that too.
