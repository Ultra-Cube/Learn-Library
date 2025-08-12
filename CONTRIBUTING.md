# Contributing to Learn-Library

Thanks for helping grow the library! Follow these guidelines to keep quality high and structure consistent.

## Quick start

1. Pick a domain/track/level/module or create a new one following the structure below.
2. Copy `templates/lesson-template.md` into the target folder and rename it.
3. Fill in the frontmatter and content; include at least two exercises and one puzzle.
4. Add sources from reputable organizations (NIST, CISA, OWASP, ISO, academic papers, vendor docs when needed).
5. Run `python3 scripts/validate_lessons.py` and fix any issues.
6. Open a PR with a descriptive title and summary.

## Content structure

```text
library/<domain>/<track>/<level>/<module-id>-<module-name>/
  lesson-XX-<slug>.md
  solutions/
    lesson-XX-<slug>.md
```

- `domain`: e.g., `cybersecurity`, `programming`, `data-science`
- `track`: e.g., `foundations`, `blue-team`, `web`
- `level`: `beginner`, `intermediate`, `advanced`
- `module-id`: `module-01`, `module-02`, ...
- `lesson-XX`: lesson order inside a module

## Writing guidelines

- Keep lessons concise (15–45 minutes). Use headings, bullets, and examples.
- Start with learning objectives and key terms.
- Prefer vendor-neutral explanations; cite standards and well-known bodies.
- Include at least one hands-on activity when applicable.
- Ensure puzzles are solvable with information in the lesson or sources.
- Add a matching solutions file in `solutions/`.

## Style

- English, clear and simple. Spell out acronyms on first use.
- Code blocks use fenced triple backticks and specify language when possible.
- Link titles should be descriptive (not just "here").

## Metadata

Frontmatter fields are required: `id, title, domain, track, level, module, duration, prerequisites, tags, sources`.

- `id` must be unique. Use pattern: `<DOM>-<TRK>-<LVL>-NNN` (e.g., `CYB-FND-BEG-001`).
- `duration` uses m/h (e.g., `30m`, `1h`).

## Licensing

- Original content: CC BY 4.0
- Do not copy full text from sources. Quote minimally and attribute.

## Review checklist

- [ ] Frontmatter complete and valid
- [ ] Clear learning objectives
- [ ] >= 2 exercises + 1 puzzle
- [ ] Accurate, reputable sources
- [ ] Solutions provided
- [ ] Lint: `scripts/validate_lessons.py` passes
