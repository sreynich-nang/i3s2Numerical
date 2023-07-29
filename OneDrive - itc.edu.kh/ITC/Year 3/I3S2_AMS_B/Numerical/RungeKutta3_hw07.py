from collections.abc import Callable
from typing import Literal
from typing import Optional
import pandas as pd
import numpy as np

def RungeKutta3(f: Callable[[float, float], float],
                t_span: list,
                y_init: float, 
                n: int,
                method: Optional[Literal['Midpoint3', 'Heun3', 'Ralston3', 'SSPR3']] = 'Heun3'
                ) -> pd.DataFrame:
    (a, b) = t_span
    h = (b-a) / n
    t = np.linspace(start=a, stop=b, num=n+1, dtype=np.float64)
    y = np.full_like(a=t, fill_value=np.nan, dtype=np.float64)
    y[0] = y_init
    
    if method == 'Heun3':
        c = np.array(object=[0, 1/3, 2/3], dtype=np.float64)
        a = np.array(object=[[0, 0, 0],
                            [1/3, 0, 0],
                            [0, 2/3, 0]], 
                            dtype=np.float64)
        b = np.array(object=[1/4, 0, 3/4], dtype=np.float64)
    elif method == 'Kutta3':
        c = np.array(object=[0, 1/2, 1], dtype=np.float64)
        a = np.array(object=[[0, 0, 0],
                            [1/2, 0, 0],
                            [-1, 2, 0]], 
                            dtype=np.float64)
        b = np.array(object=[1/6, 2/3, 1/6], dtype=np.float64)
    elif method == 'SSPRK3':
        c = np.array([0, 1/2, 1], dtype=np.float64)
        a = np.array([[0, 0, 0], [1/2, 0, 0], [-1, 2, 0]], dtype=np.float64)
        b = np.array([1/6, 2/3, 1/6], dtype=np.float64)
        
    else:
        c = np.array(object=[0, 1/2, 3/4], dtype=np.float64)
        a = np.array(object=[[0, 0, 0],
                            [1/2, 0, 0],
                            [0, 3/4, 0]], 
                            dtype=np.float64)
        b = np.array(object=[2/9, 1/3, 4/9], dtype=np.float64)

    for i in range(0, n):
        k1 = f(t[i], y[i])
        k2 = f(t[i] + c[1]*h , y[i] + h*(a[1][0]*k1))
        k3 = f(t[i] + c[2]*h , y[i] + h*(a[2][0]*k1 + a[2][1]*k2))
        y[i+1] = y[i] + h*(b[0]*k1 + b[1]*k2 + b[2]*k3)

    df = pd.DataFrame(data={'t': t,'y': y})
    return df

if __name__ == '__main__':
    from math import sin, cos
    # def f(t:float, y: float) -> float: 
    #     return t**(-2)*(sin(2*t) - 2*t*y)
    # def y(t: float) -> float:
    #     return 0.5*t**(-2)*(4 + cos(4) - cos(2*t))
    def f(t:float, y: float) -> float: 
        return t**(-2)*(sin(2*t) - 2*t*y)
    def y(t: float) -> float:
        return 0.5*t**(-2)*(4 + cos(4) - cos(2*t))
    t_span = [1.0, 2.0]
    y_init = 2.0
    n = 10
    methods = ['Midpoint3', 'Heun3', 'Ralston3', 'SSPRK3']
    
    t = np.linspace(start=t_span[0], stop=t_span[1], num=n+1, dtype=np.float64) 
    df = pd.DataFrame(data={'t': t})
    df['exact'] = df['t'].apply(func=y)

    for method in methods:
        dfi = RungeKutta3(f=f, t_span=t_span, y_init=y_init, n=n, method=method)
        df[f'y_{method}'] = dfi['y']
        df[f'e_{method}'] = abs(df['exact'] - df[f'y_{method}'])

    print(df)
    # df.to_excel('HW07.xlsx')                   
