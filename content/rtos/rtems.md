---
title: RTEMS
slug: rtems
version: "4.11"
code-url: https://devel.rtems.org/wiki/Developer/Git
site-url: https://www.rtems.org/
draft: false
date: "2016-11-29T11:36:57+00:00"
last-updated: "2018-02-16"
components:
    - FileSystem
    - Network
    - TLS/SSL
    - Command Line Interface
libraries:
    - None
licenses:
    - GPL
platforms:
    - ARM
    - x86
    - MIPS
    - PowerPC
    - m68k
---
RTEMS is an open source RTOS that supports open standard application programming interfaces such as POSIX. It is used in space flight, medical, networking and many more embedded devices.

<!--more-->

### Features
- POSIX 1003.1b API including threads.
- VMEbus Industry Trade Association RTEID/ORKID based Classic API (similar to pSOS+).
- TCP/IP including BSD Sockets.
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


### Demo Projects
- [RTEMS on the Raspberry Pi](http://alanstechnotes.blogspot.com/2013/03/rtems-on-raspberry-pi.html). RTEMS on the Raspberry Pi Setting up an RTEMS development Environment for the Raspberry PiHow to download and build RTEMSRun an RTEMS program on the Raspberry PiBuilding and running an RTEMS Application
