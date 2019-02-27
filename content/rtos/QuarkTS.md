---
title: "QuarkTS"
date: 2019-02-27T16:49:25+08:00
slug: quark-ts
version: 4.6.6(j)
site-url: https://github.com/kmilo17pet/QuarkTS/wiki
code-url: https://github.com/kmilo17pet/QuarkTS
last-updated: 2019-02-27
licenses: 
- LGPL
platforms:
- ARM
- AVR
- PIC
- ColdFire
- MSP430
- 8051
- MIPS
- HCS12
- x86
components:
- None
libraries:
- None
draft: false
---

QuarkTS is a simple non-Preemtive Real-Time OS with a quasi-static scheduler for embedded multi-tasking applications. 

<!--more-->

### Features
- QuarkTS uses a cooperative Round-Robin scheme with a linked chain approach, and a queue to provide true FIFO priority-scheduling. 
- QuarkTS uses a Time-Triggered Architecture (TTA), in which the tasks are triggered by comparing the corresponding task-time with a monotonic real-time clock. 


