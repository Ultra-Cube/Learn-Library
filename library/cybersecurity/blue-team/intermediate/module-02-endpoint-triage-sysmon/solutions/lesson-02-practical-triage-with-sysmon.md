# Solutions — Practical Endpoint Triage with Sysmon

## Exercises

1. Flow: alert -> related EID 1 events -> lineage -> EID 3/11 for network/files -> decision.
2. Persistence: Run keys, services/tasks; check EID 13/12 (Registry), EID 7 (ImageLoaded).

## Puzzle

Pull EID 1 details (cmdline/hashes), EID 3 (destinations), EID 11 (dropped files). Confirm via signatures/VT, isolate host, escalate.
