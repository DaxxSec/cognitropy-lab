# /peripheral-allocation

Map the firmware's functions onto the MCU's timers, DMA channels, and comm peripherals, resolving contention and weighing on-chip blocks against external parts — a cost trade in BOM, pins, and board area.

## Inputs

- The function list needing peripherals (PWM, capture, ADC sampling, UART/SPI/I²C/CAN, USB, radio)
- The MCU's peripheral inventory (timer count, DMA channels, comm instances, pin map)
- Performance/accuracy requirements per function

## Steps

1. List each function's **peripheral demand** (which timer mode, DMA need, data rate, pins).
2. Assign on-chip peripherals; flag **contention** (two functions wanting the same timer/DMA channel/pin).
3. Resolve contention by sharing (time-multiplex), reassigning, or — as a cost trade — adding an **external part**.
4. For each "on-chip vs external" call, weigh BOM + pins + board area (external) against on-chip spec limits.
5. Verify DMA channel and pin-mux feasibility against the datasheet; record the allocation map.

## Output

`outputs/projects/<name>/peripheral-map.md` — the function-to-peripheral assignment, contention resolutions, any internal-vs-external decisions with their cost rationale, and the pin map.

## Notes

- DMA is the cheapest performance you can buy (CPU cycles freed) but channels are scarce — allocate them to the highest-rate movers.
- An on-chip ADC/op-amp that *just* misses spec costs more in rework than the external part would have up front — decide on the datasheet, not optimism.
