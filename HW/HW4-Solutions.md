# HW 4 Solutions

* Table of Contents
{:toc}

## (1) IEEE Standard for Floating Point numbers

**Written Answers**

<embed src="floats.pdf" width="500" height="375" 
 type="application/pdf">

- Parts 1 and 2:

Solved in the attached PDF

- Part 3:

| Size   | Sign | Significand | Exponent | Bias | Colloquial Name  | Machine Epsilon | Largest number | Smallest number | Number of numbers |
| ------ | ---- | ----------- | -------- | ---- | ---------------- | --------------- | -------------- | --------------- | ----------------- |
| 16-bit | 1    | 10          | 5        | 15   | Half precision   | 9.7 x 10^{-4}   | 65,504         | 5.97 x 10^{-8}  | 63,488            |
| 32-bit | 1    | 23          | 8        | 127  | Single precision | 1.2 x 10^{-7}   | 3.4 x 10^{38}  | 1.4 x 10^{-45}  | 4.27 x 10^{9}     |
| 64-bit | 1    | 52          | 11       | 1023 | Double precision | 2.2 x 10^{-16}  | 1.8 x 10^{308} | 5 x 10^{-324}   | 1.84 x 10^{19}    |

- Part 4

Note that the highest possible value of the exponent always evaluates to `NaN`. So we will not include that here.

16-bit: Exponent ranges from -14 to 15 for a total of 30 exponents  
32-bit: Exponent ranges from -126 to 127 for a total of 254 exponents  
64-bit: Exponent ranges from -1022 to 1023 for a total of 2046 exponents.

- Part 5

These numbers differ in the part that comes before the "binary decimal point", known as the radix point for binary numbers, in the significand. 

While the two numbers `0000010000000100` and `0000000000000100` have the same significand bits, the first number is in the form `1.0000000100 x 10^{exponent}`, the second number is in the form `0.0000000100 x 10^{exponent}`. The two numbers have the same exponent, i.e., even though the exponent bits are different, we learn by using the [Float Toy](https://evanw.github.io/float-toy/) program that both of these numbers are interpreted as having the exponent `-14`.

- Part 6

Calculated in the attached PDF and included in the table above.

- Part 7

Calculated in the attached PDF.

## (2) Python program to interpret IEEE floats

~~~python
def binary_to_dec_int(num):
 # num is a string, interpreted as a binary integer.
 s = len(num)
 total_value = 0
 for index in range(s):
  power = s-index-1
  digit = int(num[index])
  value = (2 ** power) * digit
  total_value += value
 return total_value

def binary_to_dec_fraction(num):
  # num is a string of 0's and 1's. It is interpreted in the following way:
  # The first 'digit' is the multiple of (1/2). the second 'digit' is the multiple of (1/4). The third 'digit' is the multiple of (1/8), and so on.
  # for example, in the IEEE format, a 16-bit number could have the significand
  # 1.0011010101
  # This function reads the string of bits AFTER the "decimal point" and
  # returns the value of the resulting fraction as a 'float'.
  # The returned value must always be less than 1.
  s = len(num)
  total_value = 0
  for index in range(s):
    power = -index - 1
    digit = int(num[index])
    value = (2 ** power) * digit
    total_value += value
  return total_value

def readIEEEfloat(num):
  # Interpret num, type string, as a 16-bit, 32-bit or 64-bit binary number stored
  # in IEEE format. Return the answer as an object of type float.

  if len(num) == 16 or len(num) == 32 or len(num) == 64:
    # First, take out the sign bit
    signbit       = int(num[0])
    sign          = -1 if signbit == 1 else 1

    # Then, take out the exponent and significand bits
    if len(num) == 16:
      exponent      = binary_to_dec_int(num[1:6])
      significand   = binary_to_dec_fraction(num[6:])
      bias = 15
    elif len(num) == 32:
      exponent      = binary_to_dec_int(num[1:9])
      significand   = binary_to_dec_fraction(num[9:])
      bias = 127
    elif len(num) == 64:
      exponent      = binary_to_dec_int(num[1:12])
      significand   = binary_to_dec_fraction(num[12:])
      bias = 1023
    
    # Then put it together.
    return sign * (1+significand) * 2 ** (exponent - bias)
  else:
    print("Input must be a string of length 16, 32 or 64")
    return None
~~~

## (3) Conway's Game of Life

~~~python
from ConwayUtilities import *
def nbrs_v2(n,size):

  north         = n - size
  south         = n + size
  northeast     = n - size + 1
  northwest     = n - size - 1
  southeast     = n + size + 1
  southwest     = n + size - 1
  east          = n + 1
  west          = n - 1
  nbrs_list = [north,south,northeast,southeast,northwest,southwest,east,west]
  return nbrs_list

def checkBounds_v2(n,size):
  if n <= (size-1):
    # Top row
    return False
  elif n >= (size**2 - size):
    # Bottom Row
    return False
  elif n % size == 0:
    # Left edge
    return False
  elif n % size == (size-1):
    return False
  else:
    return True

def all_nbrs(size):
  nbrs = [0] * (size**2)
  for j in range(size**2):
    if not checkBounds_v2(j,size):
      nbrs[j] = []
    else:
      nbrs[j] = nbrs_v2(j,size)
  return nbrs

def new_value_n_v2(n,current_state):
 size = int(sqrt(len(current_state)))
 nbrs = all_nbrs(size=size)
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
   print(f"Cell number {n} was dead and comes alive")
   return True # comes alive only if 3 neighbors
  else:
   return False # stays dead for any other num. nbrs.
 else:
  # If currently alive:
  if num_alive_nbrs == 2 or num_alive_nbrs == 3:
   print(f"Cell number {n} was alive and stays alive")
   return True # remains alive if 2/3 neighbors
  else:
   print(f"Cell number {n} was alive and is now dead")
   return False# dies for any other num. nbrs.

def new_state_v2(old_state):
 size = sqrt(len(old_state))
 newlist = [0] * int(size**2)
 for k in range(int(size**2)):
  if checkBounds_v2(k,size):
   # i.e., if k is one of the interior cells.
   newlist[k] = new_value_n_v2(k,old_state)
  else:
   # don't make any changes if k is on the boundary.
   newlist[k] = old_state[k]
 return newlist


~~~

