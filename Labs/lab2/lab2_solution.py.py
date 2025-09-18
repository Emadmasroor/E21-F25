from board import A1, A2, A3
from adafruit_circuitplayground import cp
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull
from time import sleep
from lab2_util import rgb_from_hsv, run_tests

# Define some constants at the top of our file:

# Coordinates of NeoPixels relative to center
# of the board.
NEOPIXEL_COORDS = [
    (-0.500, 0.866),
    (-0.866, 0.500),
    (-1.000, 0.000),
    (-0.866, -0.500),
    (-0.500, -0.866),
    (0.500, -0.866),
    (0.866, -0.500),
    (1.000, 0.000),
    (0.866, 0.500),
    (0.500, 0.866)
]

# Number of bits of the ADCs on the CPX.
# TODO: set this to the correct value!
ADC_BITS = 16

# Maximum ADC reading on the CPX.
# Do not edit this directly, instead modify
# ADC_BITS above.
ADC_MAX = 2**ADC_BITS - 1

######################################################################
# Computes the linear interpolation between a and b.
#
# When x = 0, returns a.
# When x = 1, returns b.
# Return value varies linearly for all other values of x.

def lerp(a, b, x):
    # TODO: implement this function correctly!
    return x*(b-a) + a

######################################################################
# Computes the inverse linear interpolation between a and b.
#
# When c = a, returns 0.
# When c = b, returns 1.
# Return value varies linearly for all other values of x.

def unlerp(a, b, c):
    # TODO: implement this function correctly!
    return (c-a)/(b-a)

######################################################################
# Linearly remaps the input interval [a, b]
# to the output interval [s, t]

def remap(a, b, s, t, c):
    # TODO: implement this function correctly!
    return lerp(s,t,unlerp(a,b,c))

######################################################################
# Demonstrates how to read joystick values for plotting.

def lab2_ex1():

    # DO NOT MODIFY THIS FUNCTION!

    vert = AnalogIn(A3)
    horiz = AnalogIn(A2)

    sel = DigitalInOut(A1)
    sel.direction = Direction.INPUT
    sel.pull = Pull.UP

    while True:

        trace1 = vert.value
        trace2 = horiz.value

        if not sel.value:
            trace3 = max(trace1, trace2)
        else:
            trace3 = 0

        print((trace1, trace2, trace3))

        sleep(0.05)

######################################################################
# Tests your implementations of lerp, unlerp, and remap.

def lab2_ex2():

    # DO NOT MODIFY THIS FUNCTION!

    def on_pass():
        cp.play_tone(1046, 0.1)
        cp.play_tone(1319, 0.1)
        cp.play_tone(1568, 0.1)

    def on_fail():
        cp.play_tone(220, 1.0)

    tests = [

        ('lerp', lerp, [
            ((10, 20, 0.0), 10),
            ((10, 20, 0.5), 15),
            ((10, 20, 1.0), 20),
            ((3, 0, 0.66666666), 1),
            ((0, 10, 1.5), 15),
            ((0, 10, -0.5), -5)
        ]),

        ('unlerp', unlerp, [
            ((10, 20, 10), 0.0),
            ((10, 20, 15), 0.5),
            ((10, 20, 20), 1.0),
            ((3, 0, 1), 0.666666666),
            ((0, 10, 15), 1.5),
            ((0, 10, -5), -0.5)
        ]),

        ('remap', remap, [
            ((10, 20, 1, 2, 10), 1),
            ((10, 20, 1, 2, 20), 2),
            ((10, 20, 2, 1, 0), 3),
            ((10, 20, 2, 1, 30), 0)
        ])

    ]

    run_tests(tests, on_pass=on_pass, on_fail=on_fail)

######################################################################
# Remaps joystick horizontal axis to hue and vertical axis to value.

def lab2_ex3():

    vert = AnalogIn(A3)
    horiz = AnalogIn(A2)

    cp.pixels.brightness = 0.25

    while True:

        # TODO: replace these lines with two calls to remap
#         H = 180.0
#         V = 0.5
        H = remap(0,ADC_MAX,300,0,horiz.value)
        V = remap(0,ADC_MAX,0,1,vert.value)

        cp.pixels.fill(rgb_from_hsv(H, 1.0, V))


######################################################################
# Turns on a single NeoPixel to white based on joystick angle.

def lab2_ex4():

    vert = AnalogIn(A3)
    horiz = AnalogIn(A2)

    cp.pixels.brightness = 0.25

    while True:

        k = 32767.5
        u = 1 - horiz.value / k
        v = vert.value / k - 1

        # TODO: use the joystick u & v values here
        cp.pixels.fill((0, 0, 0))

        if max(abs(u), abs(v)) > 0.9:

            max_pi = None
            max_i = None

            for i, (xi, yi) in enumerate(NEOPIXEL_COORDS):
                pi = xi * u + yi * v
                if max_pi is None or pi > max_pi:
                    max_pi = pi
                    max_i = i

            cp.pixels[max_i] = (255, 255, 255)
######################################################################
# Individually controls NeoPixels based on joystick inputs.

def lab2_ex5():

    vert = AnalogIn(A3)
    horiz = AnalogIn(A2)

    sel = DigitalInOut(A1)
    sel.direction = Direction.INPUT
    sel.pull = Pull.UP

    cpx.pixels.brightness = 0.25

    while True:

        # TODO: delete the line below and insert your own code
        pass

######################################################################

# lab2_ex1()
# lab2_ex2()
# lab2_ex3()
lab2_ex4()
#lab2_ex5()
