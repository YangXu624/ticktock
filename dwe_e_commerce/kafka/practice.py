"""Kafka partitioning, consumer lag, and idempotent processing drills."""

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class OrderEvent:
    event_id: str
    order_id: str
    event_type: str
    payload: bytes


@dataclass(frozen=True)
class ConsumerMetrics:
    producer_records_per_second: float
    consumer_records_per_second: float
    lag_by_partition: dict[int, int]
    rebalance_count: int
    processing_error_rate: float


class IdempotentSink(Protocol):
    def contains(self, event_id: str) -> bool: ...
    def write(self, event: OrderEvent) -> None: ...


def partition_key(event: OrderEvent) -> bytes:
    """Preserve ordering for all events belonging to one order."""
    # TODO
    pass


def diagnose_lag(metrics: ConsumerMetrics) -> list[str]:
    """Rank likely causes using the supplied evidence."""
    # TODO: distinguish excess production, slow processing, hot partitions,
    # rebalances, errors, and a slow downstream dependency.
    pass


def process_at_least_once(event: OrderEvent, sink: IdempotentSink) -> None:
    """Make a redelivered Kafka event safe before committing its offset."""
    # TODO: deduplicate by event_id and write before the caller commits offset.
    pass


# Explain aloud:
# - why consumers beyond the partition count do not add group parallelism
# - how the key affects ordering and skew
# - what happens if the process crashes after sink.write but before offset commit
# - retention, replication, and schema-compatibility choices at 200k events/sec
