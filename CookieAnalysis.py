#! /usr/bin/env python 

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from MySort import MySort

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)
    
    Sorter = MySort()

    times = Sorter.DefaultSort(times)
    times_avg = Sorter.DefaultSort(times_avg)
   

    quantile2s =  np.quantile(times_avg,0.023)
    quantile1s =  np.quantile(times_avg,0.159)
    quantile0s =  np.quantile(times_avg,0.5)
    quantile1sp =  np.quantile(times_avg,0.841)
    quantile2sp =  np.quantile(times_avg,0.977)

    weightss = np.ones_like(times) / len(times)

    plt.hist(times, 70, weights=weightss, color='green', alpha = 0.5)
    
    plt.xlabel("time between dissapearance of cookies in day (times)")
    plt.ylabel("probability")
    plt.title("Rate = 2.1")
    plt.savefig("timevspr.png")
    plt.show()

    #plt.hist(times_avg, 100)
    #plt.show()

    weights = np.ones_like(times_avg) / len(times_avg)
    #plt.hist(times_avg, weights=weights)

    plt.hist(times_avg,weights=weights, color='green', bins = 20,alpha = 0.5)
    plt.xlabel('average time between dissapearance of cookies in days (times_avg)')
    plt.ylabel('Probability')
    plt.title('Rate = 2.1')
    
    plt.axvline(quantile2s,label="-2 $\sigma$",color="black",linestyle = "--")
    plt.axvline(quantile1s,label="-1 $\sigma$",color="yellow",linestyle = "--")
    plt.axvline(quantile0s,label="median", color="blue",linestyle = "--")
    plt.axvline(quantile1sp,label="1 $\sigma$", color="yellow",linestyle = "--")
    plt.axvline(quantile2sp,label="2 $\sigma$",color ="black",linestyle = "--")
    plt.legend()
    plt.savefig("avgtimevspr")
    plt.show()
    
    
    # try some other methods! see how long they take
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.QuickSort(times_avg)

    # ADD YOUR CODE TO PLOT times AND times_avg HERE
