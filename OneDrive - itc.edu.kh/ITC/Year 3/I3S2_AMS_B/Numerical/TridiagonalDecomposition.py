import numpy as np
def TridiagonalDecomposition(c: np.ndarray,
                             d: np.ndarray,
                             e: np.ndarray
                            ) -> tuple[np.ndarray, 
                                np.ndarray, 
                                np.ndarray]:
    _c = c.copy()
    _d = d.copy()
    n = len(_d)
    for k in range(1, n, 1):
        lam = _c[k-1] / _d[k-1]
        _d[k] -= lam * e[k-1]
        _c[k-1] = lam
    return (_c, _d, e)

if __name__ == '__main__':
    from FowardSubstitution import ForwardSubstitution
    from BackwardSubstitution import BackwardSubstitution

    c = np.full(shape=4, fill_value=-1, dtype=np.float64) 
    e = np.full(shape=4, fill_value=-1, dtype=np.float64) 
    d = np.full(shape=5, fill_value=2, dtype=np.float64) 
    b = np.array(object=[5,-5,4,-5,5], dtype=np.float64)
    cp, dp, ep = TridiagonalDecomposition(c=c, d=d, e=e)
    a = np.diag(v=c, k=1) + np.diag(v=d, k=0) + np.diag(v=e, k=1)
    print(a)
    print(cp)
    print(dp)
    print(ep)

    l = np.diag(v=cp, k=-1) + np.eye(N=5, dtype=np.float64)
    print(l)

    u = np.diag(v=dp, k=0) + np.diag(v=ep, k=1)
    print(u)
    
    y = ForwardSubstitution(a=l, b=b)
    x = BackwardSubstitution(a=u, b=y)
    print(x)

