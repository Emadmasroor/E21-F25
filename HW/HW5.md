# HW 4

* Table of Contents
{:toc}


## Summary

**Due Date**: Tue, Sep 30 at midnight  
**What to submit**:  
- Problem (1): A PDF file. 
- Problem (2): A file named `floating_point.py`
- Problem (3): A file named `Conway_v2.py`. Make sure functions have the expected names.

**Submit at**: [This link](https://moodle.swarthmore.edu/mod/lti/view.php?id=766335) for the code  
And [This link](https://moodle.swarthmore.edu/mod/lti/view.php?id=766339) for the PDF.

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

## (2) Working with Numpy arrays: Iteration

For each task below, you should create a function that takes as input an arbitrarily-sized 2D array. The functions need not return anything. The functions should be named as `func1(...), func2(...), func3(...)`, where the number after `func` denotes the part number in the following list.


You may wish to test out your code on arrays of arbitrary size. Initialize random arrays of specified size using the syntax
~~~python
numpy.random.randint(1,10,size=(7,10))
~~~
This will create a $7 \times 10$ array of integers between 1 and 10.

1. The `numpy.array` type is iterable, just like `list`s and `tuple`s are. Use this fact to write a `for` loop that iterates over the array that you created and prints all the *rows*.
2. The function `numpy.nditer` creates a different type of iterable when applied to an object of type `numpy.array`. Use this fact to write a `for` loop that iterates over `numpy.nditer(your array)`, and prints all the *elements*.
3. It is also possible to iterate over `numpy` arrays using the familiar `for x in range(n)` technique. Use a nested `for` loop (i.e., a total of two loops, one inside the other) to print every element in the array. It should first print out all the elements of the first row, starting from the first column (i.e., starting from the left), then all the elements of the second column, and so on.
4. Repeat 3, but this time, your function should print out the first *column* first, starting from the top; then it should move to the next column, and so on.


## (3) Plotting Mathematical functions in `matplotlib`

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

# Plotting numerical data using `matplotlib`

Download [this data file](HW5_prob4_data.csv), which contains the data necessary to reproduce the following plot. Write a script in Python, making use of `matplotlib.pyplot`, that generates the following plot.

![Figure to be reproduced](example2.png)

As above, you should reproduce as many features of the above plot as you can. In particular, the color and style of the markers should closely match the above figure.



## (2)




## (1) A closer look at the IEEE standard for floating point numbers

| Size   | Sign | Significand | Exponent | Bias | Colloquial Name  | Machine Epsilon | Largest number | Smallest number | Number of numbers |
| ------ | ---- | ----------- | -------- | ---- | ---------------- | --------------- | -------------- | --------------- | ----------------- |
| 16-bit | 1    | 10          | 5        | 15   | Half precision   |                 |                |                 |                   |
| 32-bit | 1    | 23          | 8        | 127  | Single precision |                 |                |                 |                   |
| 64-bit | 1    | 52          | 11       | 1023 | Double precision |                 |                |                 |                   |

1. Explain how to interpret the following 16-bit number: `0100110000001010`. Showing all of your calculations, write down its representation as (a) a decimal number, and (b) a fraction, both in base 10. 

2. Write down the next-biggest 16-bit number, (a) in IEEE binary format, (b) as a decimal number in base 10, and (c) as a fraction in base 10.

3. Complete the table above by filling in the missing fields. You are encouraged to use the [Float Toy](https://evanw.github.io/float-toy/) widget for the "Largest number" and "Smallest number" answers.  

4. It would seem that floating-point binary numbers can have $2^p$ possible  numbers in the exponent, where $p$ is the number of bits in the exponent (e.g., 32 possible exponent values for 16-bit numbers since $2^5=32$). However, in practice, you will find that the IEEE standard only allows $(2^p)-1$ distinct numbers as the exponent. Use [Float Toy](https://evanw.github.io/float-toy/) to find out the range of possible exponent values for 16-bit, 32-bit and 64-bit floating point binary numbers. Your answers should be in the form: "16-bit: Exponent ranges from x to y for a total of z exponents".

5. With the help of Float Toy, explain how the following two numbers differ from each other. `0000010000000100` and `0000000000000100`. Look carefully at the decimal representation of these numbers to help answer this question.

6. Calculate --- don't just look up --- Machine Epsilon for 16-bit, 32-bit, and 64-bit floats. In your answer, you need to show that you know how to calculate it yourself, even though you will probably need a calculator to actually perform the computation.

7. Gaps in 16-bit floating point numbers. 

- Calculate how many 16-bit floating point numbers exist between 16 and 32, not including 32, i.e., find the number of elements in the set $[2^4,2^5)$. How large is the gap between these numbers?
- Calculate how many 16-bit floating point numbers exist between 128 and 256, not including 256, i.e., find the number of elements in the set $[2^7,2^8)$. How large is the gap between these numbers?
- Calculate how many 16-bit floating point numbers exist between $1/32$ and $1/16$, not including $1/16$, i.e., find the number of elements in the set $[2^{-5},2^{-4})$. How large is the gap between these numbers?
- Calculate how many 16-bit floating point numbers exist between $1/256$ and $1/128$, not including $1/16$, i.e., find the number of elements in the set $[2^{-8},2^{-7})$. How large is the gap between these numbers?

## (2) A Python program to interpret IEEE-standard floating point binary numbers.

Write a function that can interpret a string of 1's and 0's as a decimal number. The string of 1's and 0's is presumed to be arranged according to the IEEE standard for 16-bit, 32-bit, or 64-bit numbers.

For example,

```python
>>>  readIEEEfloat('0100110000001010')
16.15625
```

```python
def readIEEEfloat(num_string):
    # Takes as input a string of `1`'s and `0`'s and returns a number (of type `float`) whose value is equal to that binary number's value according to the IEEE Standard for 16-bit, 32-bit or 64-bit numbers.

    return 0

```

To write the above function, it is recommended that you make use of two other functions, both of which are described below and one of which is provided to you.

~~~python
def binary_to_dec_int(num):
 # determine the value of the binary integer 'num'.
 # 'num' is expected to be a string.
 # return the value as an object of type `int`
 return 0

def binary_to_dec_fraction(num):
  # num is a string of 0's and 1's. It is interpreted in the following way:
  # The first 'digit' is the multiple of (1/2). the second 'digit' is the multiple of (1/4). The third 'digit' is the multiple of (1/8), and so on.
  # for example, in the IEEE format, a 16-bit number could have the significand
  # 1.0011010101
  # This function reads the string of bits AFTER the "decimal point" and
  # returns the value of the resulting fraction as a 'float'.
  # The returned value must always be less than 1.
  s = len(num)
  total_value = 0
  for index in range(s):
    power = -index - 1
    digit = int(num[index])
    value = (2 ** power) * digit
    total_value += value
  return total_value
~~~

## (3) Conway's Game of Life

**Coding an N x N version of Conway's Game of Life with functions**

Consider [Conway's Game of Life](https://playgameoflife.com/) played over an N x N grid. Each cell in the grid has an 'address', which is indicated in the following diagram using the same convention as before.

|----|----|----|----|----|----|
| 0  | 1  | 2  | 3  | 4  | 5  |
| 6  | 7  | 8  | 9  | 10 | 11 |
| 12 | 13 | 14 | 15 | 16 | 17 |
| 18 | 19 | 20 | 21 | 22 | 23 |
| 24 | 25 | 26 | 27 | 28 | 29 |
| 30 | 31 | 32 | 33 | 34 | 35 |

The state of the system can be fully determined by an (N-squared)-element list of Boolean values, where `True` indicates an 'alive' cell and `False` indicates a 'dead' cell.

**New in HW 4**: You now have access to the functions `visualizeConway(state)` and `random_boolean_list(length)` to help you visualize these long lists of booleans. Download a file contianing these functions [here](../Resources/ConwayUtilities.py).

Try these as follows.

~~~python

a = random_boolean_list(49)
visualizeConway(a)

~~~

|---|---|---|---|---|---|---|
| □ | □ | ■ | □ | □ | □ | □ |
| □ | □ | □ | ■ | ■ | ■ | ■ |
| ■ | ■ | □ | □ | □ | ■ | □ |
| ■ | □ | ■ | ■ | □ | ■ | □ |
| ■ | □ | ■ | ■ | ■ | ■ | ■ |
| ■ | □ | ■ | ■ | □ | □ | □ |
| □ | ■ | ■ | ■ | ■ | □ | □ |


**Recall the Rules for Conway's Game of Life**

- At any time, each cell is either alive or dead.
- The game moves forward in steps.
- At each step, the new state of the system is determined fully by the old state of the system.
- The update rules are as follows:
 - Any live cell with 2 or 3 live neighbors survives, and is alive in the next step.
 - All other live cells die, and are dead in the next step.
 - Any dead cell with exactly 3 live neighbors becomes alive in the next step.
 - All other dead cells remain dead, and stay dead in the next step.

### (a) Write a function to determine the neighbors of interior cells.

Write a function called `nbrs_v2` that generates a list corresponding to the addresses of the neighbors that a given interior cell has. (By _interior cell_, we mean any cell that's not on the edge of the grid). The function should take in an argumen single argument of type `int`, and should return a list of the neighbors of the cell whose address was passed to the function. For example, you can see by inspection that the cell with address 22 has the following eight neighbors:
- 16 ("North")
- 28 ("South")
- 23 ("East")
- 21 ("West")
- 27 ("Southwest")
- 29 ("Southeast")
- 15 ("Northwest")
- 17 ("Northeast")

~~~python
def nbrs_v2(n,size):
    # Returns a list of addreses for the neighbors of the cell with address n.
    # Assumes that the grid is N x N, where N = size.

    return []
~~~

When you call this function with argument 22, it should return a list containing the numbers in the list above.


Notice that edge cells, such as cell number 18 or 31, do not have eight neighbors. For now, don't pay much attention to how your function treats edge cells! Your function will probably return an incorrect answer for cells on one of the four edges, and that's okay. Later, you will write code that ensures that this function is never used on non-interior cells.

### (b) Write a function that checks whether an address is in the interior part of the grid

For this part, you will write a function `checkBounds(n,size)` that returns `True` if `n` is one of the interior cells and `False` if `n` is on the boundary of the grid, or if it is outside the grid altogether.

~~~python
def checkBounds_v2(n,size):
    # n is the address whose interior-ness is being checked. 
    # 'size' is the size of one side of the square grid.
~~~

### (c) Determine a list of neighbors for every cell in N x N grid

In this part, you will put together the code from the last two parts and use it to assemble a list of lists that denotes the neighbors of each cell in the `N x N` grid. Remember that once this list is determined, it doesn't change as the game progresses.

Write a function called `all_nbrs_v2(size)` with no input arguments that returns a "size-squared"-element list. Each element of this list should itself be a list that contains the addresses of the neighbors of the cell at that location. If a cell is on one of the edges, there should be an empty list for its 'list of neighbors'. We will pretend that cells on the edge have no neighbors (since we will never update them). 

Thus, the structure of your returned list will be:

`[[],[],[],...( total of N x N lists here)...,[],[],[]]` 

~~~python
def all_nbrs(size):
 # Start out by creating a list of 36 zeros.
 nbrs = [0] * size ** 2
 # Then modify this list so that each element is a list.
 return nbrs
~~~

### (d) A function that updates a single cell

Write a function named `new_value_n_v2(n,current_state)` that tells you what the new value of cell `n` should be, based on the current state of the whole system. This function executes *one step* of the game for *one cell*, but it takes as input the entire current state.

Your function should assume that `current_state` is an (N^2)-long list of booleans.

~~~python
def new_value_n_v2(n,current_state):
 # Based on the current state of the system, determine the new state of cell n.
 # DO NOT CHANGE current_state.
 # Return True if, according to Conway's Game of Life's rules, cell number n should
 # be alive in the next step, and False if, according to the same rules, this 
 # cell should be dead in the next step.
 
 # Placeholder code:
 return False
~~~

### (e) Update all interior cells for one step in time.

Write a function that returns a new 'state variable' for the system based on the current state variable for the system. You will likely make use of a `for` loop  here, and you must use your `new_value_n_v2` function.

~~~python
def new_state_v2(old_state)
 # Returns the new state of the system, given the old state of the system.
 # new_state should be a list of Booleans of the same size as old_state.
 # The new state should have the same size as the old state.
 
 # Write your code here
 return newlist
~~~


