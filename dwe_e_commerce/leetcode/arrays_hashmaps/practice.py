"""Arrays and hash maps: type each solution from scratch, then dry-run it."""

from collections import defaultdict


def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """Return indices of two distinct values whose sum is target. O(n) time."""
    # TODO: store what is needed to recognize a complement.
    pass


def three_sum(nums: list[int]) -> list[list[int]]:
    """Return unique triplets summing to zero. No duplicate triplets."""
    # TODO: sort, fix one value, then use two pointers.
    pass


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group strings containing the same character counts."""
    # TODO: choose a canonical, hashable key.
    pass


def subarray_sum(nums: list[int], k: int) -> int:
    """Count contiguous subarrays summing to k; values may be negative."""
    # TODO: prefix sum + frequency map. Seed the empty prefix correctly.
    pass


# Dry-run cases (write expected results before uncommenting assertions):
# assert two_sum([2, 7, 11, 15], 9) == (...)
# assert sorted(map(sorted, three_sum([-1, 0, 1, 2, -1, -4]))) == ...
# assert subarray_sum([1, 1, 1], 2) == ...
# Edge cases: empty input, duplicates, negative values, no solution.
