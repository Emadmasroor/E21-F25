# HW 3 Solutions

* Table of Contents
{:toc}

## (1) Accelerometer Activity

The following code solves this problem. If accompanied by the correct `boot.py` file on the Circuit Playground, and if the 'mode' is switched to writable, this will collect acceleration data correctly.

```python
from adafruit_circuitplayground import cp
import time

def magnitude(a,b,c):
    return (a**2 + b**2 + c**2)**(1/2)

# Number of readings
N = 100

# Create a list that will store the readings
readings_z = [0] * N
readings = [0] * N

# Time delay between measurements
delay = 0.05

f = open("/accels.txt","a")
cp.pixels[1] = (0,50,0)
for j in range(N):
    x = cp.acceleration.x
    y = cp.acceleration.y
    z = cp.acceleration.z
    a = (x**2 + y**2 + z**2)**(1/2)
    f.write(f"{x:.4f},{y:.4f},{z:.4f},{a:.4f}\n")
    f.flush()
    
    # Beep and delay
    cp.play_tone(440,delay)
    time.sleep(delay) # delay of 1 second
f.close()
cp.pixels[1] = (0,0,0)
```

## (2) A function to control Neopixels

```python
import adafruit_circuitplayground as cp
import time

def lightUp(color,n,p):
    if color == 'red':
        cp.pixels[n] = (int(p),0,0)
    elif color == 'blue':
        cp.pixels[n] = (0,0,int(p))
    elif color == 'green':
        cp.pixels[n] = (0,int(p),0)

# The function is used below; you did not need to submit anything here.
while True:
    lightUp(‘red’,8,45)
    time.sleep(3)
    lightUp('green',5,200)
    time.sleep(3)
    cp.play_tone(440,3)
```

## (3) A function to parse decimal numbers and convert to binary

The following code solves this problem.
~~~python
def decimal_to_binary(num):
    binary_digits = []
    number = int(num)
    keep_going = True
    k = 0
    while keep_going:
        rem     = number % 2
        number  = number // 2
        binary_digits.append(rem)
        print("quotient ",number, " remainder ",rem)
        if number == 0:
            break
    print("hello")
    a = binary_digits.reverse()

    result = ''
    for j in range(len(binary_digits)):
        result += str(binary_digits[j])
    print(result)
    return a
~~~

## (4) Conway's Game of Life 6x6

All functions have been placed here.

~~~python
def nbrs(n):
 north 		= n - 6
 south 		= n + 6
 northeast 	= n - 6 + 1
 northwest 	= n - 6 - 1
 southeast 	= n + 6 + 1
 southwest 	= n + 6 - 1
 east 		= n + 1
 west 		= n -1
 nbrs_list = [north,south,northeast,southeast,northwest,southwest,east,west]
 return nbrs_list 

def checkBounds(n):
 if n <= 5 or n >= 30 or n % 6 == 0 or n % 6 == 5:
  return False
 else:
  return True

def determine_nbrs():
 nbrs_list = [0] * 36
 for j in range(36):
  if not checkBounds(j):
   nbrs_list[j] = []
  else:
   nbrs_list[j] = nbrs(j)
 return nbrs_list

def new_value_n(n,current_state):
 nbrs = determine_nbrs()
 # Get a list of neighbors' locations for cell number n
 nbrs_n = nbrs[n]
 # Determine a list of Booleans for neighbors' states.
 list_nbrs_booleans = [0] * 8
 for k in range(8):
  # add k'th neighbor of cell n to this list.
  list_nbrs_booleans[k] = current_state[nbrs_n[k]] 
 # Find total alive nbrs. Booleans can add as if they were integers.
 num_alive_nbrs = sum(list_nbrs_booleans)
 # Apply Conway's rules
 if not current_state[n]:
  # If currently dead:
  if num_alive_nbrs == 3:
   return True # comes alive only if 3 neighbors
  else:
   return False # stays dead for any other num. nbrs.
 else:
  # If currently alive:
  if num_alive_nbrs == 2 or num_alive_nbrs == 3:
   return True # remains alive if 2/3 neighbors
  else:
   return False# dies for any other num. nbrs.

def new_state(old_state):
 newlist = [0] * 36
 for k in range(36):
  if checkBounds(k):
   # i.e., if k is one of the interior cells.
   newlist[k] = new_value_n(k,old_state)
  else:
   # don't make any changes if k is on the boundary.
   newlist[k] = old_state[k]
 return newlist

~~~

The following functions help visualize the game inside a terminal.


~~~python
from math import sqrt
import random

def random_boolean_list(length):
  # Generates a random list of Booleans of a certain length
  return [random.choice([True, False]) for _ in range(length)]

def visualizeConway(list):
  # list is a list of booleans. It should be square.
  size = int(sqrt(len(list)))

  full_string = ''
  
  # header1       = ''
  header2       = ''
  # header1_unit  = '|   '
  header2_unit  = '|---'

  for j in range(size):
    # header1 += header1_unit
    header2 += header2_unit
  # header1 += '|\n'
  header2 += '|\n'

  # full_string += header1
  full_string += header2

  # k counts where in the list we are.
  k = 0
  for row in range(size):
    this_row = ''
    for column in range(size):
      if list[k]:
        unit = '| ■ '
      else:
        unit = '| □ '
      k += 1
      this_row += unit
    this_row += '|\n'
    full_string += this_row
  
  print(full_string)
~~~

