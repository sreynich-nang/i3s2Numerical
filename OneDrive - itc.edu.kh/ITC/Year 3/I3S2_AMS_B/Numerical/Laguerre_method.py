import numpy as np
from numpy.polynomial import Laguerre
p = Laguerre([1,-9,34,-20,-261,949,-1014])
x = np.arange(6)

print(p(x))
print()
print(p)