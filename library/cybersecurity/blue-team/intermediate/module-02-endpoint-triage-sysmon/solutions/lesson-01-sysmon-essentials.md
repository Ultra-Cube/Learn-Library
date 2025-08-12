# Solutions — Sysmon Essentials and Event Mapping

## Exercises

1. Useful events: 1 (ProcessCreate), 3 (NetworkConnect), 11 (FileCreate).
2. Map: EID 1 (PowerShell) -> ATT&CK T1059; EID 3 (C2) -> T1071.

## Puzzle

Confirm via EID 1 (process + cmdline), EID 3 (network), and parent-child lineage. Likely LOLBAS or living-off-the-land technique.
