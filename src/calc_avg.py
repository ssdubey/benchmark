import os
import subprocess
import time
import statistics
import numpy as np
import lib.utils as utils

from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import FormatStrFormatter



def calc_avg(inputpath, outputpath, graphdetail):
    exp_time_lst = {}                            # a map to add all the time values against the key 'size'
    exp_count = 0                           # assuming that all the experiments involved all the keys
    #inputpath = path + "exp/"
    for file in os.listdir(inputpath):
        if file.endswith(".txt"):
            #readfd = open(path + file, "r")
            readfd = open(inputpath + file, "r")
            lines = readfd.read()
            lines = lines.split("\n")
            del lines[-1]
            for line in lines:
                    kv = line.split(' ')
                    key = kv[0]
                    if key in exp_time_lst:
                        exp_time_lst[key].append(float(kv[1]))
                    else:
                        lst = []
                        lst.append(float(kv[1]))
                        exp_time_lst[key] = lst

            exp_count = int(exp_count) + 1
            readfd.close()            

    # exp_time_lst contains the sum of all the keys from all the files
    # calculate avg now
    avg_map = {}
    for key in exp_time_lst:
        if exp_count != 0:
            avg_map[key] = sum(exp_time_lst[key]) / exp_count
        else : # this should never happen
            print("exp_count is 0 for " + key)

    stdev_map = {}
    for key in exp_time_lst:
        stdev_map[key] = statistics.stdev(exp_time_lst[key])

    keys = avg_map.keys()
    values = avg_map.values()
    yerr = stdev_map.values()

    # plotting the output
    encoded_key = []
    for key in keys:
        k = utils.encode[key]
        encoded_key.append(k)

    fig, ax = plt.subplots()
    plt.figure(figsize=(20,10))
    #plt.patches.Patch(label='data')
    plt.xlabel('size of file')
    plt.ylabel('time in seconds')
    plt.title('Average over all the experiments performed')

    #txt="badger ds \n private"
    plt.bar(encoded_key, values, 0.35, yerr=yerr, label=graphdetail)

    # valfloat_formatted = [ '%.4f' % elem for elem in values ]
    # valfloat_formatted = [float(i) for i in valfloat_formatted]
    # #print(valfloat_formatted)
    # for i,j in zip(encoded_key,valfloat_formatted):
    #     ax.annotate(str(j),xy=(i,j))


    plt.legend()

    timestamp = time.ctime(time.time()).replace(" ", "_")
    #path_to_save = path + "avg/" + str(timestamp)
    path_to_save = outputpath + str(timestamp)
    plt.savefig(path_to_save)

    # updating file with key avg_value std_dev
    f = open(path_to_save + '.txt',"a+")
    for key in keys:
        f.write(str(key) + ' ' + str(avg_map[key]) + ' ' + str(stdev_map[key]) + '\n')
    f.close()
    #plt.show()

    # print(stdev_map)
    # print(avg_map)
    # print(exp_count)

recordname = "output10_20190613_093921"
inputpath = "/home/shashank/work/benchmark/output_repo/" + recordname + "/size/exp/"
outputpath = "/home/shashank/work/benchmark/output_repo/" + recordname + "/size/avg/"
graphdetail = "TC-1 Badger db \nPrivate"

calc_avg(inputpath, outputpath, graphdetail)







# recordname = "output1_20190609_174718"
# path = "/home/shashank/work/benchmark/output_repo/" + recordname + "/size/"
# #calc_avg(path)

# p=path + "exp/Sun_Jun_9_17:40:27_2019"
# #print(p)
# readfd = open(path + "exp/Sun_Jun_9_17:40:27_2019", "r")

# lines = readfd.read()

# for path, dirs, files in os.walk("/home/shashank/work/benchmark/output_repo",):
#     print(dirs[0])                       
# #calc_avg("/home/shashank/work/benchmark/output_repo/output1*/size/exp/")

# directories_in_curdir = filter(os.path.isdir, os.listdir(os.curdir))
# print(directories_in_curdir)

# inf = os.walk("/home/shashank/work/benchmark/output_repo/")
# [x[0] for x in inf]