# Survey Segment Comparison

**Phase:** Customer Discovery
**Purpose:** Compare survey responses between two user segments to surface divergent needs.

## Prompt Template

```
I have survey responses from two user segments:
- Segment A: [DESCRIPTION]
- Segment B: [DESCRIPTION]

Same questions asked to both. Responses attached.
[ATTACH SURVEY RESPONSES]

Compare:
1. What themes appear in both segments vs. unique to each?
2. Same themes mentioned differently? (different language, intensity, context)
3. Different priorities? (what A cares most about vs. B)
4. Contradictory needs? (what A wants vs. what B wants)
5. Based on this, should we build one product or two?

Provide evidence for each finding.
```

## Placeholders

| Variable | Description |
|---|---|
| `[DESCRIPTION]` (Segment A) | Who these users are (role, company size, etc.) |
| `[DESCRIPTION]` (Segment B) | Who these users are |
