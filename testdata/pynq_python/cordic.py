from __future__ import print_function
import numpy as np
import sys
import struct

sys.path.append('/home/xilinx')
from pynq import Overlay
def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])
def hex_to_float(h):
    return float(struct.unpack('<f', struct.pack('<I', h))[0])

if __name__ == "main":
    print('Entry:', sys.argv[0])
    print('System argument(s):', len(sys.argv))

    print('Start of \"' + sys.argv[0] + "\"")

    ol = Overlay("/home/xilinx/IPBitFiles/svd.bit")
    regIP = ol.top_process_magnitude_0

    SCALE_FACTOR = 2**6
    
    for i in range(9):
        print("=================")
        for j in range(9):
            regIP.write(0x400, i*SCALE_FACTOR)
            regIP.write(0x800, j*SCALE_FACTOR)
            Res = regIP.read(0xc00)
            print("sqrt("+str(i+1)+"^2+"+str(j+1)+"^2) = "+str(Res/SCALE_FACTOR))
            
    print("=================")
    print("Exit process")
