---
title: Mongoose OS
slug: mongoose-os
version: 2.20.0
code-url: https://github.com/cesanta/mongoose-os
site-url: https://mongoose-os.com/
date: "2018-01-24 01:43:59"
last-updated: "2025-04-08"
star: 2547
components:
    - scheduler
    - task-management
    - timer-management
    - network-stack
    - wifi
    - http-client
    - http-server
    - mqtt-client
    - tls-ssl
    - filesystem
    - ota-update
    - shell-cli
    - logging
licenses:
    - Apache-2.0
    - Commercial
platforms:
    - arm-cortex-m
    - xtensa
---
Mongoose OS is an open-source IoT firmware development framework designed for resource-constrained microcontrollers like ESP32, ESP8266, STM32, and TI CC32xx series. It enables rapid development with support for both C/C++ and JavaScript (via its embedded mJS engine). Key features include reliable Over-the-Air (OTA) updates with rollback, built-in security features like flash encryption and TLS, and seamless integration with major cloud platforms (AWS IoT, Google Cloud IoT, Azure IoT) and MQTT servers. It comes with the `mos` command-line tool for simplified building, flashing, and device management.

<!--more-->

Mongoose OS provides a comprehensive environment for building connected embedded products. It aims to reduce development time and complexity by offering pre-built libraries, a configuration framework, remote procedure call (RPC) capabilities, and integrated device management through its companion cloud service, mDash.

The framework is built upon a real-time kernel (FreeRTOS for most ports, except ESP32 which uses its specific version) providing standard OS services. Developers can leverage the `mos` tool, which offers both a command-line interface and a web UI, to manage the entire development lifecycle: cloning example projects, building firmware, flashing devices, configuring settings (like Wi-Fi credentials), and interacting with device services remotely.

Security is a core aspect, with support for encrypted file systems, secure boot, crypto-chip integration, and an optimized mbedTLS library for secure communication. The OTA update mechanism is designed for reliability, ensuring devices can be updated securely and efficiently in the field, with automatic rollback if an update fails.

Mongoose OS supports development in both C/C++ for performance-critical tasks and JavaScript (using the lightweight `mJS` engine) for application logic, offering flexibility to developers. It has built-in support for popular communication protocols like MQTT, HTTP, and WebSockets, facilitating easy connection to cloud services and backend systems.

The project is dual-licensed, offering a free Apache 2.0 licensed Community Edition and a commercially licensed Enterprise Edition with additional features and support options. It's recognized and recommended by major industry players like AWS, Google Cloud, Microsoft Azure, Texas Instruments, and STMicroelectronics.

## Features

-   **Multi-Language Development:** Supports application development in both C/C++ and JavaScript (via embedded mJS engine).
-   **Over-The-Air (OTA) Updates:** Reliable OTA firmware updates with rollback capability.
-   **Security:** Built-in support for flash encryption, crypto chips, and optimized mbedTLS.
-   **Cloud Integration:** Native support for AWS IoT, Google Cloud IoT Core, Microsoft Azure IoT, Adafruit IO, and generic MQTT/REST backends.
-   **Remote Management:** Device management via mDash cloud service or custom solutions using RPC.
-   **Cross-Platform:** Supports popular MCUs including ESP32, ESP8266, STM32 (F4, L4, F7), TI CC3200/CC3220.
-   **Rich Connectivity:** Includes libraries for WiFi, MQTT, HTTP, WebSockets, DNS, SNTP.
-   **Configuration Management:** Flexible device configuration system accessible via CLI or RPC.
-   **RPC Framework:** Enables remote invocation of device functions over serial, MQTT, HTTP.
-   **Filesystem Support:** On-device filesystem for storing configuration and assets.
-   **`mos` Tool:** Unified command-line tool (with optional Web UI) for build, flash, configuration, and communication.
-   **Embedded JavaScript Engine (mJS):** Lightweight engine for scripting device logic.
-   **Dual Licensing:** Available under Apache 2.0 (Community) or Commercial (Enterprise) licenses.

## Components

-   **scheduler:** Core task scheduling (provided by underlying RTOS like FreeRTOS).
-   **task-management:** Task creation and management primitives.
-   **timer-management:** Software timers for scheduling events.
-   **network-stack:** Integrated networking capabilities (likely leveraging Mongoose library).
-   **wifi:** Configuration and management of Wi-Fi connectivity.
-   **http-client:** Making HTTP(S) requests.
-   **http-server:** Serving web content from the device.
-   **mqtt-client:** Connecting and communicating with MQTT brokers.
-   **tls-ssl:** Secure communication using mbedTLS.
-   **filesystem:** Managing files on the device's storage.
-   **ota-update:** Core component for firmware updates.
-   **shell-cli:** Interaction via the `mos` command-line tool.
-   **logging:** System and application logging framework.

