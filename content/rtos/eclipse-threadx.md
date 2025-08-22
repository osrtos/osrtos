---
title: Eclipse ThreadX
slug: threadx-rtos
version: v6.4.2_rel
code-url: https://github.com/eclipse-threadx/threadx
site-url: hhttps://threadx.io/ttps://azure.microsoft.com/en-us/services/rtos/
date: 2020-05-27 09:25:57+08:00
last-updated: "2025-07-29"
star: 3248
components:
    - scheduler
    - task-management
    - inter-task-communication
    - memory-management
    - timer-management
    - network-stack
    - filesystem
    - usb-host
    - usb-device
    - gui
    - dynamic-loading
    - smp-support
    - runtime-analysis
    - tls-ssl
    - http-client
    - http-server
    - mqtt-client
    - dhcp-client
    - dhcp-server
    - dns-client
    - ftp-client
    - ftp-server
    - snmp-agent
licenses:
    - MIT
platforms:
    - arm-cortex-m
    - arm-cortex-a
    - arm-cortex-r
    - risc-v
    - xtensa
    - arc
    - mips
    - nios-ii
    - microblaze
    - powerpc
    - posix
---
Eclipse ThreadX is an advanced, widely deployed Real-Time Operating System (RTOS) designed for deeply embedded, real-time, and IoT applications, especially on resource-constrained devices. Formerly known as Azure RTOS, ThreadX offers reliable, ultra-fast performance with a minimal footprint (as low as 2KB ROM, 1KB RAM). It features a picokernel architecture, preemption-threshold scheduling, event chaining, comprehensive IPC mechanisms, and a rich ecosystem including networking, file system, USB, and GUI components. ThreadX comes with extensive safety and security certifications (e.g., TÜV IEC 61508 SIL4, UL 60730, EAL4+, FIPS 140-2).

<!--more-->

## Overview

Eclipse ThreadX, originally developed by Express Logic and later known as Microsoft Azure RTOS, is now an open-source project under the Eclipse Foundation. It has been deployed on over 12 billion devices worldwide. ThreadX is designed specifically for embedded systems requiring high performance, determinism, and minimal resource usage.

## Core Kernel (ThreadX)

The heart of the Eclipse ThreadX suite is the ThreadX RTOS kernel. Its key characteristics include:

*   **Picokernel Architecture:** A non-layered design where services plug directly into the core, ensuring minimal internal function call layering and fast context switching (sub-microsecond on many processors).
*   **Scheduling:** Features priority-based preemptive scheduling with up to 1024 priority levels. It supports round-robin scheduling, time-slicing per thread, and cooperative scheduling via `tx_thread_relinquish`.
*   **Preemption-Threshold Scheduling:** A unique feature allowing threads to disable preemption up to a specified priority level, reducing context switches and aiding in preventing priority inversion.
*   **Inter-Process Communication (IPC):** Provides a rich set of synchronization and communication primitives:
    *   Message Queues (including mailboxes)
    *   Counting Semaphores (including binary semaphores)
    *   Mutexes (with optional priority inheritance to prevent non-deterministic priority inversion)
    *   Event Flags Groups (32 flags per group, supporting AND/OR logic)
*   **Memory Management:** Offers two types of memory pools:
    *   Fixed-size Block Pools: Fast, deterministic allocation with no fragmentation.
    *   Byte Pools: Flexible allocation similar to `malloc`, supporting variable-size blocks with fragmentation management (merging/splitting).
*   **Timers:** Supports application timers (one-shot and periodic) and a relative time tick counter (`tx_time_get`/`tx_time_set`).
*   **Interrupt Management:** Provides efficient interrupt handling with minimal lockout times and allows many API services to be called from ISRs.

## Additional Components & Features

