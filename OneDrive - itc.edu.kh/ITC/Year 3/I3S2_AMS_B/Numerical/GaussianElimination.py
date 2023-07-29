import numpy as np

def GaussianElimination(a: np.ndarray,
                        b: np.ndarray
                        ) -> tuple[np.ndarray,
                                   np.ndarray]:
    _a = a.copy()
    _b = b.copy()
    n = _a.shape[0]
    stop = n - 1
    for k in range(0, stop, 1):
        start = k + 1
        for i in range(start, n, 1):
            r = _a[i,k] / _a[k,k]
            _a[i,k] = 0
            for j in range(start,n,1):
                _a[i,j] = _a[i,j] - r * _a[k,j]
            _b[i] = _b[i] - r * _b[k]
    return (_a, _b)
# ---------------------------------------------
if __name__ == '__main__':
    a = np.array([[2,-3,1],
                [3,2,-5],
                [2,4,-1]], dtype=np.float64)
    b = np.array([3,-9,-5], dtype=np.float64)

    u, c = GaussianElimination(a=a, b=b)
    d = {'a': a, 'b': b, 'u': u, 'c': c}

    for k in d.keys():
        print(k)
        print(d[k])