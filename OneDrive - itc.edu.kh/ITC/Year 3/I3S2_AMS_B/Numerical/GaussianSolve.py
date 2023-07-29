import numpy as np
from GaussianElimination import GaussianElimination
from BackwardSubstitution import BackwardSubstitution

def GaussianSolve(a: np.ndarray,
                  b: np.ndarray
                 ) -> np.ndarray:
    u, c = GaussianElimination(a=a, b=b)
    x = BackwardSubstitution(a=u, b=c)
    return x
# ---------------------------------------------------
if __name__ == '__main__':
    a = np.array([[2,-3,1],
                  [3,2,-5],
                  [2,4,-1]], dtype=np.float64)
    b = np.array([3,-9,-5], dtype=np.float64) 
    x = GaussianSolve(a=a, b=b)
    print(x)