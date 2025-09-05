import numpy
import matplotlib.pyplot as plt
import scipy.linalg

######################################################################

def get_spline_matvec(y_values):

    '''Constructs the A matrix and b vector for a given set of y values
    such that the solution D of the system A*D = b can be further
    refined to give the cubic spline coefficients.

    Parameters: 
    y_values: flat numpy array of length n+1

    Returns:
    A: (n+1) by (n+1) array of coefficients
    b: (n+1) array of right-hand-side values.'''

    n = y_values.shape[0] - 1

    A = numpy.zeros((n+1, n+1))
    b = numpy.zeros_like(y_values)

    # Exercise #1: TODO - comment out the hardcoded lines that set A
    # and b below, and replace them with the general implementation of
    # equation (18) from
    # https://mathworld.wolfram.com/CubicSpline.html
    #
    # I suggest you deal with both using a 'for' loop over rows.  The
    # loop should contain an 'if' statement that deals with three
    # cases: the first row, the last row, and the middle rows.
    #
    # Note that the elements of the current row of the A matrix and b
    # vector will be slightly different in each of the three cases.
    #
    # When you are done, the printed output of A and b in the console
    # should match the commented-out lines here.

    A = numpy.array([
        [2.,  1.,  0.,  0.,  0.,  0.,  0.],
        [1.,  4.,  1.,  0.,  0.,  0.,  0.],
        [0.,  1.,  4.,  1.,  0.,  0.,  0.],
        [0.,  0.,  1.,  4.,  1.,  0.,  0.],
        [0.,  0.,  0.,  1.,  4.,  1.,  0.],
        [0.,  0.,  0.,  0.,  1.,  4.,  1.],
        [0.,  0.,  0.,  0.,  0.,  1.,  2.],
    ])

    b = numpy.array([9., 6., 3., -3., 6., 0., -15.])
        
    ##################################################

    return A, b

######################################################################

def get_coeffs(y_values, D_values):

    '''Computes the n spline coefficients for given sets of n+1 
    y values and n+1 D values.

    Parameters: 
    y_values: flat numpy array of length n+1
    D_values: flat numpy array of length n+1

    Returns:
    coeffs: n by 4 array of matrix coefficients of
            the form ai, bi, ci, di, where the i'th
            spline function is given by 

            Yi(t) = ai + bi * t + ci * t^2 + di * t^3
    '''

    n = y_values.shape[0] - 1

    if y_values.shape != D_values.shape:
        raise RuntimeError('y values and D values should have same shape!')

    coeffs = numpy.zeros((n, 4))

    # Exercise #2: TODO - comment out the line below that creates the
    # hard-coded coeffs array and instead create a coefficient array
    # that successfully implements equations (6) thru (9) from
    # https://mathworld.wolfram.com/CubicSpline.html

    # Column 0 of coeffs should contain the ai's,
    # Column 1 the bi's, etc.

    coeffs = numpy.array([
        [0, 4.43718, 0, -1.43718],
        [3, 0.125641, -4.31154, 3.1859],
        [2, 1.06026, 5.24615, -4.30641],
        [4, -1.36667, -7.67308, 6.03974],
        [1, 1.40641, 10.4462, -6.85256],
        [6, 1.74103, -10.1115, 3.37051],
    ])

    ##################################################

    return coeffs
    
######################################################################

def lab4_fit_1d():

    # get nicer looking printouts from numpy
    # without scientific notation
    numpy.set_printoptions(suppress=True)

    # Exercise #3: TODO - comment out this line, then replace it
    # with a duplicate that modifies, adds, or removes
    # values from the array. If you correctly solved
    # exercises 1 and 2, the plot should look correct regardless.
    y_values = numpy.array([0., 3., 2., 4., 1., 6., 1.])

    A, b = get_spline_matvec(y_values)

    print('A is')
    print(A)
    print()

    print('b is')
    print(b)
    print()

    # Exercise #4: TODO - comment out this line and replace it with a
    # call to scipy.linalg.solve_banded (you will need to represent A
    # in "matrix diagonal ordered form")
    D_values = numpy.linalg.solve(A, b)

    # Get cubic spline coefficients from solution of linear system
    coeffs = get_coeffs(y_values, D_values)

    print('coeffs are')
    print(coeffs)
    print()

    # NOTE: there's nothing for you to modify in the rest of the
    # function -- it is already complete! However, you will likely
    # want to use some of this code below in lab4_fit_2d()

    # n is the number of interior segments in the spline
    n = y_values.shape[0] - 1

    # u is a floating-point array that varies linearly from 0 to n,
    # with 100 points per interior segment
    u = numpy.linspace(0, n, 100*n + 1)

    # for each u, we want the index i of the coefficients for that
    # segment. e.g. for u = 1.21 we want i = 1. as a special case,
    # when u = n exactly, we still want u = (n - 1).
    i = numpy.floor(u).astype(int)
    i[-1] = n - 1

    # t is a parameter that varies from 0 to 1 linearly within each
    # segment.
    t = u - i 

    # fetch the coefficients for each cubic spline segment
    ai = coeffs[i, 0]
    bi = coeffs[i, 1]
    ci = coeffs[i, 2]
    di = coeffs[i, 3]

    # evaluate the splines using Horner's method
    y = ai + t * (bi + t * (ci + t * di))

    # get the integer values of u
    u_values = numpy.arange(n+1)

    # plot discrete u, y values as red dots
    plt.plot(u_values, y_values, 'ro', label='Original data points', zorder=2)

    # plot continuous splines as red curve
    plt.plot(u, y, 'b-', label='Interpolation curve', zorder=1)

    plt.legend()

    plt.title('1D cubic spline interpolation')

    plt.show()


######################################################################

def lab4_fit_2d():

    # get nicer looking printouts from numpy
    # without scientific notation
    numpy.set_printoptions(suppress=True)
    
    x_values = numpy.array([0., 3.5, 6., 4, 2., 4.5, 8.])
    y_values = numpy.array([0., 1., 3., 5., 3., 1., 0.])

    ##################################################
    
    # Exercise 5: TODO - adapt your code from lab4_fit_1d() to obtain
    # two sets of coefficients, one for x and one for y (they should
    # be numpy arrays instead of None). To do this you will need to
    # create two arrays of D_values, one for x, and one for y. Then
    # you'll need to get the corresponding coefficients out of each
    # one. You are free to use the functions defined above.

    x_coeffs = None
    y_coeffs = None

    ##################################################

    # TODO: copy the polynomial evaluation code from lab4_fit_1d() so
    # you can evaluate the x and y splines with 100 points per segment

    plt.plot(x_values, y_values, 'ro', label='Original data points', zorder=2)

    # TODO: replace this plot with the 2D cubic spline interpolation
    plt.plot(x_values, y_values, 'b-', label='Interpolation curve', zorder=1)

    plt.legend()
    plt.axis('equal')

    plt.show()
    

######################################################################

lab4_fit_1d()
#lab4_fit_2d()
