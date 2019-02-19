---
title: "scmRTOS"
date: 2016-11-29T11:36:58+00:00
slug: "scmrtos"
version: "v5.1.0"
site-url: "https://github.com/scmrtos/scmrtos"
code-url: "https://github.com/scmrtos/scmrtos"
last-updated: "2016-04-19"
licenses: 
- MIT
platforms:
- MSP430
- AVR
components:
- None
libraries:
- None
draft: false
---
scmRTOS is tiny Real-Time Preemptive Operating System intended for use with Single-Chip Microcontrollers. scmRTOS is capable to run on tiny uCs with as small amount of RAM as 512 bytes. The RTOS is written on C++ and supports various platforms.

<!--more-->

### Features
- Preemptive multitasking;
- Up to 31 user processes (tasks);
- Fast interprocess program control flow transfer:
- Low Resource Requirements:
- Supports separate return stack (required for IAR EW AVR);
- Kernel extensions
- Debug features
- Optional software switch on separate ISR stack on some platforms;
- Support of various target hardware features such as hardware shifters etc., for more efficiency.


