"""
PRACTICE TASK: GRAPH TRAVERSALS (DFS/BFS) FOR ML TENSORS & COMPUTATION GRAPHS
------------------------------------------------------------------------------
Graphs are everywhere in ML: from computational graphs (like PyTorch Autograd execution 
DAGs) to spatial images (where adjacent pixels form a grid graph in computer vision).

Implementations to write:
1. num_islands(grid): Counts connected components in a 2D binary grid. (Connected-component
   labeling for image segmentation).
2. topological_sort(num_courses, prerequisites): Computes a valid execution sequence 
   for a set of dependent nodes. (Computation graph node ordering / Course Schedule LeetCode 207).
"""

from typing import List

def num_islands(grid: List[List[str]]) -> int:
    """
    Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
    return the number of islands. An island is surrounded by water and is formed by 
    connecting adjacent lands horizontally or vertically.
    
    Time Complexity target: O(M * N)
    Space Complexity target: O(M * N) (call stack size or queue size)
    """
    # TODO: Implement this function (using DFS or BFS)
    pass

def topological_sort(num_nodes: int, dependencies: List[List[int]]) -> List[int]:
    """
    Given a number of nodes (labeled from 0 to num_nodes - 1) and a list of directed dependency
    pairs where dependencies[i] = [dest, src] indicates node src must be executed before dest.
    
    Return a valid topological order of nodes (execution sequence).
    If a cycle is detected, return an empty list [] (since compilation graph cannot resolve circular dependencies).
    
    Time Complexity target: O(V + E)
    Space Complexity target: O(V + E)
    """
    # TODO: Implement this function (Kahn's algorithm/BFS indegree or DFS post-order)
    pass


# --- Verification Tests ---
if __name__ == "__main__":
    print("Testing Number of Islands (Image Segmentation)...")
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    # Expected islands: 3
    # 1. Top left 2x2
    # 2. Middle 1x1
    # 3. Bottom right 2x1
    try:
        islands = num_islands(grid)
        assert islands == 3, f"Expected 3 islands, got {islands}"
        print("Number of Islands passed!")
    except Exception as e:
        print(f"Number of Islands failed or not implemented yet: {e}")

    print("Testing Computational Graph Topological Sort...")
    # 4 operators. 
    # [1, 0] -> Op 0 must execute before Op 1
    # [2, 0] -> Op 0 must execute before Op 2
    # [3, 1] -> Op 1 must execute before Op 3
    # [3, 2] -> Op 2 must execute before Op 3
    # Valid orders: [0, 1, 2, 3] or [0, 2, 1, 3]
    deps = [[1, 0], [2, 0], [3, 1], [3, 2]]
    try:
        order = topological_sort(4, deps)
        assert order in [[0, 1, 2, 3], [0, 2, 1, 3]], f"Invalid execution order: {order}"
        
        # Test cycle detection
        # [0, 1], [1, 0] (cycle)
        cycle_deps = [[0, 1], [1, 0]]
        cycle_order = topological_sort(2, cycle_deps)
        assert cycle_order == [], f"Expected empty list for cycle, got {cycle_order}"
        print("Topological Sort passed!")
    except Exception as e:
        print(f"Topological Sort failed or not implemented yet: {e}")

    print("\nAll Graph Traversal verification tests passed (once you implement them)!")
