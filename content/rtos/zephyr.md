---
title: Zephyr
slug: zephyr
version: v3.4.0
code-url: https://github.com/zephyrproject-rtos/zephyr
site-url: https://www.zephyrproject.org
draft: false
date: "2016-11-29 11:36:58"
last-updated: "2023-08-16"
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
