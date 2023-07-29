from EvaluateLagrangePolynomial import EvaluateLagrangePolynomial
def LagrangeInterpolation(x: list[complex], y:list[complex], z:complex) -> complex:
    N = len(x)
    p = 0
    for i in range(0, N, 1):
        p = p + y[i] * EvaluateLagrangePolynomial(i=i, x=x, z=z)
    return p

if __name__=="__main__":
    x = [0,1,2,3]
    y = [1,2,5,10]
    for xi in x:
        p = LagrangeInterpolation(x=x, y=y, z=xi)
        print(f"p({xi})={p}") 