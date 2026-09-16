"""Prefix sums and range-query drills."""


class NumArray:
    """Immutable array with O(1) inclusive range-sum queries."""

    def __init__(self, nums: list[int]):
        # TODO: build a prefix array with a leading zero.
        pass

    def sum_range(self, left: int, right: int) -> int:
        # TODO: subtract two prefixes.
        pass


def subarray_sum(nums: list[int], k: int) -> int:
    """Count contiguous subarrays whose sum is k."""
    # TODO: count earlier prefixes equal to current_prefix - k.
    pass


def product_except_self(nums: list[int]) -> list[int]:
    """Return products except self without division, in O(n) time."""
    # TODO: store left products, then multiply by a running right product.
    pass


# Test: [], [5], [1, 2, 3, 4], [0, 1, 2], [0, 0, 2], and negative numbers.
# Explain why a leading-zero prefix removes boundary special cases.
