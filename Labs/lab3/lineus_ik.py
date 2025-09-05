import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import sys
import numpy as np
from collections import namedtuple
from matplotlib.animation import FuncAnimation

SimState = namedtuple('SimState', 'P, Q, R, S, alpha, beta, elev')

L1 = 30
L2 = 50

S0_MIN = 10

ALPHA_LIMITS = ( -math.pi/4, 3*math.pi/4 )
BETA_LIMITS = ( math.pi/4, 5*math.pi/4 )

AB_DIFF_MIN = 20*math.pi/180
AB_DIFF_MAX = 160*math.pi/180

PEN_SPEED = 10 # mm/s
AB_SPEED = 0.5 # rad/s
LIFT_SPEED = 5 # lifts/s

INTERVAL = 50
SPEEDUP = 3
DELTA_T = INTERVAL * SPEEDUP / 1000.0


def wrap_angle(angle):
    """Wraps a given angle to the [-PI, PI] interval."""
    return ((angle + math.pi) % (2*math.pi)) - math.pi

def angle_diff(b, a):
    """Returns the smallest (magnitude) angle c such that
       wrap_angle(a + c) = wrap_angle(b)"""
    return wrap_angle(b-a)

def wrap_limits(angle, limits):
    center = 0.5*(limits[0] + limits[1])
    return center + angle_diff(angle, center)

def intersect_cc(p0, r0, p1, r1):

    x0, y0 = p0
    x1, y1 = p1

    
    dx = x1 - x0
    dy = y1 - y0

    d2 = dx*dx + dy*dy

    d = math.sqrt(d2)

    if d > r0 + r1:
        return []

    if d <= abs(r0 - r1):
        return []

    a = (r0*r0 - r1*r1 + d2) / (2*d)

    x2 = x0 + a * dx / d
    y2 = y0 + a * dy / d

    if abs(d - a) < 1e-5:
        return [(x2, y2)]

    h = math.sqrt(r0*r0 - a*a)

    rval = []
    
    for s in [-1, 1]:

        x3 = x2 + s*h*dy / d
        y3 = y2 - s*h*dx / d

        rval.append((x3, y3))

    return rval

def from_polar(r, theta):

    x = r * math.cos(theta)
    y = r * math.sin(theta)

    return x, y
    
def is_ccw(a, b, c):

    ax, ay = a
    bx, by = b
    cx, cy = c

    ux, uy = bx-ax, by-ay
    vx, vy = cx-bx, cy-by

    return ux*vy - uy*vx > 0

def lineus_fk(alpha, beta):

    P = from_polar(L2, alpha)
    Q = from_polar(L1, beta)

    px, py = P
    qx, qy = Q
    rx, ry = qx + px, qy + py
    sx, sy = px - qx * L2/L1, py - qy * L2/L1
    
    R = (rx, ry)
    S = (sx, sy)

    return P, Q, R, S

def lineus_ik(S):

    O = (0, 0)
    
    sx, sy = S

    for P in intersect_cc(O, L2, S, L2):
        if is_ccw(S, P, O):
            px, py = P
            
            qx = (px - sx) * L1 / L2
            qy = (py - sy) * L1 / L2
            Q = (qx, qy)
            rx = px + qx
            ry = py + qy
            R = (rx, ry)

            alpha = wrap_limits(math.atan2(py, px), ALPHA_LIMITS)

            beta = wrap_limits(math.atan2(qy, qx), BETA_LIMITS)
            
            return P, Q, R, alpha, beta  

    return None
    

def lineus_config_errors(P, Q, R, S, alpha, beta):

    errors = []

    if alpha < ALPHA_LIMITS[0]:
        errors.append('alpha < lower limit')
        
    if alpha > ALPHA_LIMITS[1]:
        errors.append('alpha > upper limit')

    if beta < BETA_LIMITS[0]:
        errors.append('beta < lower limit')

    if beta > BETA_LIMITS[1]:
        errors.append('beta > upper limit')

    if abs(beta - alpha) < AB_DIFF_MIN:
        errors.append('alpha & beta are too closely aligned')
    
    if abs(beta - alpha) > AB_DIFF_MAX:
        errors.append('alpha & beta are too closely anti-aligned')

    if alpha > beta:
        errors.append('alpha and beta have flipped')

    if not is_ccw(P, R, Q):
        errors.append('PRQ flipped')

    if not is_ccw(S, P, (0, 0)):
        errors.append('SPO flipped')

    if abs(S[0]) < S0_MIN:
        errors.append('S too close to base!')
    
    return errors

def linspace(start, end, cnt):
    assert cnt >= 2
    rval = []
    delta = (end - start)/(cnt-1)
    for i in range(cnt-1):
        rval.append(start + delta*i)
    rval.append(end)
    return rval

def load_contours(filename):
    contour = []
    contours = []
    with open(filename, 'r') as istr:
        for line in istr:
            line = line.strip()
            if not line:
                if contour:
                    contours.append(np.array(contour))
                    contour = []
            else:
                x, y = map(float, line.split())
                contour.append((x, y))
    if contour:
        contours.append(np.array(contour))
    return contours

class SimError(RuntimeError):
    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)

def nsteps(dist, speed):
    duration = dist / speed
    return int(math.ceil(duration / DELTA_T))

