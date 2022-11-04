# ble_scan_connect.py:
from tokenize import Pointfloat
from bluepy.btle import *
from bluepy.btle import *
import matplotlib.pyplot as plot

POINTS_NUMBER = 10
MAGX = []
MAGY = []
MAGZ = []
TIME = 0


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print ("Discovered device", dev.addr)
        elif isNewData:
            print ("Received new data from", dev.addr)
    

class MyDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        global TIME
        print("original data =",data)
        data = str(data)
        d = data
        d = d.split('(')[1]
        d = d.split(')')[0]
        print("(MagX,MagY,MagZ) = (%s)"%d)

        d = d.split(',')
        print(d)
        rawdata = [int(s) for s in d]

        if TIME < POINTS_NUMBER:
            MAGX.append(rawdata[0])
            MAGY.append(rawdata[1])
            MAGZ.append(rawdata[2])
        elif TIME == POINTS_NUMBER:
            drawResult()

        TIME += 1
            

def drawResult():
    t = [i for i in range(POINTS_NUMBER)]
    f = plot.figure() 
    ax = f.subplots(1,3,sharex='col',sharey='row')
    ax[0].scatter(t, MAGX , c='blue')
    ax[1].scatter(t, MAGY , c='c')
    ax[2].scatter(t, MAGZ , c='g')
    name_list=['MagX','MagY','MagZ']
    for i in range(3):
        ax[i].set_xlabel('sample num')
        ax[i].legend([name_list[i]])
    plot.savefig('result.png')
    print("Finish Drawing The Result")


chosenDevice = "e3:f7:e6:cf:e6:6e"

scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)
n = 0
addr = []
chosen = -1
for dev in devices:
    # print ("%d: Device %s (%s), RSSI=%d dB" % (n, dev.addr, dev.addrType, dev.rssi))
    addr.append(dev.addr)
    if dev.addr == chosenDevice:
        chosen = n
        break
    n += 1
    # for (adtype, desc, value) in dev.getScanData():
        # print (" %s = %s" % (desc, value))

# number = input('Enter your device number: ')
# print ('Device', number)
# num = int(number)

num = chosen
print (addr[num])
#
print ("Connecting...")
dev = Peripheral(addr[num],'random')
#
print ("Services...")
for svc in dev.services:
    print (str(svc))
#

#   --------------------- above implement connection -------------------------------

dev.setDelegate( MyDelegate() )


service_uuid = 0x180D
SERVICE_UUID = UUID(service_uuid)

svc = dev.getServiceByUUID(SERVICE_UUID)
ch = svc.getCharacteristics()[0]
print(ch.valHandle)

dev.writeCharacteristic(ch.valHandle+1, bytes([1,0]))

while TIME<100:
    if dev.waitForNotifications(1.0):
        continue


dev.disconnect()

