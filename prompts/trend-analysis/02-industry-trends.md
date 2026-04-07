# Industry & Market Trend Identification

**Phase:** Trend Analysis
**Purpose:** Process analyst reports, news, and financial filings to identify emerging market trends.

## Prompt Template

```
Analyze these industry sources for [CATEGORY]:
- 5 analyst reports (Gartner, Forrester, etc.) [ATTACH]
- 10 recent news articles [ATTACH]
- 10-K Annual Financial Reports [ATTACH]
- Vendor announcements [ATTACH]

Identify:
1. Emerging trends mentioned across multiple sources
2. Technologies gaining traction (mentioned increasingly)
3. Use cases or applications growing in prominence
4. Buyer priorities shifting (what matters now vs. 1-2 years ago)
5. Predictions analysts are making about the market

For each trend:
- Evidence (which sources, how often mentioned)
- Maturity (emerging, growing, or mainstream)
```

## Placeholders

| Variable | Description |
|---|---|
| `[CATEGORY]` | Your industry or product category |

## Limitations to Keep in Mind

- **Confirmation bias** — AI will find trends you ask it to look for; stay open to surprises
- **Recency bias** — A spike in mentions may be temporary noise, not a sustained trend
- **Public data only** — Stealth competitors and proprietary research won't appear
- **No causation** — AI spots correlations, not causes
