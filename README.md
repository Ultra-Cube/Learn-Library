# Learn-Library

An open, extensible library of bite-sized lessons with explanations, sources, exercises, and puzzles—organized for growth and easy contribution.

- Website: https://www.ucubetech.com
- Organization: https://github.com/company/ultra-cube

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
```
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
```
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
