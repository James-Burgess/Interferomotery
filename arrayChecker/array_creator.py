#Example Co-ords

import numpy as np
print( np.linspace(-6000, 6000, 60)[1])

# y = np.random.randn(60)*100

#create stepper function
def inc(value, step): return value + step
def step_range(start, end, step, func):
    while start <= end:
        yield start
        start = func(start, step)

#create array of cordinates
co_ords = [(x,y) for x in step_range(12, 20000, 12, inc) for y in step_range(12, 20000, 12, inc)]

#smaller array to save processing time
# co_ords = [[x,y] for x in step_range(12, 200, 12, inc) for y in step_range(12, 200, 12, inc)]


print(len(co_ords))
#>256

# for one node we would have 256 possible placements
# therefore two nodes = 256**2 
# but we still can optomise by factoring in the fact that they cant be diagonailly further than 20km. 
#(unless one was in the center?)

#so lets start with two nodes and map all the positions

#let n1 be fixed at point 0,0 for now

# possiblities = []

# for x,i in co_ords:
# 	possibitiles.append([])