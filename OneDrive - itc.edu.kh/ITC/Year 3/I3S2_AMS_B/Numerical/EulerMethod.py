import pandas as pd
import numpy as np
pd.options.display.float_format = '{:.8f}'.format
def EulerMethod(a: float,
                b: float,
                n: int,
                alpha: float,
                f: callable) -> pd.DataFrame:
    h = (b-a) / n
    t = np.linspace(start=a, stop=b, num=n+1, dtype=np.float64)
    w = np.full_like(a=t, fill_value=np.nan, dtype=np.float64)
    w[0] = alpha
    for i in range(0, n, 1):
        w[i+1] = w[i] + h*f(t[i], w[i])
    df = pd.DataFrame(data={'t': t, 'w': w}, dtype=np.float64)
    return df
if __name__ == '__main__':
    def f(t: float, y: float) -> float:
        return y-t**2+1
    (a, b) = (0,2)
    alpha = 0.5
    n = 10
    df = EulerMethod(a=a, b=b, alpha=alpha, n=n, f=f)

    def y(t: float) -> float:
        return (t+1)**2 - np.exp(t)/2
    df['y'] = df['t'].apply(func=y)
    df['|y-w|'] = abs(df['y'] - df['w'])

    print(df)
