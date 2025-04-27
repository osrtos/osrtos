---
title: Zephyr
slug: zephyr
version: v4.1.0
code-url: https://github.com/zephyrproject-rtos/zephyr
site-url: https://www.zephyrproject.org
date: "2016-11-29 11:36:58"
last-updated: "2025-04-26"
star: 11962
components:
    - scheduler
    - task-management
    - inter-task-communication
    - memory-management
    - timer-management
    - network-stack
    - ble
    - wifi
    - lorawan
    - 6lowpan
    - http-client
    - http-server
    - mqtt-client
    - coap
    - dhcp-client
    - dhcp-server
    - dns-client
    - tls-ssl
    - filesystem
    - usb-host
    - usb-device
    - can
    - modbus
    - shell-cli
    - logging
    - ota-update
    - smp-support
    - gui
    - runtime-analysis
    - simulation
licenses:
    - Apache-2.0
platforms:
    - aarch32
    - aarch64
    - arm-cortex-a
    - arm-cortex-r
    - arm-cortex-m
    - x86
    - risc-v
    - mips
    - nios-ii
    - xtensa
    - sparc
    - posix
    - qemu
---
Zephyr is a scalable, open-source Real-Time Operating System (RTOS) designed for resource-constrained embedded systems, ranging from simple sensors to complex IoT gateways. Built with security and safety in mind, it features a small-footprint kernel, extensive connectivity options (including BLE 5.0, Wi-Fi, OpenThread), and broad hardware support across multiple architectures like ARM Cortex-M/R/A, RISC-V, x86, and Xtensa. Its modular design, powered by the Kconfig and Devicetree systems, allows developers to tailor the OS precisely to their application needs, optimizing performance and memory usage. Zephyr is backed by the Linux Foundation and a large, active community.

<!--more-->

The Zephyr Project provides a vendor-neutral, open-source, permissively licensed RTOS focused on the rapidly growing IoT market. It aims to deliver a robust, scalable, and secure platform for connected, resource-constrained devices.

**Architecture and Modularity:**
Zephyr's kernel is highly configurable. Developers can select only the necessary features (like specific kernel services, drivers, or protocol stacks) through the Kconfig system, minimizing the final image size. Hardware configuration is managed using Devicetree, allowing the same application code to run on different hardware platforms by simply changing the board configuration.

**Key Capabilities:**
The RTOS offers a rich set of kernel services, including preemptive and cooperative scheduling, various inter-thread synchronization and communication mechanisms, memory management (including MPU support for thread isolation on capable hardware), and power management features.

**Connectivity and Ecosystem:**
Zephyr boasts a native, highly optimized networking stack supporting IPv4/IPv6, TCP, UDP, and common application layer protocols (HTTP, MQTT, CoAP, LwM2M). It features a Bluetooth 5.0 qualified controller and host stack, including Mesh support. File systems like LittleFS and FatFs are supported, along with comprehensive logging, a command-line shell interface, settings management, and over-the-air (OTA) update capabilities.

**Development and Community:**
Development is supported on Linux, macOS, and Windows using CMake and the `west` meta-tool for managing the source code and build process. A native simulation target (`native_sim`) allows running and debugging Zephyr applications directly on the host PC. The project benefits from a vibrant community, extensive documentation, and support from numerous semiconductor vendors.

## Features

- **Scalable & Modular Kernel:** Configurable kernel services (threads, semaphores, mutexes, messages queues, etc.) via Kconfig.
- **Cross-Architecture:** Supports ARM Cortex-M/R/A (32/64-bit), RISC-V (32/64-bit), x86 (32/64-bit), Xtensa, MIPS, NIOS II, SPARC.
- **Flexible Scheduling:** Includes preemptive/cooperative priority-based scheduling, Earliest Deadline First (EDF), round-robin time-slicing, and meta-IRQ scheduling.
- **Memory Management:** Dynamic memory allocation (slab/heap), Memory Protection Unit (MPU) support for thread isolation and userspace, stack overflow protection.
- **Devicetree Integration:** Hardware description language for configuring peripherals and board features.
- **Unified Device Driver Model:** Consistent API for accessing diverse hardware peripherals.
- **Power Management:** System and device-level power management framework.
- **Rich Connectivity:**
    - Native Networking Stack (LwIP based): TCP/IP (v4/v6), UDP, ICMP, CoAP, LwM2M, MQTT, HTTP, DNS, DHCP.
    - Bluetooth 5.0 Qualified: Host stack & Controller (Link Layer), BLE Mesh, GAP/GATT, Secure Connections.
    - Other Wireless: Wi-Fi, LoRaWAN, OpenThread, 802.15.4.
- **Security:** Designed with security focus, includes features like MPU support, secure boot capabilities (via MCUboot), TLS/DTLS integration (mbedTLS), and a dedicated security subcommittee.
- **Storage:** Virtual Filesystem (VFS) support with backends like LittleFS, FatFs, NVS (Non-Volatile Storage), FCB (Flash Circular Buffer).
- **Development Tools:** CMake build system, `west` meta-tool, extensive sample applications, native simulation (`native_sim`), debugging support (GDB, OpenOCD, J-Link).
- **Logging & Diagnostics:** Powerful logging framework with multiple backends, shell interface with auto-completion, runtime analysis hooks.
- **SMP Support:** Symmetric Multi-Processing support on multi-core devices.
- **Permissive Licensing:** Apache 2.0 license for the core OS.

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
