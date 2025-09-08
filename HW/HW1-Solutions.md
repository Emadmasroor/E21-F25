# HW 1 Solutions

* Table of Contents
{:toc}

## (1) Variables and Types

### Methods associated with built-in class `str`

1. What does the method `find` give you if you use it to find a character that doesn't exist in the searched string?  
**Ans:** This returns `-1`
2. How does `find` deal with repeated characters in a string?  
**Ans:** The location of the first instance of that character is reported.
3. Look up the documentation for the method `count` associated with the class `str`, i.e., the function `str.count`. Use this to write out the syntax for one line of code that counts the number of times the letter 'l' appears in the word 'hallelujah'.  
**Ans:** The code for this is `str.count("hallelujah","l")`, which gives the answer `3`.
4. In CircuitPython's REPL, use `dir(a)` where `a` is a string that you created. (It can be any string). This will give you all the methods that are associated with objects of type 'string' in CircuitPython. Choose 5 of these functions and look them up in the [official Python documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str). Write a short, one-to-two sentence explanation of what each function/method does. Also, write out a line of valid CircuitPython syntax for using the functions you have chosen.  
**Ans:** Using `dir` on a string gives the following result.  
```python
['__class__', 'count', 'endswith', 'find', 'format', 'index', 'isalpha', 'isdigit', 'islower', 'isspace', 'isupper', 'join', 'lower', 'lstrip', 'replace', 'rfind', 'rindex', 'rsplit', 'rstrip', 'split', 'startswith', 'strip', 'upper', 'center', 'encode', 'partition', 'rpartition', 'splitlines']
```  
We will now choose five of these to look up and explain. For example,  
a. `count` is used to count the number of times a certain character appears in a string.  
```python
>>> str.count("hello","l")
2
```  
b. `endswith` checks whether a given string ends with a given character or not. So, for example:  
```python
>>> a = "hello"
>>> a.endswith("e")
False
```  
since `hello` does not end with the letter `e`.  
c. `isalpha` checks if a given string consists of alphabetical characters only, or not. So, for example:  
```python
>>> a = "hello"
>>> str.isalpha(a)
True
```  
since `hello` consists of only letters.  
d. `upper` converts a string to uppercase letters. So, for example,  
```python
>>> str.upper("hello")
"HELLO"
```  
e. The function `rstrip` 'strips' given characters from the right side of a string. So, for example,  
```python
>>> str.rstrip("A quick brown fox","fox")
"A quick brown "
```  

### Methods associated with built-in class `list`

Using `dir` on a list returns:  
```python
['__class__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```  
We will now choose five of these to look up and explain.

- `append` adds something to the end of a list. Thus,  
```python
>>> a = [1,2,3]
>>> list.append(a,100)
>>> a
[1,2,3,100]
```  
- `clear` empties a list of all its contents. Thus,
```python
>>> a = [1,2,3]
>>> list.clear(a)
>>> a
[]
```  
- `count` counts the number of times an object appears in a list. Thus,
```python
>>> list.count([1,2,3,100,3],3)
2
```
- `reverse` reverses the order of a list. Thus,
```python
>>> a = [1,2,3,100,6]
>>> list.reverse(a)
>>> a
[6,100,3,2,1]
```
- `sort` uses alphanumeric sort on the elements of a list. So, for a list of numbers, we get
```python
>>> a = [1,2,5,2,9,0,-1]
>>> list.sort(a)
>>> a
[-1, 0, 1, 2, 2, 5, 9]
```

## (2) Conway's Game of Life

This problem can be solved with the following code. There are more elegant ways to solve this, as well, but for now something like this will do.

~~~python
# Conway's game of life
# 'True' = 'Alive'
# 'False' = 'Dead'

# Current state of the system. You should modify this to see
# how your code behaves if the state of the system is changed.
# Right now, all the surrounding cells are 'dead' and the
# cell at the center is 'alive'.

this        = True

north       = False
northwest   = False
west        = False
southwest   = True
south       = False
southeast   = False
east        = True
northeast   = False

# Print to inform the user about the current state.
# Don't change this line.
print("The cell is currently",this)

# --- Solutions --- #
live_nbrs = 0
if north == True:
    alive_nbrs += 1
if northwest == True:
    alive_nbrs += 1
if west == True:
    alive_nbrs += 1
if southwest == True:
    alive_nbrs += 1
if south == True:
    alive_nbrs += 1
if southeast == True:
    alive_nbrs += 1
if east == True:
    alive_nbrs += 1
if northeast == True:
    alive_nbrs += 1

if this == True:
    if alive_nbrs == 2 or alive_nbrs == 3:
        this = True
        # remains alive
    else:
        this = False
        # dies
elif this == False:
    if alive_nbrs == 3:
        this = True
        # comes to life
    # don't need an 'else'.
# --------------- #

# Print to inform the user about the new state:
# Don't change this line.
print("After applying the rules, the cell is now",this)
~~~


## (3) Programming the Circuit Playground Bluefruit using `if` statements

The Circuit Playground Bluefruit has a built-in light sensor and a slide switch. It also has multiple LEDs, called 'neopixels', that can be set to any color and brightness. You can read about how to use these functionalities of your board on [this page](../Resources#instructors-circuit-playground-guide-for-e21). In this problem, you are asked to use `if` statements to program the Circuit Playground Bluefruit. Note that all code run by the Circuit Playground Bluefruit should be enclosed in a `while` loop and should be preceded by the line of code shown in the example below.

~~~ python
from adafruit_circuitplayground import cp

while True:
   # implement your code here.
~~~

### Slide switch

Write a program that, when loaded on to `code.py` on your Circuit Playground Bluefruit, sets one of the neopixels to red if the slide switch is set to 'off' (all other LEDs should be switched off), and sets a different pixel to green if the slide switch is set to 'on' (all other LEDs should be switched off). You can pick any of the pixels, but two different pixels should be used.

```python
from adafruit_circuitplayground import cp

while True:
    if not cp.switch:
        cp.pixels[0] = (50,0,0)
        cp.pixels[1] = (0,0,0)
    else:
        cp.pixels[0] = (0,0,0)
        cp.pixels[1] = (0,50,0)

```

### Light sensor

Program the Circuit Playground Bluefruit to play a tone of 440 Hz if the light sensor is covered by one's hand, or if it placed in a very dark room. It should stop playing the tone once exposd to the usual light of a Singer Hall classroom.

```python
from adafruit_circuitplayground import cp

while True:
    if cp.light < 10:
        cp.start_tone(440)
    else:
        cp.stop_tone()

```

