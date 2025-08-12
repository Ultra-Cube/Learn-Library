---
id: CYB-BLT-INT-012
title: Common Scenarios (Malware, Data Breach, Account Compromise)
domain: Cybersecurity
track: Blue Team
level: Intermediate
module: Incident Response Playbooks
duration: 50m
prerequisites: [CYB-BLT-INT-011]
tags: [incident-response, scenarios, breach, malware]
sources:
  - https://www.sans.org/white-papers/33901/
  - https://attack.mitre.org/
  - https://www.cisa.gov/sites/default/files/publications/Federal_Government_Cybersecurity_Incident_and_Vulnerability_Response_Playbooks_508C.pdf
---

## Overview

Apply playbook fundamentals to three common scenarios: malware infection, data breach, and account compromise.

## Learning objectives

- Adapt playbook templates to specific incident types
- Include scenario-specific investigation steps and evidence
- Plan recovery actions and post-incident activities

## Key terms

- IOC — indicator of compromise (file hash, IP, domain)
- Breach timeline — reconstructed sequence of attacker actions
- Password reset — credential invalidation and replacement

## Explanation

Each scenario needs tailored steps:

**Malware**: Isolate -> Image -> Analyze -> IOC extraction -> Hunt for lateral spread
**Data Breach**: Scope -> Timeline -> Affected records -> Notification requirements -> Legal/PR
**Account Compromise**: Reset credentials -> Review access logs -> Check for persistence -> Monitor for re-compromise

Include environment-specific details: backup procedures, notification lists, legal requirements, and vendor contacts.

## Exercises

1. List 5 investigation steps specific to a data breach (vs. general incident steps).
2. Design a password reset procedure that balances speed with thoroughness.

## Challenges & Activities

- Activity (10m): Create an IOC extraction checklist for malware incidents.
- Challenge (30m): Draft a breach notification timeline with legal/regulatory deadlines.
- Stretch: Add a "lessons learned" template with improvement actions.

## Puzzle

During an account compromise investigation, you find the attacker used the victim's VPN and accessed sensitive files. What additional steps does this scenario require beyond basic credential reset?

## Further reading

- SANS Incident Response — [sans.org](https://www.sans.org/white-papers/33901/)
- MITRE ATT&CK — [attack.mitre.org](https://attack.mitre.org/)
- CISA Playbooks — [cisa.gov](https://www.cisa.gov/sites/default/files/publications/Federal_Government_Cybersecurity_Incident_and_Vulnerability_Response_Playbooks_508C.pdf)
