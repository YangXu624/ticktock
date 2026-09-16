-- TikTok Shop E-commerce Metrics
-- Complete one file per sitting or copy one prompt into a blank editor.

-- Shared schema
-- orders(order_id, user_id, seller_id, order_ts, paid_amount, region, status)
-- events(event_id, user_id, session_id, event_ts, event_type, product_id)
-- payment_status_log(order_id, status, status_ts, ingestion_ts)

-- 1. Top sellers
-- Find the top 3 sellers by paid GMV per region and calendar month.
-- Decide how ties, cancellations, refunds, and currency would be handled.
WITH eligible_orders AS (
    -- TODO
), seller_monthly_gmv AS (
    -- TODO
), ranked AS (
    -- TODO
)
SELECT -- TODO;

-- 2. Consecutive purchases
-- Return users with purchases on at least 3 consecutive calendar days.
-- Multiple purchases on one day count once. Use a gaps-and-islands approach.
WITH purchase_days AS (
    -- TODO
), grouped_days AS (
    -- TODO: construct a stable island key
)
SELECT -- TODO;

-- 3. Rolling GMV
-- Build a region-by-date spine and calculate trailing 7-calendar-day GMV,
-- including dates with no orders.
WITH date_spine AS (
    -- TODO: assume a calendar table if your dialect lacks generate_series
), daily_gmv AS (
    -- TODO
)
SELECT -- TODO;

-- 4. Latest payment state
-- Deduplicate logs and return one current state per order. Handle late ingestion.
WITH ranked AS (
    -- TODO
)
SELECT -- TODO;

-- 5. Session funnel
-- Return distinct users at impression, click, add_to_cart, purchase, and refund,
-- plus conversion and drop-off rates between stages. Do not allow an earlier
-- timestamped event to satisfy a later stage.
WITH staged_events AS (
    -- TODO
)
SELECT -- TODO;

-- Before finishing, say the grain, metric definition, denominator, time zone,
-- duplicate policy, and late-data policy aloud.
