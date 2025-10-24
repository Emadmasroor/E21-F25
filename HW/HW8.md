
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
