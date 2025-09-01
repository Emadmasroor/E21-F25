# Guides and Tutorials

  * [Official Python website](https://www.python.org/downloads/)
  * [Virtual Environments in Python](https://docs.python.org/3/tutorial/venv.html)
  * [Guide to using the Circuit Playground Express](CPX_guide.html)
  * [Official CircuitPython documentation](https://docs.circuitpython.org/en/latest/README.html) --- use this page to look up the full documentation for functions.
  * [Download Mu](https://codewith.mu/), the simple IDE for Python and CircuitPython
  * [Download CircuitPython for the Circuit Playground Express](https://circuitpython.org/board/circuitplayground_express/) --- this provides the library `adafruit_circuitplayground`, which contains high-level wrappers for most CPX functionality.
  * [Product page for the Circuit Playground Bluefruit](https://www.adafruit.com/product/4333)
  * [Official Guide for the Circuit Playground Bluefruit](https://learn.adafruit.com/adafruit-circuit-playground-bluefruit/overview)

# Code Snippets

## Lec 1.1

```
from adafruit_circuitplayground import cp

while True:
    cp.pixels[4] = (10,0,10)
    if cp.button_a:
         cp.play_tone(440,1)
    if cp.button_b:
         cp.play_tone(220,1)
```
