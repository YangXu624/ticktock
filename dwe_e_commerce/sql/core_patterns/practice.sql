-- SQL Core Patterns
-- Target: 20 minutes. State assumptions before you type.
-- Dialect: PostgreSQL-style SQL.

-- Schema
-- orders(order_id, user_id, seller_id, order_ts, status)
-- order_items(order_id, product_id, quantity, unit_price, discount_amount)
-- users(user_id, region, signup_date)
-- payments(payment_id, order_id, payment_ts, amount, payment_status)

-- Drill 1: Return each region with at least 100 paid orders in January 2026.
-- Include region, distinct order count, unique buyer count, and total paid amount.
-- Keep users with a NULL region under the label 'UNKNOWN'. Prevent fan-out errors.
WITH paid_orders AS (
    -- TODO: one row per paid order
)
SELECT
    -- TODO
;

-- Drill 2: For every seller, calculate gross item value and refunded item value.
-- Include sellers with zero refunded orders. Use quantity * unit_price - discount_amount.
WITH item_values AS (
    -- TODO
)
SELECT
    -- TODO: use conditional aggregation and NULL-safe arithmetic
;

-- Drill 3: Find users who signed up but never placed an order.
SELECT
    -- TODO: solve with an anti-join or NOT EXISTS
;

-- Self-review
-- [ ] I stated the grain of every CTE.
-- [ ] I checked whether joins multiply rows.
-- [ ] I explained COUNT(*), COUNT(column), and COUNT(DISTINCT column).
-- [ ] I tested NULL region, missing payments, duplicate payments, and zero orders.
