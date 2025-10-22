---
---

# HW 5

* Table of Contents
{:toc}


## Summary

**Due Date**: Tue, Oct 7 at midnight  
**What to submit**:  
- Problem (1): A single Python file containing all code for this problem
- Problem (2): A single Python file containing the required function definitions with correct names.
- Problem (3): A single Python file containing the required function definitions with correct names.
- Problem (4)  Two `*.png` files and two corresponding `*.py` files that, when run, reproduce the respective plots using `matplotlib.pyplot.show()`

**Submit at**: [This link](https://moodle.swarthmore.edu/mod/lti/view.php?id=767303) 

## (1) Complete in-class activity: Numpy functions

For each of the functions from the `numpy` package named below, write a line or set of lines of code that demonstrates how this function is used. You must also write a plain-language comment before demonstrating each function, and in this comment you should write what that function does.

The list of functions is:

~~~python
numpy.array()
numpy.zeros()
numpy.ones()
numpy.empty()
numpy.arange()
numpy.linspace()
numpy.random.rand()
numpy.random.randint()
numpy.reshape()
numpy.transpose()
numpy.concatenate()
numpy.flatten()
numpy.resize()
numpy.shape()
numpy.savetxt()
numpy.loadtxt()
~~~

**Note**: The function `flatten` cannot actually be used directly using `numpy.flatten` as written above, which was an oversight on the part of the isntructor. It is a method associated with the class `ndarray`, and you can see how to use it on the [manual page](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html).

The solutions below have been taken from a student's submission.

~~~python
import numpy as np

# numpy.array() creates an array from a python list or tuple
npArray = np.array([1,2,3,4,5,6])
print(f"npArray: {npArray}")

#numpy.zeros() creates an array filled with zeros
npZeros = np.zeros((2,2))
print(f"npZeros: {npZeros}")

#numpy.ones() creates an array filled with ones
npOnes = np.ones((2,2))
print(f"npOnes: {npOnes}")

# numpy.empty() creates an array without initializing any internal values
npEmpty = np.empty((2,2))
print(f"npEmpty: {npEmpty}")    #values are random in memory

# numpy.arange() creates an array with values evenly spaced based on a specified range
npArange = np.arange(0, 12, 3)
print(f"npArrange: {npArange}")

# numpy.linspace() creates an array with values evenly spaced betwen a start and end inclusive
npLinspace = np.linspace(0, 12, 3)
print(f"npLinspace: {npLinspace}")

# numpy.random.rand() creates an array with random numbers between 0 and 1
npRand = np.random.rand(2,2)
print(f"npRand: {npRand}")

# numpy.random.randint() creates an array filled with random numbers within a certain range
npRandint = np.random.randint(0, 4, size = (2,2))
print(f"npRandint: {npRandint}")

# numpy.reshape() alters the shape of an array without changing the data
npReshape = npRandint.reshape(1,4)
print(f"npReshape on npRandint: {npReshape}")

# numpy.transpose() switches the rows and columns of an array
npTranspose = npReshape.transpose()
print(f"npTranspose on npReshape: {npTranspose}")

# numpy.concatenate() joins two arrays together along the preexisting axis
npConcatenate = np.concatenate((npZeros, npOnes))
print(f"npConcatenate with npZeros and npOnes: {npConcatenate}")

# numpy.flatten() alters an array from multiple dimensions to one dimension
npFlatten = npConcatenate.flatten()
print(f"npFlatten on npConcatenate: {npFlatten}")

# numpy.resize() returns a new array with a specified shape
npResize = np.resize(npZeros, (3,3))
print(f"npResize npZeros to 3x3: {npResize}")

# numpy.shape() returns the dimensions of an array
npShape = np.shape(npResize)
print(f"npShape of npResize: {npShape}")

# numpy.savetxt() saves an array to a txt file
np.savetxt("test.txt", npResize)

# numpy.loadtxt() loads data from a text file to an array
npLoadtxt = np.loadtxt("test.txt")
print(f"npLoadtxt from test.txt: {npLoadtxt}")
~~~

## (2) Working with Numpy arrays: Iteration

For each task below, you should create a function that takes as input an arbitrarily-sized 2D array. The functions need not return anything. The functions should be named as `func2_1(...), func2_2(...), func2_3(...)`, where the number after `func2_` denotes the part number in the following list.


You may wish to test out your code on arrays of arbitrary size. Initialize random arrays of specified size using the syntax
~~~python
numpy.random.randint(1,10,size=(7,10))
~~~
This will create a $7 \times 10$ array of integers between 1 and 10.

1. The `numpy.array` type is iterable, just like `list`s and `tuple`s are. Use this fact to write a `for` loop that iterates over the array that you created and prints all the *rows*.
2. The function `numpy.nditer` creates a different type of iterable when applied to an object of type `numpy.array`. Use this fact to write a `for` loop that iterates over `numpy.nditer(your array)`, and prints all the *elements*.
3. It is also possible to iterate over `numpy` arrays using the familiar `for x in range(n)` technique. Use a nested `for` loop (i.e., a total of two loops, one inside the other) to print every element in the array. It should first print out all the elements of the first row, starting from the first column (i.e., starting from the left), then all the elements of the second column, and so on.
4. Repeat 3, but this time, your function should print out the first *column* first, starting from the top; then it should move to the next column, and so on.

## (3) Working with Numpy arrays: Manipulating arrays

For this problem, please name your functions `func3_1`, `func3_2`, and `func3_3`.

1. Write a function that reverses the order of rows in a `numpy` array. The function should take an arbitarily-sized 2D array and return a 2D array of the same size.

2. Write a function that reverses the order of columns in a `numpy` array. The function should take an arbitrarily-sized 2D array and return a 2D array of the same size.

3. Write a function that takes as input argument a *square* 2D array, i.e. with shape `(n,n)` and returns as output a 1-dimensional `numpy` array of length `n` containing the diagonal elements of the 2D array.


## (4) Plotting 

### Plotting Mathematical functions in `matplotlib`

Your goal in this task is to reproduce the following figure as closely as possible.

![Figure to be reproduced](example1.png)

You will turn in both a `*.png` file and a Python script (i.e., a `*.py` file that, when run, reproduces your image). Your figure should satisfy the following criteria:

Plot the two functions $$y = e^{x/2} \sin x$$ and $$y = e^{x/3} \cos x$$

over the range $x \in [0,2\pi]$.

* The y-axis range should be from -15 to 10.
* The y-axis should have tick marks at even numbers.
* The x-axis range should be from -1 to 7.
* The x-axis should have tick marks at integer intervals.
* There should be light-gray axes inside the figure, i.e. straight lines at $x=0$ and $y = 0$. These lines should have a width that is less than the width of the lines depictuing the functions.
* The function $e^{x/2}\sin(x)$ should be blue, and the function $e^{x/3}\cos(x)$ should be red.
* There should be a legend as shown.
* The two functions should be listed in the order shown in the legend.
* There should be a title
* There should be labels for the horizontal and vertical axes.
* The PNG file should be produced programmatically; you cannot just screenshot the plot.* Your Python script should include `import` commands at the top for `matplotlib.pyplot` as well as `numpy`.

### Plotting numerical data using `matplotlib`

Download [this data file](HW5_prob4_data.csv), which contains the data necessary to reproduce the following plot. Write a script in Python, making use of `matplotlib.pyplot`, that generates the following plot.

![Figure to be reproduced](example2.png)

As above, you should reproduce as many features of the above plot as you can. In particular, the color and style of the markers should closely match the above figure.


{% include mathjax.html %}
