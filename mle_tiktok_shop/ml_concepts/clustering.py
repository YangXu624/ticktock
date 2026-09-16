"""
PRACTICE TASK: K-MEANS CLUSTERING FROM SCRATCH
----------------------------------------------
Clustering is highly tested in recommendation loops to group similar users, 
categorize items into latent topics, or initialize vector quantization codes.
You must be able to code the exact iterative steps of KMeans.

Implementations to write:
1. euclidean_distance(x, y): Returns the Euclidean distance between two vectors.
2. KMeans class:
   - fit(X): Runs the iterations (centroids selection, assignment, update) 
     until convergence or max_iter is met.
   - predict(X): Assigns new data points to the nearest centroid.
"""

import numpy as np

def euclidean_distance(x: np.ndarray, y: np.ndarray) -> float:
    """
    Computes Euclidean distance: sqrt(sum((x_i - y_i)^2)).
    """
    # TODO: Implement this function
    pass

class KMeans:
    def __init__(self, K: int = 3, max_iter: int = 100, tol: float = 1e-4):
        self.K = K
        self.max_iter = max_iter
        self.tol = tol
        self.centroids: np.ndarray = None

    def fit(self, X: np.ndarray) -> 'KMeans':
        """
        Fits KMeans to the dataset X.
        
        X shape: (N, D) where N is number of samples, D is dimension of features.
        
        Steps:
        1. Initialize centroids randomly by selecting K unique points from X.
        2. Loop for max_iter:
           a. Assign each point in X to its nearest centroid.
           b. Recompute centroids as the mean of all points assigned to them.
           c. Check if centroid movements are below tol (convergence check). If so, break.
        """
        N, D = X.shape
        # TODO: Implement this method
        pass

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predicts nearest cluster index for each sample in X.
        
        X shape: (M, D)
        Returns:
          labels: (M,) integer array containing cluster index (0 to K-1).
        """
        # TODO: Implement this method
        pass


# --- Verification Tests ---
if __name__ == "__main__":
    print("Testing Euclidean Distance...")
    a = np.array([0, 0])
    b = np.array([3, 4])
    dist = euclidean_distance(a, b)
    assert np.isclose(dist, 5.0), f"Expected 5.0, got {dist}"
    print("Euclidean Distance passed!")

    print("Testing KMeans Fit/Predict...")
    # Generate 3 separable clusters in 2D
    np.random.seed(42)
    c1 = np.random.randn(20, 2) + np.array([5, 5])
    c2 = np.random.randn(20, 2) + np.array([-5, -5])
    c3 = np.random.randn(20, 2) + np.array([5, -5])
    X = np.vstack([c1, c2, c3])
    
    kmeans = KMeans(K=3, max_iter=50)
    kmeans.fit(X)
    
    # Predict clusters
    labels = kmeans.predict(X)
    
    # Centroids should be close to the original centers [5, 5], [-5, -5], [5, -5]
    centers = sorted([list(np.round(c)) for c in kmeans.centroids])
    expected_centers = sorted([[5.0, 5.0], [-5.0, -5.0], [5.0, -5.0]])
    
    # Check if centroids are reasonably close (due to random seed, should align)
    for c, ec in zip(centers, expected_centers):
        assert np.allclose(c, ec, atol=1.5), f"Centroid mismatch: expected {ec}, got {c}"
        
    print("KMeans Fit/Predict passed!")
    
    print("\nAll Clustering verification tests passed (once you implement them)!")
