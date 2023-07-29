import pandas as pd 
# from EvaluatePolynomial import EvaluatePolynomail
# from PolyEval import PloyEval
def PolyEval(a,x, d):
    N = len(a)
    n = N-1
    #p = a[n]
    #ddp = 0
    #dp = 0
    v = [0]*(d+1)
    v[0] = a[n]
    for k in range(1, N,1):
        for l in range(d, 0, -1):
            v[l] = l*v[l-1] + x*v[l]
        v[0] = a[n-k] + x*v[0]
    return v 
# if __name__=="__main__":
#     # TODO: Evaluate P(x) and P'(x) at x = 2
#     # where P(x) = 1+2x + 3x^2 + 4x^3
#     # P'(x) = 2 + 6x +12x^2
#     # and P''(x) = 6 + 24x
    
#     a = [1, 2, 3, 4]
#     x = 2
#     val = PolyEval(a=a, x=x, d=4)
#     print(a)
#     print(x)
#     print(val)
##########################################################
def Muller(a, p0, p1, p2, float = 1.0e-10, maxiter= 100):
    fp0 = PolyEval(a=a, x=p0, d=0)[0]
    fp1 = PolyEval(a=a, x=p1, d=0)[0]
    fp2 = PolyEval(a=a, x=p2, d=0)[0]
    h1 = p1 -p0
    h2 = p2 - p1
    d1 = (fp1 - fp0) / h1
    d2 = (fp2 - fp1) / h2
    d = (d2 - d1) / (h2 + h1)
    df = pd.DataFrame(data={"p": [p0, p1, p2], "f(p)": [fp0, fp1, fp2]})
    i = 3
    condition = True
    while condition:
        b = d2 + h2 * d
        fp2 = PolyEval(a=a, x=p2, d=0)[0]
        D = (b**2 - 4*fp2*d)**(1/2)
        if abs(b-D) < abs(b + D):
            E = b + D
        else:
            E = b - D
        h = -2 * fp2 / E
        p = p2 + h 
        fp = PolyEval(a=a, x=p, d=0)[0]
        df.loc[i,:] = {"p": p, "f(p)": fp}
        condition = abs(h) > float
        if condition:
            p0 = p1
            p1 = p2
            p2 = p
            h1 = p1 - p0
            h2 = p2 - p1
            fp0 = PolyEval(a=a, x=p0, d=0)[0]
            fp1 = PolyEval(a=a, x=p1, d=0)[0]
            fp2 = PolyEval(a=a, x=p2, d=0)[0]
            d1 = (fp1 - fp0) / h1
            d2 = (fp2 - fp1) / h2
            d = (d2 - d1) / (h2 + h1)
            i = i + 1
    if i >= maxiter:
        print(f"Method failed after {maxiter} iterations")
   #else:
    #   print(f"\n Root= {p:.2f}")
    return (p, df)
if __name__ == "__main__":
    a = [1,-9,34,-20,-261,949,-1014]
    p, df = Muller(a=a, p0=0, p1=1, p2=2)
    print(f"p={p:.10f}")
    print(df)

# -----------------------------------
# from math import pow
# table = []
# def muller_method(f, x_0, x_1, x_2, tol):
#   """
#   Finds the root of the function f using Muller's method.

#   Args:
#     f: The function to find the root of.
#     x_0: The initial guess of the root.
#     x_1: The next guess of the root.
#     x_2: The third guess of the root.
#     tol: The desired accuracy.

#   Returns:
#     The approximate root of f.
#   """

  
#   while abs(x_2 - x_1) > tol:
#     p = (x_1 * f(x_2) - x_2 * f(x_1)) / (f(x_2) - f(x_1))
#     q = (x_2 * f(x_0) - x_0 * f(x_2)) / (f(x_2) - f(x_0))
#     r = (x_0 * f(x_1) - x_1 * f(x_0)) / (f(x_1) - f(x_0))
#     x_3 = -(p + q + r) / 2
#     table.append([x_0, x_1, x_2, x_3, f(x_3)])
#     x_0 = x_1
#     x_1 = x_2
#     x_2 = x_3
#   return x_2


# def main():
#   f = lambda x: (pow(x,4) - 3*pow(x,3) + pow(x,2) + x + 1)

#   x_0 = -0.5
#   x_1 = 0
#   x_2 = 0.5
#   tol = 1e-10

#   root = muller_method(f, x_0, x_1, x_2, tol)

#   print("The root is", root)

#   for row in table:
#     print(row)


# if __name__ == "__main__":
#   main()

