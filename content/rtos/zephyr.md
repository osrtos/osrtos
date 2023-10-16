---
title: Zephyr
slug: zephyr
version: v3.4.0
code-url: https://github.com/zephyrproject-rtos/zephyr
site-url: https://www.zephyrproject.org
draft: false
date: "2016-11-29 11:36:58"
last-updated: "2023-10-14"
star: 8503
components:
    - FileSystem
    - Network
    - HTTP
    - TLS/SSL
    - Shell
    - Logging
    - BLE
    - LoRaWAN
    - 6LoWPAN
    - USBHost
    - USBDevice
    - OTA
    - Modbus
    - CAN
libraries:
    - None
licenses:
    - Apache License
platforms:
    - ARM
    - x86
    - MIPS
    - Xtensa
    - RISC-V
    - QEMU
    - SPARC V8
---
The Zephyr™ Project is a scalable, real-time operating system (RTOS) supporting multiple hardware architectures, optimized for resource constrained devices, and built with security in mind. This Linux Foundation hosted project embraces open source development values and governance on its mission to unite leaders from across the industry to produce a best-in-breed solution.

<!--more-->

### Features

- Scalable from 8-bit to 64-bit microcontroller environments.
- Built with safety and security in mind.
- Supports a wide variety of development tools, including SDKs, debuggers, and more.
- Provides a unified API across architectures.
- Modular design that allows for configuring the OS for various use cases.
- Extensive suite of kernel services including threads, multi-threading, and more.

### **Components:**

- **Kernel:** Core component providing essential services.
- **OS Services:** Includes services like cryptography, debugging, device management, file systems, logging, power management, shell, storage, and more.
- **Connectivity:** Provides support for various communication protocols.
- **Hardware Support:** Extensive support for different boards and architectures.

### **Supported Platforms:**

- **ARC Boards:** DesignWare ARC series.
- **ARM Boards:** 96Boards series, Adafruit series, NXP series, and more.
- **ARM64 Boards:** Broadcom, ARM BASE, Intel Agilex, NXP i.MX series, and more.
- **MIPS Boards:** MIPS Malta Emulation.
- **Nios II Boards:** Altera MAX10, Altera Nios-II Emulation.
- **POSIX/Native Boards:** POSIX architecture, Bsim boards, Native POSIX execution.
- **RISC-V Boards:** Andes, ESP32-C3, GigaDevice, SiFive, and more.
- **SPARC Boards:** Generic LEON3, GR716-MINI Development Board.
- **x86 Boards:** Alder Lake N, Elkhart Lake CRB, Intel Integrated Sensor Hub, and more.
- **Xtensa Boards:** ESP32 series, Intel ADSP series, and more.

