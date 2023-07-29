from math import cos, sin, pi
def Newton(f, fp, p0, TOL = 1e-10, N=100):
    print(f'i={0:2d},p={p0:0.16f}, f(p)={f(p0):0.16f}')
    for i in range(0, N, 1):
        p = p0 - f(p0) / fp(p0)
        print(f'i={i+1:2d}, p={p:0.16f}, f(p)={f(p):0.16f}')
        if(abs (f(p))< TOL):
            return p
        else:
            p0= p
    return None
def f(x): return cos(x) - x
def fp(x): return -sin(x) - 1
p0 = pi/4
p = Newton(f=f, fp= fp, p0= p0, TOL = 1e-16)
print(p)

# -------------------
# def newton_method(f, x_0, tol):
#   """
#   Finds the root of the function f using the Newton method.

#   Args:
#     f: The function to find the root of.
#     x_0: The initial guess of the root.
#     tol: The desired accuracy.

#   Returns:
#     The approximate root of f.
#   """

#   while abs(f(x_0)) > tol:
#     x_1 = x_0 - f(x_0) / f(x_0)
#     x_0 = x_1
#   return x_1

# if __name__ == "__main__":
#     import math 
#     def f(x): 
#         return math.cos(x)-x
#         # return (math.exp(x)-2*x-2)
#         # return x**2 - 2

#     # df = Bisection(f=f, x0=0, x1=math.pi/4, e=1.0e-16)
#     df = newton_method(f=f, x_0=math.pi/4, tol=0.0000000001)
#     print(df)
