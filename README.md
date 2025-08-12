# Learn-Library

An open, extensible library of bite-sized lessons with explanations, sources, exercises, and puzzles—organized for growth and easy contribution.

- Website: [ucubetech.com](https://www.ucubetech.com)
- Organization: [github.com/company/ultra-cube](https://github.com/company/ultra-cube)

## Why this library

We want reliable, well-structured learning paths that are easy to expand. Each lesson includes:

- Clear explanation and learning objectives
- Curated, reputable sources
- Exercises and at least one puzzle
- Lightweight metadata for indexing and validation

## Structure

- `library/` – all content, organized by domain/track/level/module/lesson
- `templates/` – templates for new lessons and modules
- `scripts/` – utilities (e.g., metadata validator)
- `TEAM.md` – team info and social links
- `CONTRIBUTING.md` – how to add lessons and improve the library

Example path:

```text
library/
  cybersecurity/
    foundations/
      beginner/
        module-01-introduction/
          lesson-01-what-is-cybersecurity.md
          solutions/
            lesson-01-what-is-cybersecurity.md
```

## Lesson metadata (frontmatter)

Lessons start with YAML-like frontmatter used for indexing:

```yaml
---
id: CYB-FND-BEG-001
title: What is Cybersecurity?
domain: Cybersecurity
track: Foundations
level: Beginner
module: Introduction
duration: 30m
prerequisites: []
tags: [security, basics, risk]
sources:
  - https://www.cisa.gov/cybersecurity-101
  - https://www.nist.gov/topics/cybersecurity
---
```

Required fields: `id, title, domain, track, level, module, duration, prerequisites, tags, sources`

## Validate lessons

Run a quick validation to ensure metadata is present and consistent:

```zsh
python3 scripts/validate_lessons.py
```

No external packages are required.

## Contribute

See `CONTRIBUTING.md` for guidelines and quality bars. Use `templates/lesson-template.md` to start quickly.

## License

Content is released under CC BY 4.0. See `LICENSE`.

## Quick index — tutorials and challenges

Browse by domain, track, level, and module. Each lesson links directly; challenges link to the module’s challenge set.

- Cybersecurity
  - Foundations (Beginner)
    - Module 00 — Setup & Tools
      - [Lesson 01 — Install Linux and Kali Linux](library/cybersecurity/foundations/beginner/module-00-setup-and-tools/lesson-01-install-linux-and-kali.md)
      - [Lesson 02 — VS Code and GitHub Workflow](library/cybersecurity/foundations/beginner/module-00-setup-and-tools/lesson-02-vscode-and-github-workflow.md)
      - [Challenges](library/cybersecurity/foundations/beginner/module-00-setup-and-tools/challenges/README.md)
    - Module 01 — Introduction
      - [Lesson 01 — What is Cybersecurity?](library/cybersecurity/foundations/beginner/module-01-introduction/lesson-01-what-is-cybersecurity.md)
    - Module 02 — Digital Hygiene
      - [Lesson 01 — Passwords and MFA](library/cybersecurity/foundations/beginner/module-02-digital-hygiene/lesson-01-passwords-and-mfa.md)
      - [Lesson 02 — Software Updates and Backups](library/cybersecurity/foundations/beginner/module-02-digital-hygiene/lesson-02-updates-and-backups.md)
      - [Challenges](library/cybersecurity/foundations/beginner/module-02-digital-hygiene/challenges/README.md)
    - Module 03 — Safe Browsing
      - [Lesson 01 — Phishing Awareness](library/cybersecurity/foundations/beginner/module-03-safe-browsing/lesson-01-phishing-awareness.md)
      - [Lesson 02 — Privacy and Browser Safety](library/cybersecurity/foundations/beginner/module-03-safe-browsing/lesson-02-privacy-and-browser-safety.md)
      - [Challenges](library/cybersecurity/foundations/beginner/module-03-safe-browsing/challenges/README.md)
    - Module 04 — Home Network Security
      - [Lesson 01 — Secure Wi‑Fi and Router Settings](library/cybersecurity/foundations/beginner/module-04-home-network-security/lesson-01-secure-wifi-and-router.md)
      - [Lesson 02 — Basic Network Monitoring at Home](library/cybersecurity/foundations/beginner/module-04-home-network-security/lesson-02-basic-network-monitoring.md)
      - [Challenges](library/cybersecurity/foundations/beginner/module-04-home-network-security/challenges/README.md)
    - Module 05 — Mobile Security
      - [Lesson 01 — Securing Your Phone](library/cybersecurity/foundations/beginner/module-05-mobile-security/lesson-01-securing-your-phone.md)
      - [Lesson 02 — App Hygiene and Permissions](library/cybersecurity/foundations/beginner/module-05-mobile-security/lesson-02-app-hygiene-and-permissions.md)
      - [Challenges](library/cybersecurity/foundations/beginner/module-05-mobile-security/challenges/README.md)
    - Module 06 — Social Engineering Defense
      - [Lesson 01 — Social Engineering Tactics and Red Flags](library/cybersecurity/foundations/beginner/module-06-social-engineering-defense/lesson-01-social-engineering-tactics.md)
      - [Lesson 02 — Verification and Reporting Procedures](library/cybersecurity/foundations/beginner/module-06-social-engineering-defense/lesson-02-verification-and-reporting.md)
      - [Challenges](library/cybersecurity/foundations/beginner/module-06-social-engineering-defense/challenges/README.md)
  - Blue Team (Intermediate)
    - Module 01 — Incident Detection
      - [Lesson 01 — Windows Event Log Triage Basics](library/cybersecurity/blue-team/intermediate/module-01-incident-detection/lesson-01-windows-event-log-triage.md)
      - [Lesson 02 — Intro to Network Threat Hunting](library/cybersecurity/blue-team/intermediate/module-01-incident-detection/lesson-02-intro-network-threat-hunting.md)
      - [Challenges](library/cybersecurity/blue-team/intermediate/module-01-incident-detection/challenges/README.md)
    - Module 02 — Endpoint Triage with Sysmon
      - [Lesson 01 — Sysmon Essentials and Event Mapping](library/cybersecurity/blue-team/intermediate/module-02-endpoint-triage-sysmon/lesson-01-sysmon-essentials.md)
      - [Lesson 02 — Practical Endpoint Triage with Sysmon](library/cybersecurity/blue-team/intermediate/module-02-endpoint-triage-sysmon/lesson-02-practical-triage-with-sysmon.md)
      - [Challenges](library/cybersecurity/blue-team/intermediate/module-02-endpoint-triage-sysmon/challenges/README.md)
    - Module 03 — SIEM Query Basics
      - [Lesson 01 — SIEM Query Fundamentals](library/cybersecurity/blue-team/intermediate/module-03-siem-query-basics/lessons/lesson-01-siem-query-fundamentals.md)
      - [Lesson 02 — From Exploration to Detection](library/cybersecurity/blue-team/intermediate/module-03-siem-query-basics/lessons/lesson-02-from-exploration-to-detection.md)
      - [Challenges](library/cybersecurity/blue-team/intermediate/module-03-siem-query-basics/challenges/README.md)
    - Module 04 — Alert Tuning & False Positive Reduction
      - [Lesson 01 — Alert Tuning Fundamentals](library/cybersecurity/blue-team/intermediate/module-04-alert-tuning-fp-reduction/lessons/lesson-01-alert-tuning-fundamentals.md)
      - [Lesson 02 — Feedback Loops and Rule Lifecycle](library/cybersecurity/blue-team/intermediate/module-04-alert-tuning-fp-reduction/lessons/lesson-02-feedback-loops-and-lifecycle.md)
      - [Challenges](library/cybersecurity/blue-team/intermediate/module-04-alert-tuning-fp-reduction/challenges/README.md)
    - Module 05 — Incident Response Playbooks
      - [Lesson 01 — Playbook Structure and Essentials](library/cybersecurity/blue-team/intermediate/module-05-incident-response-playbooks/lessons/lesson-01-playbook-structure-and-essentials.md)
      - [Lesson 02 — Hands-on: Ransomware and Phishing Response](library/cybersecurity/blue-team/intermediate/module-05-incident-response-playbooks/lessons/lesson-02-hands-on-ransomware-phishing.md)
      - [Challenges](library/cybersecurity/blue-team/intermediate/module-05-incident-response-playbooks/challenges/README.md)
