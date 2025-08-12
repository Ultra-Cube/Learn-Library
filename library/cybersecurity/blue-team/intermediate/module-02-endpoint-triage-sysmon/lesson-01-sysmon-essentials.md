---
id: CYB-BLT-INT-003
title: Sysmon Essentials and Event Mapping
domain: Cybersecurity
track: Blue Team
level: Intermediate
module: Endpoint Triage with Sysmon
duration: 45m
prerequisites: [CYB-BLT-INT-001]
tags: [sysmon, windows, endpoint]
sources:
  - https://learn.microsoft.com/sysinternals/downloads/sysmon
  - https://github.com/SwiftOnSecurity/sysmon-config
---

## Overview

Install Sysmon, understand key event types, and map them to detection use cases.

## Learning objectives

- Install/configure Sysmon
- Know key events (1 ProcessCreate, 3 NetworkConnect, 11 FileCreate, 7 ImageLoaded)
- Map events to ATT&CK techniques

## Key terms

- Sysmon — system monitor from Sysinternals producing detailed endpoint logs
- Event ID — unique identifier per Sysmon event type
- Config — XML rules controlling what Sysmon logs

## Explanation

- Install Sysmon with a reputable config (e.g., SwiftOnSecurity) and adjust to your environment.
- Capture command lines for ProcessCreate; include hashes if feasible.
- Use NetworkConnect to spot suspicious outbound connections.

## Exercises

1. List three Sysmon event IDs useful for initial triage and why.
2. Map one event to an ATT&CK technique with an example.

## Challenges & Activities

- Activity (10m): Review a sample Sysmon config and note key inclusions/exclusions.
- Challenge (20m): Propose two detection ideas using ProcessCreate and NetworkConnect.
- Stretch: Consider performance impact vs. visibility trade-offs.

## Puzzle

You see `regsvr32.exe` making an external connection and spawning `powershell.exe`. Which Sysmon events confirm this and what might it indicate?

## Further reading

- Sysmon — [learn.microsoft.com](https://learn.microsoft.com/sysinternals/downloads/sysmon)
- SwiftOnSecurity Config — [github.com/SwiftOnSecurity/sysmon-config](https://github.com/SwiftOnSecurity/sysmon-config)
