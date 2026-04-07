# Pre-Mortem Analysis

**Phase:** Idea Evaluation
**Purpose:** Imagine your feature launched and failed — identify risks before you build.

## Prompt Template

```
Feature idea: [description]
Target users: [who it is for]
Problem it solves: [user need]

Conduct a pre-mortem: Assume this feature launched and failed badly.
What went wrong?

OUTPUTS:
Consider any combination of these:
1. Technical failures (scale, performance, edge cases)
2. User adoption issues (why users might not use it)
3. Usability problems (where users get stuck or confused)
4. Business risks (cost, support burden, misalignment with strategy)
5. Unintended consequences (creates new problems)
6. Competitive vulnerabilities (how competitors could counter)

Be pessimistic. Find the flaws.
```

## Placeholders

| Variable | Description |
|---|---|
| `[description]` | What the feature does |
| `[who it is for]` | Target user segment |
| `[user need]` | The problem it addresses |
