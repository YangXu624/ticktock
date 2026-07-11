# TikTok MLE Intern Prep: Data Structures, Algorithms & ML Concepts

This roadmap is designed to guide your preparation for the TikTok MLE Intern interview. It is structured sequentially around your travel timeline and contains practice templates for both core DSA and low-level ML concepts.

---

## Workspace Directory Structure

All practice templates are organized logically in this workspace. Each file contains a top-level prompt, functional stubs, typing hints, and test assertions to verify your implementation.

```
/Users/yangxu/code/tiktok/
├── plan.md                       # This roadmap and curriculum
├── matrix/
│   └── matrix_ops.py             # Slicing, transposing, matmul, Rotate Image, Spiral Matrix
├── tree/
│   ├── binary_tree.py            # Node class, Max Depth, Serialization & Deserialization
│   └── trie.py                   # Trie Node, Insert, Search, StartsWith, Tokenizer
├── heap/
│   └── heap_ops.py               # Custom Min-Heap, K-Closest Points, Top-K Freq Elements
├── hashmap/
│   └── sparse_vector.py          # Sparse Vector representation, Vocab builder, Dot Product
├── algorithms/
│   ├── binary_search.py          # Binary Search, split thresholds, Quantiles
│   ├── graph_traversal.py        # DFS/BFS: Number of Islands, Topological Sort (DAG parsing)
│   ├── sliding_window.py         # Two pointers, rolling metrics, window tokenization
│   └── kway_merge.py             # K-Way Merge for sorting multi-stream predictions
└── ml_concepts/
    ├── attention.py              # Scaled Dot-Product & Multi-Head Attention (MHA)
    ├── clustering.py             # KMeans Clustering algorithm from scratch
    ├── optimization.py           # ADAM Optimizer step updates and momentum
    ├── evaluation.py             # Recall@K and NDCG metrics computation
    ├── moe_routing.py            # MoE Gating/Routing (top-k experts, softmax weight mapping)
    └── quantization.py           # Symmetric and Asymmetric 8-bit linear quantization
```

---

## 1. Core Data Structures & Algorithms
Refere to the respective directories (`matrix/`, `tree/`, `heap/`, `hashmap/`, `algorithms/`) to practice fundamental computer science concepts. Use the test blocks in each file to verify your logic.

---

## 2. Low-Level ML Concept Implementations
These templates test your mathematical understanding of model architectures, optimization, and evaluation metrics by implementing them from scratch using base Python or NumPy.

### Target Files:
1.  **[ml_concepts/attention.py](file:///Users/yangxu/code/tiktok/ml_concepts/attention.py)**
    *   *Concept:* Transformer scaled dot-product attention: $\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$.
    *   *MHA:* Splitting projections, executing head dot-products, and concatenating outputs.
2.  **[ml_concepts/clustering.py](file:///Users/yangxu/code/tiktok/ml_concepts/clustering.py)**
    *   *Concept:* KMeans clustering (initialization, distance calculation, centroid updating).
3.  **[ml_concepts/optimization.py](file:///Users/yangxu/code/tiktok/ml_concepts/optimization.py)**
    *   *Concept:* ADAM optimizer update formulation. Tracks first/second moments with bias correction:
        $m_t = \beta_1 m_{t-1} + (1-\beta_1) g_t$, $v_t = \beta_2 v_{t-1} + (1-\beta_2) g_t^2$.
4.  **[ml_concepts/evaluation.py](file:///Users/yangxu/code/tiktok/ml_concepts/evaluation.py)**
    *   *Concept:* Recommendation metrics: Recall@K and NDCG (Normalized Discounted Cumulative Gain) for binary relevance.
5.  **[ml_concepts/moe_routing.py](file:///Users/yangxu/code/tiktok/ml_concepts/moe_routing.py)**
    *   *Concept:* Mistral MoE gating. Performs Top-K routing, software gating with softmax scaling, and routes token tokens to specialized expert MLPs.
6.  **[ml_concepts/quantization.py](file:///Users/yangxu/code/tiktok/ml_concepts/quantization.py)**
    *   *Concept:* Quantization-Aware Training basics. Implement linear symmetric and asymmetric int8 quantization:
        $q = \text{round}(x / S) + Z$.

---

## Mode of Operation (Mock Interviews)

1.  **Context-Aware Triggers:** Pull only from the active team track specified in the prompt.
2.  **No Fluff / Strict Persona:** Act as a senior technical bar-raiser. Lead directly with technical scenarios, code constraints, or math problems without filler praise.
3.  **Strict Hint Economy:** Point out logic flaws in test cases or ask structural questions; do not give away algorithms or solutions directly.
4.  **Deep Technical Evaluation:** Probe for mathematical formulations, matrix dimensions, hardware/memory constraints, and optimization trade-offs.
