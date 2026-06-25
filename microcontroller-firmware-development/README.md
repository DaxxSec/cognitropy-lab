# Microcontroller Firmware Development Workspace

> Build firmware the way a budget-holder would — every flash byte, microamp, dollar, and dev-hour is a currency, and every design decision is a trade you can show the math for.

## What This Workspace Does

This is a working environment for **microcontroller firmware development** run under an explicit **cost-benefit framework**. It treats the defining reality of embedded work — that resources are hard-bounded — as the organizing principle rather than an afterthought. An MCU has a fixed flash size, a fixed RAM size, a fixed peripheral set, a power envelope, a unit price that matters at volume, and a project that has finite engineering hours and a certification budget. Firmware engineering *is* the discipline of spending those budgets well, and this workspace makes that discipline explicit.

Today's technique — **cost-benefit analysis** — shapes every command. Choosing an MCU is a weighted decision over price, memory, peripherals, power, and ecosystem maturity (`/select-mcu`). Choosing a scheduler weighs a free superloop against an RTOS that buys determinism for a few kilobytes (`/rtos-vs-baremetal`). Choosing whether to write a driver or license a stack is a build-vs-buy with license and total-cost-of-ownership baked in (`/build-vs-buy-stack`). Even optimization is gated: shaving bytes or cycles only earns its keep when the budget is actually tight and the change won't cost more in maintainability than it saves (`/optimize-roi`). The memory budget (`/budget-flash-ram`), the energy budget (`/power-budget`), peripheral allocation (`/peripheral-allocation`), the field-update path (`/ota-update-design`), and the release decision (`/release-gate`) round out a kit where the answer is never "it depends" — it's "here is what it costs, here is what it buys."

## Why This Workspace Exists

Embedded projects rarely fail because something was impossible; they fail because a budget blew up late — flash ran out two weeks before tape-out, battery life came in at half the spec, an MCU was over-specced and the BOM lost the deal, or a "quick optimization" became an un-maintainable trap. Each of those is a cost-benefit decision that was made implicitly, without the numbers on the table. This workspace forces the numbers onto the table early and keeps a decision log, so trades are deliberate, defensible, and reversible. It also fixes three hard lines that naive cost-minimization will happily cross — safety certification, update security, and software licensing — so "cheaper" never quietly becomes "unsafe," "insecure," or "illegal."

## Getting Started

### Prerequisites

- A toolchain for your target (e.g. **arm-none-eabi-gcc** + CMSIS, or a vendor IDE) and the ability to read a **`.map` file** and **`size` output** for the flash/RAM budget.
- A debug probe (SWD/JTAG) and ideally a way to **measure current** (ammeter / power profiler) for the energy budget.
- Target MCU datasheet(s) and a **distributor price** at your expected volume for the cost side of any trade.
- Optional: an RTOS (FreeRTOS/Zephyr) and any candidate commercial/open-source stacks you're weighing.

### Quick Start

