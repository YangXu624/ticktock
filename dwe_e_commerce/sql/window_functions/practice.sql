-- Window Functions
-- Target: 15 minutes per drill. Do not use GROUP BY where row detail must remain.

-- Schema
-- seller_daily_gmv(seller_id, category_id, metric_date, gmv)
-- order_status_log(order_id, status, status_ts, ingestion_ts)

-- Drill 1: Rank sellers by monthly GMV within each category.
-- Return all sellers tied in the top 3. Explain why you chose RANK or DENSE_RANK.
WITH monthly_gmv AS (
    -- TODO: aggregate to category, month, seller
), ranked AS (
    SELECT
        -- TODO,
        -- TODO: ranking window
    FROM monthly_gmv
)
SELECT *
FROM ranked
WHERE -- TODO
;

-- Drill 2: Show daily GMV, prior-day GMV, and a 7-row rolling average per seller.
-- Explain when 7 ROWS is different from seven calendar days.
SELECT
    -- TODO: LAG and AVG OVER
FROM seller_daily_gmv;

-- Drill 3: Keep the latest status for each order.
-- Break status_ts ties with ingestion_ts, then explain how you would make the
-- tie-break deterministic if both timestamps could match.
WITH ranked_status AS (
    SELECT
        -- TODO,
        ROW_NUMBER() OVER (
            PARTITION BY -- TODO
            ORDER BY -- TODO
        ) AS row_num
    FROM order_status_log
)
SELECT -- TODO
FROM ranked_status
WHERE -- TODO
;

-- Self-review: partition keys, ordering keys, frame boundaries, ties, NULL ordering.
