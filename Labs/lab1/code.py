import time
import board
import touchio
from adafruit_circuitplayground import cp

# Define some colors we will use in this lab.
BLACK = (0, 0, 0)
RED =   (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

######################################################################
# Helper function to wait for capacitive touch and release.
# Returns a list of pins that were touched, e.g. [board.A1].
def wait_for_touch(delay_ms):

    # NOTE: students should not edit this function!

    delay_s = delay_ms * 0.001

    print('waiting for ready...')

    ready_start = None

    while True:
        pins = cp.touched
        if pins:
            ready_start = None
        elif ready_start is None:
            ready_start = time.monotonic()
        elif time.monotonic() - ready_start > delay_s:
            break
        time.sleep(0.005)

    print('ready, waiting for touch...')

    touch_start = None

    while True:
        pins = cp.touched
        if not pins:
            touch_start = None
        elif touch_start is None:
            touch_start = time.monotonic()
        elif time.monotonic() - touch_start > delay_s:
            return pins
        time.sleep(0.005)


######################################################################
# Helper function to wait for a press of button A or button B
# on the Circuit Playground Express. Don't press the reset button
# by mistake!
def wait_for_button():
    # NOTE: students should not edit this function!
    print('waiting for button...')
    while not cp.button_a and not cp.button_b:
        pass

######################################################################
# Helper functon that must be called once before wait_for_touch().
# Check each pin once before inspecting cp.touched,
# otherwise it won't show up in that list later.
def initialize_touch():
    # NOTE: students should not edit this function!
    cp.touch_A1
    cp.touch_A2
    cp.touch_A3
    cp.touch_A4
    cp.touch_A5
    cp.touch_A6
    cp.touch_A7

######################################################################
# Run this function to complete exercise 1.
# Don't forget to uncomment it at the bottom of the file!
def lab1_ex1():

    # NOTE: Students should not edit this function!

    touch = touchio.TouchIn(board.A1)

    while True:
        reading = touch.raw_value
        print((reading,))
        time.sleep(0.05)


######################################################################
# Run and modify this function to complete exercise 4.
# Don't forget to uncomment it at the bottom of the file!
def lab1_ex2():

    # The wait_for_touch() function will not work
    # unless you call the initialize_touch() function
    # once at the start of your program.
    initialize_touch()

    # We can call cp.adjust_touch_threshold before dealing with
    # capacitive touch inputs to reduce the sensitivity a bit.
    # The default is often a bit too sensitive.
    cp.adjust_touch_threshold(0)

    # Set the master brightness of the NeoPixels, you may
    # want to crank this up when shooting video.
    cp.pixels.brightness = 0.1

    while True:

        # Sample the touch pins
        pins = wait_for_touch(50)

        print('you touched:', pins)

######################################################################
# Run and modify this function to complete exercise 4.
# Don't forget to uncomment it at the bottom of the file!
def lab1_ex3():

    # The wait_for_touch() function will not work
    # unless you call the initialize_touch() function
    # once at the start of your program.
    initialize_touch()

    # We can call cp.adjust_touch_threshold before dealing with
    # capacitive touch inputs to reduce the sensitivity a bit.
    # The default is often a bit too sensitive.
    cp.adjust_touch_threshold(0)

    # Set the master brightness of the NeoPixels, you may
    # want to crank this up when shooting video.
    cp.pixels.brightness = 0.1

    while True:

        # Turn all NeoPixels off
        cp.pixels.fill(BLACK)

        # Sample the touch pins
        pins = wait_for_touch(50)

        print('you touched:', pins)

        # TODO: put your code to implement Exercise 3 here!
        cp.pixels.fill(WHITE)

        # At the bottom of this while True loop we always
        # wait for a button press, which resets the loop
        # and returns back to the top.
        wait_for_button()


######################################################################
# Run and modify this function to complete exercise 4.
# Don't forget to uncomment it at the bottom of the file!
def lab1_ex4():

    # The wait_for_touch() function will not work
    # unless you call the initialize_touch() function
    # once at the start of your program.
    initialize_touch()

    # We can call cp.adjust_touch_threshold before dealing with
    # capacitive touch inputs to reduce the sensitivity a bit.
    # The default is often a bit too sensitive.
    cp.adjust_touch_threshold(0)

    # Set the master brightness of the NeoPixels, you may
    # want to crank this up when shooting video.
    cp.pixels.brightness = 0.1

    while True:

        # TODO: replace the interior of this loop with your
        # completed loop code from lab4_ex3().

        cp.pixels.fill(BLACK)
        time.sleep(0.5)

        cp.pixels[0] = GREEN
        time.sleep(0.5)

        cp.pixels[1] = GREEN
        time.sleep(0.5)

        cp.pixels[2] = GREEN
        time.sleep(0.5)

        cp.pixels.fill(WHITE)
        time.sleep(0.5)

######################################################################
# Run and modify this function to complete exercise 4.
# Don't forget to uncomment it at the bottom of the file!
def lab1_ex5():
    # TODO: delete the loop below, and paste in a copy
    # of all of the lines inside your lab1_ex4() function.
    while True:
        print("oops haven't started Exercise 5 yet...")
        time.sleep(0.5)

######################################################################
# Our main program starts below this line.
# Make sure only one of the lines below is un-commented!

lab1_ex1()
#lab1_ex2()
#lab1_ex3()
#lab1_ex4()
#lab1_ex5()
