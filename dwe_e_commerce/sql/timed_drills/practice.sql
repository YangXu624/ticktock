-- Two 15-minute SQL drills
-- Use a timer. Spend 2 minutes clarifying, 10 minutes coding, 3 minutes testing.

-- Drill A: Repeat buyers
-- orders(order_id, user_id, order_ts, status, amount)
-- Return each month and the percentage of that month's buyers who also made a
-- paid purchase in the immediately preceding calendar month.
-- Requirements: one row per month; deduplicate users; NULL percentage if the
-- month has no buyers; explain whether missing months appear.
WITH monthly_buyers AS (
    -- TODO
), retained AS (
    -- TODO
)
SELECT -- TODO;

-- Drill B: Product price history
-- product_price_log(product_id, price, effective_ts, ingestion_ts)
-- order_items(order_id, product_id, order_ts, quantity)
-- Attach the price effective at order_ts to every order item, then calculate
-- order value. Late-arriving price records may share effective_ts; the latest
-- ingestion_ts wins.
WITH deduped_prices AS (
    -- TODO
), matched AS (
    -- TODO: consider a range join or ranking candidate matches
)
SELECT -- TODO;

-- Verbal close-out
-- Complexity / expensive operations:
-- Edge cases tested:
-- One alternative approach:
