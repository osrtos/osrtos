---
title: FreeRTOS
slug: freertos
version: "202411.00"
code-url: https://github.com/FreeRTOS/FreeRTOS
site-url: http://www.freertos.org/
date: "2016-11-29 11:36:57"
last-updated: "2025-04-21"
star: 5918
components:
    - scheduler
    - task-management
    - inter-task-communication
    - memory-management
    - timer-management
    - network-stack
    - mqtt-client
    - http-client
    - tls-ssl
    - ota-update
    - logging
    - runtime-analysis
    - smp-support
licenses:
    - MIT
platforms:
    - arm-cortex-m
    - arm-cortex-a
    - arm-cortex-r
    - risc-v
    - xtensa
    - x86
    - mips
    - powerpc
    - avr
    - pic
    - "8051"
    - msp430
    - posix
    - qemu
---
FreeRTOS is a market-leading real-time operating system (RTOS) for microcontrollers and small microprocessors. Distributed freely under the MIT open source license, it includes a kernel and a growing set of libraries suitable for use across industry sectors and applications. Amazon Web Services (AWS) took stewardship of the FreeRTOS kernel in 2016, ensuring its continued development and support. FreeRTOS is built with an emphasis on reliability, ease of use, and includes numerous libraries for connectivity, security, and over-the-air (OTA) updates, making it a popular choice for IoT and embedded systems development.

<!--more-->

Originally developed by Richard Barry around 2003, FreeRTOS has become a de facto standard in the embedded industry. Since AWS took stewardship, FreeRTOS development continues openly on GitHub, with contributions from a large community and AWS engineers. It remains hardware, development tool, and cloud-neutral.

The FreeRTOS kernel provides core RTOS functionality including task scheduling (pre-emptive, co-operative, time-sliced), inter-task communication (queues, semaphores, mutexes, event groups, task notifications), timer management, and memory management (with multiple heap implementations). It supports a vast number of microcontroller architectures.

Beyond the kernel, the FreeRTOS ecosystem includes libraries such as FreeRTOS+TCP (a lightweight TCP/IP stack), coreMQTT, coreHTTP, corePKCS11, and integrations with security libraries like Mbed TLS and wolfSSL. AWS provides libraries for seamless integration with AWS IoT services, covering OTA updates, Device Shadow, Device Defender, and more. FreeRTOS also supports Symmetric Multiprocessing (SMP) on multi-core processors.

The project emphasizes quality control, robustness, and long-term support (LTS) releases. Commercial licensing and support options are available through strategic partners like WITTENSTEIN high integrity systems (OpenRTOS/SafeRTOS) for users requiring additional guarantees or indemnification.

## Features

-   **Choice of Scheduling Algorithms:** Supports pre-emptive, co-operative, and optional time-slicing configurations.
-   **Flexible Task Management:** Includes creation, deletion, priority assignment, and state management (Ready, Running, Blocked, Suspended).
-   **Rich Inter-Task Communication (ITC):** Provides Queues, Binary Semaphores, Counting Semaphores, Mutexes (with Priority Inheritance), Recursive Mutexes, Event Groups, Stream Buffers, and Message Buffers.
-   **Direct-to-Task Notifications:** Offers a lightweight and fast alternative for ITC and synchronization.
-   **Software Timers:** Supports one-shot and auto-reload software timers managed by a dedicated timer service task.
-   **Flexible Memory Management:** Offers both static and dynamic memory allocation options, including five sample heap implementations (heap_1 to heap_5).
-   **Interrupt Management:** Provides interrupt-safe API functions, deferred interrupt processing mechanisms, and support for interrupt nesting on capable ports.
-   **Symmetric Multiprocessing (SMP) Support:** Enables scheduling tasks across multiple identical processor cores.
-   **Resource Management:** Includes features like critical sections, scheduler suspension (locking), and support for the Gatekeeper task pattern to manage shared resources.
-   **Low Power Support:** Features include the Idle task hook for custom power saving and a tickless idle mode to stop the tick interrupt during idle periods.
-   **Stack Overflow Detection:** Offers multiple mechanisms to detect task stack overflows during runtime.
-   **Optional MPU Support:** Provides support for Memory Protection Units on certain architectures to enhance application safety and robustness.
-   **Runtime Analysis and Tracing:** Includes hooks for tracing kernel events and gathering task run-time statistics.
-   **Thread Local Storage:** Supports standard C library reentrancy (newlib, picolibc) and application-specific thread local storage pointers.
-   **Extensive Platform Support:** Officially supports over 40 microcontroller architectures and multiple compilers.

## Components

The FreeRTOS distribution includes the kernel and various supplementary libraries:

-   **FreeRTOS Kernel:** The core real-time scheduler and task management component.
-   **Inter-Task Communication:** Queues, Semaphores (Binary, Counting, Mutex, Recursive), Event Groups, Task Notifications, Stream Buffers, Message Buffers.
-   **Memory Management:** Various heap implementations (heap_1 through heap_5).
-   **Software Timers:** Kernel-managed software timers.
-   **FreeRTOS+TCP:** A lightweight, embedded TCP/IP stack (IPv4 and IPv6).
-   **coreMQTT:** Client implementation for the MQTT 3.1.1 specification.
-   **coreHTTP:** Client implementation for HTTP/1.1.
-   **coreJSON:** Parser for JSON documents.
-   **corePKCS11:** API for cryptographic objects based on the PKCS#11 standard.
-   **AWS IoT Libraries:** Components for Over-the-air Updates (OTA), Device Shadow, Jobs, Device Defender, Fleet Provisioning.
-   **Security:** Integrations with Mbed TLS and wolfSSL for TLS/SSL functionality.
-   **Other Utilities:** Backoff Algorithm, coreSNTP, SigV4 client, Logging.
-   **Cellular Interface:** Library for interfacing with cellular modems.

## Resources

- [FreeRTOS Ported to Raspberry Pi](https://github.com/jameswalmsley/RaspberryPi-FreeRTOS). This project provides a very basic port of FreeRTOS to Raspberry pi. It includes a demo application that use 2 FreeRTOS tasks to flash the LED on and off.
- [DuinOS](https://code.google.com/p/duinos/). DuinOS is a small multithreading real time operating system (RTOS), based on the FreeRTOS kernel, for Arduino compatible boards.It's installed as an Arduino core, and currently supports the following AVR processors:
- [LPC43XX-FreeRTOS-with-2xLED-Threads](https://github.com/Protoneer/LPC43XX-FreeRTOS-with-2xLED-Threads). This is example code of using a NXP LPC4337 Xplorer board from NGX with FreeRTOS.It has two LED blinking tasks running at the same time.
- [FreeRTOS on XMEGA](https://github.com/yuriykulikov/FreeRTOS-on-XMEGA). port.c and portmacro.h for FreeRTOS to run on any AVR XMEGA
- [FreeRTOS on STM32](http://www.scienceprog.com/freertos-on-stm32/). FreeRTOS demos for STM32F103ZET6 board that include LEDs, Buttons, USART, and LCD.
- [FreeRTOS on AVR with external RAM](http://www.scienceprog.com/freertos-on-avr-with-external-ram/). This project add extra RAM connected to the external memory interface of Atmega128.
- [LPC4300 Development Boards with FreeRTOS demo](http://www.lpc4350.com/). LPC4350 Dual-Core Cortex-M4 and Cortex-M0 Development BoardLPC4350 is the first asymmetrical dual-core digital signal controller with ARM Cortex-M4 and Cortex-M0 processors. The LPC-4350-DB1 development board consists of the most essential components that you need to start your development.It contains the LPC4350FET256 dual-core controller, USB, Ethernet and JTAG connectors, 4 push buttons + 4 LEDs, 16MB external NOR flash.
- [Porting FreeRTOS to MikroC for STM32 M3](http://www.libstock.com/projects/view/370/porting-freertos-to-mikroc-for-stm32-m3). This project port FreeRTOSV7.1.1 to CORTEX STM32F107 MikroC Version 2.5.
- [Using FreeRTOS kernel in AVR projects](http://www.scienceprog.com/using-freertos-kernel-in-avr-projects/). Instructions to run FreeRTOS on AVR Atmega128L, using AVRStudio5.
- [Running multiple FreeRTOS tasks on AVR](http://www.scienceprog.com/running-multiple-freertos-tasks-on-avr/). Let us go further with our example code and add more tasks to our FreeRTOS engine. We already have LED flashing task that toggles LED every second. Additionally we are going to create another task that checks button state. Also we are going to send some information to LCD. As always lets take care of drivers for all of them.
- [Running FreeRTOS on the Keil MCBSTM32 Board with the RVMDK Evaluation Tools](http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dai0210A/index.html). This application note describes how to modify an existing port demo of the FreeRTOS operating system that targets the Luminary Micro LM3S102 evaluation board. It uses Keil
- [uc3l0 freertos demo](http://www.avrfreaks.net/index.php?module=Freaks%20Academy&func=viewItem&item_id=3450&item_type=project). Demos for FreeRTOS and the UC3L0. This demo provides: Full USART Command TerminalConfigurable ADC TaskPWM control over RGB LEDs (on the L0 Xplained)Printable Data from various sources.
- [gsm control system](http://www.avrfreaks.net/projects/gsm-control-system-freertos?module=Freaks%20Academy&func=viewItem&item_id=3672&item_type=project). G.S.A. (GSM System Automation) is a control system that allows you to manage your domestic appliances by means of gsm-communication.You can program GSA simply by send a SMS.
- [STM32F4 – Deploy FreeRTOS Embedded OS in under 10 seconds!](https://istarc.wordpress.com/2014/07/10/stm32f4-deploy-freertos-in-under-10-seconds/). This tutorial describe how to build and deploy the FreeRTOS embedded operating system on STM32F4 Discovery board under 10 seconds.
- [ST ARM Cortex-M7 STM32 F7 RTOS Demo](http://www.freertos.org/ST_STM32F7_Cortex-M7_RTOS_Demo.html). This page provides documentation for the FreeRTOS demo that targets the STM32756G-EVAL Evaluation Kit, which incorporates an STM32F7 ARM Cortex-M7 microcontroller from STMicroelectronics. Pre-configured build projects are provided for both the IAR and ARM Keil tools.
- [Creating a FreeRTOS-based WiFi HTTP server for ESP8266](https://visualgdb.com/tutorials/esp8266/relay/). This tutorial shows how to create a FreeRTOS-based HTTP server with the ESP8266 chip.
- [esp-open-rtos](https://github.com/SuperHouse/esp-open-rtos). A community developed open source FreeRTOS-based framework for ESP8266 WiFi-enabled microcontrollers. Intended for use in both commercial and open source projects.
<!--github-projects-->
- [libwebsockets](https://github.com/warmcat/libwebsockets). canonical libwebsockets.org networking library.
- [InfiniTime](https://github.com/InfiniTimeOrg/InfiniTime). Firmware for Pinetime smartwatch written in C++ and based on FreeRTOS.
- [arduino-pico](https://github.com/earlephilhower/arduino-pico). Raspberry Pi Pico Arduino core, for all RP2040 boards.
- [Avem](https://github.com/avem-labs/Avem). 🚁 轻量级无人机飞控-[Drone]-[STM32]-[PID]-[BLDC].
- [Lua-RTOS-ESP32](https://github.com/whitecatboard/Lua-RTOS-ESP32). Lua RTOS for ESP32.
- [Arduino_FreeRTOS_Library](https://github.com/feilipu/Arduino_FreeRTOS_Library). A FreeRTOS Library for all Arduino AVR Devices (Uno, Leonardo, Mega, etc).
- [MuditaOS](https://github.com/mudita/MuditaOS). Mobile operating system based on FreeRTOS™ optimized for E Ink displays - developed for Mudita Pure minimalist phone.
- [luos_engine](https://github.com/Luos-io/luos_engine). Open-source and real-time orchestrator for cyber-physical-systems, to easily design, test and deploy embedded applications and digital twins..
- [freertos-addons](https://github.com/michaelbecker/freertos-addons). Additions to FreeRTOS.
- [Modbus-STM32-HAL-FreeRTOS](https://github.com/alejoseb/Modbus-STM32-HAL-FreeRTOS). Modbus TCP and  RTU,  Master and Slave for STM32 using Cube HAL and FreeRTOS.
- [FreeRTOS-rust](https://github.com/lobaro/FreeRTOS-rust). Rust crate for FreeRTOS.
- [freertos.rs](https://github.com/hashmismatch/freertos.rs). A Rust wrapper for FreeRTOS..
- [kendryte-freertos-sdk](https://github.com/kendryte/kendryte-freertos-sdk). This project is no longer maintained Not recommended for product development..
- [esp32-cam-mjpeg-multiclient](https://github.com/arkhipenko/esp32-cam-mjpeg-multiclient). ESP32 MJPEG Multiclient Streaming Server.
- [hongbomiao.com](https://github.com/hongbo-miao/hongbomiao.com). A personal research and development (R&D) lab that facilitates the sharing of knowledge..
- [blinker-doc](https://github.com/blinker-iot/blinker-doc). blinker中文文档.
- [SmartSpeaker](https://github.com/lovelyterry/SmartSpeaker). 一个基于云端语音识别的智能控制设备，类似于天猫精灵，小爱同学。采用的芯片为stm32f407,wm8978,esp8266。.
- [nesper](https://github.com/elcritch/nesper). Program the ESP32 with Nim! Wrappers around ESP-IDF API's. .
- [ESP32-freeRTOS](https://github.com/DiegoPaezA/ESP32-freeRTOS). Basic Examples of FreeRTOS with ESP32 and ESP-IDF.
- [FastLED-idf](https://github.com/bbulkow/FastLED-idf). FastLED port to the ESP-IDF 4.0 development environment.
- [stm32_framework](https://github.com/Staok/stm32_framework). 一个志在实现STM32F1、F2和F4工程模板的项目，集成了FreeRTOS、LWIP、FATFS、DSP、USB、IAP、菜单库、有限状态机模板等等的组件，以及未来将加入的加密、BPNN、最小二乘、音频图片视频解码、LittlevGL等诸多常用的算法或组件，并具有良好的易用性、解耦性和可剪裁性！.
- [esp32-mjpeg-multiclient-espcam-drivers](https://github.com/arkhipenko/esp32-mjpeg-multiclient-espcam-drivers). ESP32 MJPEG Multiclient Streaming Server with latest Espressif drivers.
- [ot-rtos](https://github.com/openthread/ot-rtos). OpenThread RTOS, an integration of OpenThread, LwIP, and FreeRTOS..
- [ds18b20](https://github.com/nimaltd/ds18b20). ds18b20 library for stm32 hal.
- [XR871-OLD](https://github.com/XradioTech/XR871-OLD). XR871 SDK.
- [reliance-edge](https://github.com/tuxera/reliance-edge). Transactional power-failsafe filesystem for microcontrollers.
- [nuclei-sdk](https://github.com/Nuclei-Software/nuclei-sdk).   Nuclei RISC-V Software Development Kit.
- [OV-Watch](https://github.com/No-Chicken/OV-Watch). A powerful Smart Watch. Only cost ￥80 RMB ( $12 USD )..
- [esp-wifi-logger](https://github.com/VedantParanjape/esp-wifi-logger). ESP32 WiFi Logger component.
- [XC-OS](https://github.com/FASTSHIFT/XC-OS). Open source graphics operating system for microcontroller.
- [multizone-sdk](https://github.com/hex-five/multizone-sdk). MultiZone® Security TEE is the quick and safe way to add security and separation to any RISC-V processors. The RISC-V standard ISA doesn't define TrustZone-like primitives to provide hardware separation. To shield critical functionality from untrusted third-party components, MultiZone provides hardware-enforced, software-defined separation of multiple equally secure worlds. Unlike antiquated hypervisor-like solutions, MultiZone is self-contained, presents an extremely small attack surface, and it is policy driven, meaning that no coding is required – and in fact even allowed. MultiZone works with any 32-bit or 64-bit RISC-V processors with standard Physical Memory Protection unit (PMP) and “U” mode..
- [FreeRTOS-RISCV](https://github.com/illustris/FreeRTOS-RISCV). A port of FreeRTOS for the RISC-V ISA.
- [freertos-teensy](https://github.com/tsandmann/freertos-teensy). FreeRTOS port with C++ std::thread support for ARM boards Teensy 3.5, 3.6, 4.0 and 4.1 (cortex-m4f and cortex-m7f).
- [STM32_Base_Project](https://github.com/rgujju/STM32_Base_Project). STM32 Base project with a lot of stuff.
- [RP2040-FreeRTOS](https://github.com/smittytone/RP2040-FreeRTOS). Raspberry Pi RP2040 FreeRTOS baseline development project.
- [smart-home-automation-rtos](https://github.com/parikshitpagare/smart-home-automation-rtos). A complete home automation system developed on ESP32 microcontroller using freeRTOS. The system is controlled wirelessly via Bluetooth with an android app developed using MIT App Inventor..
- [unabto](https://github.com/nabto/unabto). uNabto SDK - direct P2P connectivity for embedded devices (and more).
- [FreeRTOS-Emulator](https://github.com/alxhoff/FreeRTOS-Emulator). POSIX based FreeRTOS emulator with SDL2 graphics interface and multiple async communications interfaces, aiming to make it possible to teach FreeRTOS without embedded hardware using similar processes.
- [ArduRTOS](https://github.com/Dentrax/ArduRTOS). Real Time Operating System Lessons using Arduino and The FreeRTOS Kernel.
- [pubsub-c](https://github.com/jaracil/pubsub-c). Pub/Sub library for C.
- [EmbeddedMqttBroker](https://github.com/alexCajas/EmbeddedMqttBroker). This is a Mqtt broker for embedded devices, developed in C++, FreeRTOS, arduino core and tested in an Esp32. .
- [freertos-cell](https://github.com/siemens/freertos-cell). FreeRTOS for Jailhouse Cells.
- [mTower](https://github.com/Samsung/mTower). mTower is Trusted Execution Environment specially designed to be used on MicroController Units (MCUs) supporting ARM TrustZone technology (e.g., Cortex-M23/33/35p). mTower operates well under restrictions typical for such environment – small RAM and ROM sizes, relatively low performance, absence of rich OSes providing variety of services available on PCs or in enterprise environments. mTower is intended for usage in IoT, embedded devices, Smart Home applications, distributed heterogeneous networks and other environments where secure processing of sensitive data is necessary..
- [hsmcpp](https://github.com/igor-krechetov/hsmcpp). C++ based Hierarchical / Finite State Machine library oriented for embedded and RTOS systems..
- [STM32_HTTPs_WolfSSL](https://github.com/PeterH0323/STM32_HTTPs_WolfSSL). STM32 HTTPs demo , using lib : WolfSSL, Lwip, FreeRTOS, LAN8720.
- [stm32f10x_makefile_freertos](https://github.com/freelamb/stm32f10x_makefile_freertos). stm32f10x gcc makefile freertos.
- [SUCHAI-Flight-Software](https://github.com/spel-uchile/SUCHAI-Flight-Software). THIS REPOSITORY HAS BEEN MOVED TO GITLAB.
- [FreeVario](https://github.com/FreeVario/FreeVario). FreeVario for paragliders.
- [pid-stm32f746](https://github.com/JON95Git/pid-stm32f746). Embedded graphical interface for PID control.
- [Seeed_Arduino_FreeRTOS](https://github.com/Seeed-Studio/Seeed_Arduino_FreeRTOS). This library gives an example of how to get FreeRTOS running on Seeed production. The project can be used as a template to build your projects off of as well..
- [FreeRTOS-Cpp](https://github.com/jonenz/FreeRTOS-Cpp). C++17 header-only interface to the FreeRTOS kernel API..
- [openMMC](https://github.com/lnls-dig/openMMC). Open source firmware for MMC controllers.
- [rtos-wot](https://github.com/jollen/rtos-wot). Open source FreeRTOS SDK for ESP8266 WiFi Module.
- [coreMQTT-Agent-Demos](https://github.com/FreeRTOS/coreMQTT-Agent-Demos). Demonstrates use of coreMQTT-Agent for simple MQTT connection sharing among different threads of execution. .
- [TM4C129_FreeRTOS_Demo](https://github.com/akobyl/TM4C129_FreeRTOS_Demo). Demo of FreeRTOS 10.2.1 for the Tiva TM4C1294 Connected Launchpad from Texas Instruments.
- [esp32-i2c-mpu6050](https://github.com/imxieyi/esp32-i2c-mpu6050). ESP32 I2C MPU6050 driver for esp-idf.
- [aimbots-dev](https://github.com/TAMU-Robomasters/aimbots-dev). The Taproot-based rewrite of our 2021 development platform..
- [STM32H745_Ethernet](https://github.com/AnielShri/STM32H745_Ethernet). Ethernet on STM32H745 using FreeRTOS and LWIP.
- [freertos-mcpp](https://github.com/IntergatedCircuits/freertos-mcpp). Wrapping FreeRTOS in modern C++ classes.
- [uas-catpilot](https://github.com/ctlst-tech/uas-catpilot). CatPilot is a hardware and OS agnostic drone's autopilot software stack. It is designed for faster creation of scalable distributed control systems for mission-critical applications. (UAS-CatPilot repo is a upper lever repo for sharing configurations for UAVs).
- [ZYNQ_ADC_DMA_LWIP](https://github.com/Hamid-R-Tanhaei/ZYNQ_ADC_DMA_LWIP). Interfacing ZYNQ SoC device with ADC, Transferring data through DMA and LwIP.
- [pico-freertos-sample](https://github.com/yunkya2/pico-freertos-sample). Raspberry Pi Pico Sample application with FreeRTOS.
- [ESP8266-RTOS-HomeKit](https://github.com/luigifcruz/ESP8266-RTOS-HomeKit). ESP8266 HomeKit Accessory Implementation based on FreeRTOS..
- [air32f103-template](https://github.com/IOsetting/air32f103-template). AIR32F103 template project for GNU Arm Embedded Toolchain.
- [IPv6-ESP8266](https://github.com/IPv6-ESP8266/IPv6-ESP8266). examples for setting up ipv6 on the esp8266.
- [LPTIM-Tick](https://github.com/jefftenney/LPTIM-Tick). FreeRTOS Tick/Tickless via LPTIM.
- [golioth-firmware-sdk](https://github.com/golioth/golioth-firmware-sdk). Golioth Firmware SDK.
- [micro_ros_stm32_template](https://github.com/husarion/micro_ros_stm32_template). Boilerplate to create a project with:  STM32 + Ethernet + micro-ROS + FreeRTOS + Arduino + PlatformIO.
- [Cicada-FW](https://github.com/EnAccess/Cicada-FW). IoT Communications Module for Energy Access. An easy way to get production ready, bi-directional communications for your IoT embedded device. Proiect supported by the EnAccess Foundation - https://enaccess.org.
- [frt](https://github.com/Floessie/frt). Lightweight, easy-to-use wrapper around the Arduino_FreeRTOS_Library.
- [STM32F407VG-freeRTOS-FATFS-SDIO-SD-CARD](https://github.com/avaan/STM32F407VG-freeRTOS-FATFS-SDIO-SD-CARD). STM32F407VG+freeRTOS+FATFS+SDIO+SD CARD example.
- [FreeRTOS-Wrapper](https://github.com/RT-Thread-packages/FreeRTOS-Wrapper). RT-Thread操作系统的FreeRTOS兼容层 | FreeRTOS Application Compatibility Layer (ACL) for RT-Thread.
- [platformio-libopencm3-freertos](https://github.com/bjwschaap/platformio-libopencm3-freertos). Sample blinky project for PlatformIO using libopencm3 and FreeRTOS.
- [obdh](https://github.com/floripasat/obdh). On-Board Data Handling Module.
- [coreMQTT-Agent](https://github.com/FreeRTOS/coreMQTT-Agent). Implements an MQTT agent (or daemon) task for simple MQTT connection sharing among different threads of execution..
- [CorePartition](https://github.com/solariun/CorePartition). Universal Cooperative Multithread Lib with real time Scheduler that was designed to work, virtually, into any modern micro controller or Microchip and, also, for user space applications for modern OS  (Mac, Linux, Windows) or on FreeRTOS as well. Supports C and C++ .
- [obdh2](https://github.com/spacelab-ufsc/obdh2). On-Board Data Handling Module 2.
- [multizone-iot-sdk](https://github.com/hex-five/multizone-iot-sdk). MultiZone® Trusted Firmware is the quick and safe way to build secure IoT applications with any RISC-V processor. It provides secure access to commercial and private IoT clouds, real-time monitoring, secure boot, and remote firmware updates. The built-in Trusted Execution Environment provides hardware-enforced separation ... .
- [FreeRTOS-HIFI4-DSP](https://github.com/YuzukiHD/FreeRTOS-HIFI4-DSP). FreeRTOS for Cadence Tensilica HIFI 4 DSP on R329, D1-H, T113 With GCC Compiler.
- [Prust](https://github.com/visionspacetec/Prust). PUS-C on Rust. This is the entry point for the Prust tools. List of the tools and a Wiki for them..
- [dscKeybusInterface-RTOS](https://github.com/taligentx/dscKeybusInterface-RTOS). An esp-open-rtos library to directly interface with DSC security systems, including native HomeKit support..
- [development-of-real-time-systems](https://github.com/ragu-manjegowda/development-of-real-time-systems). Coursera Development of Real-Time Systems Course Assignments.
- [freertos-mqttclient](https://github.com/jiejieTop/freertos-mqttclient). a demo of mqttclient on freertos platform，https://github.com/jiejieTop/mqttclient.
- [murasaki](https://github.com/suikan4github/murasaki). STM32 HAL class library.
- [drone_stm32](https://github.com/EmbeddedArea/drone_stm32). An Open Source Hobby Drone project with STM32F103C8T6 (BluePill).
- [FreeRTOS-raspi3](https://github.com/eggman/FreeRTOS-raspi3). FreeRTOS port Raspberry Pi 3 ( 64bit /  aarch64 ).
- [selfie-archive-cc-iarrc2018](https://github.com/KNR-Selfie/selfie-archive-cc-iarrc2018). Software for 1:10 scale autonomous cars.
- [supla-device](https://github.com/SUPLA/supla-device). Create your own Supla device! This software can be used as a library for Arduino IDE, or can be used directly with ESP8266 RTOS SDK and with ESP IDF. It is also possible to compile and run it on Linux and in FreeRTOS..
- [open-authenticator-app](https://github.com/Open-Authenticator/open-authenticator-app). Firmware for Open Authenticator.
- [catpilot](https://github.com/ctlst-tech/catpilot). CatPilot is a hardware and OS agnostic drone's autopilot software stack. It is designed for faster creation of scalable distributed control systems for mission-critical applications..
- [FreeRTOS_RH850](https://github.com/mikisama/FreeRTOS_RH850). FreeRTOS port for Renesas RH850.
- [ESP32-Repo](https://github.com/coder137/ESP32-Repo). ESP-IDF with ESP32.
- [lorawan_freertos_esp32](https://github.com/phfbertoleti/lorawan_freertos_esp32). Projeto open-source de end-device LoRaWAN com ESP32, sensor BMP180 e FreeRTOS.
