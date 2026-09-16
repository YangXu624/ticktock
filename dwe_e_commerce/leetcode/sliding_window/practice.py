"""Sliding-window and two-pointer drills."""


def longest_unique_substring(text: str) -> int:
    """Length of the longest substring with no repeated character. O(n)."""
    left = 0
    last_seen: dict[str, int] = {}
    best = 0
    for right, char in enumerate(text):
        # TODO: move left without ever moving it backward.
        # TODO: update last_seen and best.
        pass
    return best


def max_container_area(heights: list[int]) -> int:
    """Largest water container area. O(n) time and O(1) extra space."""
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        # TODO: calculate area.
        # TODO: justify which pointer can be discarded.
        pass
    return best


def min_subarray_len(target: int, nums: list[int]) -> int:
    """Shortest nonempty subarray with sum >= target; nums are positive."""
    # TODO: expand right, shrink left while the window is valid.
    pass


# Say aloud: What invariant does the window maintain? Why is each element
# visited at most twice? Why would the last problem fail if negatives appeared?
