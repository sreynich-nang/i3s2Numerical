import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Literal
from collections.abc import Callable

def RungeKutta4(f: Callable[[np.float64, np.float64], np.float64],
               t_span: np.ndarray,
               y_init: np.float64,
               n: int,
               method: Literal['Classic', 'ThreeEighth'] = 'Classic') -> pd.DataFrame:
    if method == 'Classic':
        c = np.array(object=[0, 1/2, 1/2, 1],
                    dtype=np.float64)
        a = np.array(object=[[0, 0, 0, 0],
                            [1/2, 0, 0, 0],
                            [0, 1/2, 0, 0],
                            [0, 0, 1, 0]], 
                    dtype=np.float64)
        b = np.array(object=[1/6, 1/3, 1/3, 1/6], 
                dtype=np.float64)
    elif method == 'ThreeEighth':
        c = np.array(object=[0, 1/3, 2/3, 1],
                    dtype=np.float64)
        a = np.array(object=[[0, 0, 0, 0],
                            [1/3, 0, 0, 0],
                            [-1/3, 1, 0, 0],
                            [1, -1, 1, 0]], 
                    dtype=np.float64)
        b = np.array(object=[1/8, 3/8, 3/8, 1/8], 
                dtype=np.float64)
    h = (t_span[1] - t_span[0]) / n
    t = np.linspace(start=t_span[0],
                    stop=t_span[1],
                    num=n+1,
                    dtype=np.float64)
    y = np.full_like(a=t, fill_value=np.nan,
                     dtype=np.float64)
    y[0] = y_init
    for i in range(0, n, 1):
        k0 = f(t[i], y[i])
        k1 = f(t[i] + c[1]*h, y[i] + (a[1,0]*k0)*h)
        k2 = f(t[i] + c[2]*h, y[i] + (a[2,0]*k0) + (a[2,1]*k1)*h)
        k3 = f(t[i] + c[3]*h, y[i] + (a[3,0]*k0) + (a[3,1]*k1) + (a[3,2]*k2)*h)
        y[i+1] = y[i] + h*(b[0]*k0 + b[1]*k1 + b[2]*k2 + b[3]*k3)
    df = pd.DataFrame(data={'t':t, 'y':y}, dtype=np.float64)
    return df
if __name__ == '__main__':
    def f(t: np.float64, y: np.float64) -> np.float64:
        return t**(-2)*(np.cos(t)-2*t*y)
    t_span = np.array(object=[1, 2], dtype=np.float64)
    y_init = 0.0
    n = 10
    
    methods = ['Classic', 'ThreeEighth']
    for method in methods:
        df = RungeKutta4(f=f, t_span=t_span, y_init=y_init, n=n, method=method)

        def y(t: np.float64) -> np.float64:
            return t**(-2)*(np.sin(t)-np.sin(1))
        df.loc[:, 'exact'] = df.loc[:, 't'].apply(func=y)
        df.loc[:, 'error'] = abs(df.loc[:, 'y']-df.loc[:,'exact'])
        pd.options.display.float_format = '{:.10f}'.format
        print(df)
        fig = plt.figure(figsize=(8,8))
        ax = fig.add_subplot(1,1,1)
        ax.plot(df.loc[:,'t'], df.loc[:,'y'], 'o')
        ax.plot(df.loc[:,'t'], df.loc[:,'exact'], '-')
        plt.show()
