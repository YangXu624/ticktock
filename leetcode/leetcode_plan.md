# TikTok MLE Interview: LeetCode Preparation Plan

Based on the uploaded frequency logs (`1. Thirty Days.csv`, `2. Three Months.csv`, `3. Six Months.csv`, `4. All.csv`), this plan outlines a high-efficiency path to master the algorithms and design patterns most frequently asked in TikTok interview loops.

---

## Roadmap: Recommended Preparation Order

### Phase 1: High-Frequency Core (Priority 1)
*Focus: These represent the highest density of questions in recent 30-day and 3-month windows. Master these first.*

| Problem | Difficulty | Topics | Why It's Critical | Link |
| :--- | :--- | :--- | :--- | :--- |
| **LRU Cache** (LeetCode 146) | Medium | Hash Table, Doubly-Linked List, Design | **100% frequency.** Directly maps to the custom `OrderedDict` implementation you are building today. | [Link](https://leetcode.com/problems/lru-cache) |
| **Number of Islands** (LeetCode 200) | Medium | DFS, BFS, Matrix | Extremely high frequency (82%). Core matrix/graph traversal anchor. | [Link](https://leetcode.com/problems/number-of-islands) |
| **Course Schedule** (LeetCode 207) | Medium | DFS, BFS, Topological Sort | High frequency (88% in 30d). Master topological sorting (cycle detection in graphs). | [Link](https://leetcode.com/problems/course-schedule) |
| **Longest Mountain in Array** (LeetCode 845) | Medium | Array, Two Pointers, DP | High frequency (88% in 30d). Tests array boundary check accuracy. | [Link](https://leetcode.com/problems/longest-mountain-in-array) |
| **Number of Distinct Islands** (LeetCode 694) | Medium | DFS, BFS, Hash Function | High frequency (88% in 30d). Teaches how to serialize grid shapes to compare uniqueness. | [Link](https://leetcode.com/problems/number-of-distinct-islands) |
| **Path Sum III** (LeetCode 437) | Medium | Tree, DFS, Prefix Sum | High frequency (88% in 30d). Tests nested tree traversals combined with prefix tracking. | [Link](https://leetcode.com/problems/path-sum-iii) |
| **Meeting Rooms II** (LeetCode 253) | Medium | Line Sweep, Greedy, Heap | Line sweep is a highly requested TikTok pattern. | [Link](https://leetcode.com/problems/meeting-rooms-ii) |

---

### Phase 2: Design & High-Difficulty Implementations (Priority 2)
*Focus: TikTok loops frequently test pointer manipulation and structural design under hard complexity bounds.*

| Problem | Difficulty | Topics | Why It's Critical | Link |
| :--- | :--- | :--- | :--- | :--- |
| **Reverse Nodes in k-Group** (LeetCode 25) | Hard | Linked List, Recursion | High frequency (88% in 30d). Ultimate test of nested pointer manipulations. | [Link](https://leetcode.com/problems/reverse-nodes-in-k-group) |
| **All O`one Data Structure** (LeetCode 432) | Hard | Hash Table, Doubly-Linked List, Design | High frequency (65% in 3m). An extension of LRU Cache; requires maintaining keys grouped by frequency count in $O(1)$ time. | [Link](https://leetcode.com/problems/all-oone-data-structure) |
| **Text Justification** (LeetCode 68) | Hard | String, Simulation | High frequency (68% in 6m). Extremely tedious simulation problem testing pure string edge-case handling. | [Link](https://leetcode.com/problems/text-justification) |
| **Serialize & Deserialize N-ary Tree** (LeetCode 428) | Hard | String, Tree, DFS | High frequency (65% in 3m). Checks your ability to transform structural trees to/from strings. | [Link](https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree) |
| **Cheapest Flights Within K Stops** (LeetCode 787) | Medium | Graph, DP, Shortest Path | High frequency (65% in 3m). Master Bellman-Ford, Dijkstra, or BFS with state tracking constraints. | [Link](https://leetcode.com/problems/cheapest-flights-within-k-stops) |

---

### Phase 3: Core Algorithm Patterns (Priority 3)
*Focus: Master these classical algorithmic building blocks that appear consistently in 6-month lists.*

| Problem | Difficulty | Topics | Link |
| :--- | :--- | :--- | :--- |
| **Longest Increasing Subsequence** (LeetCode 300) | Medium | Array, Binary Search, DP | [Link](https://leetcode.com/problems/longest-increasing-subsequence) |
| **Longest Substring Without Repeating Characters** (LeetCode 3) | Medium | Hash Table, Sliding Window | [Link](https://leetcode.com/problems/longest-substring-without-repeating-characters) |
| **Kth Largest Element in an Array** (LeetCode 215) | Medium | Heap, Quickselect | [Link](https://leetcode.com/problems/kth-largest-element-in-an-array) |
| **Subarray Sum Equals K** (LeetCode 560) | Medium | Hash Table, Prefix Sum | [Link](https://leetcode.com/problems/subarray-sum-equals-k) |
| **Search in Rotated Sorted Array** (LeetCode 33) | Medium | Binary Search | [Link](https://leetcode.com/problems/search-in-rotated-sorted-array) |
| **Word Search** (LeetCode 79) | Medium | Backtracking, DFS, Matrix | [Link](https://leetcode.com/problems/word-search) |

---

## Key Execution Patterns to Master
1.  **Linked List + Hash Map (O(1) Design):** Master the coordination between a hash lookup dictionary and a doubly linked list. This pattern solves **LRU Cache**, **LFU Cache**, and **All O`one** with optimal time constraints.
2.  **Topological Sort:** Be ready to code Kahn's algorithm (indegree BFS) or DFS cycle-detection immediately for any graph dependency problems.
3.  **Prefix Sum Hash Maps:** For subarray target problems (like LeetCode 560), never use a nested $O(N^2)$ loop. Always track cumulative sums in a map to achieve $O(N)$ execution.
