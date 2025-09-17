# HW 2 Solutions

* Table of Contents
{:toc}

## (1) Base Systems

All of the answers are included in the following PDF

<embed src="binary_hex" width="500" height="375" 
 type="application/pdf">

## (2) Using `for` loops to play music

```python
from adafruit_circuitplayground import cp

# Define a new class called 'music'
class music:
    # The class has two attributes: 'pattern' and 'duration'
    pattern = []    # contains frequency values (in Hz)
    durations = []  # contains note durations (in seconds)

# Define the attributes of sample_music. 
# [E E F G G F E D C C D D E D D]
sample_music = music()
sample_music.pattern = [330,330,349,392,392,349,330,294,262,262,294,294,330,294,294]
sample_music.durations = [1,1,1,1,1,1,1,1,1,1,1,1,1.5,0.5,2]

# Your code starts here

for i in range(len(sample_music.pattern)):
    cp.play_tone(sample_music.pattern[i],sample_music.durations[i])
```
## (3) Analog vs Digital

```python
from adafruit_circuitplayground import cp
import time

while True:
    time.sleep(0.2)
    if cp.switch:
        print(f"({cp.temperature})")
    else:
        if cp.temperature < 27:
            value = 0
        else:
            value = 1
        print(f"({value})")
```

## (4)  Reaction times

The code to solve this problem is as follows.

```python
from statistical_functions import std
from adafruit_circuitplayground import cp
import time
import random

# Choose the number of data points to collect
N = 10

# Create a list to collect data points
data = [0] * N

# Print some information
print("Welcome to the reaction time game.")
print(f"We will collect {N} samples.")
print("Press button A when an LED lights up.")

for j in range(N):
    # Turn off all LEDs
    cp.pixels.fill((0, 0, 0))

    # Wait for a random time between 1 and 5 seconds
    random_delay = random.uniform(1, 5)
    time.sleep(random_delay)
    # Turn on a random LED (pick an index from 0 to 9)
    
    if cp.switch:
        led_index = random.randint(0, 9)
    else:
        led_index = 4
    cp.pixels[led_index] = (0, 10, 0)  # Green LED lights up

    # Record the time the LED lights up
    start_time = time.monotonic()

    # Wait for button A press
    while not cp.button_a:
        # do nothing; keep waiting in this while loop
        pass

    # Button pressed! First, calculate the reaction time.
    reaction_time = time.monotonic() - start_time

    # Switch off the LED
    cp.pixels[led_index] = (0,0,0)

    # Print the reaction time to the serial console
    print(f"Reaction time: {reaction_time:.3f} seconds")

    # Assign data to a list
    data[j] = reaction_time

    # Pause before restarting the game
    time.sleep(2)
    
print(f"The mean reaction time is {sum(data)/len(data)}")
print(f"The standard deviation is {std(data)}")


```

