from math import cos, pi, sin

table = []
def false_position(f, a, b, tol):
  """
  Finds the root of the function f using the method of false position.

  Args:
    f: The function to find the root of.
    a: The lower bound of the interval.
    b: The upper bound of the interval.
    tol: The desired accuracy.

  Returns:
    The approximate root of f.
  """


  while abs(b - a) > tol:
    c = (a * f(b) - b * f(a)) / (f(b) - f(a))
    table.append([a, b, c, f(c)])
    if f(c) == 0:
      return c
    elif f(a) * f(c) < 0:
      b = c
    else:
      a = c
  return (a + b) / 2


def main():
  f = lambda x: 1-(x*sin(x))
  a = 1
  b = 2
  tol = 1e-6

  root = false_position(f, a, b, tol)

  print("The root is", root)

  for row in table:
    print(row)

# a, b, c, f(c)
if __name__ == "__main__":
  main()

