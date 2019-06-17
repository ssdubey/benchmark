import os
import subprocess
import time
import statistics
import numpy as np
import lib.utils as utils

from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import FormatStrFormatter


def func():
    #below code can be used to take values from the file and plot
    plot = {}
    readfd = open("output1", "r")
    lines = readfd.read()
    lines = lines.split("\n")
    del lines[-1]
    for line in lines:
            #print(line)
            kv = line.split(' ')
            key = kv[0]
            value = kv[1]
            plot[key] = value

    readfd.close()

    keyset = plot.keys()
    valset = plot.values()

    keyint = []
    valfloat = []

    for key in keyset:
        keyint.append(int(key))

    for val in valset:
        valfloat.append(float(val))

    #plotting
    fig, ax = plt.subplots()
    #ax.yaxis.set_major_formatter(FormatStrFormatter('%.5f'))
    plt.xlabel('size of file')
    plt.ylabel('time in seconds')
    plt.title('Time taken to add the file in ipfs ')

    txt="badger ds \n private"
    plt.bar(keyset, valfloat, width = 0.2, align='center', color='red', alpha=0.6, label=txt)

    valfloat_formatted = [ '%.4f' % elem for elem in valfloat ]
    valfloat_formatted = [float(i) for i in valfloat_formatted]
    #print(valfloat_formatted)
    for i,j in zip(keyset,valfloat_formatted):
        ax.annotate(str(j),xy=(i,j))

    plt.legend()

    plt.show()
        
func()