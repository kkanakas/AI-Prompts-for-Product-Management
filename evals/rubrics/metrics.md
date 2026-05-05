# Metrics Category Bonus Checks

Score the following bonus dimension for prompts in the `metrics` category. Set `is_bonus: true`.

### Metric Row Completeness (1–5)
Every metric row in the output template includes: metric name, measurement method, target value, and baseline. No row has a metric with a target but no baseline.

- 5: All rows have metric name, measurement method, target, and baseline
- 3: Most rows complete; 1–2 rows missing measurement method or baseline
- 1: Majority of rows lack measurement method or baseline values
