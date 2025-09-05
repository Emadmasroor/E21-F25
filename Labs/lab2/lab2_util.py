######################################################################

def rgb_from_hsv(H, S, V):

    '''Converts from HSV colorspace to RGB colorspace.
       
         H: the input hue in [0, 360] interval
         S: the input saturation in [0, 1] interval
         V: the input value in [0, 1] interval
      
       Outputs integer RGB triple with elements in [0, 255] interval.

       Code adapted from https://www.ca5.co/convert/color/hsv-to-rgb
    '''

    # Wrap hue to [0, 360] interval if outside it
    H = H % 360.0

    C = V * S
    X = C * (1.0 - abs((H / 60.0) % 2.0 - 1.0))
    m = V - C

    if H < 60.0:
        (Rp, Gp, Bp) = (C, X, 0)
    elif H < 120.0:
        (Rp, Gp, Bp) = (X, C, 0)
    elif H < 180.0:
        (Rp, Gp, Bp) = (0, C, X)
    elif H < 240.0:
        (Rp, Gp, Bp) = (0, X, C)
    elif H < 300.0:
        (Rp, Gp, Bp) = (X, 0, C)
    else:
        (Rp, Gp, Bp) = (C, 0, X)

    R = int(round((Rp + m)*255))
    G = int(round((Gp + m)*255))
    B = int(round((Bp + m)*255))

    return (R, G, B)

######################################################################

def run_tests(tests, tol=1e-5, on_pass=None, on_fail=None):

    '''Run a series of numerical tests and return True for success or
    False for failure.

       tests
         a list of (fname, func, test_cases) triples, where
         - fname is the name of the function being tested
         - func is a callable function
         - test_cases is a list of (args, desired_rval) pairs, where
           - args is a tuple of arguments that gets sent to func
           - desired_rval is the desired return value

       tol
         the desired accuracy of the return value

       on_pass
         if not None, a callable to invoke after each passed test

       on_fail
         if not None, a callable to invoke after each failed test

    For each test case, if the actual return value is within tol of
    the actual return value, the test passes; otherwise the test
    fails.
    
    This function returns False as soon as the first test fails.
    '''

    ok = True
    
    for fname, func, test_cases in tests:
        if not ok:
            break
        print('***** testing function', fname, '*****\n')
        for args, desired_rval in test_cases:
            print(f'  calling {fname}{args}...')
            actual_rval = func(*args)
            print(f'    expected output {desired_rval}')
            print(f'    actual output  {actual_rval}')
            if abs(desired_rval - actual_rval) < tol:
                print('    result: pass 😀')
                if on_pass is not None:
                    on_pass()
            else:
                print('    result: FAIL 😢\n')
                if on_fail is not None:
                    on_fail()
                ok = False
                break
            print()
        if ok:
            print(f'all tests for {fname} pass!')
            print()

    return ok