### Sample projects and resources
<!--github-projects-->
- [mgos-to-tasmota](https://github.com/yaourdt/mgos-to-tasmota). A minimal firmware for OTA (over the air) flashing Tasmota, HAA, or ESPurna from Mongoose OS or compatible firmware types..
- [tasmota-to-mgos](https://github.com/yaourdt/tasmota-to-mgos). A minimal firmware for OTA (over the air) flashing Mongoose OS from Tasmota, Tuya stock, or compatible firmware types..
- [weather-station-gcp-mongoose-os](https://github.com/alvarowolfx/weather-station-gcp-mongoose-os). A Weather station made with an ESP32, sending data through Google Cloud IoT Core and storing in BigQuery.
- [mel-ac](https://github.com/mongoose-os-libs/mel-ac). Mitsubishi Electric AC (air conditioner unit) and ATW (air to water unit) control library for Mongoose OS.
- [sonoff-basic-openhab](https://github.com/mongoose-os-apps/sonoff-basic-openhab). A Sonoff Basic firmware to work with openHAB.
- [aqua-app](https://github.com/atanasyanew/aqua-app). Fish tank automation.
- [PIR-Monitor](https://github.com/Tommystus/PIR-Monitor). ESP8266 PIR monitor with deep sleep and RTC memory store.
- [pellet-aws-iot](https://github.com/daniele-salvagni/pellet-aws-iot). 🔥 Mongoose OS firmware for ESP32 to connect a pellet stove (Micronova) to AWS IoT. Implemented for a Piazzetta P937 model. (WIP).
- [losant-mqtt-mongoose-os](https://github.com/Losant/losant-mqtt-mongoose-os). This is an example Mongoose OS app that connects to Losant via MQTT..
- [IoTea](https://github.com/seanfhear/IoTea). IoT system for growing a tea plant..
- [mgos_telegram](https://github.com/kotelnikov/mgos_telegram). Telegram Bot API for Mongoose OS.
- [timezones](https://github.com/mamuesp/timezones). A Mongoose-OS library which will set the cryptic 'sys.tz_spec' from a human readable notation..
- [mongoose_os_playground](https://github.com/pmanna/mongoose_os_playground). Playground app for Mongoose OS - ESP 32 & ESP8266.
- [esp-temp](https://github.com/UtkarshVerma/esp-temp). :thermometer: A Mongoose OS app for sending temperature readings of ESP devices to Losant..
- [losant-temp-sensor](https://github.com/mongoose-os-apps/losant-temp-sensor). :thermometer: A Mongoose OS app for sending temperature readings of ESP32 to Losant..
- [arduino-rf24](https://github.com/eduardb/arduino-rf24). The nRF24L01 library for Arduino ported to Mongoose OS.
- [LilyGo-HiGrow-Sensor-v1](https://github.com/mercdev/LilyGo-HiGrow-Sensor-v1). Use this code with MongooseOS and the LilyGo HiGrow ESP32 Plant Monitoring Sensor board (v1) to obtain sensor readings and control LED's.
- [LilyGo-HiGrow-Sensor-v1](https://github.com/mongoose-os-apps/LilyGo-HiGrow-Sensor-v1). LilyGo HiGrow ESP32 Plant Monitoring Sensor Firmware (Hardware v1).
- [mos-native](https://github.com/v-kiniv/mos-native). Build Mongoose OS apps without docker to speed up process.
- [mgos-combine](https://github.com/yaourdt/mgos-combine). Combine all parts of a Mongoose OS firmware ZIP-file into a single binary.
- [losant-mqtt](https://github.com/mongoose-os-apps/losant-mqtt). Losant + Mongoose OS example.
- [mgos_skeleton](https://github.com/kotelnikov/mgos_skeleton). Mongoose OS Initial project skeleton.
- [sonoff-http](https://github.com/OllieDay/sonoff-http). Alternative firmware for the ITEAD Sonoff Wi-Fi Remote Control Smart Switch.
- [mosmqtt_wakeonlan](https://github.com/jamezrin/mosmqtt_wakeonlan). Mongoose OS app designed to run on esp8266 to help you wake your PCs remotely in a secure manner..
- [mongoose-os-docker](https://github.com/cruftlab/mongoose-os-docker). Docker container with the Mongoose OS (mos) tool.
- [esp32-experiments](https://github.com/lucabelluccini/esp32-experiments). A set of ESP32 experiments.
- [mgos-alexa-wemo](https://github.com/yaourdt/mgos-alexa-wemo). A Mongoose OS library emulating WEMO UPnP plugs in Amazon Alexa.
- [iot-workshop](https://github.com/eyantra-iot-platform/iot-workshop). Resources for e-Yantra IoT workshop.
- [mel-ac-demo](https://github.com/mongoose-os-apps/mel-ac-demo). Demo app for the MEL-AC library. Controll Mitsubishi Electirc AC and AWT unit using Mongoose OS RPC.
- [mongoose-os-x](https://github.com/meticulousCraftman/mongoose-os-x). 'x' stands for extended. Mongoose OS extended to support STM32F446RE.
- [coffee-bin-mqtt](https://github.com/vergissberlin/coffee-bin-mqtt). MQTT sensor project for coffee-bin.
- [mos_programs](https://github.com/nivu/mos_programs). Mongoose-OS.
- [mjs-array](https://github.com/Dietatko/mjs-array). Partial Array prototype polyfill for mJS engine.
- [mjs-polyfill](https://github.com/Asondo/mjs-polyfill). Mongoose os example project with standardization polyfill.
- [mongoose-os-action](https://github.com/dea82/mongoose-os-action). Github action with mongoose-os environment and mos tool.
- [arduino-ir](https://github.com/scotthernandez/arduino-ir). Mongoose-OS IR Library.
- [mgos-sgp30](https://github.com/wolfeidau/mgos-sgp30). A Sensirion's SGP30 Mongoose OS library.
- [Den_Trai_Tim](https://github.com/dentraitim/Den_Trai_Tim). Đèn Trái Tim (HeartLight).
- [common-tools](https://github.com/mamuesp-libs/common-tools).  A bunchs of tools and routines in C as well as in mJS always needed in every project..
- [mongoose-os-libs-ir](https://github.com/dvv/mongoose-os-libs-ir). IR library for Mongoose OS.
- [hc-sr04test](https://github.com/Tommystus/hc-sr04test). HC-SR04 Ultrasonic module test with Mongoose OS.
- [stm32f4_experimental_mgos_app](https://github.com/meticulousCraftman/stm32f4_experimental_mgos_app). Running Mongoose OS app on STM32F446RE platform..
- [Mongoose-OS-LIS3DH](https://github.com/gitcodr/Mongoose-OS-LIS3DH). Arduino Adafruit LIS3DH library for Mongoose OS.
- [arduino-adafruit-epd](https://github.com/mongoose-os-libs/arduino-adafruit-epd). Adafruit E-Paper / E-Ink Library for Mongoose OS.
- [qdbm](https://github.com/ztittle/qdbm). QDBM Library for Mongoose OS https://mongoose-os.com/.
- [mgos-sdcard-port](https://github.com/meticulousCraftman/mgos-sdcard-port). A port for ESP32 Arduino's SD.h and FS.h libraries to Mongoose OS..
- [mongoose-os-samples](https://github.com/douglaszuqueto/mongoose-os-samples). Exemplos de uso do Mongoose-os no ESP32.
- [homey](https://github.com/chris-zen/homey). My Smart Home hardware/firmware projects (2nd edition).
- [ESP32Firmware](https://github.com/nopesir/ESP32Firmware). Part of the Chrono-thermostat project for the course of "Project and laboratories on communication systems"..
- [led-matrix](https://github.com/ericogr/led-matrix). A MongooseOS ledMatrix implementation.
- [mongoose-ds3231](https://github.com/OllieDay/mongoose-ds3231). Mongoose OS I2C driver for the DS3231 real-time clock.
- [mongoose-ws2812b](https://github.com/OllieDay/mongoose-ws2812b). Mongoose OS driver for the WS2812B (aka NeoPixel) RGB LED strip.
- [MAX17263](https://github.com/Podnet/MAX17263). A mongoose OS library to talk to MAX17263..
- [mjs-testing](https://github.com/Dietatko/mjs-testing). mJS engine script testing framework.
- [esp-enum](https://github.com/Spiritdude/esp-enum). Enumerate ESP8266 and ESP32 according their MAC address and chip id.
- [hx711-mgos-test](https://github.com/Podnet/hx711-mgos-test). A mongoose OS app to test HX711 library ported from Arduino..
- [max17263-mgos-test](https://github.com/Podnet/max17263-mgos-test). Mongoose os app to test MAX17263 library ported from Arduino..
- [mjs-math](https://github.com/Dietatko/mjs-math). Partial Math object polyfill for mJS engine.
- [esp32_nextion_js_binary_clock](https://github.com/aschuma/esp32_nextion_js_binary_clock). A binary clock driven by an ESP32 microcontroller and a Nextion display, utilizing Mongoose OS and JavaScript technology.
- [rainnow-core](https://github.com/elzup/rainnow-core). rainnow api server.
- [mongoose-mlx90614](https://github.com/popstas/mongoose-mlx90614). MLX90614 (GY-906) sensor on Mongoose OS, publish to MQTT..
- [compteur-velib](https://github.com/licarth/compteur-velib). Compteur de velibs pour ESP8266.
- [mgos-combine-action](https://github.com/yaourdt/mgos-combine-action). Github Action to combine all parts of a Mongoose OS firmware ZIP-file into a single binary..
- [mongoose-button-switch](https://github.com/kriansa/mongoose-button-switch). A Mongoose OS project using MQTT to integrate with AWS IoT.
- [cloudhome-firmware](https://github.com/aghoneim92/cloudhome-firmware). Cloudhome is a (WIP) home automation system.
- [auth-post-c](https://github.com/manjrekarom/auth-post-c). A mongoose OS application that has three HTTP endpoints with digest access authentication..
- [nodemcu](https://github.com/felipeandres254/nodemcu). Base IoT framework fot NodeMCU.
- [To-Do-List](https://github.com/SakshiLajurkar/To-Do-List). A To-do list created over Node.js, Express.js and MongoDB Atlas..
- [robotcar](https://github.com/pmanna/robotcar). This app uses Mongoose OS to drive a small off-the-shelf, two-wheels car robot..
- [mgos-ltc68xx](https://github.com/Dietatko/mgos-ltc68xx). LTC68xx battery monitoring chip communication library for Mongoose OS.
- [audio-input-selector](https://github.com/spinningarrow/audio-input-selector). ESP32 audio input selector using Mongoose OS..
- [leilei](https://github.com/elzup/leilei). Room sensing and MQTT publish. with MongooseOS.
- [piCam](https://github.com/dbmarch/piCam). Raspberry Pi GCP IoT Device & ML execution.  .
- [mos-esp8266](https://github.com/nielswart/mos-esp8266). General sensor node based on Mongoose OS and ESP8266 hardware.
- [energymon-js](https://github.com/infrat/energymon-js). Energy monitor based on energy counter LED pulses.
- [mgos_libskeleton](https://github.com/kotelnikov/mgos_libskeleton). Mongoose OS Initial library skeleton.
- [swarmsense-mongoose-test](https://github.com/gopalkildoliya/swarmsense-mongoose-test). Example to integrate SwarmSense IoT Platform with Mongoose OS..
- [mgos-bme680](https://github.com/wolfeidau/mgos-bme680). A Bosch Sensortec's BME680 Mongoose OS library.
- [energymon-c](https://github.com/infrat/energymon-c). Energy monitor based on energy counter LED pulses.
- [mos-aws](https://github.com/bravokeyl/mos-aws). ESP8266 - AWS IoT - UART0 - Thing Shadow.
- [mgos-hlw8012](https://github.com/yaourdt/mgos-hlw8012). A Mongoose OS library for HLW8012 and BL0937 energy sensors..
- [mongoose-mqtt-ssd1306](https://github.com/popstas/mongoose-mqtt-ssd1306). MongooseOS: Display MQTT message on SSD1306.
- [mgos-environment-logger](https://github.com/anyhotcountry/mgos-environment-logger). Environment logger for Mongoose OS using BME280 sensor logging data to ThingSpeak..
- [ElectricityDisplay](https://github.com/anyhotcountry/ElectricityDisplay). Display for an electricity monitor publishing to an MQTT topic.
- [mgos-envsensors](https://github.com/wolfeidau/mgos-envsensors). Demonstrates the BME680 and SGP30 sensors delivering data to AWS IoT.
- [ds18b20-mgos-test](https://github.com/Podnet/ds18b20-mgos-test). Mongoose OS library for DS18B20 temperature sensor.
- [torrent](https://github.com/avishkarabhishek786/torrent). Torrent projects.
- [HX711](https://github.com/Podnet/HX711). A mongoose OS library for talking to HX711 (Arduino Port).
- [empty-mos-app](https://github.com/meticulousCraftman/empty-mos-app). An empty mongoose os app template repository.
- [mongoose-cron-app](https://github.com/sumancvb/mongoose-cron-app). This is cron job app for Mongoose OS.
- [pppos-mgos-test](https://github.com/Podnet/pppos-mgos-test). An application to test internet connectivity with GSM module using the PPPoS protocol.
- [websocket-mgos-test](https://github.com/Podnet/websocket-mgos-test). Mongoose OS WebSocket client application.
- [mcp2515-mgos-test](https://github.com/Podnet/mcp2515-mgos-test). Mongoose os app to test MCP2515 CAN library ported from Arduino..
- [mgos_relay](https://github.com/kotelnikov/mgos_relay). Mongoose OS Relay library.
- [uart-out-mgos-test](https://github.com/Podnet/uart-out-mgos-test). An MGOS app to periodically push data via UART interface.
