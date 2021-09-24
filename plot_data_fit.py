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
    plt.plot(the_array[starting_index:starting_index+points_to_plot:1])
    #print(the_array[starting_index:starting_index+points_to_plot])
    #print(len(the_array[starting_index:starting_index+points_to_plot]))


#print(data)
#print(len(data))
#print(data[intchan::32])
#print(len(data[intchan::32]))
    
if(intchan<0):
    for i in range(32):
        plot_array(data[i::32])
else:
    plot_array(data[intchan::32])
    
plt.show()
    
Fs = 200000
f = 10000
sample = 40
x = np.arange(sample)
y = np.sin(2 * np.pi * f * x / Fs)
plt.plot(x, y)

plt.show()


from scipy.optimize import curve_fit

def sinfunc(n,A,f,p,c): return A*np.sin(2*np.pi*f*n/Fs+p)+c
guess_amp=3000
guess_freq=10000
guess_phase=0
guess_offset=0
guess=[guess_amp,guess_freq,guess_phase,guess_offset]

all_data_for_this_channel=data[intchan::32]
data_points_we_want=all_data_for_this_channel[starting_index:starting_index+points_to_plot]

nvalues=range(starting_index,starting_index+points_to_plot)

popt,pcov=curve_fit(sinfunc,nvalues,data_points_we_want,p0=guess)
A,f,p,c=popt
print("The frequency is %f"%f)
print(popt)

fit_result=sinfunc(nvalues,A,f,p,c)
plt.plot(data_points_we_want)
plt.plot(fit_result)
plt.show()
