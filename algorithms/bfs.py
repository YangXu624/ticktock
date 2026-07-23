"""
PRACTICE TASK: CORE BREADTH-FIRST SEARCH (BFS) IMPLEMENTATION
------------------------------------------------------------
BFS traverses a graph layer-by-layer, making it the mathematical choice for 
finding the shortest path in an unweighted graph and computing level-by-level 
activations/nodes.

Implementations to write:
1. bfs_iterative(adj_list, start): Traverses the graph from a start node using 
   a queue (deque) and returns the list of nodes visited in order.
2. bfs_shortest_path(adj_list, start, target): Uses BFS to find the shortest 
   path from start to target. Returns the list of node IDs. Returns empty list 
   if target is unreachable.
3. level_order_traversal(root): Traverses a binary tree level-by-level, returning 
   a list of lists showing node values at each level.
"""

from collections import deque
from typing import List, Dict, Set, Optional

# Tree node definition
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def bfs_iterative(adj_list: Dict[int, List[int]], start: int) -> List[int]:
    """
    Traverses the graph iteratively using a queue.
    
    Time Complexity: O(V + E)
    Space Complexity: O(V) (queue + visited set)
    """
    # TODO: Implement this function
    queue = deque([start])
    traversal_order = []
    visited = {start}

    while queue:
        curr = queue.popleft()
        visited.add(curr) # use set for O(1) lookup time
        traversal_order.append(curr) # add node to path

        for neighbour in adj_list[curr]: # check neighbours
            if neighbour not in visited:
                visited.add(neighbour) # mark as visited
                queue.append(neighbour)
    
    return traversal_order


def bfs_shortest_path(adj_list: Dict[int, List[int]], start: int, target: int) -> List[int]:
    """
    Finds the shortest path in an unweighted graph from start to target.
    
    Returns:
      List of node IDs from start to target. If unreachable, return [].
      
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    # TODO: Implement this function (store path state or parent pointers in a dict)
    queue = deque([start])
    parents = {start: None} # begin : end

    visited = {}

    while queue:
        curr = queue.popleft()
        visited.add(curr)
        


def level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Performs level-order traversal on a binary tree.
    
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    # TODO: Implement this function
    queue = deque([root])
    traversal = []

    while queue:
        curr = queue.popleft()
        if curr:
            traversal.append(curr.val)
            queue.append(curr.left)
            queue.append(curr.right)
    return traversal


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

    print("Testing BFS Iterative...")
    try:
        path = bfs_iterative(graph, 0)
        print(f"BFS Path: {path}")
        assert len(path) == 5
        assert set(path) == {0, 1, 2, 3, 4}
        # First layer after 0 must be 1 and 2
        assert set(path[1:3]) == {1, 2}
        print("BFS Iterative passed!")
    except Exception as e:
        print(f"BFS Iterative failed or not implemented yet: {e}")

    print("Testing BFS Shortest Path...")
    try:
        sp = bfs_shortest_path(graph, 0, 4)
        print(f"Shortest path from 0 to 4: {sp}")
        # Expected shortest path: 0 -> 1 -> 3 -> 4 (len 4) OR 0 -> 2 -> 3 -> 4 (len 4)
        assert len(sp) == 4
        assert sp[0] == 0 and sp[-1] == 4
        print("BFS Shortest Path passed!")
    except Exception as e:
        print(f"BFS Shortest Path failed or not implemented yet: {e}")

    print("Testing Binary Tree Level Order...")
    # Tree:
    #      1
    #     / \
    #    2   3
    #   /
    #  4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    # Expected output: [[1], [2, 3], [4]]
    try:
        levels = level_order_traversal(root)
        print(f"Tree levels: {levels}")
        assert levels == [[1], [2, 3], [4]], f"Expected [[1], [2, 3], [4]], got {levels}"
        print("Binary Tree Level Order passed!")
    except Exception as e:
        print(f"Binary Tree Level Order failed or not implemented yet: {e}")

    print("\nAll BFS fundamentals verification tests passed (once you implement them)!")
