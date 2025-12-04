---
---

# HW 10 Solutions

* Table of Contents
{:toc}

[HW 10 Questions](HW10)

## (1) Golden Section Search

### (1.1) Code

From the textbook:

~~~python
import math
def bracket(f,x1,h):
    c = 1.618033989 
    f1 = f(x1)
    x2 = x1 + h; f2 = f(x2)
  # Determine downhill direction and change sign of h if needed
    if f2 > f1:
        h = -h
        x2 = x1 + h; f2 = f(x2)
      # Check if minimum between x1 - h and x1 + h
        if f2 > f1: return x2,x1 - h 
  # Search loop
    for i in range (100):    
        h = c*h
        x3 = x2 + h; f3 = f(x3)
        if f3 > f2: return x1,x3
        x1 = x2; x2 = x3
        f1 = f2; f2 = f3
    print("Bracket did not find a mimimum")

def search(f,a,b,tol=1.0e-9):
    nIter = int(math.ceil(-2.078087*math.log(tol/abs(b-a))))
    R = 0.618033989
    C = 1.0 - R
  # First telescoping
    x1 = R*a + C*b; x2 = C*a + R*b
    f1 = f(x1); f2 = f(x2)
  # Main loop
    for i in range(nIter):
        if f1 > f2:
            a = x1
            x1 = x2; f1 = f2
            x2 = C*a + R*b; f2 = f(x2)
        else:
            b = x2
            x2 = x1; f2 = f1
            x1 = R*a + C*b; f1 = f(x1)
    if f1 < f2: return x1,f1
    else: return x2,f2
~~~

## (2)

~~~python
import numpy as np
from scipy.optimize import minimize_scalar
from noisy_function import make_noisy_function
from numpy.linalg import norm
import matplotlib.pyplot as plt

def naive_nd_optimize(f,guess,directions,n):
    x_current = np.array(guess)
    v1 = np.array(directions[0])
    v2 = np.array(directions[1])

    x_history = np.zeros((n,2))

    def f_1d(alpha):
        return f(*x_current + direction*alpha)

    for i in range(n):
        if (i%2):
            # if i is even:
            direction = v2
        else:
            #if i is odd:
            direction = v1

##        direction = v2 if (i % 2) else v1

        step_size = minimize_scalar(f_1d).x
        x_new = x_current + step_size*direction
        x_history[i,:] = x_current
        x_current = x_new
        print(x_current)

    return x_history

def test_f(x_vector):
    x = x_vector[0]
    y = x_vector[1]
    return (x-1)**2 + (y+1)**2 + x*y

# Optimize the noisy function
f2 = make_noisy_function(n=2, noise_amp=3.1, sigma=12)
hist1 = naive_nd_optimize(f2,[0,0],[[1,0],[0,1]],40)

# Now, plot the trajectory of your directions over a contour plot
# of the function.

# Create a grid of points
x = np.linspace(-5, 5, 300)
y = np.linspace(-5, 5, 300)
X, Y = np.meshgrid(x, y)

# Evaluate your noisy function over the above grid.
Z = f2(X.ravel(), Y.ravel()).reshape(X.shape)

# Plot

# Create a figure with two sets of axes, arranged
# as 1 row, two columns.
figure1, (axes1, axes2) = plt.subplots(1,2,figsize=(10,5))

figure1.figsize = (10,5)
figure1.suptitle('HW 10, Problem 3')

contour1 = axes1.contourf(X, Y, Z, levels=40)
plt.colorbar(contour1, label='f(x, y)')
axes1.set_xlim(left=-2,right=1)
axes1.set_ylim(bottom=-2,top=1)
axes1.plot(hist1[:,0],hist1[:,1],color='red')
axes1.set_title('Zoomed-in view')


contour2 = axes2.contourf(X, Y, Z, levels=40)
plt.colorbar(contour2, label='f(x, y)')
axes2.plot(hist1[:,0],hist1[:,1],color='red')
axes2.set_title('Zoomed-out view')

plt.show()

~~~

{% include mathjax.html %}
