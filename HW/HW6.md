# HW 6

* Table of Contents
{:toc}

## Summary

**Due Date**: Wed, Sep 24 at midnight
**What to submit**:
- A PDF file for problem 1.1, 1.2, 2.1, 2.3, 3.1, and 3.2
- A Python file for problem 1.3, titled bisection.py
- A Python file for problem 2.2, titled secant.py
- A Python file for problem 3.3, titled newton.py



## (1) The Bisection Algorithm

### (1.1) Working out the successive brackets *by hand*
The bisection algorithm works by successively `bracketing' the root between a lower bound and an upper bound, i.e., a left edge and a right edge. If we use the bisection algorithm on the function $$ f(x) = (x+\pi)(x-\pi/2)(x-5)$$ starting with the bracket $[-4,-3]$,
* what will be the next six brackets predicted by the algorithm? Arrange your answer neatly in a table similar to the one developed in class.
* Explain how many steps it will take to bracket the root within an interval of size $1 \times 10^{-6}$.

!!! Tip
    You should not use a computer to solve this problem. It's okay to use a calculator, though!

### (1.2) Choice of initial bracket
Using hand-calculations and a simple calculator, explain how the bisection algorithm will behave when initialized with each of the following brackets. For each case, indicate whether or not it will converge on a solution, and if so, which root it will converge on.

    You should not use a computer to solve this problem. It's okay to use a calculator, though!

* You start with the bracket $[-4,-2]$
* You start with the bracket $[-4,+2]$
* You start with the bracket $[-4,+6]$
* You start with the bracket $[0,+4.9]$
* You start with the bracket $[+2,+4]$

You may answer these questions with the help of a graph of the given function, shown below.

![$ f(x) = (x+\pi)(x-\pi/2)(x-5)$](bisection-fig.png)

### (1.3) A Python program for bisection

Complete the in-class activity with the bisection method, i.e., finish writing the program found at [this link](../Resources/#lec-61-tue-oct-7bisection_algorithm.py).

## (2) The Secant Method
In class, we learned how to implement the secant method to find the roots of a given function $f(x)$, starting with two estimates of the root.

### (2.1) Illustrating the secant method
Using the following image, graphically illustrate two steps of the secant method, starting with the pair of estimates, $x_1 = -3.0$ and $x_2 = -2.7$. In your solution, you should print out (or otherwise reproduce) the figure below, and should accurately determine, with the help of a straight edge and pencil, the next two estimates of the root.

![figure](secant-fig.png)
A complete illustration will contain four labeled points: $(x_1,f_1)$, $(x_2,f_2)$, $(x_3,f_3)$, and $(x_4,f_4)$, together with any other points that were necessary in order to find these four points. It should also contain straight lines connecting the points in the manner demonstrated in class. For each straight line shown, you should write down the equation of the straight line in the form of $y = mx+c$, where $m$ and $c$ are replaced with numbers precise up to two decimal places.

Include with your figure a written explanation of the steps that you took. This does not need to be very detailed, but you should expect to write at least a few sentences.

### (2.2) A Python program for the secant method


**Note:** You may wish to use the Python program for the bisection method, included in the files for lecture 11, as a template.

Write a Python program that uses the secant method to find the root of a function. Your program should take the following arguments:
* A function, whose root is to be found.
* `x1`, one estimate of the root
* `x2`, another estimate of the root
* `n`, the number of steps of the secant method that are to be carried out.

After each iteration, your program should 'forget' the estimate named `x1`; you do not need to calculate which estimate should be forgotten.

Your function should return the most recently calculated estimate of the root.


**Tip:** You may be tempted to store all subsequent values of $x$ that arise in the course of iterating the secant method. I strongly recommend that you avoid doing this. It's a good idea to write your program in such a way that you only store what you absolutely must. However, if you cannot think of a way to do this problem without storing all past values of $x$, you may ignore this advice.

**Testing out your code**

In class, we tested out our root-finding code using the function `numpy.cos`. This is because we know that this function has a root at $\pi/2$. Feel free to use this function to test out your code. However, you can also write your own test function. For example, you could define the following test function:

~~~python
def f_test(x):
    y = x ** 2 - 2*x - 4
    return y
~~~

and then pass `f_test` to your root-finding program. The result should be either $x \approx -1.236$ or $x \approx 3.236$.

### (2.3) Troubleshooting the secant method

**Tip:** For this part, you should have a working Python program that implements the secant method for `n` steps.

1. Use your Python function to determine a root for the function $f(x) = \sin(x)$ starting with the estimates $x = 4.3$ and $x=5.0$, using only a *single* iteration of the secant method. Comment on the answer that was found, and make a plot or sketch of the function $f(x)$, together with the straight line that was used by your program to arrive at this result.
2. Use your Python function to determine a root for the function $f(x) = \sin(x)$ starting with the estimates $x = 4.3$ and $x = 5.0$, using exactly *two* iterations of the secant method. Do this in two ways: (1) By passing `x1 = 4.3` and `x2 = 5.0`, and (2) by passing `x1 = 5.0` and `x2 = 4.3`. For both cases, use `n=2`. Report the results that are given by your Python program, and comment on why they are the way that they are.
3. Repeat 2, but this time using 7 iterations instead of 2. Comment on the results.

## (3) Newton's Method

In class, we learned how to implement Newton's method to find the roots of a given function $f(x)$, starting with a single estimate of the root. We also learned that, in order to implement this method, we need to be able to evaluate both $f(x)$ for any $x$, *and* evaluate $f'(x)$ for any $x$.

### (3.1) Illustrating Newton's Method


Using the following image, graphically illustrate two steps of Newton's method on the function $f(x) = x^2 -2x -4$, starting with the estimate that $x_0 = 0.0$ is the location of the root. This is not correct, but Newton's method will improve this estimate. In your solution, you should print out (or otherwise reproduce) the figure below, and should accruately determine, with the help of a straight edge and pencil, the next two estimates of the root.

![The function $f(x) = x^2-2x-4$](newton-fig.png)

A complete illustration will contain three illustrated points: $(x_0,f_0)$, $(x_1,f_1)$, and $(x_3,f_3)$, together with any other points that were necessary in order to find these three points. It should also contain straight lines as needed, as demonstrated in class.


**Hint:** You have to use the idea of a *tangent* to successfully execute this problem. There will be some variable human judgement in determining tangents; that's okay.

### (3.2) Thinking about gradients

1. For the same function illustrated above, $f(x) = x^2 - 2x - 4$, assume that Newton's method was being initiated starting from $x_0 = -4$. What is the value of the gradient of $f(x)$ evaluated at $x_0$ ?
2. What is the equation of the straight line that would be used to advance Newton's method starting at $x = -4$ ? Use the form $y = mx+c$, and replace $m$ and $c$ with their respective values.
2. When a Python program is written for Newton's method, the program takes as input two functions (among other things). What two Python functions would you have to pass to `newton_n` in order to find a root of the above function, $f(x) = x^2 - 2x - 4$ ? Write down these functions, 'by hand'. Use proper Python syntax, including the `def` and `return` keywords.

### (3.3) A Python program for Newton's method

Write a Python function that implements Newton's method for `n` iterations. Your function will look like this:

~~~python
def newton_n(f,derivative_of_f,x0,n):
    # Carries out n iterations of Newton's method to
    # find the root of the function f, starting from
    # the estimate x0.
    # ...
    return 0.0
~~~

and it should return the most recent estimate of the root of `f`.
