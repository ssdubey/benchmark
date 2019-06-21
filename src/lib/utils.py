encode = {}
encode.update({
    '16':'16B',
    '32':'32B',
    '16':'16B',
    '16':'16B',
    '32':'32B',
    '64':'64B',
    '128':'128B',
    '256':'256B',
    '512':'512B',
    '1024':'1KB',
    '2048':'2KB',
    '4096':'4KB',
    '8192':'8KB',
    '16384':'16KB',
    '32768':'32KB',
    '65536':'64KB',
    '131072':'128KB',
    '262144':'256KB',
    '524288':'512KB',
    '1048576':'1MB',
    '2097152':'2MB'
    })

from enum import Enum

class User_input(Enum):
    SIZE_PARAM = '1'
    NEW_EXPERIMENT = '1'
    CALC_AVERAGE = '2'

#tl = {}
#tl.update({'2': '0.5'
#    })

tl = {} #latency:throughput map
tl.update({
    '2': '0.5',
    '1': '1',
    '0.5': '2',
    '0.25': '4',
    '0.125': '8',
    '0.0625': '16',
    '0.03125': '32',
    '0.015': '64',
    '0.01':'100',
    '0.008': '125',
    '0.0066':'150',
    '0.005': '200',
    '0.004':'250',
    '0.0033':'300',
    '0.00285':'350',
    '0.0025':'400',
    '0.00222':'450',
    '0.002': '500',
    '0.00153':'650',
    '0.00125':'800',
    '0.001':'1000',
    '0':'1050'
    })
    
    
#     '0.5':'2',
#     '1':'1',
#     '2':'0.5',
#     '4':'0.25',
#     '8':'0.125',
#     '16':'0.0625',
#     '32':'0.03125',
#     '64':'0.015',
#     '128':'0.007',
#     '256':'0.039',
#     '512':'0.0019'
# })