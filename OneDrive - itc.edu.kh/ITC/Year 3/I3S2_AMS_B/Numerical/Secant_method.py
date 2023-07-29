import pandas as pd
from math import cos, pi

def Secant(f, x0, x1, e, N=100):
    """
  Finds the root of the function f using the bisection method.

  Args:
    f: The function to find the root of.
    x0: The lower bound of the interval.
    x1: The upper bound of the interval.
    e: The desired accuracy.
    N: The number of maximum of iterations.

  Returns:
    The approximate root of f.
    """
    step = 1
    condition = True
    df = pd.DataFrame(data = {'x0':[x0], 'x1':[x1], 'f(x1)':f(x1)})
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break
        
        x2 = x0 - (x1 - x0) * f(x0) / (f(x1)- f(x0))
        print(f'step: {step}, x2 = {x2: 0.16f} and f(x2) = {f(x2):0.16f}')
        x0 = x1
        x1 = x2
        df.loc[step] = pd.Series(data={'x0': x0, 'x1':x1, 'f(x1)': f(x1)})
        step = step + 1
        
        if step > N:
            print('Not Conveergent!')
            break
            
        condition = abs(f(x2)) > e
    print(f'\n Required root is: %{x2:0.16f}')
    return df

if __name__=="__main__":
    import math
    def f(x):
        return math.log(x, math.base) - math.exp(x) + 3
    p0 = 0.5
    p1 = math.pi / 4
    df = Secant(f=f, x0=p0, x1=p1, e=1.0e-16, N=20)
    print(df.style.format({'x': '{:.16f}', 'x1': '{:.16f}', 'f(x1)': '{:.16f}'}).to_latex())

# ----------------------------
# def Secant(f, p0, p1, TOL = 1e-10, N=100):
#     stop = N + 1
#     for i in range(2, stop, 1):
#         q0 = f(p0)
#         q1 = f(p1)
#         p = p1 -q1 * (p1 - p0) / (q1 - q0)
#         print(f'i = {i:2d}, p0 = {p0:.16f}, p1 = {p1:.16f}, p = {p:.16f}, f(p) = {f(p):.16f}')
#         if (abs(p - p1)< TOL):
#             return p
#         p0 = p1
#         p1 = p
#     return None

# def f(x): return cos(x) - x

# p = Secant(f=f, p0=0, p1=pi/4, TOL=1e-16)