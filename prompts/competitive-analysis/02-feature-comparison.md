# Feature Comparison & Prioritization Signals

**Phase:** Competitive Analysis
**Purpose:** Build a feature matrix identifying table stakes, expected features, and potential differentiators.

## Prompt Template

```
My product is [DESCRIPTION OR CATEGORY]. This is my website [URL].
I am analyzing my feature positioning against the competition. Here is a list of competitors:
Competitor 1: [WEBSITE]
Competitor 2: [WEBSITE]
Competitor 3: [WEBSITE]

Create:
1. Feature comparison matrix (which features each competitor has)
2. Identify features that are:
   - Universal (everyone has them) → table stakes
   - Common (most have them) → expected
   - Rare (1-2 have them) → potential differentiators
3. What features exist that we do not support?
4. What features do we have that our competitors don't?

Focus on functional capabilities, not just marketing claims.
```

## Placeholders

| Variable | Description |
|---|---|
| `[DESCRIPTION OR CATEGORY]` | What your product does |
| `[URL]` | Your product's website |
| `[WEBSITE]` | Each competitor's website URL |
