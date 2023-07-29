from EvaluatePolynomial import EvaluatePolynomial
from DeflatePolynomial import DeflatePolynomial

def ShiftedPowerPolynomial(a: list[complex], c: complex) -> list[complex]:
    N = len(a)
    b = [0] * N
    b[0] = EvaluatePolynomial(a=a, x=c)
    for k in range(1, N, 1):
        a[0] = a[0] - b[k-1]
        a = DeflatePolynomial(a=a, x=c)
        b[k] = EvaluatePolynomial(a=a, x=c)
    return b

if __name__ == "__main__":
    a = [2,3,-4,5]
    b = ShiftedPowerPolynomial(a=a, c=2)
    print(a)
    print(b)