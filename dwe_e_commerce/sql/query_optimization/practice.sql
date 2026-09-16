-- Analytical SQL optimization drills
-- For each case, rewrite the query and annotate how the change reduces scanned
-- data, shuffle volume, or intermediate rows. Preserve result correctness.

-- Case 1: partition pruning
-- fact_order_item is partitioned by order_date. The original filter applies a
-- function to order_ts and scans 4 TB.
SELECT seller_id, SUM(item_amount) AS gmv
FROM fact_order_item
WHERE DATE(order_ts) = DATE '2026-09-01'  -- TODO: replace with pruneable predicate
GROUP BY seller_id;

-- Diagnosis:
-- Rewritten predicate:
-- Execution-plan evidence to inspect:

-- Case 2: fan-out and early aggregation
-- Both sources have many rows per user, so joining raw rows inflates GMV.
WITH raw_clicks AS (
    SELECT user_id, campaign_id, click_ts
    FROM click_events
),
raw_items AS (
    SELECT o.user_id, i.order_id, i.quantity * i.unit_price AS gmv
    FROM orders AS o
    JOIN order_items AS i ON i.order_id = o.order_id
),
unsafe_join AS (
    SELECT c.campaign_id, i.gmv
    FROM raw_clicks AS c
    JOIN raw_items AS i ON i.user_id = c.user_id
)
SELECT campaign_id, SUM(gmv)
FROM unsafe_join
GROUP BY campaign_id;

-- TODO: rewrite with an explicit attribution rule and safe pre-join grains.
-- Required output grain:
-- Event-side grain before join:
-- Order-side grain before join:
-- Join keys and time condition:

-- Case 3: skewed join
-- Forty percent of events have seller_id = 0. Write one version that separates
-- the hot key and one that uses salting. State the correctness risks.
WITH regular_keys AS (
    -- TODO
),
hot_key AS (
    -- TODO
)
SELECT -- TODO
;

-- Self-review:
-- [ ] Partition pruning and column projection
-- [ ] Early filtering and safe pre-aggregation
-- [ ] Join strategy and shuffle reduction
-- [ ] Skew handling without changing results
