# /quiz — Knowledge Assessment

Usage: `/quiz` (current level) or `/quiz [level]` or `/quiz [topic]`

## Quiz Generation Protocol

1. **Read `context/role.md`** to establish current level (default if not specified).
2. **Generate 5 questions** calibrated to the specified level:
   - 2 recall questions (definitions, procedures)
   - 2 application questions (fault scenarios, circuit logic)
   - 1 analysis question (why something is designed a certain way, or what would happen if...)
3. **Present questions one at a time.** Wait for learner response before proceeding.
4. **After each answer:**
   - Confirm correct, or explain the correct answer
   - Explain *why* — not just what the right answer is
   - For safety-critical questions, always reinforce the safety implication
5. **At the end of 5 questions:** Give a brief summary — areas strong, areas to revisit.

## Sample Questions by Level

### L1 Foundation
- "What does a single yellow signal aspect mean to a driver, and what action does it require?"
- "If a track circuit relay de-energizes due to a broken feed cable, what state does the signal associated with that track circuit show? Why?"

### L2 Developing
- "You're called to a track circuit fault. The track circuit relay is energized but weak. List three possible causes in order of likelihood."
- "What is the difference between route locking and approach locking? Give an example of when approach locking prevents an action that route locking wouldn't."

### L3 Competent
- "An axle counter section shows 'in' count of 4 and 'out' count of 2. A lineman has walked the section and confirmed no train is present. What process must be followed before the section can be reset, and who can authorize it?"
- "Explain why a relay interlocking uses vital relays (forced-guided contacts) rather than standard relays."

### L4 Proficient
- "A new CBI interlocking is being commissioned. What does 'SIL 4 certification' mean in practice, and what evidence would you expect to see in the safety case?"
- "Compare ETCS Level 1 and Level 2 from a signaling infrastructure perspective. What are the main operational and safety trade-offs?"
