"""
PRACTICE TASK: BINARY SEARCH PATTERNS FOR ML
-------------------------------------------
Binary search is widely used in ML optimization, from finding split thresholds 
in Decision Trees to computing percentile-based thresholds and quantiles on 
prediction scores (e.g., thresholding model probability outputs for classification).

Implementations to write:
1. binary_search(nums, target): Returns index of target in sorted array, or -1 if not found.
2. search_insert_position(nums, target): Returns insertion index to maintain sorted order 
   (identical to finding decision tree split point boundaries, or bisect_left).
3. find_threshold_for_percentile(sorted_scores, percentile): Returns the score threshold 
   such that a given percentage (e.g., 90%) of scores are less than or equal to it.
"""

from typing import List

def binary_search(nums: List[int], target: int) -> int:
    """
    Finds the target in a sorted list of integers.
    Return the index of target if found, otherwise return -1.
    
    Time Complexity target: O(log N)
    Space Complexity target: O(1)
    """
    # TODO: Implement this function
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if target == nums[m]:
            return m
        elif target > nums[m]:
            l = m + 1
        else:
            r = m - 1
    return -1

def search_insert_position(nums: List[float], target: float) -> int:
    """
    Returns the index where target should be inserted to maintain sorted order.
    If the target is already present, return the index of the first occurrence (bisect_left).
    
    Time Complexity target: O(log N)
    Space Complexity target: O(1)
    """
    # TODO: Implement this function
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if target == nums[m]:
            return m
        elif target > nums[m]:
            l = m + 1
        else:
            r = m - 1
    return l

def find_threshold_for_percentile(sorted_scores: List[float], percentile: float) -> float:
    """
    Given a sorted list of prediction probabilities/scores (ascending) and a percentile
    value (0.0 to 1.0), return the score threshold.
    
    Example: 
      sorted_scores = [0.1, 0.15, 0.2, 0.5, 0.8, 0.9, 0.95]
      percentile = 0.80 (80th percentile)
      Should return the score bounding the lower 80% of data.
      Use binary search (bisect style) to locate the index.
      Index of percentile: index = ceil(percentile * (len(scores) - 1))
      
    Time Complexity target: O(1) if already sorted, but if we need to search or verify 
    elements close to it, write the index boundary search logic.
    """
    # TODO: Implement this function
    pass


# --- Verification Tests ---
if __name__ == "__main__":
    print("Testing Binary Search...")
    nums = [1, 3, 5, 6, 8, 10, 15]
    assert binary_search(nums, 5) == 2
    assert binary_search(nums, 7) == -1
    print("Binary Search passed!")

    print("Testing Search Insert Position...")
    scores = [0.1, 0.2, 0.4, 0.4, 0.6, 0.8]
    # Insert 0.4: should return index 2 (the first occurrence)
    assert search_insert_position(scores, 0.4) == 2
    # Insert 0.5: should return index 4
    assert search_insert_position(scores, 0.5) == 4
    # Insert 0.0: should return index 0
    assert search_insert_position(scores, 0.0) == 0
    # Insert 0.9: should return index 6
    assert search_insert_position(scores, 0.9) == 6
    print("Search Insert Position passed!")

    print("Testing Threshold for Percentile...")
    all_scores = [0.05, 0.12, 0.22, 0.35, 0.48, 0.55, 0.68, 0.75, 0.88, 0.92, 0.99]
    # Length = 11. 80th percentile (80% of data is <= threshold).
    # Index computation should select the appropriate boundary.
    thresh = find_threshold_for_percentile(all_scores, 0.8)
    assert thresh == 0.88, f"Expected 0.88, got {thresh}"
    print("Threshold for Percentile passed!")

    print("\nAll Binary Search verification tests passed (once you implement them)!")
