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