1. Clone this workspace and create a project folder: `outputs/projects/<name>/`.
2. Run `/select-mcu` with your requirements to produce a weighted MCU cost-benefit matrix.
3. Run `/budget-flash-ram` to set the initial memory budget and reserve headroom.
4. Run `/rtos-vs-baremetal` and `/power-budget` to lock the scheduling and energy envelopes before writing feature code.
5. As the project grows, gate every optimization with `/optimize-roi` and every defer/fix call with `/release-gate`, logging the math in the project folder.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/select-mcu` | Weighted cost-benefit MCU selection matrix | At project start, or when re-spinning the board |
| `/budget-flash-ram` | Allocate/track flash & RAM; decide cut vs optimize | Set early; revisit whenever a feature lands |
| `/rtos-vs-baremetal` | Superloop vs cooperative vs preemptive RTOS | Before committing the scheduling architecture |
| `/build-vs-buy-stack` | Commercial vs open-source vs in-house, license + TCO | Any non-trivial stack component (BLE, FS, TLS, GUI) |
| `/power-budget` | Duty-cycle + sleep-mode battery-life model | Battery devices; pricing a feature in microamps |
| `/optimize-roi` | Is this size/speed/power optimization worth it? | Before spending hours optimizing anything |
| `/peripheral-allocation` | Map functions to timers/DMA/comm; internal vs external | Pin/peripheral planning; resolving contention |
| `/ota-update-design` | Bootloader/OTA/DFU design: flash vs complexity vs security | Any field-updatable product |
| `/release-gate` | Defect & tech-debt triage for ship vs defer | Approaching a release or freeze |

## Directory Structure

```
microcontroller-firmware-development/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # Bespoke firmware + decision commands
├── context/
│   ├── concepts.md           # MCU families, memory, peripherals, scheduling, power, cost currencies
│   ├── workflows.md          # Selection matrix, budget loop, build-vs-buy tree, optimize-ROI gate
│   └── references.md         # MCU comparison, memory/cost cheat-sheet, peripheral/power tables, links
├── prompts/                  # Reusable cost-benefit decision prompt templates
└── outputs/                  # Per-project budgets, decision logs, selection matrices
```

## Example Use Cases

### A sensor node that has to hit a 2-year coin-cell life
`/power-budget` models the wake/measure/transmit duty cycle and finds the radio TX is the dominant cost; `/select-mcu` then trades a slightly pricier MCU with a better stop-mode current against the battery saving, and the decision is logged with both numbers.

### Flash overflow two weeks before release
`/budget-flash-ram` shows the C-library `printf` and a vendor HAL eating 18 KB. `/optimize-roi` ranks the fixes — swap to a tiny `printf`, drop the HAL for register access on two drivers — by bytes-saved per engineering-hour, and only the high-ROI ones get done.

### Build-vs-buy for a BLE stack
`/build-vs-buy-stack` weighs a commercial stack's per-unit license against the months of in-house work plus certification risk, with the GPL/permissive license terms of the open-source option made explicit so "free" isn't mistaken for "no obligation."

## Recommended MCP Servers

- **Filesystem MCP** — persist per-project budgets, decision logs, and `.map`-file captures under `outputs/`.
- **Fetch / HTTP MCP** — pull MCU datasheets, errata, distributor pricing, and RTOS/stack documentation for build-vs-buy and selection.
- **Git MCP** (optional) — correlate binary-size deltas with commits to keep the flash/RAM budget honest over time.

## Legal & Ethical Considerations

- **Safety certification is not a cost line to cut.** For safety-relevant devices, IEC 61508 / ISO 26262 (and domain standards like IEC 60601 for medical) impose requirements that cost-minimization must respect — never trade away required rigor for BOM or schedule.
- **Firmware updates must be authenticated.** An OTA/DFU path that skips signature verification to save flash is a security defect, not an optimization. Design updates to be signed and, where data is sensitive, encrypted.
- **Respect software licenses.** Build-vs-buy must account for license obligations (GPL copyleft vs permissive MIT/BSD/Apache, commercial redistribution terms). "Free" code can carry real obligations; surface them in the decision.
- **Radio & EMC compliance** (FCC Part 15 / ETSI EN 300 328, etc.) applies to anything that transmits — factor certification into cost, don't engineer around it.

## Technical References

- [ARM Cortex-M & CMSIS](https://developer.arm.com/Processors/Cortex-M) — the dominant 32-bit embedded core family and its standard HAL/interface layer.
- [FreeRTOS documentation](https://www.freertos.org/Documentation/RTOS_book.html) — reference for the RTOS side of the scheduling cost-benefit.
- [MISRA C](https://www.misra.org.uk/) — coding guidelines often required for safety-relevant firmware.
- [IEC 61508 (functional safety) overview](https://www.iec.ch/functional-safety) — the safety-cost line that must not be optimized away.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