*   **ThreadX SMP:** A Symmetric Multi-Processing (SMP) version of ThreadX for multi-core processors, featuring automatic load balancing and per-thread/timer core exclusion capabilities.
*   **ThreadX Modules:** Enables dynamic loading and execution (or execute-in-place) of application modules, facilitating field upgrades, bug fixes, and memory protection via MPU/MMU if available.
*   **FileX:** A high-performance, FAT-compatible (FAT12/16/32, exFAT) embedded file system, fully integrated with ThreadX. Supports various media like RAM disk, SD cards, and Flash memory via LevelX.
*   **LevelX:** Provides Flash wear leveling support for NAND and NOR flash memory, working beneath FileX.
*   **NetX Duo:** An advanced, industrial-grade dual IPv4/IPv6 TCP/IP network stack. It includes support for core protocols (TCP, UDP, IPv4, IPv6, ICMPv4, ICMPv6, IGMP, MLD, ARP, RARP, NDP) and numerous application protocols like MQTT, HTTP(S), FTP(S), DHCP, DNS, mDNS/DNS-SD, SNMP, SMTP, POP3, Telnet, TFTP, SNTP, AutoIP, PPP, PPPoE, DTLS, TLS, and more. Includes BSD socket compatibility layer.
*   **USBX:** A high-performance USB Host, Device, and OTG embedded stack supporting various device classes (HID, CDC/ACM, PIMA/MTP, Storage, Audio, DPUMP, GSER, RNDIS, etc.).
*   **GUIX:** A professional-quality embedded graphical user interface (GUI) development package, small, fast, and easily portable. Includes GUIX Studio, a desktop design tool that generates C code.
*   **TraceX:** A host-based analysis tool providing a graphical view of real-time system events for visualization and debugging.
*   **Adaptation Layers:** Provides compatibility layers for easier migration from other RTOS APIs like FreeRTOS, POSIX, and OSEK.

## Certifications and Compliance

Eclipse ThreadX is notable for its extensive pre-certifications:

*   **Safety:** SGS-TÜV Saar certified to IEC 61508 SIL 4. Recognized by UL for compliance with UL/IEC 60730 Annex H, UL/IEC 60335 Annex R, and UL 1998.
*   **Security:** EAL4+ Common Criteria security certification (covering ThreadX, NetX Duo, TLS, MQTT). FIPS 140-2 validated crypto libraries.
*   **MISRA:** MISRA C:2004 and MISRA C:2012 compliant source code.

## Supported Architectures

Eclipse ThreadX runs on a vast majority of popular 32/64-bit microprocessors and microcontrollers, including:

*   ARM Cortex-M (M0/M0+/M3/M4/M7/M23/M33/M35P/M55/M85), including TrustZone (ARMv8-M)
*   ARM Cortex-R (R4/R5/R7)
*   ARM Cortex-A (A5/A7/A8/A9/A1x/A3x/A5x/A6x/A7x), including 64-bit variants
*   Legacy ARM (ARM7/9/11)
*   RISC-V (32/64-bit)
*   Synopsys ARC (EM, HS, SMP variants)
*   Cadence Xtensa
*   MIPS (MIPS32, MIPS64, microAptiv, interAptiv, proAptiv)
*   Renesas RX, SH, HS, V850, RA, RZ, Synergy
*   Intel x86
*   Xilinx MicroBlaze, Zynq
*   NXP PowerPC
*   And many others.
*   Simulation/Emulation: Linux and Windows ports available for development and testing.

## Features

*   **Picokernel Architecture:** Non-layered design for maximum performance and minimal overhead.
*   **Preemption-Threshold Scheduling:** Advanced scheduling feature unique to ThreadX, reduces context switching and improves responsiveness.
*   **Event Chaining:** Efficiently links multiple synchronization events for complex coordination.
*   **Small Footprint:** Highly scalable, minimal configuration requires ~2KB ROM and ~1KB RAM.
*   **Fast and Deterministic:** Sub-microsecond context switch times on typical MCUs, highly deterministic behavior.
*   **Comprehensive IPC:** Includes Queues, Semaphores, Mutexes (with Priority Inheritance), and Event Flags.
*   **Memory Management:** Offers fast Fixed Block Pools (no fragmentation) and flexible Byte Pools.
*   **Application Timers:** Supports one-shot and periodic software timers.
*   **SMP Support:** Optional Symmetric Multi-Processing capability with automatic load balancing and core exclusion.
*   **Modules:** Supports dynamic loading of application code with optional memory protection.
*   **Safety/Security Certified:** Pre-certified for IEC 61508 SIL 4, UL 60730/60335/1998, EAL4+, FIPS 140-2.
*   **MISRA C Compliant:** Adheres to MISRA C:2004 and C:2012 standards.
*   **Wide Processor Support:** Extensive support for various 32-bit and 64-bit architectures.
*   **Rich Ecosystem:** Includes mature components for Networking (NetX Duo), File System (FileX), USB (USBX), GUI (GUIX), Flash Wear Leveling (LevelX), and analysis tools (TraceX, GUIX Studio).
*   **Adaptation Layers:** Simplifies migration from other RTOS environments like FreeRTOS, POSIX, OSEK.

