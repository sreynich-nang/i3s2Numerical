def EvaluateLagrangePolynomial( i : int, x: list[complex], z: complex) -> complex:
    L = 1
    stop  = len(x)
    for j in range (0, stop, 1):
        if (i != j):
            L = L *(z-x[j])/(x[i]-x[j])
    return L
if __name__=="__main__":
    i = 2
    x = [0,1,2,3]
    z = 4 
    L = EvaluateLagrangePolynomial(i=i, x=x, z=z)
    print(L)