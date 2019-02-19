---
title: "NuttX"
date: 2016-11-29T11:36:57+00:00
slug: "nuttx"
version: "7.25"
site-url: "http://nuttx.org/"
code-url: "https://sourceforge.net/projects/nuttx/"
last-updated: "2018-06-11"
licenses: 
- BSD
platforms:
- ARM
- AVR
- 8051
- PIC
- x86
- MIPS
- Xtensa
- RISC-V
- Freescale HCS12
- Zilog
components:
- FileSystem
- Network
- 6LoWPAN
- Command Line Interface
- USBHost
- USBDevice
- GUI
libraries:
- LittlevGL
draft: false
---
NuttX is a real-time operating system (RTOS) with an emphasis on standards compliance and small footprint. Scalable from 8-bit to 32-bit microcontroller environments, the primary governing standards in NuttX are Posix and ANSI standards.

<!--more-->

### Features
- Standards Compliant.
- Core Task Management.
- Modular, micro-kernel.
- Fully pre-emptible.
- Naturally scalable.
- Highly configurable.
- Easily extensible to new processor architectures, SoC architecture, or board architectures. See Porting Guide.
- FIFO and round-robin scheduling.
- Realtime, deterministic, with support for priority inheritance.
- POSIX/ANSI-like task controls, named message queues, counting semaphores, clocks/timers, signals, pthreads, environment variables, filesystem.
- VxWorks-like task management and watchdog timers.
- BSD socket interface.
- Extensions to manage pre-emption.
- Optional tasks with address environments (Processes).
- Inheritable


### Demo Projects
- [PX4](http://pixhawk.org/choice). PX4 is an independent, open-source, open-hardware project aiming at providing a high-end autopilot to the academic, hobby and industrial communities (BSD licensed) at low costs and high availability.
- [HOWTO: Installing NuttX on the STM32F4 Discovery board (using Debian Linux)](http://fob.po8.org/node/613). Installed the NuttX RTOS on a new STM32F4 Discovery board.
- [Running NuttX on a less than U$2.00 board](https://acassis.wordpress.com/2016/06/12/running-nuttx-on-a-less-than-u2-00-board/). Running NuttX on a STM32 Minimum System Development Board.
- [CC3200 development on Linux with NuttX](http://www.mcfish.org/blog/6-cc3200-linux-nuttx). This article shows how to compile and install NuttX real-time OS to CC3200 launchpad using Fedora (24) Linux.
