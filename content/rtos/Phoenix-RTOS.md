---
title: Phoenix-RTOS
slug: phoenix-rtos
version: v3.3.2
code-url: https://github.com/phoenix-rtos/phoenix-rtos-kernel
site-url: https://phoenix-rtos.com/
date: "2019-02-12 06:00:17"
last-updated: "2025-04-18"
star: 135
components:
    - scheduler
    - task-management
    - inter-task-communication
    - memory-management
    - filesystem
    - network-stack
    - tls-ssl
    - http-client
    - http-server
    - mqtt-client
    - wifi
    - usb-host
    - usb-device
    - shell-cli
    - logging
    - gui
licenses:
    - BSD-3-Clause
platforms:
    - arm-cortex-m
    - arm-cortex-a
    - x86
    - risc-v
    - sparc
    - posix
---
Phoenix-RTOS is a scalable, open-source, real-time operating system designed for IoT devices and other resource-constrained applications. It features a custom microkernel architecture, separating core functionalities like memory management, scheduling, and IPC from higher-level services such as filesystems, networking stacks, and device drivers, which run as server processes in user space. This design emphasizes modularity and scalability, allowing deployment on microcontrollers up to multi-processor systems. It supports multiple hardware architectures including ARM Cortex-M/A, x86, RISC-V, and SPARC (LEON).

<!--more-->

Phoenix-RTOS utilizes a message-passing mechanism for inter-process communication (IPC), enabling interaction between the microkernel, servers, and applications. While this can introduce some overhead compared to monolithic kernels, it enhances system modularity, robustness (fault isolation), and scalability. User-space device drivers communicate with hardware via memory mapping or special I/O privileges granted by the kernel, with interrupts redirected to the relevant driver processes.

The system provides its own standard C library (libphoenix) and can emulate a POSIX environment, allowing many standard Unix/Linux applications and libraries to be ported and executed. This portability is demonstrated by the availability of numerous "ports" - adapted open-source tools and libraries like busybox, curl, dropbear (SSH), lighttpd, mbedtls/openssl, micropython, and network utilities like wpa_supplicant and OpenVPN.

Phoenix-RTOS has seen practical deployment in smart utility applications (gas/energy meters, data concentrators). Development includes ongoing work on an ARINC653 (avionics standard) execution environment. It also offers core libraries for graphics (libgraph), CGI (libcgi), virtual I/O (libvirtio), UUIDs, caching, and software watchdog services.

## Features

- **Microkernel Architecture:** Core OS services (scheduling, memory management, IPC) in the kernel, drivers and filesystems run as user-space servers.
- **Real-time Capabilities:** Designed with real-time performance considerations for time-critical applications.
- **Scalability:** Suitable for small microcontrollers up to complex multi-processor systems.
- **Modularity:** System services are implemented as independent server processes communicating via IPC.
- **Multi-architecture Support:** Runs on ARM Cortex-M, Cortex-A, x86, RISC-V, and SPARC (LEON).
- **Message Passing IPC:** Primary communication mechanism between system components.
- **User-space Device Drivers:** Drivers run as processes, enhancing fault isolation.
- **Filesystem Abstraction:** Supports multiple filesystems via dedicated file server processes.
- **POSIX Compatibility Layer:** Enables porting and running standard POSIX applications.
- **Ported Software Ecosystem:** Includes ports of common utilities (busybox), network tools (curl, ssh, httpd, vpn), crypto libraries (mbedtls, openssl), and scripting languages (lua, micropython).
- **ARINC653 Support (In Development):** Work towards supporting the avionics application software standard.

## Components

- **Scheduler:** Manages thread scheduling within the microkernel.
- **Task Management:** Handles process and thread creation, termination, and management.
- **Inter-task Communication:** Provides message passing ports for IPC between kernel, servers, and applications.
- **Memory Management:** Microkernel manages memory allocation and protection.
- **Filesystem:** Implemented via user-space file servers (e.g., FAT, JFFS2, rootfs).
- **Network Stack:** Provided through ports like lwIP and support for standard protocols (TCP/IP, UDP). Includes associated services:
    - `http-client` (via curl)
    - `http-server` (via lighttpd)
    - `tls-ssl` (via mbedtls, openssl)
    - `mqtt-client` (via Azure SDK port)
    - `wifi` (via wpa_supplicant port)
- **USB Host:** Support for USB host functionality.
- **USB Device:** Support for USB device functionality.
- **Shell/CLI:** Command-line interface provided via ports like busybox.
- **Logging:** System logging facilities.
- **GUI:** Basic graphics support via libgraph library.

## Resources

<!--github-projects-->
- [phoenix-rtos/phoenix-rtos-project](https://github.com/phoenix-rtos/phoenix-rtos-project): Sample project using Phoenix-RTOS.
- [phoenix-rtos/phoenix-rtos-ports](https://github.com/phoenix-rtos/phoenix-rtos-ports): Repository containing ports of third-party software.
- [Phoenix-RTOS Documentation](https://phoenix-rtos.com/documentation/): Official documentation portal.
