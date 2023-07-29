import numpy as np

def DoolittleDecomposition(a: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    n = a.shape[0]
    l = np.eye(n)
    u = a.copy()
    stop = n-1
    for k in range(0, stop, 1):
        start = k + 1
        for i in range(start, n, 1):
            r = u[i, k] / u[k, k]
            l[i, k] = r
            u[i, k] = 0
            for j in range(start, n, 1):
                u[i, j] = u[i, j] - r*u[k, j]
    return (l, u)

if __name__ == '__main__':
    a = np.array(object=[[2,-1,0,0,0],
                         [2,-3,2,0,0],
                         [0,4,-7,-3,0],
                         [0,0,-9,-7,4],
                         [0,0,0,-4,-7]], dtype=np.float64)
    l, u = DoolittleDecomposition(a=a)
    print(f'a = {a}')
    print(f'l = {l}')
    print(f'u = {u}')
