---
title: MARK3
slug: mark3
version: ""
code-url: https://sourceforge.net/projects/mark3/
site-url: http://www.mark3os.com/index.html
draft: false
date: "2016-11-29 11:36:57"
last-updated: "2015-03-08"
components:
    - None
libraries:
    - None
licenses:
    - BSD
platforms:
    - AVR
---
Mark3 is a sophisticated, modern RTOS and application development platform, targeted towards a growing list of today's most compelling embedded devices.

<!--more-->

### Features

- Deterministic, multiple-priority preemptive scheduler, with round-robin scheduling within each priority
- Binary and counting semaphores
- Mutex objects supporting both recursion and priority inheritence
- Event flags for efficient synchronization of multiple threads
- Dynamic message queues for IPC
- Device driver (open/close/read/write/ioctl) infrastructure baked into the kernel
- Tickless software-based timers for maximum CPU, interrupt, and power efficienccy
- High accuracy code-profiling timers
- Extendable debug infrastructure for runtime debugging and critical error handling
