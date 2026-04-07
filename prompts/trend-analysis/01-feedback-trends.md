# Customer Feedback Trend Monitoring

**Phase:** Trend Analysis
**Purpose:** Track how customer sentiment and feature requests evolve over time.

## Prompt Template

```
I have 12 months of customer reviews/feedback for [PRODUCT]:
- Reviews tagged by month [ATTACH]
- Support tickets categorized by theme [ATTACH]

Analyze changes over time:
1. What themes are increasing in mentions (last 3 months vs. 6-12 months ago)?
2. What complaints are growing vs. declining?
3. New use cases or user types appearing in recent feedback?
4. Sentiment trend: improving or declining? Why?
5. Feature requests that didn't exist 6 months ago?

Focus on changes/trends, not current state.
```

## Placeholders

| Variable | Description |
|---|---|
| `[PRODUCT]` | Your product name or category |

## Tips

- Tag your data with dates before uploading — the AI needs temporal markers to spot trends
- Run this quarterly to catch shifts early
