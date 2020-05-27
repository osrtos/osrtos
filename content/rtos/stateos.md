---
code-url: https://github.com/stateos/StateOS
components:
- None
date: 2016-11-29 11:36:58
draft: false
last-updated: '2020-05-13'
libraries:
- None
licenses:
- MIT
platforms:
- ARM Cortex-M, STM8
site-url: https://github.com/stateos/StateOS
slug: stateos
title: StateOS
version: v6.6
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

