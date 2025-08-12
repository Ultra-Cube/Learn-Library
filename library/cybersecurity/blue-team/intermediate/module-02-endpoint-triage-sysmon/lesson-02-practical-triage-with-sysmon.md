---
id: CYB-BLT-INT-004
title: Practical Endpoint Triage with Sysmon
domain: Cybersecurity
track: Blue Team
level: Intermediate
module: Endpoint Triage with Sysmon
duration: 50m
prerequisites: [CYB-BLT-INT-003]
tags: [sysmon, triage]
sources:
  - https://learn.microsoft.com/sysinternals/downloads/sysmon
  - https://malpedia.caad.fkie.fraunhofer.de/ (for families/behaviors)
---

## Overview

Use Sysmon to investigate suspicious processes, network activity, and persistence artifacts.

## Learning objectives

- Build a quick triage flowchart
- Follow parent-child process trees
- Correlate process, network, and file events

## Key terms

- Parent-child — process lineage
- Persistence — mechanisms for autorun/launch
- Hashes — file integrity/identification

## Explanation

- Start at alert/event: gather related ProcessCreate events, track lineage, note command lines/hashes.
- Check NetworkConnect for outbound indicators; review FileCreate for dropped artifacts.
- Summarize findings and determine next steps (contain/isolate).

## Exercises

1. Draft a triage flow for suspicious PowerShell execution.
2. Identify two persistence mechanisms to review and the Sysmon events to check.

## Challenges & Activities

- Activity (10m): Build a simple parent-child tree for a known benign process.
- Challenge (20m): Given a hypothetical alert, outline the Sysmon events you’d pull and why.
- Stretch: Suggest one automation to accelerate triage.

## Puzzle

You see an unsigned binary spawning `powershell.exe -nop -w hidden -enc …` and connecting to a dynamic DNS domain. What triage steps and Sysmon events help confirm malicious behavior?

## Further reading

- Sysmon — [learn.microsoft.com](https://learn.microsoft.com/sysinternals/downloads/sysmon)
- Malpedia — [malpedia.caad.fkie.fraunhofer.de](https://malpedia.caad.fkie.fraunhofer.de/)