def sim_move_to(states, Snew):

    rval = lineus_ik(Snew)

    if rval is None:
        raise SimError('unable to reach ' + str(S))

    x0, y0 = states[-1].S
    elev = states[-1].elev

    alpha0, beta0 = states[-1].alpha, states[-1].beta

    x1, y1 = Snew

    P1, Q1, R1, alpha1, beta1 = rval

    errors = lineus_config_errors(P1, Q1, R1, Snew, alpha1, beta1)
    if errors:
        raise SimError('config errors: ' + 'l '.join(errors))

    if elev == 0:


        d = math.sqrt((x1-x0)**2 + (y1-y0)**2)

        n = max(nsteps(d, PEN_SPEED),
                nsteps(abs(alpha1-alpha0), AB_SPEED),
                nsteps(abs(beta1-beta0), AB_SPEED))

        for i in range(1, n):
            u = i / n

            xi = x0 + u * (x1 - x0)
            yi = y0 + u * (y1 - y0)

            Si = (xi, yi)

            rval = lineus_ik(Si)

            if rval is None:
                raise SimError('unable to reach ' + str(S))

            P, Q, R, alpha, beta = rval

            errors = lineus_config_errors(P, Q, R, Si, alpha, beta)

            if errors:
                raise SimError('config errors: ' + 'l '.join(errors))

            states.append(SimState(P, Q, R, Si, alpha, beta, elev))

    else:

        n = max(nsteps(abs(alpha1-alpha0), AB_SPEED),
                nsteps(abs(beta1-beta0), AB_SPEED))

        for i in range(1, n):
            u = i / n

            ai = alpha0 + u * (alpha1-alpha0)
            bi = beta0 + u * (beta1-beta0)

            P, Q, R, S = lineus_fk(ai, bi)

            errors = lineus_config_errors(P, Q, R, S, ai, bi)

            if errors:
                raise SimError('config errors: ' + 'l '.join(errors))

            states.append(SimState(P, Q, R, S, ai, bi, elev))

    states.append(SimState(P1, Q1, R1, Snew, alpha1, beta1, elev))

def sim_pen(states, elev1):
    
    
    P, Q, R, S, alpha, beta, elev0 = states[-1]

    if elev1 == elev0:
        return

    n = nsteps(abs(elev1 - elev0), LIFT_SPEED)

    for i in range(1, n):

        u = i / n

        elev = elev0 + u * (elev1 - elev0)

        states.append(SimState(P, Q, R, S, alpha, beta, elev))

    states.append(SimState(P, Q, R, S, alpha, beta, elev1))

def sim_pen_up(states):
    sim_pen(states, 1)

def sim_pen_down(states):
    sim_pen(states, 0)


def main():

    if len(sys.argv) < 2:

        for alpha in linspace(ALPHA_LIMITS[0], ALPHA_LIMITS[1], 40):
            for beta in linspace(BETA_LIMITS[0], BETA_LIMITS[1], 40):
                P, Q, R, S = lineus_fk(alpha, beta)
                if not lineus_config_errors(P, Q, R, S, alpha, beta):
                    rval = lineus_ik(S)
                    if not rval:
                        plt.plot(S[0], S[1], 'm^')
                    P2, Q2, R2, alpha2, beta2 = rval
                    if abs(alpha - alpha2) > 1e-5 or abs(beta - beta2) > 1e-5:
                        plt.plot(S[0], S[1], 'rx')
                    plt.plot(S[0], S[1], 'b.')

        plt.axis('equal')
        plt.show()

        return

    else:

        contours = load_contours(sys.argv[1])

        # state is time, P, Q, R, S, alpha, beta, elev
        alpha = 45*np.pi/180
        beta = 135*np.pi/180
        P, Q, R, S = lineus_fk(alpha, beta)
        elev = 1.0

        assert not lineus_config_errors(P, Q, R, S, alpha, beta)

        init_state = SimState(P, Q, R, S, alpha, beta, elev)
        states = [init_state]

        try:

            for contour in contours:
                # move to contours[0]
                sim_move_to(states, contour[0])

                sim_pen_down(states)

                for point in contour[1:]:
                    sim_move_to(states, point)

                sim_pen_up(states)

            print('success! have', len(states), 'states')

        except SimError as e:
            print('error:', e)
            pass

        fig, ax = plt.subplots()

        aOP, = ax.plot([0, P[0]], [0, P[1]], 'b.-', zorder=2)
        aOQ, = ax.plot([0, Q[0]], [0, Q[1]], 'b.-', zorder=2)
        aQR, = ax.plot([Q[0], R[0]], [Q[1], R[1]], 'b.-', zorder=2)
        aRS, = ax.plot([R[0], P[0], S[0]], [R[1], P[1], S[1]], 'b.-', zorder=2)

        artists = (aOP, aOQ, aQR, aRS)


        def init():
            ax.set_xlim(-50, 100)
            ax.set_ylim(-50, 80)
            ax.set_aspect('equal')
            for contour in contours:
                ax.plot(contour[:,0], contour[:,1], color=[0.8, 0.8, 0.8], zorder=0)
            return artists

        def update(frame):
            P, Q, R, S, _, _, elev = states[frame]

            aOP.set_data([0, P[0]], [0, P[1]])
            aOQ.set_data([0, Q[0]], [0, Q[1]])
            aQR.set_data([Q[0], R[0]], [Q[1], R[1]])
            aRS.set_data([R[0], P[0], S[0]], [R[1], P[1], S[1]])

            for artist in artists:
                if elev == 0:
                    artist.set_color([1.0, 0.0, 0.0])
                else:
                    artist.set_color([0.0, 0.0, 1.0])


            return artists

        ani = FuncAnimation(fig, update, frames=len(states),
                            init_func=init, blit=True, interval=INTERVAL)

        plt.show()


######################################################################

main()
