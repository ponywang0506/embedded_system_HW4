# Mbed Homework 4

## Introduction

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
This is the program to let raspberry pi be a gatt client and find gatt server(STM32L4S5I for example) and get the 3D values of magnetometer sensor from the server.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
To run the program, we should follow steps below:

**Server Part**
1. run the command ```git clone https://github.com/ARMmbed/mbed-os-example-ble``` to get BLE_GattServer_AddService program
2. run the command ```git clone https://github.com/ponywang0506/embedded_system_HW4``` to get this program
3. cd mbed-os-example-ble
4. New an mbed studio project, delete the main.cpp
5. Copy the files under the directory BLE_GattServer_AddService to the new project
6. Replace the source folder in the new project to the one in embedded_system_HW4
7. Modify the ```target_overrides``` section in mbed_app.json in order to use the wanted board
for example, to use STM32 board, we must add 
```
        "DISCO_L475VG_IOT01A": {
            "target.features_add":["BLE"],
            "target.extra_labels_add":["CORDIO", "CORDIO_BLUENRG"]
        },
```
8. Compile and Run the mbed part and will build a gattserver on your board.

**Client Part**
1. Modify the device mac address at ```ble_scan_connect.py, line 65``` to your device mac address
```
        chosenDevice = "e3:f7:e6:cf:e6:6e"
```
2. Upload the ```ble_scan_connect.py``` to raspiberry pi and run the command ```sudo python ble_scan_connect.py``` to start the client.
3. The python program will save visualized image to ```result.png``` after ten data received. (Changing the value of ```POINT_NUMBERS``` can change sample number)



## Result
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
#### From command line of raspiberry pi, we may find the client received the data from server. The form is of "(MagX,MagY,MagZ)"
![](https://github.com/ponywang0506/embedded_system_HW4/blob/master/result/raspiberry_cmd.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
#### Visualizing the data of magneto
![](https://github.com/ponywang0506/embedded_system_HW4/blob/master/result/result.png)