## Resources
<!--github-projects-->
- [guix](https://github.com/eclipse-threadx/guix). Eclipse GUIX Studio provides a complete, embedded graphical user interface (GUI) library and design environment, facilitating the creation and maintenance of all graphical elements needed by your device..
- [netxduo](https://github.com/eclipse-threadx/netxduo). Eclipse NetX Duo is an advanced, industrial-grade TCP/IP network stack designed specifically for deeply embedded real-time and IoT applications.
- [x-cube-azrtos-h7](https://github.com/STMicroelectronics/x-cube-azrtos-h7). X-CUBE-AZRTOS-H7 (Eclipse Software Expansion for STM32Cube) provides a full integration of Microsoft Eclipse in the STM32Cube environment for the STM32H7 series of microcontrollers..
- [filex](https://github.com/eclipse-threadx/filex). Eclipse FileX is a high-performance, FAT-compatible file system that’s fully integrated with Eclipse ThreadX.
- [usbx](https://github.com/eclipse-threadx/usbx). Eclipse USBX is a high-performance USB host, device, and on-the-go (OTG) embedded stack, that is fully integrated with Eclipse ThreadX .
- [levelx](https://github.com/eclipse-threadx/levelx). Eclipse LevelX Provides Flash Wear Leveling for FileX and Stand Alone purposes..
- [x-cube-azrtos-f4](https://github.com/STMicroelectronics/x-cube-azrtos-f4). X-CUBE-AZRTOS-F4 (Eclipse Software Expansion for STM32Cube) provides a full integration of Microsoft Eclipse in the STM32Cube environment for the STM32F4 series of microcontrollers..
- [x-cube-iota1](https://github.com/STMicroelectronics/x-cube-iota1). The X-CUBE-IOTA1 is an expansion software package for STM32Cube. The software runs on the STM32 and includes the middleware for enabling the IOTA Distributed Ledger Technology..
- [x-cube-azrtos-l4](https://github.com/STMicroelectronics/x-cube-azrtos-l4). X-CUBE-AZRTOS-L4 (Eclipse Software Expansion for STM32Cube) provides a full integration of Microsoft Eclipse in the STM32Cube environment for the STM32L4 series of microcontrollers..
- [x-cube-azrtos-g4](https://github.com/STMicroelectronics/x-cube-azrtos-g4). X-CUBE-AZRTOS-G4 (Eclipse Software Expansion for STM32Cube) provides a full integration of Microsoft Eclipse in the STM32Cube environment for the STM32G4 series of microcontrollers..
- [x-cube-azrtos-f7](https://github.com/STMicroelectronics/x-cube-azrtos-f7). X-CUBE-AZRTOS-F7 (Eclipse Software Expansion for STM32Cube) provides a full integration of Microsoft Eclipse in the STM32Cube environment for the STM32F7 series of microcontrollers..
- [iotc-azurertos-sdk](https://github.com/avnet-iotconnect/iotc-azurertos-sdk). IoTConnect C SDK for AzureRTOS Devices.
- [x-cube-azrtos-wb](https://github.com/STMicroelectronics/x-cube-azrtos-wb). X-CUBE-AZRTOS-WB (Eclipse Software Expansion for STM32Cube) provides a full integration of Microsoft Eclipse in the STM32Cube environment for the STM32WB series of microcontrollers..
- [H747-Test](https://github.com/c4chris/H747-Test). STM32 H747I DISCO trying out Eclipse ThreadX and GUIX on dual core and DSI LTDC display.
- [x-cube-azrtos-wl](https://github.com/STMicroelectronics/x-cube-azrtos-wl). X-CUBE-AZRTOS-WL (Eclipse Software Expansion for STM32Cube) provides a full integration of Microsoft Eclipse in the STM32Cube environment for the STM32WL series of microcontrollers..
- [x-cube-azrtos-g0](https://github.com/STMicroelectronics/x-cube-azrtos-g0). X-CUBE-AZRTOS-G0 (Eclipse Software Expansion for STM32Cube) provides a full integration of Microsoft Eclipse in the STM32Cube environment for the STM32G0 series of microcontrollers..
- [rp2040-eclipse-threadx-blink](https://github.com/jgroman/rp2040-eclipse-threadx-blink). Blink example with RPi Pico RP2040 and Eclipse.
- [H747-Camera](https://github.com/c4chris/H747-Camera). Explore AI possibilities to sort seeds using STM32 H7 board coupled to a camera.
- [x-cube-azrtos-l5](https://github.com/STMicroelectronics/x-cube-azrtos-l5). X-CUBE-AZRTOS-L5 (Eclipse Software Expansion for STM32Cube) provides a full integration of Microsoft Eclipse in the STM32Cube environment for the STM32L5 series of microcontrollers..
- [H747-WeighingStation](https://github.com/c4chris/H747-WeighingStation). Control board for a prototype weighing station, HDMI display and touchscreen USB interface.
