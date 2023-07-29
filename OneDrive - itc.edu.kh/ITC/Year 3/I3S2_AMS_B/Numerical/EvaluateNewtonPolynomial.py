def EvaluateNewtonPolynomial(a: list[complex], c: list[complex], x: complex) -> complex:
    n = len(a) - 1
    p = a[n]
    start = n-1
    for k in range (start , -1, -1):
        p = a[k] + p * (x - c[k])
    return p

if __name__=="__main__":
    a=[0, 14, -4, 1]
    c = [2, -3, 1]
    x = 0
    p = EvaluateNewtonPolynomial(a=a, c=c, x=x)
    print(p)