import numpy as np
import pandas as pd
from collections.abc import Callable
from typing import Literal


def RungeKutta(f: Callable[[np.float64, np.ndarray], np.ndarray],
               t_span: np.ndarray,
               y_init: np.ndarray,
               n: int,
               method: Literal["Classic", "ThreeEighth"] = "Classic"
               ) -> pd.DataFrame:
    if method == "Classic":
        c = np.array(object=[0, 1/2, 1/2, 1],
                     dtype=np.float64)
        a = np.array(object=[[0, 0, 0, 0],
                             [1/2, 0, 0, 0],
                             [0, 1/2, 0, 0],
                             [0, 0, 1, 0]],
                     dtype=np.float64)
        b = np.array(object=[1/6, 1/3, 1/3, 1/6],
                     dtype=np.float64)
    elif method == "ThreeEighth":
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
                    num=n+1)
    m = len(y_init)
    y = np.full(shape=(n+1, m),
                fill_value=np.nan,
                dtype=np.float64)
    y[0, :] = y_init
    for i in range(0, n, 1):
        k0 = f(t[i], y[i, :])
        k1 = f(t[i]+c[1]*h, y[i, :]+(a[1, 0]*k0)*h)
        k2 = f(t[i]+c[2]*h, y[i, :]+(a[2, 0]*k0 + a[2, 1]*k1)*h)
        k3 = f(t[i]+c[3]*h, y[i, :]+(a[3, 0]*k0 + a[3, 1]*k1 + a[3, 2]*k2)*h)
        y[i+1, :] = y[i, :] + h*(b[0]*k0 + b[1]*k1 + b[2]*k2 + b[3]*k3)
    df_t = pd.DataFrame(data=t, columns=["t"])
    df_y = pd.DataFrame(data=y, columns=[f"y{i+1}" for i in range(0, m, 1)])
    df = pd.concat(objs=[df_t, df_y], axis="columns")
    return df


if __name__ == "__main__":
    def f(t: np.float64, y: np.ndarray) -> np.ndarray:
        f1 = 3*y[0]+2*y[1]-(2*t**2 + 1)*np.exp(2*t)
        f2 = 4*y[0]+y[1]+(t**2+2*t-4)*np.exp(2*t)
        return np.array(object=[f1,f2],dtype=np.float64)
    t_span = np.array(object=[0,1],dtype=np.float64)
    y_init = np.array(object=[1,1],dtype=np.float64)
    n = 5
    df = RungeKutta(f=f,t_span=t_span,y_init=y_init,n=n,method="ThreeEighth")
    print(df)
