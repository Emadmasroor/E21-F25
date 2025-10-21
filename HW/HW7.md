---
---

# HW 7

* Table of Contents
{:toc}

## Summary

**Due Date**: Tue, Oct 28 at midnight   
**What to submit**:  
- A PDF file that contains
  - the completed template from problem 2
  - the completed table from problem 4.2
  - the plot from problem 4.3, which should be the output of your `residual_history.py` file
- `GaussianElimination.py` from problem 1
- `GaussSeidel.py` from problem 3
- `iterative_methods.py` from problem 4.1 
- `compare_steps.py` from problem 4.2
- `residual_history.py` from problem 4.3.
**Where to submit**:  
- Code at [this link]()
- PDF at [this link]()

## Some Tips

**Built-in methods to solve linear systems**

`numpy` already contains the capabilities to solve linear systems efficiently. If a solution to a linear system Ax=b exists, `numpy` can find it using built-in methods.

For example, the following code works:
~~~python
from numpy import dot
from numpy.linalg import inv as invert

# Assuming A is a square matrix and b is a column vector:
x = dot(invert(A),b)
~~~

**Calculating the norm**

`numpy` can calculate the norm. Just include the line

~~~python
from numpy.linalg import norm
~~~

and then use the function `norm`.


## (1) Gaussian Elimination in Python

In this problem, you will write a program that solves a linear system of equations using Gaussian elimination followed by forward substitution. Turn in both functions that you write in a **single** python file called `GaussianElimination.py`.

### (1.1) Forward Elimination

Write a function named `forward_elimination` that takes as input a matrix `A` and a column vector `b`. It should output the augmented matrix after it has been put in 'row echelon form', i.e., after the lower-left portion has been appropriately replaced with zeros. Note that:

- your function should work with `numpy` arrays.
- `b` must be a *column vector* in `numpy`. See below for an example of how to create a column vector using `numpy`.
- Your program should return `None` if there are any size discrepancies. You should think about the possible ways in which the size of `A` or `b` may be incompataible with the Gaussian elimination procedure.


**Hint**: You may find it helpful to use the function `numpy.concatenate((A,b),axis=1)`.

~~~python
import numpy as np
def forward_elimination(A,b):
    # A is a square matrix of size N x N,
    # e.g., [[1,2,3],[1,4,5],[0,1,2]]
    # b is a column vector of size N x 1
    # e.g., [[-1],[5],[7]]
    # Function returns augmented matrix [A | b]
    
    aug = np.concatenate((A,b),axis=1)
    return aug
~~~

Try out your code on the problem that was on the slides for Tuesday's lecture, i.e., when you provide the following variables to your function:

~~~
A1 = np.array([[2,1,-1,2],
               [4,5,-3,6],
               [-2,5,-2,6],
               [4,11,-4,8]])

b1 = np.array([[5],
               [9],
               [4],
               [2]])
~~~

and then call your function on it, the result should be as shown below.

~~~
>>> forward_elimination(A1,b1)

[[ 2  1 -1  2  5]
 [ 0  3 -1  2 -1]
 [ 0  0 -1  4 11]
 [ 0  0  0  2  6]]
~~~

### (1.2) Backward Substitution

Write a Python function that performs backward substitution. The function should take as input an 'augmented matrix', and should output a column vector of *values* corresponding to the solution to the system of equations $Ax=b$.

**Hint**: Recall that `A[:,-1]` returns the last column of a matrix.

~~~python
import numpy as np
def backward_substitution(Ab):
    # Input is a N x (N+1) matrix
    # output is a column vector of size N x 1

    # Initialize your 'x' vector that will contain your solution
    x = np.zeros((N,1))

    return x
~~~

## (2) Gaussian Elimination by hand

Fill in the following template to carry out Gaussian elimination by hand on the following matrix $A$ and right-hand-side $b$:

$$
A =\begin{bmatrix}
2 & 1 & -1 & 0\\
1 & 1 & 2 & 0\\
-1 & 2 & 1 & 1\\
6 & 1 & 1 & -2
\end{bmatrix}, \quad b = \begin{bmatrix} 1 \\ -1 \\ 0 \\ 2 \end{bmatrix},
$$

(###) Template

<embed src="GaussianElimination.pdf" width="500" height="375" 
 type="application/pdf">

## (3) Gauss-Seidel Method: an iterative approach to solving $Ax=b$

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

You should test your function on the following problem. For full credit, make sure your function works on this problem before turning it in!

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

## (4) (Unspecified problem, will be updated)


{% include mathjax.html %} 
