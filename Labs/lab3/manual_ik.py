import board
from robot import Robot, ik, fk

robot = Robot(board.A1, board.A2, board.A3)

try:

    while True:

        while True:
            try:
                pt = input('pos? ')
                if pt == 'down':
                    robot.pen_down()
                    continue
                elif pt == 'up':
                    robot.pen_up()
                    continue
                else:
                    x, y = pt.split()
                    x = float(x)
                    y = float(y)
                    break
            except ValueError as e:
                print(e)
                continue

        print(f'trying to move to {x} {y}...')
        result = ik((x, y), return_all=True)

        if result is None:
            print('unreachable!')
        else:
            _, _, _, alpha, beta, errors = result
            print(f'want to drive motors to {alpha} {beta}')
            if errors:
                print('errors after ik:', '; '.join(errors))
            else:
                robot.move_arm(alpha, beta)

except:

    robot.disable()
    raise



