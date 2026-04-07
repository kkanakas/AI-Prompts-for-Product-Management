# Research Synthesis & Insight Generation

**Phase:** Customer Discovery
**Purpose:** Synthesize interview transcripts into themes, Job Stories, and key insights.

## Prompt Template

```
Synthesize the interviews I conducted, identify common themes and patterns,
and generate a list of insights.

INPUT:
- Problem statement: [DESCRIBE THE PROBLEM]
- Description of the users: [WHO DID YOU INTERVIEW?]
- Responses from the interviews: [PROVIDE TRANSCRIPT OF EACH INTERVIEW]

OUTPUT:
Identify the following:
- Common themes/patterns: Are there any common themes/patterns that emerged
  from the interviews?
- Rephrase the problems/frustrations/needs of the users based on what they said
- Create a list of 3-5 Job Stories using the Job-to-be-done statement:
  "When I am (situation), I want to (motivation), so I can (desired outcome)."
- Create a list of 5-7 key insights from the interviews that were new,
  unexpected, surprising. Use the following format:
  "We heard... I wonder if that means..."
```

## Placeholders

| Variable | Description | Example |
|---|---|---|
| `[DESCRIBE THE PROBLEM]` | Your problem statement | "Remote workers struggle to form meaningful professional relationships" |
| `[WHO DID YOU INTERVIEW?]` | User descriptions | "15 fully-remote startup employees, mix of engineers and designers, 2-8 years experience" |
| `[PROVIDE TRANSCRIPT OF EACH INTERVIEW]` | Raw transcripts | Attach as files or paste inline |

## Tips

- Provide full transcripts, not just summaries — the AI needs raw data to find patterns
- The "We heard... I wonder if that means..." format forces actionable interpretation
