---
title: HuskEOS
slug: huskeos
version: dev
code-url: https://github.com/gscultho/HuskEOS
site-url: https://github.com/gscultho/HuskEOS
date: "2023-08-20 11:36:57"
last-updated: "2024-09-11"
star: 2
components:
    - None
licenses:
    - MIT license
platforms:
    - ARM
---
HuskEOS is a real-time operating system (RTOS) designed for embedded systems. It offers a priority-based preemptive scheduler and boasts impressive performance metrics, such as achieving 50,000 context switches per second on a Cortex-M4 configured at 16MHz.

<!--more-->

### Features

- **Priority-based Preemptive Scheduler:** Efficiently schedules tasks based on their priority.
- **Performance:** Achieves 50,000 context switches per second on Cortex-M4 at 16MHz.
- **Memory Management:** Memory footprint can be as low as 550 bytes. All memory is statically allocated, eliminating the need for a heap.
- **Hardware Agnostic:** The entire OS is hardware-independent except for an internal OS/CPU interface layer, allowing for portability across different platforms.
- **Consistent API:** Public modules have consistent API structures and naming conventions.
- **Stack Overflow Detection:** Supports stack overflow detection for each task with configurable fault handlers.
- **Debugging Support:** Collects runtime data for debugging, which can be turned off for reduced overhead.

### Components

- **Scheduler:** Handles task scheduling and state management.
- **Flags:** Provides event flag objects for task synchronization.
- **Mailbox:** Allows tasks to pass single pieces of data between them.
- **Memory:** Emulates dynamic memory allocation with block allocation and overflow/underflow detection.
- **Semaphore:** Designed for counting and signaling. For mutual exclusion, Mutex is used.
- **Mutex:** Mutual exclusion semaphore with priority inheritance to prevent priority inversion.
- **Queue:** Offers fully configurable FIFO message queues.

<!--github-projects-->
