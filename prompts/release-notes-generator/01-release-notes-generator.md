# Release Notes Generator

**Phase:** Development
**Purpose:** Communicating Updates in a non-technical language for customers using the git history and ticket information written in product voice.

## Expected Inputs

- Version number or tag (e.g. 2.5.0 or git tag)
- Date range (e.g.,"commits since last release" or "January 1-31,2026")
- Optional Jira filter or tickets list for additional context

## Process

1. Read git commits in the specified range
2. Identity user-facing changes (filter out internal refactoring, depenendency updates)
3. Categorize changes:
    - **Added**: New features or capabilities
    - **Changed**: Improvements to existing features
    - **Fixed**: Bug Fixes
    - **Removed**: Deprecated or removed feature

4. Write descriptions in product language (not technical jargon)
5. Group related changes together
6. Order by user impact (most impactful first)

## Output

Generate `CHANGELOG.md` entry or `docs/releases/[version].md`

```

## [Version X.Y.Z] - YYYY-MM-DD

### Added

- [Feature descritopn in user terms]

### Changed

- [Improvement description]

### Fixed

- [Bug fix in plain language]

### Removed

- [Deprecated feature with migration guidance if needed]

```

## Voice and Tone 

- **Customer-facing, not technical**: "Bulk user import now supports up to 1,000 users" not "Increased MAX_IMPORT_SIZE constant" 

- **Benefit-Oriented**: Explain what the user can now do, not just what changed

-**Clear and concise**: One sentence per change typically

- **Active Voice**: "Added dashboard customization" not "Dashboard customization has been added"

## Quality Criteria

- Only include changes that affect user experience

- Each change must be understandable without reading commit messages 

- Related changes should be grouped together, not listed separately

- Version number and date should be accurate

## Common Patterns

- Internal refactoring -> exclude unless it affects performance 

- Dependency updates -> exclude unless they add user-facing capability

- Bug fixes in unreleased features -> exclude (not relevant to customers)

- Breaking Changes -> call out explicitly with migration guidance

