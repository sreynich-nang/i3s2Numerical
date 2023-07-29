import pandas as pd
import math

def Bisection (f, x0, x1, e):
    """
  Finds the root of the function f using the bisection method.

  Args:
    f: The function to find the root of.
    x0: The lower bound of the interval.
    x1: The upper bound of the interval.
    e: The desired accuracy.

  Returns:
    The approximate root of f.
  """
    step = 1
    condition = True
    df = pd.DataFrame(data = {'x': [x0], 'f(x)':[f(x0)]})
    while condition:
    # for i in range(10):
        x2 = (x0+x1)/2
        print(f'Step:{step}, x2 = {x2:0.16f} and f(x2) = {f(x2): 0.16f}')
        
        if f(x0) * f(x2) < 0:
            x1=x2
        else:
            x0=x2

        df.loc[step] = {'x':x0, 'f(x)':f(x0)}
        step += 1
        # condition = abs(f(x2)) > e
        condition = abs(f(x2)) < 0.0001
    print(f'\nRequied Root is: {x2:0.16f}')
    return df

if __name__ == "__main__":
    def f(x): 
        # return math.cos(x)-x
        # return (math.exp(x)-2*x-2)
        return x**2 - 2

    # df = Bisection(f=f, x0=0, x1=math.pi/4, e=1.0e-16)
    df = Bisection(f=f, x0=0, x1=2, e=0.0001)
    print(df)
    # print(df.style.format({'x':'{:.16f}','f(x)':'{:.16f}'}).to_latex())
