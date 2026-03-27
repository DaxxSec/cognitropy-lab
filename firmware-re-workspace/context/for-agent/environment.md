# User Environment
<!-- Populated during /onboard — agent reads this to calibrate tool suggestions -->

## Operating System
- **OS:** [Linux distro / macOS / Windows WSL2]
- **Architecture:** [x86_64 / ARM / other]
- **Virtualization:** [Docker available / VMs / bare metal]

## Installed Tools

### Extraction & Identification
- binwalk: [yes/no — version if known]
- file: [yes/no]
- xxd / hexdump: [yes/no]
- 7zip / p7zip: [yes/no]
- jefferson (JFFS2): [yes/no]
- ubireader (UBIFS): [yes/no]
- sasquatch (non-standard squashfs): [yes/no]
- firmwalker: [yes/no]

### Disassembly / Decompilation
- Ghidra: [yes/no — version]
- radare2 / Cutter: [yes/no — version]
- Binary Ninja: [yes/no — version]
- IDA Pro/Free: [yes/no — version]
- objdump: [yes/no]
- capstone: [yes/no]

### Emulation
- qemu-user-static: [yes/no]
- qemu-system-*: [which targets]
- Unicorn Engine: [yes/no]
- FIRMAE / FirmAFL: [yes/no]

### Dynamic Analysis
- gdb / gdb-multiarch: [yes/no]
- strace / ltrace: [yes/no]
- frida: [yes/no]

### Scripting & Automation
- Python: [yes/no — version]
- pwntools: [yes/no]
- pycryptodome: [yes/no]
- angr: [yes/no]

### Hardware Interface
- OpenOCD: [yes/no]
- flashrom: [yes/no]
- minicom / picocom: [yes/no]
- Logic analyzer software: [e.g., sigrok/PulseView]

## Working Directory
- **Firmware storage path:** [e.g., ~/firmware-analysis/]
- **Workspace root:** [path to this workspace repo]
- **Outputs directory:** [outputs/ within this workspace]

## Notes
<!-- Any special configuration, limitations, or environment quirks -->
