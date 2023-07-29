# 1rd version
# def PolyEval(a,x):
#     N=len(a)
#     n = N-1
#     dp = 0
#     ddp = 0
#     p = a[n]
#     for k in range(1, N, 1):
#         dp = p + x * dp
#         ddp = 2 * dp + x * ddp
#         p = a[n - k] + x * p
#     return p,dp
# if __name__ == "__main__":
#     a = [1,2,3,4] # element of each in list_a are the coffeiction P(x) = 1 + 2x + 3x^2 + 4x^3
#     x = 2
#     p, dp = PolyEval(a=a, x=x)
#     print(a)
#     print(x)
#     print(p)
#     print(dp)

# 2nd version
def PolyEval(a, x, d):
    N = len(a)
    n = N - 1
    v = [0] * (d+1)
    v[0] = a[n]
    for k in range(1, N, 1):
        for l in range(d, 0, -1):
            v[l] = l*v[l-1] + x*v[l]
        v[0] = a[n-k] + x*v[0]
    return v
if __name__ == "__main__":
    a = [1,2,3,4]
    x = 2
    val = PolyEval(a=a, x=x, d=3)
    print(a)
    print(x)
    print(val)