from collections.abc import Callable
import numpy as np

def integrate_simpson(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    '''
    Compute the approximate value of the definite integral of f between a and b using 
    the Composite Simpson's rule with n subintervals.
    '''
    if (n % 2) != 0:
        raise ValueError("Number of subintervals must be even for Composite Simpson's rule")
    h = (b-a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return h/3 * (y[0] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-1:2]) + y[n])

def CompositeSimpson(f: Callable[[float], float], a:float, b:float, n:int) -> float:
    h = (b-a) / n
    f0 = f(a) + f(b)
    f1 = 0
    f2 = 0
    x = a
    for i in range(1, n, 1):
        x = x + h
        if(i%2 == 0):
            f2 = f2 + f(x)
        else:
            f1 = f1+f(x)
    A = h*(f0+2*f2+4*f1)/3
    return A
# ---------------------------------------------------
import math
if __name__ == '__main__':
    def f(x): return math.exp(math.cos(x))
    # I = CompositeSimpson(f=f, a=0, b=1, n=10)
    I = CompositeSimpson(f=f, a=0, b=1, n=6)
    print(I)