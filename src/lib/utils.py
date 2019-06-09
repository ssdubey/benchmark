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