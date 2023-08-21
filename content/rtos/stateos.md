---
title: StateOS
slug: stateos
version: v6.9
code-url: https://github.com/stateos/StateOS
site-url: https://github.com/stateos/StateOS
draft: false
date: "2016-11-29 11:36:58"
last-updated: "2023-03-18"
components:
    - None
libraries:
    - None
licenses:
    - MIT
platforms:
    - ARM Cortex-M, STM8
---
Free, extremely simple and amazingly tiny real-time operating system (RTOS) designed for deeply embedded applications. Target: ARM Cortex-M, STM8. It was inspired by the concept of a state machine.

<!--more-->

### Features

- kernel can operate in preemptive or cooperative mode
- kernel can operate with 16, 32 or 64-bit timer counter
- kernel can operate in tick-less mode
- spin locks
- once flags
- events
- signals with protection mask
- flags (any, all, protect, ignore)
- barriers
- semaphores (binary, limited, counting)
- mutexes with configurable type, protocol and robustness
- fast mutexes (error checking)
- condition variables
- memory pools
- stream buffers
- message buffers
- mailbox queues
- event queues
- job queues
- timers (one-shot, periodic)
- cmsis-rtos api
- cmsis-rtos2 api
- nasa-osal support
- c++ wrapper
- all documentation is contained within the source files
- examples and templates are in separate repositories

### Resources
<!--github-projects-->
- [StateOS_cpp11](https://github.com/stateos/StateOS_cpp11). RTOS designed for microcrocontrollers using std::thread. TEMPLATE..