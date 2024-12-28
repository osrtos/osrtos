---
title: RIOT
slug: riot
version: "2024.10"
code-url: https://github.com/RIOT-OS/RIOT
site-url: http://riot-os.org/
date: "2016-11-29 11:36:58"
last-updated: "2024-12-23"
star: 5355
components:
    - BLE
    - LoRaWAN
    - FileSystem
    - Network
    - 6LoWPAN
    - GUI
    - TLS/SSL
    - USBDevice
    - OTA
libraries:
    - SPIFFS
    - FatFs
    - littlefs
    - Ucglib
licenses:
    - LGPLv2.1
platforms:
    - MSP430
    - ARM
    - AVR
    - MIPS
    - RISC-V
---
RIOT is a real-time multi-threading operating system that supports a range of devices that are typically found in the Internet of Things (IoT): 8-bit, 16-bit and 32-bit microcontrollers.

<!--more-->

### Features

- A preemptive, tickless scheduler with priorities
- Flexible memory management
- High resolution, long-term timers
- Support for AVR, MSP430, ARM7, and ARM Cortex-M on over 50 boards
- The native port allows to run RIOT as-is on Linux, BSD, and MacOS. Multiple instances of RIOT running on a single machine can also be interconnected via a simple virtual Ethernet bridge
- IPv6
- 6LoWPAN (RFC4944, RFC6282, and RFC6775)
- UDP
- RPL (storing mode, P2P mode)
- CoAP
- CCN-Lite

### Sample projects and resources

- [Arduino Hello World](https://github.com/RIOT-OS/RIOT/tree/master/examples/arduino_hello-world). This application demonstrates the usage of Arduino sketches in RIOT.
<!--github-projects-->
- [examples](https://github.com/riot/examples). Demos and examples for Riot and submodules.
- [PineTime-apps](https://github.com/bosmoment/PineTime-apps). Firmware for the PineTime based on RIOT, NimBLE and LittleVGL.
- [applications](https://github.com/RIOT-OS/applications). Some useful RIOT applications.
