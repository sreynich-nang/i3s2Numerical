import pandas as pd
# x is list of coffiecient of x_axis, a is list of coffiencient of y_axis
def NaturalCubicSpline(x: list[float], a: list[float]) -> pd.DataFrame:
    N = len(x)
    n = N - 1
    h = [0] * N
    al = [0] * N
    l = [0] * N
    mu = [0] * N
    z = [0] * N
    c = [0] * N
    b = [0] * N
    d = [0] * N
    for i in range(0, n, 1):
        h[i] = x[i+1] - x[i]
    for i in range(1, n, 1):
        al[i] = 3 * (a[i+1] - a[i]) / h[i] - 3 * (a[i] - a[i-1]) / h[i - 1]
        l[0] = 1
        mu[0] = 0
        z[0] = 0
    for i in range(1, n, 1):
        l[i] = 2 * (x[i+1] - x[i-1]) - h[i-1] * mu[i-1]
        mu[i] = h[i]/l[i]
        z[i] = (al[i] - h[i-1] * z[i-1]) / l[i]
    l[n] = 1
    z[n] = 0
    c[n] = 0
    for j in range(n-1, -1, -1):
        c[j] = z[j] - mu[j] * c[j+1]
        b[j] = (a[j+1] - a[j]) / h[j] - h[j] * (c[j+1]+2*c[j]) / 3
        d[j] = (c[j+1] - c[j]) / (3*h[j])
    data = [a[:-1], b[:-1], c[:-1], d[:-1]]
    index = list('abcd')
    columns = [pd.Interval(left = x[i], right = x[i+1], closed = 'both') for i in range(len(x)-1)]
    df = pd.DataFrame(data=data, index=index, columns=columns).transpose()
    return df
if __name__ == "__main__":
    df = NaturalCubicSpline(x=[-2,-1,0,1,2,3],a=[70,2,-4,-8,2,110])
    print(df)
    # # ----------------------------------------------------
    # from EvaluateCubicSpline import EvaluateCubicSpline
    # p = EvaluateCubicSpline(df=df, x=2.5)
    # print(p)
    # # ----------------------------------------------------
    # import numpy as np
    # import matplotlib.pyplot as plt
    # figure = plt.figure()
    # axes = figure.add_subplot (111)
    # x = np.linspace(0,4,num=11)
    # y = np.array(object = [xi**2 for xi in x])
    # print(x)
    # print(y)
    # axes.set_aspect("equal")
    # axes.plot(x,y)