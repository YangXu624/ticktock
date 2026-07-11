"""
PRACTICE TASK: ATTENTION MECHANICS (SCALED DOT-PRODUCT & MULTI-HEAD ATTENTION)
----------------------------------------------------------------------------
Attention mechanisms are the backbone of modern Transformers (BERT, GPT, ViT).
In MLE loops, you must be able to write the exact tensor transformations and 
matrix operations for attention, including causal masking and multi-head splits.

Implementations to write:
1. stable_softmax(x): Computes softmax along the last dimension, stabilized 
   against overflow using x - max(x).
2. scaled_dot_product_attention(Q, K, V, mask=None):
   - Computes Q @ K.T / sqrt(d_k).
   - Applies optional boolean mask (sets True/1 positions to -inf before softmax).
   - Computes output = softmax(scores) @ V.
3. MultiHeadAttention (MHA) forward pass:
   - Project inputs X into Q, K, V tensors.
   - Split into multiple heads.
   - Run scaled dot-product attention per head.
   - Concatenate head outputs and project back to original dimension.
"""

import numpy as np

def stable_softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    """
    Computes numerical stable softmax along the specified axis.
    
    Formula: exp(x_i - max(x)) / sum(exp(x_j - max(x)))
    """
    # TODO: Implement this function
    pass

def scaled_dot_product_attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray, mask: np.ndarray = None) -> tuple[np.ndarray, np.ndarray]:
    """
    Computes scaled dot-product attention.
    
    Q shape: (..., seq_len_q, d_k)
    K shape: (..., seq_len_k, d_k)
    V shape: (..., seq_len_k, d_v)
    mask shape: (..., seq_len_q, seq_len_k) - boolean array where True indicates positions to MASK OUT.
    
    Returns:
      output: (..., seq_len_q, d_v)
      attention_weights: (..., seq_len_q, seq_len_k)
    """
    # TODO: Implement this function
    pass

class MultiHeadAttention:
    def __init__(self, d_model: int, num_heads: int):
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        
        # Linear projection weights (biases omitted for simplicity)
        self.W_q = np.random.randn(d_model, d_model) * 0.02
        self.W_k = np.random.randn(d_model, d_model) * 0.02
        self.W_v = np.random.randn(d_model, d_model) * 0.02
        self.W_o = np.random.randn(d_model, d_model) * 0.02

    def forward(self, X: np.ndarray, mask: np.ndarray = None) -> np.ndarray:
        """
        Runs the MHA forward pass.
        
        X shape: (batch_size, seq_len, d_model)
        mask shape: (batch_size, seq_len, seq_len)
        
        Returns:
          output shape: (batch_size, seq_len, d_model)
        """
        batch_size, seq_len, d_model = X.shape
        assert d_model == self.d_model
        
        # 1. Project to Q, K, V using self.W_q, self.W_k, self.W_v
        # 2. Reshape & transpose to split into heads: (batch_size, num_heads, seq_len, d_k)
        # 3. Apply scaled_dot_product_attention (broadcasting mask appropriately)
        # 4. Transpose & reshape back: (batch_size, seq_len, d_model)
        # 5. Apply output projection self.W_o
        
        # TODO: Implement this method
        pass


# --- Verification Tests ---
if __name__ == "__main__":
    print("Testing stable_softmax...")
    x = np.array([[1.0, 2.0, 1000.0]]) # Large value to test numerical stability
    sm = stable_softmax(x)
    assert np.allclose(sm[:, 2], 1.0, atol=1e-5), f"Softmax unstable, got {sm}"
    print("stable_softmax passed!")

    print("Testing scaled_dot_product_attention...")
    # 1 query, 2 keys/values
    Q = np.array([[1.0, 0.0]]) # seq_len=1, d_k=2
    K = np.array([[1.0, 0.0], [0.0, 1.0]]) # seq_len=2, d_k=2
    V = np.array([[10.0], [20.0]]) # seq_len=2, d_v=1
    
    # Q @ K^T = [[1, 0]] @ [[1, 0], [0, 1]] = [[1, 0]]
    # Scaling factor = sqrt(2) approx 1.414. Scores: [[1/1.414, 0]] = [[0.707, 0.0]]
    # Softmax(scores) = softmax([[0.707, 0.0]]) = [[0.67, 0.33]]
    # Output = [[0.67 * 10 + 0.33 * 20]] = [[13.3]]
    out, weights = scaled_dot_product_attention(Q, K, V)
    assert np.allclose(out, [[13.3]], atol=0.1), f"Expected around [[13.3]], got {out}"
    print("scaled_dot_product_attention passed!")

    print("Testing MHA forward pass...")
    mha = MultiHeadAttention(d_model=8, num_heads=2)
    X = np.random.randn(2, 5, 8) # Batch=2, Seq=5, Dim=8
    out = mha.forward(X)
    assert out.shape == (2, 5, 8), f"Expected (2, 5, 8), got {out.shape}"
    print("MHA forward pass passed!")
    
    print("\nAll Attention verification tests passed (once you implement them)!")
