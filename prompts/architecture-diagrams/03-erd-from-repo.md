# Entity Relationship Diagram from Git Repository

**Phase:** Architecture Diagram Generation
**Purpose:** Analyze a GitHub repository and generate an Entity Relationship Diagram (ERD) that captures the data model — entities, attributes, primary and foreign keys, and relationships — giving product managers, architects, and engineers a clear picture of how data is structured and connected without reading every schema file.

## Prompt Template

```
I have a GitHub repository here: [GITHUB_REPO_URL]

Please analyze the codebase and generate an Entity Relationship Diagram (ERD) that captures the data model of the system.

Focus on:

1. **Entities** — the core tables, models, or domain objects that store persistent data (e.g., User, Order, Product, Invoice)
2. **Attributes** — the key fields or columns for each entity, including data types where visible (e.g., id: INT, email: VARCHAR, created_at: TIMESTAMP)
3. **Primary keys** — identify the unique identifier for each entity (PK)
4. **Foreign keys** — identify fields that reference another entity (FK), making relationships explicit
5. **Relationships and cardinality** — the connections between entities with multiplicity:
   - One-to-one (1:1): each record in A relates to exactly one record in B
   - One-to-many (1:N): one record in A relates to many records in B
   - Many-to-many (M:N): many records in A relate to many records in B (often via a junction table)
   - Optional vs. mandatory participation (||, |o, }|, }o notation)
6. **Junction / associative tables** — intermediate tables that resolve many-to-many relationships (e.g., OrderItems, UserRoles)
7. **Enumerations and lookup tables** — reference tables or enum types that constrain field values

Scope: [SCOPE — e.g., "the entire database schema", "the /db/migrations directory", "the user management and billing domain", "the core domain entities only"]

Output format: Generate the diagram in **Mermaid `erDiagram` syntax**. After the diagram, provide:

1. **Data model summary** — 3–5 sentences describing the overall structure, the central aggregate or root entity, and how the major domains relate to each other
2. **Key design observations** — 2–3 observations about notable design choices (e.g., use of soft deletes, polymorphic associations, denormalization for performance, absence of referential integrity constraints)
3. **Data integrity risks** — any missing constraints, nullable foreign keys, or structural patterns that could lead to orphaned records, duplicates, or inconsistent state
4. **Scalability considerations** — entities or relationships that may become bottlenecks at scale (e.g., high-write junction tables, wide tables with many nullable columns)
5. **Assumptions** — any inferences you made due to incomplete visibility (e.g., relationships inferred from naming conventions, omitted lookup tables for readability)
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[GITHUB_REPO_URL]` | Full URL to the GitHub repository | `https://github.com/owner/repo` |
| `[SCOPE]` | Which part of the repo or schema to analyse | `"the /db/schema.sql file"`, `"the entire codebase"`, `"the order management domain"` |

## Output Variants

Depending on your goal, add one of these instructions after the main prompt:

**Core domain entities only** — add to the prompt:
```
Focus only on the primary business entities and their direct relationships. Exclude audit tables, session tables, configuration tables, and migration history. The goal is a clean domain model suitable for a business stakeholder or architect review.
```

**Full schema including system tables** — add to the prompt:
```
Include all tables in the schema, including audit logs, session management, feature flags, and migration tracking tables. Show every foreign key relationship. The goal is a complete technical reference.
```

**Data flow for a specific feature** — add to the prompt:
```
Focus on the entities involved in [FEATURE NAME — e.g., "the checkout and payment flow"]. Trace all tables touched from the moment a user initiates the action through to the final persisted state. Show every join table and foreign key in this path.
```

**Read model / reporting view** — add to the prompt:
```
Identify the entities and joins required to support a reporting or analytics use case for [REPORTING GOAL — e.g., "monthly revenue by customer segment"]. Show denormalization opportunities and which joins are expensive.
```

## Tips

- **Scope is essential for large schemas** — a full ERD for a 100-table database is unreadable; always specify a domain, module, or feature unless the schema is small
- **Migration files are the most reliable source** — ask the model to look at `/db/migrations` or `/prisma/schema.prisma` rather than inferring from application code; explicit schema files produce far more accurate ERDs than ORM model inference
- **Use for PRD technical feasibility sections** — the data integrity risks and scalability considerations outputs feed directly into the technical feasibility section of a PRD; include them verbatim
- **Pair with the UML class diagram prompt** — the ERD shows your persistence layer; the class diagram shows your domain objects; run both to see how well your data model maps to your domain model
- **Re-run after schema migrations** — ERDs decay quickly as the schema evolves; treat the output as a snapshot tied to a specific commit or migration version, not a permanent document
- **Junction tables reveal hidden complexity** — a many-to-many relationship that looks simple in a class diagram often hides business rules in its junction table (e.g., `OrderItems` carries price, quantity, discount); always inspect these carefully

## Rendering

Paste the Mermaid output into any of these tools to render it:

- [Mermaid Live Editor](https://mermaid.live) — instant browser rendering, shareable link
- GitHub Markdown — Mermaid renders natively in `.md` files
- Notion — paste as a code block with `mermaid` language tag
- VS Code — install the Markdown Preview Mermaid Support extension
- dbdiagram.io — alternative ERD tool if you prefer DBML syntax
