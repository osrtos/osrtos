---
title: Tock
slug: tock
version: release-2.2
code-url: https://github.com/tock/tock
site-url: https://github.com/tock/tock
date: "2019-02-12 05:45:10"
last-updated: "2025-04-23"
star: 5751
components:
    - scheduler
    - task-management
    - inter-task-communication
    - memory-management
    - timer-management
    - logging
    - dynamic-loading
    - filesystem
licenses:
    - Apache-2.0
    - MIT
platforms:
    - arm-cortex-m
    - risc-v
---
Tock is an embedded operating system designed for running multiple concurrent, mutually distrustful applications on ARM Cortex-M and RISC-V microcontrollers. Its core design prioritizes safety and reliability, utilizing Rust's compile-time guarantees to protect the kernel and drivers, and hardware Memory Protection Units (MPUs) to isolate applications. Tock introduces a unique architecture dividing components into kernel-space "capsules" (Rust-based, cooperatively scheduled, minimal overhead) and user-space "processes" (MPU-isolated, preemptively scheduled, can be written in any language and loaded dynamically). This approach enables robust, secure applications on resource-constrained devices like wearables and IoT nodes.

<!--more-->

## Architecture and Core Concepts

Tock's architecture aims to provide strong isolation guarantees suitable for embedded systems where resources are scarce, and reliability is paramount. It achieves this through a combination of language features and hardware protection:

1.  **Rust-Based Kernel and Capsules:** The core kernel, device drivers, and virtualization layers ("capsules") are written in Rust. Rust's ownership and borrowing system provides compile-time memory safety and type safety, preventing common errors like null pointer dereferences, buffer overflows, and data races within the kernel space. This allows fine-grained isolation between kernel components with virtually no runtime overhead. Capsules run in privileged mode but are cooperatively scheduled within a single-threaded event loop. While safe in terms of memory, a misbehaving capsule could potentially block the system.

2.  **MPU-Protected Processes:** Applications run as user-space "processes". Each process is isolated from the kernel and other processes using the hardware Memory Protection Unit (MPU). This allows processes to be written in any language (commonly C/C++) and loaded dynamically at runtime without recompiling the kernel. Processes are preemptively scheduled, ensuring that one process cannot monopolize the CPU indefinitely.

3.  **Grants Mechanism:** To allow safe sharing of memory between untrusted user-space processes and trusted kernel capsules (e.g., for driver buffers or asynchronous operation context), Tock uses a "grant" mechanism. Processes allocate a specific memory region that the kernel can manage on their behalf. Capsules can safely allocate typed data within this grant region without violating memory safety, even if the process crashes or terminates.

4.  **Asynchronous Event-Driven Model:** Tock employs an asynchronous, event-driven model based on callbacks (upcalls). Processes register callbacks for driver events (e.g., timer expiry, data reception) using the `subscribe` system call and then yield execution using the `yield` system call. The kernel wakes the process only when a subscribed event occurs, enabling efficient low-power operation.

## System Calls

Processes interact with the kernel via a minimal set of system calls:
*   `subscribe`: Register a callback function for a driver event.
*   `command`: Issue a synchronous command to a driver.
*   `allow`: Share a read-only or read-write buffer from process memory with a driver.
*   `memop`: Perform operations related to process memory management (e.g., requesting more memory).
*   `yield`: Relinquish control to the kernel, waiting for the next pending callback.

## Target Applications

Tock is well-suited for applications requiring high security and reliability on low-power microcontrollers, such as:
*   Secure IoT devices
*   Wearable technology
*   Wireless sensor nodes
*   Systems requiring secure third-party application support

## Features

- **Memory Safety:** Kernel and drivers written in Rust for compile-time memory safety.
- **Hardware Isolation:** Uses Memory Protection Units (MPU) to isolate processes from the kernel and each other.
- **Dual Component Model:**
    - **Capsules:** Kernel-space, Rust-based, type-safe, cooperative scheduling, fine-grained isolation.
    - **Processes:** User-space, MPU-isolated, preemptive scheduling, language-agnostic, dynamic loading.
- **Concurrency:** Supports multiple concurrent applications (processes) and kernel tasks (capsules).
- **Grant Mechanism:** Safe dynamic memory allocation for kernel capsules from process memory.
- **Asynchronous Operations:** Callback-based system calls (`subscribe`/`yield`) for efficient, event-driven execution.
- **Resource Constrained:** Designed specifically for MCUs like ARM Cortex-M and RISC-V with limited memory.
- **Modularity:** Clear separation between chip support, board support, kernel core, and capsules.
- **Minimal System Call Interface:** Reduces attack surface and complexity.

## Components

- **Scheduler:** Manages both cooperative scheduling for capsules and preemptive scheduling for processes.
- **Task Management:** Handles creation, scheduling, and lifecycle of processes and capsules.
- **Memory Management:** Enforces MPU regions for processes, manages kernel memory, and implements the Grant mechanism.
- **Inter-task Communication:** Primarily via system calls (`command`, `subscribe`, `allow`) and the Grant mechanism. Kernel includes an IPC service.
- **Timer Management:** Provides virtualized timers and alarms accessible by processes and capsules.
- **Hardware Abstraction Layer (HIL):** Defines traits for abstracting hardware peripherals (GPIO, UART, SPI, Timers, etc.).
- **Dynamic Loading:** Supports loading new processes at runtime without kernel modification.
- **Logging:** Provides debugging macros (`debug!`) for kernel-level logging.
- **Storage Management:** Mechanisms for managing access permissions to non-volatile storage areas.

### Resources
<!--github-projects-->
- [OpenSK](https://github.com/google/OpenSK). OpenSK is an open-source implementation for security keys written in Rust that supports both FIDO U2F and FIDO2 standards..
- [libtock-c](https://github.com/tock/libtock-c). Userland apps for Tock written in C and C++.
- [tockloader](https://github.com/tock/tockloader). Tool for programming Tock onto hardware boards..
- [tock-stm32](https://github.com/tock/tock-stm32). Ports of Tock for STM32 chips and discovery boards.
- [tock-bootloader](https://github.com/tock/tock-bootloader). Software bootloader for boards running Tock..
- [hail](https://github.com/lab11/hail). An IoT development module that supports the Tock operating system..
- [pinetime-tock](https://github.com/JayKickliter/pinetime-tock). An out-of-tree port of Tock to the PineTime smart watch.
- [tock-docker](https://github.com/jehoffmann/tock-docker). TockOS build.
- [tock-test-harness](https://github.com/goodoomoodoo/tock-test-harness). Tock OS test runner.
- [tock-docker](https://github.com/george-hopkins/tock-docker). Tock OS Docker Image.
