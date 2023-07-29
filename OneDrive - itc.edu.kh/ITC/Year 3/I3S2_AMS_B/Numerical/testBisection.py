# Author: Manas Sharma
# Website: www.bragitoff.com
# Email: manassharma07@live.com
# License: MIT
# BISECTION METHOD
 
import numpy as np
import matplotlib.pyplot as plt
import math
 
 
 
# Define the function whose roots are required
def f(x):
    #return x**3-8
    return (math.exp(x)-2*x-2)
 
maxiter = 50 # Max. number of iterations
# eps = 10E-6  # Acceptable Error (termination criteria)
a = -1       # Guess Value for the lower bound on the root
b = 0       # Guess Value for the upper bound on the root
 
# Check if these values bracket the root or not?
if f(a)*f(b)>0:
    print('The given guesses do not bracket the root.')
    exit()
 
# Print the table header
print('--------------------------------------------------------------------------')
print('iter \t\t a \t\t b \t\t c \t\t f(c)        ')
print('--------------------------------------------------------------------------')
 
# Begin iterations for bisection method
for i in range(maxiter):
    # Calculate the value of the root at the ith step
    c = (a+b)/2
  
    # Print some values for the table
    print(str(i+1)+'\t\t% 10.8f\t% 10.8f\t% 10.8f\t% 10.8f\t' %(a, b, c, f(c)))
 
    # Check if the root has been found with acceptable error or not?
    if np.abs(f(c)-a)<0.0001:
        print('--------------------------------------------------------------------------')
        print('Root found : '+str(c))
        exit()
    # Check whether the root lies between a and c
    if f(a)*f(c)<0:
        # Change the upper bound
        b = c
    else: # The root lies between c and b
        # Change the lower bound
        a = c
 
 
     
     
print('--------------------------------------------------------------------------')
if i==maxiter-1:
    print('\n\nMax iterations reached!')
    print('Approximaiton to the Root after max iterations is : '+str(c))