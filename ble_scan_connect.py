# ble_scan_connect.py:
from tokenize import Pointfloat
from bluepy.btle import *
from bluepy.btle import *
import matplotlib.pyplot as plot

MAGX = []
MAGY = []
MAGZ = []

POINTS_NUMBER = 10

def dec(data):
    ans = []
    for i in data:
        ans.append(i)
    print("array =",ans)
    if len(ans)==2:
        data = ans[1]
    else:
        data = ans[2]*256+ans[1]
    
    if data >= 32768:
        data = data-65536
    return ans , data


class RingBuffer:
    def __init__(self,size_max):
        self.max = size_max
        self.data = []

    class __Full: 
        def append(self, x):
            self.data[self.cur] = x
            self.cur = (self.cur+1) % self.max
        def get(self):
            return self.data[self.cur:]+self.data[:self.cur]

    def append(self,x):
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0
            self.__class__ = self.__Full

    def get(self):
        return self.data


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
        print("original data =",data)
        # ans = []
        # for i in data:
        #     ans.append(i)
        # print("array =",ans)
        # if len(ans)==2:
        #     data = ans[1]
        # else:
        #     data = ans[2]*256+ans[1]
        
        # if data >= 32768:
        #     data = data-65536

        ans , data = dec(data)
        # print('arr =', ans)
        # print("A notification was received:", data)
        print(MAGX,MAGY,MAGZ)

        if len(MAGX) < POINTS_NUMBER:
            MAGX.append(data)
        elif len(MAGY) < POINTS_NUMBER:
            MAGY.append(data)
        elif len(MAGZ) < POINTS_NUMBER:
            MAGZ.append(data)




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


'''###############################################################################'''
service_uuid = 0x180F
SERVICE_UUID = UUID(service_uuid)
svc = dev.getServiceByUUID(SERVICE_UUID)
ch = svc.getCharacteristics()[0]
print(ch.valHandle)

dev.writeCharacteristic(ch.valHandle+1, bytes([1,0]))

while len(MAGX)<POINTS_NUMBER:
    if dev.waitForNotifications(1.0):
        # handleNotification() was called
        continue


dev.writeCharacteristic(ch.valHandle+1, bytes([0,0]))

'''###############################################################################'''
service_uuid = 0x1803
SERVICE_UUID = UUID(service_uuid)
svc = dev.getServiceByUUID(SERVICE_UUID)
ch = svc.getCharacteristics()[0]
print(ch.valHandle)

dev.writeCharacteristic(ch.valHandle+1, bytes([1,0]))

while len(MAGY)<POINTS_NUMBER:
    if dev.waitForNotifications(1.0):
        # handleNotification() was called
        continue

dev.writeCharacteristic(ch.valHandle+1, bytes([0,0]))

'''###############################################################################'''
service_uuid = 0x1809
SERVICE_UUID = UUID(service_uuid)
svc = dev.getServiceByUUID(SERVICE_UUID)
ch = svc.getCharacteristics()[0]
print(ch.valHandle)

dev.writeCharacteristic(ch.valHandle+1, bytes([1,0]))

while len(MAGZ)<POINTS_NUMBER:
    if dev.waitForNotifications(1.0):
        # handleNotification() was called
        continue

dev.writeCharacteristic(ch.valHandle+1, bytes([0,0]))




print(MAGX,MAGY,MAGZ)

t = [i for i in range(POINTS_NUMBER)]

f = plot.figure() 

ax = f.subplots(1,3,sharex='col',sharey='row')

ax[0].scatter(t, MAGX , c='blue')
ax[1].scatter(t, MAGY , c='c')
ax[2].scatter(t, MAGZ , c='g')

name_list=['MagX','MagY','MagZ']
for i in range(3):
    print(type(ax[i]))
    ax[i].set_xlabel('sample num')
    ax[i].legend([name_list[i]])

plot.show()



# disconnect
dev.disconnect()

