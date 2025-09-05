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

def lerp_point(a, b, x):
    return (a[0] + x*(b[0]-a[0]), a[1] + x*(b[1]-a[1]))

######################################################################
# function to move pen from plotter.get_pen_pos() to dst, both
# specified in mm, at a constant speed of MOVE_SPEED mm/s

def move_linear(plotter, dst):

    #alpha, beta = ik(dst)
    #plotter.set_angles(alpha, beta)
    #sleep(1.0)
    #return

    org = plotter.get_pen_pos()

    x0, y0 = org
    x1, y1 = dst

    d = sqrt((x1-x0)**2 + (y1-y0)**2)

    if d == 0.0:
        return

    t = d / MOVE_SPEED

    start = monotonic_ns()

    u = 0

    while u < 1.0:

        now = monotonic_ns()
        elapsed = (now - start) * 1e-9

        u = min(elapsed/t, 1.0)

        p = lerp_point(org, dst, u)

        alpha, beta = ik(p)
        plotter.set_angles(alpha, beta)

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
                print('driving from', plotter.get_pen_pos(), 'to', p)
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
                        print('pen up at ', plotter.get_pen_pos())
                        plotter.pen_up()
                    else:
                        pen_was_down = plotter.is_pen_down()
                        x, y = line.split()
                        x = float(x)
                        y = float(y)
                        move_linear(plotter, (x, y))
                        if not pen_was_down:
                            plotter.pen_down()
                            print('pen down at ', plotter.get_pen_pos())

            print('finished!')
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

#lab3_ex3()
lab3_ex4()

