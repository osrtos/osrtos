---
title: TizenRT
slug: tizenrt
version: 3.0_GBM
code-url: https://github.com/Samsung/TizenRT
site-url: https://github.com/Samsung/TizenRT
draft: false
date: "2018-02-11 06:48:49"
last-updated: "2023-08-18"
components:
    - FileSystem
    - Network
    - HTTP
    - HTTP/2
    - TLS/SSL
    - Command Line Interface
    - gRPC
    - IPv6
libraries:
    - None
licenses:
    - Apache License 2.0
platforms:
    - ARM
    - iMX RT
    - QEMU
---
TizenRT is a lightweight RTOS (Real-Time Operating System) designed to support low-end IoT devices. It aims to extend the Tizen platform device coverage to devices like home appliances without display and wearable bands with a small LCD. These devices are typically equipped with Cortex-M/R processors with MPU, less than 2 MB RAM, and less than 16 MB Flash.

<!--more-->

### Features

- **RTOS-based Platform**: Specifically designed for low-end IoT devices.
- **IPv6 Support**: Includes support for Neighbor Discovery (ND6), Multicast Listener Discovery (MLD), and ICMPv6 protocols.
- **Docker Build Environment**: Provides an easy way to build using Docker, eliminating the need for manual library and toolchain installations.
- **Media Framework**: Offers player/recorder functionalities for voice/audio streaming.
- **Task Manager Framework**: Enables control and messaging between applications.
- **Network Monitoring Tool**: Monitors real-time information regarding network sockets, network interface, and WiFi Manager.
- **gRPC for Client Roles**: Supports various RPC types and both insecure and secure modes of RPC execution.
- **HTTP/2 Support**: Ported nghttp2 version 1.32.0 from Github.

### Components

- **Kernel and System**: Provides features like stack trace in text, new pthread_tryjoin_np API, and Docker build environment.
- **Network and Connectivity**: Offers IPv6 support, network monitoring tools, gRPC for client roles, and HTTP/2.
- **Framework**: Includes a media framework, voice control manager, task manager framework, and Wi-Fi manager framework.
- **External**: Incorporates libc++, protocol buffer, cURL, and a stress test tool.

### Platforms

- ARTIK053
- ARTIK053S
- ARTIK055S
- CY4390X
- ESP32-DevKitC
- ESP-WROVER-KIT
- iMX RT 1020 EVK
- iMX RT 1050 EVK
- SIDK_S5JT200
- STM32F407-DISC1
- STM32F429I-DISCO
- STM32L4R9AI-DISCO
- QEMU

### Resources
<!--github-projects-->
- [IoTJS-Plus-TizenRT](https://github.com/SKKU-ESLAB/IoTJS-Plus-TizenRT). IoT.js of ANT based on Tizen RT.
- [docker-artik-devenv](https://github.com/webispy/docker-artik-devenv). Dockerfile for ARTIK development environment.
- [ocf_mylight](https://github.com/webispy/ocf_mylight). OCF Light sample for Linux and TizenRT using IoTivity stack..