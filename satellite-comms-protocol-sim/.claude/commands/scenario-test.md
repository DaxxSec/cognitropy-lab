# scenario-test

Design and document a complete protocol scenario test plan.

When this command is invoked:

1. **Understand the test target** — Ask:
   - What system or component is being tested? (Ground station software, satellite modem, protocol parser, AX.25 stack, CCSDS TC processor, etc.)
   - What protocol and version?
   - What interface does the SUT expose? (TCP socket, serial port, audio, file input)
   - What is the test goal? (Compliance verification, regression testing, security testing, interoperability)

2. **Define test categories** — Generate test cases across:
   - **Nominal operation** — Standard, well-formed inputs
   - **Boundary conditions** — Minimum/maximum field values, empty fields, max-length frames
   - **Error handling** — Malformed frames, invalid CRCs, truncated data
   - **Sequence testing** — Multi-frame sequences, state machine transitions
   - **Performance/timing** — Rapid frame injection, timing constraints
   - **Security cases** — If applicable: spoofed addresses, replayed frames, oversized inputs

3. **Generate test vectors** — For each test case, produce:
   - The exact byte sequence to inject (as annotated hex)
   - The pre-conditions
   - The expected SUT behavior
   - The observable indicator of pass/fail
   - Python code snippet to generate/send the test vector if useful

4. **Format as test plan document**:
   ```
   TEST PLAN: [SUT Name] — [Protocol] Scenario Test
   Version: 1.0 | Date: [date]
   ============================================================
   TC-001: [Description]
   Pre-condition: ...
   Input: [hex bytes with annotation]
   Expected: ...
   Pass Criterion: ...
   ============================================================
   ```

5. **Provide execution guidance** — How to run the test suite, what tooling to use (gr-satellites, direwolf, nc, Python socket), and how to interpret results.

Aim to generate at least 10 test cases covering a reasonable range of scenarios. For security-focused testing, generate 15+ cases.
