---
title: Apache Mynewt
slug: apache-mynewt
version: pre_sterly_refactor
code-url: https://github.com/apache/mynewt-core
site-url: https://mynewt.apache.org/
date: "2016-11-29 11:36:58"
last-updated: "2025-08-20"
star: 873
components:
    - scheduler
    - task-management
    - inter-task-communication
    - memory-management
    - timer-management
    - network-stack
    - ble
    - 6lowpan
    - coap
    - dhcp-client
    - dns-client
    - tls-ssl
    - filesystem
    - shell-cli
    - logging
    - ota-update
    - runtime-analysis
licenses:
    - Apache-2.0
platforms:
    - arm-cortex-m
    - risc-v
    - mips
    - posix
---
Apache Mynewt is a community-driven, open-source RTOS designed for highly constrained embedded systems where power and cost are primary concerns. It emphasizes modularity and portability, enabling developers to include only the necessary components for their application. Mynewt features a preemptive real-time kernel, the high-performance Apache NimBLE Bluetooth 5 stack, secure bootloader, and flash filesystems (NFFS, FatFS). Its companion `Newt` build and package management tool simplifies development, configuration, and deployment across diverse hardware, facilitating fine-grained control over the final firmware image.

<!--more-->

Apache Mynewt provides a complete ecosystem for developing and managing connected IoT devices operating under significant memory and power constraints. The core of the system is a highly efficient, preemptive RTOS kernel offering standard features like task management, timers, memory allocation, and inter-task communication primitives.

A key differentiator is the `Newt` tool, which manages the build process and package dependencies. This allows developers to easily compose custom OS configurations tailored to specific hardware and application requirements. `Newt` handles source package management, dependency resolution, building, and flashing firmware images, streamlining the development workflow.

Mynewt integrates the Apache NimBLE stack, a highly portable and efficient open-source Bluetooth Low Energy 5.0 implementation supporting both host and controller roles. Notably, NimBLE can replace proprietary vendor stacks on supported chipsets (like Nordic nRF series) and is designed to be OS-agnostic, although tightly integrated with Mynewt.

Filesystem support includes NFFS (Newtron Flash File System), optimized for small NOR flash devices, FatFS for compatibility with SD cards and other FAT media, and FCB (Flash Circular Buffer) for efficient logging or data streaming to flash.

Device management is facilitated by the `Newtmgr` tool and corresponding Mynewt libraries, enabling secure remote firmware updates (OTA), statistics collection, log retrieval, and configuration management over various transports like BLE or serial.

Networking capabilities are provided through integration with LwIP (offering IPv4/IPv6) and support for 6LoWPAN. Higher-level protocols like CoAP (via OIC support) are also available. Security is addressed through integration with mbedTLS for TLS/SSL connections. The OS provides extensive logging and statistics frameworks for monitoring and debugging.

## Features

- **Preemptive RTOS Kernel:** Provides core real-time scheduling, task management, IPC, and timing services.
- **Modular Architecture:** Highly composable using the `Newt` build and package management tool.
- **Apache NimBLE Bluetooth 5 Stack:** Integrated, open-source BLE Host & Controller supporting concurrent roles, extended advertising, and security features. (NimBLE source now in separate repo)
- **Multiple Filesystem Support:** Includes NFFS (optimized for small flash), FatFS, and FCB (Flash Circular Buffer).
- **Secure Bootloader & OTA:** Integrated bootloader supporting secure image validation and remote firmware updates via `Newtmgr`.
- **Hardware Abstraction Layer (HAL):** Simplifies porting across different microcontroller architectures.
- **Power Management:** Features designed for low-power operation in constrained devices.
- **Networking Stack:** Includes LwIP (IPv4/IPv6), 6LoWPAN, CoAP (via OIC), and standard TCP/IP utilities.
- **Rich Peripheral Support:** Drivers for common peripherals like UART, SPI, I2C, GPIO, Timers, Watchdog.
- **Shell & Console:** Command-line interface for debugging and interaction.
- **Logging & Statistics:** Infrastructure for system diagnostics and performance monitoring.
- **Data Serialization:** Support for JSON and CBOR encoding/decoding.
- **Security:** Integration with mbedTLS for secure communication (TLS/SSL).

<!--github-projects-->
