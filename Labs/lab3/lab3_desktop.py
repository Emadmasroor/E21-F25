import numpy
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

l1 = 30.0
l2 = 50.0

alpha_min = -numpy.pi/4
alpha_max = 3*numpy.pi/4

beta_min = numpy.pi/4
beta_max = 5*numpy.pi/4

######################################################################
# Computes forward kinematics of the pen plotter robot

def fk(alpha, beta):
    
    P = l2 * numpy.array([numpy.cos(alpha), numpy.sin(alpha)])
    Q = l1 * numpy.array([numpy.cos(beta), numpy.sin(beta)])

    R = P + Q
    S = P - (l2/l1) * Q

    return P, Q, R, S

######################################################################
# Computes the intersection of two circles centered at the 
# origin and at point S, both with radius l2.
#
# This function should return None if point S is at the origin, or if
# it lies at a distance 2*l2 or greater from the origin.  Otherwise,
# the function should return the intersection point P such that the
# triangle formed by origin, point S, and point P is wound
# counter-clockwise.

def intersect_circles(S):

    # TODO: replace this with a correct implementation
    return numpy.array([40, 30])

######################################################################
# Computes inverse kinematics for the pen plotter robot.
# If point S is not reachable, this should return None.
# Otherwise, returns a pair of angles (alpha, beta) within the
# joint limits to reach point S with the end effector.

def ik(S):

    # TODO: replace this with a correct implementation
    return (numpy.pi/4, 3*numpy.pi/4)

######################################################################

def plot_robot(P, Q, R, S, 
               line_color='b', 
               point_color='k', 
               text_color='k'):

    O = [0, 0]

    segments = [
        (O, P),
        (O, Q),
        (Q, R),
        (R, S)
    ]

    if line_color is not None:
        for ((x1, y1), (x2, y2)) in segments:
            plt.plot([x1, x2], [y1, y2], line_color + '-')

    points = numpy.array([O, P, Q, R, S])
    labels = 'OPQRS'

    for i, (x, y) in enumerate(points):
        if point_color is not None:
            plt.plot(x, y, point_color + '.')
        if text_color is not None:
            plt.text(x, y, ' ' + labels[i], 
                     ha='left', va='top', color=text_color)


######################################################################
# Exercise 1: Circle intersection

def lab3_ex1():

    # YOU SHOULD NOT MODIFY THIS FUNCTION!
    #
    # Instead, implement intersect_circles above according 
    # to the specification in the assignment.
    #
    # Interpreting the plots: each subplot shows the positions
    # of points O and S along with the two circles of radius
    # l2 centered on those points. 
    #
    # The point P returned from intersect_circles (if any) is plotted
    # as a blue dot. It should lie at the intersection of both
    # circles.
    #
    # See the text output in the console for detailed information
    # about test failures.

    test_cases = [
        ((80, 0), True),
        ((120, 0), False),
        ((0, 0), False),
        ((20, 30), True),
        ((70, -30), True),
        ((25, -60), True)
    ]

    ok = True

    plt.subplot(2, 3, 1)

    print('testing intersect_circles...')
    print()

    for i, ((sx, sy), expect_solution) in enumerate(test_cases):

        S = numpy.array([sx, sy])

        print(f'  calling intersect_circles({S})...')
        
        P = intersect_circles(S)

        print(f'  it returned {P}')

        errors = []

        if expect_solution and P is None:
            errors.append('intersect_circles returned None but expected solution')
        elif not expect_solution and P is not None:
            errors.append('intersect_circles returned a point but no solution expected')

        if P is not None:

            dist_OP = numpy.linalg.norm(P)

            if not numpy.isclose(dist_OP, l2):
                errors.append(f'distance OP is {dist_OP}, expected {l2}')

            dist_PS = numpy.linalg.norm(P - S)

            if not numpy.isclose(dist_PS, l2):
                errors.append(f'distance PS is {dist_PS}, expected {l2}')
            
            if P[0]*S[1] - P[1]*S[0] > 0:
                errors.append('incorrect orientation (wrong choice of P?)')

        if not errors:
            print('  looks good!')
        else:
            print('  found some errors:')
            for error in errors:
                print('    - ' + error)
            
        print()
        
        plt.subplot(2, 3, (i+1))

        plt.gca().add_patch(Circle((0, 0), l2, 
                                   fc='none', ec=[0, 0.5, 0.5]))

        plt.gca().add_patch(Circle(S, l2, 
                                   fc='none', ec=[0, 0.5, 0.5]))

        plt.plot([0, S[0]], [0, S[1]], 'k.')
        plt.text(0, 0, ' O', ha='left', va='top')
        plt.text(S[0], S[1], ' S', ha='left', va='top')

        if P is None:
            plt.annotate('no intersection found', (0.5, 1.0), 
                         xycoords='axes fraction', 
                         ha='center', va='top', color='b')
        else:
            plt.plot(P[0], P[1], 'bo')

        if not errors:
            plt.annotate('pass', (0.5, 0.0), 
                         xycoords='axes fraction', 
                         ha='center', va='bottom', color='g')
        else:
            plt.annotate('FAIL', (0.5, 0.0),
                         xycoords='axes fraction',
                         ha='center', va='bottom', color='r')
        
        plt.axis('equal')

    plt.suptitle('test cases for intersect_circles')
    plt.show()

