def DeflatePolynomial(a: list[complex], x: complex) -> list[complex]:
    """
    TODO
    ----------
    Deflate a polynomial `p(x)` to `q(x)` with monic linear factor containing the given zero.

    Parameters
    ----------
    1) `a` : `list[complex]`
        list of coefficients `[a_0,a_1,...,a_n]` of `p(x)=a_0+a_1 x+...+a_n x^n`
    2) `x` : `complex`
        zero of `p(x)`

    Return
    ----------
    1) `b` : `list[complex]`
        list of coefficients `[b_0,b_1,...,b_{n-1}]` of `q(x)=b_0+b_1 x+...+b_{n-1} x^{n-1}`

    Example
    ----------
    >>> import NumericalAnalysis as na
    >>> a = [1, 2, -3]
    >>> b = na.DeflatePolynomial(a=a, x=1)
    >>> print(f"a = {a}")
    >>> print(f"b = {b}")
    """
    n = len(a) - 1
    b = [(0 + 0j)] * n
    b[n - 1] = a[n]
    for k in range(n - 2, -1, -1):
        b[k] = a[k + 1] + x * b[k + 1]
    return b