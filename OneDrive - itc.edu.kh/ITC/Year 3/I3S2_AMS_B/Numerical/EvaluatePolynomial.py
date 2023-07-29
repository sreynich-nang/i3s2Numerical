def EvaluatePolynomial(a: list[complex], x: complex) -> complex:
    """
    TODO
    ----------
    Evaluate a polynomial and its first and second derivatives at a given value of `x`.

    Parameters
    ----------
    1) `a` : `list[complex]`
        list of complex coefficients `[a_0,...,a_n]` of the polynomial `p(x)=a_0+a_1 x+...+a_n x^n`
    2) `x` : `complex`
        complex value at which the polynomial to be evaluated

    Return
    ----------
    1) `p` : `complex`
        complex value of the polynomial evaluated at `x`

    Example
    ----------
    >>> import NumericalAnalysis as na
    >>> p = na.EvaluatePolynomial(a=[1, 1, 1], x=1)
    >>> print(p)
    """
    N = len(a)
    n = N - 1
    p = a[n]
    for i in range(1, N, 1):
        p = a[n - i] + x * p
    return p