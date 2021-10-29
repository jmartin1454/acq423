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

points_to_plot=int(options.points_to_plot)
starting_index=int(options.starting_index)

# figure out the offset in bytes
numchan=32 # total number of channels in the module
bytes_per_int16=2
offset=starting_index*numchan*bytes_per_int16 # offset in bytes

# figure out how many int16's to read in
count=points_to_plot*numchan

data=np.fromfile(options.file,offset=offset,count=count,dtype=np.int16)

def plot_array(the_array):
    plt.plot(the_array)

if(intchan<0):
    for i in range(32):
        plot_array(data[i::32])
else:
    plot_array(data[intchan::32])
    
plt.show()
