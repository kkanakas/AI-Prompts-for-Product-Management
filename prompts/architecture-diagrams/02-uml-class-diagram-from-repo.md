# UML Class Diagram from Git Repository

**Phase:** Architecture Diagram Generation
**Purpose:** Analyze a GitHub repository and generate a UML class diagram that captures the key classes, their attributes, methods, and relationships — giving product managers, architects, and engineers a clear structural view of the codebase without reading every file.

## Prompt Template

```
I have a GitHub repository here: [GITHUB_REPO_URL]

Please analyze the codebase and generate a UML class diagram that captures the structure of the system. 

Focus on:

1. **Core classes and entities** — the primary domain objects, models, or data structures that represent the key concepts in the system (e.g., User, Order, Product, Contract)
2. **Attributes** — the key properties or fields of each class, with data types where visible
3. **Methods** — the most important public methods or behaviours of each class (omit private utility methods to keep the diagram readable)
4. **Relationships** — the connections between classes:
   - Inheritance (is-a): a class extends or implements another
   - Composition (has-a, strong): a class owns another and the child cannot exist without the parent
   - Aggregation (has-a, weak): a class contains another but the child can exist independently
   - Association: a class references or uses another
   - Dependency: a class depends on another transiently (e.g., as a method parameter)
5. **Interfaces and abstract classes** — any contracts or base types that define shared behaviour
6. **Multiplicity** — where visible, indicate relationship cardinality (1, 0..1, 1..*, 0..*)

Scope: [SCOPE — e.g., "the entire codebase", "the `/src/models` directory", "the authentication and user management modules", "the domain layer only"]

Output format: Generate the diagram in **Mermaid `classDiagram` syntax**. After the diagram, provide:

1. **Structural summary** — 3–5 sentences describing the overall architecture pattern visible in the class structure (e.g., layered, domain-driven, MVC)
2. **Key design decisions** — 2–3 observations about notable design choices (e.g., heavy use of interfaces, God classes, tight coupling between modules)
3. **Complexity hotspots** — any classes with an unusually high number of relationships or methods that may indicate technical debt or refactoring candidates
4. **Assumptions** — any inferences you made due to incomplete visibility (e.g., inferred relationships from method signatures, omitted classes for readability)
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[GITHUB_REPO_URL]` | Full URL to the GitHub repository | `https://github.com/owner/repo` |
| `[SCOPE]` | Which part of the repo to analyse | `"the /src/domain directory"`, `"the entire codebase"`, `"the payment and billing modules"` |

## Output Variants

Depending on your goal, ask for a different focus after the main prompt:

**Domain model only** — add to the prompt:
```
Focus only on domain entities and their relationships. Exclude infrastructure, controller, and utility classes. The goal is a clean domain model suitable for a business stakeholder review.
```

**Inheritance hierarchy only** — add to the prompt:
```
Focus only on inheritance and interface implementation relationships. Show all abstract classes and interfaces prominently. Omit attributes and methods to keep the diagram clean.
```

**Dependency map for a specific feature** — add to the prompt:
```
Focus on the classes involved in [FEATURE NAME — e.g., "user authentication"]. Trace all dependencies from the entry point through to the data layer and show every class touched by this feature.
```

## Tips

- **Scope is critical for large repos** — a full-codebase class diagram for a large project will be unreadable; always specify a module, layer, or feature area unless the repo is small
- **Mermaid class diagrams render in GitHub** — paste the output directly into a `.md` file in the repo and it renders natively in GitHub, Notion, and most documentation tools
- **Use the complexity hotspots output for PRD context** — classes with many relationships often correspond to the parts of the system where new features are most expensive to build; include this in your technical feasibility assessment
- **Re-run after major refactors** — class diagrams decay quickly; treat them as a snapshot, not a permanent document
- **Combine with the sequence diagram prompt** — a class diagram shows structure; a sequence diagram shows behaviour; together they give a complete architectural picture

## Rendering

Paste the Mermaid output into any of these tools to render it:

- [Mermaid Live Editor](https://mermaid.live) — instant browser rendering, shareable link
- GitHub Markdown — Mermaid renders natively in `.md` files
- Notion — paste as a code block with `mermaid` language tag
- VS Code — install the Markdown Preview Mermaid Support extension
