Due date: Tuesday September 10 at midnight
		Submit via Gradescope/Moodle [here](https://moodle.swarthmore.edu/mod/lti/view.php?id=694525).                             
Turn in the following files for this assignment.

* A file titled `methods_str.py` for problem 1.1
* A file titled `methods_list.py` for problem 1.2
* A file titled `logic_gates.py` for problem 2.2
* A file titled `conway_v1.py` for problem 2.3
* A file titled `slide_switch.py` for problem 3.1
* A file titled `light_sensor.py` for problem 3.2

# Variables and Types

For this problem, please use the Circuit Python REPL inside the Mu Editor. For this, you need to:

1. Open the Mu Editor while your Circuit Playground Bluefruit is connected via USB-C.
2. You should see the text "Circuit Python" at the bottom right together with a micro-chip symbol **without** a red X. If so, you have successfully completed the installation instructions from lecture 1. If not, please follow those instructions.
3. Click the 'Serial' button on the toolbar. This should open a new area of the Mu Editor screen.
4. The REPL should say "Press any key to enter the REPL. Use CTRL-D to reload." Follow this instruction and press any key. The lights on the circuit board will turn white and you are now in the "REPL" mode. 
5. This is the interactive version of Circuit Python.

## Methods associated with built-in class `str`

In class, you were shown how to create string objects.

Objects of type `str` are "strings" such as `hello` or `hello2` or `hello2!` and so on. To make a string and **assign it to a variable**, say, `a1`, execute the following line on the REPL. The `>>>` is only shown to indicate that you are doing this in REPL mode.


```python
>>> a = "hello!"
```


By using the `dir()` function on an object of type `str`, obtain a list of possible methods associated with class `str` in CircuitPython. Look up these methods in the official [Python documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) to find out what they do.

**Tasks**

Complete the following tasks. You will turn in text (hand-written or typed), not code.

1. What does the method `find` give you if you use it to find a character that doesn't exist in the searched string?
2. How does `find` deal with repeated characters in a string? 
3. Look up the documentation for the method `count` associated with the class `str`, i.e., the function `str.count`. Use this to write out the syntax for one line of code that counts the number of times the letter 'l' appears in the word 'hallelujah'.
4. In CircuitPython's REPL, use `dir(a)` where `a` is a string that you created. (It can be any string). This will give you all the methods that are associated with objects of type 'string' in CircuitPython. Choose 5 of these functions and look them up in the [official Python documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str). Write a short, one-to-two sentence explanation of what each function/method does.
5. Browse the list of methods associated with Python's `str` class, also at the [official documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) website. These methods are named `str.<methodname>(...)`. Find 2 methods that you see in this list that are **not** available in CircuitPython, i.e., methods that you do not see when you run `dir()` on a string that you created on your Circuit Playground. Write a short, one-to-two sentence explanation of what these methods/functions do.


## Methods associated with built-in class `list`.
By using the `dir()` function on an object of type `list`, obtain a list of possible methods associated with class `list`. For **five** of these methods, write one line of code that uses the method, followed by a line or two of comments explaining what the method does to a list. Make sure that the `list`s you use to demonstrate the methods are varied enough for the methods to make sense.

# Conditionals

## Background on Logic Gates

[Logic gates](https://en.wikipedia.org/wiki/Logic_gate) are physical devices that implement Boolean functions. For example, an 'AND' logic gate has two inputs and one output; the inputs can be set to either 'On' or 'Off', and the output is 'On' if and only if both the inputs are 'On'. In the following example, Bulb C will only light up if both switch A **and** switch B are on, because A and B are inputs to an AND gate.

![Fig. 2.1 An 'AND' gate. Bulb C does not light up because it needs *both* A *and* B to be on.](gate_example.png)

In Python, we can represent this situation as follows.

~~~ python
# 'And' gate in Python
A = False # right now, switch A is 'off'
B = True  # right now, switch B is 'on'

C = A and B # C will only be True if both A and B are True

# or, alternatively:
if A and B:
    C = True
~~~

Thus, implementing an 'AND' gate in Python is quite intuitive.


## Implement NAND and XOR gates in Python using `if` statements.

Two other kinds of logic gates are 'XOR' and 'NAND'. You can read about these gates on the internet; for example, [this webpage](https://www.techtarget.com/whatis/definition/logic-gate-AND-OR-XOR-NOT-NAND-NOR-and-XNOR)  offers a summary of the different types of gates and what logic they implement.

In the diagrams below, toggle switches A and B are connected via a NAND gate to light bulb X. Toggle switches C and D are connected via a XOR gate to light bulb Y. The outputs of the NAND gate and the XOR gate are connected via an AND gate to light bulb Z. Note that both figure 2.2 and 2.3 show the same system, but with different switches pressed. Blue color means 'On', and white means 'Off'.

Implement this logic in a Python script. Start with the skeleton script [logic_gates.py](logic_gates.py), which is embedded below.

~~~ python

# This part of the code sets the value of all four switches. 
# You can change them to test out different configurations.
# Your code should produce the correct result depending on which switches are set 
# to 'On' and which are set to 'Off'. 
# The current configuration corresponds to figure 2.1, but the logic is incorrect.

A = False
B = True
C = True
D = False

# ---- Implement Logic Gates below ---- #

if A and B:
    X = True
else:
    X = False

if C or D:
    Y = True
else:
    Y = False

Z = True

# ---- This part prints out a summary of the results. ----#
print("When switch A is set to",A)
print("When switch A is set to",A)
print("When switch A is set to",A)
print("When switch A is set to",A)

if X:
    print("light bulb X is on")
else:
    print("Light bulb X is off")
if Y:
    print("light bulb Y is on")
else:
    print("Light bulb Y is off")
if Z:
    print("Light bulb Z is on")
else:
    print("Light bulb Z is off")



~~~

![Fig. 2.2 System shown with switches B and C set to 'On'](A0B1C1D0.png)
![Fig. 2.3 System shown with all switches set to 'Off'](A0B0C0D0.png)

## Modify `conway_v1.py`
[Conway's game of life](https://playgameoflife.com/) works on the principle that every 'cell' in a 2-dimensional grid is either 'alive' or 'dead' at any given time. Time moves forward in discrete increments, and the state of the system at time step $n$ is determined completely by the state of the system at time step $n-1$, according to the following rules.

- If a cell is currently dead, then it becomes alive in the subsequent time step if it has exactly three live neighbors. 
- If a cell is currently alive, then it stays alive in the next time step only if it has either 2 or 3 live neighbors. Otherwise, it dies.

Download the script [`conway_v1.py`](conway_v1.py), which is embedded below. The variable `this` represents the state of a certain cell, and its neighbors are named `north`, `southwest`, etc, depending on their location relative to the reference cell. Modify the script so that the variable `this` gets updated to the correct state, depending on the state of its neighbors. You will only update the state of the reference cell. 

!!! Tip
    Note that this script implements a *single* time increment in the game, and does so for a single cell. You are not programming the entire game!

!!! Tip
    Consider creating a variable of type `int` and using it as a 'counter' variable. Then, use the `+` operator to increment this counter variable.
~~~
# Conway's game of life
# 'True' = 'Alive'
# 'False' = 'Dead'

# Current state of the system.

this        = True

north       = False
northwest   = False
west        = False
southwest   = False
south       = False
southeast   = False
east        = False
northeast   = False

#--- Implement logic here ---#
if this == True:
    # implement logic for alive cells
elif this == False:
    # implement logic for dead cells


~~~

You may wish to test out your code by modifying the neighbors' states (lines 9 to 16) and making sure that your script updates the reference cell correctly according to the rules of Conway's game of life. 


!!! WARNING
    
    If you can see a better way to do this using 'loops', that's great! But don't use them for this assignment.


# Programming the Circuit Playground Express using `if` statements

The Circuit Playground Express has a built-in light sensor and a slide switch. It also has multiple LEDs, called 'neopixels', that can be set to any color and brightness. You can read about how to use these functionalities of your board on [this page](../CPX_guide.html). In this problem, you are asked to use `if` statements to program the CPX. Note that all code run by the CPX should be enclosed in a `while` loop and should be preceded by the line of code shown in the example below.

~~~ python
from adafruit_circuitplayground.express import cpx

while True:
   # implement your code here.
~~~

## Slide switch

Write a program that, when loaded on to `code.py` on your Circuit Playground Express, sets one of the neopixels to red if the slide switch is set to 'off' (all other LEDs should be switched off), and sets a different pixel to green if the slide switch is set to 'on' (all other LEDs should be switched off). You can pick any of the pixels, but two different pixels should be used.

## Light sensor

Program the CPX to play a tone of 440 Hz if the light sensor is covered by one's hand, or if it placed in a very dark room. It should stop playing the tone once exposd to the usual light of a Singer Hall classroom.

!!! Tip
    There may be more than one way to solve this problem!
