"""Choose partition and clustering keys for analytical workloads."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Workload:
    name: str
    rows_per_day: int
    common_date_range_days: int
    common_filters: tuple[str, ...]
    join_keys: tuple[str, ...]
    late_arrival_days: int


@dataclass(frozen=True)
class StorageStrategy:
    partition_key: str
    partition_granularity: str
    cluster_keys: tuple[str, ...]
    late_data_policy: str
    compaction_policy: str
    rationale: str


PRODUCT_EVENTS = Workload(
    "product_events",
    rows_per_day=20_000_000_000,
    common_date_range_days=7,
    common_filters=("event_date", "seller_id", "product_id", "region"),
    join_keys=("user_id", "product_id", "seller_id"),
    late_arrival_days=3,
)

ORDER_ITEMS = Workload(
    "order_items",
    rows_per_day=300_000_000,
    common_date_range_days=90,
    common_filters=("order_date", "seller_id"),
    join_keys=("order_id", "seller_id"),
    late_arrival_days=7,
)


def choose_storage_strategy(workload: Workload) -> StorageStrategy:
    # TODO: avoid high-cardinality partition keys such as seller_id.
    # TODO: justify pruning, skew, file size, and backfill behavior.
    pass


if __name__ == "__main__":
    for workload in (PRODUCT_EVENTS, ORDER_ITEMS):
        print(choose_storage_strategy(workload))

# After coding, write one pruneable date predicate and one predicate that
# accidentally defeats partition pruning.
