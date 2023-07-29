# from collections.abc import Callable

# def GaussianQuadrature(f: Callable[[float], float], a: float, b: float, n: int = 5) -> float:
#     """
#   Integrates the function `f` over the interval `[a, b]` using Gaussian quadrature with `n` points.

#   Args:
#     f: The function to integrate.
#     a: The lower bound of the interval.
#     b: The upper bound of the interval.
#     n: The number of quadrature points.

#   Returns:
#     The approximation of the integral of `f` over `[a, b]`.
#   """
#     cs = {
#         1:  [2.000000000],
#         2:  [1.0000000000, 1.0000000000],
#         3:  [0.8888888889, 0.5555555556, 0.5555555556],
#         4:  [0.6521451549, 0.6521451549, 0.3478548451, 0.3478548451],
#         5:  [0.5688888889, 0.4786286705, 0.4786286705, 0.2369268851, 0.2369268851]
#     }
#     xs = {
#         1:  [0.0000000000],
#         2:  [0.5773502692, -0.5773502692],
#         3:  [0.0000000000,-0.7745966692, 0.7745966692],
#         4:  [0.3399810436, -0.3399810436, -0.8611363116, 0.8611363116],
#         5:  [0.0000000000, 0.5384693101, -0.5384693101, -0.9061798459, 0.9061798459]
#     }
#     A = 0.0
#     a0 = b + a
#     a1 = b - a


#     for (c, x) in zip(cs[n], xs[n]):
#         A = A + c * f(0.5 * (a0 + a1 * x))
#     A = A * 0.5 * a1
#     return A

# if __name__ == '__main__':
#     from math import exp
#     def f(x: float) -> float: return exp(-x**2)
#     A = GaussianQuadrature(f, a=0, b=1, n=5)
#     print(f'A = {A:.12f}')
# -------------------------------------------
import numpy as np
from math import exp
def gaussian_quadrature(f, a, b, n):
  """
  Integrates the function `f` over the interval `[a, b]` using Gaussian quadrature with `n` points.

  Args:
    f: The function to integrate.
    a: The lower bound of the interval.
    b: The upper bound of the interval.
    n: The number of quadrature points.

  Returns:
    The approximation of the integral of `f` over `[a, b]`.
  """

  # Compute the quadrature points and weights.
  x = np.linspace(a, b, n)
  w = np.zeros(n)
  for i in range(n):
    w[i] = 2 * (1 - x[i]**2)**(n - 1)

  # Evaluate the function at the quadrature points.
  y = f(x)

  # Return the approximation of the integral.
  return np.sum(w * y)

# def f(x: float) -> float: return exp(-x**2)
import numpy as np

def f(x):
  return np.exp(-x**2)

a = -1
b = 1
n = 5

integral = gaussian_quadrature(f, a, b, n)

print(integral)


# integral = gaussian_quadrature(f, a, b, n)

# print(integral)
