"""
PRACTICE TASK: ADAM OPTIMIZER STEP UPDATES
------------------------------------------
Optimization algorithms are the engine behind backpropagation. Recommender and 
deep model architectures rely heavily on ADAM (Adaptive Moment Estimation) due 
to its robust handling of sparse gradients. You must memorize its bias-correction 
equations and step calculations.

Implementations to write:
1. AdamOptimizer Class:
   - step(params, grads): Updates weights/parameters in-place based on the 
     gradient step computation.
"""

import numpy as np
from typing import Dict

class AdamOptimizer:
    def __init__(self, lr: float = 0.001, beta1: float = 0.9, beta2: float = 0.999, eps: float = 1e-8):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.eps = eps
        
        # State tracking dictionaries: parameter_id -> moment_array
        self.m: Dict[str, np.ndarray] = {}  # 1st moment vector
        self.v: Dict[str, np.ndarray] = {}  # 2nd moment vector
        self.t = 0                           # Time step

    def step(self, params: Dict[str, np.ndarray], grads: Dict[str, np.ndarray]) -> None:
        """
        Performs one step of parameter updates.
        Modifies params dictionary IN-PLACE.
        
        Parameters:
          params: Dict containing string parameter keys (e.g. "W1", "b1") and weight arrays.
          grads: Dict containing matching parameter keys and gradient arrays.
          
        Adam Equations:
          1. Increment time step: t += 1
          2. Update biased first moment: m = beta1 * m_prev + (1 - beta1) * grad
          3. Update biased second raw moment: v = beta2 * v_prev + (1 - beta2) * (grad^2)
          4. Compute bias-corrected first moment: m_hat = m / (1 - beta1^t)
          5. Compute bias-corrected second raw moment: v_hat = v / (1 - beta2^t)
          6. Update parameters: param = param - (lr / (sqrt(v_hat) + eps)) * m_hat
        """
        self.t += 1
        
        for key in params.keys():
            if key not in self.m:
                self.m[key] = np.zeros_like(params[key])
                self.v[key] = np.zeros_like(params[key])
                
            # TODO: Implement parameter update equations for each parameter key
            pass


# --- Verification Tests ---
if __name__ == "__main__":
    print("Testing Adam Optimizer updates...")
    optimizer = AdamOptimizer(lr=0.1, beta1=0.9, beta2=0.99)
    
    # 1D weight and matching gradient
    params = {"W": np.array([10.0, 5.0])}
    grads = {"W": np.array([2.0, -1.0])}
    
    # Run step 1
    optimizer.step(params, grads)
    # Check if weights decreased/increased in the direction of the negative gradient
    # Since grad[0] > 0, W[0] should decrease (less than 10.0)
    # Since grad[1] < 0, W[1] should increase (greater than 5.0)
    
    print(f"Updated weights after Step 1: {params['W']}")
    assert params["W"][0] < 10.0, "Weight W[0] did not decrease"
    assert params["W"][1] > 5.0, "Weight W[1] did not increase"
    
    # Save values to check Step 2 updates
    step1_w = params["W"].copy()
    
    # Run step 2
    optimizer.step(params, grads)
    print(f"Updated weights after Step 2: {params['W']}")
    assert params["W"][0] < step1_w[0], "Weight W[0] did not decrease in step 2"
    
    print("Adam Optimizer passed!")
    
    print("\nAll Optimization verification tests passed (once you implement them)!")