######################################################################

def lab3_ex2():

    # YOU SHOULD NOT MODIFY THIS FUNCTION!
    #
    # Instead, implement ik above according to the specification in
    # the assignment.
    #
    # Interpreting the plots: each subplot shows the desired end
    # effector position as a green circle.
    #
    # The robot pose returned by ik is plotted in blue.
    #
    # See the text output in the console for detailed information
    # about test failures.

    test_cases = [
        ((30, 20), True),
        ((70, 80), False),
        ((80, 40), True),
        ((0, 0), False),
        ((90, 0), True),
        ((20, 80), True) # <-- UPDATE THAT LINE -- was (30, -50)
    ]

    plt.subplot(2, 3, 1)

    print('testing ik...')
    print()

    for i, ((sx, sy), expect_solution) in enumerate(test_cases):

        
        Sdes = numpy.array([sx, sy])

        print(f'  calling ik({Sdes})...')

        result = ik(Sdes)

        print(f'  it returned {result}')

        errors = []

        if expect_solution and result is None:
            errors.append('ik returned None but expected solution')
        elif not expect_solution and result is not None:
            errors.append('ik returned angles but no solution expected')

        if result is not None:
            
            alpha, beta = result

            if alpha < alpha_min:
                errors.append('alpha less than min limit')
            
            if alpha > alpha_max:
                errors.append('alpha greater than max limit')

            if beta < beta_min:
                errors.append('beta less than min limit')
            
            if beta > beta_max:
                errors.append('beta greater than max limit')

            P, Q, R, S = fk(alpha, beta)

            if P[0]*S[1] - P[1]*S[0] > 0:
                errors.append('incorrect orientation (wrong choice of P?)')

            if not numpy.allclose(Sdes, S):
                errors.append('fk(ik(S)) != S')

        if not errors:
            print('  looks good!')
        else:
            print('  found some errors:')
            for error in errors:
                print('    - ' + error)
            
        print()

        plt.subplot(2, 3, i+1)

        plt.gca().add_patch(Circle(Sdes, 5.0, ec='g', fc='none'))
        
        if result is None:
            plt.annotate('no ik solution found', (0.5, 1.0), 
                         xycoords='axes fraction', 
                         ha='center', va='top', color='b')
        else:
            plot_robot(P, Q, R, S)

        if not errors:
            plt.annotate('pass', (0.5, 0.0), 
                         xycoords='axes fraction', 
                         ha='center', va='bottom', color='g')
        else:
            plt.annotate('FAIL', (0.5, 0.0),
                         xycoords='axes fraction',
                         ha='center', va='bottom', color='r')


        plt.axis('equal')
        
    plt.suptitle('test cases for ik')

    plt.show()
    
######################################################################
# Plots the file whose filename is provided at the top of the
# function.

def lab3_ex5():

    input_filename = 'debug.txt'
    output_filename = input_filename.replace('.txt', '.png')

    # TODO: insert your file reading and plotting code here...

    plt.savefig(output_filename)
    print('saved', output_filename)

    plt.show()

######################################################################

lab3_ex1()
#lab3_ex2()
#lab3_ex5()
