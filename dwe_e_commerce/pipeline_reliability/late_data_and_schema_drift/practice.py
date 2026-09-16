"""Handle late events and schema changes without silently corrupting metrics."""

from dataclasses import dataclass
from datetime import datetime, timedelta
from decimal import Decimal, InvalidOperation
from typing import Any


@dataclass(frozen=True)
class ProductEvent:
    event_id: str
    event_time: datetime
    processing_time: datetime
    seller_id: str
    price: Decimal
    currency: str


@dataclass(frozen=True)
class DeadLetter:
    raw_event: dict[str, Any]
    error: str
    failed_at: datetime
    schema_version: str | None


def is_late(event: ProductEvent, watermark: timedelta) -> bool:
    # TODO: compare event time and processing time using the chosen lateness rule.
    pass


def parse_event(raw: dict[str, Any]) -> ProductEvent:
    """Accept legacy integer cents and new decimal-string prices."""
    # TODO: validate required fields, convert both price forms, and default or
    # reject a missing currency according to an explicit contract.
    try:
        raise NotImplementedError
    except (KeyError, TypeError, ValueError, InvalidOperation):
        raise


def affected_partitions(
    run_at: datetime, allowed_lateness: timedelta
) -> list[str]:
    """Return date partitions that must be recomputed for late data."""
    # TODO
    pass


# Add tests for: event 10 minutes late, event 72 hours late, duplicate event,
# price=1234 cents, price="12.34", missing currency, and removed seller_id.
# Decide which failures stop the pipeline and which go to a replayable dead letter.
