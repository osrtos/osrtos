---
title: Eclipse ThreadX
slug: threadx-rtos
version: v6.4.1_rel
code-url: https://github.com/eclipse-threadx/threadx
site-url: hhttps://threadx.io/ttps://azure.microsoft.com/en-us/services/rtos/
date: 2020-05-27 09:25:57+08:00
last-updated: "2024-03-26"
star: 2989
components:
    - FileSystem
    - Network
    - Runtime Analysis
    - GUI
    - USBHost
    - USBDevice
libraries:
    - None
licenses:
    - MIT
platforms:
    - Arm Cortex-A7/A8/A9/A1x/A3x/A6x/A5x/A7x
    - Arm Cortex-R4/R5/R7
    - Arm Cortex-M0+/M3/M4/M7/M23/M33/M55/M85
    - RISC-V
    - Xtensa
    - RXv1/v2/v3
---
This advanced real-time operating system (RTOS) is designed specifically for deeply embedded applications. Among the multiple benefits it provides are advanced scheduling facilities, message passing, interrupt management, and messaging services. Eclipse ThreadX has many advanced features, including picokernel architecture, preemption threshold, event chaining, and a rich set of system services.

<!--more-->

### Eclipse ThreadX Core Scheduler

- Minimal 2KB FLASH, 1KB RAM footprint
- Fast, sub-microsecond context-switch
- Fully deterministic regardless of number of threads
- Priority-based, fully preemptive-scheduling
- 32 default priority levels, optionally up to 1024 levels
- Cooperative scheduling within priority level (FIFO)
- Preemption-threshold technology
- Optional timer services, including:
- Per-thread optional time-slice
- Optional timeout on all blocking
- APIs Requires on hardware timer interrupt
- Execution profiling
- System-level Trace
- Safety certified to many standards

### Features

- Intuitive and consistent API
- Blocking APIs have optional thread timeout
- Many APIs are directly available from application ISRs
- Core Scheduler:
- No limits on the number of threads
- Dynamic queue creation.
- Dynamic semaphore creation. No limits on the number of semaphores. 32-bit counting semaphores (0 to 4,294,967,295). Supports consumer-producer or resource protection. Optional thread suspension when semaphore unavailable
Optional timeout on all suspension.
- Dynamic mutex creation. No limits on the number of mutexes. Nested resource protection supported. Optional priority inheritance supported. Optional thread suspension when mutex unavailable. Optional timeout on all suspension.
- Dynamic event flag group creation. No limits on the number of event flag groups. Synchronization of one thread or multiple threads. Atomic get and clear supported. Optional multithread suspension on AND/OR set of events. Optional timeout on all suspension
- Dynamic block pool creation. No limits on the number of block pools. No limits on size of fixed-size blocks or size of pool. Fastest possible memory allocation/deal-location. Optional thread suspension on empty pool. Optional timeout on all suspension
- Dynamic byte pool creation. No limits on the number of byte pools. No limits on size of byte pool. Most flexible variable-length memory allocation/deallocation. Allocation size locality supported.
- Dynamic timer creation. No limits on the number of timers. Periodic or one-shot timers supported. Periodic timers may have different initial expiration value. No searching on timer activation or deactivation. All timers driven from one hardware timer interrupt.

### Sample projects and resources
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
