# /protocol-map — Build Protocol State Machine

Build a state machine model from captured and decoded frames.

## Required Inputs
- Decoded frame captures (from `/decode-signal` or user-provided)
- Frame type classifications (if known)
- Any protocol documentation

## Steps

### 1. Frame Classification
Group by structure, assign type labels (BEACON, DATA, ACK, NACK, POLL, RESPONSE), identify request-response pairs.

### 2. Temporal Analysis
Order by timestamp. Identify conversation sequences, measure inter-frame timing, detect periodic transmissions, identify timeouts and retransmissions.

### 3. State Identification
Map device states: Idle, Discovery/Pairing, Connected, Data Transfer, Error/Recovery, Sleep/Low Power.

### 4. Transition Mapping
For each state pair: trigger condition, frames exchanged, timing constraints, error fallbacks.

### 5. Generate Diagram
Output Mermaid state diagram and text spec with states, transitions, timing, and error paths.

### 6. Validate
Replay captured data against model, identify unmatched frames, flag gaps needing more captures.

Save to `outputs/protocol-state-machine-{name}.md`.
