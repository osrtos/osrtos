---
title: RTEMS
slug: rtems
version: "6.1"
code-url: https://gitlab.rtems.org/rtems/rtos/rtems
site-url: https://www.rtems.org/
draft: false
date: "2016-11-29T11:36:57+00:00"
last-updated: "2023-10-14"
star: 585
components:
    - FileSystem
    - TLS/SSL
    - Command Line Interface
libraries:
    - LibBSD
    - lwIP
    - net-legacy
licenses:
    - BSD
platforms:
    - AArch64
    - ARM
    - Blackfin
    - i386
    - lm32
    - m68k
    - MIPS
    - Microblaze
    - Moxie
    - PowerPC
    - RISC-V
    - SPARC
    - SPARC64
    - v850
    - x86_64
---
RTEMS is an open source RTOS that supports open standard application programming interfaces such as POSIX. It is used in space flight, medical, networking and many more embedded devices.

<!--more-->

### Features

- POSIX 1003.1b API including threads.
- VMEbus Industry Trade Association RTEID/ORKID based Classic API (similar to pSOS+).
- TCP/IP including BSD Sockets (provided by one of the 3 associated network libraries).
- GNU Toolset Supports Multiple Language Standards. Multitasking capabilities.
- Homogeneous and heterogeneous multiprocessor systems. Event-driven, priority-based pre-emptive scheduling.
- Optional rate-monotonic scheduling. Intertask communication and synchronization.
- Priority inheritance.
- Responsive interrupt management.
- Dynamic memory allocation.
- High level of user configurability.
- Portable to many target environments.
- High performance port of FreeBSD TCP/IP stack.
- POSIX standard file system semantics.
- GNU debugger. DDD GUI interface to gdb.
- Self-hosted debugging on AArch64, ARM, i386, Microblaze, PowerPC
- Loadable modules on AArch64, ARM, Blackfin, i386, lm32, m68k, Microblaze, MIPS, Moxie, PowerPC, RISC-V, SPARC, v850


### Sample projects and resources

- [RTEMS on the Raspberry Pi](http://alanstechnotes.blogspot.com/2013/03/rtems-on-raspberry-pi.html). RTEMS on the Raspberry Pi Setting up an RTEMS development Environment for the Raspberry PiHow to download and build RTEMSRun an RTEMS program on the Raspberry PiBuilding and running an RTEMS Application
<!--github-projects-->
- [rtems-cmake](https://github.com/robamu-org/rtems-cmake). First version of a RTEMS CMake build support system.
- [ArchMinix](https://github.com/Maxul/ArchMinix). RTEMS C66 BSP Support.
- [LFR_Flight_Software](https://github.com/LaboratoryOfPlasmaPhysics/LFR_Flight_Software). Solar Orbiter's LFR instrument flight software.
- [rtems-ec-cli](https://github.com/maxpoliak/rtems-ec-cli). Command line interface for embedded controllers based on RTEMS RTOS..
- [Strong-APA-Documentation](https://github.com/richidubey/Strong-APA-Documentation). Strong APA Scheduler to be added to RTEMS. https://richidubey.github.io/Strong-APA-Documentation/html/.
- [RTEMS_rpi_testing](https://github.com/asuol/RTEMS_rpi_testing). Test cases and drivers for the Raspberry Pi BSP on RTEMS.
- [rtems-stm32-lwip](https://github.com/robamu/rtems-stm32-lwip). Test repository for the RTEMS lwIP support on the STM32H7 Nucleo-H743ZI board.
- [GSoC-rtems-18](https://github.com/uditagarwal97/GSoC-rtems-18). This repository contains the work done during GSoC'18 with RTEMS under the project of Importing SDIO driver and benchmarking tools.
- [gemini-swg-stack-tracer](https://github.com/rcardenes/gemini-swg-stack-tracer). A little script to extract info out of stack traces.
- [rtems-i2c-max961x-driver](https://github.com/polycone/rtems-i2c-max961x-driver). An implementation of MAX9611 / MAX9612 chips I2C driver for RTEMS OS..
- [RTEMS-5-CMake-CPP11-Starter](https://github.com/roncapat/RTEMS-5-CMake-CPP11-Starter). A demo project targeting RTEMS 5 (SPARC ERC32 BSP), with CMake as build system and C++11 as source language..
