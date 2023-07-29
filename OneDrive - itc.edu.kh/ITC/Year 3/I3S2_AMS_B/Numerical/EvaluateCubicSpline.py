import pandas as pd
from EvaluatePolynomial import EvaluatePolynomial
# to see example in NaturalCubicSpline.py at the several last lines
def EvaluateCubicSpline(df: pd.DataFrame, x: float) -> float:
    n = len(df)
    index = df.index.values
    for k in range(0, n ,1):
        inter = index[k]
        if (x in inter):
            i = k
            break
    p = EvaluatePolynomial(a=df.iloc[i, : ].to_list(), x = x - inter.left)
    return p
