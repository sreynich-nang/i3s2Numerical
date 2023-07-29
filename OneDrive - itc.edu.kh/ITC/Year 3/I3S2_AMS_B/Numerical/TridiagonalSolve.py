import numpy as np
from TridiagonalDecomposition import TridiagonalDecomposition

def TridiagonalSolve(c: np.ndarray,
                     d: np.ndarray,
                     e: np.ndarray,
                     b: np.ndarray) -> np.ndarray:
    _c, _d, _e = TridiagonalDecomposition(c=c, d=d, e=e)
    n = len(b)
    y = np.full_like(a=b, fill_value=np.nan, dtype=np.float64)
    x = np.full_like(a=b, fill_value=np.nan, dtype=np.float64)
    y[0] = b[0]
    for i in range(1, n, 1):
        y[i] = b[i] - _c[i-1] * y[i-1]
    x[n-1] = y[n-1]/_d[n-1]
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - _e[i]*x[i+1])/_d[i]
    return x
if __name__ == '__main__':
    c = np.full(shape=4, fill_value=-1, dtype=np.float64)
    e = np.full(shape=4, fill_value=-1, dtype=np.float64)
    d = np.full(shape=5, fill_value=2, dtype=np.float64)
    b = np.array(object=[5,-5,4,-5,5], dtype=np.float64)
    x = TridiagonalSolve(c=c, d=d, e=e, b=b)
    print(x)
