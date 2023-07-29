import numpy as np
import pandas as pd
from collections.abc import Callable
from RungeKutta import RungeKutta

def LinearShooting(p: Callable[[np.ndarray], np.ndarray],
                   q: Callable[[np.ndarray], np.ndarray],
                   r: Callable[[np.ndarray], np.ndarray],
                   t_span: np.ndarray,
                   y_init: np.ndarray,
                   n: np.int64,
                   ) -> pd.DataFrame:
    def f1(t: np.float64, y: np.ndarray) -> np.ndarray:
        return np.array(object=[y[1], p(t)*y[1] + q(t)*y[0] + r(t)],
                        dtype=np.float64)
    def f2(t: np.float64, y: np.ndarray) -> np.ndarray:
        return np.array(object=[y[1], p(t)*y[1] + q(t)*y[0]],
                        dtype=np.float64)
    y_init1 = np.array(object=[y_init[0], 0.], dtype=np.float64)
    y_init2 = np.array(object=[0., 1.], dtype=np.float64)
    df1 = RungeKutta(f=f1, t_span=t_span, y_init=y_init1, n=n)
    df2 = RungeKutta(f=f2, t_span=t_span, y_init=y_init2, n=n)

    t = df1.loc[:, 't']
    y1 = df1.loc[:, 'y1']
    y2 = df2.loc[:, 'y2']
    fac = (y_init[1] - y1[n]) / y2[n]
    y = y1 + fac*y2
    df = pd.DataFrame(data={'t': t, 'y1':y1, 'y2': y2, 'y': y})
    return df

if __name__ == '__main__':
    def f(t: np.float64, y: np.ndarray) -> np.ndarray:
        f1 = y[0] + 2*y[1] - 2*y[2] + np.exp(-t)
        f2 = y[1] + y[2] - 2*np.exp(-t)
        f3 = y[0] + 2*y[1] + np.exp(-t)
        return np.array(object=[f1, f2, f3], dtype=np.float64)
    t_span = np.array(object=[0, 1], dtype=np.float64)
    y_init = np.array(object=[3, -1, 1], dtype=np.float64)
    n = 10

    df = RungeKutta(f=f, t_span=t_span, y_init=y_init, n=n)
    print(df)

    # def f(t: np.float64, y: np.ndarray) -> np.ndarray:
    #     f1 = y[1]
    #     f2 = y[2]
    #     f3 = y[2]/t - 3*y[1] /t**2 + 4*y[0]/t**3 + 5*np.log(t) + 1
    #     return np.array(object=[f1, f2, f3], dtype=np.float64)
    # t_span = np.array(object=[0, 1], dtype=np.float64)
    # y_init = np.array(object=[3, -1, 1], dtype=np.float64)
    # n = 10

    # df = RungeKutta(f=f, t_span=t_span, y_init=y_init, n=n)
    # print(df)

