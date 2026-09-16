"""Implement explicit GMV definitions and simple channel attribution."""

from dataclasses import dataclass
from datetime import datetime, timedelta
from decimal import Decimal


@dataclass(frozen=True)
class Order:
    order_id: str
    user_id: str
    paid_amount: Decimal
    refunded_amount: Decimal
    status: str
    paid_at: datetime | None
    completed_at: datetime | None


@dataclass(frozen=True)
class Touchpoint:
    user_id: str
    channel: str
    occurred_at: datetime


def paid_gmv(orders: list[Order]) -> Decimal:
    """Gross value recognized when payment succeeds, before refunds."""
    # TODO: encode the status and timestamp rules explicitly.
    pass


def completed_gmv(orders: list[Order]) -> Decimal:
    """Gross value of completed orders, before refunds."""
    # TODO
    pass


def net_gmv(orders: list[Order]) -> Decimal:
    """Paid GMV less valid refund value; define cancellation behavior."""
    # TODO
    pass


def last_touch_channel(
    order: Order, touchpoints: list[Touchpoint], window: timedelta
) -> str | None:
    """Return the latest eligible pre-payment channel inside the window."""
    # TODO: match user, enforce event order, and apply the lookback window.
    pass


# Extend the model with currency/FX date, discount, tax, shipping, time zone,
# late-data finalization, cross-device identity, direct traffic, and refund rules.
# Construct one order for which paid GMV, completed GMV, and net GMV differ.
