import math

def f(x):
    return math.sin(x)

def simpson_adaptive_quadrature(a, b, tol):
    h = b - a
    c = (a + b) / 2.0
    d = (a + c) / 2.0
    e = (c + b) / 2.0
    S = (h / 6.0) * (f(a) + 4.0 * f(c) + f(b))
    S1 = (h / 12.0) * (f(a) + 4.0 * f(d) + 2.0 * f(c) + 4.0 * f(e) + f(b))
    if abs(S1 - S) < tol:
        return S1 + (S1 - S) / 15.0
    else:
        return simpson_adaptive_quadrature(a, c, tol/2.0) + simpson_adaptive_quadrature(c, b, tol/2.0)

a = 0.0
b = math.pi/2
tol = 1e-6
approximation = simpson_adaptive_quadrature(a, b, tol)
print(approximation)
