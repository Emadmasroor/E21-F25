---
---

# HW 8

* Table of Contents
{:toc}

## Summary

**Due Date**: Tue, Oct 28 at midnight
**What to submit**:
- A PDF file that contains
  - the completed template from problem 2
  - the answers to problem 3.
  - the system of equations for problem 4
- `GaussianElimination.py` from problem 1
- The code that you used to solve problem 4.
**Where to submit**:
- Code at [this link](https://moodle.swarthmore.edu/mod/lti/view.php?id=769541)
- PDF at [this link](https://moodle.swarthmore.edu/mod/lti/view.php?id=769542)


## (1) Gauss-Seidel Method: an iterative approach to solving $Ax=b$

Write a Python function that takes as inputs:

- a square matrix `A`
- a column vector `b`
- a column vector `x0`
- an optional keyword argument called `tol`

and returns the solution to $Ax=b$, starting with the guess `x0` and using the Gauss-Seidel procedure until the norm of the residual falls below `tol`. 

~~~python
def Gauss_Seidel(A,b,x0,tol=1e-6):
    # A is the system matrix
    # b is the right-hand-side vector
    # x0 is the first guess.
    return x0
~~~

Recall that the residual is a column vector given by $$\boldsymbol{r} \equiv A \boldsymbol{x} - \boldsymbol{b},$$ and its norm is a scalar that represents 'how large' it is. The norm of the residual is given by $$||\boldsymbol{r}|| \equiv \sqrt{\sum_{i=1}^{N} r_i^2}.$$

**Hint**: You can either write your own function for the norm, or you can add the line `from numpy.linalg import norm` at the top of your Python file to make use of a built-in function from `numpy`.


(##) Test out your code on a sample problem
Solve $Ax = b$, where

$$A =
\begin{bmatrix}
-4.002509 & 1.009014 & 0.004640 & 1.001973 & -0.006880 & -0.006880 & -0.008838 & 0.007324 & 0.002022 \\
1.004161 & -4.009588 & 1.009398 & 0.006649 & 0.994247 & -0.006364 & -0.006332 & -0.003915 & 0.000495 \\
-0.001361 & 0.995825 & -3.997763 & 0.992790 & -0.004157 & 0.997327 & -0.000879 & 0.005704 & -0.006007 \\
1.000285 & 0.001848 & 0.990929 & -3.997849 & 0.993410 & -0.008699 & 1.008978 & 0.009313 & 0.006168 \\
-0.003908 & 0.991953 & 0.003685 & 0.998803 & -4.007559 & 0.999904 & -0.009312 & 1.008186 & -0.004824 \\
0.003250 & -0.003766 & 1.000401 & 0.000934 & 0.993697 & -3.990608 & 1.005503 & 0.008790 & 1.007897 \\
0.001958 & 0.008437 & -0.008230 & 0.993920 & -0.009095 & 0.996507 & -4.002226 & 0.995427 & 0.006575 \\
-0.002865 & -0.004381 & 0.000854 & -0.007182 & 1.006044 & -0.008509 & 1.009738 & -3.994555 & 0.993974 \\
-0.009890 & 0.006309 & 0.004137 & 0.004580 & 0.005425 & 0.991481 & -0.002831 & 0.992317 & -3.992738
\end{bmatrix}
$$
$$ 
b =
\begin{bmatrix}
  0 \\
  0 \\
1 \\
  0 \\
  0 \\
1 \\
2 \\
2 \\
3
\end{bmatrix}
$$

The solution to this system of equations is approximately:

~~~
[[-0.44438476]
 [-0.69183054]
 [-1.09794069]
 [-1.09218993]
 [-1.24513538]
 [-1.62781765]
 [-1.57135064]
 [-1.59193644]
 [-1.55419129]]
~~~

You may load these arrays into your Python code by downloading the files in the following table with, e.g., this code:

~~~
import numpy
A = numpy.loadtxt('test_A.txt')
b = numpy.loadtxt('test_B.txt')
x = numpy.loadtxt('true_x.txt')
~~~

| Description 			| File 			     |
|-------------------------------|----------------------------|
| System matrix $A$    		| [test_A.txt](test_A.txt)   |
| Right-hand side $b$    	| [test_B.txt](test_B.txt)   |
| True value $x_{\text{true}}$ 	| [true_x.txt](true_x.txt)   |


## (2) Gradient-based methods

In class, we briefly talked about the Conjugate Gradient method, which is one of the most widely-used methods for the solution of linear systems. You will not be writing your own code for this method, but you will make use of a pre-written program that implements this method. You can read more about it on page 88 of the textbook by [Kiusalaas](https://abukhan.weebly.com/uploads/2/5/1/7/25179218/numerical_methods_in_engineering_with_python.pdf)

~~~python
import numpy as np
from numpy import transpose as tr
from numpy import dot
from numpy.linalg import norm

def conjugate_gradient(A,b,x_guess,tol=1e-6):
    # Uses the conjugate gradient method to solve Ax=b within tolerance specified by 'tol'.
    x = x_guess.copy()
    r = b - dot(A,x)
    beta = 0
    s = r.copy()

    while 2+2 == 4: 
        a = dot(tr(s),r)/(dot(dot(tr(s),A),s))  # step size alpha
        x = x + a*s                             # update x
        r = b - dot(A,x)                     # calculate residual
        if norm(r) <  tol:
            break
        beta = - (dot(dot(tr(r),A),s)/
                  (dot(dot(tr(s),A),s)))        # step size beta
        s = r + beta*s                          # update search direction
    return x
~~~

**Written questions**

1. Modify the code above so that it tells you how many steps it took to arrive at the right answer. Using a very small tolerance such as `1e-6` in both cases, compare the number of steps that the Conjugate Gradient method takes vs the Gauss-Seidel method on the sample problem $Ax=b$ given above.

2. Modify the code above so that it returns, in addition to the solution vector `x`, an array containing the scalar values of the norm of the residual at eachiteration. To successfully do this, you will have to identify where the residual is calculated, use the `norm` function on the residual, and store the resulting answer in an array that you create for this purpose. Note that you may want to **preallocate** this array.
