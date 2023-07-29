from collections.abc import Callable

def CompositeTrapzoid(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    h = (b-a)/n
    f0 = f(a) + f(b)
    fi = 0
    x = a
    for i in range(1, n, 1):
        x = x + h
        fi = fi + f(x)
    A = h * (0.5 * f0 + fi)
    return A

if __name__ == '__main__':
    def f(x): return x**2
    # I = CompositeSimpson(f=f, a=0, b=1, n=10)
    I = CompositeTrapzoid(f=f, a=0, b=1, n=10)
    print(I)

