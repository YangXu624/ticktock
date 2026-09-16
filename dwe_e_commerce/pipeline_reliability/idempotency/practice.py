"""Build an idempotent hourly seller-revenue pipeline."""

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass(frozen=True)
class PaymentEvent:
    event_id: str
    seller_id: str
    occurred_at: datetime
    amount: Decimal
    status: str
    ingested_at: datetime


@dataclass(frozen=True)
class SellerRevenue:
    seller_id: str
    revenue_date: str
    amount: Decimal


def deduplicate(events: list[PaymentEvent]) -> list[PaymentEvent]:
    """Return one deterministic version of each source event."""
    # TODO: use event_id and an explicit latest-version rule.
    pass


def aggregate(events: list[PaymentEvent]) -> list[SellerRevenue]:
    """Aggregate successful payments at seller-day grain."""
    # TODO: specify time zone and accepted statuses.
    pass


def merge_revenue(
    target: dict[tuple[str, str], SellerRevenue],
    batch: list[SellerRevenue],
) -> None:
    """Atomically upsert by the target natural key."""
    # TODO: replace affected keys rather than incrementing existing totals.
    pass


def run_pipeline(
    events: list[PaymentEvent], target: dict[tuple[str, str], SellerRevenue]
) -> None:
    """Rerunning with identical input must leave target unchanged."""
    # TODO: stage complete output, validate it, then commit atomically.
    pass


# Tests to write:
# - duplicate and replayed events do not double count
# - crash before commit leaves the old target intact
# - crash after commit and before success acknowledgement is safe to retry
# - target keys are unique and totals reconcile to deduplicated inputs
