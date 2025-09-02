# Step B Module Naming Consolidation Plan

Objective: Consolidate duplicate introductory module directories (e.g., `module-01-introduction` vs `module-01-<domain>-fundamentals`) into a single canonical `module-01-<domain>-fundamentals` structure across all foundations beginner tracks. Preserve rich lesson content; remove shallow/duplicate variants; update all internal links.

## Affected Domains & Current State

| Domain | Canonical Target Folder | Duplicate Folder(s) | Primary Lesson File (Rich) | Secondary (Shallow) |
|--------|-------------------------|---------------------|----------------------------|---------------------|
| Cloud Computing | module-01-cloud-fundamentals (DONE) | module-01-introduction (minimal redirect stub in place) | lesson-01-cloud-computing-fundamentals.md (canonical) | (legacy stub only) |
| Cybersecurity | module-01-introduction (rename to module-01-cybersecurity-fundamentals) | N/A (only intro naming) | lesson-01-cybersecurity-fundamentals.md | — |
| Data Science | module-01-data-science-fundamentals (DONE) | module-01-introduction (stub) | lesson-01-introduction-to-data-science.md (canonical) | (legacy stub only) |
| Digital Marketing | module-01-digital-marketing-fundamentals | module-01-introduction | lesson-01-introduction-to-digital-marketing.md | lesson-01-digital-marketing-fundamentals.md |
| IT Infrastructure | module-01-infrastructure-fundamentals | module-01-introduction | lesson-01-introduction-to-it-infrastructure.md | lesson-01-it-infrastructure-fundamentals.md |
| Software Development | module-01-programming-fundamentals | module-01-introduction | lesson-01-software-development-fundamentals.md | (module README) |

## Consolidation Rules

1. Keep the richer, more comprehensive lesson file; migrate its front matter if needed to the canonical folder.
2. If both rich and shallow versions exist, retain richer naming: prefer `introduction-to-<topic>` naming as Lesson 01; add redirect stub in removed path if required (future enhancement).
3. Standardize module README to new template with Objectives, Visual, Summary (already applied to many; ensure after moves).
4. Update all references in:
   - Root `README.md`
   - `PLATFORM_TRANSFORMATION_SUMMARY.md`
   - Any quiz or assessment metadata referencing old folder names.
5. Remove obsolete duplicate directories after migration.

## Execution Order (Minimize Broken Links Window)

1. Cloud: Merge `module-01-introduction` into `module-01-cloud-fundamentals` (Completed: migration, cleanup, canonical formatting, legacy replaced with minimal stub).
2. Data Science: Merge intro into fundamentals similarly.
3. Digital Marketing: Merge intro into fundamentals.
4. IT Infrastructure: Merge intro into infrastructure-fundamentals.
5. Software Development: Move rich lesson into `module-01-programming-fundamentals` as `lesson-01-software-development-fundamentals.md`.
6. Cybersecurity: Rename folder `module-01-introduction` to `module-01-cybersecurity-fundamentals` (consistent pattern) and adjust links.
7. Global link updates and search/replace checks.

## Link Patterns To Update (Regex Examples)

```text
library/(.+?)/foundations/beginner/module-01-introduction/lesson-01-(.*?)-fundamentals.md
→ library/$1/foundations/beginner/module-01-$2-fundamentals/lesson-01-introduction-to-$2.md
```

Will perform targeted replacements rather than blanket regex to avoid accidental matches.

## Post-Migration Validation

- Grep for `module-01-introduction` should return zero references (except in change log if added).
- Run existing validation script (if any) to ensure no broken relative links (future automation).
- Update CHANGELOG with consolidation note.

## Deferred (Future Enhancements)

- Add redirect stub Markdown files with notice of relocation.
- Introduce automated link validation workflow.

---

Status Update (2025-09-02): Cloud domain consolidation complete; canonical lesson formatted (tabs removed). Minimal stub retained only for link hygiene pending audit; scheduled for full removal after confirmation of zero inbound references.

Status Update (2025-09-02 #2): Data Science domain consolidation executed. Legacy `module-01-introduction/lesson-01-data-science-fundamentals.md` replaced with redirect stub to `module-01-data-science-fundamentals/lesson-01-introduction-to-data-science.md`. Refactor plan updated accordingly.
