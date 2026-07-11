"""
PRACTICE TASK: K-WAY MERGE & STREAM SORTING FOR DISTRIBUTED PREDICTIONS
----------------------------------------------------------------------
In large-scale recommendation systems, candidate items are generated from 
multiple distributed pipelines (e.g. collaborative filtering worker, deep 
retrieval worker, popular item worker). Each worker produces a sorted list of 
scores. You must merge these sorted lists into a single consolidated, sorted 
stream to serve the ranker.

Implementations to write:
1. kway_merge_lists(lists): Merges K sorted lists of numbers into a single sorted list.
   Hint: Use a Min-Heap containing (value, list_index, element_index).
2. merge_prediction_streams(streams): Merges K sorted prediction streams where each element 
   is a tuple of (item_id, score), sorted descending by score. The merged result must
   also be sorted descending by score.
"""

from typing import List, Tuple
import heapq

def kway_merge_lists(lists: List[List[float]]) -> List[float]:
    """
    Merges K sorted lists (ascending order) into one sorted list.
    
    Time Complexity target: O(N log K) where N is total number of elements.
    Space Complexity target: O(K) heap size.
    """
    # TODO: Implement this function
    pass

def merge_prediction_streams(streams: List[List[Tuple[str, float]]]) -> List[Tuple[str, float]]:
    """
    Merges K lists of item predictions (each sorted in descending order by score)
    into a single consolidated list sorted descending by score.
    
    Example input:
      streams = [
        [("item_A", 0.95), ("item_B", 0.80)],
        [("item_C", 0.90), ("item_D", 0.75)],
      ]
      Returns: [("item_A", 0.95), ("item_C", 0.90), ("item_B", 0.80), ("item_D", 0.75)]
      
    Time Complexity target: O(N log K)
    Space Complexity target: O(K)
    """
    # TODO: Implement this function
    pass


# --- Verification Tests ---
if __name__ == "__main__":
    print("Testing K-Way Merge Lists...")
    lists = [
        [1.5, 4.0, 7.5],
        [2.0, 5.5, 8.0],
        [0.5, 9.0]
    ]
    # Expected sorted: [0.5, 1.5, 2.0, 4.0, 5.5, 7.5, 8.0, 9.0]
    try:
        merged = kway_merge_lists(lists)
        assert merged == [0.5, 1.5, 2.0, 4.0, 5.5, 7.5, 8.0, 9.0], f"Expected sorted, got {merged}"
        print("K-Way Merge Lists passed!")
    except Exception as e:
        print(f"K-Way Merge Lists failed or not implemented yet: {e}")

    print("Testing Merge Prediction Streams...")
    streams = [
        [("item_A", 0.98), ("item_C", 0.85)],
        [("item_B", 0.92), ("item_E", 0.70)],
        [("item_D", 0.88), ("item_F", 0.65)]
    ]
    # Expected sorted descending:
    # A (0.98), B (0.92), D (0.88), C (0.85), E (0.70), F (0.65)
    expected = [
        ("item_A", 0.98),
        ("item_B", 0.92),
        ("item_D", 0.88),
        ("item_C", 0.85),
        ("item_E", 0.70),
        ("item_F", 0.65)
    ]
    try:
        merged_stream = merge_prediction_streams(streams)
        assert merged_stream == expected, f"Expected {expected}, got {merged_stream}"
        print("Merge Prediction Streams passed!")
    except Exception as e:
        print(f"Merge Prediction Streams failed or not implemented yet: {e}")

    print("\nAll K-Way Merge verification tests passed (once you implement them)!")
