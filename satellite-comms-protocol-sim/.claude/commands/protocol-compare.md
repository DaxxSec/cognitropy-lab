# protocol-compare

Side-by-side comparison of two satellite communication protocols or protocol implementations.

When this command is invoked:

1. **Identify the two protocols to compare** — Examples:
   - AX.25 vs. CCSDS TC for cubesat commanding
   - DVB-S2 vs. DVB-S2X for high-throughput downlink
   - APRS vs. raw AX.25 for position reporting
   - Unprotected CCSDS TC vs. CCSDS TC with Security Layer (CCSDS 352)
   - Two different implementations of the same protocol (e.g., two open-source AX.25 stacks)

2. **Define comparison dimensions** — Based on the user's goal, select relevant dimensions from:
   - Frame/packet structure (header overhead, payload efficiency)
   - Maximum data rate or throughput
   - Error detection/correction capability
   - Authentication and security features
   - Implementation complexity
   - Hardware requirements
   - Standards compliance and documentation quality
   - Community adoption and tooling availability
   - Licensing/regulatory constraints

3. **Produce a comparison matrix**:
   ```
   PROTOCOL COMPARISON: AX.25 vs. CCSDS TC Transfer Frame
   ==========================================================
   Dimension            | AX.25              | CCSDS TC
   ---------------------|--------------------|-----------------
   Header overhead      | 15+ bytes          | 5 bytes
   Max payload          | 256 bytes (std)    | ~1019 bytes
   Authentication       | None               | Optional (CCSDS 352)
   Error detection      | CRC-CCITT (16-bit) | CRC-CCITT (16-bit)
   Sequence numbering   | Yes (I-frames)     | Yes (FSN 0-255)
   Addressing           | Callsign-based     | SCID + VCID
   Regulatory           | Amateur license    | No restriction
   Tool support         | Excellent          | Good (YAMCS, etc.)
   ...
   ```

4. **Provide a recommendation** — Based on the user's use case, which protocol is better suited and why? Be specific: don't say "it depends" without explaining exactly what it depends on.

5. **Frame structure visual** — For each protocol, show a byte-level frame layout diagram so the user can see the structural differences at a glance.

6. **Migration consideration** — If the user is considering switching from one to the other, what are the key differences to address in the implementation?
