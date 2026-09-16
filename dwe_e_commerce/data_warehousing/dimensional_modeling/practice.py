"""Design a TikTok Shop star schema by completing the code template."""

from dataclasses import dataclass, field


@dataclass
class FactTable:
    name: str
    grain: str
    foreign_keys: list[str]
    measures: dict[str, str]  # measure -> aggregation rule
    degenerate_dimensions: list[str] = field(default_factory=list)


@dataclass
class DimensionTable:
    name: str
    business_key: str
    attributes: list[str]
    history_strategy: str


@dataclass
class WarehouseModel:
    facts: list[FactTable]
    dimensions: list[DimensionTable]


REQUIRED_METRICS = [
    "daily GMV by seller, category, and region",
    "product-view to purchase conversion",
    "refund rate",
    "historical product-category reporting",
]


def design_shop_warehouse() -> WarehouseModel:
    """Define facts at explicit grains and dimensions with history behavior."""
    # TODO: Add fact_order_item, fact_product_event, and fact_refund.
    # TODO: Add conformed date, user, seller, and product dimensions.
    # TODO: State whether each measure is additive, semi-additive, or non-additive.
    return WarehouseModel(facts=[], dimensions=[])


def validate_model(model: WarehouseModel) -> list[str]:
    """Return design problems such as a missing grain or duplicate table name."""
    errors: list[str] = []
    # TODO: validate nonempty, unique names and unambiguous grains.
    return errors


if __name__ == "__main__":
    model = design_shop_warehouse()
    print(model)
    print("Validation:", validate_model(model))

# Explain aloud after coding:
# 1. Why is order-item grain safer than order grain for category GMV?
# 2. How do partial refunds relate to order items?
# 3. Which product category receives historical GMV after a category change?
