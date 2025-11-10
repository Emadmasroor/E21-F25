# starter code for E21 Lab 5
# originally written by Matt Zucker in Fall 2022

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Ellipse
import scipy.optimize
import time


# each gaussian function is defined by six parameters:
#
#       a: amplitude/weight
#      xc: x center point in pixels
#      yc: y center point in pixels
#      su: gaussian size in u direction
#      sv: gaussian size in v direction
#   theta: angle of u axis with respect to image x axis

PARAMS_PER_BASIS_FUNC = 6

######################################################################
# bounds for gaussian function parameters, for an image with w cols
# and h rows

def get_bounds(w, h):

    lo = np.array([ -1.0, 0.0, 0.0,   1.0,   1.0, -np.pi ])
    hi = np.array([  1.0,   w,   h, 0.2*w, 0.2*h,  np.pi ])

    return lo, hi

######################################################################
# create a set of random initial gaussian function paramters for an
# image with given dimensions, and given the desired count of gaussian
# functions
#
# note that each gaussian function has six parameters but instead
# of returning a 2D array of size count-by-6, we instead return
# flat array of size (count*6)

def rand_params(w, h, count):

    # create lower and upper bounds for random gaussian function
    # parameters
    lo, hi = get_bounds(w, h)

    # sample uniformly in between lower and upper bounds
    q = np.random.uniform(lo, hi, (count, PARAMS_PER_BASIS_FUNC))

    # convert to float32 for quicker reconstruction
    q = q.astype(np.float32)

    # take 2d array and flatten down to 1d array
    return q.flatten()

######################################################################
# create an image as a sum of gaussian functions given x and y
# coordinates of each pixel location

def make_image_loops(q, xmesh, ymesh):

    # reshape from flat array to n-by-6 array of params
    q = q.reshape(-1, PARAMS_PER_BASIS_FUNC)

    # initialize output to zeros
    gimg = np.zeros_like(xmesh)

    # for each gaussian function
    for (a, xc, yc, su, sv, theta) in q:

        # get cosine and sine of rotation angle
        ct = np.cos(theta)
        st = np.sin(theta)

        # subtract out the x/y center of the gaussian function
        xs = xmesh - xc
        ys = ymesh - yc

        # decompose into u/v coordinate system
        u = xs*ct - ys*st
        v = xs*st + ys*ct
        
        # add contribution of gaussian function to output image
        # note scaled by amplitude of this individual function
        gimg += a * np.exp( -u**2 / (2*su**2)  - v**2 / (2*sv**2) )

    # return the summed image
    return gimg

def make_image_vectorized(q, xmesh, ymesh):
    # Reshape q from (k*6,) to (k, 6)
    q = q.reshape(-1, PARAMS_PER_BASIS_FUNC)
    
    # 1. Prepare parameters for broadcasting
    # k = number of Gaussians.
    # We want dimensions (k, 1, 1) for broadcasting with (h, w)
    
    # Extract parameters
    a     = q[:, 0, np.newaxis, np.newaxis] # Amplitudes (k, 1, 1)
    xc    = q[:, 1, np.newaxis, np.newaxis] # x centers (k, 1, 1)
    yc    = q[:, 2, np.newaxis, np.newaxis] # y centers (k, 1, 1)
    su    = q[:, 3, np.newaxis, np.newaxis] # sigma_u (k, 1, 1)
    sv    = q[:, 4, np.newaxis, np.newaxis] # sigma_v (k, 1, 1)
    theta = q[:, 5, np.newaxis, np.newaxis] # angle (k, 1, 1)
    
    ct = np.cos(theta) # (k, 1, 1)
    st = np.sin(theta) # (k, 1, 1)

    # 2. Coordinate Transformation (Broadcasting)
    # xmesh, ymesh are (h, w). xmesh - xc is (k, h, w)
    xs = xmesh - xc # (k, h, w)
    ys = ymesh - yc # (k, h, w)

    # u = xs*ct - ys*st
    u = xs * ct - ys * st # (k, h, w)
    # v = xs*st + ys*ct
    v = xs * st + ys * ct # (k, h, w)
    
    # 3. Gaussian Calculation (Broadcasting)
    # The exponent term (k, h, w)
    exponent = - (u**2 / (2*su**2) + v**2 / (2*sv**2))
    
    # Gaussian contribution (k, h, w)
    g_contrib = a * np.exp(exponent)
    
    # 4. Sum contributions
    # Sum along the first axis (k) to get the final image (h, w)
    gimg = np.sum(g_contrib, axis=0)
    
    return gimg