### Resources
<!--github-projects-->
- [awtk](https://github.com/zlgopen/awtk). AWTK = Toolkit AnyWhere(a cross-platform embedded GUI).
- [zmk](https://github.com/zmkfirmware/zmk). ZMK Firmware Repository.
- [ZSWatch](https://github.com/jakkra/ZSWatch). ZSWatch - the Open Source Zephyr™ based Smartwatch, including both HW and FW..
- [HeliOS](https://github.com/heliosproj/HeliOS). A community delivered, open source embedded operating system project..
- [zephyr-rtos-tutorial](https://github.com/maksimdrachov/zephyr-rtos-tutorial). Zephyr: Tutorial for beginners.
- [west](https://github.com/zephyrproject-rtos/west). West, Zephyr's meta-tool.
- [zephyr-doc](https://github.com/chunhuajiang/zephyr-doc). 《Zephyr OS 文档 - 中文版》.
- [zephyr-inside](https://github.com/chunhuajiang/zephyr-inside). 揭秘 Zephyr OS  .
- [sdk-ng](https://github.com/zephyrproject-rtos/sdk-ng). Zephyr SDK (Toolchains, Development Tools).
- [iot_security](https://github.com/iotwuxi/iot_security). 《密码技术与物联网安全——mbedtls开发实战》示例代码.
- [zscilib](https://github.com/zephyrproject-rtos/zscilib). An open-source scientific computing library for embedded systems running Zephyr OS or standalone..
- [awesome-zephyr-rtos](https://github.com/golioth/awesome-zephyr-rtos). 🪁 A curated list of awesome projects and resources for the Zephyr RTOS project..
- [control](https://github.com/swedishembedded/control). Embedded Firmware Control Systems Toolbox (Pure C and GNU Octave).
- [pinetime-hypnos](https://github.com/albsod/pinetime-hypnos). Zephyr firmware for the nRF52832 PineTime smartwatch.
- [lava](https://github.com/Linaro/lava). Read only mirror https://git.lavasoftware.org/lava/lava.
- [monocart-reporter](https://github.com/cenfun/monocart-reporter). A playwright test reporter (Node.js).
- [lispBM](https://github.com/svenssonjoel/lispBM). An interpreter for a concurrent lisp-like language with message-passing and pattern-matching implemented in C..
- [golioth-zephyr-sdk](https://github.com/golioth/golioth-zephyr-sdk). Golioth SDK For Zephyr.
- [mcumgr-android](https://github.com/JuulLabs-OSS/mcumgr-android). A mobile management library for devices running Apache Mynewt and Zephyr (DFU, logs, stats, config, etc.).
- [fwrisc](https://github.com/Featherweight-IP/fwrisc). Featherweight RISC-V implementation.
- [nrf-docker](https://github.com/NordicPlayground/nrf-docker). Dockerfile that contains all dependencies needed to build nRF Connect SDK applications..
- [Dynamic_App_Loading](https://github.com/rgujju/Dynamic_App_Loading). Dynamically load apps to zephyr RTOS.
- [zephyr-dwm1001](https://github.com/RT-LOC/zephyr-dwm1001). Open source DWM1001 + Zephyr example implementations.
- [mcumgr-ios](https://github.com/JuulLabs-OSS/mcumgr-ios). A mobile management library for devices running Apache Mynewt and Zephyr (DFU, logs, stats, config, etc.).
- [bms](https://github.com/scttnlsn/bms). Battery management system for 4-series li-ion packs.
- [zpp](https://github.com/lowlander/zpp). Zephyr C++ Framework.
- [openhaystack-zephyr](https://github.com/koenvervloesem/openhaystack-zephyr). Zephyr-based OpenHaystack firmware to track your personal Bluetooth devices via Apple's Find My network.
- [micro_ros_zephyr_module](https://github.com/micro-ROS/micro_ros_zephyr_module). micro-ROS Zephyr module and sample code.
- [sdk](https://github.com/swedishembedded/sdk). Embedded firmware development, simulation and verification SDK.
- [nrf52840-m2-devkit](https://github.com/makerdiary/nrf52840-m2-devkit). An open-source developer kit based on a removable nRF52840 M.2 module, designed for IoT prototyping.
- [tcf](https://github.com/intel/tcf). Documentation.
- [vscode-kconfig](https://github.com/trond-snekvik/vscode-kconfig). Kconfig language support in vscode.
- [Anjay-zephyr-client](https://github.com/AVSystem/Anjay-zephyr-client). Anjay Zephyr LwM2M client..
- [NCS-MIDI](https://github.com/BLE-MIDI/NCS-MIDI). MIDI tools for nRF Connect SDK.
- [bluetooth-low-energy-applications](https://github.com/koenvervloesem/bluetooth-low-energy-applications). Code examples, errata and additional tips and references to interesting projects for the book "Develop your own Bluetooth Low Energy Applications for Raspberry Pi, ESP32 and nRF52 with Python, Arduino and Zephyr".
- [zmk-docker](https://github.com/zmkfirmware/zmk-docker). Lightweight Docker images for ZMK.
- [playwright-zephyr](https://github.com/elaichenkov/playwright-zephyr). Zephyr reporter for the Playwright.
- [workstation](https://github.com/swedishembedded/workstation). Docker based development environment for coding, building and flashing embedded firmware..
- [zephyr-coaps-client](https://github.com/boaks/zephyr-coaps-client). CoAP / DTLS 1.2 CID client for Zephyr - Reliable - Efficient - Encrypted.
- [herald-for-cpp](https://github.com/theheraldproject/herald-for-cpp). Herald for C++ - Reliable mobile Bluetooth communications - Native library & test apps.
- [awesome-zephyr-rtos](https://github.com/Technoculture/awesome-zephyr-rtos). Zephyr RTOS for building modular firmware.
- [cozy](https://github.com/lindemer/cozy). CBOR Object Signing and Encryption (COSE) for Zephyr RTOS.
- [pinetime](https://github.com/ck-telecom/pinetime). zephyr based PineTime smartwatch.
- [ruuvitag_fw_zephyr](https://github.com/a-smiggle/ruuvitag_fw_zephyr). Ruuvitag FW using Zephyr OS.
- [zephyr](https://github.com/illinois/zephyr). A unified grading platform for student code.
- [zephyr](https://github.com/CharlyCst/zephyr). A Programming Language built for WebAssembly.
- [zephyr-stm32-webusb](https://github.com/dimka-rs/zephyr-stm32-webusb). Playing with Zephyr Web USB example on STM32 Bluepill.
- [send-my-sensor](https://github.com/koenvervloesem/send-my-sensor). Zephyr-based firmware to upload sensor data via Apple's Find My network.
- [zephyr_cve-2021-3625](https://github.com/szymonh/zephyr_cve-2021-3625). CVE-2021-3625 - Sample exploits for Zephyr.
- [platform-nxpimxrt](https://github.com/platformio/platform-nxpimxrt). NXP i.MX RT: development platform for PlatformIO.
- [aW_1-keyboard](https://github.com/winnedatsch/aW_1-keyboard). A split (semi-)wireless keyboard based on the NRF52832.
- [zephyrWithCucumber](https://github.com/vkirankumar3090/zephyrWithCucumber). This Framework will help you to update the Test Cycle Status and Steps of the Test Case which is executed in the Test Cycle with the help of cucumber json file.
- [teensy4_shell](https://github.com/ufechner7/teensy4_shell). Tutorial on how to use the shell of Zephyr with Teensy 4.0.
- [zephyr-docker](https://github.com/beriberikix/zephyr-docker). Develop with Zephyr locally using Docker containers.
- [zephyr-grbl](https://github.com/iwasz/zephyr-grbl). Started as a firmware for https://hackaday.io/project/177237-corexy-pen-plotter, possibly could be adapted to other CNCs as well..
- [Zephyr_WiFi](https://github.com/craigpeacock/Zephyr_WiFi). Example Zephyr WiFi code.
- [bridle](https://github.com/tiacsys/bridle). Bridle and kite line for embedded systems based on Zephyr..
- [ly10-zephyr-fw](https://github.com/bcdevices/ly10-zephyr-fw). Zephyr-based firmware for PLT Demo V2.
- [mcumgr-dart](https://github.com/jkdhn/mcumgr-dart). Dart mcumgr client.
- [JiphyLib](https://github.com/jezztify/JiphyLib). making it easier to publish robotframework results to JIRA.
- [Zephyr_LoRaWAN](https://github.com/craigpeacock/Zephyr_LoRaWAN). An example LoRaWAN Application on the Zephyr RTOS.
- [Anjay-zephyr](https://github.com/AVSystem/Anjay-zephyr). Anjay LwM2M library module for Zephyr..
- [Kconfig-Highlighter](https://github.com/fallrisk/Kconfig-Highlighter). Sublime Text 3 highlight script for the Kconfig language..
- [vscode-zephyr](https://github.com/codingspirit/vscode-zephyr). This is an example vscode setting to provide supports for zephyr based projects build/debug..
- [zLorawan_Node](https://github.com/fcgdam/zLorawan_Node). A Zephyr RTOS based Lorawan node..
- [mender-stm32l4a6-zephyr-example](https://github.com/joelguittet/mender-stm32l4a6-zephyr-example). Mender MCU example running on STM32L4 using Zephyr RTOS.
- [bazel2zephyr](https://github.com/GatCode/bazel2zephyr). Hands-on tutorial on building a static library (.a) with Bazel and linking it into a Zephyr based project..
- [twatch](https://github.com/ck-telecom/twatch). Zephyr based firmware for ligo twatch.
- [stm32_blackpill_zephyr_ssd1306_demo](https://github.com/oldrev/stm32_blackpill_zephyr_ssd1306_demo). A demo for Zephyr RTOS to shows how to using a custom TTF Font with CFB sub-system to prints text on a small OLED screen..
- [patient_monitoring](https://github.com/96boards-projects/patient_monitoring). Patient Monitoring System using 96Boards.
- [pyrinas-zephyr](https://github.com/pyrinas-iot/pyrinas-zephyr). Open companion cloud client to Pyrinas Server for the nRF9160 Feather and Zephyr.
- [Netflix-clone](https://github.com/ravindrakumarkumawat/Netflix-clone). This the clone of Netflix functionalities using YouTube Data API. Where you can watch videos, search videos (Not Channel). You can view the preview screen. Every Video has a recommended video list. Sign in with Google..
- [Bluetooth-Mesh-Sensor-Network](https://github.com/lucamoroz/Bluetooth-Mesh-Sensor-Network). Bluetooth Mesh sensor network.
- [nrf_servo](https://github.com/inductivekickback/nrf_servo). Servo implementation that uses the NRFX PWM driver.
- [Lemon-IoT-Accessories](https://github.com/aaron-mohtar-co/Lemon-IoT-Accessories). Support files for Lemon IoT Ecosystem Accessories.
- [Lemon-IoT-LTE-nRF9160](https://github.com/aaron-mohtar-co/Lemon-IoT-LTE-nRF9160). Support files for the Lemon IoT LTE nRF9160 Board.
- [zmk-config-split-template](https://github.com/zmkfirmware/zmk-config-split-template). A template used to generate user configuration repos for split (left + right) keyboards.
- [ZAPI](https://github.com/chaitanya8/ZAPI). Test execution and result reporting on Jira + Zephyr setup.
- [MG100_firmware](https://github.com/LairdCP/MG100_firmware). MG100 Zephyr RTOS based firmware.
- [Pinnacle-100-Firmware-Manifest](https://github.com/LairdCP/Pinnacle-100-Firmware-Manifest). Manifest repository for Pinnacle 100 and MG100 BLE Gateway Firmware demos: https://github.com/LairdCP/BLE_Gateway_Firmware.
- [hc-sr04](https://github.com/inductivekickback/hc-sr04). Zephyr RTOS driver for HC-SR04 Ultrasonic Ranging Module.
- [alturia-firmware](https://github.com/rckTom/alturia-firmware). Firmware for the alturia flight computer.
- [zephyr-stm32-spi](https://github.com/ideak/zephyr-stm32-spi). Simple example of using SPI on the STM32 Nucleo-F411RE board.
- [kw1281-diag](https://github.com/jonnykl/kw1281-diag). Simple KW1281 diagnosis tool using Zephyr shell.
- [nrf-connect-sdk-build-docker](https://github.com/hardwario/nrf-connect-sdk-build-docker). Build Environment for nRF Connect SDK.
- [zephyr-data-migrator](https://github.com/gaurav1264/zephyr-data-migrator). This is self-service utility to migrate zephyr for Jira data from one instance to another..
- [zephyr-usb-midi](https://github.com/stuffmatic/zephyr-usb-midi). A configurable USB MIDI 1.0 device class driver for the Zephyr RTOS..
- [AffectHub](https://github.com/williamcaruso/AffectHub). A multimodal physiological and affective data hub affectivecomputing.
- [sdk-hsm-thingy53](https://github.com/HomeSmartMesh/sdk-hsm-thingy53). Zephyr Samples for Nordic Thingy53 dev kit OpenThread mesh with json data, BME688 BSEC2 for Air Quality, Light color, RGB Les, Battery.
- [bpm](https://github.com/HeartfeltBP/bpm). Firmware for the Heartfelt Cardiac Monitor. Consists of sensor (MAX86150) driver, WiFi and Bluetooth connectivity, and client authentication..
- [zephyr-demo-wifi](https://github.com/jptcarreira/zephyr-demo-wifi). Zephyr Demo Wifi and TCP/UDP connection console using STM32L4+ B-L4S5I-IOT01A.
- [Pinnacle_100_OOB_Demo_Manifest](https://github.com/LairdCP/Pinnacle_100_OOB_Demo_Manifest). Manifest repo for the Pinnacle 100 Out of Box Demo.
- [hello-zephyr](https://github.com/nrjn/hello-zephyr). playing around with zephyr .
