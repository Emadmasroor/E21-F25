---
---

# HW 11 Solutions

* Table of Contents
{:toc}

[HW 11 Questions](HW11)


## (1) Polynomial Interpolation

### (1.1) Set up the linear system of equations

~~~python
def interpolation_system(x_values,y_values):
    n = len(x_values)
    A = np.zeros((n,n))
    b = np.zeros((n,))
    for row in range(n):
        for col in range(n):
            summation = 0
            for k in range(n):
                summation += x_values[k]**(row+col)
            A[row,col] = summation
    for row in range(n):
        summation = 0
        for k in range(n):
            summation += y_values[k] * x_values[k]**row
        b[row] = summation
    return A,b
~~~

### (1.2) Solve the linear system for the data provided

To do this, it is sufficient to write:

~~~python
import numpy as np
from numpy.linalg import solve

data = np.loadtxt("interpolate_these.txt")
x_vals = data[:,0]
y_vals = data[:,1]

AA,bb = interpolation_system(x_vals,y_vals)
coeffs = solve(AA,bb)
~~~

### (1.3) Assemble an interpolating function that uses these coefficients

If you read the documentation of [`numpy.polyval`](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html) you will see that it expects, as its first argument, an array of coefficients. However, `polyval` expects the array of coefficients `p` to be ordered in the form 

~~~
p[0]*x**(N-1) + p[1]*x**(N-2) + ... + p[N-2]*x + p[N-1]
~~~
i.e., the coefficient of the highest power of $x$ is first, and the coefficient of the second-highest power of $x$ is second, ... and the last element of `p` is supposed to be the constant coefficient (a.k.a. the y-intercept). This is opposite to the convention that we used when we ordered our vector of unkonwns, so we need to 'flip' it. That's all you had to do in this question!

~~~python
def interpolating_polynomial(x,array_a):
    # Thin wrapper around polyval
    return np.polyval(np.flip(array_a),x)
~~~

It is also possible to write this out more fully and to not make use of `polyval` at all. 

### (1.4) Make a plot showing the data points and the interpolation

You already know what this was supposed to look like.

![Sample figure](interpolation_sample.png)

## (2) Polynomial curve-fit using least-squares

### (2.1) A function for generating the linear system

~~~python
def curvefit_system(x_values,y_values,m):
    n = len(x_values)
    A = np.zeros((m+1,m+1))
    b = np.zeros((m+1,))
    for row in range(m+1):
        for col in range(m+1):
            # There is a summation for each term.
            summation = 0
            for k in range(n):
                summation += x_values[k]**(row+col)
            A[row,col] = summation
    for row in range(m+1):
        # There is a summation for each term.
        summation = 0
        for k in range(n):
            summation += y_values[k]*x_values[k]**row
        b[row] = summation
    return A,b
~~~

### (2.2) Solve the linear system for the data provided, using $m=2$

~~~python
import numpy as np
from numpy.linalg import solve

data = np.loadtxt("datapoints.txt")
x_vals = data[:,0]
y_vals = data[:,1]
M = 2               # fit quadratic curve to this data

mat,rhs = curvefit_system(x_vals,y_vals,M)
coeffs = solve(mat,rhs)
~~~

### (2.3) Assemble a curve-fit function that uses the coefficients

The task here is pretty much identical to the task in (1.3). We will do it by writing a wrapper around `polyval` like before.

```
def interpolating_polynomial(x,array_a):
    # Thin wrapper around polyval
    return np.polyval(np.flip(array_a),x)
```

### (2.4) Make a plot

You already know what this was supposed to look like.

![Sample figure](curvefit_sample.png)



## (1) Golden Section Search

### (1.1) Working out by hand

<embed src="GoldenSectionSearchCompleted.pdf" width="500" height="375" 
 type="application/pdf">

### (1.2) Pseudo-code

Consider the following procedure.

```
Given: a,b,epsilon, and the function f to be maximized
R = (sqrt(5)-1)/2
h = b-a
x1 = b - R*h
x2 = a + R*h
f1 = f(x1)
f2 = f(x2)
while h > epsilon:
	if f1 > f2:
		leave a unchanged
		change b to be the current value of x2
		update h = b-a
		change x2,f2 to be the current value of x1,f1
		update x1 = b - R*h
		calculate a new f1 = f(x1)
	else if f1 < f2:
		change a to be the current value of x1
		leave b unchanged
		update h = b-a
		change x1,f1 to be the current value of x2,f2
		update x2 = a + R*h
		calculate a new f2 = f(x2)
once the loop has exited because h became smaller than epsilon,
return (a+b)/2
```

...

## (2) Naive multi-dimensional optimization

<embed src="NaiveNdimOpt.pdf" width="500" height="375" 
 type="application/pdf">




{% include mathjax.html %}
