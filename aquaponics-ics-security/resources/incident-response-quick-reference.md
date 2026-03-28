# Incident Response Quick Reference — Aquaponics ICS

## Immediate Decision Matrix

```
SUSPECTED COMPROMISE DETECTED
         │
         ▼
Is biological system stable?
(DO >6, pumps running, no alarm)
    │              │
   YES             NO
    │              │
    ▼              ▼
Proceed to     MANUAL MONITORING
containment    FIRST — alert staff,
               check DO/temp manually
                      │
                      ▼
               THEN begin containment
```

## Safe vs. Risky Containment Actions

| Action | Biological Risk | Authorized by |
|--------|----------------|--------------|
| Block internet at firewall | NONE | Security analyst |
| Revoke external VPN credentials | NONE | Security analyst |
| Change SCADA/HMI passwords | NONE | Security analyst |
| Disable vendor remote access | NONE | Security analyst |
| Isolate OT VLAN from IT | LOW (monitoring loss only) | Security analyst + biological operator |
| Reboot SCADA/HMI server | MEDIUM (loss of visibility) | Biological operator must be present |
| Reboot PLC | HIGH (pump disruption) | Biological operator + maintenance window |
| Re-image controller | CRITICAL — manual operation required | Full team, biological op in manual mode |

## Evidence Collection Checklist

### Network Evidence
- [ ] `tcpdump -i [OT_iface] -w evidence_ot_$(date +%Y%m%d_%H%M%S).pcap`
- [ ] Export firewall/router logs covering past 30 days
- [ ] DHCP lease history
- [ ] DNS query logs (if captured)
- [ ] WiFi association logs

### Windows SCADA/HMI Host
- [ ] `wevtutil epl Security security_$(date +%Y%m%d).evtx`
- [ ] `wevtutil epl System system_$(date +%Y%m%d).evtx`
- [ ] `wevtutil epl Application app_$(date +%Y%m%d).evtx`
- [ ] Running processes: `tasklist /v > processes.txt`
- [ ] Network connections: `netstat -anob > netstat.txt`
- [ ] Autoruns: (use Autoruns/autorunsc from Sysinternals)
- [ ] Prefetch: copy `C:\Windows\Prefetch\` directory
- [ ] Recent files: check `C:\Users\[user]\AppData\Recent`

### Linux / Raspberry Pi Controller
```bash
# Critical artifacts
last -w > logins.txt
who > who.txt
ps aux > processes.txt
netstat -antp > netstat.txt 2>/dev/null || ss -antp > netstat.txt
crontab -l > crontab.txt
cat /etc/crontab >> crontab.txt
ls -la /etc/cron.d/ >> crontab.txt

# Log collection
cp /var/log/auth.log auth.log
cp /var/log/syslog syslog.log
cp /var/log/daemon.log daemon.log
journalctl --no-pager > journal.txt

# Recent file modifications (last 7 days)
find / -newer /etc/passwd -mtime -7 -type f 2>/dev/null > recent_files.txt

# Hash all evidence
sha256sum *.log *.txt > evidence_hashes.txt
```

### PLC Evidence (Limited)
- Export current PLC program logic (compare to known-good backup)
- Export PLC audit log (if available on model)
- Document current setpoint values vs. expected
- Photo/screenshot current HMI display state

## CISA Reporting
If the incident involves confirmed compromise of water/food production control systems:
- CISA 24/7 hotline: 1-888-282-0870
- Email: CISAservicedesk@cisa.dhs.gov
- Online: https://myservices.cisa.gov/report
- FDA CFSAN (for FDA-regulated aquaculture): 1-866-300-4374

## Post-Incident Verification Checklist (Before Returning to Automated Operation)
- [ ] All credentials changed (PLCs, HMIs, SCADA, VPN, cloud platforms, SSH keys)
- [ ] PLC logic verified against signed backup
- [ ] All network connections verified as authorized
- [ ] Logging confirmed working and forwarding to SIEM/collector
- [ ] Biological parameters manually verified stable for minimum 2 hours
- [ ] Operator briefed and confident in automated operation resumption
- [ ] Incident timeline documented
- [ ] Root cause identified and remediated (not just cleaned up)
