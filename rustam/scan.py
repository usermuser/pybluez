import time
import my_inquiry_with_rssi as lib

import os
import sys
import struct
import bluetooth._bluetooth as bluez
import bluetooth

DEVICE = '04:B1:67:84:6E:21'

print('[+] starting')

for i in range(10):
    
    dev_id = 0
    try:
        sock = bluez.hci_open_dev(dev_id)
    except:
        print("error accessing bluetooth device...")
        sys.exit(1)

    try:
        mode = lib.read_inquiry_mode(sock)
    except Exception as e:
        print("error reading inquiry mode.  ")
        print("Are you sure this a bluetooth 1.2 device?")
        print(e)
        sys.exit(1)
    print("current inquiry mode is %d" % mode)    
    
    lib.device_inquiry_with_with_rssi(sock)
    time.sleep(0.3)

# device_inquiry_with_with_rssi(sock)
