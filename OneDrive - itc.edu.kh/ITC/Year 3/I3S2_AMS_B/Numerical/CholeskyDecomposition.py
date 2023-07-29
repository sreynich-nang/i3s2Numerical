import numpy as np

def CholeskyDecomposition (a:np.ndarray)-> tuple [np.ndarray, np.ndarray]:
    N=a.shape[0]
    l=np.zeros_like(a)
    l[0,0]=np.sqrt(a[0,0])
    l[1,0]=a[1,0] / l[0,0]
    l[1,1]=np.sqrt(a[1,1]-l[1,0]**2)
    for i in range(2,N,1):
        l[i,0]=a[i,0]/l[0,0]
        for j in range(1,i,1):
            l[i,j]=a[i,j]
            for k in range (0,j,1):
                l[i,j]=l[i,j]-l[i,k]*l[j,k]
            l[i,j]=l[i,j]/l[j,j]
        l[i,i]=a[i,i]
        for k in range(0,i,1):
            l[i,i]=l[i,i]-l[i,k]**2
        l[i,i]=np.sqrt(l[i,i])
    return l,l.transpose()
#     """
#     TODO
#     Performs Cholesky LU decomposition 'A = LL^T' on a matrix A.

#     Args:
#     a: A square matrix.

#     Returns:
#     l: The lower triangular matrix L of the Cholesky decomposition.
#     u: The upper triangular matrix U of the Cholesky decomposition which is the transpose of 'l'.
#     """

if __name__ == '__main__':
    a = np.array(object=[[2,4,-2,4,-2],
                         [4,9,-2,7,-2],
                         [-2,-2,8,-2,4],
                         [4,7,-2,18,-8],
                         [-2,-2,4,-8,14]],
                         dtype=np.float64)
    b = np.array(object=[2,8,8,1,-4],
                 dtype=np.float64)
    l, lt = CholeskyDecomposition(a=a)
    print(l)
    print(lt)
    print(l @ lt)
    print(a)
