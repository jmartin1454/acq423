#!/usr/bin/python3


from optparse import OptionParser
import matplotlib.pyplot as plt
import numpy as np


parser = OptionParser()

parser.add_option("-c", "--channel", dest="channel",
                  default="-1", help="channel to plot", metavar="CHAN")

(options, args) = parser.parse_args()


intchan=int(options.channel)

print(intchan)

data = np.fromfile("mybigdatafile",dtype=np.int16)

if(intchan<0):
    for i in range(32):
        plt.plot(data[i::32])
else:
    plt.plot(data[intchan::32])
        
plt.show()
