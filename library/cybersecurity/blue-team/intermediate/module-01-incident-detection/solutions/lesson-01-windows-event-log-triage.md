# Solutions — Windows Event Log Triage Basics

## Exercises

1. 4624/4625 red flags: rapid failures then success, unusual logon types (e.g., 3 or 10 in odd contexts), off-hours spikes, rare sources.
2. Suspicious 4688: `powershell.exe -enc <base64>`, `rundll32.exe javascript:...` or LOLBAS patterns.

## Puzzle

Likely brute-force or credential stuffing locally, followed by successful logon and potentially execution via rundll32. Investigate account, source, and child processes.
