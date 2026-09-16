# Technical practice folders

Organized by topic to match [the five-day roadmap](5_day_roadmap.md). Use these folders for your own SQL, Python solutions, schema designs, debugging notes, and technical case write-ups.

```text
sql/
  core_patterns/                 # JOIN, GROUP BY/HAVING, CASE, NULLs
  window_functions/              # Ranking, LAG/LEAD, running aggregates
  ecommerce_metrics/             # Top sellers, retention, rolling GMV, dedup, funnel
  query_optimization/            # Pruning, joins, pre-aggregation, shuffles
  timed_drills/                  # Day 2's two timed SQL problems
leetcode/
  arrays_hashmaps/               # Two Sum, 3Sum, Subarray Sum, Group Anagrams
  sliding_window/                # Sliding windows and two pointers
  prefix_sums/                   # Range sums, subarray sums, product except self
  trees_traversal/               # Trees, BFS/DFS, LCA, Number of Islands
  heaps_top_k/                   # Top K Frequent Elements
data_warehousing/
  dimensional_modeling/          # Grain, OLTP/OLAP, star/snowflake, Shop schema
  slowly_changing_dimensions/    # SCD Type 1/2 and historical lookups
  partitioning/                  # Date partitions and user/seller clustering
ecommerce_analytics/
  metrics_and_attribution/       # GMV definitions, order states, channel attribution
  incident_triage/               # Investigate the 15% seller-performance drop
pipeline_reliability/
  idempotency/                   # Safe reruns, deduplication, reconciliation
  late_data_and_schema_drift/    # Late events, backfills, evolving schemas
  batch_vs_streaming/            # Ingestion, latency, scale, architecture trade-offs
spark/                          # Driver/executors, shuffles, skew, salting, joins
kafka/                          # Topics, partitions, consumers, offsets, lag
networks/                       # TCP/UDP, HTTP/HTTPS, DNS, throughput, API retries
time_series_data_quality/       # Preprocessing, windowing, imbalance, leakage
technical_mocks/                # Timed SQL/DSA, warehouse cases, reliability Q&A
```

| Roadmap day | Practice folders |
| --- | --- |
| Day 1 | `sql/core_patterns`, `sql/window_functions`, `sql/ecommerce_metrics`, `sql/query_optimization` |
| Day 2 | `leetcode/*`, `sql/timed_drills` |
| Day 3 | `data_warehousing/*`, `ecommerce_analytics/*`, `pipeline_reliability/idempotency` |
| Day 4 | `spark`, `kafka`, `pipeline_reliability/*`, `networks` |
| Day 5 | `time_series_data_quality`, `technical_mocks` |

For Day 1's e-commerce drills, use separate `.sql` files for top-N sellers, consecutive purchases, rolling seven-day GMV, payment-state deduplication, and the conversion funnel.

For Day 5, use `time_series_data_quality` for technical experiments with preprocessing and validation. Keep self-introductions, resume explanations, project pitches, STAR stories, and career motivation in your existing notes.

Each folder now contains a practice file with prompts, starter templates, and a self-review checklist. The SQL and Python starters are deliberately incomplete: type the solution yourself, then explain it aloud and test edge cases. No solutions are provided; follow the roadmap's no-AI rule during timed coding practice.
