---
title: SPIFFS
slug: spiffs
version: 0.3.7
code-url: https://github.com/pellepl/spiffs
site-url: https://github.com/pellepl/spiffs
draft: false
date: "2016-11-29 16:41:42"
last-updated: "2022-11-24"
components: []
libraries: []
licenses:
    - MIT
platforms: []
---
Spiffs is a file system intended for SPI NOR flash devices on embedded targets.

<!--more-->

### Features
- Specifically designed for low ram usage
- Uses statically sized ram buffers, independent of number of files
- Posix-like api: open, close, read, write, seek, stat, etc
- It can run on any NOR flash, not only SPI flash - theoretically also on embedded flash of a microprocessor
- Multiple spiffs configurations can run on same target - and even on same SPI flash device
- Implements static wear leveling
- Built in file system consistency checks
- Highly configurable

<!--github-projects-->
- [nodemcu-firmware](https://github.com/nodemcu/nodemcu-firmware). Lua based interactive firmware for ESP8266, ESP8285 and ESP32.
- [ESPUI](https://github.com/s00500/ESPUI). A simple web user interface library for ESP32 and ESP8266.
- [esp_littlefs](https://github.com/joltwallet/esp_littlefs). LittleFS port for ESP-IDF.
- [esp32-sniffer](https://github.com/ETS-PoliTO/esp32-sniffer). ESP32 firmware that sniffs PROBE REQUEST packets sent from smartphones looking for a Wi-Fi connection in order to extract different types of information.
- [ESP32_BLE_OTA_Arduino](https://github.com/fbiego/ESP32_BLE_OTA_Arduino). OTA update on ESP32 via BLE.
- [ESP32-targz](https://github.com/tobozo/ESP32-targz). 🗜️ An Arduino library to unpack/uncompress tar, gz, and tar.gz files on ESP32 and ESP8266.
- [ESP8266-Webserver-Tutorials](https://github.com/projetsdiy/ESP8266-Webserver-Tutorials). How to use ESP8266 as a Web Server.
- [SimpleFTPServer](https://github.com/xreef/SimpleFTPServer). A simple FTP server for Arduino, ArduinoSAMD WiFiNINA, esp8266, esp32, stm32 and Raspberry Pi Pico W.
- [ESP32_spiffs_example](https://github.com/loboris/ESP32_spiffs_example). Full example of using SPIFFS with ESP32 VFS.
- [Bleeper](https://github.com/workilabs/Bleeper). Library to manage your firmware configurations written in C++.
- [SFX-I2S-web-trigger](https://github.com/bbx10/SFX-I2S-web-trigger). ESP8266 Sound F/X I2S web trigger.
- [esp-fs-webserver](https://github.com/cotestatnt/esp-fs-webserver). ESP32/ESP8266 webserver, WiFi manager and web editor Arduino library.
- [ESPxWebFlMgr](https://github.com/holgerlembke/ESPxWebFlMgr). Manage your ESP8266/ESP32 SPIFFS/LittleFS files with a simple web based interface.
- [esp32-asyncwebserver-fileupload-example](https://github.com/smford/esp32-asyncwebserver-fileupload-example). Examples of how to upload files to an ESP32 using Asyncwebserver, SPIFFS and an Upload progress bar..
- [ESP_DoubleResetDetector](https://github.com/khoih-prog/ESP_DoubleResetDetector). ESP_DoubleResetDetector is a library for the ESP32/ESP8266 Arduino platform to enable trigger configure mode by resetting twice..
- [Blynk_WM](https://github.com/khoih-prog/Blynk_WM). Blynk and WiFiManager Library for configuring/auto(re)connecting ESP8266/ESP32 modules to the best or available MultiWiFi APs and MultiBlynk servers at runtime, with or without SSL. Configuration data saved in either SPIFFS or EEPROM..
- [remote-control-with-websocket](https://github.com/m1cr0lab-esp32/remote-control-with-websocket). ESP32 Remote Control with WebSocket.
- [Effortless-SPIFFS](https://github.com/thebigpotatoe/Effortless-SPIFFS). A class designed to make reading and storing data on the ESP8266 and ESP32 effortless.
- [SPIFFSLogger](https://github.com/bitmario/SPIFFSLogger). A minimal library for binary data logging in ESP8266 systems.
- [ESP8266SDUpdater](https://github.com/tobozo/ESP8266SDUpdater). 💾 ESP8266 Prequel to M5Stack-SD-Updater.
- [watch](https://github.com/lunokjod/watch). lunokWatch (lilygo twatch2020 series).
- [BlynkGSM_Manager](https://github.com/khoih-prog/BlynkGSM_Manager). Simple GSM shield Manager for Blynk and ESP32 / ESP8266 boards, with or without SSL, configuration data saved in SPIFFS / EEPROM. This library enables user to include both Blynk GSM/GPRS and WiFi libraries in one sketch, run both WiFi and GSM/GPRS simultaneously, or select one to use at runtime after reboot..
- [ESP32-Ruuvitag-Collector](https://github.com/hpirila/ESP32-Ruuvitag-Collector). Ruuvitag data collector for ESP32.
- [ESP8266-WiFi-Relay](https://github.com/Jorgen-VikingGod/ESP8266-WiFi-Relay). simple sketch of using ESP8266WebServer to switch relays on GPIO pins. It serves a simple website with toggle buttons for each relay.
- [RTCMemory](https://github.com/fabianoriccardi/RTCMemory). An intuitive library to simplify read and write operations on RTC memory of ESP8266 and its backup on flash memory..
- [Blynk_Async_WM](https://github.com/khoih-prog/Blynk_Async_WM). Simple WiFiManager for Blynk and ESP8266/ESP32 (including ESP32-S2, ESP32-C3) with or without SSL, configuration data saved in either LittleFS, SPIFFS or EEPROM. This library, using AsyncWebServer instead of (ESP8266)WebServer, for configuring/auto(re)connecting ESP8266/ESP32 modules to best or available MultiWiFi APs and MultiBlynk servers at runtime. Enable adding dynamic custom parameters from sketch and input using the same Config Portal. Config Portal will be auto-adjusted to match the number of dynamic parameters. Optional default Credentials to be autoloaded into Config Portal to use or change instead of manually input. Static STA IP and DHCP Hostname as well as Config Portal AP channel, IP, SSID, Password can be configured. Multi or Double DetectDetector feature permits entering Config Portal as requested..
- [easy_Iot_file_system](https://github.com/renat2985/easy_Iot_file_system). A simple and beautiful file system for your Iot devices. For ESP8266, ESP32.
- [ESP32Cam-MQTT-SPIFFS-PIR](https://github.com/JJFourie/ESP32Cam-MQTT-SPIFFS-PIR). ESP32Cam - PIR-triggered photos uploaded to webserver. Motion broadcast via MQTT. Video streaming. Settings stored in SPIFFS. Temperature sensor..
- [ESP8266-WiFi-Relay-Async](https://github.com/Jorgen-VikingGod/ESP8266-WiFi-Relay-Async). simple sketch for ESP8266 of using ESPAsyncWebServer to switch relays on GPIO pins, serves a simple website with toggle buttons for each relay and uses AsyncWiFiManager to configure WiFi network..
- [settingsmanager](https://github.com/SergiuToporjinschi/settingsmanager). Saving, reading and changing settings from Json file on SPIFFS.
- [Timezone_Generic](https://github.com/khoih-prog/Timezone_Generic). Library to facilitate time zone conversions and automatic daylight saving (summer) time adjustments. For ESP8266, ESP32, WT32-ETH01 (ESP32 + LAN8720), SAMD21, SAMD51, nRF52, STM32F/L/H/G/WB/MP1, Teensy, SAM DUE, RTL8720DN, RP2040-based (Nano_RP2040_Connect, RASPBERRY_PI_PICO), Portenta_H7 (Ethernet or WiFi) boards, etc. using W5x00/ENC28J60/LAN8742A Ethernet, ESP or ESP-AT WiFi or WiFiNINA. Ethernet_Generic library is used as default for W5x00..
- [spiffs_circular_queue](https://github.com/rykovv/spiffs_circular_queue). ESP-IDF and PlatformIO compatible library for a circular queue or circular FIFO buffer over SPIFFS..
- [DS323x_Generic](https://github.com/khoih-prog/DS323x_Generic). Library for DS3231/DS3232 Extremely Accurate I2C-Integrated RTC/TCXO/Crystal. For nRF52, SAMD21/SAMD51, STM32F/L/H/G/WB/MP1, Teensy, Portenta_H7 boards, RP2040-based, etc. besides ESP8266/ESP32, using ESP WiFi, Portenta_H7 WiFi, WiFiNINA, Portenta_H7 Ethernet, Ethernet W5x00, ENC28J60, LAN8742A, ESP8266/ESP32 AT-command WiFi. Ethernet_Generic library is used as default for W5x00 Ethernet.
- [ESP32_SEA_SPIFFS_Loader](https://github.com/Cellgalvano/ESP32_SEA_SPIFFS_Loader). SPIFFS Bitstreamloader for the Spartan Edge Accelerator Board.
- [ESP32-OTA-File-management](https://github.com/AR-D-R/ESP32-OTA-File-management). ESP32 Async OTA Firmware Update & File Management..
- [ESP8266-arduino-serial-programmer](https://github.com/gaurabdg/ESP8266-arduino-serial-programmer). A serial bootloader utility---using an ESP12E to upload programs to Arduino boards, using the SPIFFS file system. .
- [Blynk_Async_ESP32_BT_WF](https://github.com/khoih-prog/Blynk_Async_ESP32_BT_WF). Simple WiFiManager for Blynk and ESP32 with or without SSL, configuration data saved in either SPIFFS or EEPROM. Enable inclusion of both ESP32 Blynk BT/BLE and WiFi libraries. Then select one at reboot or run both. Eliminate hardcoding your Wifi and Blynk credentials and configuration data saved in either SPIFFS or EEPROM. Using AsyncWebServer instead of (ESP8266)WebServer..
- [ReadMePaper](https://github.com/kc1r74p/ReadMePaper). Just some ESP32 - ePaper 7 Color project 🎉.
- [ESP32_ASYNC_WEB_SERVER_SPIFFS_OTA](https://github.com/har-in-air/ESP32_ASYNC_WEB_SERVER_SPIFFS_OTA). Demo of ESP32 Async Web Server for webpage access and OTA firmware updates, SPIFFS hosted html and css files, DNS for user friendly webpage url. Visual Studio Code + PlatformIO project..
- [ESP_MultiResetDetector](https://github.com/khoih-prog/ESP_MultiResetDetector). Library to detect a multi reset within a predetermined time, using RTC Memory, EEPROM, LittleFS or SPIFFS for ESP8266 and ESP32, ESP32_C3, ESP32_S2, ESP32_S3. An alternative start-up mode can be used. One example use is to allow re-configuration of device WiFi credentials.
- [Blynk_Async_GSM_Manager](https://github.com/khoih-prog/Blynk_Async_GSM_Manager). Library, now using AsyncWebServer instead of (ESP8266)WebServer, for enabling GSM/GPRS and WiFi running simultaneously as well as configuring/auto(re)connecting at runtime GSM shields to Internet and Blynk and ESP8266/ESP32 WiFi modules to best or available MultiWiFi APs and MultiBlynk servers. Enable adding dynamic custom parameters from sketch and input using the same Config Portal. Config Portal will be auto-adjusted to match the number of dynamic parameters. Optional default Credentials to be autoloaded into Config Portal to use or change instead of manually input. Static STA IP and DHCP Hostname as well as Config Portal AP channel, IP, SSID, Password can be configured. DoubleDetectDetector feature permits entering Config Portal as requested..
- [madWiFi](https://github.com/DaVieS007/madWiFi). madWiFi Project on ESP8266.
- [ESP-Datalogger](https://github.com/iotlearner0level/ESP-Datalogger). A general purpose datalogger for esp8266 with provisions for displaying data & graphing it. Also send data to firebase..
- [hommie_logger](https://github.com/r-zlotorzynski/hommie_logger). Creates logs in file using the circular buffer algorithm.
- [ESP32_32x32RGBMatrix](https://github.com/polygontwist/ESP32_32x32RGBMatrix). ESP32 width 32x32 RGB Matrix, OTA, SPIFFS.
- [EspSaveCrashSpiffs](https://github.com/brainelectronics/EspSaveCrashSpiffs). Save exception details and stack trace to the SPIFFS everytime the ESP8266 crashes.
- [Esp32PC8001SIO](https://github.com/bellTanTan/Esp32PC8001SIO). NEC/PC-8001 SIO(DIP16 socket)に挿すゲタのハードとソフトです。ESP32とBME280を活用してSNTP/BME280情報取得/FTPorSPIFFSリスト取得/FTPorSPIFFS DL GETを行うことが出来ます。.
- [geiger-counter-iot](https://github.com/mkgeiger/geiger-counter-iot). Geiger Mueller counter for IoT on an ESP8266 microcontroller.
- [ESP8266-config-data](https://github.com/jxmot/ESP8266-config-data). A demonstration of how to use SPIFFS on the ESP8266.
- [esp8266_spiffs](https://github.com/quackmore/esp8266_spiffs). Spiffs for ESP8266 NON-OS SDK. Forked from the original SPIFFS. No dependecies..
- [ESP8266-DHT-SPIFFS](https://github.com/Deliaz/ESP8266-DHT-SPIFFS). ESP8266 Web interface for DHT22.
- [ConfigAssist-ESP32-ESP8266](https://github.com/gemi254/ConfigAssist-ESP32-ESP8266). A lightweight library allowing quick configuration for esp32/esp8266 devices using async requests. Edit application vars using a responsive captive portal and a json definition  dictionary and saving them on a file in local storage..
- [RTKBaseManager](https://github.com/jangleboom/RTKBaseManager). Web interface (on ESP32) for managing caster and wifi credentials on a real time kinematics base station..
- [esp-razorlike](https://github.com/gertvantslot/esp-razorlike). Code generator, generates code for a Web-server on the ESP8266 powered from Html pages with Razor-like syntax..
- [7-Segment-Clock](https://github.com/iml885203/7-Segment-Clock). 7 segment clock with LED's.
- [ESP32WebScope](https://github.com/guohaomeng/ESP32WebScope). 只用一块ESP32制作的ESP32网页示波器+波形发生器,可以拿来生成以及观察低频信号 esp32 web oscilloscope.
- [esp8266-MLX90614](https://github.com/jxmot/esp8266-MLX90614). A sketch that reads a MLX90614 non-contact temperature sensor. An HTML/JavaScript client is also present..
- [NMEA0183-WiFi](https://github.com/AndrasSzep/NMEA0183-WiFi). This is and Arduino ESP32 code to display UDP-broadcasted NMEA0183 messages through a webserver to be seen on any mobile device for free.
- [DevFsUploadESP](https://github.com/DaveBrad/DevFsUploadESP). ESP32 ESP8266 file-system upload development aid with SPIFFS or LittleFS file-system.
- [RTKRoverManager](https://github.com/jangleboom/RTKRoverManager). Web interface (on ESP32) for managing the credential settings for real time kinematics rover..
- [esp-configuration-manger](https://github.com/awaistkd/esp-configuration-manger). Configuration manager for ESP32  and ESP8266.
- [esp32_spiffsgen](https://github.com/Shaopus/esp32_spiffsgen). how to use mkspiffs in esp32.
- [awtk-fs-adapter](https://github.com/zlgopen/awtk-fs-adapter). filesystem adapter for awtk.
- [ESP32_WEB-SERVER_SPIFFS](https://github.com/SimonCrA/ESP32_WEB-SERVER_SPIFFS). Este código permite al esp32 conectarse a una red WIFI, usando el SPIFFS monta los archivos HTML y CSS en la memoria flash, y sirve una página web..
- [IOT_ESP8266_webserver_SPIFFS](https://github.com/Gupta-Harshit/IOT_ESP8266_webserver_SPIFFS). A basic How-to for different functionalities of the ESP8266 (NodeMCU) - web server and SPIFFS file system Note - these codes are working sub-parts of a project I am working on.
- [ESP8266-WSN](https://github.com/hatembk/ESP8266-WSN). ESP8266 wireless sensor network using websockets and chartjs to send and display sensor data .
- [ShelfEdgeClock](https://github.com/CaptSnus/ShelfEdgeClock). Shelf Edge Clock is a sleek clock hidden behind the edges of shelves..
- [esp8266-WSN](https://github.com/mssm199996/esp8266-WSN). WSN using ESP8266.
- [ESP8266-WiFi-Relay-Bahtinov-Masks](https://github.com/Jorgen-VikingGod/ESP8266-WiFi-Relay-Bahtinov-Masks). simple sketch for ESP8266 of using ESP8266WebServer to switch relays on GPIO pins, control servos to open and close masks, serves a simple website with toggle buttons for each relay and mask servo..
- [test_spiffs_read_data](https://github.com/ghettobuilder2027/test_spiffs_read_data). List all files and their content of the root folder of the spiffs memory on esp32.
- [fs-uploader-spiffs](https://github.com/TakayunDev/fs-uploader-spiffs). filesystem uploader for esp32, using mkspiffs..
- [nodemcu-device](https://github.com/fikin/nodemcu-device). Collection of Lua modules for NodeMCU.
- [ESP8266-config-data-V2](https://github.com/jxmot/ESP8266-config-data-V2). Based on my 'ESP8266-config-data' repo, but with extensive improvements and modifications..
- [Sistema-de-apertura-de-porton-con-modulo-GSM---Taller-comunicaciones-electricas](https://github.com/andrey-08/Sistema-de-apertura-de-porton-con-modulo-GSM---Taller-comunicaciones-electricas). Se busca la implementación de protocolos de comunicación entre dispositivos a través de aplicación de una ESP32 v1.3  para apertura de un portón eléctrico, el proyecto se realiza sobre una maqueta..
- [arduino-esp8266-spiffs-utils](https://github.com/mhightower83/arduino-esp8266-spiffs-utils). Some misc. utilities for accessing, backing up the SPIFFS file system on a ESP8266 running a Web Server sketch..
- [Y3S2](https://github.com/carmenauk/Y3S2). IO&E Project 2; ESP32 .
- [vortexCannon-AP](https://github.com/creative-engineering/vortexCannon-AP). ESP32 Arduino code for Vortex Cannon LED & message control interface.
- [Thing](https://github.com/g3rb3n/Thing). A MQTT/Wifi/SPIFFS library based on PubSubClient for creating sensor and actuator things on the ESP..
- [iot-esp8266-serial-fwd](https://github.com/devel0/iot-esp8266-serial-fwd). use esp8266 as a serial forwarder over wifi.
- [avr_spiffs](https://github.com/lshw/avr_spiffs). add spiffs to ardino mega 2560.
- [IoT-Project-on-Agricultural-Data-Monitoring](https://github.com/Ariful17/IoT-Project-on-Agricultural-Data-Monitoring). An IoT project on agricultural data monitoring using nodemcu.
- [arduino-esp-utils](https://github.com/josephlarralde/arduino-esp-utils). a collection of utility classes for esp8266 and esp32 chips.
- [AC_control](https://github.com/samlewis02/AC_control). Switch A/C on and off using MQTT.
- [IoT-project-on-industrial-operation-and-room-condition](https://github.com/Ariful17/IoT-project-on-industrial-operation-and-room-condition). An arduino and nodemcu are used to monitor various room conditions and send them over the local internet..
- [esp32logger](https://github.com/Jurand2020/esp32logger). Custom temperature / humidity logger.
- [EasyINI](https://github.com/bvujovic/EasyINI). Utility class for reading from/writing to .ini files on ESP's SPIFFS.
- [format_spiffs_esp32](https://github.com/ghettobuilder2027/format_spiffs_esp32). List files on spiffs memory and format if wanted.
- [IoT-Project-on-HVAC](https://github.com/Ariful17/IoT-Project-on-HVAC). An IoT project that monitors Heating, Ventilation and Air-Conditioning of a closed area. .
- [UBA_MSE-6Co2021_SED-TPI](https://github.com/mauriciobarroso/UBA_MSE-6Co2021_SED-TPI). Trabajo práctico integrador para la materia Sistemas Embebidos Distribuidos.
- [MeinDataLogger](https://github.com/bvujovic/MeinDataLogger). Customer defined data is added to circular buffer and then dumped to LittleFS/SPIFFS (ESP8266/ESP32) file..
- [Esp32-Webserver](https://github.com/Joaosilgo/Esp32-Webserver). 📡.
- [Freebees-AC-Arduino](https://github.com/FreebeesClub/Freebees-AC-Arduino). Access control using Arduino IDE ESP32 PN532 DS3231 MQTT.
- [ESP32_MQTT_Motor_Control](https://github.com/JJFourie/ESP32_MQTT_Motor_Control). Use an ESP32 to automate control of a DC motor based on MQTT messages received from e.g. Home Assistant.
- [MCOTAUpdater](https://github.com/calfizzi/MCOTAUpdater). Simple Updaer using ESP HTTPUpdate library.
- [animated_gif_sdcard_spiffs](https://github.com/thelastoutpostworkshop/animated_gif_sdcard_spiffs). Animated GIF stored in SD Card and played from SPIFFS on a Round Display (GC9A01) with the ESP32.
- [esp8266-home-automation](https://github.com/snackk/esp8266-home-automation). Home Automation firmware for IoT devices based on esp8266..
- [ESP32-monaco-editor-spiffs](https://github.com/JakubAndrysek/ESP32-monaco-editor-spiffs). This is the example that is possible to create VSCode like editor on ESP32 based on Monaco editor..