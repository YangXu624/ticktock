-- Copy a slow query here and annotate each change.
-- Output grain:
-- Largest input:
-- Partition filter:
-- Expected join strategy:
-- Expected reduction in scanned/shuffled data:

WITH filtered_source AS (
    -- TODO: project only required columns and filter partitions early
), aggregated_source AS (
    -- TODO: aggregate to the required pre-join grain when safe
)
SELECT
    -- TODO
;
