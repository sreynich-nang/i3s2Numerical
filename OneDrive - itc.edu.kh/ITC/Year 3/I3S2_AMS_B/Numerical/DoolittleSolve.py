import numpy as np
from FowardSubstitution import ForwardSubstitution
from BackwardSubstitution import BackwardSubstitution
from DoolittleDecomposition import DoolittleDecomposition

def DoolittleSolve(a: np.ndarray,
                  b: np.ndarray
                  ) -> np.ndarray:
    l, u = DoolittleDecomposition(a)
    y = ForwardSubstitution(a=l, b=b)
    x = BackwardSubstitution(a=u, b=y)
    return x
'''
    To solve AX = B using Doolittle Decopostion,
    where A and B are as follow
    1. First, we decopose A into UL, 
       L and U are as follow: '
       >>> print(l)
       >>> print(u)
    Hence, the equation becomes LUX = B
       Denote that Y = UX. Then LY = B
    2. Next, we solve LY = B for Y using Forward Substitution
       >>> print(y)
    3. Finally, we solve UX = Y for X using Backward Substitution
       >>> print(x)
'''
# --------------------------------------------
# if __name__ == '__main__':
#     a = np.array([[2,-3,1],
#                   [3,2,-5],
#                   [2,4,-1]], dtype=np.float64)
#     b = np.array([3,-9,-5], dtype=np.float64) 
#     x = DoolittleSolve(a=a, b=b)
#     print(x)
# --------------------------------------------
if __name__ == '__main__':
    al = [2,4,-9,-4]
    ad = [2,-3,-7,-7,-7]
    au = [-1,2,-3,4]
    a = np.diag(v=al, k=-1) + np.diag(v=ad, k=0) + np.diag(v=au, k=1)
    print(a)

    b = np.array(object=[-5,-3,-1,7,5], dtype=np.float64)
    print(b)
    x = DoolittleSolve(a=a, b=b)
    print(x)
