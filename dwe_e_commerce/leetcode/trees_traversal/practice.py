"""Tree and graph traversal templates."""

from collections import deque
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


def level_order(root: TreeNode | None) -> list[list[int]]:
    """Return values grouped by tree depth using BFS."""
    if root is None:
        return []
    queue = deque([root])
    levels: list[list[int]] = []
    while queue:
        # TODO: snapshot the current level size before consuming it.
        pass
    return levels


def lowest_common_ancestor(
    root: TreeNode | None, p: TreeNode, q: TreeNode
) -> TreeNode | None:
    """Find the LCA in a binary tree (not necessarily a BST)."""
    # TODO: define the recursive base cases and combine left/right results.
    pass


def number_of_islands(grid: list[list[str]]) -> int:
    """Count four-directionally connected components of '1' cells."""
    # TODO: scan cells and run DFS/BFS from each unvisited land cell.
    pass


# Discuss recursive stack depth, iterative alternatives, visited marking, an
# empty grid, a one-node tree, p == q, and nodes missing from the tree.
