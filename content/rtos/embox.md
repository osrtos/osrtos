---
title: embox
slug: embox
version: v0.6.5
code-url: https://github.com/embox/embox
site-url: https://github.com/embox/embox
date: "2017-03-18 01:28:16"
last-updated: "2025-04-09"
star: 1361
components:
    - scheduler
    - task-management
    - inter-task-communication
    - memory-management
    - timer-management
    - network-stack
    - http-client
    - http-server
    - dhcp-client
    - dns-client
    - tls-ssl
    - mqtt-client
    - filesystem
    - usb-host
    - usb-device
    - shell-cli
    - logging
    - gui
    - smp-support
    - simulation
licenses:
    - BSD-3-Clause
platforms:
    - arm-cortex-m
    - arm-cortex-a
    - aarch64
    - x86
    - risc-v
    - mips
    - powerpc
    - microblaze
    - sparc
    - qemu
    - posix
---
Embox is a highly configurable Real-Time Operating System (RTOS) designed for resource-constrained embedded systems. Its core philosophy is enabling the use of familiar Linux software and development paradigms *without* needing a full Linux kernel. Embox achieves this through strong POSIX compliance and a modular architecture (Mybuild system) allowing developers to select only necessary components. It supports a wide range of architectures and platforms, aiming to bring desktop-like capabilities, including networking, filesystems, GUIs (Qt, LVGL), and various scripting languages, to microcontroller environments.

<!--more-->

Embox stands out with its ambition to bridge the gap between traditional RTOSes and desktop Linux environments. By providing a POSIX-compliant API, it allows developers to port and run a surprising amount of existing software, originally intended for Linux/Unix systems, directly on microcontrollers and other embedded hardware. This includes complex libraries and applications like Qt, OpenCV, PJSIP (for VoIP), Dropbear (SSH server), Mesa3D, and even games like Quake3.

The system is built around a custom build system called "Mybuild", which manages dependencies and configuration options. This allows for fine-grained control over the final firmware image size and features, crucial for memory-constrained devices. Developers can choose from various filesystems (FAT, ext2/3/4), networking protocols (TCP/IP stack with BSD sockets, HTTP, NTP, etc.), and even include interpreters for languages like Python, Lua, JavaScript, and Ruby.

Embox supports symmetric multiprocessing (SMP) and runs on a diverse set of CPU architectures including ARM (Cortex-M/A), x86, RISC-V, MIPS, PowerPC, Microblaze, and SPARC. It has demonstrated capabilities on popular boards like various STM32 Discovery/Nucleo series, Raspberry Pi, i.MX6 platforms, MAiX BiT (K210), and supports simulation via QEMU for rapid development and testing.

## Features

-   **POSIX Compliance:** Enables porting of Linux/Unix applications with minimal effort.
-   **High Configurability:** Modular design using the Mybuild system allows tailoring the OS to specific needs.
-   **Wide Architecture Support:** Runs on ARM (Cortex-M/A), x86, RISC-V, MIPS, PowerPC, Microblaze, SPARC, AArch64.
-   **Rich Networking Stack:** Includes BSD Sockets API, TCP/IP, UDP, HTTP, DHCP, DNS, NTP, ICMP, Telnet, SSH (Dropbear), NFS, Samba.
-   **Filesystem Support:** Supports FAT12/16/32, ext2/3/4, and others.
-   **Third-Party Software Integration:** Capable of running complex libraries and applications like Qt, LVGL, Nuklear, OpenCV, PJSIP, Mesa3D, FFMPEG.
-   **Multi-Language Support:** Includes support for C, C++, and interpreters for Python, Lua, Java (phoneme), JavaScript, Ruby, Lisp, TCL, Scheme.
-   **Unix-like Shell:** Provides a command-line interface with familiar utilities (ls, cat, mount, etc.).
-   **Hardware Abstraction:** Drivers for various peripherals including GPIO, I2C, SPI, UART, Ethernet, USB, SD/MMC, Frame buffer, RTC.
-   **Debugging Support:** Integrates with GDB, OpenOCD, JLink, including support for SEGGER RTT logging.
-   **SMP Support:** Symmetric Multiprocessing capabilities demonstrated on multi-core platforms (e.g., via QEMU).
-   **Simulation:** Extensive support for running and testing on QEMU across multiple architectures.

### Resources
<!--github-projects-->
- [mybuild-mode](https://github.com/easimonenko/mybuild-mode). GNU Emacs major mode for editing Mybuild files from Embox operating system.
