# Microcontroller Firmware Development — Core Concepts

Background the agent reads before acting on a firmware design or optimization task. Optimised for fast recall and for *making the trade*, not exhaustive theory.

## MCU Architecture Families (the cost/benefit landscape)

| Family | Typical core | Sweet spot | Trade |
|---|---|---|---|
| **8-bit (AVR, 8051, PIC)** | proprietary | ultra-low cost, simple control | cheap unit + tiny RAM; painful for 32-bit math, comms stacks |
| **MSP430** | 16-bit | ultra-low-power sensing | excellent µA budget; modest compute |
| **ARM Cortex-M0/M0+** | 32-bit | low-cost 32-bit, deterministic | great $/feature; no cache, limited DSP |
| **Cortex-M3/M4(F)** | 32-bit + (FPU/DSP) | mainstream, signal work | M4F adds FPU/DSP for a little die/power |
| **Cortex-M7** | 32-bit, cache | high-throughput control | fast, but cache makes timing less deterministic |
| **RISC-V (e.g. ESP32-C, GD32V)** | 32-bit | royalty-free cores, low cost | growing ecosystem; tooling less mature than ARM |
| **Wireless SoC (nRF52/53, ESP32)** | M4/M33/RISC-V + radio | connected products | integrated radio saves BOM; flash split with stack |

The MCU choice is the **highest-leverage cost-benefit decision** in the project: it fixes the flash/RAM ceiling, the peripheral set, the power floor, and the per-unit cost for the product's life.

## Memory Hierarchy — the budgets that bind

| Memory | Holds | Scarcity | Notes |
|---|---|---|---|
| **Flash** | code + const data (`.text`, `.rodata`) | tight on small parts (8–256 KB) | the number that overflows late; watch the `.map` |
| **RAM (SRAM)** | `.data`, `.bss`, stack, heap | often tighter than flash | stack overflow is silent and lethal |
| **EEPROM / emulated** | small persistent config | very scarce, wear-limited | wear-leveling costs flash/RAM |
| **External (QSPI/PSRAM)** | large assets/buffers | adds BOM + pins + latency | a cost trade vs a bigger MCU |

**Static budget = flash/RAM from the `size`/`.map` output. Dynamic budget = worst-case stack + heap.** Both must fit with headroom; a part run at 99% flash leaves no room for a field fix.

## Peripherals & DMA

- **Timers** — PWM, input capture, periodic interrupts; usually the contended resource. DMA-driven timers free the CPU.
- **DMA** — moves data without CPU cycles; the cheapest "performance" you can buy, paid in setup complexity and a scarce channel count.
- **Comm**: UART (simple, slow), SPI (fast, master/slave), I²C (multi-drop, slow, addressing), CAN (robust, automotive/industrial), USB (host stack cost), and radio (BLE/802.15.4/Wi-Fi).
- **Analog**: ADC (resolution vs sample rate vs power), DAC, comparators. On-chip analog vs an external part is a recurring cost trade.

**Internal block vs external part** is a classic cost-benefit: an on-chip ADC/op-amp/RTC saves BOM and pins but may not meet spec; an external part costs money and board area but buys performance.

## Scheduling Models (free → expensive)

| Model | Cost | Buys |
|---|---|---|
| **Superloop (bare-metal)** | ~free, tiny | simplicity; fine for soft timing |
| **Superloop + interrupts** | low | responsiveness on events |
| **Cooperative scheduler** | small | structured tasks without preemption hazards |
| **Preemptive RTOS** (FreeRTOS/Zephyr) | few KB RAM/flash + complexity | hard-ish determinism, priorities, blocking APIs |

An RTOS is not "better" — it is a purchase. Buy it when the workload has genuinely concurrent, priority-ordered timing needs; don't pay its RAM and its race-condition surface for a blink-an-LED loop.

## Power Modes & the Energy Budget

- Modes scale **Run → Sleep → Stop/Deep-sleep → Standby/Shutdown**, trading current (mA → µA → nA) against wake latency and retained state.
- **Battery life ≈ capacity ÷ average current.** Average current is dominated by **duty cycle**: time in active vs sleep, and the cost of each wake (radio TX is usually the spike).
- Pricing a feature in **microamps** is as real as pricing it in dollars on a coin-cell product.

## Toolchain & Build Size

- GCC (`-Os` for size, `-O2` for speed), LTO, `--gc-sections` to drop unused code, `newlib-nano` vs full newlib (`printf` float support is expensive).
- The **`.map` file** is the source of truth for where flash/RAM went; the `size` tool gives the totals. Optimization decisions cite these, not vibes.

## Where Cost-Benefit Reasoning Attaches

Firmware is a sequence of trades; the economic concepts that apply:

- **Weighted decision matrix.** Score MCUs/options on weighted criteria (cost, flash, RAM, power, peripherals, ecosystem). Used by `/select-mcu` and `/build-vs-buy-stack`.
- **NRE vs COGS.** Non-recurring engineering (your hours, one-time) vs cost-of-goods (per unit, forever). At volume, a $0.20 cheaper MCU can dwarf weeks of dev; at low volume, the reverse. Volume sets the trade.
- **Marginal value of an optimization.** Bytes/cycles/µA saved are worth *nothing* until the budget is tight, then worth a lot. `/optimize-roi` ranks fixes by saving-per-engineering-hour and only acts when the budget demands.
- **Total cost of ownership (build-vs-buy).** Buy price + integration + maintenance + license + certification risk, over the product's life — not just the sticker.
- **Opportunity cost & schedule.** Engineering hours spent optimizing are hours not shipping; a deadline can make the slightly-more-expensive-but-done option the right one.
- **Real options / headroom.** Reserving flash/RAM/pins is buying the option to fix or extend in the field — usually cheap insurance.

## Common Failure Modes (of the *engineering*, not the chip)

- **Premature optimization** — hours spent shaving a budget that wasn't tight; the canonical waste.
- **Optimizing without profiling** — guessing the hot spot and being wrong; always read the `.map`/profiler first.
- **Flash/RAM blowout discovered late** — no budget tracked, no headroom reserved; the most common schedule-killer.
- **Over-specced MCU** — paying COGS forever for headroom the product never used.
- **Under-specced MCU** — a board re-spin (the most expensive mistake) because RAM or a peripheral ran out.
- **"Free" code that wasn't** — a GPL stack in a closed product, or a HAL that pulled in 18 KB; license and size are part of the cost.
- **Silent stack overflow** — no worst-case stack analysis; corrupts RAM intermittently.

## Operating Constraints

- **Safety standards** (IEC 61508 functional safety, ISO 26262 automotive, IEC 60601 medical) impose required rigor on safety-relevant firmware — cost-benefit operates *within* them, never against them.
- **Update security** — field updates must be authenticated (signed); skipping verification to save flash is a vulnerability, not an optimization.
- **Software licensing** — copyleft (GPL) vs permissive (MIT/BSD/Apache) vs commercial terms are real obligations and real costs in any build-vs-buy.
- **Radio/EMC compliance** (FCC Part 15, ETSI EN 300 328) applies to transmitters; certification is a cost to budget, not to evade.
- **Reproducible builds** — pin the toolchain and flags; size and timing numbers are only comparable when the build is.
