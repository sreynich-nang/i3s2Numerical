from EvaluateCubicSpline import EvaluateCubicSpline
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.figure import Figure
# to see example in NaturalCubicSpline.py at the several last lines
def PlotCublicSpline(df: pd.DataFrame, aspect: str = "auto") -> tuple[Figure, Axes]:
    index = df.index.values
    n = len(df)
    x = [inter.right for inter in index]
    x = [index[0].left] + x
    y = [EvaluateCubicSpline(df=df, x=xi) for xi in x]
    x_range = x[n] - x[0]
    num = int(x_range / 0.01) + 1
    x_grid = np.linspace(start=x[0], stop=x[n], num=num)
    y_grid = [EvaluateCubicSpline(df, x=xi) for xi in x_grid]
    figure = plt.figure()
    axes = figure.add_subplot(111)
    axes.set_aspect(aspect=aspect)
    axes.plot(x_grid, y_grid)
    axes.scatter(x,y)
    return (figure, axes)