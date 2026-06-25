# Microcontroller Firmware Development — Reference Tables

Compact lookup data the agent grep's during a task. Numbers are order-of-magnitude for **cost-benefit framing** — always confirm against the live datasheet and your distributor's price.

## MCU Family Quick-Compare (order-of-magnitude)

| Family / example | Core | Flash / RAM (typical) | Active | Deep-sleep | ~Unit $ (vol) | Best for |
|---|---|---|---|---|---|---|
| AVR (ATtiny/ATmega) | 8-bit | 2–256 KB / 0.1–32 KB | ~0.2 mA/MHz | ~0.1 µA | $0.30–2 | cheap simple control |
| MSP430 | 16-bit | 1–256 KB / 0.1–66 KB | ~0.1 mA/MHz | ~0.5 µA | $0.50–3 | ultra-low-power sensing |
| STM32C0/G0 (M0+) | M0+ | 16–512 KB / 6–144 KB | ~0.1 mA/MHz | ~0.5 µA | $0.40–3 | low-cost 32-bit |
| STM32F4 / L4 | M4F | 256K–2M / 64–320 KB | ~0.1–0.2 mA/MHz | ~0.3 µA (L4 stop) | $2–8 | mainstream / DSP / low-power |
| nRF52832/840 | M4F + BLE | 256K–1M / 64–256 KB | ~3–5 mA radio | ~0.4 µA System OFF | $2–5 | BLE products |
| ESP32 (-S/-C) | LX6/RISC-V + Wi-Fi/BT | ext flash / 0.3–0.5 MB | ~20–240 mA Wi-Fi | ~5–10 µA | $1–3 | Wi-Fi/BT, ext flash |
| Cortex-M7 (STM32H7) | M7 + cache | 1–2 M / 0.5–1 MB | higher | — | $6–15 | high-throughput control |

## Memory Budget Cheat-Sheet

| Lever | Typical flash impact | Notes |
|---|---|---|
| `newlib-nano` vs full newlib | saves several KB | lose some `printf` features |
| `printf` float support | costs ~2–6 KB | gate behind a flag |
| `-Os` vs `-O2` | `-Os` smaller, `-O2` faster | measure both |
| `-flto` (LTO) | a few % smaller | longer link, harder debug |
| `--gc-sections` + `-ffunction-sections` | drops dead code | almost always on |
| Vendor HAL vs registers | HAL can cost 5–20 KB | trade dev-speed vs size |

Read the **`.map`** for attribution; `arm-none-eabi-size` for totals. **Worst-case stack** must be analyzed, not guessed.

## Peripheral Selection Quick-Reference

| Need | Cheapest fit | Step up if… |
|---|---|---|
| Periodic event | timer IRQ | many events → DMA/timer |
| Bulk move | DMA | CPU-bound copy is the bottleneck |
| Short-range comm | UART/SPI/I²C | distance/noise → CAN/RS-485 |
| Connectivity | on-chip radio SoC | saves BOM vs MCU+module |
| Analog in | on-chip ADC | accuracy/speed → external ADC |

## Power-Mode Ladder (typical)

| Mode | Current | Wake latency | Retains |
|---|---|---|---|
| Run | mA (∝ MHz) | — | all |
| Sleep | ~½ run | instant | all |
| Stop / Deep-sleep | µA | µs–ms | RAM (+ some periph) |
| Standby/Shutdown | nA–µA | ms (reset-like) | little/none |

Battery life ≈ capacity(mAh) ÷ average current(mA). Average current is set by the **duty cycle**.

## Cost Currencies (name them in every trade)

| Currency | Unit | Scarce when… |
|---|---|---|
| Flash | bytes | small part / late project |
| RAM | bytes | buffers, RTOS, stacks |
| Energy | µA average | battery/coin-cell |
| CPU | cycles / % load | tight control loops |
| Unit cost (COGS) | $ / unit | high volume |
| Engineering (NRE) | dev-hours | low volume / deadline |
| Certification | $ + time | safety/radio/medical |

## Upstream Catalogues & Standards

- **ARM Cortex-M / CMSIS** — https://developer.arm.com/Processors/Cortex-M — core docs + standard HAL interface.
- **FreeRTOS** — https://www.freertos.org/ — RTOS reference for the scheduling trade.
- **Zephyr Project** — https://www.zephyrproject.org/ — RTOS + driver model + build system.
- **MISRA C** — https://www.misra.org.uk/ — safety-relevant coding guidelines.
- **IEC 61508 functional safety** — https://www.iec.ch/functional-safety — the safety-cost line.
- Vendor sites (ST, Nordic, TI, Espressif, Microchip) — datasheets, errata, and **the price** that anchors every cost trade.

## Operating Cheat-Sheet

- The MCU choice fixes flash/RAM/power/COGS for the product's life — spend the most analysis there.
- Optimize only a **tight** budget; profile (`.map`/ammeter) before, re-measure after.
- Build-vs-buy TCO = buy price + integration + maintenance + **license** + certification risk.
- NRE vs COGS flips with volume — let the real volume pick.
- Safety, update authentication, and software licenses are not currencies to spend.
