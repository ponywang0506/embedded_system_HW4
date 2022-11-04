#ifndef BLE_MAG_SERVICE_H__
#define BLE_MAG_SERVICE_H__

#include "ble/BLE.h"
#include "ble/Gap.h"
#include "ble/GattServer.h"
#include <cstdint>
#include <stdint.h>

class Mag {
public:
    const static uint16_t MAGNETO_SERVICE_UUID = 0x180D;
    const static uint16_t MAGNETO_STATE_CHARACTERISTIC_UUID = 0x180E;

    Mag(BLE &_ble, char str[]):
        ble(_ble),
        valueBytes(str),
        magState(
            MAGNETO_STATE_CHARACTERISTIC_UUID,
            valueBytes.getPointer(),
            valueBytes.getNumValueBytes(),
            ValueBytes::MAX_VALUE_BYTES,
            GattCharacteristic::BLE_GATT_CHAR_PROPERTIES_NOTIFY
        )
        // magState(MAGNETO_STATE_CHARACTERISTIC_UUID,
        //         &str,
        //         GattCharacteristic::BLE_GATT_CHAR_PROPERTIES_NOTIFY)
        
        {
            GattCharacteristic *charTable[] = { &magState };
            GattService magService(
                Mag::MAGNETO_SERVICE_UUID,
                charTable,
                sizeof(charTable) / sizeof(charTable[0])
            );
            ble.gattServer().addService(magService);
        }

    void updateMagState(char str[])
    {
        valueBytes.updateHeartRate(str);

        ble.gattServer().write(
            magState.getValueHandle(),
            valueBytes.getPointer(),
            valueBytes.getNumValueBytes()
        );


        // ble.gattServer().write(magState.getValueHandle(), (uint8_t *)valueBytes, 4);


        // ble.gattServer().write(magState.getValueHandle(),(int8_t *)&(test[0]),60);
    }

///////////////////////////////////////////////////////////////////////////////////////////
protected:
    struct ValueBytes {
        static const unsigned MAX_VALUE_BYTES = 20;

        ValueBytes(char str[]) : valueBytes()
        {
            updateHeartRate(str);
        }

        void updateHeartRate(char str[])
        {
            for(int i = 0 ; i < 20 ; i ++)
            {
                valueBytes[i] = int(str[i]);
            }
        }

        uint8_t *getPointer()
        {
            return valueBytes;
        }

        const uint8_t *getPointer() const
        {
            return valueBytes;
        }

        unsigned getNumValueBytes() const
        {
            return MAX_VALUE_BYTES;
        }

    private:
        uint8_t valueBytes[MAX_VALUE_BYTES];
    };
///////////////////////////////////////////////////////////////////////////////////////////


private:
    BLE &ble;
    // ReadOnlyGattCharacteristic<char *> magState;
    // int8_t valueBytes[50];
    ValueBytes valueBytes;
    GattCharacteristic magState;
    // ReadOnlyGattCharacteristic<char *> magState;
    
};

#endif


/* mbed Microcontroller Library
 * Copyright (c) 2006-2013 ARM Limited
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
 
// #ifndef __BLE_MAG_SERVICE_H__
// #define __BLE_MAG_SERVICE_H__


// #include "ble/BLE.h"
// #include "ble/Gap.h"
// #include "ble/GattServer.h"
// #include <cstdint> 
// #include <stdint.h>
// #include <string.h>

// class Mag {
// public:
//     const static uint16_t MAG_SERVICE_UUID              = 0xA000;
//     const static uint16_t MAG_STATE_CHARACTERISTIC_UUID = 0xA001;
 
//     Mag(BLE &_ble, bool buttonPressedInitial) :
//         ble(_ble), magState(MAG_STATE_CHARACTERISTIC_UUID, &buttonPressedInitial, GattCharacteristic::BLE_GATT_CHAR_PROPERTIES_NOTIFY)
//     {
//         GattCharacteristic *charTable[] = {&magState};
//         GattService         magService(Mag::MAG_SERVICE_UUID, charTable, sizeof(charTable) / sizeof(GattCharacteristic *));
//         ble.gattServer().addService(magService);
//     }
 
//     void updateMagState(char str[]) {
//         int16_t valueBytes[50];
//         ble.gattServer().write(magState.getValueHandle(), (uint8_t *)&valueBytes, sizeof(char[1024]));
//     }
 
// private:
//     BLE                                 &ble;
//     ReadOnlyGattCharacteristic<bool>    magState;
// };
 
// #endif /* #ifndef __BLE_MAG_SERVICE_H__ */