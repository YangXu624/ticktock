"""
PRACTICE TASK: TWO POINTERS & SLIDING WINDOWS FOR TIME-SERIES & TEXT SEQUENCES
-----------------------------------------------------------------------------
In ML engineering, sequence processing uses sliding windows to construct local context 
tokens in NLP or to calculate rolling statistical metrics (mean, standard deviation) 
over time-series feature streams.

Implementations to write:
1. rolling_mean(nums, K): Computes the rolling average of an array using a sliding window of size K.
2. rolling_variance(nums, K): Computes the rolling variance of an array using a sliding window of size K.
   Hint: Use Welford's algorithm or track dynamic sum and sum-of-squares in O(1) step-updates.
3. longest_substring_no_repeats(s): Finds the length of the longest substring without repeating characters.
"""

from typing import List, Tuple

def rolling_mean(nums: List[float], K: int) -> List[float]:
    """
    Computes rolling mean of the array using window of size K.
    The window size must be exactly K, so output array size will be len(nums) - K + 1.
    If len(nums) < K, return an empty list.
    
    Time Complexity target: O(N)
    Space Complexity target: O(1) (excluding output list)
    """
    # TODO: Implement this function
    pass

def rolling_variance(nums: List[float], K: int) -> List[float]:
    """
    Computes rolling population variance (sigma^2) using window of size K.
    Formula: Var = (1/K) * sum((x - mean)^2)
    To achieve O(1) slide update, keep track of:
      - sum_x: sum of elements in current window
      - sum_x2: sum of squared elements in current window
      Then Var = (sum_x2 / K) - (sum_x / K)^2
      
    Time Complexity target: O(N)
    Space Complexity target: O(1) (excluding output list)
    """
    # TODO: Implement this function
    pass

def longest_substring_no_repeats(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.
    
    Time Complexity target: O(N)
    Space Complexity target: O(min(N, A)) where A is alphabet size.
    """
    # TODO: Implement this function
    pass


# --- Verification Tests ---
if __name__ == "__main__":
    print("Testing Rolling Mean...")
    nums = [1.0, 2.0, 3.0, 4.0, 5.0]
    # For window size 3:
    # [1, 2, 3] -> mean = 2.0
    # [2, 3, 4] -> mean = 3.0
    # [3, 4, 5] -> mean = 4.0
    try:
        means = rolling_mean(nums, 3)
        assert means == [2.0, 3.0, 4.0], f"Expected [2.0, 3.0, 4.0], got {means}"
        print("Rolling Mean passed!")
    except Exception as e:
        print(f"Rolling Mean failed or not implemented yet: {e}")

    print("Testing Rolling Variance...")
    # For window [1, 2, 3] (mean = 2.0)
    # Var = ((1-2)^2 + (2-2)^2 + (3-2)^2) / 3 = 2/3 = 0.6666...
    # For window [2, 3, 4] (mean = 3.0) -> Var = 2/3
    # For window [3, 4, 5] (mean = 4.0) -> Var = 2/3
    try:
        vars = rolling_variance(nums, 3)
        # Using tolerance for float precision
        for v in vars:
            assert abs(v - 2/3) < 1e-7, f"Expected 0.66666..., got {v}"
        print("Rolling Variance passed!")
    except Exception as e:
        print(f"Rolling Variance failed or not implemented yet: {e}")

    print("Testing Longest Substring Without Repeats...")
    s = "abcabcbb"
    try:
        ans = longest_substring_no_repeats(s)
        assert ans == 3, f"Expected 3, got {ans}"
        print("Longest Substring Without Repeats passed!")
    except Exception as e:
        print(f"Longest Substring Without Repeats failed or not implemented yet: {e}")

    print("\nAll Sliding Window verification tests passed (once you implement them)!")
