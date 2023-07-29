import numpy as np
from CholeskyDecomposition import CholeskyDecomposition
from FowardSubstitution import ForwardSubstitution
from BackwardSubstitution import BackwardSubstitution

'''
    Solve AX = B using LLt-Cholesky Decomposition
    Decompose A int LLt
    >>> print(l)
    >>> print(lt)
    1st, solve Ly = B using Forward Substitution
    >>> print(y)
    2nd, solve LtX = y using Backward Substitution
    >>> print(X)
'''
def CholeskySolve(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    l, lt = CholeskyDecomposition(a=a)
    y = ForwardSubstitution(a=l, b=b)
    x = BackwardSubstitution(a=lt, b=y)
    return x
if __name__ == '__main__':
    a = np.array(object=[[2,4,-2,4,-2],
                         [4,9,-2,7,-2],
                         [-2,-2,8,-2,4],
                         [4,7,-2,18,-8],
                         [-2,-2,4,-8,14]],
                         dtype=np.float64)
    b = np.array(object=[2,8,8,1,-4],
                 dtype=np.float64)
    x = CholeskySolve(a=a, b=b)
    print(a)
    print(b)
    print(x)
    print(a @ x)
