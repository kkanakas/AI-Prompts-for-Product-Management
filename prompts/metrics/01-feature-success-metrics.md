# Feature Success Metrics

**Phase:** Metrics
**Purpose:** Get tailored metric suggestions for a feature to help define what success looks like before and after launch.

## Prompt Template

```
I am a product manager working on the following feature:

Feature name: [FEATURE_NAME]
Description: [FEATURE_DESCRIPTION]
Target users: [TARGET_USERS]
Primary goal of the feature: [FEATURE_GOAL]

Please suggest success metrics I should consider for this feature. For each metric, include:

1. Metric name — what it is called
2. Type — categorize it (e.g., adoption, engagement, retention, revenue, quality, operational)
3. How to measure it — what data or events need to be tracked
4. Why it matters — how it connects to the feature's goal
5. Potential pitfall — any way this metric could be misleading or gamed

Organize the suggestions from highest to lowest priority. Also flag any counter-metrics I should track to avoid optimizing for the wrong thing.
```

## Placeholders

| Variable | Description |
|---|---|
| `[FEATURE_NAME]` | Short name of the feature (e.g., "Onboarding checklist") |
| `[FEATURE_DESCRIPTION]` | What the feature does and how users interact with it |
| `[TARGET_USERS]` | Who the feature is designed for (e.g., new users, power users, admins) |
| `[FEATURE_GOAL]` | The intended outcome (e.g., increase activation, reduce support tickets, drive upsell) |

## Tips

- If you already have a north star metric in mind, mention it so suggestions can be framed around it.
- Ask for leading indicators (early signals of success) separately from lagging indicators (long-term outcomes) if you need metrics for both a launch dashboard and a quarterly review.
- For features with multiple user roles, ask for metrics per role to avoid aggregation masking per-segment behavior.
