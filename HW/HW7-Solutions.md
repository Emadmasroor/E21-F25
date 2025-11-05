---
---

# HW 7 Solutions

* Table of Contents
{:toc}

[HW 7 Questions](HW7)

## (1) Gaussian Elimination in Python

In this problem, you will write a program that solves a linear system of equations using Gaussian elimination followed by forward substitution. Turn in both functions that you write in a **single** python file called `GaussianElimination.py`.

### (1.1) Forward Elimination

~~~python
import numpy as np
def forward_elimination(a,b):
    n = len(b)
    for k in range(0,n-1):
        for i in range(k+1,n):
           if a[i,k] != 0.0:
               lam = a[i,k]/a[k,k]
               a[i,k:n] = a[i,k:n] - lam*a[k,k:n]
               b[i] = b[i] - lam*b[k]
    return np.concatenate((a,b),axis=1)
~~~

### (1.2) Backward Substitution

~~~python
```
Note: This solution is from the textbook,
and the backward substitution phase is implemented in a strange way here.
The vector "b" is used to store the value of the solution "x". This is done
to improve memory management and to not use more storage than absolutely necessary,
but it makes it harder to follow the logic. If you'd like to understand this better,
please talk to the instructor.
```
def backward_substitution(Ab):
    # 'unpack' the augmented matrix:
    n,m = np.shape(Ab)
    a = Ab[:,0:n]
    b = Ab[:,-1]

    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b
~~~

## (2) Gaussian Elimination by hand

<embed src="GaussianElimination-solution.pdf" width="500" height="375" 
 type="application/pdf">

## (3) The condition number.

The matrix-vector equation $$\begin{bmatrix} 4.1 & 2.8 \\ 9.7 & 6.6 \end{bmatrix} \cdot \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 4.1 \\ 9.7 \end{bmatrix}$$ has the solution $$\begin{bmatrix} 1 \\ 0 \end{bmatrix}.$$

If the above problem is repeated with a small difference to the right-hand side, i.e., $$\begin{bmatrix} 4.1 & 2.8 \\ 9.7 & 6.6 \end{bmatrix} \cdot \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 4.11 \\ 9.7 \end{bmatrix},$$ we find that the solution to this new equation is now $$\begin{bmatrix} 0.34 \\ 0.97 \end{bmatrix}.$$

This behavior can be explained by the **condition number** of this matrix. In class, we learned that the condition number of a matrix is equal to $$||A|| \cdot ||A^{-1}||,$$ i.e., it equals the norm of the matrix multiplied by the norm of its inverse. In this problem, $||A|| = 12.74$ and $||A^{-1}|| = 127.4$, so their product is $1,623$, a number that is much greater than $1$. Therefore, the matrix $A$ is ill-conditioned. Another way to see this is to notice that the determinant of the matrix, $|A|$, which is equal to $-0.1$, is much less than the norm $||A||$.

The matrix $A$ has a large condition number and is therefore **ill-conditioned**. This explains the fact that a tiny change of $0.01$ in the right-hand side of the equation $Ax=b$ makes a very large difference to the solution.

Consider the matrix $$\begin{bmatrix} 4.1 & 2.8 \\ 9.7 & 6.6 \end{bmatrix},$$ and the right-hand side vector $$\begin{bmatrix} 4.1 \\ 9.7 \end{bmatrix}.$$

## (4) Using linear systems to solve circuits


<embed src="Circuit-calcs.pdf" width="500" height="375" 
 type="application/pdf">

After writing out the circuit equations as shown in the PDF above, we find that the system of equations is

$$
\begin{bmatrix}
 -3 & 0 & 5 & 0 \\
 -4 & -2 & -9 & 2 \\
 0 & 2 & 0 & -3 \\
 1 & -1 & 1 & 0 \\
\end{bmatrix}
\cdot
\begin{bmatrix}
I_1 \\ I_2 \\ I_3 \\ I_4 \\ 
\end{bmatrix}
=
\begin{bmatrix}
-6 \\ 0 \\ 3 \\ 0 \\
\end{bmatrix}
$$

After using Gaussian elimination, we find:
~~~python
# HW 7 problem 4
A = np.array([[-3.,0.,5.,0.],
              [-4.,-2.,-9.,2],
              [0.,2.,0.,-3.],
              [1.,-1.,1.,0.]])

b = np.array([[-6.],
              [0.],
              [3.],
              [0.]])

print("Row-reduced matrix and rhs:")
print(forward_elimination(A,b))
print("Solution:")
print(backward_substitution(forward_elimination(A,b)))
~~~

~~~python
Row-reduced matrix and rhs:
[[ -3.           0.           5.           0.          -6.        ]
 [  0.          -2.         -15.66666667   2.           8.        ]
 [  0.           0.         -15.66666667  -1.          11.        ]
 [  0.           0.           0.          -1.67021277   1.37234043]]
Solution:
[ 0.91719745  0.26751592 -0.64968153 -0.82165605]
~~~

These have the right magnitudes, and any differences in sign simply mean that the original arrows were incorrectly drawn.

{% include mathjax.html %}
