import os
import subprocess
import time
import statistics
import numpy as np
import lib.utils as utils
import statistics

from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import FormatStrFormatter

latency_list = list(utils.tl.keys())
total = 0
filesize = '10mb'
#print(total)
#for latency in latency_list:
    #print(float(latency))
# run all the files(of same size) for one latency and find its average. 
# record the value as <size:throughput>
# goto step one with another latency

for latency in latency_list:
    total = 0
    for path, dirs, files in os.walk("/home/shashank/work/benchmark/input_repo/throughput/input_set_" + filesize + "/"):
        filecount = len(files)
        elapselst = []              # this is the list of elapsed time to calculate the standard deviation
        print("filecount = " + str(filecount))
        for file in files:
            cmd = ['ipfs', 'add', path + '/' + file]
            start = time.time()
            subprocess.run(cmd, stdout=subprocess.PIPE)
            time.sleep(float(latency))
            elapsed = time.time() - start
            total = total + elapsed
            elapselst.append(elapsed)
            # f = open("/home/shashank/work/benchmark/output_repo/throughput/" + filesize,"a+")
            # f.write(file + " throughput = " + str(utils.tl[latency]) + "elapsed = " + str(elapsed) + " total = " + str(total) + "\n")
            # f.close()

        
        avg = total/float(len(files)) #observed latency
        
        stddev = statistics.stdev(elapselst)

        observed_throughput = 1/(float(avg))
        offered_throughput = utils.tl[latency]
        
        
        f = open("/home/shashank/work/benchmark/output_repo/machinethroughput/" + filesize,"a+")
        #f.write("---------" + file + " " + str(offered_throughput) + " " + str(observed_throughput) + "\n") #we are taking separate files for our exp so that we can tackle
        #content addressability without having to delete the ipfs multiple times. since all the files are of same size and it does not matter if we repeat the same file, not printing the file name in the outptu
        #f.write("----------avg = " + str(avg) + "   offered = " + str(offered_throughput) + " " + "obser = " + str(observed_throughput) + "\n")
        f.write(str(offered_throughput) + " " + str(observed_throughput) + " " + str(stddev) + "\n")
        f.close()

