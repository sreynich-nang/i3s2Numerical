import pandas as pd
from NewtonDividedDifference import NewtonDividedDifference
from EvaluatePolynomial import EvaluatePolynomial

def NewtonInterPolation(x: list[float], y: list[float], x0: float) -> tuple[float, list[float], pd.DataFrame ]:
    b, F = NewtonDividedDifference(x=x, y=y)
    p = EvaluatePolynomial(a=b, c=x[:-1], x=x0)
    return (p, b, F)
if __name__ == "__main__":
    x = [1,2,3]
    y = [2,5,10]
    x0 = 1.5
    p, b, F = NewtonDividedDifference(x=x, y=y, x0=x0)
    print(p)
    from LagrangeInterpolation import LagrangeInterpolation
    q = LagrangeInterpolation(x=x, y=y, z=x0)
    print(q)