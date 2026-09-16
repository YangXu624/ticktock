"""
PRACTICE TASK: HEAPS & PRIORITY QUEUES FOR SEARCH & RETRIEVAL
-------------------------------------------------------------
Heaps are essential in search, ranking, and recommender candidate generation. 
They allow retrieving the Top-K closest items or scoring predictions efficiently 
without full sorting.

Implementations to write:
1. MinHeap: A custom binary min-heap implementing:
   - heapify(arr): Build a valid heap in-place in O(N) time.
   - push(val): Add an element in O(log N) time.
   - pop(): Remove and return the min element in O(log N) time.
2. k_closest_points(points, K): Find the K closest 2D points to the origin (0, 0)
   using a custom Max-Heap (or python's heapq) to maintain size K.
3. top_k_frequent(nums, K): Find the K most frequent numbers using a Heap.
"""

from hashlib import algorithms_available
from typing import List, Tuple
import heapq  # You may use heapq for points/frequency tasks if you implement MinHeap from scratch.

class MinHeap:
    def __init__(self, arr: List[int] = None):
        self.heap = []
        if arr:
            self.heap = list(arr)
            self.heapify()

    def siftdown(self, i: int, n: int) -> None:
        while True:
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if n > left and self.heap[smallest] > self.heap[left]:
                    smallest = left
            if n > right and self.heap[smallest] > self.heap[right]:
                    smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest


    def heapify(self) -> None:
        """
        Builds the heap in-place from the array self.heap.
        
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        # TODO: Implement in-place heapify (sift-down starting from last non-leaf node)

        n = len(self.heap)

        for i in range(n // 2 - 1, -1, -1):
            self.siftdown(i, n)

    def push(self, val: int) -> None:
        """
        Inserts a new value into the heap.
        
        Time Complexity: O(log N)
        Space Complexity: O(1)
        """
        # TODO: Implement push (append then sift-up)

        n = len(self.heap)
        self.heap.append(val)
        i = n # new value always pushed to index n

        while i > 0:
            parent = (i - 1) // 2 # pointer to parent of new value

            if self.heap[parent] <= val: # if parent is smaller than new value
                break # good to go; no changes
        
            self.heap[i] = self.heap[parent]
            i = parent
        
        self.heap[i] = val

    def pop(self) -> int:
        """
        Removes and returns the minimum element from the heap.
        Raises IndexError if the heap is empty.
        
        Time Complexity: O(log N)
        Space Complexity: O(1)
        """
        # TODO: Implement pop (swap root with last, pop last, sift-down root)
        n = len(self.heap) - 1
        val = self.heap[0]
        self.heap[0], self.heap[n] = self.heap[n], self.heap[0]
        self.siftdown(0, n)
        return self.heap.pop(n)



def k_closest_points(points: List[List[int]], K: int) -> List[List[int]]:
    """
    Given an array of 2D points, return the K closest points to the origin (0, 0).
    Compute distance as squared Euclidean distance: x^2 + y^2.
    
    Hint: Use a Max-Heap of size K.
    Time Complexity target: O(N log K)
    Space Complexity target: O(K)
    """
    # TODO: Implement this function
    pass


def top_k_frequent(nums: List[int], K: int) -> List[int]:
    """
    Given an integer array nums and an integer K, return the K most frequent elements.
    
    Time Complexity target: O(N log K) or O(N) using bucket sort.
    Space Complexity target: O(N) for hash map.
    """
    # TODO: Implement this function
    pass


# --- Verification Tests ---
if __name__ == "__main__":
    print("Testing Custom MinHeap...")
    arr = [9, 4, 7, 1, 2, 6, 3]
    h = MinHeap(arr)
    print(h.heap)
    h.push(0)
    print(h.heap)
    val = h.pop()
    print(h.heap, val)
    # The minimum element should be popped first
    sorted_out = []
    try:
        while len(h.heap) > 0:
            sorted_out.append(h.pop())
        assert sorted_out == sorted(arr), f"Expected sorted array, got {sorted_out}"
        print("MinHeap push/pop/heapify passed!")
    except Exception as e:
        print(f"Heap verification failed or not implemented yet: {e}")

    print("Testing K Closest Points...")
    points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
    k_close = k_closest_points(points, 2)
    # Distance of [0,1] is 1, [-2,2] is 8, [1,3] is 10, [5,8] is 89
    # Closest 2 are [0,1] and [-2,2]
    # Verify elements are correct (order does not matter in return)
    sorted_k_close = sorted(k_close, key=lambda p: p[0]**2 + p[1]**2)
    assert sorted_k_close == [[0, 1], [-2, 2]], f"Expected [[0, 1], [-2, 2]], got {sorted_k_close}"
    print("K Closest Points passed!")

    print("Testing Top K Frequent Elements...")
    nums = [1, 1, 1, 2, 2, 3, 100, 100, 100, 100]
    top_k = top_k_frequent(nums, 2)
    # Frequency: 100 -> 4 times, 1 -> 3 times, 2 -> 2 times, 3 -> 1 time.
    # Top 2 are [100, 1] (order irrelevant)
    assert set(top_k) == {100, 1}, f"Expected {100, 1}, got {top_k}"
    print("Top K Frequent Elements passed!")

    print("\nAll Heap verification tests passed (once you implement them)!")
