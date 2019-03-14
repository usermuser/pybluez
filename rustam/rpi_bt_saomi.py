# Device 04:B1:67:84:6E:21 saomi
# Device 3C:A1:0D:8A:FC:59 Самса Чебурек sgs4
from bluepy.btle import Scanner, DefaultDelegate
import time

SAOMI = '04:B1:67:84:6E:21'
SAMSUNG = '3C:A1:0D:8A:FC:59'
DELAY = 0.5

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print ("Discovered device", dev.addr)
        elif isNewData:
            print ("Received new data from", dev.addr)

scanner = Scanner().withDelegate(ScanDelegate())
# devices = scanner.scan(10.0)


for i in range(5): # tries qty
    
    print('[+] Starting scanning process for 2 secs')
    devices = scanner.scan(5.0) # scanning time in secs
    print('[+] Scanning done')
    
    target_mac = False
    
    for dev in devices:
        # print(type(dev.addr))
        #if dev.addr == '04:B1:67:84:6E:21':  # my saomi phone mac
        if dev.addr == SAOMI or dev.address_string == SAOMI:
            print('[+] saomi found, rssi: ',dev.rssi)
            target_mac = True
        time.sleep(DELAY)
        print('DELAY: {} seconds'.format(DELAY)) 
        
    if not target_mac:
        print('[-] target mac not found, bt is on?\n\n')
        time.sleep(0.5)    
    