######################################################################
# utility function to plot outlines of Gaussian ellipses on a figure

def plot_gaussian_ellipses(ax, q):

    q = q.reshape(-1, PARAMS_PER_BASIS_FUNC)

    for (a, xc, yc, su, sv, theta) in q:

        red = np.clip(0.5*a + 0.5, 0, 1)
        blue = 1-red

        ei = Ellipse(xy=(xc,yc),
                     width=3*su, height=3*sv,
                     angle=-theta*180/np.pi)
        
        ei.set_facecolor('none')
        ei.set_edgecolor([red, 0, blue])
        ax.add_artist(ei)

######################################################################
# nice imshow that uses grayscale colormap, makes pixels chunky
# squares, and turns axis ticks off.

def imshow_nice(ax, img, cmap='gray'):
    ax.imshow(img, cmap=cmap, interpolation='nearest')
    ax.set_axis_off()

######################################################################
# save parameters to a text file

def save_params(filename, q):
    np.savetxt(filename, q, fmt='%f')
    print('wrote', filename)

######################################################################
# save image data to file

def save_image(filename, img, scale, bias):

    img = img * scale + bias

    mpimg.imsave(filename, img, vmin=0.0, vmax=1.0, cmap='gray')

    print('wrote', filename)
    
######################################################################

