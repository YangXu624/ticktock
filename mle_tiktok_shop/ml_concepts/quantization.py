"""
PRACTICE TASK: SYMMETRIC & ASYMMETRIC 8-BIT LINEAR QUANTIZATION
----------------------------------------------------------------
Model compression is critical for high-throughput streaming inference and 
on-device AI. Linear quantization maps 32-bit floats to 8-bit integers (int8), 
reducing memory bandwidth and accelerating execution.

Implementations to write:
1. symmetric_quantize_int8(x):
   - Computes scale S = max(|x|) / 127.
   - Quantizes x: q = clip(round(x / S), -128, 127).
   - Returns quantized array q (int8) and scale S.
2. symmetric_dequantize_int8(q, S):
   - Restores values to float32: x_approx = q * S.
3. asymmetric_quantize_int8(x):
   - Computes scale S = (max(x) - min(x)) / 255.
   - Computes zero point Z = round(-min(x) / S) - 128 (shifted for int8 range [-128, 127]).
   - Clamps Z to [-128, 127].
   - Quantizes x: q = clip(round(x / S) + Z, -128, 127).
   - Returns quantized array q (int8), scale S, and zero point Z.
4. asymmetric_dequantize_int8(q, S, Z):
   - Restores values to float32: x_approx = (q - Z) * S.
"""

import numpy as np
from typing import Tuple

def symmetric_quantize_int8(x: np.ndarray) -> Tuple[np.ndarray, float]:
    """
    Quantizes a float32 array to int8 using symmetric quantization.
    Symmetric range: [-127, 127] or [-128, 127]. Use [-127, 127] to prevent negative overflow bounds.
    
    Formula:
      S = max(abs(x)) / 127
      q = round(x / S)
      q = clip(q, -127, 127)
    """
    # TODO: Implement this function
    pass

def symmetric_dequantize_int8(q: np.ndarray, S: float) -> np.ndarray:
    """
    Dequantizes symmetric int8 array back to float32.
    
    Formula: x_approx = q * S
    """
    # TODO: Implement this function
    pass

def asymmetric_quantize_int8(x: np.ndarray) -> Tuple[np.ndarray, float, int]:
    """
    Quantizes a float32 array to int8 using asymmetric quantization.
    Target range is [-128, 127] (total range of 255 values).
    
    Formula:
      S = (max(x) - min(x)) / 255
      Z = round(-min(x) / S) - 128
      Z = clip(Z, -128, 127)
      q = round(x / S) + Z
      q = clip(q, -128, 127)
    """
    # TODO: Implement this function
    pass

def asymmetric_dequantize_int8(q: np.ndarray, S: float, Z: int) -> np.ndarray:
    """
    Dequantizes asymmetric int8 array back to float32.
    
    Formula: x_approx = (q - Z) * S
    """
    # TODO: Implement this function
    pass


# --- Verification Tests ---
if __name__ == "__main__":
    print("Testing Symmetric Quantization...")
    x = np.array([-10.0, -5.0, 0.0, 5.0, 10.0], dtype=np.float32)
    # Symmetric: max(abs(x)) = 10.0. S = 10.0 / 127.
    q, S = symmetric_quantize_int8(x)
    assert q.dtype == np.int8 or q.dtype == np.intc
    assert np.allclose(q, [-127, -64, 0, 64, 127], atol=1), f"Expected ~[-127, -64, 0, 64, 127], got {q}"
    
    x_approx = symmetric_dequantize_int8(q, S)
    # Reconstructed values should be very close to original (within quantization noise)
    assert np.allclose(x, x_approx, atol=0.1), f"Dequantization error too high: {x_approx}"
    print("Symmetric Quantization passed!")

    print("Testing Asymmetric Quantization...")
    # Asymmetrical values (shifted positive)
    x_asym = np.array([0.0, 1.0, 2.0, 3.0, 4.0], dtype=np.float32)
    q_asym, S_asym, Z_asym = asymmetric_quantize_int8(x_asym)
    
    assert q_asym.dtype == np.int8 or q_asym.dtype == np.intc
    x_approx_asym = asymmetric_dequantize_int8(q_asym, S_asym, Z_asym)
    assert np.allclose(x_asym, x_approx_asym, atol=0.05), f"Dequantization error too high: {x_approx_asym}"
    print("Asymmetric Quantization passed!")

    print("\nAll Quantization verification tests passed (once you implement them)!")
