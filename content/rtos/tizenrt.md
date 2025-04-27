---
title: TizenRT
slug: tizenrt
version: 3.0_GBM
code-url: https://github.com/Samsung/TizenRT
site-url: https://github.com/Samsung/TizenRT
date: "2018-02-11 06:48:49"
last-updated: "2025-04-24"
star: 613
components:
    - scheduler
    - task-management
    - inter-task-communication
    - memory-management
    - timer-management
    - network-stack
    - wifi
    - http-client
    - http-server
    - mqtt-client
    - coap
    - grpc
    - http2
    - ftp-client
    - dhcp-client
    - dhcp-server
    - dns-client
    - tls-ssl
    - filesystem
    - database
    - shell-cli
    - logging
    - runtime-analysis
    - simulation
licenses:
    - Apache-2.0
platforms:
    - arm-cortex-m
    - arm-cortex-r
    - xtensa
    - qemu
    - posix
---
TizenRT is a lightweight Real-Time Operating System (RTOS) developed by Samsung, designed to extend the Tizen platform to low-end, resource-constrained IoT devices. Based initially on the NuttX kernel, TizenRT targets microcontrollers like ARM Cortex-M/R with limited memory (less than 2MB RAM) and flash storage (less than 16MB). It provides a familiar Linux-like development environment with POSIX API compatibility, BSD sockets, and a shell interface (TASH). TizenRT includes integrated networking stacks (IPv4/IPv6), file systems, a lightweight database (AraStorage), and support for various IoT protocols, aiming to simplify development for connected devices.

<!--more-->

TizenRT originated from the TinyAra project in 2015, leveraging the NuttX RTOS known for its standards compliance and small footprint. While retaining the core NuttX kernel architecture, Samsung significantly built upon it, adding essential middleware for IoT applications. This includes a robust IPv4/IPv6 network stack based on LwIP, multiple file system options including SmartFS (optimized for flash) and ROMFS, the AraStorage lightweight database for local data handling, and support for prominent IoT protocols such as OCF, LWM2M, MQTT, and CoAP. Security is addressed through TLS/SSL integration.

A key design goal of TizenRT is to provide a development experience familiar to Linux developers, thereby lowering the barrier to entry for embedded development. It achieves this through strong POSIX API compliance, a standard BSD Socket API for networking, an interactive shell (TASH) for debugging and device management, and a Kconfig-based build system similar to the Linux kernel. This allows developers to more easily port existing applications or leverage familiar development paradigms.

To cater to modern web-centric IoT development, TizenRT incorporated support for a lightweight JavaScript environment using JerryScript and IoT.js starting in 2017. This enables application development using JavaScript on resource-constrained devices.

The build system is streamlined, offering tools like `configure.sh` and `dbuild.sh`, and notably provides official Docker containers. These containers package the necessary toolchains and libraries, simplifying the setup process across different development host environments. TizenRT also supports QEMU for simulation and testing purposes.

TizenRT has seen commercial deployment in Samsung smart home appliances and various IoT devices since 2017.

## Features

- **NuttX-based Kernel:** Real-time, standards-compliant kernel with a small footprint.
- **POSIX Compatibility:** Provides a familiar API for developers migrating from Linux environments.
- **BSD Socket API:** Standard interface for network programming.
- **Integrated Network Stack:** Supports IPv4 and IPv6 using LwIP, with features like DHCP, DNS, TLS/SSL.
- **Connectivity:** Built-in Wi-Fi management framework supporting STA and SoftAP modes.
- **File Systems:** Includes SmartFS (flash-optimized), ROMFS, and others. Supports FAT.
- **Lightweight Database:** AraStorage for efficient on-device data management.
- **IoT Protocol Support:** Includes native or library support for MQTT, CoAP, HTTP/2, gRPC, OCF, LWM2M.
- **Shell Interface:** TASH (TinyAra SHell) for interactive command-line access.
- **Low Resource Usage:** Optimized for devices with minimal RAM and Flash (e.g., Cortex-M/R).
- **JavaScript Support:** Integrates JerryScript and IoT.js for JavaScript application development.
- **Build System:** Kconfig-based configuration and Docker support for easy environment setup.
- **Simulation:** QEMU support for development and testing without hardware.
- **Runtime Analysis:** Tools like T-trace and heap information commands for debugging and profiling.
- **Frameworks:** Includes frameworks for Media (Audio Player/Recorder), Task Management, and Wi-Fi Management.
- **libc++ Support:** Provides LLVM-based C++ standard library implementation.

### Resources
<!--github-projects-->
- [IoTJS-Plus-TizenRT](https://github.com/SKKU-ESLAB/IoTJS-Plus-TizenRT). IoT.js of ANT based on Tizen RT.
- [docker-artik-devenv](https://github.com/webispy/docker-artik-devenv). Dockerfile for ARTIK development environment.
- [ocf_mylight](https://github.com/webispy/ocf_mylight). OCF Light sample for Linux and TizenRT using IoTivity stack..
