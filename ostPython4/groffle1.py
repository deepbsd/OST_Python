#!/usr/bin/env python3
#
#
#          groffle.py
#
#    Lesson 5: Optimizing Your Code
#
#     by David S. Jackson
#          7/21/2015
#   
#  OST Python4: Advanced Python
#     for Pat Barton, Instructor
#

"""
Program for optimization.  Python 4, Lesson 5.

Calculates the groffle speed of a knurl widget
of average density given by user input.

groffle_slow() is the starting point.  It takes
about 4 seconds to run on my home machine.  groffle_faster()
takes about 1.4 seconds to run on the same machine
after my optimizations.
"""

from math import log
from timeit import Timer

#import cProfile as profile
#import pstatspeed s

def groffle_slow(mass, density):
    "Starting point for optimizing the code for speed"
    total = 0.0
    for i in range(10000):
        masslog = log(mass * density)
        total += masslog/(i+1)
    return total

def groffle_faster(mass, density):
    "Hopefully fastest way to optimize this function for speed"
    # Option #1
    #constant = sum(1/(i+1) for i in range(10000))
    #masslog = log(mass * density)
    #return masslog * constant

    # Option #2
    #masslog = log(mass*density)
    #return  sum(masslog/(i+1) for i in range(10000))
    
    # Option #3
    #return sum(map((log(mass * density)).__truediv__, range(1,10001)))

    # Option #4
    #masslog = log(mass * density)
    #return sum(map(masslog.__truediv__, range(1,10001)))

    # Option #5
    constant = sum(map((1).__truediv__, range(1,10001)))
    masslog = log(mass * density)
    return masslog * constant




if __name__ == '__main__':

    mass = 2.5
    density = 12.0

    slowtimer = Timer("total = groffle_slow(mass, density)", "from __main__ import groffle_slow, mass, density")

    fastertimer = Timer("total = groffle_faster(mass, density)", "from __main__ import groffle_faster, mass, density")


    print("starting slow Timer...")
    slowertime = slowtimer.timeit(number=1000)
    print("starting faster Timer...")
    fastertime = fastertimer.timeit(number=1000)

    print("\ngetting knurl widget speed from slower function...")
    speed1 = groffle_slow(mass, density)
    print("getting knurl widget speed from faster function...")
    speed2 = groffle_faster(mass, density)

    print("\nslow function: knurl velocity is {} units/sec".format(speed1))
    print("fast function: knurl velocity is {} units/sec".format(speed2))


    print("\nComputation time for slower function: {}".format(slowertime))
    print("Computation time for faster function: {}".format(fastertime))
    #pctdecrease = ((slowertime-fastertime)/slowertime)*100
    timepct = (fastertime/slowertime)*100
    print("faster module is {:.4f}% speed of slower module.".format(timepct))

    #print("\nNew function decreases time by {0:.4f}%.\n".format(pctdecrease))
    
    # I don't think the profile data is all that useful.  
    '''
    profile.run("groffle_slow(mass, density)", "slow_profiledata")
    s = pstats.Stats("slow_profiledata")
    s.sort_stats("cumulative").print_stats(r"\.py")
    profile.run("groffle_faster(mass, density)", "faster_profiledata")
    s = pstats.Stats("faster_profiledata")
    s.sort_stats("cumulative").print_stats(r"\.py")
    '''



