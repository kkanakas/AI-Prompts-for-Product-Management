# Problem Refinement

**Phase:** Customer Discovery
**Purpose:** Refine your understanding of a problem across different audiences. AI challenges your hypotheses.

## Prompt Template

```
What I believe is true: [DESCRIBE THE PROBLEM AS YOU UNDERSTAND IT]
What I think is the impact: [DESCRIBE THE IMPACT]
How do people address the impact today: [DESCRIBE WHAT YOU UNDERSTAND CURRENT SOLUTIONS ARE]
How big is the problem: [SIZE OF THE PROBLEM]
Who is likely to feel the impact: [CUSTOMER SEGMENTS]
Consequences: [CONSEQUENCES IF PROBLEM IS NOT ADDRESSED]

OUTPUTS:
Give me 5 specific problem statements for 5 different audiences, with a clear
description of the impact on them if the problem is not addressed. Do this
based on data you have available about the problem I described and the different
audiences you identify. Challenge my hypotheses if data suggests otherwise.
```

## Placeholders

| Variable | Description |
|---|---|
| `[DESCRIBE THE PROBLEM AS YOU UNDERSTAND IT]` | Your current understanding — be honest about gaps |
| `[DESCRIBE THE IMPACT]` | What happens because of this problem |
| `[DESCRIBE WHAT YOU UNDERSTAND CURRENT SOLUTIONS ARE]` | How people cope today |
| `[SIZE OF THE PROBLEM]` | How many people affected, $ cost, etc. (say "I don't know" if unsure) |
| `[CUSTOMER SEGMENTS]` | Who feels it most |
| `[CONSEQUENCES IF PROBLEM IS NOT ADDRESSED]` | What gets worse over time |

## Tips

- It's OK to write "I don't know" for any section — the AI can help fill gaps
- Ask the AI to challenge your hypotheses, not just confirm them
- See `examples/problem-refinement-example.md` for a worked example
