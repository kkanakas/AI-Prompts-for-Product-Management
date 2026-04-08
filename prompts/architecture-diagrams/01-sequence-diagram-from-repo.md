# Sequence Diagram from Git Repository

**Phase:** Architecture Diagram Generation
**Purpose:** Analyze a Git repository and generate a Mermaid sequence diagram that captures the key interactions and flows within the codebase.

## Prompt Template

```
I have a Git repository here: [GIT_REPO_URL]

Please analyze the codebase and generate a Mermaid sequence diagram that captures the primary interactions in this system. Focus on:

1. Entry points — how requests or events enter the system (e.g., API routes, CLI commands, event listeners)
2. Key actors — the main services, modules, classes, or components involved
3. Core flows — the most important end-to-end interactions (e.g., a user action from request to response)
4. Data movement — how data is passed between components, including any database, queue, or external service calls
5. Error or branching paths — any notable alternative flows or failure handling

Output the diagram in Mermaid syntax using `sequenceDiagram`. After the diagram, provide a short plain-English summary of the flow you modeled and any assumptions you made due to incomplete visibility into the repo.
```

## Placeholders

| Variable | Description |
|---|---|
| `[GIT_REPO_URL]` | Full URL to the Git repository (e.g., `https://github.com/owner/repo`) |

## Tips

- If the repo is large, specify a subfolder or a specific feature area to focus on (e.g., "focus on the `/src/auth` module").
- You can ask for multiple diagrams for different flows (e.g., authentication flow, payment flow, data ingestion pipeline).
- To render the output, paste the Mermaid block into [Mermaid Live Editor](https://mermaid.live) or any Markdown viewer that supports Mermaid.
