# HW 3 (Under Construction)

* Table of Contents
{:toc}


## Summary

**Due Date**: Tue, Sep 16 at midnight  
**What to submit**:  
- Problem (1): a PDF file only
- Problem (2): a file named `music.py`
- Problem (3): a file named `analog_digital_temperature.py`
- Problem (4): a PDF file _and_ a file named `reaction_times.py`

**Submit at**: [This link](https://moodle.swarthmore.edu/mod/lti/view.php?id=763898) for the PDF and [this link](https://moodle.swarthmore.edu/mod/lti/view.php?id=763897) for the code. You can see the submission pages on the course Moodle page as well.

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

Write the function `lightUp` as defined in the comments below. Turn in code including the function definition as well as the `while` loop you can see beneath the function definition. 

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

(##) Recall the Rules for Conway's Game of Life

- At any time, each cell is either alive or dead.
- The game moves forward in steps.
- At each step, the new state of the system is determined fully by the old state of the system.
- The update rules are as follows:
 - Any live cell with 2 or 3 live neighbors survives, and is alive in the next step.
 - All other live cells die, and are dead in the next step.
 - Any dead cell with exactly 3 live neighbors becomes alive in the next step.
 - All other dead cells remain dead, and stay dead in the next step.

### Write a function to determine the neighbors of interior cells.

Write a function called `nbrs_v1` that generates a list corresponding to the (up to 8) neighbors that each interior cell has. (By _interior cell_, we mean any cell that's not on the edge of the grid). The function should take in a single argument of type `int`, and should return a list of the neighbors of the cell whose address was passed to the function. For example, you can see by inspection that the cell with address 22 has the following eight neighbors:
- 16 ("North")
- 28 ("South")
- 23 ("East")
- 21 ("West")
- 27 ("Southwest")
- 29 ("Southeast")
- 15 ("Northwest")
- 17 ("Northeast")

Thus, when you call this function with argument 22, it should return a list containing the above numbers.





