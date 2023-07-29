import numpy as np
import pandas as pd


def NewtonDividedDifference(x: list[float], y: list[float]) -> tuple[list[float], pd.DataFrame]:
    """
    TODO
    ----------
    Newton form from power form using Newton Devided Difference

    Parameters
    ----------
    1) `x` : `list[float]`
        list of pairwise distinct floating values
    2) `y` : `list[float]`
        list of floating values corresponding to `x`

    Return
    ----------
    1) `b` : `list[float]`
        coefficients `[b_0,b_1,...,b_n]` of `b_0+b_1 (x-x_0)+...+b_n (x-x_0)(x-x_1)...(x-x_{n-1})`
    2) `F` : `pd.DataFrame`
        `pd.DataFrame` storing Newton Forward-Divided Difference table
    Example
    ----------
    >>> import NumericalAnalysis as na
    >>> na.pd.options.display.float_format = "{:.11f}".format
    >>> x = [1, 2, 3]
    >>> y = [2, 5, 10]
    >>> b, F = na.NewtonDividedDifference(x=x, y=y)
    >>> print(f"Newton Form: {b}")
    >>> print(F)
        Newton Form: [2, 3.0, 1.0]
           x   0             1             2
        0  1   2           NaN           NaN
        1  2   5 3.00000000000           NaN
        2  3  10 5.00000000000 1.00000000000
    """
    N = len(x)
    F = np.empty(shape=(N, N))
    F.fill(np.nan)
    F[:, 0] = y
    for i in range(1, N, 1):
        I = i + 1
        for j in range(1, I, 1):
            F[i, j] = (F[i, j - 1] - F[i - 1, j - 1]) / (x[i] - x[i - j])
    b = [F[i, i] for i in range(N)]
    F = pd.DataFrame(data=F)
    F.insert(loc=0, column="x", value=x)
    return (b, F)

if __name__ == '__main__':
    x = [2,3,-1,1,-3,-2]
    y = [1,-23,-367,-248,-110,-55]
    b, F = NewtonDividedDifference(x=x, y=y)
    print(f"Newton Form: {b}")
    print(F)
