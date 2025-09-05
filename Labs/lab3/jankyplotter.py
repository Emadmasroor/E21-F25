from pwmio import PWMOut
from adafruit_motor.servo import Servo
from math import pi, sqrt, cos, sin, atan2
from time import sleep

L1 = 30
L2 = 50

S0_MIN = 10

DEG = pi/180

ALPHA_LIMITS = (-45*DEG, 135*DEG)
BETA_LIMITS = (45*DEG, 225*DEG)

AB_DIFF_MIN = 20*DEG
AB_DIFF_MAX = 160*DEG

######################################################################

def wrap_limits(angle, limits):
    center = 0.5*(limits[0] + limits[1])
    diff = angle - center
    return center + ((diff + pi) % (2*pi)) - pi

######################################################################

def make_servo(pin):
    return Servo(
        PWMOut(pin, frequency=200),
        actuation_range=180,
        min_pulse=500,
        max_pulse=2500)

######################################################################

def config_errors(P, Q, S, alpha, beta):

    errors = []

    if alpha < ALPHA_LIMITS[0]:
        errors.append('α < limit')

    if alpha > ALPHA_LIMITS[1]:
        errors.append('α > limit')

    if beta < BETA_LIMITS[0]:
        errors.append('β < limit')

    if beta > BETA_LIMITS[1]:
        errors.append('β > limit')

    if abs(beta - alpha) < AB_DIFF_MIN:
        errors.append('|α - β| < limit')

    if abs(beta - alpha) > AB_DIFF_MAX:
        errors.append('|α - β| > limit')

    if alpha > beta:
        errors.append('α > β')

    if S[0] * P[1] - S[1] * P[0] < 0:
        errors.append('arm flipped')

    if abs(S[0]) < S0_MIN:
        errors.append('S too close')

    return errors

######################################################################

def fk(alpha, beta):
    
    p = (L2*cos(alpha), L2*sin(alpha))
    t = (cos(beta), sin(beta))

    q = (L1*t[0], L1*t[1])
    s = (p[0] - L2*t[0], p[1] - L2*t[1])
    
    return p, q, s

######################################################################

def ik(s, return_fk=False, return_errors=False):

    d = sqrt(s[0]*s[0] + s[1]*s[1])

    if d == 0 or d >= 2*L2:

        ab = None

        if return_fk:
            fk = (None, None, s)

        if return_errors:
            errors = ['S is unreachable']

    else:

        t = (s[0]/d, s[1]/d)

        a = 0.5 * d

        m = (a*t[0], a*t[1])

        h = sqrt(L2*L2 - a*a)

        p = (m[0] - h*t[1], m[1] + h*t[0])

        q = ((p[0]-s[0])*L2/L1, (p[1]-s[1])*L2/L1)

        alpha = wrap_limits(atan2(p[1], p[0]), ALPHA_LIMITS)
        beta = wrap_limits(atan2(q[1], q[0]), BETA_LIMITS)

        ab = (alpha, beta)
        
        if return_fk:
            fk = (p, q, s)

        if return_errors:
            errors = config_errors(p, q, s, alpha, beta)

    if return_fk:
        if return_errors:
            return (ab, fk, errors)
        else:
            return (ab, fk)
    elif return_errors:
        return (ab, errors)
    else:
        return ab

######################################################################

class JankyPlotter:

    def __init__(self, alpha_pin, beta_pin, cam_pin, 
                 alpha_home=pi/2, beta_home=pi):

        self.alpha_motor = make_servo(alpha_pin)
        self.beta_motor = make_servo(beta_pin)
        self.cam_motor = make_servo(cam_pin)

        self.alpha_home = alpha_home
        self.beta_home = beta_home
        
        self.pen_up()
        self.go_home()

    def get_angles(self):
        return self.alpha, self.beta

    def get_pen_pos(self):
        return self.pen_pos

    def go_home(self):
        self.set_angles(self.alpha_home, self.beta_home)
        sleep(1.0)
    
    def set_angles(self, alpha, beta):

        p, q, s = fk(alpha, beta)
        errors = config_errors(p, q, s, alpha, beta)
        if errors:
            raise ValueError('configuration errors: ' + '; '.join(errors))
        else:
            self.pen_pos = s
            self.alpha = alpha 
            self.beta = beta
            # even tho alpha/beta guaranteed to be in limits here,
            # need to clip to [0, 180] interval due to round-off error
            self.alpha_motor.angle = max(0, min(180, -alpha/DEG + 135))
            self.beta_motor.angle = max(0, min(180, beta/DEG - 45))
        
    def pen_up(self):
        self.pen_is_down = False
        self.cam_motor.angle = 0
        sleep(0.4)
        
    def pen_down(self):
        self.pen_is_down = True
        self.cam_motor.angle = 180
        sleep(0.4)

    def is_pen_down(self):
        return self.pen_is_down

