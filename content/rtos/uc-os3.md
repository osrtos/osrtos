---
title: "uC/OS-III"
date: 2020-05-04T10:22:58+08:00
slug: uc-os-iii
version: v3.08.00 
site-url: https://doc.micrium.com/display/ucos/
code-url: https://github.com/SiliconLabs/uC-OS3
last-updated: 2020-02-29
licenses: 
- Apache License 2.0
platforms:
- ARM
- ColdFire
- AVR
- AVR32
- 80X86
- PowerPC
- RISC-V
- MSP430
- PIC32
components:
- FileSystem
- Network
- TLS/SSL
- USBHost
- USBDevice
- Modbus
- GUI
- CAN
libraries:
- None
draft: false
---

µC/OS-III is a highly portable, ROMable, scalable, preemptive, real-time, deterministic, multitasking kernel for microprocessors, microcontrollers and DSPs.


<!--more-->

### Features
- Preemptive multitasking real-time kernel with optional round robin scheduling
- Delivered with complete, clean, consistent source code with in-depth documentation.
- Highly scalable: Unlimited number of tasks, priorities and kernel objects
- Resource-efficient: 6K to 24K bytes code space, 1K+ bytes data space)
- Very low interrupt disable time
- Extensive performance measurement metrics (configurable)
- Certifiable for safety-critical applications