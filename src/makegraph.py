import os
import subprocess
import time
import statistics
import numpy as np
import lib.utils as utils
import operator

#from matplotlib import pyplot as plt
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import FormatStrFormatter


def linegraph():
    # reading values from file
    #size = "100mb"
    
    dir = "output9_20190620_201707"
    cond = 2 # 1 = separate graph, else aggregate graph
    graph_path = "/home/shashank/work/benchmark/output_repo/throughput/" + dir + "/"
    aggregate_graph_path = "/home/shashank/work/benchmark/output_repo/throughput/aggregate/" + dir + "/"
    graph_text = "TC-9  Public FS" # (two nodes)"
    output_files = []

    if cond == 1:
        for path, dirs, files in os.walk(graph_path, "r"):
            output_files = files
    else:
        for path, dirs, files in os.walk(aggregate_graph_path, "r"):
            output_files = files
            
    plt.figure(figsize=(22,13))

    for size in output_files:
        
        graphdetail = size
        plot = {}
        stdev = {}

        readfd = open(graph_path + size, "r")
        lines = readfd.read()
        lines = lines.split("\n")
        del lines[-1]
        for line in lines:
                #print(line)
                kv = line.split(' ')        # the output contains 'offered throughput, observed throughput, standard deviation'
                key = kv[0]
                value = kv[1]
                sd = kv[2]
                plot[key] = value
                stdev[key] = sd

        readfd.close()

        keyset = plot.keys()
        valset = plot.values()

        stdevkeyset = stdev.keys()
        stdevvalset = stdev.values()

        # putting the values in data structure
        
        keyint = []
        valfloat = []
        
        stdevkeylst = []
        stdevvallst = []

        for key in keyset:
            keyint.append(float(key))

        for val in valset:
            valfloat.append(float(val))

        for std in stdevkeyset:
            stdevkeylst.append(float(std))

        for std in stdevvalset:
            stdevvallst.append(float(std))

        a = [list(pair) for pair in zip(keyint, valfloat)]
        sorteda = sorted(a,key=operator.itemgetter(0))
        print(sorteda)

        b = [list(pair) for pair in zip(stdevkeylst, stdevvallst)]
        sortedb = sorted(b,key=operator.itemgetter(0))
        print(sortedb)

        x = []
        y = []
        for ele in sorteda:
            x.append(ele[0])
            y.append(ele[1])

        err = []
        for ele in sortedb:
            err.append(ele[1])

        # ax = plt.subplot(111)

        # box = ax.get_position()
        # ax.set_position([box.x0, box.y0 + box.height * 0.1,
        #          box.width, box.height * 0.99])

        # ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
        #   fancybox=True, shadow=True, ncol=5)

        
        plt.rcParams.update({'font.size': 17})
        plt.xlabel("Offered Throughput")
        plt.ylabel("Observed Throughput")
        plt.title("Relation between Offered and Observed throughput (" + graph_text + ")")
        #plt.plot(x, y, 5,'*g-')
        #error = [y-1.0, y+1.0]
        
        
        plt.errorbar(x, y, yerr=err, fmt='-o', label=graphdetail)
        # plt.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
        #         mode="expand", borderaxespad=0, ncol=3)
        plt.subplots_adjust(right = 0.89)
        plt.legend(bbox_to_anchor=(1.11,1), borderaxespad=0)
        # plt.legend(bbox_to_anchor=(1.04,0), loc="lower left", borderaxespad=0)
        # plt.legend(bbox_to_anchor=(1.04,0.5), loc="center left", borderaxespad=0)
        # plt.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
        #                 mode="expand", borderaxespad=0, ncol=3)
        # plt.legend(bbox_to_anchor=(1,0), loc="lower right", 
        #                 bbox_transform=fig.transFigure, ncol=3)
        # plt.legend(bbox_to_anchor=(0.4,0.8), loc="upper right")

        if cond == 1:
            plt.savefig(graph_path + size)
            plt.close()
            plt.figure(figsize=(22,13))
        else:
            plt.savefig(aggregate_graph_path + size)
        #plt.show() 
        
        #plt.pause(0.0001)

def bargraph():
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

#filenames = ["output1_20190620_051758", "output2_20190620_082028", "output3_20190620_085522", "output4_20190620_092747", 
#"output5_20190620_103040", "output6_20190620_115925"]        

#for file in filenames:
linegraph()