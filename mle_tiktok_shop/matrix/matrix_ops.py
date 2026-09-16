"""
PRACTICE TASK: MATRIX & GRID OPERATIONS FOR ML
----------------------------------------------
In Machine Learning, matrices represent image tensors, weight configurations, 
and intermediate activation grids. Complete the implementations below WITHOUT
using external libraries like NumPy.

Implementations to write:
1. transpose(matrix): Transposes an M x N matrix in-place (if square) or returns a new transposed matrix.
2. matmul(A, B): Computes matrix multiplication of matrix A (size M x K) and matrix B (size K x N).
3. rotate_image(matrix): Rotates an N x N matrix (image) 90 degrees clockwise IN-PLACE.
4. spiral_order(matrix): Traverses an M x N grid in spiral order and returns a 1D list.
"""

from typing import List

def transpose(matrix: List[List[float]]) -> List[List[float]]:
    """
    Transposes the given M x N matrix.
    If the matrix is square (M == N), do the transpose IN-PLACE and return it.
    If the matrix is rectangular (M != N), return a new transposed matrix.
    
    Time Complexity target: O(M * N)
    Space Complexity target: O(1) for square (in-place), O(M * N) for rectangular.
    """
    # TODO: Implement this function
    pass

def matmul(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """
    Computes the matrix multiplication C = A x B.
    A is of shape M x K, B is of shape K x N. Output C is of shape M x N.
    Raise a ValueError if the dimensions do not match (K columns of A != K rows of B).
    
    Time Complexity target: O(M * N * K)
    Space Complexity target: O(M * N) for the output matrix.
    """
    # TODO: Implement this function
    pass

def rotate_image(matrix: List[List[int]]) -> None:
    """
    Rotates the N x N square grid 90 degrees clockwise IN-PLACE.
    Do not allocate another 2D matrix or return anything.
    
    Time Complexity target: O(N^2)
    Space Complexity target: O(1)
    """
    # TODO: Implement this function
    pass

def spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    Returns all elements of the M x N matrix in spiral order.
    
    Time Complexity target: O(M * N)
    Space Complexity target: O(1) (excluding the output list)
    """
    # TODO: Implement this function
    pass


# --- Verification Tests ---
if __name__ == "__main__":
    print("Testing Transpose...")
    # Test square transpose
    sq_mat = [[1, 2], [3, 4]]
    transpose(sq_mat)
    assert sq_mat == [[1, 3], [2, 4]], f"Expected [[1, 3], [2, 4]], got {sq_mat}"
    
    # Test rect transpose
    rect_mat = [[1, 2, 3], [4, 5, 6]]
    rect_t = transpose(rect_mat)
    assert rect_t == [[1, 4], [2, 5], [3, 6]], f"Expected [[1, 4], [2, 5], [3, 6]], got {rect_t}"
    print("Transpose passed!")

    print("Testing Matrix Multiplication...")
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    C = matmul(A, B)
    assert C == [[19, 22], [43, 50]], f"Expected [[19, 22], [43, 50]], got {C}"
    print("Matmul passed!")

    print("Testing Rotate Image (Clockwise)...")
    img = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate_image(img)
    assert img == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ], f"Expected rotated image, got {img}"
    print("Rotate Image passed!")

    print("Testing Spiral Order...")
    sp_mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    sp_out = spiral_order(sp_mat)
    assert sp_out == [1, 2, 3, 6, 9, 8, 7, 4, 5], f"Expected [1, 2, 3, 6, 9, 8, 7, 4, 5], got {sp_out}"
    print("Spiral Order passed!")
    
    print("\nAll matrix verification tests passed (once you implement them)!")
