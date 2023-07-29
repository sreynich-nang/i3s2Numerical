import numpy as np
from DoolittleLDLtDecomposition import DoolittleLDLtDecomposition
from FowardSubstitution import ForwardSubstitution
from BackwardSubstitution import BackwardSubstitution

def DoolittleLDLtSolve (a: np.ndarray,
                        b: np.ndarray,
                        info: bool=False,
                        ) -> np.ndarray:
    l, d, lt = DoolittleLDLtDecomposition(a=a)
    z = ForwardSubstitution(a=l, b=b)
    y = z/d
    x = BackwardSubstitution(a=lt, b=y)
    if info:
        print(a)
        print(b)
        
        print(l)
        print(d)
        print(lt)

        print(z)
        print(y)
        print(x)
    return x
'''
    We have matrix A and B
    >>> print(a)
    >>> print(b)
    Decompose A = LDL^T 
        Sole the equation of AX = B
        Since A = LDL^T 
        => AX = B <=>LDL^T X = B
    >>> print(l)
    >>> print(d)
    >>> print(lt)

    Let Z = DL^TX 
        => LZ = B, solve for Z
        We get DL^TX = Z
    >>> print(z)
    Let Y = L^TX 
        => DY = Z, solve for Y
    >>> print(y)
    Since Y = L^TX solve for X
    >>> print(x)
'''
if __name__ == '__main__':
    a = np.array(object = [[2,4,-2,4,-2],
                           [4,9,-2,7,-2],
                           [-2,-2,8,-2,4],
                           [4,7,-2,18,-8],
                           [-2,-2,4,-8,14]],
                  dtype = np.float64)
    b = np.array(object=[2,8,8,1,-4],
                 dtype=np.float64)
    x = DoolittleLDLtSolve(a=a, b=b, info=True)