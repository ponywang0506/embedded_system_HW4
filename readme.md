# Mbed Homework 4

## Introduction

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
This is the program to let raspberry pi be a gatt client and find gatt server(STM32L4S5I for example) and get the 3D values of magnetometer sensor from the server.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
To run the program, we should follow steps below:
1. run the command ```git clone https://github.com/ARMmbed/mbed-os-example-ble``` to get BLE_GattServer_AddService program
2. cd mbed-os-example-ble
3. New an mbed studio project, delete the main.cpp
4. Copy the files under the directory BLE_GattServer_AddService to the new project
5. Modify the ```target_overrides``` section in mbed_app.json in order to use the wanted board

for example, to use STM32 board, we must add 
```
        "NUCLEO_F401RE": {
            "target.components_add": ["BlueNRG_2"],
            "target.features_add": ["BLE"],
            "target.extra_labels_add": ["CORDIO"]
        },
```

6. Compile and Run



