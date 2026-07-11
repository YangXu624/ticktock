"""
PRACTICE TASK: BINARY TREE OPERATIONS FOR ML
---------------------------------------------
Decision trees and recursive partitions (like KD-Trees) are fundamental in ML.
Interviews frequently test your ability to traverse trees, check hyperparameters 
(like depth constraints), and serialize model models to files.

Implementations to write:
1. max_depth(root): Returns the maximum depth of a binary tree.
2. serialize(root): Serializes a binary tree into a single string representation.
3. deserialize(data): Restores a serialized string back into a binary tree.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root: Optional[TreeNode]) -> int:
    """
    Returns the maximum depth of the binary tree.
    An empty tree has depth 0.
    
    Time Complexity target: O(N) where N is number of nodes.
    Space Complexity target: O(H) where H is tree height (recursion stack).
    """
    # TODO: Implement this function
    pass

def serialize(root: Optional[TreeNode]) -> str:
    """
    Encodes a tree to a single string.
    Use any traversal pattern (e.g., Pre-order DFS with delimiters and '#' representing Null).
    
    Time Complexity target: O(N)
    Space Complexity target: O(N)
    """
    # TODO: Implement this function
    pass

def deserialize(data: str) -> Optional[TreeNode]:
    """
    Decodes the encoded string data back to a TreeNode tree.
    
    Time Complexity target: O(N)
    Space Complexity target: O(N)
    """
    # TODO: Implement this function
    pass


# --- Verification Tests ---
if __name__ == "__main__":
    # Construct a test tree:
    #      1
    #     / \
    #    2   3
    #       / \
    #      4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    print("Testing max_depth...")
    depth = max_depth(root)
    assert depth == 3, f"Expected depth 3, got {depth}"
    print("max_depth passed!")

    print("Testing serialization & deserialization...")
    serialized = serialize(root)
    # The exact string depends on traversal, but checking round-trip ensures correctness
    print(f"Serialized tree format: {serialized}")
    
    deserialized_root = deserialize(serialized)
    assert deserialized_root is not None, "Deserialization returned None"
    assert deserialized_root.val == 1
    assert deserialized_root.left.val == 2
    assert deserialized_root.right.val == 3
    assert deserialized_root.right.left.val == 4
    assert deserialized_root.right.right.val == 5
    assert max_depth(deserialized_root) == 3
    print("Serialization & Deserialization passed!")

    print("\nAll binary tree verification tests passed (once you implement them)!")
