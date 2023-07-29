import numpy as np
import pandas as pd

def RalstonMethod(a: float,
                  b: float,
                  n: int,
                  alpha: float,
                  f: callable) -> pd.DataFrame:
    h = (b-a) / n
    t = np.linspace(start=a, stop=b, num=n+1, dtype=np.float64)
    w = np.full_like(a=t, fill_value=np.nan, dtype=np.float64)
    b1, b2, c2, a21 = 1/4, 3/4, 2/3, 2/3
    w[0] = alpha
    for i in range(0, n, 1):
        k1 = f(t[i], w[i])
        k2 = f(t[i] + c2*h, w[i] + a21*k1*h)
        w[i+1] = w[i] + h*(b1*k1 + b2*k2)
    df = pd.DataFrame(data={'t': t, 'w': w}, dtype=np.float64)
    return df
if __name__ == '__main__':
    import math
    def f(t: float, y: float) -> float:
        return 2*y/t + (t**2) * math.exp(t)
    a,b = 1,2
    alpha = 0.0
    n = 20
    df = RalstonMethod(a=a, b=b, alpha=alpha, n=n, f=f)
    def y(t: float) -> float:
        return (t**3 * math.exp(t) - 2)/(t**2 -2)
    df['y'] = df['t'].apply(func=y)
    df['|y-w|'] = abs(df['y'] - df['w'])
    print(df)