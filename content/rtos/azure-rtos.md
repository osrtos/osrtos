---
code-url: https://github.com/azure-rtos/threadx
components:
- FileSystem
- Network
- Runtime Analysis
- GUI
- USBHost
- USBDevice
date: 2020-05-27 09:25:57+08:00
draft: false
last-updated: '2021-06-07'
libraries:
- None
licenses:
- Other
platforms:
- ARM Cortex M
site-url: https://azure.microsoft.com/en-us/services/rtos/
slug: azure-rtos
title: Azure RTOS
version: v6.1.7_rel
---

This advanced real-time operating system (RTOS) is designed specifically for deeply embedded applications. Among the multiple benefits it provides are advanced scheduling facilities, message passing, interrupt management, and messaging services. Azure RTOS ThreadX has many advanced features, including picokernel architecture, preemption threshold, event chaining, and a rich set of system services.


<!--more-->

## Azure RTOS ThreadX Core Scheduler
- Minimal 2KB FLASH,1KB RAM footprint
- Fast, sub-microsecond context-switch
- Fully deterministic regardless of number of threads
- Priority-based, fully preemptive-scheduling
- 32 default priority levels, optionally up to 1024 levels
- Cooperative scheduling within priority level (FIFO)
- Preemption-threshold technology
- Optional timer services, including:
- Per-thread optional time-slice
- Optional timeout on all blocking
- APIs Requires on hardware timer interrupt
- Execution profiling
- System-level Trace
- Safety certified to many standards

### Features
- Intuitive and consistent API
- Blocking APIs have optional thread timeout
- Many APIs are directly available from application ISRs
- Core Scheduler:
- No limits on the number of threads
- Dynamic queue creation.
- Dynamic semaphore creation. No limits on the number of semaphores. 32-bit counting semaphores (0 to 4,294,967,295). Supports consumer-producer or resource protection. Optional thread suspension when semaphore unavailable
Optional timeout on all suspension.
- Dynamic mutex creation. No limits on the number of mutexes. Nested resource protection supported. Optional priority inheritance supported. Optional thread suspension when mutex unavailable. Optional timeout on all suspension.
- Dynamic event flag group creation. No limits on the number of event flag groups. Synchronization of one thread or multiple threads. Atomic get and clear supported. Optional multithread suspension on AND/OR set of events. Optional timeout on all suspension
- Dynamic block pool creation. No limits on the number of block pools. No limits on size of fixed-size blocks or size of pool. Fastest possible memory allocation/deal-location. Optional thread suspension on empty pool. Optional timeout on all suspension
- Dynamic byte pool creation. No limits on the number of byte pools. No limits on size of byte pool. Most flexible variable-length memory allocation/deallocation. Allocation size locality supported.
- Dynamic timer creation. No limits on the number of timers. Periodic or one-shot timers supported. Periodic timers may have different initial expiration value. No searching on timer activation or deactivation. All timers driven from one hardware timer interrupt.
