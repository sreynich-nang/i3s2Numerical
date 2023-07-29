def composite_midpoint(f, a, b, n):
  """
  Integrates the function `f` over the interval `[a, b]` using the composite midpoint method.

  Args:
    f: A function that takes a number as input and returns a number.
    a: The lower bound of the interval.
    b: The upper bound of the interval.
    n: The number of subintervals.

  Returns:
    The approximation of the integral of `f` over `[a, b]`.
  """

  # Calculate the step size.
  h = (b - a) / n

  # Create a list of the midpoints of the subintervals.
  midpoints = [a + i * h for i in range(n)]

  # Evaluate the function at the midpoints.
  values = [f(x) for x in midpoints]

  # Calculate the sum of the function values.
  sum_of_values = sum(values)

  # Return the approximation of the integral.
  return (h * sum_of_values) / 2
import math
if __name__ == '__main__':
    def f(x): return math.exp(math.sin(x))
    # I = CompositeSimpson(f=f, a=0, b=1, n=10)
    I = composite_midpoint(f=f, a=0, b=1, n=6)
    print(I)