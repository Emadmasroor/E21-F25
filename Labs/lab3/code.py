import board
from jankyplotter import JankyPlotter, ik
from time import monotonic_ns, sleep
from math import sqrt, ceil, pi
from adafruit_circuitplayground.express import cpx

MOVE_SPEED = 50.0 # mm/s

######################################################################
# waits for a button press on A or B

def wait_for_button():
    while not (cpx.button_a or cpx.button_b):
        sleep(0.05)

######################################################################
# function to move pen from plotter.get_pen_pos() to dst, both
# specified in mm, at a constant speed of MOVE_SPEED mm/s

def move_linear(plotter, new_pos):

    # here is how to get the current pen position
    cur_pos = plotter.get_pen_pos()

    # TODO: delete this and replace with a correct implementation
    # of the specification from the assignment
    alpha, beta = ik(new_pos)
    plotter.set_angles(alpha, beta)
    sleep(1.0)

######################################################################
# Exercise 3: Motion along a line segment

def lab3_ex3():

    # DO NOT MODIFY THIS FUNCTION
    # instead, just implement move_linear above!

    points = [
        (30, 25),
        (80, 25),
        (80, -25),
        (30, -25)
    ]

    alpha, beta = ik(points[-1])

    plotter = JankyPlotter(board.A1, board.A2, board.A3,
                           alpha_home=alpha, beta_home=beta)

    print('load a pen and press button A or B when ready')

    wait_for_button()

    plotter.pen_down()

    try: # check for errors/interruptions

        while True:
            for p in points:
                print('driving to', p)
                move_linear(plotter, p)

    except:

        # if an error/interruption happens, pick up the pen
        # and pass along the error somewhere else
        plotter.pen_up()
        raise

######################################################################
# Exercise 4: State machine for drawing

def lab3_ex4():

    # DO NOT MODIFY ANYTHING OUTSIDE OF THE while LOOP BELOW

    plotter = JankyPlotter(board.A1, board.A2, board.A3)

    print('load a pen and press button A or B to start drawing...')
    wait_for_button()

    try: # check for errors/interruptions

        while True:

            with open('hello.txt') as istr:

                for line in istr:
                    line = line.strip()
                    if not line:
                        # we read a blank line

                        # TODO: replace the "pass" line below
                        # with your own code...
                        pass
                    else:
                        # we read an X Y line
                        x, y = line.split()
                        x = float(x)
                        y = float(y)

                        # TODO: replace the "pass" line below
                        # with your own code...
                        pass

            plotter.pen_up()
            plotter.go_home()

            print('press button A or B to draw again...')
            wait_for_button()

    except:

        # if an error/interruption happens, pick up the pen
        # and pass along the error somewhere else
        plotter.pen_up()
        raise

######################################################################

lab3_ex3()
#lab3_ex4()

