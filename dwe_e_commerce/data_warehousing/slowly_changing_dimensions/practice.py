"""Implement an idempotent Slowly Changing Dimension Type 2 update."""

from dataclasses import dataclass
from datetime import datetime


MAX_TIME = datetime.max.replace(microsecond=0)


@dataclass(frozen=True)
class ProductChange:
    product_id: int
    name: str
    category: str
    effective_at: datetime
    ingested_at: datetime


@dataclass
class ProductVersion:
    surrogate_key: int
    product_id: int
    name: str
    category: str
    valid_from: datetime
    valid_to: datetime
    is_current: bool


def deduplicate_changes(changes: list[ProductChange]) -> list[ProductChange]:
    """Keep the latest-ingested change for each business key/effective time."""
    # TODO: make the result deterministic and sorted for application.
    pass


def apply_scd2(
    existing: list[ProductVersion], changes: list[ProductChange]
) -> list[ProductVersion]:
    """Return Type 2 history using half-open [valid_from, valid_to) intervals."""
    # TODO: close old versions, insert changed versions, and support late changes.
    # TODO: rerunning with identical input must produce identical output.
    pass


CHANGES = [
    ProductChange(42, "Air Fryer", "Electronics", datetime(2026, 1, 1), datetime(2026, 1, 1, 1)),
    ProductChange(42, "Air Fryer", "Home Appliances", datetime(2026, 5, 10), datetime(2026, 5, 11)),
]

# Tests to add:
# - the category valid on 2026-05-09 differs from 2026-05-10
# - no overlapping validity intervals
# - exactly one current row per product
# - applying CHANGES twice is idempotent
# - a late change inserted between two existing versions splits the interval