def main():

    # seed the random number generator so we get the same initial
    # random weights each time we run the program (otherwise we would
    # have different results for each program run, which can be hard
    # to debug while you are learning the course material!)
    np.random.seed(12345)

    input_filename = 'eye.png'

    gaussian_count = 16

    # read the input image and convert it to floating point
    target = mpimg.imread(input_filename).astype(np.float32)

    if len(target.shape) == 3:
        raise RuntimeError('only grayscale images are supported right now')

    h, w = target.shape

    print(f'image {input_filename} has width {w} and height {h}')

    # rescale target to have mean zero and lie in [-1, 1] range
    #
    # this is not technically necessary but helps the optimization
    # converge a bit faster

    bias = target.mean()

    target -= bias # set mean to zero

    scale = np.abs(target).max()

    target /= scale # set to be within [-1, 1] interval

    xrng = np.arange(w, dtype=np.float32)
    yrng = np.arange(h, dtype=np.float32)

    xmesh, ymesh = np.meshgrid(xrng, yrng)

    ##################################################################
    # inner functions for optimization

    # reconstruct an image
    def recons(q):
        # calls make_image function above using
        # the xmesh, ymesh variables defined in main
        return make_image_vectorized(q, xmesh, ymesh)

    # compute an "error image" showing good fit = close to zero, poor
    # fit = high magnitude pixels
    def err_img(q):
        return target - recons(q)

    # reshapes the 2D h-by-w image into a flat array of length (h*w)
    def err_vec(q):
        return err_img(q).flatten()

    # the objective function computes squared norm of the error vector
    def objective(q):
        e = err_vec(q)
        return np.dot(e, e)

    # reconstruct an image
    def recons_loops(q):
        # calls make_image function above using
        # the xmesh, ymesh variables defined in main
        return make_image_loops(q, xmesh, ymesh)

    # compute an "error image" showing good fit = close to zero, poor
    # fit = high magnitude pixels
    def err_img_loops(q):
        return target - recons_loops(q)

    # reshapes the 2D h-by-w image into a flat array of length (h*w)
    def err_vec_loops(q):
        return err_img_loops(q).flatten()
    
    ##################################################################
    # Note: you can replace all of the code below this line with
    # your solution for exercise 2.

    # TODO: comment this line out or delete it
    # q = np.genfromtxt('example_params.txt')


    # TODO: uncomment this line!
    # q = rand_params(w, h, gaussian_count)

    # print('initial objective value:', objective(q))

    # # TODO: optimize q to improve the objective function value!
    # q_res = scipy.optimize.minimize(objective, q, method="Powell", options=dict(maxfev=10000))
    # print('q_res: ',q_res.x)

    # img = recons(q_res.x)
    NUM_TRIALS = 5

    start_time = time.perf_counter()
    best_params = [[None for j in range(3)] for i in range(3)]
    means = [[None for j in range(3)] for i in range(3)]
    stds = [[None for j in range(3)] for i in range(3)]
    costs = [[[None for trial in range(NUM_TRIALS)] for j in range(3)] for i in range(3)]

    for i,k in enumerate([8, 16, 32]):
        for j,method in enumerate(['Powell', 'L-BFGS-B', 'trf']):
            min_cost = float('inf')
            for trial in range(NUM_TRIALS):
                q = rand_params(w, h, gaussian_count)

                # optimize
                if method == 'Powell':
                    q_res = scipy.optimize.minimize(objective, q, method=method, options=dict(maxfev=10000))
                    cost = objective(q_res.x)
                elif method == 'L-BFGS-B':
                    q_res = scipy.optimize.minimize(objective, q, method=method, jac='2-point', options=dict(maxfun=10000))
                    cost = objective(q_res.x)
                else:
                    q_res = scipy.optimize.least_squares(err_vec_loops, q, method=method, max_nfev=10000)
                    cost = q_res.cost

                # keep track of best trial
                if cost < min_cost:
                    best_params[i][j] = q_res
                    min_cost = cost
                    print('New Min Cost: ',cost)

                # keep track of all costs for statistics
                costs[i][j][trial] = cost

                # status update
                print("Method: ",method,'\t','Gaussian Count: ',k,'Trial: ',trial)
                # print('Cost: ',q_res.cost,'\t','Min Cost: ',best_params[i][j].cost)
                print("Elapsed Time: ",time.perf_counter() - start_time)
                print("================================")

            # calculate means and stds
            means[i][j] = np.mean(costs[i][j])
            stds[i][j] = np.std(costs[i][j])
            img = recons(q_res.x)
            fig, axes = plt.subplots(2, 2)

            ax1, ax2, ax3, ax4 = axes.flatten()

            # below here is just plotting things:
            imshow_nice(ax1, target)
            ax1.set_title('Target (original)')

            n = len(q) // PARAMS_PER_BASIS_FUNC

            imshow_nice(ax2, img)
            ax2.set_title(f'Mixture of {n} Gaussians')

            imshow_nice(ax3, np.abs(target - img))
            ax3.set_title(f'Absolute error (sse={objective(q):.2f})')

            imshow_nice(ax4, img)
            plot_gaussian_ellipses(ax4, q)
            ax4.set_title('Ellipses')

            plt.show()

    # plot results
    x = np.arange(3)  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for i, k in enumerate([8, 16, 32]):
        offset = width * multiplier
        rects = ax.bar(x + offset, means[i], width, label=k)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Error')
    ax.set_title('Gaussian Approximation with Different Optimizers')
    ax.set_xticks(x + width, [8, 16, 32])
    ax.legend(loc='upper left', ncols=3)
    # ax.set_ylim(0, 250)
    print('Total time: ',time.perf_counter() - start_time)

    plt.show()

    ##################################################################
    # demonstrate how to save parameters and images

    save_params('my_params.txt', q)
    save_image('my_image.png', img, scale, bias)

    ##################################################################
    # demonstrate how to plot images and ellipses

    fig, axes = plt.subplots(2, 2)

    ax1, ax2, ax3, ax4 = axes.flatten()

    # below here is just plotting things:
    imshow_nice(ax1, target)
    ax1.set_title('Target (original)')

    n = len(q) // PARAMS_PER_BASIS_FUNC

    imshow_nice(ax2, img)
    ax2.set_title(f'Mixture of {n} Gaussians')

    imshow_nice(ax3, np.abs(target - img))
    ax3.set_title(f'Absolute error (sse={objective(q):.2f})')

    imshow_nice(ax4, img)
    plot_gaussian_ellipses(ax4, q)
    ax4.set_title('Ellipses')

    plt.show()

######################################################################

main()
