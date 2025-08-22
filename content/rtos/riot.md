---
title: RIOT
slug: riot
version: "2025.07"
code-url: https://github.com/RIOT-OS/RIOT
site-url: http://riot-os.org/
date: "2016-11-29 11:36:58"
last-updated: "2025-08-21"
star: 5573
components:
    - scheduler
    - task-management
    - inter-task-communication
    - memory-management
    - timer-management
    - network-stack
    - ble
    - lorawan
    - 6lowpan
    - coap
    - mqtt-client
    - usb-device
    - filesystem
    - ota-update
    - shell-cli
    - logging
    - simulation
    - runtime-analysis
    - crypto
licenses:
    - LGPL-2.1
platforms:
    - arm-cortex-m
    - risc-v
    - xtensa
    - avr
    - msp430
    - posix
---
RIOT, "The friendly Operating System for IoT," is an open-source RTOS designed for resource-constrained embedded devices, particularly in the Internet of Things space. It supports a wide range of 8-bit, 16-bit, and 32-bit microcontrollers. Key design goals include energy efficiency, real-time capabilities, a small memory footprint, modularity, and a hardware-independent API with partial POSIX compliance. Developed by a vendor-independent open-source community, RIOT uses the LGPLv2.1 license, allowing integration with closed-source components. Its extensive feature set, especially in networking, makes it a strong choice for connected embedded systems.

<!--more-->

RIOT aims to provide a developer-friendly environment for building IoT applications. It features a preemptive, tickless real-time kernel, flexible memory management, and high-resolution timers. Its hardware support is broad, covering architectures like ARM Cortex-M, RISC-V, ESP32/ESP8266, AVR, and MSP430, with over 200 specific boards supported.

A standout feature is the `native` port, which allows RIOT applications to run as standard processes on Linux, BSD, or macOS. This facilitates development, debugging, testing, and simulation without requiring target hardware initially. Multiple native instances can be interconnected using virtual network interfaces (TAP devices) or simulated IEEE 802.15.4 networks.

Networking is a core strength, built around the modular GNRC (Generic Network Stack). GNRC provides a comprehensive IPv6 stack including 6LoWPAN (with header compression and fragmentation), UDP, and RPL (routing protocol). Higher-level protocols like CoAP and MQTT are also supported. Wireless connectivity options include LoRaWAN and Bluetooth Low Energy (via Apache NimBLE integration).

RIOT employs a standard Make-based build system and offers Docker images for simplified toolchain setup across different development environments. The community provides support through a forum and Matrix chat, maintaining extensive documentation including API references and tutorials. The LGPLv2.1 license encourages adoption by allowing proprietary code linkage while keeping the core OS open.

## Features

- **Real-time Kernel:** Preemptive, tickless scheduler with configurable priorities.
- **Low Footprint:** Designed for memory-constrained devices (8/16/32-bit MCUs).
- **Modularity:** Highly configurable via Kconfig and module selection.
- **Hardware Abstraction:** Uniform API access across different microcontrollers.
- **Partial POSIX Compliance:** Offers a familiar API for developers.
- **Native Port:** Run RIOT applications on Linux/BSD/macOS for development and simulation.
- **Extensive Networking (GNRC):** IPv6, 6LoWPAN (RFC6282, RFC6775), UDP, RPL (Storing & P2P), TCP (experimental).
- **IoT Protocols:** CoAP, MQTT client support.
- **Wireless Support:** LoRaWAN, Bluetooth Low Energy (via NimBLE), IEEE 802.15.4 MAC protocols (e.g., CSMA, TSCH).
- **Wide Platform Support:** ARM Cortex-M, RISC-V, Xtensa (ESP32/ESP8266), AVR, MSP430, native (POSIX).
- **Timers:** High-resolution `ztimer` abstraction layer for precise timing.
- **Memory Management:** Flexible options including heap allocators.
- **Filesystem Integration:** Virtual File System (VFS) support.
- **USB Device Stack:** Support for USB device functionality.
- **OTA Updates:** Secure Firmware Updates using the SUIT (Software Updates for IoT) standard.
- **Cryptography:** Integrated crypto libraries (e.g., HWRNG support, PSA Crypto API, C25519, TweetNaCl).
- **Shell Interface:** Built-in command-line shell for interaction and diagnostics.
- **Development Tools:** Make build system, Docker support, `pyterm` serial terminal, GDB debugging integration.

## Components

- **scheduler:** Preemptive, tickless, priority-based kernel scheduler.
- **task-management:** Multi-threading support with standard RTOS primitives (creation, termination, synchronization).
- **inter-task-communication:** Includes messaging (IPC), mailboxes, event queues, semaphores, and mutexes.
- **memory-management:** Provides various memory allocation strategies suitable for constrained devices.
- **timer-management:** `ztimer` high-resolution timer abstraction for scheduling events and delays.
- **network-stack:** Modular GNRC stack supporting IPv6, 6LoWPAN, UDP, TCP (experimental), RPL, and various MAC layers.
- **ble:** Support via integrated Apache NimBLE stack.
- **lorawan:** LoRaWAN stack implementation integrated with GNRC.
- **6lowpan:** Integrated 6LoWPAN adaptation layer with fragmentation (RFC4944) and header compression (RFC6282, RFC6775).
- **coap:** Support for the Constrained Application Protocol.
- **mqtt-client:** MQTT client functionality for IoT messaging.
- **usb-device:** USB device stack enabling peripherals like CDC-ACM (Serial), MSC (Mass Storage), DFU (Device Firmware Upgrade).
- **filesystem:** Virtual File System (VFS) layer allowing integration of filesystems like FATFS (SPIFFS, LittleFS via external modules).
- **ota-update:** Secure Firmware Updates using the IETF SUIT standard manifest format.
- **shell-cli:** Interactive command-line interface accessible via serial/network for system control and debugging.
- **logging:** Configurable logging framework for diagnostics.
- **simulation:** Native port allows running RIOT applications directly on host OS (Linux, macOS, BSD) for rapid development and testing.
- **runtime-analysis:** Utilities like `ps` (process status) and scheduler statistics (`schedstatistics`) for observing system state.
- **crypto:** Includes cryptographic primitives, hash functions, and support for PSA Cryptographic API.

### Resources

- [Arduino Hello World](https://github.com/RIOT-OS/RIOT/tree/master/examples/arduino_hello-world). This application demonstrates the usage of Arduino sketches in RIOT.
- [RIOT Documentation](https://doc.riot-os.org/): Official documentation, including API reference and guides.
<!--github-projects-->
- [examples](https://github.com/riot/examples). Demos and examples for Riot and submodules.
- [PineTime-apps](https://github.com/bosmoment/PineTime-apps). Firmware for the PineTime based on RIOT, NimBLE and LittleVGL.
- [applications](https://github.com/RIOT-OS/applications). Some useful RIOT applications.
