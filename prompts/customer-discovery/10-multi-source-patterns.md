# Multi-Source Pattern Finding

**Phase:** Customer Discovery
**Purpose:** Triangulate insights across interviews, surveys, support tickets, and other data.

## Prompt Template

```
I have data from multiple sources about [PRODUCT/PROBLEM]:
Source 1: 20 customer interviews [ATTACH TRANSCRIPTS]
Source 2: 100 survey responses [ATTACH CSV]
Source 3: 500 support tickets [ATTACH]

OUTPUT:
Aggregate and synthesize common themes:
1. What themes appear across ALL sources? (high confidence)
2. What appears in some sources but not others? (why might this be?)
3. Any contradictions between what users say (interviews/surveys)
   vs. what they do (support tickets)?
4. Prioritize top 3-5 issues by:
   - Frequency across sources
   - Intensity (how much users care)
   - Impact on user success
5. What may need more research?

Be explicit about confidence levels for each finding.
```

## Placeholders

| Variable | Description |
|---|---|
| `[PRODUCT/PROBLEM]` | What you're researching |

## Tips

- The more diverse your sources, the stronger the triangulation
- Contradictions between "say" and "do" data are often the most valuable findings
