import os
import subprocess
import time
import statistics
import numpy as np
import lib.utils as utils

from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
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
    #plt.patches.Patch(label='data')
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
    path_to_save = "/home/shashank/work/benchmark/test_output" + str(timestamp)
    #cmd = ['cp', '/home/shashank/work/benchmark/test_output', path_to_save + '.txt']

    plt.savefig(path_to_save)
    subprocess.run(cmd, stdout=subprocess.PIPE)
    #plt.show()




perform_exp()

# # ask user preferences
# param = input("select the parameter for benchmarking: \n1. size \n2. <upcoming>\n")
# act_code = input("1. Perform new experiment\n2. Check the average of existing output: \n")
# #act_code = utils.User_input.NEW_EXPERIMENT.value
# #param = utils.User_input.SIZE_PARAM.value

# if act_code == utils.User_input.NEW_EXPERIMENT.value:
#     if param == utils.User_input.SIZE_PARAM.value:
#         path = '/home/shashank/work/benchmark/input_repo/size/input_set1'
        
#     elif param == '2':
#         print("upcoming")

#     perform_exp(path)
# elif act_code == '2' :
#     if param == utils.User_input.SIZE_PARAM.value:
#         path = './output_repo/size/docker_op_collect/output2/'
        
#     elif param == '2':
#         print("upcoming")

#     calc_avg(path)

