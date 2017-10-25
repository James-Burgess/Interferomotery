import numpy as np

def cost(x,y):
    cost = 0
    for i in range(len(x)):
        cost += 1000*np.sqrt(x[i]**2 + y[i]**2)
    cost += len(x)*100000
    return cost

def tmax(n):
    time = np.linspace(1,24,24)
    goal = 2000000/n
    costForHour = [1000*np.exp((-1*t)/6) + 1000 for t in time]
    val = [np.array(costForHour[0:i+1]).sum() for i in range(len(costForHour))]


    iter = 0
    for q in val:
        if q > goal:
            remainder = goal - val[iter-1]
            break
        elif iter == len(val):
            print ('no limit')
        iter += 1
    try:
        tExtra = remainder/costForHour[iter-1]
    except:
        tExtra = 0
    tmax = (iter + tExtra)*3600
    return tmax

def tsys(n):
    return 0.3*(n + (50 - n%50)) + 1

def sens(n, bt):
    k = 1.38064852e3
    Tsys = tsys(n)
    eff = (bt + 1)/3
    t = (1825 - n*bt)*tmax(n)
    top = np.sqrt(2.)*k*Tsys
    bottom = eff*np.sqrt(n*(n-1)*10e6*t)
    sens = top/bottom
    return sens

# print ('Cost =', np.round(cost(x,y)/1e6,2), 'MCR')
# print ('N =', n, 'dishes')
# print ('Tsys =', tsys(n), 'K')
# print ('Running time/day =', np.round(tmax(n),2), 's', '/', tmax(n)/3600, 'h', '\n')
# print ('Sensitivity =', np.round(sens(n, 2)*1e6,2), u'\u00B5' + 'Jy')

def viable(x,y):
    n = len(x)
    Cost =np.round(cost(x,y)/1e6,2)
    Tsys = tsys(n)
    Running_time=np.round(tmax(n),2)
    Sensitivity =np.round(sens(n, 2)*1e6,2)

    if (Sensitivity >= 10 and Running_time <= 200):
        return
    else: return(False)

x = np.linspace(-6000, 6000, 60)
y = np.random.randn(60)*100

def inc(value, step): return value + step
def step_range(start, end, step, func):
    while start <= end:
        yield start
        start = func(start, step)

co_ords = [(x,y) for x in step_range(12, 20000, 12, inc) for y in step_range(12, 20000, 12, inc)]
print(len(co_ords))

# for i in len(co_ords):
#     new_c = co_ords[i]

# for single in co_ords:
#     if not(viable(*single)):
#         co_ords.pop(single)
