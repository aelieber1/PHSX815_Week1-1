#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import os 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#################
# Random class
#################
# class that can generate random numbers
class Random:
    """A random number generator class"""

    # initialization method for Random class
    def __init__(self, seed = 5555):
        self.seed = seed
        self.m_v = np.uint64(4101842887655102017)
        self.m_w = np.uint64(1)
        self.m_u = np.uint64(1)
        
        self.m_u = np.uint64(self.seed) ^ self.m_v
        self.int64()
        self.m_v = self.m_u
        self.int64()
        self.m_w = self.m_v
        self.int64()

    # function returns a random 64 bit integer
    def int64(self):
        self.m_u = np.uint64(self.m_u * 2862933555777941757) + np.uint64(7046029254386353087)
        self.m_v ^= self.m_v >> np.uint64(17)
        self.m_v ^= self.m_v << np.uint64(31)
        self.m_v ^= self.m_v >> np.uint64(8)
        self.m_w = np.uint64(np.uint64(4294957665)*(self.m_w & np.uint64(0xffffffff))) + np.uint64((self.m_w >> np.uint64(32)))
        x = np.uint64(self.m_u ^ (self.m_u << np.uint64(21)))
        x ^= x >> np.uint64(35)
        x ^= x << np.uint64(4)
        with np.errstate(over='ignore'):
            return (x + self.m_v)^self.m_w

    # function returns a random floating point number between (0, 1) (uniform)
    def rand(self):
        return 5.42101086242752217E-20 * self.int64()

# main function for this Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)

    # default seed
    seed = 5555

    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]

    # set random seed for numpy
    np.random.seed(seed)

    # class instance of our Random class using seed
    random = Random(seed)

    # create some random data
    N = 10000

    # an array of random numbers from numpy
    x = np.random.rand(N)

    # an array of random numbers using our Random class
    myx = []
    for i in range(0,N):
        myx.append(random.rand())

    # Write the array of random numbers into a new file in the same directory
    file1 = open("rand_nums.txt", "w")
    for i in myx:
    	file1.write("%s\n" % i)
        
    # Read in the file using Pandas
    # This opens and reads the text file
    data = pd.read_csv('rand_nums.txt', header=None)  #Using header as none ensures that the first value isn't excluded and seen as a title
    
    # Plotting a histogram of our data
    #n, bins, patches = plt.hist(data, 50, density=True, facecolor='g', alpha=0.75, color = "purple")
    
    # Alternative method to plot the histogram
    # Terms: color:fill color; ec:edgecolor
    data.hist(bins=50, grid=True, density=True, color='lightblue', ec='C0', orientation='vertical', alpha=0.75)

    # Formatting the plot
    plt.xlabel('x', color='C0', fontsize=15)
    plt.ylabel('Probability', color='C0', fontsize=15)
    plt.title('Uniform Random Number', color='C0', fontsize=20)
    plt.grid(True)
    
    # Show figure (program exits when plot is closed)
    plt.show()
    
    # Save figure
    # plt.savefig("random_nums_plot")
