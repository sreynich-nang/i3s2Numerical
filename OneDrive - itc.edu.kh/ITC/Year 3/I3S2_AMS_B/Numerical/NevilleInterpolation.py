import pandas as pd
def NevilleInterpolation(x: list[float], y: list[float], x0: float) -> tuple[float, pd.DataFrame]:
    N = len(x)
    n = N - 1
    import numpy as np
    Q = np.empty(shape=(N, N))
    Q.fill(np.nan)
    Q[:,0] = y
    for i in range(1, N, 1):
        I = i + 1
        for j in range(1, I, 1):
            Q[i, j] = ((x0 - x[i-j]) * Q[i,j-1] - (x0-x[i]) * Q[i-1,j-1]) / (x[i]-x[i-j])
        p = Q[n,n]
        Q = pd.DataFrame(data=Q)
        Q.insert(loc=0, column="x", value=x)
        return(p,Q)

if __name__ == "__main__":
    x = [1,2,3]
    y = [2,5,10]
    x0 = 1.5
    p, Q = NevilleInterpolation(x=x, y=y, x0=x0)
    print(p)
    print(Q)

