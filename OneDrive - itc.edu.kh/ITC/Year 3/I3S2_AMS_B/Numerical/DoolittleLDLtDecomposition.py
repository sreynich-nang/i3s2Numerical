import numpy as np
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
def DoolittleLDLtDecomposition(a: np.ndarray) -> tuple[np.ndarray,
                                                       np.ndarray,
                                                       np.ndarray]:
    N = a.shape[0]
    l = np.eye(N=N)
    d = np.zeros(shape=N)
    d[0] = a[0,0]
    l[1,0] = a[1,0] / d[0]
    d[1] = a[1,1] - d[0] * l[1,0]**2
    for i in range(2,N,1):
        l[i, 0] = a[i,0] / d[0]
        for j in range(1, i, 1):
            l[i,j] = a[i,j]
            for k in range(0,j):
                l[i,j] = l[i,j] - d[k] * l[i,k] * l[j,k]
            l[i,j] = l[i,j] / d[j]
        d[i] = a[i,i]
        for k in range(0, i):
            d[i] = d[i] - d[k] * l[i,k]**2
    return l,d,l.transpose() 

if __name__ == "__main__":
    a = np.array(object = [[2,4,-2,4,-2],
                           [4,9,-2,7,-2],
                           [-2,-2,8,-2,4],
                           [4,7,-2,18,-8],
                           [-2,-2,4,-8,14]],
                  dtype = np.float64)
    b = np.array(object=[2,8,8,1,-4],
                 dtype=np.float64)
    l,d,lt = DoolittleLDLtDecomposition(a=a)
    d = np.diag(v=d, k=0)
    print(l)
    print(d)
    print(lt) 