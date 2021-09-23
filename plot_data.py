#!/usr/bin/python3


from optparse import OptionParser
import matplotlib.pyplot as plt
import numpy as np

parser = OptionParser()

parser.add_option("-c", "--channel", dest="channel",
                  default="-1", help="channel to plot", metavar="CHAN")

parser.add_option("-f", "--file", dest="file",
                  default="mybigdatafile", help="file to plot", metavar="FILE")

parser.add_option("-s", "--start", dest="starting_index",
                  default="0", help="starting index")

parser.add_option("-p", "--points", dest="points_to_plot",
                  default="1000", help="number of points to plot")

(options, args) = parser.parse_args()


intchan=int(options.channel)

data=np.fromfile(options.file,dtype=np.int16)

points_to_plot=int(options.points_to_plot)
starting_index=int(options.starting_index)

def plot_array(the_array):
    plt.plot(the_array[starting_index:starting_index+points_to_plot])


if(intchan<0):
    for i in range(32):
        plot_array(data[i::32])
else:
    plot_array(data[intchan::32])
    
plt.show()
