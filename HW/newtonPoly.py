## module newtonPoly
''' p = evalPoly(a,xData,x).
    Evaluates Newton's polynomial p at x. The coefficient
    vector 'a' can be computed by the function 'coeffts'.

    a = coeffts(xData,yData).
    Computes the coefficients of Newton's polynomial.
'''
import numpy as np
import matplotlib.pyplot as plt

def evalPoly(a,xData,x):
    n = len(xData) - 1  # Degree of polynomial
    p = a[n]
    for k in range(1,n+1):
        p = a[n-k] + (x -xData[n-k])*p
    return p

def coeffts(xData,yData):
    m = len(xData)  # Number of data points
    a = yData.copy()
    for k in range(1,m):
        a[k:m] = (a[k:m] - a[k-1])/(xData[k:m] - xData[k-1])
    return a

# Specify a set of x- and y- coordinates to interpolate through.
# Keep the x-coordinates in order.
# x_set1 = np.array([0.0,1.0,3.0,4.0,6.0])    
# y_set1 = np.array([1.1,-2.1,3,7,-4])        

# Set up a continuously-spaced x-vector to represent the horizontal axis
# on which you will plot your interpolation function.
# xs1 = np.linspace(x_set1[0],x_set1[-1],100) 

# Write one line of code that calls the function 'coeffts' and stores the
# resulting coefficients in a variable 'a'.
# a = coeffts(x_set1,y_set1)

# Evaluate the polynomial interpolating function over many x values
# and assign the resulting array to a variable 'ys1'
# ys1 = evalPoly(a,x_set1,xs1)

# Make plots
# plt.plot(xs1,ys1,label='Interpolating function')
# plt.scatter(x_set1,y_set1,label='Data points')
# plt.legend()
# plt.show()
