"""
PRACTICE TASK: CORE DEPTH-FIRST SEARCH (DFS) IMPLEMENTATION
----------------------------------------------------------
Before applying DFS to complex scenarios (like topological sorting or graph cloning), 
you must master the fundamentals: recursive execution flow, explicit stack state 
tracking, and target path backtracking.

Implementations to write:
1. dfs_recursive(adj_list, start, visited=None): Runs DFS recursively from the start node 
   and returns the traversal path list.
2. dfs_iterative(adj_list, start): Runs DFS iteratively using an explicit stack 
   and returns the traversal path list.
3. find_path_dfs(adj_list, start, target): Returns a list representing the path 
   from start to target using DFS backtracking. Returns empty list if no path exists.
"""

from typing import List, Dict, Set, Optional

def dfs_recursive(adj_list: Dict[int, List[int]], start: int, visited: Set[int] = None) -> List[int]:
    """
    Traverses the graph using recursion.
    
    Time Complexity: O(V + E)
    Space Complexity: O(V) (call stack + visited set)
    """
    if visited is None:
        visited = set()
    # TODO: Implement recursive DFS traversal, returning list of nodes visited in order
    pass

def dfs_iterative(adj_list: Dict[int, List[int]], start: int) -> List[int]:
    """
    Traverses the graph using an explicit Stack (list).
    
    Time Complexity: O(V + E)
    Space Complexity: O(V) (stack + visited set)
    """
    # TODO: Implement iterative DFS traversal, returning list of nodes visited in order
    pass

def find_path_dfs(adj_list: Dict[int, List[int]], start: int, target: int) -> List[int]:
    """
    Uses DFS backtracking to find a path from start to target.
    
    Returns:
      List of node IDs from start to target, e.g. [start, node1, ..., target].
      If no path exists, return [].
      
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    # TODO: Implement path finding
    pass


# --- Verification Tests ---
if __name__ == "__main__":
    # Test Graph:
    #     0 --- 1
    #     |     |
    #     2 --- 3 --- 4
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2, 4],
        4: [3]
    }

    print("Testing DFS Recursive...")
    try:
        path_rec = dfs_recursive(graph, 0)
        print(f"Recursive Path: {path_rec}")
        # Traversal order depends on neighbor ordering, but all nodes must be reached
        assert len(path_rec) == 5
        assert set(path_rec) == {0, 1, 2, 3, 4}
        print("DFS Recursive passed!")
    except Exception as e:
        print(f"DFS Recursive failed or not implemented yet: {e}")

    print("Testing DFS Iterative...")
    try:
        path_iter = dfs_iterative(graph, 0)
        print(f"Iterative Path: {path_iter}")
        assert len(path_iter) == 5
        assert set(path_iter) == {0, 1, 2, 3, 4}
        print("DFS Iterative passed!")
    except Exception as e:
        print(f"DFS Iterative failed or not implemented yet: {e}")

    print("Testing Path Finding via DFS...")
    try:
        path_to_4 = find_path_dfs(graph, 0, 4)
        print(f"Path to 4: {path_to_4}")
        assert path_to_4[0] == 0
        assert path_to_4[-1] == 4
        # Validate path connectedness
        for i in range(len(path_to_4) - 1):
            assert path_to_4[i+1] in graph[path_to_4[i]]
        print("DFS Path Finding passed!")
    except Exception as e:
        print(f"DFS Path Finding failed or not implemented yet: {e}")

    print("\nAll DFS fundamentals verification tests passed (once you implement them)!")
