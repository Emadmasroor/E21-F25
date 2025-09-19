# HW 3 (Under Construction)

* Table of Contents
{:toc}


## Summary

**Due Date**: Wed, Sep 24 at midnight  
**What to submit**:  
- Problem (1): A file named `accelerometer.py`
- Problem (2): A file named `neopixelfunction.py`
- Problem (3): A file named `numbersystemconversion.py`
- Problem (4): A file for each of parts (a) through (e), named `nbrs.py`, `checkBounds.py`, `all_nbrs.py`, `new_value_n.py` and `new_state.py` respectively. 

**Submit at**: [This link](https://moodle.swarthmore.edu/mod/lti/view.php?id=765384) for the code. There is no PDF submission for this HW.

## (1) Completing Accelerometer Activity from class

In this task, you have to complete the activity that you started in class, this time with a little bit more specificity.

Write a program that, when saved to your Circuit Playground Bluefruit, creates a text file containing  acceleration data recorded from the accelerometer. This data should contain four numbers: the acceleration in the x, y and z directions and the magnitude of the acceleration.

You are encouraged to make use of code from the [Resources](../Resources) page.

The text file should look like this:

```
0.134,0.456,9.105,9.714
0.627,0.479,9.405,9.864
0.234,0.356,9.304,9.643
```

Note that you will probably need to use a line of code similar to:

```python
file.write(f"{a:.3f},{b:.3f},{c:.3f},{d:.3f}\n")
```

**Data Collection Parameters**

- There should be a total of 100 readings
- Each reading should be taken after a delay of `0.05` seconds **and** a `cp.play_tone()` of `0.05` seconds using any frequency of your choice. Every time the acceleration data is read, the circuit playground should beep.
- During the data collection, an LED light should light up, and it should switch off when the reading is completed.
- Use your program to collect one set of 100 readings. During this time, your board should be stationary for approximately half of the data collection period, and you should throw/move it around a few times so that these motions are captured by the acclerometer as well.


## (2) Completing the function activity from class

Write the function `lightUp` as defined in the comments below. Turn in code including the function definition as well as the `while` loop you can see beneath the function definition, inside a single file.

You will probably want to use `if` statements so that the strings `red`, `green` and `blue` can be interpreted correctly.

```python
import adafruit_circuitplayground as cp
import time
def lightUp(color,n,p):
    # Lights up pixel number n using color "color"
    # 'Color' should be a string, either 'red', 'blue', or 'green'
    # n should be an int between 0 and 9
    # p should be any number between 1 and 255
    return 42

# Now call it inside a while loop
while True:
    lightUp(‘red’,8,45)
    time.sleep(3)
    lightUp('green',5,200)
    time.sleep(3)
    cp.play_tone(440,3)
```

## (3) While loops and type conversions

Write a function that takes as argument a decimal number in string format (type `str`). The function should return that number as a binary number in string format (type `str`).

~~~python
def decimal_to_binary(num):
 # Takes as input a string 'num'.
 # Interprets this string as a decimal number (integer).
 # Returns the binary representation of that number in string format.
 return num
~~~

For example, calling `decimal_to_binary('15')` should return `'1111'`.

Some hints:
- You can append characters to a string by using `+`. For example, `'10' + '1'` will return `'101'`
- Remember that you can convert strings to integers and vice versa using the functions `int` and `str` respectively.

## (4) Coding a 6x6 version of Conway's Game of Life with functions

Consider [Conway's Game of Life](https://playgameoflife.com/) played over a 6x6 grid. Each cell in the grid has an 'address', which is indicated in the following diagram.

|    |    |    |    |    |    |
|----|----|----|----|----|----|
| 0  | 1  | 2  | 3  | 4  | 5  |
| 6  | 7  | 8  | 9  | 10 | 11 |
| 12 | 13 | 14 | 15 | 16 | 17 |
| 18 | 19 | 20 | 21 | 22 | 23 |
| 24 | 25 | 26 | 27 | 28 | 29 |
| 30 | 31 | 32 | 33 | 34 | 35 |



The state of the system can be fully determined by a 36-element list of Boolean values, where `True` indicates an 'alive' cell and `False` indicates a 'dead' cell.

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

Write a function called `nbrs` that generates a list corresponding to the (up to 8) neighbors that each interior cell has. (By _interior cell_, we mean any cell that's not on the edge of the grid). The function should take in a single argument of type `int`, and should return a list of the neighbors of the cell whose address was passed to the function. For example, you can see by inspection that the cell with address 22 has the following eight neighbors:
- 16 ("North")
- 28 ("South")
- 23 ("East")
- 21 ("West")
- 27 ("Southwest")
- 29 ("Southeast")
- 15 ("Northwest")
- 17 ("Northeast")

Thus, when you call this function with argument 22, it should return a list containing the above numbers.

Notice that edge cells, such as cell number 18 or 31, do not have eight neighbors. For now, don't pay much attention to how your function treats edge cells! Your function will probably return an incorrect answer for cells on one of the four edges, and that's okay. Later, you will write code that ensures that this function is never used on non-interior cells.

### (b) Write a function that checks whether an address is in the interior part of the grid

For this part, you will write a function `checkBounds(n)` that returns `True` if `n` is one of the interior cells and `False` if `n` is on the boundary of the grid, or if it is outside the grid altogether.

You must use an appropriate conditional (or conditionals) inside this function. You won't get full credit for 'hard-coding' all the addresses that should return True, for example.

### (c) Determine a list of neighbors for every cell in 6x6 grid

In this part, you will put together the code from the last two parts and use it to assemble a list of lists that denotes the neighbors of each cell in the `6x6` grid shown above. Remember that once this list is determined, it doesn't change as the game progresses.

Write a function called `all_nbrs()` with no input arguments that returns a 36-element list. Each element of this list should itself be a list that contains the addresses of the neighbors of the cell at that location. If a cell is on one of the edges, there should be an empty list for its 'list of neighbors'. We will pretend that cells on the edge have no neighbors (since we will never update them). 

Thus, the structure of your returned list will be:

`[[],[],[],...( total of 36 lists here)...,[],[],[]]` 

**Note:** Theoretically, you could solve this problem by 'hardcoding' it, i.e., you could write a function that returns the correct list because you've written out every element of every list inside the 36-element list. But this won't give you full (or, really, any) credit.

~~~python
def all_nbrs():
 # Start out by creating a list of 36 zeros.
 nbrs = [0] * 36
 # Then modify this list so that each element is a list.
 return nbrs
~~~

The graders will check this function by calling `all_nbrs()` and making sure that the resulting list matches the correct one. For example, `your_returned_list[22]` should be equal to `[16,28,23,21,27,29,15,17]` or some permutation thereof because this is the correct list of neighbors for cell number `22`. You can place the neighbors in any order you like. Similarly, `your_returned_list[31]` should be equal to `[]` since `31` is the address for one of the cells on the edge, which we are pretending have no neighbors at all.

### (d) A function that updates a single cell

Write a function named `new_value_n(n,current_state)` that tells you what the new value of cell `n` should be, based on the current state of the whole system. This function executes *one step* of the game for *one cell*, but it takes as input the entire current state.

Your function should assume that `current_state` is a 36-element list of booleans.

~~~python
def new_value_n(n,current_state):
 # Based on the current state of the system, determine the new state of cell n.
 # DO NOT CHANGE current_state.
 # Return True if, according to Conway's Game of Life's rules, cell number n should
 # be alive in the next step, and False if, according to the same rules, this 
 # cell should be dead in the next step.
 
 # Placeholder code:
 return False
~~~

**An Example**

If the current state of the system looks like this, where filled squares represent true/alive and empty squares represent false/dead:

|---|---|---|---|---|---|
| ■ | □ | □ | ■ | □ | □ |
| □ | ■ | □ | □ | ■ | ■ |
| ■ | ■ | □ | ■ | □ | □ |
| □ | □ | ■ | □ | ■ | ■ |
| ■ | □ | ■ | □ | □ | ■ |
| □ | ■ | □ | ■ | ■ | □ |

This can be represented as a list of Booleans as follows:
~~~python
a=[True, False, False, True, False, False,
 False, True, False, False, True, True,
 True, True, False, True, False, False,
 False, False, True, False, True, True,
 True, False, True, False, False, True,
 False, True, False, True, True, False]
~~~

If the current state of the system is as above, then calling `new_value_n(9,a)` should return `True`, since cell 9 is currently dead but it has exactly three live neighbors. If your function is called on a cell that is at the edge of the grid, it should return `True` if that cell is currently alive and `False` if that cell is currently dead, i.e., it should not change the state of any cell on the boundary.

### (e) Update all the (interior) cells

Write a function that returns a new 'state variable' for the system based on the current state variable for the system. You will likely make use of a `for` loop  here, and you must use your `new_value_n` function.

~~~python
def new_state(old_state)
 # Returns the new state of the system, given the old state of the system.
 # new_state should be a list of Booleans of the same size as old_state.
 # Assume both lists are 36 elements long.
 newlist = [0] * 36
 # Write your code here
 return newlist
~~~

