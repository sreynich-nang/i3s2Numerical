from _collections_abc import Callable
import pandas as pd
import numpy as np
def RungekuttaFehlberg (f: Callable [[float, float], float],
                        t_span: list or tuple,
                        y_init: float,
                        TOL: float,
                        hmax: float,
                        hmin: float) -> pd.DataFrame:
    (a, b) = t_span
    t = a
    y = y_init
    h = hmax
    t_list = []
    y_list = []
    h_list = []
    err_list = []      
    def runge_kutta_step(t, y, h):
        k1= h*f(t, y)
        k2= h* f(t + h / 4, y + k1 / 4)
        k3= h*f(t + 3 * h / 8, y + 3* k1 / 32 +9 * k2 / 32)
        k4= h* f(t + 12* h/13, y + 1932 *k1 / 2197 -7200 * k2/2197 + 7296* k3/2197)
        k5= h * f(t + h, y + 439 *k1 / 216 - 8*k2 + 3680* k3 / 513 - 845 *k4 / 4104)
        k6= h * f(t + h / 2, y - 8 * k1/ 27 + 2 * k2 - 3544 * k3 / 2565 + 1859*k4 / 4104 - 11* k5 / 40)
        y_new = y + 25 *k1 / 216 + 1408* k3 / 2565 +2197 *k4 / 4104 - k5 / 5
        y_hat = y + 16 *k1 / 135 + 6656 * k3 / 12825 +28561*k4 / 56430- 9 * k5 / 50 + 2 * k6 / 55
        return y_new, y_hat
    delta = 0
    while t < b:
        if t + h > b:
            h = b - t
        y_new, y_hat= runge_kutta_step(t, y, h)
        R = abs(y_hat- y_new)
        if R <= TOL:
            t_list.append(t)
            y_list.append(y_new)
            h_list.append(h)
            err_list.append(R)
            t = t + h
            y = y_new
            delta = 0.84* (TOL / R) *0.25
            delta= max(min(delta, 4), 0.1)
        if R == 0.0:
            h=hmax
        else:
            h = delta * h
            h = max(min(h, hmax), hmin)
    df = pd.DataFrame (data={"t": t_list, "y": y_list, "error": err_list, "h": h_list})
    return df
if __name__=="__main__":
    import math
    def f(t, y):  
        return  (2+2*(t**(3)))*y**(3) - t*y
    t_span= [0, 2]
    y_init = 1/3
    TOL = 1e-6
    hmax = 0.5
    hmin = 0.05
    df = RungekuttaFehlberg (f=f, t_span=t_span, y_init=y_init, TOL=TOL, hmax=hmax, hmin=hmin)
    def y(t: float) -> float: 
        return (3 + 2 * t**(2 )+ 6 * math.exp(t**2)) ** (-1 / 2)
    df ["exact"]= df ["t"].apply(func=y)
    df ["error"]= abs(df["exact"] - df ["y"])
    print(df)