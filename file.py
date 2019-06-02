import os
import subprocess
import time

from matplotlib import pyplot as plt

keyset = []
valfloat = []
#os.walk returns path, directory and files
for path, dirs, files in os.walk("./size"):
    files.sort(key=int)
    
    if(os.path.isfile("output")):
        os.remove("output")
     
    for file in files:
        
        cmd = ['time', 'ipfs', 'add', './size/' + file]
        start = time.time()
        subprocess.run(cmd, stdout=subprocess.PIPE)
        elapsed = time.time() - start
        #putting values in list for plotting
        keyset.append(file)
        valfloat.append(elapsed)
        #putting values in file for ref and plotting
        f = open("output","a+")
        f.write(file + " " + str(elapsed) + "\n")
        f.close()

#below code can be used to take values from the file and plot
# plot = {}
# readfd = open("output", "r")
# lines = readfd.read()
# lines = lines.split("\n")
# del lines[-1]
# for line in lines:
#         kv = line.split(' ')
#         key = kv[0]
#         value = kv[1]
#         plot[key] = value

# readfd.close()

# keyset = plot.keys()
# valset = plot.values()

#keyint = []
#valfloat = []

# for key in keyset:
#     keyint.append(int(key))

# for val in valset:
#     valfloat.append(float(val))

#plotting
plt.bar(keyset, valfloat, width = 0.2, align='center', color='red', alpha=0.6)
plt.show()
