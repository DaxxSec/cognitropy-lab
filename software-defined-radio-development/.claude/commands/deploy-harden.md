# /deploy-harden

Prepare an SDR application for headless / embedded deployment — service management, watchdog, thermal, USB stability, auto-recovery.

## Inputs

- **Flowgraph** + its validated resource profile (from `/throughput-profile`).
- **Target platform** — Raspberry Pi, x86 mini-PC, embedded SBC, cloud VM.
- **Operating mode** — continuous 24/7, scheduled, on-demand.
- **Failure tolerance** — must auto-recover? acceptable downtime? alerting needed?
- **Physical environment** — ambient temperature, power stability, enclosure.

## Steps

1. Read `context/workflows.md` "Deployment hardening".
2. Convert the flowgraph to a headless Python script (no GUI sinks; replace QT sinks with file/network/null sinks).
3. Create a systemd service: `Restart=always`, `RestartSec`, resource limits, `After=` USB/network dependencies, CPU affinity if needed.
4. Add a watchdog — heartbeat file or systemd `WatchdogSec` + `sd_notify`; restart the flowgraph if it stalls (overrun storm, USB drop).
5. Thermal management — on Pi/SBC, monitor SoC temp; if the resource profile is near the throttle point, add active cooling or reduce sample rate. Document the thermal headroom.
6. USB stability — SDR-over-USB is a common failure point: disable USB autosuspend (`usbcore.autosuspend=-1`), pin the device by serial (udev rule), handle device-disconnect/reconnect gracefully.
7. Storage management — if capturing, log rotation / ring buffer / disk-full handling so the service doesn't crash on a full disk.
8. Alerting — optional: push a notification on restart/failure (webhook, MQTT, email).
9. Boot persistence — enable the service, test a full reboot cycle, confirm clean auto-start.
10. Write the deployment package to `outputs/deploy/<app>/` (systemd unit, udev rule, watchdog script, README).

## Output

A deployment package at `outputs/deploy/<app>/` containing: headless flowgraph script, systemd unit file, udev rule (device-by-serial), watchdog script, thermal/USB sysctl settings, log-rotation config, optional alerting hook, and a deployment README with the reboot-test procedure. Plus a hardening checklist in `outputs/deploy/<app>/checklist.md`.

## Decision points

- **If the resource profile has <20% thermal/CPU headroom on the target** → either add cooling, reduce sample rate, or pick a more powerful platform before deploying; tight headroom + 24/7 = eventual failure.
- **If USB drops are frequent on the target** → check power supply (under-powered Pi USB is a classic culprit), use a powered hub, pin the device by serial.
- **If the app captures to disk continuously** → ring buffer or rotation is mandatory; a full disk crashing the service at 3 AM is the predictable failure.

## Notes

- USB autosuspend silently killing the SDR mid-run is the #1 embedded-SDR failure; disable it explicitly.
- Pin the SDR by serial in a udev rule — `/dev/swradio0` numbering is not stable across reboots/replugs.
- Test the FULL reboot cycle, not just `systemctl start` — boot-order dependencies (USB enumeration, network) surface only on cold boot.
- Quote the measured thermal headroom in the deployment README; the next operator needs to know how close to the edge it runs.
