Note: Gradescope only allows a single PDF file in one submission. Therefore, you will combine your non-code files into a single PDF. Turn in the following files for this assignment on Moodle / Gradescope.

* A file titled `HW2.pdf` for problem 1 and problem 3.2
* A Python file titled `analog_digital.py` for problem 2
* A file titled `reaction_time.py` for problem 3.1

There is a separate submission page for the PDF and for Python files.

# Base Systems

For the problems in this section, you must turn in a PDF. It can be either handwritten or typed. 

For full credit, **show how you arrived at your answers**, don't just write the correct answers!

## Decimal / Binary

### Convert the following integers from decimal to binary:
* `100`
* `59`
* `250`
* `476`

### Conver the following integers from binary to decimal:
* `0b110001`
* `0b1000001`
* `0b1010101011`

## Decimal / Hexadecimal

### Convert the following integers from decimal to hexadecimal:
* `1000`
* `597`
* `42678`
* `250`

### Convert the following integers from hexadecimal to decimal:
* `0x14E3`
* `0xA10B`
* `0x1000`
* `0x1010`

## Addition and multiplication of numbers
In grade school, you learned how to add two multi-digit numbers by hand. In case, you've forgotten, [here's](https://www.youtube.com/watch?v=5Vj50p4k6i8) a video explaining this to elementary school students.

Your task in this problem is to explain how the same concept of 'carrying over' a digit (perhaps you learned the term 'regrouping') applies to binary and hexadecimal numbers. Write out, by hand,

1. The sum `0b110001` + `0b11011`
2. The sum `0b1001110` + `0b1101`
3. The sum `0xAFC` + `0x115`
4. The sum `0xE5A` + `0x85A`
5. The product `0x353` times `0x3`


For each arithmetic problem you write (5 total), write down the same calculation in decimal form as well (no need to do these `by hand`). For example, if you were showing that 

```
0b101 + 0b100 = 1001
```

then you would show the process 'by hand' as in the YouTube video above.  
In addition, you would write --- without explanation since this is not elementary school --- the line

```
5 + 4 = 9
```

You will not get credit for this problem if you simply write down correct answers. e.g., if you write down `10010 x 10111 = 101001`. You have to _show your work_!

# Analog vs Digital on Circuit Python Bluefruit
In this problem, you will write a CircuitPython script that will use the Circuit Python Bluefruit' light sensor (an _analog_ signal) to create a digital signal if the on-board slide switch is moved to one side and an analog signal if the on-board slide switch is moved to the other side. Your program will be placed inside the `while True:` block that we have been using in this class, and should accomplish the following objectives:

1. If the slide switch is in the 'off' position, it should continuously plot the light intensity in lux in intervals of `0.2` seconds. Meanwhile, pixel 4 should be dimly lit to a purple hue, and all other pixels should be off. This is the 'analog mode'.
2. If the slide switch is in the 'on' position, it should treat the light sensor as a digital signal, and continuously plot `1` (every `0.2` seconds) if the light sensor is exposed to the light inside a Singer Hall classroom, and plot `0` if the CPX is covered with your hand. In this mode, the board should play a tone of `440` Hz whenever it is covered by your hand, and should stop playing this tone when uncovered. Meanwhile, during this mode, pixel 5 should be dimly lit continuously to a yellow hue, and all other pixels should be off. This is the 'digital mode'.

Some further requirements:
* It is up to you to choose a 'threshold value'; however, the value you choose should work such that, when the CPX is placed in a well-lit room in Singer Hall, your program should plot `1`, and when you cover it with your hand about 2-3 inches above the board, your program should plot zero.
* It should be possible to move the slide switch back and forth repeatedly and switch the 'mode' from digital to analog.
* You should use the [calibration curve](../Lecs/calibration1.png) from the in-class activity on September 12.

!!! Tip
   If you're not sure where to start, you might want to start by modifying the files used in class.

!!! Tip
   The graders will copy your code into their board's `code.py` and will run it. There may be small differences from board to board, but your code _should work_ when saved on a CPX. We will grade by checking if our board works with your code, so test it out thoroughly on your own board!
 
# Measuring your reaction time
In this problem, you will measure your own reaction time using the Circuit Playground Bluefruit. The code provided to you lights up an LED at an unpredictable time, and you are supposed to press button A on the board when you see the LED light up. The program then reports your reaction time, i.e., the time between when the LED was lit and the button was pressed.

Currently, it collects data through 5 button presses only.

~~~python

from adafruit_circuitplayground import cp
import time
import random

# Choose the number of data points to collect
N = 5

# Create a list to collect data points
data = [0] * N

for j in range(N):
    # Turn off all LEDs
    cp.pixels.fill((0, 0, 0))

    # Wait for a random time between 1 and 5 seconds
    random_delay = random.uniform(1, 5)
    time.sleep(random_delay)
    # Turn on a random LED (pick an index from 0 to 9)
    led_index = random.randint(0, 9)
    cp.pixels[led_index] = (0, 10, 0)  # Green LED lights up

    # Record the time the LED lights up
    start_time = time.monotonic()

    # Wait for button A press
    while not cp.button_a:
        # do nothing; keep waiting in this while loop
        pass

    # Button pressed! First, calculate the reaction time.
    reaction_time = time.monotonic() - start_time

    # Switch off the LED
    cp.pixels[led_index] = (0,0,0)

    # Print the reaction time to the serial console
    print(f"Reaction time: {reaction_time:.3f} seconds")

    # Assign data to a list
    data[j] = reaction_time

    # Pause before restarting the game
    time.sleep(2)

~~~

## Modify the program

Paste the code above into `code.py` on your device. Then, download the file `[statistical_functions.py](statistical_functions.py)` and place it inside your `CIRCUITPY` drive. Then, add the line `from statistical_functions import std` at the top of your `code.py` file. This imports a function `std` that calculates the standard deviation of a list of numbers.

### Tasks

1. Modify the code so that, in addition to printing the reaction time for each press, the mean and standard deviation are also printed at the end of the data-collection process.
2. Modify the code so that, if the slide switch is set to one side, a random LED (out of the ten LEDs in a circular arrangement) lights up. If the slide switch is set to the other side, the _same_ LED lights up. Thus, there should be two _modes_ of operation: in one mode, a random LED lights up; in the other mode, the same LED lights up.
3. Modify the code so that it collects more data points --- as many as you think are appropriate to get an _accurate_ and _precise_ measurement of your reaction time.

Turn in your modified program. To do this, name the file `reaction_time.py` instead of `code.py`.

## Use the program

Run the code that you developed to collect some real-world data on reaction times. Collect a table of values in each of the two modes (random LED & fixed LED), and determine the mean and standard deviation of your collected data in both modes.

Turn in one paragraph of text, your data table, and a chart summarizing your results, and comment on whether your reaction time was different in the two modes. Also explain how precise and how accurate you think these measurements are. 

The word 'chart' can be interpreted broadly: you can take a piece of graph paper and plot some data on an appropriate set of axes, or you can use Excel, or you can use some other program that you are familiar with. The goal is to convey what you've learned about your own reaction time using this experiment, and to tell a reader what you can say about the accuracy and precision. There is no need to include your data as a separate file; everything should just be embedded into your PDF.

An example of the kind of chart that would be acceptable is shown below.

![reaction times chart](reaction_time.png)

