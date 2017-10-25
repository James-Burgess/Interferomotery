from array_viability_test import viable

#create stepper function
def inc(value, step): return value + step
def step_range(start, end, step, func):
    while start <= end:
        yield start
        start = func(start, step)

#create array of cordinates
co_ords = [(x,y) for x in step_range(12, 20000, 12, inc) for y in step_range(12, 20000, 12, inc)]
print(len(co_ords))

#Example Co-ords
# x = np.linspace(-6000, 6000, 60)
# y = np.random.randn(60)*100

# for i in len(co_ords):
#     new_c = co_ords[i]

for single in co_ords:
    if not(viable(*single)):
        co_ords.pop(single)
