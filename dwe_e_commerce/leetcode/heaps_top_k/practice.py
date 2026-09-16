"""Heap drills. State whether k is small relative to n before choosing a method."""

import heapq
from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Return k most frequent values using O(u log k) time, u unique values."""
    counts = Counter(nums)
    heap: list[tuple[int, int]] = []
    for value, frequency in counts.items():
        # TODO: maintain a min-heap containing at most k entries.
        pass
    return [value for _, value in heap]


def merge_k_sorted(lists: list[list[int]]) -> list[int]:
    """Merge sorted lists in O(total_items * log k) time."""
    heap: list[tuple[int, int, int]] = []  # value, list_index, item_index
    # TODO: seed the heap with the first item from each nonempty list.
    # TODO: pop the smallest and push its successor.
    pass


# Explain: min-heap vs max-heap, why tuples need deterministic tie fields,
# complexity in n/k/u, and behavior for k == 0 or k > number of unique values.
