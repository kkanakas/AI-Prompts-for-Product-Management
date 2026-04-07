# Open-Ended Survey Response Analysis

**Phase:** Customer Discovery
**Purpose:** Theme-code hundreds of open-ended survey responses automatically.

## Prompt Template

```
I asked 500 survey respondents: "[QUESTION]"
Their responses are attached (CSV with text responses).

Please:
1. Identify 5-8 major themes in responses
2. For each theme:
   - % of responses (approximate)
   - 3-4 representative quotes
   - Variations within the theme
3. Outlier responses that don't fit themes but seem important
4. If I provide demographic data (role, company size), do certain
   themes correlate with segments?

Be specific with theme names - avoid generic labels like "usability"
unless that's literally what people said.
```

## Placeholders

| Variable | Description |
|---|---|
| `[QUESTION]` | The exact survey question you asked |
