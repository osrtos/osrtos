---
title: QuarkTS
slug: quark-ts
version: 7.3.3
code-url: https://github.com/kmilo17pet/QuarkTS
site-url: https://github.com/kmilo17pet/QuarkTS/wiki
draft: false
date: "2019-02-27 08:49:25"
last-updated: "2023-05-12"
components:
    - None
libraries:
    - None
licenses:
    - LGPL
platforms:
    - ARM
    - AVR
    - PIC
    - ColdFire
    - MSP430
    - "8051"
    - MIPS
    - HCS12
    - x86
---
QuarkTS is a simple non-Preemtive Real-Time OS with a quasi-static scheduler for embedded multi-tasking applications. 

<!--more-->

### Features
- QuarkTS uses a cooperative Round-Robin scheme with a linked chain approach, and a queue to provide true FIFO priority-scheduling. 
- QuarkTS uses a Time-Triggered Architecture (TTA), in which the tasks are triggered by comparing the corresponding task-time with a monotonic real-time clock. 


