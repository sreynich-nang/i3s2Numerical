from collections.abc import Callable
from typing import Literal
from typing import Optional
import pandas as pd
import numpy as np

def RungeKutta2(f: Callable[[float, float], float],
                t_span: list,
                y_init: float, 
                n: int,
                method: Optional[Literal['Midpoint', 'Heun', 'Rolston']] = 'Ralston'
                ) -> pd.DataFrame:
    (a, b) = t_span
    h = (b-a) / n
    t = np.linspace(start=a, stop=b, num=n+1, dtype=np.float64)
    y = np.full_like(a=t, fill_value=np.nan, dtype=np.float64)
    y[0] = y_init
    if method == 'Midpoint':
        c = np.array(object=[0, 1/2], dtype=np.float64)
        a = np.array(object=[[0, 0],
                            [1/2, 0]], 
                            dtype=np.float64)
        b = np.array(object=[0, 1], dtype=np.float64)
    elif method == 'Midpoint':
        c = np.array(object=[0, 1], dtype=np.float64)
        a = np.array(object=[[0, 0],
                            [1, 0]], 
                            dtype=np.float64)
        b = np.array(object=[0, 1], dtype=np.float64)
    else:
        c = np.array(object=[0, 2/3], dtype=np.float64)
        a = np.array(object=[[0, 0],
                            [2/3, 0]], 
                            dtype=np.float64)
        b = np.array(object=[1/4, 3/4], dtype=np.float64)
    for i in range(0, n, 1):
        k0 = f(t[i], y[i])
        k1 = f(t[i] + c[1]*h, y[i]+(a[1,0]*k0)*h)
        y[i+1] = y[i] + h*(b[0]*k0 + b[1]*k1)
    df = pd.DataFrame(data={'t': t, 'y': y})
    return df
if __name__ == '__main__':
    import math
    # Check TP05, ex4
    def f(t:float, y: float) -> float: 
        return 2.0 * (1-t*y)/(t**2.0 +1) # y' of ex4
    def y(t: float) -> float:
        return (2.0*t + 1) * (1-t)/(t**2.0 + 1) # cal the 1st derivate y_actual_solution
    # def f(t:float, y: float) -> float: 
    #     return 1.0 + y/t
    # def y(t: float) -> float:
    #     return t*(math.log(math.exp(1), t)) + 2
    
    t_span = [1.0, 2.0]
    y_init = 2.0
    n = 20
    t_span = [0.0, 1.0]
    y_init = 1.0
    n = 10
    methods = ['Midpoint', 'Heun', 'Ralston']

    
    t = np.linspace(start=t_span[0], 
                    stop=t_span[1],
                    num=n+1,
                    dtype=np.float64)
    
    df = pd.DataFrame(data={'t': t})
    df['exact'] = df['t'].apply(func=y)

    for method in methods:
        dfi = RungeKutta2(f= f, 
                        t_span= t_span, 
                        y_init= y_init, 
                        n=n,
                        method='Ralston')
        df = pd.concat(objs=[df, dfi], axis=1)
        df[f'e_{method}'] = abs(df['exact'] - df['y'])
        df.rename(columns={'y': f'y_{method}'}, inplace=True)
        
    print(df)
