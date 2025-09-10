# Resources

* Table of Contents
{:toc}

## External Guides and Tutorials

  * [Official Python website](https://www.python.org/downloads/)
  * [Virtual Environments in Python](https://docs.python.org/3/tutorial/venv.html)
  * [Official CircuitPython documentation](https://docs.circuitpython.org/en/latest/README.html) --- use this page to look up the full documentation for functions.
  * [Download Mu](https://codewith.mu/), the simple IDE for Python and CircuitPython
  * [Download CircuitPython for the Circuit Playground Bluefruit](https://circuitpython.org/board/circuitplayground_bluefruit/) 
  * [Product page for the Circuit Playground Bluefruit](https://www.adafruit.com/product/4333)
  * [Official Guide for the Circuit Playground Bluefruit](https://learn.adafruit.com/adafruit-circuit-playground-bluefruit/overview)

If Mu does not work for you on Windows, you can follow [these instructions](https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-windows) to use PuTTY as your console as an alernative.

## Instructor's Circuit Playground Guide for E21

To use any of these features, make sure your Python code includes the following line at the top:

- `from adafruit_circuitplayground import cp`


#### Taps and shakes
``````````````````````````````````````````````````````````````````````````````````````````````
cp.shake()  # Returns True if it's currently being shaken
cp.shake(shake_threshold=20)  # optional parameter to change sensitivity

cp.tapped # Returns True if it's currently being tapped
cp.detect_taps  # A variable that can be set to either 1 or 2; 2 looks for double taps.
``````````````````````````````````````````````````````````````````````````````````````````````

#### Switching on the Red LED
```
cp.red_led = True  # switches on the red LED
```

#### Detecting state of Slide switch
```
cp.switch  # returns True or False
```

#### Using the Neopixels
There are 10 neopixels. The state of each is determined by a 3-tuple of RGB values, i.e. `(p,q,r)` where each element of the tuple is an integer between 0 and 255 and represents the red, green and blue channels respectively.

The full state of the neopixels is determined by a 10-element list of 3-tuples, i.e., 30 numbers in total, arranged in the form
```
[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
```
the variable `cp.pixels` contains the above list.

You can set individual elements of the neopixels, e.g., turn the 4th pixel to a mild green like so:
```
cp.pixels[4] = (0,10,0)  # for pixel number 4, set red to 0, green to 10, and blue to 0
```


There is also a convenient method, `cp.pixels.fill()`, which you can use to control all the pixels at the same time. You must pass a 3-tuple to this method.
```
cp.pixels.fill((10,0,0))  # set red channel to a strength of 10 for all the neopixels.
```

#### Reading the light sensor
The light sensor on the Circuit Playground Bluefruit detects ambient light and returns an integer between 0 and ?. Access the curent reading of the light sensor using
```
cp.light
```

#### Reading raw data from the accelerometer
Access the raw data from the accelerometer in meters per seconds squared using

```
cp.acceleration
```
This yields an object of class `acceleration` with three attributes: `x`, `y`, and `z`. Thus,
```
cp.acceleration.z
```
returns the acceleration in the z direction.

#### Physical buttons A and B
There are two buttons on the Circuit Playground Bluefruit, labeled A and B. The boolean variables
```
cp.button_a
cp.button_b
```
are `True` **while** the corresponding buttons are pressed.

#### Temperature sensor
The temperature sensor on the Circuit Playground Bluefruit detects ambient temperature and returns a real number equal to the temperature in Celsius. Access the current temperature in Celsius using
```
cp.temperature
```

#### Capacitive Touch

Seven of the pins on the Circuit Playground Bluefruit can take capacitive touch input.
[image](https://cdn-learn.adafruit.com/assets/assets/000/054/810/large1024/circuitpython_cp_capacitive_touch_pads.jpg?1527982763)

These are A1, A2, A3, A4, A5, A6, and TX. You can see these names on the capacative input regions on the edges of the board, i.e. the mounting holes. The variable `cp.touch_A1` will be `True` when pin `A1` is being touched, and will be `False` otherwise. Thus, there are seven such variables:
- `cp.touch_A1`
- `cp.touch_A2`
- `cp.touch_A3`
- `cp.touch_A4`
- `cp.touch_A5`
- `cp.touch_A6`
- `cp.touch_TX`

#### Speaker
- Play a tone at a frequency of x Hz for a duration of y seconds using `cp.play_tone(x,y)`.
- Start playing a tone at a frequency of x Hz using `cp.start_tone(x)`
- Stop playing the currently-playing tone using `cp.stop_tone()`
- Play a `*.wav` file using `cp.play_file("filename.wav"). The file should be stored on the `CIRCUITPY` drive.

## Links and Code Snippets

### Lec 1.1, Tue Sep 2

#### Installation Instructions

1. [Installing Circuit Python on your Circuit Playground Bluefruit](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython). This will install Circuit Python, a compact and pared-down version of Python for embedded systems.
2. [Installing Mu on your computer](https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor). This is the IDE that we will use for Circuit Playground.
3. [Downloading Libraries and copying them on to Circuit Playground Bluefruit](https://docs.circuitpython.org/projects/circuitplayground/en/latest/). Make sure you use the libraries from Circuit Python 9! Note that you must copy 2 folders and 3 files into the `lib` folder of your Circuit Playground device.

#### Sample First Code to run on your board

```python
from adafruit_circuitplayground import cp

while True:
    cp.pixels[4] = (10,0,10)
    if cp.button_a:
         cp.play_tone(440,1)
    if cp.button_b:
         cp.play_tone(220,1)
```

### Lec 2.1, Tue Sep 9

- `read_pinA1_as_digital_input.py`

```python
from adafruit_circuitplayground import cp
import time

for j in range(200):
    print("Pin A1 digital read:",cp.touch_A1)
    print((int(cp.touch_A1),))
    if cp.touch_A1:
        cp.pixels[3] = (0,25,0)
    else:
        cp.pixels[3] = (25,0,0)
    time.sleep(0.1)
```


- `read_pinA1_as_analog_input.py`

```python
import board
import analogio
import time

pin_a1 = analogio.AnalogIn(board.A1)

for j in range(200):
    print("Pin A1 analog read:",pin_a1.value)
    print((pin_a1.value,))
    time.sleep(0.1)

```


- `read_pinA1_as_analog_input_v2.py`

```python
import board
import analogio
import time
import neopixel

pin_a1 = analogio.AnalogIn(board.A1)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

for j in range(200):
    print("Pin A1 analog read:",pin_a1.value)
    print((pin_a1.value,))
    mapped_brightness = 150 # change this!
    pixels[3] = (0,mapped_brightness,0)
    pixels.show()
    time.sleep(0.1)
```

### Lec 2.2, Thu Sep 11

#### Code for `time` package

```python
from adafruit_circuitplayground import cp

import time

delay = 3.0

print("Switching on pixel 0")
cp.pixels[0] = (0,10,0)
print(f"Waiting for {delay} seconds")
time.sleep(delay)

print("Switching on pixel 1")
cp.pixels[1] = (10,0,0)
print(f"Waiting for {delay} seconds")
time.sleep(delay)

print("Switching on pixel 2")
cp.pixels[2] = (0,0,10)
print(f"Waiting for {delay} seconds")
time.sleep(delay)
```


