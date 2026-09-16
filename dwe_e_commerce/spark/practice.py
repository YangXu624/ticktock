"""Spark diagnosis and DataFrame transformation templates.

The functions accept Spark-like DataFrames, so this file parses without requiring
PySpark locally. Fill them while describing stage boundaries and shuffle costs.
"""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class StageMetrics:
    task_count: int
    median_task_seconds: float
    max_task_seconds: float
    max_input_gb: float
    shuffle_read_gb: float
    spill_gb: float
    gc_seconds: float


def diagnose_stage(metrics: StageMetrics) -> list[str]:
    """Return evidence-based diagnoses, not generic optimization advice."""
    # TODO: detect skew, excessive shuffle/spill, GC pressure, and low parallelism.
    pass


def broadcast_dimension_join(events_df: Any, region_df: Any) -> Any:
    """Join a 3 TB event table to a 2 MB region dimension."""
    # from pyspark.sql.functions import broadcast
    # TODO: return events_df.join(broadcast(region_df), "region_id")
    pass


def salted_join(events_df: Any, orders_df: Any, salt_buckets: int = 16) -> Any:
    """Handle a hot join key while preserving correctness."""
    # TODO: salt the large side and replicate only the matching small-side keys.
    # TODO: remove helper columns and prove no rows were lost or multiplied.
    pass


SKEWED_STAGE = StageMetrics(400, 180, 2700, 600, 900, 500, 300)

if __name__ == "__main__":
    print(diagnose_stage(SKEWED_STAGE))

# Also practice: repartition vs coalesce, compaction of 20,000 tiny files, and
# Spark UI checks for task distribution, shuffle, spill, GC, and executor loss.
