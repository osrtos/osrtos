---
title: ChibiOS/RT
slug: chibios-rt
version: ver21.11.3
code-url: https://github.com/ChibiOS/ChibiOS
site-url: http://www.chibios.org/dokuwiki/doku.php
date: "2016-11-29 11:36:57"
last-updated: "2025-08-20"
star: 790
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
    - can
    - shell-cli
    - logging
    - dynamic-loading
    - smp-support
    - runtime-analysis
    - simulation
licenses:
    - GPL-3.0
    - Apache-2.0
    - Commercial
platforms:
    - arm-cortex-m
    - arm-cortex-a
    - risc-v
    - avr
    - msp430
    - powerpc
    - pic
    - posix
    - x86
---
ChibiOS is a complete development environment for embedded applications, featuring a compact and high-performance Real-Time Operating System (RTOS). It includes two kernel variants: ChibiOS/RT, a feature-rich preemptive kernel, and ChibiOS/NIL, designed for extremely resource-constrained devices. The ecosystem encompasses a Hardware Abstraction Layer (HAL) with drivers for many peripherals, an OS library (OSLIB) for extensions like dynamic memory allocation and advanced IPC, and tools like ChibiStudio IDE. ChibiOS emphasizes efficiency, a fully static architecture (for core components), and portability, primarily targeting ARM Cortex-M MCUs but supporting various other architectures.

<!--more-->

ChibiOS provides a comprehensive suite for embedded systems development. Its core offering is the RTOS, available in two main flavors:

1.  **ChibiOS/RT:** A high-performance, preemptive, real-time kernel designed for efficiency and a rich feature set. It supports multiple scheduling strategies, including priority-based preemptive and round-robin. It offers a wide range of synchronization primitives (semaphores, mutexes with priority inheritance, condition variables, event flags, synchronous messages) and efficient timer management, including virtual timers and tickless operation. RT is known for its speed and deterministic behavior. Recent versions also introduce experimental SMP support.
2.  **ChibiOS/NIL:** An extremely tiny RTOS designed for MCUs with very limited resources (potentially sub-kB code size). While significantly smaller, it retains a core set of RTOS functionalities and follows a similar API structure to RT, allowing easier migration. It also employs a fully static architecture.

Beyond the kernels, the ChibiOS project includes:

*   **ChibiOS/HAL:** A Hardware Abstraction Layer providing a consistent API across different microcontroller families. It includes drivers for peripherals like ADC, CAN, DAC, GPIO, I2C, SPI, UART, USB (Device & Host), SD/MMC, Ethernet, RTC, PWM, Timers, and more. It heavily supports STMicroelectronics STM32, Raspberry Pi RP2040, Microchip PIC32/AVR/SAM, NXP Kinetis/LPC/i.MX RT, TI MSP430/Tiva, Infineon XMC, GigaDevice GD32 and others.
*   **ChibiOS/OSLIB:** An optional library extending both RT and NIL kernels with features like dynamic memory allocators (heap, memory pools), additional IPC mechanisms (mailboxes, object FIFOs), and dynamic thread creation support (RT only).
*   **ChibiOS/SB (Sandbox):** An extension for Cortex-M3/M4/M7 providing MPU-based memory isolation (sandboxing) capabilities, allowing applications to run untrusted or less critical code safely. Supports static and dynamic sandboxes, including loading ELF files into RAM-only sandboxes.
*   **ChibiOS/EX (Explore):** A newer component, potentially focusing on higher-level device abstractions or explorations.
*   **ChibiOS/VFS:** A Virtual File System layer allowing integration with various file systems like FatFS and LittleFS on different storage media (SD Cards, Flash).
*   **ChibiStudio:** A free, ready-to-use Eclipse-based IDE pre-configured with GCC toolchain, debugger (OpenOCD), and demo projects for quick setup and development.

