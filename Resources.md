---
title: Resources
---

# Guides and Tutorials

  * [Official Python website](https://www.python.org/downloads/)
  * [Virtual Environments in Python](https://docs.python.org/3/tutorial/venv.html)
  * [Guide to using the Circuit Playground Express](CPX_guide.html)
  * [Official CircuitPython documentation](https://docs.circuitpython.org/en/latest/README.html) --- use this page to look up the full documentation for functions.
  * [Download Mu](https://codewith.mu/), the simple IDE for Python and CircuitPython
  * [Download CircuitPython for the Circuit Playground Bluefruit](https://circuitpython.org/board/circuitplayground_bluefruit/) --- this provides the library `adafruit_circuitplayground`, which contains high-level wrappers for most Circuit Playground functionality.
  * [Product page for the Circuit Playground Bluefruit](https://www.adafruit.com/product/4333)
  * [Official Guide for the Circuit Playground Bluefruit](https://learn.adafruit.com/adafruit-circuit-playground-bluefruit/overview)

# Links and Code Snippets

## Lec 1.1

1. [Installing Circuit Python on your Circuit Playground Bluefruit](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython). This will install Circuit Python, a compact and pared-down version of Python for embedded systems.
2. [Installing Mu on your computer](https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor). This is the IDE that we will use for Circuit Playground.
3. [Downloading Libraries and copying them on to Circuit Playground Bluefruit](https://docs.circuitpython.org/projects/circuitplayground/en/latest/). Make sure you use the libraries from Circuit Python 9! Note that you must copy 2 folders and 3 files into the `lib` folder of your Circuit Playground device.


`)``python
from adafruit_circuitplayground import cp

while True:
    cp.pixels[4] = (10,0,10)
    if cp.button_a:
         cp.play_tone(440,1)
    if cp.button_b:
         cp.play_tone(220,1)
```
