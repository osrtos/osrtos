---
title: RTIC
slug: rtic
version: v2.0.0
code-url: https://github.com/rtic-rs/rtic
site-url: https://rtic.rs/
draft: false
date: "2016-11-29 11:36:58"
last-updated: "2023-07-01"
components: []
libraries: []
licenses:
    - Apache License, Version 2.0
    - MIT license
platforms:
    - ARM
---


RIOT, the hardware accelerated Rust RTOS. A concurrency framework for building real-time systems.

<!--more-->

### Features
- Tasks as the unit of concurrency 1. Tasks can be event triggered (fired in response to asynchronous stimuli) or spawned by the application on demand.
- Message passing between tasks. Specifically, messages can be passed to software tasks at spawn time.
- A timer queue 2. Software tasks can be scheduled to run at some time in the future. This feature can be used to implement periodic tasks.
- Support for prioritization of tasks and, thus, preemptive multitasking.
- Efficient and data race free memory sharing through fine-grained priority based critical sections 1.
- Deadlock free execution guaranteed at compile time. This is a stronger guarantee than what's provided by the standard Mutex abstraction.
- Minimal scheduling overhead. The task scheduler has minimal software footprint; the hardware does the bulk of the scheduling.
- Highly efficient memory usage: All the tasks share a single call stack and there's no hard dependency on a dynamic memory allocator.
- All Cortex-M devices are fully supported.
- This task model is amenable to known WCET (Worst Case Execution Time) analysis and scheduling analysis techniques.


### Demo Projects
- [STM32WL Lightswitch Demo](https://github.com/newAM/stm32wl-lightswitch-demo). This is a demo project for the stm32wl-hal.
