# RICE Scoring & Idea Prioritization

**Phase:** Idea Evaluation
**Purpose:** Score and rank ideas using RICE or simplified Impact/Feasibility/Fit/Confidence scoring.

## Prompt Template — RICE

```
[Given the attached list of ideas and descriptions]
For each idea, estimate using the RICE framework and sort results based on
total score. Explain reasoning.
```

## Prompt Template — Simplified Scoring (Recommended for AI-Generated Ideas)

```
Score each idea on these 4 dimensions (1-5 scale):

| Dimension      | What You're Evaluating                                               |
|----------------|----------------------------------------------------------------------|
| Impact         | Combined user value + business value. Will this move important metrics? |
| Feasibility    | Effort, technical complexity, dependencies. Can we properly build this? |
| Strategic Fit  | Alignment with company vision, roadmap themes, core competencies       |
| Confidence     | How validated is this? Do we have data supporting problem-solution fit? |

Scoring guide:
- 1-2: Low (questionable value, very hard, misaligned, or highly speculative)
- 3: Medium (moderate on this dimension)
- 4-5: High (strong value, feasible, aligned, or well-validated)

Sort by total score. Explain reasoning for each score.
```

## Expanded Scoring (Top 5-10 Ideas)

For your highest-scoring ideas, add these criteria:

```
For each of the top ideas, also evaluate:
- Problem-Solution Fit: How well does this address the underlying problem?
- Data Availability: Do we have the right data/model to support it?
- Market Timing: Is now the right time? Are users/market ready?
- Competitive Positioning: Does this strengthen our moat or create vulnerability?
- Dependencies: What needs to happen first? From whom do we need buy-in?
- Risk Assessment: What could go wrong? What's the downside if we're wrong?
```

## Tips for AI-Generated Ideas

- Set Confidence to "low" (< 50%) for unvalidated AI ideas
- AI often underestimates Effort — add buffer or get engineering input
- Use AI's Reach estimate as a starting point, then apply your product intuition
