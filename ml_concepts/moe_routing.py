"""
PRACTICE TASK: MIXTURE OF EXPERTS (MoE) ROUTING MECHANISM
---------------------------------------------------------
Mixture of Experts (MoE) layers (as in Mistral 8x7B or DeepSeek) substitute 
dense FFN layers with multiple parallel sparse "experts". A gating router 
projects token embeddings to choose the Top-K experts dynamically per token 
and computes softmax-scaled routing weights.

Implementations to write:
1. moe_route(x, W_gate, K):
   - Projects tokens X to experts using W_gate.
   - Selects the top-K expert indices.
   - Computes softmax over the top-K logits to generate the routing weights.
2. MoELayer forward pass:
   - Routes tokens to expert index list.
   - Passes tokens through the selected expert MLP projections.
   - Multiplies expert outputs by routing weights and sums them up.
"""

import numpy as np
from typing import List, Tuple

def moe_route(x: np.ndarray, W_gate: np.ndarray, K: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Computes top-K gating routing weights.
    
    x shape: (num_tokens, d_model)
    W_gate shape: (d_model, num_experts)
    K: number of experts to route each token to (usually 2)
    
    Returns:
      expert_indices: (num_tokens, K) - integer indices of the top-K experts.
      routing_weights: (num_tokens, K) - softmax-normalized weights for the top-K experts.
    """
    # 1. Compute logits: x @ W_gate -> shape (num_tokens, num_experts)
    # 2. Identify the top-K experts along the last axis.
    # 3. Apply softmax ONLY over the selected top-K logits (stable softmax!).
    #    g_i = exp(logit_i) / sum_{j in Top-K} exp(logit_j)
    
    # TODO: Implement this function
    pass

class ExpertMLP:
    def __init__(self, d_model: int, d_ff: int):
        # Dense linear projections (biases omitted)
        self.W_in = np.random.randn(d_model, d_ff) * 0.02
        self.W_out = np.random.randn(d_ff, d_model) * 0.02

    def forward(self, x: np.ndarray) -> np.ndarray:
        """
        Standard FFN pass: ReLU(x @ W_in) @ W_out
        x shape: (N, d_model) -> output shape: (N, d_model)
        """
        # TODO: Implement FFN forward pass
        pass

class MoELayer:
    def __init__(self, d_model: int, d_ff: int, num_experts: int, K: int):
        self.d_model = d_model
        self.num_experts = num_experts
        self.K = K
        
        # Gating projection weights
        self.W_gate = np.random.randn(d_model, num_experts) * 0.02
        # Initialize experts list
        self.experts = [ExpertMLP(d_model, d_ff) for _ in range(num_experts)]

    def forward(self, X: np.ndarray) -> np.ndarray:
        """
        Executes the MoE layer forward pass.
        
        X shape: (batch_size, seq_len, d_model)
        
        Steps:
        1. Flatten input to (num_tokens, d_model) where num_tokens = batch_size * seq_len.
        2. Run moe_route to get (num_tokens, K) expert indices and weights.
        3. Pass each token through its assigned experts.
           Hint: To optimize, group tokens by their assigned expert to batch the FFN passes, 
           or process sequentially if implementing by hand.
        4. Weight expert outputs by routing weights and aggregate.
        5. Reshape back to (batch_size, seq_len, d_model).
        """
        batch_size, seq_len, d_model = X.shape
        num_tokens = batch_size * seq_len
        x_flat = X.reshape(num_tokens, d_model)
        
        # TODO: Implement this method
        pass


# --- Verification Tests ---
if __name__ == "__main__":
    print("Testing MoE Routing...")
    # 2 tokens, 4 experts, d_model = 3
    x = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
    W_gate = np.array([
        [10.0, 5.0, 1.0, 0.0],
        [0.0,  5.0, 8.0, 1.0],
        [0.0,  0.0, 0.0, 0.0]
    ])
    
    # Token 0: x @ W_gate -> [10.0, 5.0, 1.0, 0.0]. Top 2: expert 0 (10.0), expert 1 (5.0).
    # Normalized weights: softmax([10.0, 5.0]) -> [exp(10)/(exp(10)+exp(5)), exp(5)/(exp(10)+exp(5))]
    # exp(5) relative to exp(10) is extremely small (~0.0067), so weights should be ~[0.993, 0.007].
    
    # Token 1: x @ W_gate -> [0.0, 5.0, 8.0, 1.0]. Top 2: expert 2 (8.0), expert 1 (5.0).
    # Normalized weights: softmax([8.0, 5.0]) -> [exp(8)/(exp(8)+exp(5)), exp(5)/(exp(8)+exp(5))]
    # ~[0.952, 0.048].
    
    indices, weights = moe_route(x, W_gate, K=2)
    
    assert np.array_equal(indices[0], [0, 1]), f"Expected indices [0, 1], got {indices[0]}"
    assert np.array_equal(indices[1], [2, 1]), f"Expected indices [2, 1], got {indices[1]}"
    assert np.isclose(weights[0, 0], 1.0, atol=0.01), f"Expected weight close to 1.0, got {weights[0, 0]}"
    print("MoE Routing passed!")

    print("Testing MoE Layer Forward Pass...")
    moe = MoELayer(d_model=6, d_ff=12, num_experts=4, K=2)
    X_input = np.random.randn(2, 3, 6) # Batch=2, Seq=3, Dim=6
    out = moe.forward(X_input)
    assert out.shape == (2, 3, 6), f"Expected shape (2, 3, 6), got {out.shape}"
    print("MoE Layer Forward Pass passed!")
    
    print("\nAll MoE verification tests passed (once you implement them)!")
