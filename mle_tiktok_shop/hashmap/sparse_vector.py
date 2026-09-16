"""
PRACTICE TASK: HASH MAPS & SPARSE VECTOR REPRESENTATION
-------------------------------------------------------
In web-scale recommendation systems, features (like user history or search tags)
are extremely high-dimensional but sparse. Storing them as dense vectors is
highly inefficient. Instead, we represent them as Sparse Vectors (index-to-value maps).

Implementations to write:
1. SparseVector Class:
   - __init__(nums): Initializes a sparse representation of a list of floats, storing only non-zero values.
   - dot_product(other): Computes the dot product of two SparseVector instances efficiently by iterating 
     over the vector with fewer non-zero entries.
2. build_vocabulary(corpus): Build a token-to-index mapping from a list of text documents.
3. get_sparse_bow(document, vocab): Create a sparse frequency vector (BoW) matching vocabulary tokens.
"""

from typing import List, Dict

class SparseVector:
    def __init__(self, nums: List[float]):
        """
        Stores non-zero elements of the input array in a dictionary: index -> value.
        
        Space Complexity target: O(NZ) where NZ is number of non-zero elements.
        """
        self.data: Dict[int, float] = {}
        # TODO: Implement this initialization
        pass

    def dot_product(self, other: 'SparseVector') -> float:
        """
        Computes the dot product with another SparseVector.
        Optimize runtime by iterating over the smaller sparse dictionary.
        
        Time Complexity target: O(min(N1, N2)) where N1 and N2 are non-zero counts of vectors.
        Space Complexity target: O(1)
        """
        # TODO: Implement this function
        pass


def build_vocabulary(corpus: List[str]) -> Dict[str, int]:
    """
    Given a list of document strings, tokenizes them by splitting on whitespace,
    and returns a vocabulary map mapping unique words to unique integer indices.
    
    Example:
      corpus = ["hello world", "hello tiktok"]
      returns: {"hello": 0, "world": 1, "tiktok": 2} (order of IDs doesn't matter)
    """
    # TODO: Implement this function
    pass


def get_sparse_bow(document: str, vocab: Dict[str, int]) -> SparseVector:
    """
    Converts a text document into a Bag-of-Words (BoW) SparseVector using
    word frequencies mapping to the corresponding vocabulary IDs.
    Words not in vocab are ignored.
    
    Example:
      document = "hello tiktok tiktok"
      vocab = {"hello": 0, "world": 1, "tiktok": 2}
      Underlying dense: [1, 0, 2]
      Returns: SparseVector with data: {0: 1.0, 2: 2.0}
    """
    # TODO: Implement this function
    pass


# --- Verification Tests ---
if __name__ == "__main__":
    print("Testing SparseVector Dot Product...")
    v1 = SparseVector([1.0, 0.0, 0.0, 2.0, 0.0, 3.0])
    v2 = SparseVector([0.0, 0.0, 5.0, 4.0, 0.0, 0.0])
    # Non-zeros: v1 -> {0: 1.0, 3: 2.0, 5: 3.0}, v2 -> {2: 5.0, 3: 4.0}
    # Dot product: 2.0 * 4.0 = 8.0
    try:
        res = v1.dot_product(v2)
        assert res == 8.0, f"Expected 8.0, got {res}"
        print("SparseVector dot product passed!")
    except Exception as e:
        print(f"Dot product verification failed or not implemented yet: {e}")

    print("Testing Vocabulary & BoW Builder...")
    corpus = ["tiktok shop", "global shop e-commerce"]
    try:
        vocab = build_vocabulary(corpus)
        assert len(vocab) == 4, f"Expected vocabulary of size 4, got {len(vocab)}"
        
        doc = "shop shop tiktok"
        sparse_bow = get_sparse_bow(doc, vocab)
        
        # Verify term frequencies are correct
        # shop -> 2, tiktok -> 1.
        shop_idx = vocab["shop"]
        tiktok_idx = vocab["tiktok"]
        assert sparse_bow.data[shop_idx] == 2.0
        assert sparse_bow.data[tiktok_idx] == 1.0
        print("Vocabulary and BoW builders passed!")
    except Exception as e:
        print(f"Vocab/BoW verification failed or not implemented yet: {e}")

    print("\nAll Hash Map verification tests passed (once you implement them)!")
