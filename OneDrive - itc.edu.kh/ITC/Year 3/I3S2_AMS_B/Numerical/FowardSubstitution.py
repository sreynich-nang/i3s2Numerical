import numpy as np

def ForwardSubstitution(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    N = a.shape[0]
    x = np.zeros_like(b)
    x[0] = b[0] / a[0, 0]
    for i in range(0, N, 1):
        x[i] = b[i]
        for j in range(0, i, 1):
            x[i] -= a[i, j] * x[j]
        x[i] /= a[i, i]
    return x

if __name__ == '__main__':
    a = np.array(object=[[2, 0, 0, 0],
                         [-1, 3, 0, 0],
                         [-2, 2, -3, 0],
                         [1, -2, 2, 4],], dtype = np.float64)
    b  = np.array(object=[-4, 8, 5, 8], dtype = np.float64)
    x = ForwardSubstitution(a=a, b=b)
    d = {'a': a, 'b': b, 'x': x}
    for key in d.keys():
        print(f'{key} = {d[key]}')

