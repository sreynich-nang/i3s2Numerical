import numpy as np
from GaussianElimination import GaussianElimination

def DiagonalSolve(a: np.ndarray,
                  b: np.ndarray
                 ) -> np.ndarray:
    N = len(b)
    x = np.zeros_like(b)
    for i in range(0, N, 1):
        x[i] = b[i] / a[i, i]
    return x
# ---------------------------------------------------
if __name__ == '__main__':
    a = np.array([[2,-3,1],
                  [3,2,-5],
                  [2,4,-1]], dtype=np.float64)
    b = np.array([3,-9,-5], dtype=np.float64) 
    u, c = GaussianElimination(a=a, b=b)
    x = DiagonalSolve(a=u, b=c)
    print(x)