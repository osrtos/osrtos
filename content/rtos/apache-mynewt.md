---
title: Apache Mynewt
slug: apache-mynewt
version: pre_sterly_refactor
code-url: https://github.com/apache/mynewt-core
site-url: https://mynewt.apache.org/
draft: false
date: "2016-11-29 11:36:58"
last-updated: "2023-08-10"
components:
    - BLE
    - LoRaWAN
    - FileSystem
    - Network
    - 6LoWPAN
    - TLS/SSL
    - Runtime Analysis
libraries:
    - None
licenses:
    - Apache License
platforms:
    - ARM
    - MIPS
---
Apache Mynewt OS is a real-time, modular operating system for connected IoT devices that need to operate for long periods of time under power, memory, and storage constraints. It provides a complete environment for prototyping, developing, and managing em

<!--more-->

### Features
- A Pre-emptive, Real Time OS Kernel
- A open-source Bluetooth 4.2 stack (both Host & Controller), NimBLE, that completely replaces the proprietary SoftDevice on Nordic chipsets.
- Support for 251 byte packet size
- Support for all 4 roles concurrently - Broadcaster, Observer, Peripheral and Central
- Support for up to 32 simultaneous connections.
- Legacy SMP support (pairing and bonding).
- A flash filesystem, NFFS, which is designed for tiny (128KB->16MB) flashes.
- Bootloader support
- Remote Software Upgrade
- HAL and BSP infrastructure designed to abstract microcontroller specifics
- Shell and Console support
- Statistics and Logging Infrastructure.


