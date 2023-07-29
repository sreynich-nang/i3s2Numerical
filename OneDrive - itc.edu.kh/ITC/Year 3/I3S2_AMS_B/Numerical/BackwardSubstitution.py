import numpy as np
from GaussianElimination import GaussianElimination
def BackwardSubstitution(a: np.ndarray,
                         b: np.ndarray
                         ) -> np.ndarray:
    N = a.shape[0]
    x = np.zeros_like(b)
    x[N-1] = b[N-1] / a[N-1, N-1]
    start_i = N - 2
    for i in range(start_i, -1, -1):
        x[i] = b[i]
        start_j = i+1
        for j in range(start_j, N, 1):
            x[i] -= a[i,j] * x[j]
        x[i] /= a[i,i]
    return x
# ---------------------------------------------------
if __name__ == '__main__':
    a = np.array([[2,-3,1],
                [3,2,-5],
                [2,4,-1]], dtype=np.float64)
    b = np.array([3,-9,-5], dtype=np.float64) 
    u, c = GaussianElimination(a=a, b=b)
    x = BackwardSubstitution(a=u, b=c)
    print(x)