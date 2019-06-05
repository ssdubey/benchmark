import os
import subprocess
import time
import statistics
import numpy as np
import lib.utils as utils

from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter


# this function will execute cmd line arguments for ipfs 
# 'path' is the filesystem location of the input data 
def perform_exp(path):
    keyset = []         # this list will contain the file name on which exp is performed
    valfloat = []       # this list will contain the time taken in execution

    for path, dirs, files in os.walk(path):
        files.sort(key=int)
    
    if(os.path.isfile("./output_repo/output")):       # file 'output' contains the data from the latest experiment.
        os.remove("./output_repo/output")             # it is used in append mode
     
    for file in files:

        # executing command and recording time
        cmd = ['ipfs', 'add', path + '/' + file]
        start = time.time()
        subprocess.run(cmd, stdout=subprocess.PIPE)
        elapsed = time.time() - start

        #putting values in list for plotting
        keyset.append(file)
        valfloat.append(elapsed)

        #putting values in file for ref and plotting
        f = open("./output_repo/output","a+")
        f.write(file + " " + str(elapsed) + "\n")
        f.close()

    # plotting the output
    encoded_key = []
    for key in keyset:
        k = utils.encode[key]
        encoded_key.append(k)

    fig, ax = plt.subplots()
    plt.figure(figsize=(20,10))
    plt.xlabel('size of file')
    plt.ylabel('time in seconds')
    plt.title('Time taken to add the file in ipfs ')
    plt.bar(encoded_key, valfloat, width = 0.2, align='center', color='red', alpha=0.6)
    
    # adding the annotation
    valfloat_formatted = [ '%.3f' % elem for elem in valfloat ]
    valfloat_formatted = [float(i) for i in valfloat_formatted]
    
    for i,j in zip(encoded_key,valfloat_formatted):
        ax.annotate(str(j),xy=(i,j))

    ax.yaxis.set_major_formatter(FormatStrFormatter('%.5f'))

    # saving the output in output directory with timestamp
    timestamp = time.ctime(time.time()).replace(" ", "_")
    path_to_save = "./output_repo/size/exp/" + str(timestamp)
    cmd = ['cp', './output_repo/output', path_to_save + '.txt']

    plt.savefig(path_to_save)
    subprocess.run(cmd, stdout=subprocess.PIPE)
    #plt.show()

def calc_avg(path):
    exp_time_lst = {}                            # a map to add all the time values against the key 'size'
    exp_count = 0                           # assuming that all the experiments involved all the keys
    for file in os.listdir(path):
        if file.endswith(".txt"):
            readfd = open(path + file, "r")
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
    plt.xlabel('size of file')
    plt.ylabel('time in seconds')
    plt.title('Average over all the experiments performed')
    plt.bar(encoded_key, values, 0.35, yerr=yerr)

    timestamp = time.ctime(time.time()).replace(" ", "_")
    path_to_save = "./output_repo/size/avg/" + str(timestamp)
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
                
        


# ask user preferences
param = input("select the parameter for benchmarking: \n1. size \n2. <upcoming>\n")
act_code = input("1. Perform new experiment\n2. Check the average of existing output: \n")

if act_code == '1':
    if param == '1':
        path = './input_repo/size'
        
    elif param == '2':
        print("upcoming")

    perform_exp(path)
elif act_code == '2' :
    if param == '1':
        path = './output_repo/size/exp/'
        
    elif param == '2':
        print("upcoming")

    calc_avg(path)