ChibiOS is known for its code quality, extensive documentation, strong debug support (including runtime checks, stack checking, kernel statistics, and a trace buffer), and flexible licensing (GPLv3, Apache 2.0, or Commercial).

## Features

- **Kernel Options:** Offers ChibiOS/RT (full-featured) and ChibiOS/NIL (minimalist) kernels.
- **High Performance:** Designed for low latency and fast context switching.
- **Static Architecture:** Core kernel objects can be statically allocated, enhancing determinism and reducing runtime overhead.
- **Preemptive Scheduler:** Priority-based scheduling with round-robin support.
- **Tickless Mode:** Reduces power consumption during idle periods (RT).
- **Rich IPC Mechanisms:** Semaphores (counting & binary), Mutexes (with priority inheritance), Condition Variables, Event Flags, Synchronous Messages, Mailboxes, Object FIFOs.
- **Memory Management:** Static allocation focus, with optional dynamic memory pools and heap allocation via OSLIB. MPU-based stack protection on supported platforms.
- **Comprehensive HAL:** Extensive set of peripheral drivers with a consistent API across supported MCUs.
- **Timer Management:** System timer, one-shot and periodic virtual timers.
- **Sandboxing (ChibiOS/SB):** MPU-based isolation for Cortex-M3/M4/M7.
- **Filesystem Support:** Virtual File System (VFS) with integrations for FatFS and LittleFS.
- **USB Stack:** Support for USB Device and USB Host.
- **Network Stack:** Integration with lwIP TCP/IP stack.
- **Shell/CLI:** Integrated command-line shell component (XShell, msh).
- **Debugging Support:** Extensive compile-time and runtime checks, assertions, stack overflow detection, kernel statistics, trace buffer.
- **SMP Support:** Experimental Symmetric Multiprocessing support in recent RT versions.
- **Dynamic Loading:** Supports loading ELF applications into sandboxes.
- **Platform Portability:** Supports a wide range of architectures including ARM Cortex-M, RISC-V, AVR, MSP430, PIC32, PowerPC. Includes simulation ports (POSIX, Win32).
- **Licensing:** Dual licensed under GPLv3/Apache 2.0 and Commercial licenses.

## Components

- **Kernel (RT/NIL):** Core RTOS providing scheduling, task management, IPC, and timing services.
- **HAL (Hardware Abstraction Layer):** Provides portable device drivers for MCU peripherals.
- **OSLIB (OS Library):** Extends kernel functionality with dynamic memory allocation, advanced IPC, etc.
- **SB (Sandbox):** MPU-based memory isolation framework for Cortex-M.
- **VFS (Virtual File System):** Abstraction layer for filesystem access.
- **Network:** Integration layer for networking stacks like lwIP.
- **USB Stack:** Provides USB Device and Host functionalities.
- **Shell:** Command-line interface for interaction and debugging.

## Resources

- [Raspberry Pi ChibiOS/RT Port](http://www.stevebate.net/chibios-rpi/GettingStarted.html). Raspberry Pi ChibiOS/RT Port by Steverino. So far, this port has drivers for the Port (GPIO), Serial, GPT (General-Purpose Timer), I2C, SPI and PWM. An example application is in demos/demos/ARM11-BCM2835-GCC. This example creates one thread to blink the onboard LED and another thread to support a very simple command shell. There are also examples showing how to use ChibiOS/RT to access devices likeTMP102 temperature sensor.
- [Getting started](http://www.chibios.org/dokuwiki/doku.php?id=chibios:articles:start). More demo projects.
<!--github-projects-->
- [MotoLink](https://github.com/fpoussin/MotoLink). K-line/Serial/CAN interface and fuel mapper for motorcycles..
- [nisc-examples](https://github.com/delloiaconos/nisc-examples). Examples made for the NeaPolis Innovation Summer Campus.
- [chibios](https://github.com/tickelton/chibios). Mirror of the original ChibiOS [https://chibios.org] SVN repository at http://svn.osdn.net/svnroot/chibios/.
