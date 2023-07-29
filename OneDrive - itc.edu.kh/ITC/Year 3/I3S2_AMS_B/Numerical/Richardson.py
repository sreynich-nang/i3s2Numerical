from collections.abc import Callable
import numpy as np
import pandas as pd

def Richardson(f: Callable[[float], float],
               x: float,
               h: float,
               n: int = 9,
               rtol: float = 1.e-10
               ) -> tuple[float, pd.DataFrame]:
    N = n + 1
    D = np.full(shape=(N, N), fill_value=np.nan, dtype=np.float64)
    D[0,0] = 0.5 * (f(x + h) - f(x-h)) / h
    for i in range(1, N, 1):
        h = 0.5 * h
        D[i, 0] = 0.5 * (f(x + h) - f(x-h)) / h
        I = i + 1
        p = 1
        for j in range(1, I, 1):
            p = 4 * p
            D[i, j] = D[i, j-1] + (D[i, j-1] - D[i-1, j-1]) / (p-1)
        if abs(D[i, i] - D[i-1, i-1]) < rtol:
            break
    d = D[i, i]
    columns = [f'O(h^{2*(k+1)})' for k in range(0, I, 1)]
    D = pd.DataFrame(data=D[:I, :I], columns=columns)
    return (d, D)

if __name__ == '__main__':

    import math

    pd.options.display.width = 1000
    pd.options.display.float_format = '{:.10f}'.format
    
    def f(x): return math.log(1+x)
    
    d, D = Richardson(f=f, x=0, h=0.1)
    # d, D = Richardson(f=exp, x=0, h=0.1)
    print(f'd = {d:.10f}')
    print(D)