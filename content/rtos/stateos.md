---
code-url: https://github.com/stateos/StateOS
components:
- None
date: 2016-11-29 11:36:58
draft: false
last-updated: '2018-11-20'
libraries:
- None
licenses:
- GPL v3
platforms:
- ARM
site-url: https://github.com/stateos/StateOS
slug: stateos
title: StateOS
version: v6.4
---
Free, extremely simple and amazingly tiny real-time operating system (RTOS) designed for deeply embedded applications. Target: ARM Cortex-M family. It was inspired by the concept of a state machine.

<!--more-->

### Features
- kernel works in preemptive or cooperative mode
- kernel can operate in tick-less mode (32-bit timer required)
- signals (auto clearing, protected)
- events
- flags (one, all, accept, ignore)
- barriers
- semaphores (binary, limited, counting)
- mutexes (recursive and priority inheritance)
- fast mutexes (non-recursive and non-priority-inheritance)
- condition variables
- memory pools
- message queues
- mailbox queues
- timers (one-shot, periodic)
- cmsis-rtos api
- c++ wrapper
- all documentation is contained within the source files


