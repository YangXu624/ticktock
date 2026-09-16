"""
PRACTICE TASK: EVALUATION METRICS (RECALL@K & NDCG@K)
------------------------------------------------------
Recommendation systems must be evaluated using metrics that account for candidate 
ranking order. Recall@K measures coverage, while NDCG@K (Normalized Discounted 
Cumulative Gain) rewards placing relevant items at the top of the feed.

Implementations to write:
1. recall_at_k(recs, ground_truth, K): Calculates Recall@K for a list of recommended 
   items and a set of actual user interactions.
2. ndcg_at_k(recs, ground_truth, K): Calculates NDCG@K using binary relevance values 
   (1 if recommended item is in ground truth, 0 otherwise).
"""

from typing import List, Set
import math

def recall_at_k(recs: List[str], ground_truth: Set[str], K: int) -> float:
    """
    Computes Recall@K.
    
    Formula: (Count of relevant recommended items in Top K) / (Total relevant items)
    If ground_truth is empty, return 0.0.
    """
    # TODO: Implement this function
    pass

def ndcg_at_k(recs: List[str], ground_truth: Set[str], K: int) -> float:
    """
    Computes NDCG@K (Normalized Discounted Cumulative Gain) for binary relevance.
    
    Binary relevance: rel_i = 1 if recs[i] in ground_truth else 0.
    
    Formula:
      DCG@K = sum_{i=1}^{K} (rel_i / log2(i + 1))  -- (using 1-based indexing for i, so index 0 maps to i=1)
      IDCG@K = sum_{i=1}^{min(K, len(ground_truth))} (1 / log2(i + 1))
      NDCG@K = DCG@K / IDCG@K
      
    If IDCG@K is 0 (no ground truth matches possible), return 0.0.
    """
    # TODO: Implement this function
    pass


# --- Verification Tests ---
if __name__ == "__main__":
    print("Testing Recall@K...")
    recs = ["item_A", "item_B", "item_C", "item_D", "item_E"]
    ground_truth = {"item_B", "item_D", "item_Z"} # 3 total items, B and D are recommendations
    
    # Recall@3: Top 3 is ["item_A", "item_B", "item_C"]. Intersection with ground truth is {"item_B"} (1 item).
    # Recall@3 = 1 / 3 = 0.3333...
    rec_3 = recall_at_k(recs, ground_truth, K=3)
    assert math.isclose(rec_3, 1/3, rel_tol=1e-5), f"Expected 0.3333, got {rec_3}"
    
    # Recall@5: Top 5 contains B and D (2 items). Recall@5 = 2 / 3 = 0.6666...
    rec_5 = recall_at_k(recs, ground_truth, K=5)
    assert math.isclose(rec_5, 2/3, rel_tol=1e-5), f"Expected 0.6666, got {rec_5}"
    print("Recall@K passed!")

    print("Testing NDCG@K...")
    # Recommendations: ["item_A", "item_B"] (A is irrelevant, B is relevant)
    # ground_truth = {"item_B"}
    # K = 2.
    # relevance: rel_1 (index 0) = 0 (item_A), rel_2 (index 1) = 1 (item_B)
    # DCG@2 = 0 / log2(2) + 1 / log2(3) = 0 + 1 / 1.58496 = 0.63093
    # IDCG@2: min(2, 1) = 1 hit. Best possible: put B at index 0.
    # IDCG@2 = 1 / log2(2) = 1.0
    # NDCG@2 = 0.63093 / 1.0 = 0.63093
    r = ["item_A", "item_B"]
    gt = {"item_B"}
    ndcg = ndcg_at_k(r, gt, K=2)
    expected_ndcg = 1.0 / math.log2(3)
    assert math.isclose(ndcg, expected_ndcg, rel_tol=1e-5), f"Expected {expected_ndcg}, got {ndcg}"
    
    # Ideal sorting: ["item_B", "item_A"]. NDCG should be 1.0
    ndcg_ideal = ndcg_at_k(["item_B", "item_A"], gt, K=2)
    assert math.isclose(ndcg_ideal, 1.0, rel_tol=1e-5), f"Expected 1.0, got {ndcg_ideal}"
    print("NDCG@K passed!")
    
    print("\nAll Evaluation verification tests passed (once you implement them)!")
